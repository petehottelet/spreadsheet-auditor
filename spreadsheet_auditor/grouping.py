"""Collapse per-cell findings that repeat one formula pattern into one finding per pattern.

A formula filled across a block normalizes to a single relative pattern. A
rule that fires on the pattern (an embedded literal, an IFERROR wrapper, a
volatile function) would otherwise fire once per cell, and a schedule sheet
turns into hundreds of identical findings. Reporting the pattern once, at its
first cell, with the other cells listed as evidence, keeps the location
suppressible and the report readable.
"""

from __future__ import annotations

from .formula_parser import normalize_formula

MAX_SHOWN = 8


def group_by_pattern(cells: list[dict]) -> list[list[dict]]:
    """Group formula cells by (sheet, relative formula pattern), keeping input order.

    The first cell of each group leads it; the formula inventory is in sheet
    order, so that is the top-left cell of the block.
    """
    groups: dict[tuple[str, str], list[dict]] = {}
    for cell in cells:
        key = (cell["sheet"], normalize_formula(cell["formula"], cell["row"], cell["col"]))
        groups.setdefault(key, []).append(cell)
    return list(groups.values())


def pattern_note(members: list[dict]) -> str | None:
    """Evidence line naming the other cells that share the leading cell's pattern."""
    if len(members) < 2:
        return None
    others = [cell["location"] for cell in members[1:]]
    shown = ", ".join(others[:MAX_SHOWN]) + (", ..." if len(others) > MAX_SHOWN else "")
    return f"The same relative formula appears in {len(members)} cells on this sheet; the others are {shown}."
