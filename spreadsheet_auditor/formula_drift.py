from __future__ import annotations

from collections import Counter, defaultdict

from .budget import tick
from .finding import Finding
from .formula_parser import is_formula, normalize_formula
from .workbook_inventory import iter_existing_cells, location


def detect_formula_drift(formula_cells: list[dict], budget=None) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()

    by_row: dict[tuple[str, int], list[dict]] = defaultdict(list)
    by_col: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for cell in formula_cells:
        by_row[(cell["sheet"], cell["row"])].append(cell)
        by_col[(cell["sheet"], cell["col"])].append(cell)

    groups = [(values, "row") for values in by_row.values()]
    groups += [(values, "column") for values in by_col.values()]
    for cells, axis in groups:
        key = "col" if axis == "row" else "row"
        for segment in _contiguous_segments(sorted(cells, key=lambda c: c[key]), key):
            tick(budget)
            if len(segment) < 3:
                continue
            patterns = [normalize_formula(c["formula"], c["row"], c["col"]) for c in segment]
            counts = Counter(patterns)
            majority, count = counts.most_common(1)[0]
            if count < len(segment) - 1:
                continue
            for idx, (cell, pattern) in enumerate(zip(segment, patterns)):
                if pattern == majority or cell["location"] in seen:
                    continue
                seen.add(cell["location"])
                neighbors = _drift_neighbors(segment, idx)
                evidence = [
                    f"Formula differs from the dominant relative pattern in this {axis}.",
                    f"Dominant pattern (n={count}): {majority}",
                    f"This cell: {pattern}",
                ]
                if neighbors:
                    evidence.append("Neighboring formulas: " + "; ".join(neighbors))
                findings.append(
                    Finding(
                        rule_id="FORMULA_DRIFT",
                        severity="High",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=cell["location"],
                        title="Formula breaks neighboring pattern",
                        formula=cell["formula"],
                        evidence=evidence,
                        suggested_fix="Compare this formula to adjacent formulas and restore the intended relative references.",
                    )
                )
    return findings


def _drift_neighbors(segment: list[dict], idx: int, radius: int = 1) -> list[str]:
    """Return up to 2*radius adjacent formulas (with their locations) for evidence."""
    neighbors: list[str] = []
    start = max(0, idx - radius)
    end = min(len(segment), idx + radius + 1)
    for j in range(start, end):
        if j == idx:
            continue
        cell = segment[j]
        neighbors.append(f"{cell['location']}={cell['formula']}")
    return neighbors


def detect_hardcode_breaks(formula_wb, allowed_sheet_names: set[str] | None = None, budget=None) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()
    for ws in formula_wb.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        by_row: dict[int, dict[int, object]] = defaultdict(dict)
        by_col: dict[int, dict[int, object]] = defaultdict(dict)
        for cell in iter_existing_cells(ws):
            if cell.value is None:
                continue
            by_row[cell.row][cell.column] = cell.value
            by_col[cell.column][cell.row] = cell.value
        for row, values in by_row.items():
            tick(budget)
            _hardcode_breaks_in_line(values, ws.title, row, None, seen, findings)
        for col, values in by_col.items():
            tick(budget)
            _hardcode_breaks_in_line(values, ws.title, None, col, seen, findings)
    return findings


def _hardcode_breaks_in_line(values: dict[int, object], sheet: str, row: int | None, col: int | None, seen, findings) -> None:
    formula_keys = [key for key, value in values.items() if is_formula(value)]
    if len(formula_keys) < 2:
        return
    start, end = min(formula_keys), max(formula_keys)
    for key in sorted(values):
        if key <= start or key >= end:
            continue
        value = values[key]
        if is_formula(value) or isinstance(value, str):
            continue
        r = row if row is not None else key
        c = col if col is not None else key
        loc = location(sheet, r, c)
        if loc in seen:
            continue
        seen.add(loc)
        findings.append(
            Finding(
                rule_id="HARDCODE_IN_FORMULA_BLOCK",
                severity="High",
                error_confidence="Likely defect",
                detection_mode="DET",
                location=loc,
                title="Hardcoded value inside formula block",
                formula=None,
                evidence=[f"Value {value!r} sits between formulas in the same row or column."],
                suggested_fix="Confirm whether this is an intentional plug. If not, restore the formula pattern.",
            )
        )


def _contiguous_segments(cells: list[dict], key: str) -> list[list[dict]]:
    if not cells:
        return []
    segments = [[cells[0]]]
    for cell in cells[1:]:
        if cell[key] == segments[-1][-1][key] + 1:
            segments[-1].append(cell)
        else:
            segments.append([cell])
    return segments
