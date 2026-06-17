"""Reconciliation checks: totals and cross-foot agreement."""

from __future__ import annotations

from ..finding import Finding
from .base import Check, CheckContext, register


@register
class TotalMismatchCheck(Check):
    name = "total_mismatches"
    description = "Compares a total formula against the sum of its components and reports disagreements."
    rule_ids = ("TOTAL_MISMATCH",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..reconcile import detect_total_mismatches

        return detect_total_mismatches(ctx.formula_wb, ctx.value_wb, ctx.formulas)


@register
class CrossFootCheck(Check):
    name = "cross_foot"
    description = "Detects rectangular tables where row totals and column totals disagree at the corner."
    rule_ids = ("CROSS_FOOT_FAILURE",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..reconcile import detect_cross_foot_failures

        return detect_cross_foot_failures(ctx.formula_wb, ctx.value_wb, ctx.allowed_sheet_names)
