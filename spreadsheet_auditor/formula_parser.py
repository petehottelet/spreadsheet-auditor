"""Formula parsing built on openpyxl's formula tokenizer.

Everything the auditor knows about a formula's structure comes from here:
cell and range references (with defined names and structured table
references resolved to A1 ranges when a ``NameTable`` is supplied), function
names, numeric literals, error literals, and flags for constructs the checks
cannot reason about (external links, 3-D references, implicit intersection,
spill ranges).

The previous implementation ran regular expressions over the raw formula
text, which misread function names such as ``LOG10`` or ``DAYS360`` and the
tails of names such as ``EBITDA2025`` as cell references.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any

from openpyxl.formula import Tokenizer
from openpyxl.formula.tokenizer import Token, TokenizerError
from openpyxl.utils.cell import column_index_from_string, get_column_letter

try:  # openpyxl >= 3.1
    from openpyxl.worksheet.formula import ArrayFormula, DataTableFormula
except ImportError:  # pragma: no cover - older openpyxl
    ArrayFormula = None  # type: ignore[assignment,misc]
    DataTableFormula = None  # type: ignore[assignment,misc]


TRIVIAL_CONSTANTS = {0, 1, -1, 2, 4, 7, 12, 13, 24, 30, 31, 52, 100, 365, 1000}
YEAR_RANGE = range(1900, 2101)
ERROR_LITERALS = {
    "#NULL!",
    "#DIV/0!",
    "#VALUE!",
    "#REF!",
    "#NAME?",
    "#NUM!",
    "#N/A",
    "#GETTING_DATA",
    "#SPILL!",
    "#CALC!",
}
FUNCTION_PREFIXES = ("_XLFN.", "_XLWS.", "_XLPM.", "_XLL.")

_CELL = r"\$?[A-Za-z]{1,3}\$?\d{1,7}"
CELL_OR_RANGE_RE = re.compile(rf"^{_CELL}(?::{_CELL})?$")
WHOLE_COLUMN_RE = re.compile(r"^\$?[A-Za-z]{1,3}:\$?[A-Za-z]{1,3}$")
WHOLE_ROW_RE = re.compile(r"^\$?\d{1,7}:\$?\d{1,7}$")
NAME_RE = re.compile(r"^[A-Za-z_\\][A-Za-z0-9_.\\?]*$")
# External references carry a bracketed workbook index or file name followed by
# a sheet name and "!": [1]Sheet1!A1, '[Book.xlsx]Sheet1'!A1. A structured
# reference such as [@Sales] or [[#Totals],[Sales]] has no "!" tail.
EXTERNAL_RE = re.compile(r"^'?\[[^\]]*\][^!\[]*'?!")
STRUCTURED_RE = re.compile(r"^(?P<table>[A-Za-z_\\][A-Za-z0-9_.]*)?\[(?P<body>.*)\]$", re.S)
_CELL_PART_RE = re.compile(r"^(\$?)([A-Za-z]{1,3})(\$?)(\d{1,7})$")
_COL_PART_RE = re.compile(r"^(\$?)([A-Za-z]{1,3})$")
_ROW_PART_RE = re.compile(r"^(\$?)(\d{1,7})$")
# Kept for callers that imported the old regex-based helper.
STRING_RE = re.compile(r'"(?:[^"]|"")*"')


@dataclass(frozen=True)
class ParsedReference:
    """A cell or range reference found in a formula.

    ``ref`` is normalized (upper-case, no ``$``). ``bounded`` is False for
    whole-column/whole-row references such as ``A:A`` or ``1:1``. ``via_name``
    records the defined name or structured reference the range came from.
    """

    raw: str
    sheet: str | None
    ref: str
    is_range: bool
    bounded: bool = True
    via_name: str | None = None


@dataclass
class ParsedFormula:
    formula: str
    references: list[ParsedReference] = field(default_factory=list)
    functions: set[str] = field(default_factory=set)
    numeric_literals: list[str] = field(default_factory=list)
    error_literals: list[str] = field(default_factory=list)
    external_references: list[str] = field(default_factory=list)
    structured_references: list[str] = field(default_factory=list)
    unresolved_structured: list[str] = field(default_factory=list)
    unresolved_names: list[str] = field(default_factory=list)
    three_d_references: list[str] = field(default_factory=list)
    implicit_intersection: bool = False
    spill: bool = False
    parse_error: str | None = None

    @property
    def deleted_reference(self) -> bool:
        return "#REF!" in self.error_literals


def formula_text(value: object) -> str | None:
    """Return the formula text for a cell value, or None if it is not a formula.

    Handles plain ``=...`` strings and openpyxl's ``ArrayFormula`` objects
    (legacy CSE arrays and dynamic arrays). Data-table formulas carry no text.
    """
    if isinstance(value, str):
        return value if value.startswith("=") else None
    if ArrayFormula is not None and isinstance(value, ArrayFormula):
        text = getattr(value, "text", None)
        if not isinstance(text, str) or not text:
            return None
        return text if text.startswith("=") else "=" + text
    return None


def is_formula(value: object) -> bool:
    if formula_text(value) is not None:
        return True
    return DataTableFormula is not None and isinstance(value, DataTableFormula)


@lru_cache(maxsize=65536)
def _tokenize(formula: str) -> tuple[tuple[str, str, str], ...] | None:
    try:
        return tuple((tok.value, tok.type, tok.subtype) for tok in Tokenizer(formula).items)
    except (TokenizerError, IndexError, ValueError):
        return None


def tokens(formula: str) -> tuple[tuple[str, str, str], ...] | None:
    """Tokenize ``formula`` into ``(value, type, subtype)`` triples; None if unparseable."""
    return _tokenize(formula)


def strip_string_literals(formula: str) -> str:
    return STRING_RE.sub('""', formula)


def normalize_sheet_name(sheet: str | None) -> str | None:
    if not sheet:
        return None
    if sheet.startswith("'") and sheet.endswith("'"):
        return sheet[1:-1].replace("''", "'")
    return sheet


def split_sheet(text: str) -> tuple[str | None, str]:
    """Split ``Sheet!A1`` / ``'My Sheet'!A1`` into (sheet, rest)."""
    if text.startswith("'"):
        i = 1
        while i < len(text):
            if text[i] == "'":
                if i + 1 < len(text) and text[i + 1] == "'":
                    i += 2
                    continue
                break
            i += 1
        if i < len(text) - 1 and text[i] == "'" and text[i + 1] == "!":
            return text[1:i].replace("''", "'"), text[i + 2 :]
        return None, text
    if "!" in text:
        sheet, rest = text.split("!", 1)
        return sheet, rest
    return None, text


def _keep_literal(text: str) -> bool:
    try:
        value = float(text)
    except ValueError:
        return False
    if value.is_integer():
        integer_value = int(value)
        if integer_value in TRIVIAL_CONSTANTS:
            return False
        # Bare integers that look like calendar years are usually period
        # labels, not embedded assumptions; skip to reduce noise.
        if integer_value in YEAR_RANGE:
            return False
    return True


def _classify_operand(
    text: str,
    parsed: ParsedFormula,
    names: Any,
    origin: tuple[str, int, int] | None,
) -> None:
    raw = text
    if text.startswith("@"):
        parsed.implicit_intersection = True
        text = text[1:]
    if not text:
        return
    if EXTERNAL_RE.match(text):
        parsed.external_references.append(raw)
        return
    sheet, rest = split_sheet(text)
    if sheet is None and STRUCTURED_RE.match(text):
        parsed.structured_references.append(raw)
        resolved = names.resolve_structured(text, origin) if names is not None else []
        if resolved:
            for target_sheet, target_ref in resolved:
                parsed.references.append(
                    ParsedReference(
                        raw=raw,
                        sheet=target_sheet,
                        ref=target_ref,
                        is_range=":" in target_ref,
                        via_name=text,
                    )
                )
        else:
            parsed.unresolved_structured.append(raw)
        return
    if sheet is not None and ":" in sheet:
        parsed.three_d_references.append(raw)
        return
    clean = rest.replace("$", "")
    upper = clean.upper()
    if upper in ERROR_LITERALS:
        parsed.error_literals.append(upper)
        return
    if CELL_OR_RANGE_RE.match(clean):
        parsed.references.append(ParsedReference(raw=raw, sheet=sheet, ref=upper, is_range=":" in upper))
        return
    if WHOLE_COLUMN_RE.match(clean) or WHOLE_ROW_RE.match(clean):
        parsed.references.append(
            ParsedReference(raw=raw, sheet=sheet, ref=upper, is_range=True, bounded=False)
        )
        return
    if NAME_RE.match(clean):
        origin_sheet = origin[0] if origin else None
        resolved = names.resolve(clean, sheet or origin_sheet) if names is not None else []
        if resolved:
            for target_sheet, target_ref in resolved:
                parsed.references.append(
                    ParsedReference(
                        raw=raw,
                        sheet=target_sheet,
                        ref=target_ref,
                        is_range=":" in target_ref,
                        via_name=clean,
                    )
                )
        else:
            parsed.unresolved_names.append(clean)
        return
    parsed.unresolved_names.append(raw)


def parse_formula(
    formula: str,
    names: Any = None,
    origin: tuple[str, int, int] | None = None,
) -> ParsedFormula:
    """Parse ``formula`` once and classify every token.

    ``names`` is an optional ``NameTable`` used to resolve defined names and
    structured table references. ``origin`` is ``(sheet, row, col)`` of the
    formula cell; it is needed for sheet-scoped names and ``[@Column]``
    this-row references.
    """
    parsed = ParsedFormula(formula=formula)
    tokens = _tokenize(formula)
    if tokens is None:
        parsed.parse_error = "unparseable formula"
        return parsed
    for idx, (value, ttype, subtype) in enumerate(tokens):
        if ttype == Token.FUNC and subtype == Token.OPEN:
            name = value[:-1]
            if ":" in name:
                # The tokenizer glues a range start to a function call in
                # constructs such as ``A1:OFFSET(...)``.
                left, name = name.rsplit(":", 1)
                _classify_operand(left, parsed, names, origin)
            fname = name.upper()
            for prefix in FUNCTION_PREFIXES:
                if fname.startswith(prefix):
                    fname = fname[len(prefix) :]
                    break
            parsed.functions.add(fname)
            if fname == "SINGLE":
                parsed.implicit_intersection = True
            elif fname == "ANCHORARRAY":
                parsed.spill = True
        elif ttype == Token.OPERAND:
            if subtype == Token.RANGE:
                _classify_operand(value, parsed, names, origin)
            elif subtype == Token.NUMBER:
                nxt = tokens[idx + 1] if idx + 1 < len(tokens) else None
                if nxt is not None and nxt[1] == Token.OP_POST and nxt[0] == "%":
                    continue
                if _keep_literal(value):
                    parsed.numeric_literals.append(value)
            elif subtype == Token.ERROR:
                parsed.error_literals.append(value.upper())
        elif ttype == Token.OP_PRE and value == "@":
            parsed.implicit_intersection = True
    return parsed


def extract_references(
    formula: str,
    names: Any = None,
    origin: tuple[str, int, int] | None = None,
) -> list[ParsedReference]:
    return parse_formula(formula, names=names, origin=origin).references


def extract_functions(formula: str) -> set[str]:
    return parse_formula(formula).functions


def extract_numeric_literals(formula: str) -> list[str]:
    return parse_formula(formula).numeric_literals


def _relative_row(row: int, absolute: bool, origin_row: int) -> str:
    if absolute:
        return f"R{row}"
    return "R" if row == origin_row else f"R[{row - origin_row}]"


def _relative_col(col: int, absolute: bool, origin_col: int) -> str:
    if absolute:
        return f"C{col}"
    return "C" if col == origin_col else f"C[{col - origin_col}]"


def _normalize_operand(text: str, origin_row: int, origin_col: int) -> str:
    prefix = ""
    if text.startswith("@"):
        prefix, text = "@", text[1:]
    if EXTERNAL_RE.match(text):
        return prefix + text.upper()
    sheet, rest = split_sheet(text)
    if sheet is None and STRUCTURED_RE.match(text):
        return prefix + text.upper()
    parts = rest.split(":")
    normalized: list[str] = []
    if CELL_OR_RANGE_RE.match(rest):
        for part in parts:
            match = _CELL_PART_RE.match(part)
            if match is None:
                return prefix + text.upper()
            col_abs, col, row_abs, row = match.groups()
            normalized.append(
                _relative_row(int(row), bool(row_abs), origin_row)
                + _relative_col(column_index_from_string(col.upper()), bool(col_abs), origin_col)
            )
    elif WHOLE_COLUMN_RE.match(rest):
        for part in parts:
            match = _COL_PART_RE.match(part)
            if match is None:
                return prefix + text.upper()
            col_abs, col = match.groups()
            normalized.append(
                _relative_col(column_index_from_string(col.upper()), bool(col_abs), origin_col)
            )
    elif WHOLE_ROW_RE.match(rest):
        for part in parts:
            match = _ROW_PART_RE.match(part)
            if match is None:
                return prefix + text.upper()
            row_abs, row = match.groups()
            normalized.append(_relative_row(int(row), bool(row_abs), origin_row))
    else:
        return prefix + text.upper()
    body = ":".join(normalized)
    if sheet is not None:
        return f"{prefix}{sheet.upper()}!{body}"
    return prefix + body


def normalize_formula(formula: str, origin_row: int, origin_col: int) -> str:
    """Rewrite references relative to the formula's own cell (R1C1 style).

    Two formulas that follow the same relative pattern normalize to the same
    string regardless of where they sit. Absolute markers are honoured, so a
    row of formulas that all anchor to ``$B$1`` still shares one pattern.
    """
    tokens = _tokenize(formula)
    if tokens is None:
        return formula.upper()
    out: list[str] = []
    for value, ttype, subtype in tokens:
        if ttype == Token.WSPACE:
            continue
        if ttype == Token.OPERAND and subtype == Token.RANGE:
            out.append(_normalize_operand(value, origin_row, origin_col))
        elif ttype == Token.FUNC and subtype == Token.OPEN and ":" in value[:-1]:
            left, name = value[:-1].rsplit(":", 1)
            out.append(_normalize_operand(left, origin_row, origin_col) + ":" + name.upper() + "(")
        elif ttype == Token.OPERAND and subtype == Token.TEXT:
            out.append(value)
        else:
            out.append(value.upper())
    return "=" + "".join(out)


def cell_to_location(sheet: str, row: int, col: int) -> str:
    return f"{sheet}!{get_column_letter(col)}{row}"


def column_letters_to_index(col_letters: str) -> int:
    return column_index_from_string(col_letters.replace("$", ""))
