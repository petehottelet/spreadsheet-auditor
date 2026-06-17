from __future__ import annotations

from collections import Counter, defaultdict

from finding import Finding
from formula_parser import is_formula, normalize_formula
from workbook_inventory import location


def detect_formula_drift(formula_cells: list[dict]) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()

    by_row: dict[tuple[str, int], list[dict]] = defaultdict(list)
    by_col: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for cell in formula_cells:
        by_row[(cell["sheet"], cell["row"])].append(cell)
        by_col[(cell["sheet"], cell["col"])].append(cell)

    for cells, axis in [(values, "row") for values in by_row.values()] + [(values, "column") for values in by_col.values()]:
        key = "col" if axis == "row" else "row"
        for segment in _contiguous_segments(sorted(cells, key=lambda c: c[key]), key):
            if len(segment) < 3:
                continue
            patterns = [
                normalize_formula(c["formula"], c["row"], c["col"])
                for c in segment
            ]
            counts = Counter(patterns)
            majority, count = counts.most_common(1)[0]
            if count < len(segment) - 1:
                continue
            for cell, pattern in zip(segment, patterns):
                if pattern == majority or cell["location"] in seen:
                    continue
                seen.add(cell["location"])
                findings.append(
                    Finding(
                        rule_id="FORMULA_DRIFT",
                        severity="High",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=cell["location"],
                        title="Formula breaks neighboring pattern",
                        formula=cell["formula"],
                        evidence=[f"Formula differs from the dominant relative pattern in this {axis}."],
                        suggested_fix="Compare this formula to adjacent formulas and restore the intended relative references.",
                    )
                )
    return findings


def detect_hardcode_breaks(formula_wb, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()
    for ws in formula_wb.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        for row in range(1, ws.max_row + 1):
            values = [ws.cell(row=row, column=col).value for col in range(1, ws.max_column + 1)]
            _hardcode_breaks_in_sequence(values, ws.title, row, None, seen, findings)
        for col in range(1, ws.max_column + 1):
            values = [ws.cell(row=row, column=col).value for row in range(1, ws.max_row + 1)]
            _hardcode_breaks_in_sequence(values, ws.title, None, col, seen, findings)
    return findings


def _hardcode_breaks_in_sequence(values, sheet, row, col, seen, findings):
    formula_indexes = [idx for idx, value in enumerate(values) if is_formula(value)]
    if len(formula_indexes) < 2:
        return
    start, end = min(formula_indexes), max(formula_indexes)
    for idx in range(start, end + 1):
        value = values[idx]
        if value is None or is_formula(value) or isinstance(value, str):
            continue
        r = row if row is not None else idx + 1
        c = col if col is not None else idx + 1
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
