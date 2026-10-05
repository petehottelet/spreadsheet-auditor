"""Index of the cells and ranges that formulas reference.

Data-hygiene checks use it to stay quiet about cells nothing consumes: a
number stored as text matters when a SUM silently ignores it, a merged region
matters when a formula reads through it, and duplicate keys matter inside the
ranges that lookup functions search.
"""

from __future__ import annotations

import re
from bisect import bisect_right
from collections import defaultdict
from dataclasses import dataclass

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

# (function, argument index) of the range a lookup returns from, read
# together with the searched range of the same formula: XLOOKUP's and
# LOOKUP's result array, and the array INDEX picks from in INDEX/MATCH.
RETURN_SLOTS = {("XLOOKUP", 2), ("LOOKUP", 2), ("INDEX", 0)}
_START_ROW_RE = re.compile(r"^\$?[A-Za-z]{1,3}(\$?)(\d+)")


@dataclass(frozen=True)
class SearchedRange:
    """One range a first-match lookup searches, in the direction it searches.

    ``box`` is the key column (VLOOKUP's first column, a MATCH range) or the
    key row (HLOOKUP's first row, a one-row MATCH range). ``moving_start``
    marks a range that starts on the row below its formula and moves with it
    (``MATCH(G5,$G6:$G28,0)`` in row 5): it looks for the next occurrence, so
    repeats are what it is for. ``returns`` are the cells the lookup returns
    from, or None when the formula does not say.
    """

    box: Box
    horizontal: bool
    moving_start: bool = False
    returns: tuple[Box, ...] | None = None


def _merge(intervals: list[Interval]) -> list[Interval]:
    merged: list[Interval] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def _bounded(ref: str) -> Box | None:
    """The box of ``ref`` with open sides (``A:A``, ``5:5``) filled to the sheet's limits."""
    raw = raw_boundaries(ref)
    if raw is None:
        return None
    min_col, min_row, max_col, max_row = raw
    return (
        min_col or 1,
        min_row or 1,
        EXCEL_MAX_COL if max_col is None else max_col,
        EXCEL_MAX_ROW if max_row is None else max_row,
    )


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


class ReferenceIndex:
    """Which cells formulas read, per sheet, and the ranges first-match lookups search."""

    def __init__(self) -> None:
        self._all: dict[str, _ColumnIndex] = {}
        self._numeric: dict[str, _ColumnIndex] = {}
        self._unconverted: dict[str, _ColumnIndex] = {}
        self._boxes: dict[str, list[tuple[Box, bool]]] = defaultdict(list)
        self._searched: dict[str, set[SearchedRange]] = defaultdict(set)

    @classmethod
    def from_formulas(cls, formulas: list[dict], names=None, budget=None) -> "ReferenceIndex":
        index = cls()
        for item in formulas:
            tick(budget)
            parsed = parse_formula(
                item["formula"], names=names, origin=(item["sheet"], item["row"], item["col"])
            )
            index._add_lookups(item, parsed.references)
            for ref in parsed.references:
                if ref.positional:
                    continue
                key = (ref.sheet or item["sheet"]).casefold()
                box = _bounded(ref.ref)
                if box is None:
                    continue
                index._boxes[key].append((box, ref.is_range))
                index._all.setdefault(key, _ColumnIndex()).add(box)
                if ref.numeric:
                    index._numeric.setdefault(key, _ColumnIndex()).add(box)
                    if not ref.converted:
                        index._unconverted.setdefault(key, _ColumnIndex()).add(box)
        for column_index in (
            list(index._all.values()) + list(index._numeric.values()) + list(index._unconverted.values())
        ):
            column_index.build()
        return index

    def _add_lookups(self, item: dict, references) -> None:
        """Record each range a first-match lookup in this formula searches."""
        returns: dict[str, list[Box]] = defaultdict(list)
        for ref in references:
            box = _bounded(ref.ref)
            if box is not None and (ref.func, ref.arg) in RETURN_SLOTS:
                returns[(ref.sheet or item["sheet"]).casefold()].append(box)
        for ref in references:
            if not (ref.bare and (ref.func, ref.arg) in KEY_SLOTS):
                continue
            box = _bounded(ref.ref)
            if box is None:
                continue
            key = (ref.sheet or item["sheet"]).casefold()
            # Only the searched column or row of a lookup table is a key;
            # VLOOKUP's other columns are what it returns.
            found: tuple[Box, ...] | None = tuple(returns[key]) or None
            if ref.func == "VLOOKUP":
                found = ((box[0] + 1, box[1], box[2], box[3]),) if box[2] > box[0] else None
                box = (box[0], box[1], box[0], box[3])
            elif ref.func == "HLOOKUP":
                found = ((box[0], box[1] + 1, box[2], box[3]),) if box[3] > box[1] else None
                box = (box[0], box[1], box[2], box[1])
            horizontal = ref.func == "HLOOKUP" or (box[1] == box[3] and box[2] > box[0])
            start = _START_ROW_RE.match(ref.ref)
            moving_start = (
                not horizontal
                and box[3] > box[1]
                and key == item["sheet"].casefold()
                and start is not None
                and not start.group(1)
                and int(start.group(2)) == item["row"] + 1
            )
            self._searched[key].add(SearchedRange(box, horizontal, moving_start, found))

    def searched_ranges(self, sheet: str) -> list[SearchedRange]:
        """The ranges first-match lookups search on ``sheet``; a range nested in a wider one is dropped.

        A repeat inside the narrower range is inside the wider one too, so a
        growing range (``$B$4:$B4`` filled down) costs one pass, not one per row.
        """
        # Ranges along one column (or row) are intervals; sorted by start, and
        # longest first, an interval ends inside the widest one before it
        # exactly when it is nested in it.
        lines: dict[tuple, list[SearchedRange]] = defaultdict(list)
        for searched in self._searched.get(sheet.casefold(), ()):
            box = searched.box
            across = (box[1], box[3]) if searched.horizontal else (box[0], box[2])
            lines[(searched.horizontal, searched.moving_start, across)].append(searched)
        kept: list[SearchedRange] = []
        for (horizontal, _moving, _across), ranges in sorted(lines.items()):
            span = (lambda r: (r.box[0], r.box[2])) if horizontal else (lambda r: (r.box[1], r.box[3]))
            widest: SearchedRange | None = None
            for searched in sorted(ranges, key=lambda r: (span(r)[0], -span(r)[1])):
                if widest is not None and span(searched)[1] <= span(widest)[1]:
                    if widest.returns != searched.returns:
                        # Read the returns of both: an unknown return wins.
                        merged = None if widest.returns is None or searched.returns is None else tuple(
                            dict.fromkeys(widest.returns + searched.returns)
                        )
                        widest = SearchedRange(widest.box, widest.horizontal, widest.moving_start, merged)
                        kept[-1] = widest
                    continue
                widest = searched
                kept.append(searched)
        return kept

    def contains(self, sheet: str, row: int, col: int) -> bool:
        """True when some formula reads the cell at (row, col) on ``sheet``."""
        column_index = self._all.get(sheet.casefold())
        return bool(column_index and column_index.covers(row, col))

    def numeric_contains(self, sheet: str, row: int, col: int) -> bool:
        """True when a formula consumes the cell at (row, col) as a number (arithmetic, SUM, ...)."""
        column_index = self._numeric.get(sheet.casefold())
        return bool(column_index and column_index.covers(row, col))

    def unconverted_contains(self, sheet: str, row: int, col: int) -> bool:
        """True when a formula consumes the cell as a number without converting it first.

        ``--A1``, ``A1*1`` and ``A1+0`` read a number stored as text
        correctly; ``SUM(A1:A5)`` skips it and ``A1+B1`` relies on coercion.
        """
        column_index = self._unconverted.get(sheet.casefold())
        return bool(column_index and column_index.covers(row, col))

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
