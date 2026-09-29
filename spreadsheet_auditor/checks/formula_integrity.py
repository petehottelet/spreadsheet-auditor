"""Formula-integrity checks: live errors, broken refs, drift, cycles."""

from __future__ import annotations

from collections import defaultdict

from ..finding import Finding
from ..formula_parser import normalize_formula
from ..locations import anchor
from .base import Check, CheckContext, register

MAX_DEPENDENTS_SHOWN = 8


def _position(location: str) -> tuple:
    """Sort key in sheet order: row, then column (``D11`` before ``D100``)."""
    spot = anchor(location)
    return spot if spot is not None else (location, 0, 0)
# Functions that can swallow or branch around an error literal, so a formula
# containing one does not necessarily evaluate to it.
ERROR_HANDLERS = {
    "IFERROR",
    "IFNA",
    "ISERROR",
    "ISERR",
    "ISNA",
    "ISREF",
    "ERROR.TYPE",
    "IF",
    "IFS",
    "CHOOSE",
    "SWITCH",
    "AGGREGATE",
}


def _extents(formula_wb) -> dict[str, tuple[int, int]] | None:
    if formula_wb is None:
        return None
    return {ws.title: (int(ws.max_row or 1), int(ws.max_column or 1)) for ws in formula_wb.worksheets}


@register
class LiveErrorCheck(Check):
    name = "live_errors"
    description = (
        "Reports cells whose cached value is a live spreadsheet error (#REF!, #VALUE!, ...), "
        "once per root cause with the cells the error propagates to."
    )
    rule_ids = ("LIVE_ERROR",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..dependency_graph import build_dependency_graph
        from ..formula_parser import parse_formula
        from ..workbook_inventory import scan_live_errors

        # A formula that carries an error literal outside any error-handling
        # function evaluates to that error whatever the inputs, so it is
        # reported the same way with or without cached values.
        errors: dict[str, str] = {}
        static: set[str] = set()
        for cell in ctx.formulas:
            if cell["sheet"] not in ctx.allowed_sheet_names:
                continue
            parsed = parse_formula(
                cell["formula"], names=ctx.names, origin=(cell["sheet"], cell["row"], cell["col"])
            )
            if parsed.error_literals and not parsed.functions & ERROR_HANDLERS:
                errors[cell["location"]] = parsed.error_literals[0]
                static.add(cell["location"])
        for loc, error_value in scan_live_errors(ctx.formula_wb, ctx.value_wb):
            if loc.split("!", 1)[0] in ctx.allowed_sheet_names:
                errors.setdefault(loc, error_value)
        if not errors:
            return []

        graph = build_dependency_graph(
            ctx.formulas, names=ctx.names, extents=_extents(ctx.formula_wb), budget=ctx.budget
        )
        reverse: dict[str, set[str]] = defaultdict(set)
        for source, deps in graph.items():
            for dep in deps:
                reverse[dep].add(source)

        # A root is an error cell with no erroring precedent: a literal error
        # value, or the formula where the error is born.
        roots = [loc for loc in errors if not any(dep in errors for dep in graph.get(loc, ()))]
        # The root's formula is where the error is born; the report shows it so
        # the cause can be read without opening the workbook.
        cell_at = {cell["location"]: cell for cell in ctx.formulas}
        covered: set[str] = set()
        propagated_from: dict[str, set[str]] = {}
        for root in roots:
            seen = {root}
            stack = [root]
            while stack:
                node = stack.pop()
                for dependent in reverse.get(node, ()):
                    if dependent in errors and dependent not in seen:
                        seen.add(dependent)
                        stack.append(dependent)
            covered.update(seen)
            propagated_from[root] = seen - {root}

        # Errors inside a cycle have no root (a lookup whose table spans its
        # own column: every row reads the others); each is its own source.
        for loc in set(errors) - covered:
            propagated_from[loc] = set()

        # A formula filled down a column that errors in every row is one
        # mistake, not one per row: sources that share a sheet, an error value
        # and a relative formula (or are the same error typed as a constant)
        # are one finding, led by their top-left cell.
        groups: dict[tuple, list[str]] = defaultdict(list)
        for root in propagated_from:
            cell = cell_at.get(root)
            shape = normalize_formula(cell["formula"], cell["row"], cell["col"]) if cell else "constant"
            groups[(root.rsplit("!", 1)[0], errors[root], shape)].append(root)
        findings: list[Finding] = []
        for (_sheet, error_value, shape), members in groups.items():
            members.sort(key=_position)
            lead = members[0]
            dependents = set().union(*(propagated_from[root] for root in members)) - set(members)
            findings.append(
                self._finding(
                    lead,
                    error_value,
                    sorted(dependents, key=_position),
                    lead in static,
                    cell_at[lead]["formula"] if lead in cell_at else None,
                    members,
                    shape == "constant",
                )
            )
        return findings

    @staticmethod
    def _finding(
        loc: str,
        error_value: str,
        propagated: list[str],
        static: bool = False,
        formula: str | None = None,
        members: list[str] | None = None,
        constant: bool = False,
    ) -> Finding:
        if static:
            evidence = [f"Formula contains {error_value}, so the cell evaluates to that error whatever its inputs."]
        else:
            evidence = [f"Cell contains {error_value}."]
        if members and len(members) > 1:
            others = members[1:]
            shown = ", ".join(others[:MAX_DEPENDENTS_SHOWN])
            if len(others) > MAX_DEPENDENTS_SHOWN:
                shown += f", and {len(others) - MAX_DEPENDENTS_SHOWN} more"
            what = f"{error_value} is typed as a value" if constant else f"the same relative formula evaluates to {error_value}"
            evidence.append(f"{what[0].upper()}{what[1:]} in {len(members)} cells on this sheet; the others are {shown}.")
        if propagated:
            shown = ", ".join(propagated[:MAX_DEPENDENTS_SHOWN])
            if len(propagated) > MAX_DEPENDENTS_SHOWN:
                shown += f", and {len(propagated) - MAX_DEPENDENTS_SHOWN} more"
            evidence.append(
                f"The error propagates to {len(propagated)} dependent cell(s): {shown}. Fixing the source clears them."
            )
        return Finding(
            rule_id="LIVE_ERROR",
            severity="Critical",
            error_confidence="Defect",
            detection_mode="DET",
            location=loc,
            title="Cell contains live spreadsheet error",
            formula=formula,
            evidence=evidence,
            suggested_fix="Trace the formula precedent chain and resolve the underlying spreadsheet error.",
        )


@register
class ReferenceIntegrityCheck(Check):
    name = "references"
    description = "Reports broken references, blank precedents, external workbook links, IFERROR masks."
    rule_ids = ("BROKEN_REFERENCE", "BLANK_PRECEDENT", "IFERROR_MASK")
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..audit import detect_reference_issues

        return detect_reference_issues(
            ctx.formula_wb,
            ctx.value_wb,
            ctx.formulas,
            ctx.unsupported_features,
            names=ctx.names,
            budget=ctx.budget,
        )


@register
class FormulaDriftCheck(Check):
    name = "formula_drift"
    description = "Detects rows/columns where one formula breaks the dominant relative pattern."
    rule_ids = ("FORMULA_DRIFT",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..formula_drift import detect_formula_drift

        return detect_formula_drift(ctx.formulas, budget=ctx.budget, names=ctx.names, formula_wb=ctx.formula_wb)


@register
class HardcodeBreakCheck(Check):
    name = "hardcode_breaks"
    description = "Flags constants that interrupt a run of formulas sharing one relative pattern."
    rule_ids = ("HARDCODE_IN_FORMULA_BLOCK",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..formula_drift import detect_hardcode_breaks

        if not ctx.grid_scan_allowed:
            return []
        return detect_hardcode_breaks(
            ctx.formula_wb, ctx.allowed_sheet_names, budget=ctx.budget, names=ctx.names
        )


@register
class CircularReferenceCheck(Check):
    name = "circular_references"
    description = "Reports dependency cycles between formula cells, including a cell that references itself."
    rule_ids = ("CIRCULAR_REFERENCE",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..audit import detect_cycles

        return detect_cycles(
            ctx.formulas, names=ctx.names, extents=_extents(ctx.formula_wb), budget=ctx.budget
        )
