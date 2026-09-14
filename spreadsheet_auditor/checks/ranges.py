"""Range-shape checks: off-by-one, subtotal double counts, hidden inputs, length mismatches, literals, volatile functions."""

from __future__ import annotations

from ..finding import Finding
from .base import Check, CheckContext, register


@register
class RangeIssueCheck(Check):
    name = "range_issues"
    description = (
        "Detects totals that stop short of an adjacent input, ranges that sum a subtotal "
        "together with its components, and hidden rows/columns/sheets that feed visible formulas."
    )
    rule_ids = ("RANGE_EXCLUSION", "RANGE_INCLUDES_SUBTOTAL", "HIDDEN_STRUCTURE_IN_TOTAL")
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_hidden_structure, detect_range_issues

        findings = detect_range_issues(
            ctx.formula_wb, ctx.value_wb, ctx.formulas, names=ctx.names, budget=ctx.budget
        )
        findings.extend(
            detect_hidden_structure(
                ctx.formula_wb,
                ctx.formulas,
                names=ctx.names,
                budget=ctx.budget,
                allowed_sheet_names=ctx.allowed_sheet_names,
            )
        )
        return findings


@register
class RangeLengthMismatchCheck(Check):
    name = "range_length_mismatch"
    description = "Flags peer aggregate formulas whose ranges have different lengths."
    rule_ids = ("RANGE_LENGTH_MISMATCH",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_range_length_mismatch

        return detect_range_length_mismatch(ctx.formulas, names=ctx.names, budget=ctx.budget)


@register
class LiteralConstantCheck(Check):
    name = "literal_constants"
    description = "Surfaces likely-magic numbers embedded inside formulas."
    rule_ids = ("LITERAL_CONSTANT",)
    mode = "HEUR"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_literal_constants

        return detect_literal_constants(ctx.formulas, budget=ctx.budget)


@register
class FragileFunctionCheck(Check):
    name = "volatile_functions"
    description = "Flags volatile/whole-column constructs that often introduce bugs (TODAY, OFFSET, A:A)."
    rule_ids = ("VOLATILE_FUNCTION", "WHOLE_COLUMN_REFERENCE")
    mode = "HEUR"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_fragile_functions

        return detect_fragile_functions(ctx.formulas, names=ctx.names, budget=ctx.budget)
