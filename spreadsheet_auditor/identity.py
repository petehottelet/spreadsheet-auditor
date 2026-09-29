"""Identify findings by what the flagged cell holds, not by its address.

A fingerprint over (rule, location) changes whenever a row or column is
inserted above or left of the finding, and a suppression written for one
address then hides whatever lands there next. The identity built here uses
the flagged cell's sheet, its row label (the first text in its row, reading
from column A), and its content: a formula rewritten relative to its own
cell, so ``=A5*B5`` in C5 and ``=A6*B6`` in C6 agree, or a constant's value.
Findings of one rule that share all three are numbered in sheet order, which
inserted rows and columns do not change.
"""

from __future__ import annotations

from collections import defaultdict

from .formula_parser import normalize_formula
from .locations import anchor
from .reference_resolver import existing_cell


def _row_label(ws, row: int, col: int) -> str:
    for column in range(1, col):
        cell = existing_cell(ws, row, column)
        value = None if cell is None else cell.value
        if isinstance(value, str) and value.strip() and not value.startswith("="):
            return value.strip()
    return ""


def _content(ws, row: int, col: int) -> str:
    cell = existing_cell(ws, row, col)
    value = None if cell is None else cell.value
    text = getattr(value, "text", value)  # array formulas carry their text on .text
    if isinstance(text, str) and text.startswith("="):
        return normalize_formula(text, row, col)
    return "" if value is None else f"{type(value).__name__}:{value}"


def assign_identities(findings, formula_wb) -> None:
    """Set ``finding.identity`` for every finding anchored on a workbook cell.

    Findings whose location names no sheet of the workbook keep the
    location-based fingerprint.
    """
    groups: dict[tuple[str, str], list[tuple[tuple[int, int, str], object]]] = defaultdict(list)
    sheets = set(formula_wb.sheetnames)
    for finding in findings:
        spot = anchor(finding.location)
        if spot is None or spot[0] not in sheets:
            continue
        sheet, row, col = spot
        ws = formula_wb[sheet]
        key = f"{sheet.casefold()}|{_row_label(ws, row, col)}|{_content(ws, row, col)}"
        groups[(finding.rule_id, key)].append(((row, col, finding.location), finding))
    for (_rule, key), members in groups.items():
        for ordinal, (_position, finding) in enumerate(sorted(members, key=lambda m: m[0]), start=1):
            finding.identity = f"{key}|{ordinal}"
