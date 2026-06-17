from __future__ import annotations

import re
from dataclasses import dataclass

from openpyxl.utils.cell import column_index_from_string, coordinate_to_tuple


CELL_REF_RE = re.compile(
    r"(?:(?P<sheet>'(?:[^']|'')+'|[A-Za-z_][A-Za-z0-9_ .]*)!)?"
    r"(?P<ref>\$?[A-Z]{1,3}\$?\d{1,7}(?::\$?[A-Z]{1,3}\$?\d{1,7})?)",
    re.IGNORECASE,
)
FUNCTION_RE = re.compile(r"\b([A-Z][A-Z0-9_.]*)\s*\(", re.IGNORECASE)
NUMERIC_RE = re.compile(r"(?<![A-Za-z0-9_.$])[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?(?![A-Za-z0-9_.%])")
STRING_RE = re.compile(r'"(?:[^"]|"")*"')
TRIVIAL_CONSTANTS = {0, 1, -1, 2, 4, 7, 12, 13, 24, 30, 31, 52, 100, 365, 1000}


@dataclass(frozen=True)
class ParsedReference:
    raw: str
    sheet: str | None
    ref: str
    is_range: bool


def strip_string_literals(formula: str) -> str:
    return STRING_RE.sub('""', formula)


def normalize_sheet_name(sheet: str | None) -> str | None:
    if not sheet:
        return None
    if sheet.startswith("'") and sheet.endswith("'"):
        return sheet[1:-1].replace("''", "'")
    return sheet


def extract_references(formula: str) -> list[ParsedReference]:
    clean = strip_string_literals(formula)
    refs: list[ParsedReference] = []
    for match in CELL_REF_RE.finditer(clean):
        raw = match.group(0)
        sheet = normalize_sheet_name(match.group("sheet"))
        ref = match.group("ref").replace("$", "").upper()
        refs.append(ParsedReference(raw=raw, sheet=sheet, ref=ref, is_range=":" in ref))
    return refs


def extract_functions(formula: str) -> set[str]:
    clean = strip_string_literals(formula)
    return {match.group(1).upper() for match in FUNCTION_RE.finditer(clean)}


def extract_numeric_literals(formula: str) -> list[str]:
    clean = strip_string_literals(formula)
    for ref in extract_references(clean):
        clean = clean.replace(ref.raw, "")
    literals: list[str] = []
    for match in NUMERIC_RE.finditer(clean):
        text = match.group(0)
        try:
            value = float(text)
        except ValueError:
            continue
        if value.is_integer() and int(value) in TRIVIAL_CONSTANTS:
            continue
        literals.append(text)
    return literals


def _normalize_single_ref(ref: str, origin_row: int, origin_col: int) -> str:
    row, col = coordinate_to_tuple(ref.replace("$", ""))
    return f"R{row - origin_row:+d}C{col - origin_col:+d}"


def normalize_formula(formula: str, origin_row: int, origin_col: int) -> str:
    def replace(match: re.Match[str]) -> str:
        sheet = normalize_sheet_name(match.group("sheet"))
        ref = match.group("ref").replace("$", "").upper()
        if ":" in ref:
            start, end = ref.split(":", 1)
            norm = f"{_normalize_single_ref(start, origin_row, origin_col)}:{_normalize_single_ref(end, origin_row, origin_col)}"
        else:
            norm = _normalize_single_ref(ref, origin_row, origin_col)
        return f"{sheet}!{norm}" if sheet else norm

    return CELL_REF_RE.sub(replace, strip_string_literals(formula).upper())


def is_formula(value: object) -> bool:
    return isinstance(value, str) and value.startswith("=")


def cell_to_location(sheet: str, row: int, col: int) -> str:
    from openpyxl.utils.cell import get_column_letter

    return f"{sheet}!{get_column_letter(col)}{row}"


def column_letters_to_index(col_letters: str) -> int:
    return column_index_from_string(col_letters.replace("$", ""))
