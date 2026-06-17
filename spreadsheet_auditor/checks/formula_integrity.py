"""Formula-integrity checks: live errors, broken refs, drift, cycles."""

from __future__ import annotations

from ..finding import Finding
from .base import Check, CheckContext, register


@register
class LiveErrorCheck(Check):
    name = "live_errors"
    description = "Reports cells whose cached value is a live spreadsheet error (#REF!, #VALUE!, ...)."
    rule_ids = ("LIVE_ERROR",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..workbook_inventory import scan_live_errors

        findings: list[Finding] = []
        for loc, error_value in scan_live_errors(ctx.formula_wb, ctx.value_wb):
            sheet = loc.split("!", 1)[0]
            if sheet not in ctx.allowed_sheet_names:
                continue
            findings.append(
                Finding(
                    rule_id="LIVE_ERROR",
                    severity="Critical",
                    error_confidence="Defect",
                    detection_mode="DET",
                    location=loc,
                    title="Cell contains live spreadsheet error",
                    evidence=[f"Cell contains {error_value}."],
                    suggested_fix="Trace the formula precedent chain and resolve the underlying spreadsheet error.",
                )
            )
        return findings


@register
class ReferenceIntegrityCheck(Check):
    name = "references"
    description = "Reports broken references, blank precedents, external workbook links, IFERROR masks."
    rule_ids = ("BROKEN_REFERENCE", "BLANK_PRECEDENT", "IFERROR_MASK")
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..audit import detect_reference_issues

        return detect_reference_issues(
            ctx.formula_wb, ctx.value_wb, ctx.formulas, ctx.unsupported_features
        )


@register
class FormulaDriftCheck(Check):
    name = "formula_drift"
    description = "Detects rows/columns where one formula breaks the dominant relative pattern."
    rule_ids = ("FORMULA_DRIFT",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..formula_drift import detect_formula_drift

        return detect_formula_drift(ctx.formulas)


@register
class HardcodeBreakCheck(Check):
    name = "hardcode_breaks"
    description = "Flags numeric literals that sit inside otherwise-formula rows or columns."
    rule_ids = ("HARDCODE_IN_FORMULA_BLOCK",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..formula_drift import detect_hardcode_breaks

        return detect_hardcode_breaks(ctx.formula_wb, ctx.allowed_sheet_names)


@register
class CircularReferenceCheck(Check):
    name = "circular_references"
    description = "Reports dependency cycles between formula cells."
    rule_ids = ("CIRCULAR_REFERENCE",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..audit import detect_cycles

        expansion_limit = int((ctx.config.get("limits") or {}).get("max_range_expansion_cells", 500))
        return detect_cycles(ctx.formulas, expansion_limit=expansion_limit)
