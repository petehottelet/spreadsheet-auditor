from __future__ import annotations

from collections.abc import Iterable

from openpyxl.utils.cell import get_column_letter, range_boundaries

from .formula_parser import ParsedReference

EXCEL_MAX_ROW = 1048576
EXCEL_MAX_COL = 16384

Box = tuple[int, int, int, int]


def ref_location(sheet: str, row: int, col: int) -> str:
    return f"{sheet}!{get_column_letter(col)}{row}"


def raw_boundaries(ref: str) -> tuple[int | None, int | None, int | None, int | None] | None:
    """openpyxl boundaries for ``ref``; open sides of whole-column/row refs are None.

    Returns None when the text is not a cell or range reference.
    """
    try:
        return range_boundaries(ref.replace("$", ""))
    except (ValueError, TypeError):
        return None


def boundaries(ref: str) -> Box | None:
    """Fully bounded ``(min_col, min_row, max_col, max_row)`` or None."""
    box = raw_boundaries(ref)
    if box is None or any(edge is None for edge in box):
        return None
    return box  # type: ignore[return-value]


def clamped_boundaries(ref: str, max_row: int, max_col: int) -> Box | None:
    """Like :func:`boundaries` but clamps whole-column/row references to an extent."""
    box = raw_boundaries(ref)
    if box is None:
        return None
    min_col, min_row, end_col, end_row = box
    return (
        min_col or 1,
        min_row or 1,
        max_col if end_col is None else end_col,
        max_row if end_row is None else end_row,
    )


def range_size(ref: str) -> int:
    box = boundaries(ref)
    if box is None:
        return 0
    min_col, min_row, max_col, max_row = box
    return (max_col - min_col + 1) * (max_row - min_row + 1)


def find_sheet(workbook, name: str | None) -> str | None:
    """Resolve a sheet name case-insensitively to the workbook's actual title."""
    if name is None:
        return None
    sheetnames = list(getattr(workbook, "sheetnames", []) or [])
    if name in sheetnames:
        return name
    wanted = name.casefold()
    for title in sheetnames:
        if title.casefold() == wanted:
            return title
    return None


def existing_cell(ws, row: int, col: int):
    """Return the cell at (row, col) if it exists, without creating it.

    ``ws.cell()`` and ``ws[coord]`` materialize missing cells, which silently
    grows the sheet's used range; a reference to a far-away cell must never
    turn a 20-row sheet into a million-cell scan.
    """
    cells = getattr(ws, "_cells", None)
    if cells is None:  # pragma: no cover - non-standard worksheet implementations
        return ws.cell(row=row, column=col)
    return cells.get((row, col))


def cell_value(ws, row: int, col: int):
    cell = existing_cell(ws, row, col)
    return None if cell is None else cell.value


def expand_reference(
    ref: ParsedReference,
    default_sheet: str,
    limit: int = 1000,
    extents: dict[str, tuple[int, int]] | None = None,
) -> list[str]:
    sheet = ref.sheet or default_sheet
    box = boundaries(ref.ref)
    if box is None and extents and sheet in extents:
        max_row, max_col = extents[sheet]
        box = clamped_boundaries(ref.ref, max_row=max_row, max_col=max_col)
    if box is None:
        return []
    min_col, min_row, max_col, max_row = box
    if (max_col - min_col + 1) * (max_row - min_row + 1) > limit:
        return []
    return [
        ref_location(sheet, row, col)
        for row in range(min_row, max_row + 1)
        for col in range(min_col, max_col + 1)
    ]


def reference_in_bounds(ref: ParsedReference, default_sheet: str, workbook) -> tuple[bool, str | None]:
    sheet = ref.sheet or default_sheet
    if find_sheet(workbook, sheet) is None:
        return False, f"Missing sheet '{sheet}'"
    box = raw_boundaries(ref.ref)
    if box is None:
        return False, "Unsupported reference syntax"
    _min_col, _min_row, max_col, max_row = box
    # Referencing cells beyond the populated/used range is normal Excel usage
    # (intentionally oversized ranges, future inputs). Only flag references that
    # fall outside Excel's absolute grid.
    if max_row is not None and max_row > EXCEL_MAX_ROW:
        return False, f"{sheet}!{ref.ref} row exceeds Excel's maximum of {EXCEL_MAX_ROW}"
    if max_col is not None and max_col > EXCEL_MAX_COL:
        return False, f"{sheet}!{ref.ref} column exceeds Excel's maximum of {EXCEL_MAX_COL}"
    return True, None


def cells_from_locations(workbook, locations: Iterable[str]):
    """Yield ``(location, cell_or_None)`` without materializing missing cells."""
    for location in locations:
        if "!" not in location:
            continue
        sheet, coord = location.rsplit("!", 1)
        title = find_sheet(workbook, sheet)
        if title is None:
            continue
        box = boundaries(coord)
        if box is None:
            continue
        yield location, existing_cell(workbook[title], box[1], box[0])
