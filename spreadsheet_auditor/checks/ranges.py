"""Range-shape checks: off-by-one, length mismatches, embedded literals, volatile functions."""

from __future__ import annotations

from ..finding import Finding
from .base import Check, CheckContext, register


@register
class RangeIssueCheck(Check):
    name = "range_issues"
    description = "Detects ranges that exclude adjacent data rows/columns or straddle subtotals."
    rule_ids = ("RANGE_EXCLUSION", "RANGE_INCLUDES_SUBTOTAL", "HIDDEN_STRUCTURE_IN_TOTAL", "WHOLE_COLUMN_REFERENCE")
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_range_issues

        return detect_range_issues(ctx.formula_wb, ctx.value_wb, ctx.formulas)


@register
class RangeLengthMismatchCheck(Check):
    name = "range_length_mismatch"
    description = "Flags peer aggregate formulas whose ranges have different lengths."
    rule_ids = ("RANGE_LENGTH_MISMATCH",)
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_range_length_mismatch

        return detect_range_length_mismatch(ctx.formulas)


@register
class LiteralConstantCheck(Check):
    name = "literal_constants"
    description = "Surfaces likely-magic numbers embedded inside formulas."
    rule_ids = ("LITERAL_CONSTANT",)
    mode = "HEUR"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_literal_constants

        return detect_literal_constants(ctx.formulas)


@register
class FragileFunctionCheck(Check):
    name = "volatile_functions"
    description = "Flags volatile/whole-column constructs that often introduce bugs (TODAY, OFFSET, A:A)."
    rule_ids = ("VOLATILE_FUNCTION", "WHOLE_COLUMN_REFERENCE")
    mode = "HEUR"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..range_checks import detect_fragile_functions

        return detect_fragile_functions(ctx.formulas)
