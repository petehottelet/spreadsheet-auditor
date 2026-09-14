"""Formula-integrity checks: live errors, broken refs, drift, cycles."""

from __future__ import annotations

from collections import defaultdict

from ..finding import Finding
from .base import Check, CheckContext, register

MAX_DEPENDENTS_SHOWN = 8
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
        covered: set[str] = set()
        findings: list[Finding] = []
        for root in sorted(roots):
            propagated: list[str] = []
            seen = {root}
            stack = [root]
            while stack:
                node = stack.pop()
                for dependent in reverse.get(node, ()):
                    if dependent in errors and dependent not in seen:
                        seen.add(dependent)
                        propagated.append(dependent)
                        stack.append(dependent)
            covered.add(root)
            covered.update(propagated)
            findings.append(self._finding(root, errors[root], sorted(propagated), root in static))
        for loc in sorted(set(errors) - covered):  # error cycles with no root
            findings.append(self._finding(loc, errors[loc], [], loc in static))
        return findings

    @staticmethod
    def _finding(loc: str, error_value: str, propagated: list[str], static: bool = False) -> Finding:
        if static:
            evidence = [f"Formula contains {error_value}, so the cell evaluates to that error whatever its inputs."]
        else:
            evidence = [f"Cell contains {error_value}."]
        if propagated:
            shown = ", ".join(propagated[:MAX_DEPENDENTS_SHOWN])
            if len(propagated) > MAX_DEPENDENTS_SHOWN:
                shown += ", ..."
            evidence.append(
                f"The error propagates to {len(propagated)} dependent cell(s): {shown}. Fixing this cell clears them."
            )
        return Finding(
            rule_id="LIVE_ERROR",
            severity="Critical",
            error_confidence="Defect",
            detection_mode="DET",
            location=loc,
            title="Cell contains live spreadsheet error",
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

        return detect_formula_drift(ctx.formulas, budget=ctx.budget, names=ctx.names)


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
