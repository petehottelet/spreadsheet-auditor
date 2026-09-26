"""Location parsing and containment.

Used by suppressions and by ``scope.headline_outputs`` matching. Locations are
``Sheet!A1``, ``Sheet!A1:B10``, whole columns/rows (``Sheet!A:A``), or a
comma-joined list of those (``Model!A37, Model!A38``). Finding locations
carry sheet names unquoted, and a sheet name may itself contain a comma
(``P&L, 2025!B1``) or an exclamation mark; targets written by users may quote
them (``'P&L, 2025'!B1``).
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
# CSV findings use R1C1 coordinates (``CSV!R2C1``).
_R1C1_RE = re.compile(r"^R\d+C\d+$")

Box = tuple[int, int, int, int]


def unquote_sheet(sheet: str) -> str:
    """``'O''Brien'`` -> ``O'Brien``; an unquoted name is returned stripped."""
    sheet = sheet.strip()
    if len(sheet) >= 2 and sheet[0] == "'" and sheet[-1] == "'":
        return sheet[1:-1].replace("''", "'")
    return sheet


def _split(piece: str) -> tuple[str | None, str]:
    piece = piece.strip()
    if "!" not in piece:
        return None, piece
    sheet, addr = piece.rsplit("!", 1)
    return unquote_sheet(sheet), addr.strip()


def target_sheet(target: str) -> str | None:
    """The sheet a suppression or headline target names (a bare target is a sheet)."""
    if not target.strip():
        return None
    sheet, addr = _split(target)
    return sheet if sheet is not None else unquote_sheet(addr)


def _is_address(addr: str) -> bool:
    text = addr.replace("$", "").replace(" ", "").upper()
    return _box(text) is not None or bool(_R1C1_RE.match(text))


def split_location(location: str) -> list[str]:
    """Split a comma-joined location into its pieces.

    A comma ends a piece only when the text before it is a complete
    ``Sheet!address``; otherwise it belongs to a sheet name, so
    ``P&L, 2025!B1, P&L, 2025!B2`` is two pieces, not four.
    """
    pieces: list[str] = []
    pending = ""
    for segment in (location or "").split(","):
        pending = f"{pending},{segment}" if pending else segment
        sheet, addr = _split(pending)
        if sheet is not None and _is_address(addr):
            pieces.append(pending.strip())
            pending = ""
    if pending.strip():
        pieces.append(pending.strip())
    return pieces


def anchor(location: str) -> tuple[str, int, int] | None:
    """``(sheet, row, col)`` of the top-left cell of a location's first piece.

    A whole column anchors on row 1 and a whole row on column A. ``None`` when
    the location names no sheet or no A1-style address.
    """
    pieces = split_location(location)
    if not pieces:
        return None
    sheet, addr = _split(pieces[0])
    box = _box(addr) if sheet else None
    if box is None:
        return None
    return sheet, box[1], box[0]


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

    ``target`` is ``Sheet!cell``, ``Sheet!range``, ``Sheet!A:A`` or
    ``Sheet!5:5``, or a bare sheet name for the whole sheet. A target without
    ``!`` is always a sheet name, even one that reads like a cell (``Q1``,
    ``FY2025``). A multi-cell ``location`` matches when any of its pieces is
    covered. Sheet names compare case-insensitively and ``$`` markers are
    ignored. Locations that are not A1-style (for example CSV ``R1C2``
    coordinates) match only on exact text. Nothing is matched by substring,
    so ``Imports!A1`` never covers ``Imports!A10``.
    """
    if not location or not target:
        return False
    target = target.strip()
    t_sheet, t_addr = _split(target)
    whole_sheet = t_sheet is None
    whole_sheet_key = unquote_sheet(t_addr).casefold() if whole_sheet else None
    t_box = None if whole_sheet else _box(t_addr)
    t_sheet_key = (t_sheet or "").casefold()
    for piece in split_location(location):
        if _norm_text(piece) == _norm_text(target):
            return True
        p_sheet, p_addr = _split(piece)
        p_sheet_key = (p_sheet or "").casefold()
        if whole_sheet:
            if p_sheet_key == whole_sheet_key:
                return True
            continue
        if p_sheet_key != t_sheet_key:
            continue
        if t_box is None:
            if _norm_text(p_addr) == _norm_text(t_addr):
                return True
            continue
        p_box = _box(p_addr)
        if p_box is not None and _contains(t_box, p_box):
            return True
    return False
