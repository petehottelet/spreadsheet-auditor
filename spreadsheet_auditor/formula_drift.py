from __future__ import annotations

from bisect import bisect_left
from collections import Counter, defaultdict

from .budget import tick
from .finding import Finding
from .formula_parser import formula_text, is_formula, normalize_formula, parse_formula
from .range_checks import is_total_of_segment
from .reference_resolver import boundaries
from .workbook_inventory import iter_existing_cells, location

# A plug is a few constants interrupting a formula run, not a block of inputs.
MAX_PLUG_GAP = 3


def _is_plain_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def detect_formula_drift(formula_cells: list[dict], budget=None, names=None) -> list[Finding]:
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
            fixed = segment[0]["row"] if axis == "row" else segment[0]["col"]
            low, high = segment[0][key], segment[-1][key]
            members = [c for c in segment if not is_total_of_segment(c, axis, fixed, low, high, names)]
            if len(members) < 3:
                continue
            patterns = [normalize_formula(c["formula"], c["row"], c["col"]) for c in members]
            counts = Counter(patterns)
            majority, count = counts.most_common(1)[0]
            if count < len(members) - 1:
                continue
            for idx, (cell, pattern) in enumerate(zip(members, patterns)):
                if pattern == majority or cell["location"] in seen:
                    continue
                seen.add(cell["location"])
                neighbors = _drift_neighbors(members, idx)
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


def _aggregates_over(text: str, origin: tuple[int, int], sheet: str, target: tuple[int, int], names) -> bool:
    """True when the formula at ``origin`` sums a range that contains ``target``."""
    parsed = parse_formula(text, names=names, origin=(sheet, origin[0], origin[1]))
    for ref in parsed.references:
        if not ref.is_range or not ref.bounded:
            continue
        if (ref.sheet or sheet).casefold() != sheet.casefold():
            continue
        box = boundaries(ref.ref)
        if box is None:
            continue
        min_col, min_row, max_col, max_row = box
        if min_row <= target[0] <= max_row and min_col <= target[1] <= max_col:
            return True
    return False


def detect_hardcode_breaks(
    formula_wb,
    allowed_sheet_names: set[str] | None = None,
    budget=None,
    names=None,
) -> list[Finding]:
    """Flag constants that interrupt a run of formulas sharing one relative pattern.

    A plug replaces a formula: the formulas on either side of it (within a
    short gap) normalize to the same pattern. Inputs that an adjacent subtotal
    sums are not plugs, however many formulas surround them.
    """
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
            _hardcode_breaks_in_line(values, ws.title, row, None, seen, findings, names)
        for col, values in by_col.items():
            tick(budget)
            _hardcode_breaks_in_line(values, ws.title, None, col, seen, findings, names)
    return findings


def _hardcode_breaks_in_line(
    values: dict[int, object],
    sheet: str,
    row: int | None,
    col: int | None,
    seen: set[str],
    findings: list[Finding],
    names,
) -> None:
    keys = sorted(values)
    formula_keys = [key for key in keys if is_formula(values[key])]
    if len(formula_keys) < 2:
        return

    def position(key: int) -> tuple[int, int]:
        return (row, key) if row is not None else (key, col)  # type: ignore[return-value]

    for key in keys:
        value = values[key]
        if not _is_plain_number(value):
            continue
        idx = bisect_left(formula_keys, key)
        if idx == 0 or idx >= len(formula_keys):
            continue
        left, right = formula_keys[idx - 1], formula_keys[idx]
        if right - left - 1 > MAX_PLUG_GAP:
            continue
        left_pos, right_pos, cell_pos = position(left), position(right), position(key)
        left_text = formula_text(values[left])
        right_text = formula_text(values[right])
        if left_text is None or right_text is None:
            continue
        pattern = normalize_formula(left_text, *left_pos)
        if pattern != normalize_formula(right_text, *right_pos):
            continue
        if _aggregates_over(left_text, left_pos, sheet, cell_pos, names) or _aggregates_over(
            right_text, right_pos, sheet, cell_pos, names
        ):
            continue
        loc = location(sheet, *cell_pos)
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
                evidence=[
                    f"Value {value!r} sits between {location(sheet, *left_pos)} and {location(sheet, *right_pos)}, "
                    f"which share the pattern {pattern}."
                ],
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
