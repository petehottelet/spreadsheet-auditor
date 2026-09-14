"""Index of the cells and ranges that formulas reference.

Data-hygiene checks use it to stay quiet about cells nothing consumes: a
number stored as text matters when a SUM silently ignores it, a merged region
matters when a formula reads through it, and duplicate keys matter inside the
ranges that lookup functions search.
"""

from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict

from .budget import tick
from .formula_parser import parse_formula
from .reference_resolver import raw_boundaries

EXCEL_MAX_ROW = 1048576
EXCEL_MAX_COL = 16384
WIDE_SPAN = 512  # ranges wider than this are kept as row intervals shared by every column

# (function, 0-based argument index) of the range a first-match lookup
# searches. SUMIF/COUNTIF criteria ranges are not keys: repeats there are the
# point of the aggregation.
KEY_SLOTS = {
    ("VLOOKUP", 1),
    ("HLOOKUP", 1),
    ("MATCH", 1),
    ("XMATCH", 1),
    ("XLOOKUP", 1),
    ("LOOKUP", 1),
}

Box = tuple[int, int, int, int]
Interval = tuple[int, int]


def _merge(intervals: list[Interval]) -> list[Interval]:
    merged: list[Interval] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def _covers(starts: list[int], intervals: list[Interval], row: int) -> bool:
    if not intervals:
        return False
    idx = bisect_right(starts, row) - 1
    return idx >= 0 and intervals[idx][1] >= row


class _ColumnIndex:
    def __init__(self) -> None:
        self._raw: dict[int, list[Interval]] = defaultdict(list)
        self._wide_raw: list[Interval] = []
        self.columns: dict[int, list[Interval]] = {}
        self.starts: dict[int, list[int]] = {}
        self.wide: list[Interval] = []
        self.wide_starts: list[int] = []

    def add(self, box: Box) -> None:
        min_col, min_row, max_col, max_row = box
        if max_col - min_col + 1 > WIDE_SPAN:
            self._wide_raw.append((min_row, max_row))
            return
        for col in range(min_col, max_col + 1):
            self._raw[col].append((min_row, max_row))

    def build(self) -> None:
        self.columns = {col: _merge(intervals) for col, intervals in self._raw.items()}
        self.starts = {col: [start for start, _ in intervals] for col, intervals in self.columns.items()}
        self.wide = _merge(self._wide_raw)
        self.wide_starts = [start for start, _ in self.wide]

    def covers(self, row: int, col: int) -> bool:
        if _covers(self.wide_starts, self.wide, row):
            return True
        return _covers(self.starts.get(col, []), self.columns.get(col, []), row)

    def intervals(self, col: int) -> list[Interval]:
        return _merge(self.columns.get(col, []) + self.wide)

    def column_numbers(self) -> list[int]:
        return sorted(self.columns)


class ReferenceIndex:
    """Which cells formulas read, per sheet, with a lookup-only view."""

    def __init__(self) -> None:
        self._all: dict[str, _ColumnIndex] = {}
        self._lookup: dict[str, _ColumnIndex] = {}
        self._numeric: dict[str, _ColumnIndex] = {}
        self._boxes: dict[str, list[tuple[Box, bool]]] = defaultdict(list)

    @classmethod
    def from_formulas(cls, formulas: list[dict], names=None, budget=None) -> "ReferenceIndex":
        index = cls()
        for item in formulas:
            tick(budget)
            parsed = parse_formula(
                item["formula"], names=names, origin=(item["sheet"], item["row"], item["col"])
            )
            for ref in parsed.references:
                if ref.positional:
                    continue
                key = (ref.sheet or item["sheet"]).casefold()
                raw = raw_boundaries(ref.ref)
                if raw is None:
                    continue
                min_col, min_row, max_col, max_row = raw
                box = (
                    min_col or 1,
                    min_row or 1,
                    EXCEL_MAX_COL if max_col is None else max_col,
                    EXCEL_MAX_ROW if max_row is None else max_row,
                )
                index._boxes[key].append((box, ref.is_range))
                index._all.setdefault(key, _ColumnIndex()).add(box)
                if ref.numeric:
                    index._numeric.setdefault(key, _ColumnIndex()).add(box)
                if ref.bare and (ref.func, ref.arg) in KEY_SLOTS:
                    # Only the searched column or row of a lookup table is a key
                    # column; VLOOKUP's other columns are what it returns.
                    key_box = box
                    if ref.func == "VLOOKUP":
                        key_box = (box[0], box[1], box[0], box[3])
                    elif ref.func == "HLOOKUP":
                        key_box = (box[0], box[1], box[2], box[1])
                    index._lookup.setdefault(key, _ColumnIndex()).add(key_box)
        for column_index in (
            list(index._all.values()) + list(index._lookup.values()) + list(index._numeric.values())
        ):
            column_index.build()
        return index

    def contains(self, sheet: str, row: int, col: int) -> bool:
        """True when some formula reads the cell at (row, col) on ``sheet``."""
        column_index = self._all.get(sheet.casefold())
        return bool(column_index and column_index.covers(row, col))

    def numeric_contains(self, sheet: str, row: int, col: int) -> bool:
        """True when a formula consumes the cell at (row, col) as a number (arithmetic, SUM, ...)."""
        column_index = self._numeric.get(sheet.casefold())
        return bool(column_index and column_index.covers(row, col))

    def lookup_columns(self, sheet: str) -> list[int]:
        """Columns on ``sheet`` that lookup-style functions search."""
        column_index = self._lookup.get(sheet.casefold())
        return column_index.column_numbers() if column_index else []

    def lookup_intervals(self, sheet: str, col: int) -> list[Interval]:
        """Row intervals of ``col`` on ``sheet`` searched by lookup-style functions."""
        column_index = self._lookup.get(sheet.casefold())
        return column_index.intervals(col) if column_index else []

    def intersects_box(self, sheet: str, box: Box, ranges_only: bool = False) -> bool:
        """True when any referenced range overlaps ``box`` on ``sheet``.

        With ``ranges_only`` a single-cell reference does not count: a formula
        that addresses the top-left cell of a merge directly reads the value
        the author sees, only a range read through the merge sees blanks.
        """
        min_col, min_row, max_col, max_row = box
        for (c1, r1, c2, r2), is_range in self._boxes.get(sheet.casefold(), ()):
            if ranges_only and not is_range:
                continue
            if c1 <= max_col and c2 >= min_col and r1 <= max_row and r2 >= min_row:
                return True
        return False
