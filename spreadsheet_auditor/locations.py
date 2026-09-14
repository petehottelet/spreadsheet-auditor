"""Location parsing and containment.

Used by suppressions and by ``scope.headline_outputs`` matching. Locations are
``Sheet!A1``, ``Sheet!A1:B10``, whole columns/rows (``Sheet!A:A``), or a
comma-joined list of those (``Model!A37, Model!A38``).
"""

from __future__ import annotations

import re

from openpyxl.utils.cell import column_index_from_string

EXCEL_MAX_ROW = 1048576
EXCEL_MAX_COL = 16384

_CELL_RE = re.compile(r"^([A-Z]{1,3})(\d{1,7})$")
_RANGE_RE = re.compile(r"^([A-Z]{1,3})(\d{1,7}):([A-Z]{1,3})(\d{1,7})$")
_COLS_RE = re.compile(r"^([A-Z]{1,3}):([A-Z]{1,3})$")
_ROWS_RE = re.compile(r"^(\d{1,7}):(\d{1,7})$")

Box = tuple[int, int, int, int]


def _split(piece: str) -> tuple[str | None, str]:
    piece = piece.strip()
    if "!" not in piece:
        return None, piece
    sheet, addr = piece.rsplit("!", 1)
    sheet = sheet.strip()
    if len(sheet) >= 2 and sheet[0] == "'" and sheet[-1] == "'":
        sheet = sheet[1:-1].replace("''", "'")
    return sheet, addr.strip()


def _box(addr: str) -> Box | None:
    text = addr.replace("$", "").replace(" ", "").upper()
    match = _CELL_RE.match(text)
    if match:
        col = column_index_from_string(match.group(1))
        row = int(match.group(2))
        return (col, row, col, row)
    match = _RANGE_RE.match(text)
    if match:
        col1 = column_index_from_string(match.group(1))
        row1 = int(match.group(2))
        col2 = column_index_from_string(match.group(3))
        row2 = int(match.group(4))
        return (min(col1, col2), min(row1, row2), max(col1, col2), max(row1, row2))
    match = _COLS_RE.match(text)
    if match:
        col1 = column_index_from_string(match.group(1))
        col2 = column_index_from_string(match.group(2))
        return (min(col1, col2), 1, max(col1, col2), EXCEL_MAX_ROW)
    match = _ROWS_RE.match(text)
    if match:
        row1, row2 = int(match.group(1)), int(match.group(2))
        return (1, min(row1, row2), EXCEL_MAX_COL, max(row1, row2))
    return None


def _contains(outer: Box, inner: Box) -> bool:
    return (
        outer[0] <= inner[0]
        and outer[1] <= inner[1]
        and outer[2] >= inner[2]
        and outer[3] >= inner[3]
    )


def _norm_text(text: str) -> str:
    return text.replace("$", "").replace(" ", "").upper()


def location_matches(location: str, target: str) -> bool:
    """True when ``target`` covers ``location``.

    ``target`` is a cell, a range, a whole column/row, or a bare sheet name
    (the whole sheet). A multi-cell ``location`` matches when any of its
    pieces is covered. Sheet names compare case-insensitively and ``$``
    markers are ignored. Locations that are not A1-style (for example CSV
    ``R1C2`` coordinates) match only on exact text. Nothing is matched by
    substring, so ``Imports!A1`` never covers ``Imports!A10``.
    """
    if not location or not target:
        return False
    target = target.strip()
    t_sheet, t_addr = _split(target)
    t_box = _box(t_addr)
    whole_sheet = t_sheet is None and t_box is None and bool(t_addr)
    whole_sheet_key = t_addr.strip("'").casefold() if whole_sheet else None
    t_sheet_key = (t_sheet or "").casefold()
    for piece in location.split(","):
        piece = piece.strip()
        if not piece:
            continue
        if _norm_text(piece) == _norm_text(target):
            return True
        p_sheet, p_addr = _split(piece)
        p_sheet_key = (p_sheet or "").casefold()
        if whole_sheet:
            if p_sheet_key == whole_sheet_key:
                return True
            continue
        if t_sheet is not None and p_sheet_key != t_sheet_key:
            continue
        if t_box is None:
            if _norm_text(p_addr) == _norm_text(t_addr):
                return True
            continue
        p_box = _box(p_addr)
        if p_box is not None and _contains(t_box, p_box):
            return True
    return False
