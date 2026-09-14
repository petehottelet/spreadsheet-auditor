from __future__ import annotations

from collections import Counter, defaultdict

from openpyxl.utils.cell import get_column_letter

from .budget import tick
from .finding import Finding
from .formula_parser import ParsedReference, is_formula, parse_formula
from .reference_resolver import boundaries, cell_value, find_sheet


AGG_FUNCS = {"SUM", "AVERAGE", "COUNT", "COUNTA"}
SUBTOTAL_WORDS = {"total", "subtotal", "grand total", "sum"}


def _origin(cell: dict) -> tuple[str, int, int]:
    return (cell["sheet"], cell["row"], cell["col"])


def aggregate_ranges(formula: str, names=None, origin: tuple[str, int, int] | None = None) -> list[ParsedReference]:
    parsed = parse_formula(formula, names=names, origin=origin)
    if not parsed.functions.intersection(AGG_FUNCS):
        return []
    return [ref for ref in parsed.references if ref.is_range]


def _single_aggregate_range_size(formula: str, names=None, origin=None) -> int | None:
    ranges = aggregate_ranges(formula, names=names, origin=origin)
    if len(ranges) != 1:
        return None
    box = boundaries(ranges[0].ref)
    if box is None:
        return None
    min_col, min_row, max_col, max_row = box
    return (max_col - min_col + 1) * (max_row - min_row + 1)


def _contiguous_by(items: list[tuple[dict, int]], key: str) -> list[list[tuple[dict, int]]]:
    if not items:
        return []
    ordered = sorted(items, key=lambda it: it[0][key])
    segments = [[ordered[0]]]
    for item in ordered[1:]:
        if item[0][key] == segments[-1][-1][0][key] + 1:
            segments[-1].append(item)
        else:
            segments.append([item])
    return segments


def detect_range_length_mismatch(formula_cells: list[dict], names=None, budget=None) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[str] = set()

    sized: list[tuple[dict, int]] = []
    for cell in formula_cells:
        tick(budget)
        size = _single_aggregate_range_size(cell["formula"], names=names, origin=_origin(cell))
        if size is not None:
            sized.append((cell, size))

    by_row: dict[tuple[str, int], list[tuple[dict, int]]] = defaultdict(list)
    by_col: dict[tuple[str, int], list[tuple[dict, int]]] = defaultdict(list)
    for cell, size in sized:
        by_row[(cell["sheet"], cell["row"])].append((cell, size))
        by_col[(cell["sheet"], cell["col"])].append((cell, size))

    groups = [(items, "col", "row") for items in by_row.values()]
    groups += [(items, "row", "column") for items in by_col.values()]

    for items, sort_key, axis_name in groups:
        for segment in _contiguous_by(items, sort_key):
            if len(segment) < 3:
                continue
            sizes = [size for _, size in segment]
            counts = Counter(sizes)
            majority, count = counts.most_common(1)[0]
            if count < len(segment) - 1:
                continue
            for cell, size in segment:
                if size == majority or cell["location"] in seen:
                    continue
                seen.add(cell["location"])
                findings.append(
                    Finding(
                        rule_id="RANGE_LENGTH_MISMATCH",
                        severity="High",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=cell["location"],
                        title="Aggregate range length differs from peer formulas",
                        formula=cell["formula"],
                        evidence=[
                            f"This aggregate spans {size} cell(s) while peer formulas in this {axis_name} span {majority}."
                        ],
                        suggested_fix="Compare this aggregate range to adjacent peers and align the range boundaries unless the difference is intentional.",
                    )
                )
    return findings


def detect_range_issues(formula_wb, value_wb, formula_cells: list[dict], names=None, budget=None) -> list[Finding]:
    findings: list[Finding] = []
    for cell in formula_cells:
        tick(budget)
        for ref in aggregate_ranges(cell["formula"], names=names, origin=_origin(cell)):
            if not ref.bounded:
                continue
            title = find_sheet(formula_wb, ref.sheet or cell["sheet"])
            if title is None:
                continue
            ws = formula_wb[title]
            box = boundaries(ref.ref)
            if box is None:
                continue
            min_col, min_row, max_col, max_row = box
            findings.extend(_detect_exclusion(ws, cell, ref.ref, min_col, min_row, max_col, max_row))
            findings.extend(_detect_subtotal_inclusion(ws, cell, ref.ref, min_col, min_row, max_col, max_row))
            findings.extend(_detect_hidden_intersections(ws, cell, ref.ref, min_col, min_row, max_col, max_row))
    return findings


def _has_data(value) -> bool:
    if value is None:
        return False
    if is_formula(value):
        return True
    if isinstance(value, str) and value.strip() == "":
        return False
    return True


def _row_label(ws, row: int, min_col: int) -> str:
    labels = []
    for col in range(1, min_col):
        value = cell_value(ws, row, col)
        if value is not None:
            labels.append(str(value).strip())
    return " ".join(labels).lower()


def _detect_exclusion(ws, formula_cell: dict, ref_text: str, min_col: int, min_row: int, max_col: int, max_row: int):
    findings: list[Finding] = []
    loc = formula_cell["location"]
    formula = formula_cell["formula"]

    if min_col == max_col:
        candidates = []
        if min_row > 1:
            candidates.append((min_row - 1, min_col, "above"))
        if max_row + 1 < formula_cell["row"]:
            candidates.append((max_row + 1, min_col, "below"))
        for row, col, direction in candidates:
            neighbor_value = cell_value(ws, row, col)
            if _has_data(neighbor_value):
                label = _row_label(ws, row, min_col)
                if any(word in label for word in SUBTOTAL_WORDS):
                    continue
                coord = f"{get_column_letter(col)}{row}"
                findings.append(
                    Finding(
                        rule_id="RANGE_EXCLUSION",
                        severity="Critical",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=loc,
                        title="Aggregation range appears to exclude adjacent data row",
                        formula=formula,
                        evidence=[f"{ws.title}!{ref_text} excludes adjacent {direction} cell {ws.title}!{coord} with value {neighbor_value!r}."],
                        suggested_fix=f"Confirm whether {ws.title}!{coord} belongs in the aggregate, then extend the range if appropriate.",
                    )
                )
    if min_row == max_row:
        candidates = []
        if min_col > 1:
            candidates.append((min_row, min_col - 1, "left"))
        if max_col + 1 < formula_cell["col"]:
            candidates.append((min_row, max_col + 1, "right"))
        for row, col, direction in candidates:
            neighbor_value = cell_value(ws, row, col)
            if _has_data(neighbor_value):
                coord = f"{get_column_letter(col)}{row}"
                findings.append(
                    Finding(
                        rule_id="RANGE_EXCLUSION",
                        severity="Critical",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=loc,
                        title="Aggregation range appears to exclude adjacent data column",
                        formula=formula,
                        evidence=[f"{ws.title}!{ref_text} excludes adjacent {direction} cell {ws.title}!{coord} with value {neighbor_value!r}."],
                        suggested_fix=f"Confirm whether {ws.title}!{coord} belongs in the aggregate, then extend the range if appropriate.",
                    )
                )
    return findings


def _detect_subtotal_inclusion(ws, formula_cell: dict, ref_text: str, min_col: int, min_row: int, max_col: int, max_row: int):
    findings: list[Finding] = []
    for row in range(min_row, max_row + 1):
        label = _row_label(ws, row, min_col)
        if any(word in label for word in SUBTOTAL_WORDS):
            findings.append(
                Finding(
                    rule_id="RANGE_INCLUDES_SUBTOTAL",
                    severity="High",
                    error_confidence="Likely defect",
                    detection_mode="DET",
                    location=formula_cell["location"],
                    title="Aggregation range appears to include subtotal or total row",
                    formula=formula_cell["formula"],
                    evidence=[f"{ws.title}!{ref_text} includes row {row}, labeled {label!r}."],
                    suggested_fix="Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.",
                )
            )
    return findings


def _row_hidden(ws, row: int) -> bool:
    dim = ws.row_dimensions.get(row)
    return bool(dim is not None and dim.hidden)


def _col_hidden(ws, col: int) -> bool:
    dim = ws.column_dimensions.get(get_column_letter(col))
    return bool(dim is not None and dim.hidden)


def _detect_hidden_intersections(ws, formula_cell: dict, ref_text: str, min_col: int, min_row: int, max_col: int, max_row: int):
    hidden_rows = [row for row in range(min_row, max_row + 1) if _row_hidden(ws, row)]
    hidden_cols = [get_column_letter(col) for col in range(min_col, max_col + 1) if _col_hidden(ws, col)]
    if not hidden_rows and not hidden_cols:
        return []
    pieces = []
    if hidden_rows:
        pieces.append(f"hidden rows {hidden_rows}")
    if hidden_cols:
        pieces.append(f"hidden columns {hidden_cols}")
    return [
        Finding(
            rule_id="HIDDEN_STRUCTURE_IN_TOTAL",
            severity="Medium",
            error_confidence="Review",
            detection_mode="DET",
            location=formula_cell["location"],
            title="Aggregate includes hidden structure",
            formula=formula_cell["formula"],
            evidence=[f"{ws.title}!{ref_text} intersects " + ", ".join(pieces) + "."],
            suggested_fix="Confirm hidden inputs are intentional and disclosed in visible workbook documentation.",
        )
    ]


def detect_literal_constants(formula_cells: list[dict], budget=None) -> list[Finding]:
    findings: list[Finding] = []
    for cell in formula_cells:
        tick(budget)
        literals = parse_formula(cell["formula"]).numeric_literals
        if literals:
            findings.append(
                Finding(
                    rule_id="LITERAL_CONSTANT",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula contains embedded numeric literal",
                    formula=cell["formula"],
                    evidence=[f"Non-trivial numeric literal(s) found: {', '.join(literals)}."],
                    suggested_fix="Move the assumption to a labeled input cell and reference it from the formula.",
                )
            )
    return findings


def detect_fragile_functions(formula_cells: list[dict], names=None, budget=None) -> list[Finding]:
    findings: list[Finding] = []
    volatile = {"OFFSET", "INDIRECT", "NOW", "RAND", "RANDBETWEEN", "TODAY"}
    for cell in formula_cells:
        tick(budget)
        parsed = parse_formula(cell["formula"], names=names, origin=_origin(cell))
        found = parsed.functions.intersection(volatile)
        if found:
            findings.append(
                Finding(
                    rule_id="VOLATILE_FUNCTION",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula uses volatile or fragile function",
                    formula=cell["formula"],
                    evidence=[f"Function(s) found: {', '.join(sorted(found))}."],
                    suggested_fix="Confirm the volatility is intentional; prefer stable bounded references when possible.",
                )
            )
        if any(not ref.bounded for ref in parsed.references):
            findings.append(
                Finding(
                    rule_id="WHOLE_COLUMN_REFERENCE",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula references an entire column",
                    formula=cell["formula"],
                    evidence=["Whole-column references can hide range and performance issues."],
                    suggested_fix="Use a bounded range sized to the actual table.",
                )
            )
    return findings
