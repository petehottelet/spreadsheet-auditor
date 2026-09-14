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
    pattern_at: dict[tuple[str, int, int], str] = {}
    for cell in formula_cells:
        by_row[(cell["sheet"], cell["row"])].append(cell)
        by_col[(cell["sheet"], cell["col"])].append(cell)
        pattern_at[(cell["sheet"], cell["row"], cell["col"])] = normalize_formula(
            cell["formula"], cell["row"], cell["col"]
        )

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
            patterns = [pattern_at[(c["sheet"], c["row"], c["col"])] for c in members]
            counts = Counter(patterns)
            majority, count = counts.most_common(1)[0]
            if "#REF!" in majority:
                continue
            pairs = list(zip(members, patterns))
            # The seed of a chain (an opening balance, year 0 of a projection)
            # links to its source while every later cell builds on the
            # previous one; it is expected to differ and is not a member.
            if pairs[0][1] != majority and _chain_step(majority, axis, -1):
                pairs = pairs[1:]
            if pairs and pairs[-1][1] != majority and _chain_step(majority, axis, 1):
                pairs = pairs[:-1]
            if len(pairs) < 3 or count < len(pairs) - 1:
                continue
            for cell, pattern in pairs:
                if pattern == majority or cell["location"] in seen:
                    continue
                if _conforms_across(cell, pattern, axis, pattern_at):
                    continue
                seen.add(cell["location"])
                neighbors = _drift_neighbors(members, members.index(cell))
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


def _conforms_across(cell: dict, pattern: str, axis: str, pattern_at: dict[tuple[str, int, int], str]) -> bool:
    """True when the cell's formula matches its formula neighbours on the other axis.

    A row of unrelated columns (a label link, a derived column, a mirror
    column) is not a fill. The cell that differs from the two beside it but
    agrees with the cells above and below it is a different column by design,
    not a broken pattern. The price is a column that was filled down wrongly
    in every row, which then reads as consistent; the column scan still sees
    it when the column's own pattern breaks.
    """
    if axis == "row":
        keys = [(cell["sheet"], cell["row"] - 1, cell["col"]), (cell["sheet"], cell["row"] + 1, cell["col"])]
    else:
        keys = [(cell["sheet"], cell["row"], cell["col"] - 1), (cell["sheet"], cell["row"], cell["col"] + 1)]
    found = [pattern_at[key] for key in keys if key in pattern_at]
    return bool(found) and all(other == pattern for other in found)


def _chain_step(majority: str, axis: str, direction: int) -> bool:
    """True when the dominant pattern reads the neighbouring cell one step back along the axis.

    ``direction`` -1 means each cell builds on its predecessor (a running
    balance, a projection), so the first cell of the run is the seed; 1 means
    the run chains the other way and the last cell is the seed.
    """
    if axis == "row":
        token = "RC[-1]" if direction < 0 else "RC[1]"
    else:
        token = "R[-1]C" if direction < 0 else "R[1]C"
    return token in majority


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
            _hardcode_breaks_in_line(values, ws.title, row, None, seen, findings, names, by_row)
        for col, values in by_col.items():
            tick(budget)
            _hardcode_breaks_in_line(values, ws.title, None, col, seen, findings, names, by_row)
    return findings


def _is_input_line(
    by_row: dict[int, dict[int, object]],
    cell_pos: tuple[int, int],
    left_pos: tuple[int, int],
    right_pos: tuple[int, int],
) -> bool:
    """True when the constant belongs to a line of inputs between two lines of formulas.

    An input column between two running-sum columns, or an input row between
    two ratio rows, puts a constant between two formulas that share a pattern
    on every line. The tell is the other axis: the constant's neighbours
    there are constants too, while the formulas' neighbours are formulas.
    """

    def at(row: int, col: int):
        return by_row.get(row, {}).get(col)

    row, col = cell_pos
    across = left_pos[0] == row  # the formula pair lies in this row
    matched = False
    for step in (-1, 1):
        if across:  # look up and down
            beside = at(row + step, col)
            corners = [at(row + step, left_pos[1]), at(row + step, right_pos[1])]
        else:  # look left and right
            beside = at(row, col + step)
            corners = [at(left_pos[0], col + step), at(right_pos[0], col + step)]
        if is_formula(beside):
            return False
        if _is_plain_number(beside):
            if not all(is_formula(v) for v in corners):
                return False
            matched = True
        # A header, a label or the edge of the block beside the constant says
        # nothing either way.
    return matched


def _hardcode_breaks_in_line(
    values: dict[int, object],
    sheet: str,
    row: int | None,
    col: int | None,
    seen: set[str],
    findings: list[Finding],
    names,
    by_row: dict[int, dict[int, object]],
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
        if any(isinstance(values.get(k), str) and not is_formula(values[k]) for k in range(left + 1, right)):
            continue  # a text label between the two formulas ends one block and starts another
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
        if _is_input_line(by_row, cell_pos, left_pos, right_pos):
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
