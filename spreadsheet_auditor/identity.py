"""Identify findings by what the flagged cell holds, not by its address.

A fingerprint over (rule, location) changes whenever a row or column is
inserted above or left of the finding, and a suppression written for one
address then hides whatever lands there next. The identity built here uses
the flagged cell's sheet, its row label (the first text in its row, reading
from column A), its column label (the first text in its column, reading down
from row 1), and its content: a formula rewritten relative to its own cell,
so ``=A5*B5`` in C5 and ``=A6*B6`` in C6 agree, with absolute coordinates and
other sheets' addresses left out, or a constant's value. A finding that
stands for several cells also carries the labels of all of them, so a cell
joining or leaving the group changes it.

Findings of one rule that still share all of that are numbered in sheet
order, with their count ("2/3"), and marked ``identity_shared``: a new one
could take an old one's number, so a pinned suppression must match their
address too, and any change to the set changes all their identities.
"""

from __future__ import annotations

from collections import defaultdict

from openpyxl.worksheet.formula import DataTableFormula

from .formula_parser import normalize_formula
from .locations import anchor
from .reference_resolver import existing_cell
from .workbook_inventory import iter_existing_cells


class _Labels:
    """The first text of each row and each column of one sheet, read once."""

    def __init__(self, ws) -> None:
        self.by_row: dict[int, tuple[int, str]] = {}
        self.by_col: dict[int, tuple[int, str]] = {}
        for cell in iter_existing_cells(ws):
            value = cell.value
            if not (isinstance(value, str) and value.strip() and not value.startswith("=")):
                continue
            text = value.strip()
            if cell.row not in self.by_row or cell.column < self.by_row[cell.row][0]:
                self.by_row[cell.row] = (cell.column, text)
            if cell.column not in self.by_col or cell.row < self.by_col[cell.column][0]:
                self.by_col[cell.column] = (cell.row, text)

    def of(self, row: int, col: int) -> str:
        """``row label|column label``: text left of the cell in its row, and above it in its column."""
        left = self.by_row.get(row)
        above = self.by_col.get(col)
        return f"{left[1] if left and left[0] < col else ''}|{above[1] if above and above[0] < row else ''}"


def _content(ws, row: int, col: int) -> str:
    cell = existing_cell(ws, row, col)
    value = None if cell is None else cell.value
    if isinstance(value, DataTableFormula):
        # Its default text names the object's memory address, new every run.
        parts = [f"{key}={val}" for key, val in value if key not in {"ref", "r1", "r2"}]
        inputs = [normalize_formula(f"={val}", row, col, stable=True) for val in (value.r1, value.r2) if val]
        return "dataTable:" + ",".join(parts + inputs)
    text = getattr(value, "text", value)  # array formulas carry their text on .text
    if isinstance(text, str) and text.startswith("="):
        return normalize_formula(text, row, col, stable=True)
    return "" if value is None else f"{type(value).__name__}:{value}"


def assign_identities(findings, formula_wb) -> None:
    """Set ``finding.identity`` for every finding anchored on a workbook cell.

    Findings whose location names no sheet of the workbook keep the
    location-based fingerprint.
    """
    groups: dict[tuple[str, str], list[tuple[tuple[int, int, str], object]]] = defaultdict(list)
    sheets = set(formula_wb.sheetnames)
    labels: dict[str, _Labels] = {}

    def labels_of(sheet: str) -> _Labels:
        if sheet not in labels:
            labels[sheet] = _Labels(formula_wb[sheet])
        return labels[sheet]

    for finding in findings:
        spot = anchor(finding.location)
        if spot is None or spot[0] not in sheets:
            continue
        sheet, row, col = spot
        key = f"{sheet.casefold()}|{labels_of(sheet).of(row, col)}|{_content(formula_wb[sheet], row, col)}"
        if len(finding.members) > 1:
            member_labels = []
            for member in finding.members:
                where = anchor(member)
                if where is not None and where[0] in sheets:
                    member_labels.append(f"{where[0].casefold()}|{labels_of(where[0]).of(where[1], where[2])}")
            key += "|cells:" + ";".join(sorted(member_labels))
        if finding.identity_hint:
            key += f"|{finding.identity_hint}"
        groups[(finding.rule_id, key)].append(((row, col, finding.location), finding))
    for (_rule, key), members in groups.items():
        # "2/3": the second of three alike. Counting them means a finding that
        # is added or fixed changes the others' identities too, so an accepted
        # one's number never passes to a newcomer or to the one left over.
        count = f"/{len(members)}" if len(members) > 1 else ""
        for ordinal, (_position, finding) in enumerate(sorted(members, key=lambda m: m[0]), start=1):
            finding.identity = f"{key}|{ordinal}{count}"
            finding.identity_shared = len(members) > 1
