"""Data-hygiene checks: numbers-as-text, whitespace keys, duplicates, merged cells."""

from __future__ import annotations

from ..finding import Finding
from .base import Check, CheckContext, register


@register
class DataHygieneCheck(Check):
    name = "data_hygiene"
    description = "Surfaces numbers-stored-as-text, whitespace keys, duplicate keys, merged cells in data ranges."
    rule_ids = (
        "NUMBERS_STORED_AS_TEXT",
        "WHITESPACE_KEY",
        "DUPLICATE_KEY",
        "MERGED_CELL_IN_DATA_RANGE",
    )
    mode = "DET"

    def run(self, ctx: CheckContext) -> list[Finding]:
        from ..data_hygiene import detect_data_hygiene

        return detect_data_hygiene(ctx.formula_wb, ctx.allowed_sheet_names)
