from __future__ import annotations

from collections import defaultdict

from openpyxl.formula.tokenizer import Token
from openpyxl.utils.cell import get_column_letter

from .budget import tick
from .finding import Finding
from .formula_parser import extract_functions, formula_text, split_sheet, tokens
from .range_checks import AGG_FUNCS, aggregate_ranges
from .reference_resolver import (
    EXCEL_MAX_COL,
    EXCEL_MAX_ROW,
    boundaries,
    cell_value,
    find_sheet,
    raw_boundaries,
)
from .workbook_inventory import iter_existing_cells

Box = tuple[int, int, int, int]
TokenTriple = tuple[str, str, str]


def _numeric(value) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _is_aggregate_formula(value) -> bool:
    text = formula_text(value)
    return bool(text) and bool(extract_functions(text).intersection(AGG_FUNCS))


# --- token helpers -----------------------------------------------------------


def _significant(toks) -> list[TokenTriple]:
    return [tok for tok in toks if tok[1] != Token.WSPACE]


def _opens(tok: TokenTriple) -> bool:
    return tok[2] == Token.OPEN and tok[1] in (Token.FUNC, Token.PAREN, Token.ARRAY)


def _closes(tok: TokenTriple) -> bool:
    return tok[2] == Token.CLOSE and tok[1] in (Token.FUNC, Token.PAREN, Token.ARRAY)


def _bare_sum_range(toks) -> str | None:
    """Return the range text when ``toks`` is exactly ``SUM(<range>)`` (optionally ``+SUM(...)``)."""
    sig = _significant(toks)
    if sig and sig[0][1] == Token.OP_PRE and sig[0][0] == "+":
        sig = sig[1:]
    if (
        len(sig) == 3
        and sig[0][1] == Token.FUNC
        and sig[0][2] == Token.OPEN
        and sig[0][0].upper() == "SUM("
        and sig[1][1] == Token.OPERAND
        and sig[1][2] == Token.RANGE
        and sig[2][1] == Token.FUNC
        and sig[2][2] == Token.CLOSE
    ):
        return sig[1][0]
    return None


def _ref_box(text: str, default_sheet: str) -> tuple[str, Box] | None:
    sheet, rest = split_sheet(text.lstrip("@"))
    raw = raw_boundaries(rest)
    if raw is None:
        return None
    min_col, min_row, max_col, max_row = raw
    return (
        (sheet or default_sheet).casefold(),
        (
            min_col or 1,
            min_row or 1,
            EXCEL_MAX_COL if max_col is None else max_col,
            EXCEL_MAX_ROW if max_row is None else max_row,
        ),
    )


def _is_single_cell(box: Box) -> bool:
    return box[0] == box[2] and box[1] == box[3]


def _inside(inner: Box, outer: Box) -> bool:
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]


def _additive_terms(toks) -> list[tuple[str, list[TokenTriple]]]:
    """Split a formula into top-level ``+``/``-`` terms as ``(sign, tokens)``."""
    terms: list[tuple[str, list[TokenTriple]]] = []
    current: list[TokenTriple] = []
    sign = "+"
    depth = 0
    for tok in _significant(toks):
        value, ttype, _subtype = tok
        if _opens(tok):
            depth += 1
            current.append(tok)
            continue
        if _closes(tok):
            depth -= 1
            current.append(tok)
            continue
        if depth == 0 and ttype == Token.OP_IN and value in ("+", "-"):
            terms.append((sign, current))
            current = []
            sign = value
            continue
        if depth == 0 and ttype == Token.OP_PRE and value in ("+", "-") and not current:
            if value == "-":
                sign = "-" if sign == "+" else "+"
            continue
        current.append(tok)
    terms.append((sign, current))
    return [(term_sign, term) for term_sign, term in terms if term]


def _sum_call_args(toks) -> list[list[list[TokenTriple]]]:
    """Argument token lists of every ``SUM(...)`` call in the formula."""
    sig = _significant(toks)
    calls: list[list[list[TokenTriple]]] = []
    for start, tok in enumerate(sig):
        if not (tok[1] == Token.FUNC and tok[2] == Token.OPEN and tok[0].upper() == "SUM("):
            continue
        depth = 1
        args: list[list[TokenTriple]] = [[]]
        for inner in sig[start + 1 :]:
            if _opens(inner):
                depth += 1
            elif _closes(inner):
                depth -= 1
                if depth == 0:
                    break
            elif depth == 1 and inner[1] == Token.SEP and inner[2] == Token.ARG:
                args.append([])
                continue
            args[-1].append(inner)
        calls.append([arg for arg in args if arg])
    return calls


def _single_operand(term: list[TokenTriple]) -> str | None:
    if len(term) == 1 and term[0][1] == Token.OPERAND and term[0][2] == Token.RANGE:
        return term[0][0]
    return None


def double_counted_cells(formula: str, default_sheet: str) -> list[tuple[str, str]]:
    """Return ``(cell, range)`` pairs where the formula adds a cell that a SUM already covers.

    Catches both ``=SUM(B2:B5)+B5`` and ``=SUM(B2:B5,B5)``. Subtraction is left
    alone: ``=SUM(B2:B5)-B3`` is a normal "total excluding X".
    """
    toks = tokens(formula)
    if toks is None:
        return []
    hits: list[tuple[str, str]] = []

    sum_ranges: list[str] = []
    plus_cells: list[str] = []
    for sign, term in _additive_terms(toks):
        range_text = _bare_sum_range(term)
        if range_text is not None:
            if sign == "+":
                sum_ranges.append(range_text)
            continue
        operand = _single_operand(term)
        if sign == "+" and operand is not None:
            plus_cells.append(operand)
    for range_text in sum_ranges:
        resolved_range = _ref_box(range_text, default_sheet)
        if resolved_range is None or _is_single_cell(resolved_range[1]):
            continue
        for cell_text in plus_cells:
            resolved_cell = _ref_box(cell_text, default_sheet)
            if (
                resolved_cell is not None
                and _is_single_cell(resolved_cell[1])
                and resolved_cell[0] == resolved_range[0]
                and _inside(resolved_cell[1], resolved_range[1])
            ):
                hits.append((cell_text, range_text))

    for args in _sum_call_args(toks):
        operands = [text for text in (_single_operand(arg) for arg in args) if text is not None]
        resolved = [(text, _ref_box(text, default_sheet)) for text in operands]
        ranges = [(text, box) for text, box in resolved if box is not None and not _is_single_cell(box[1])]
        cells = [(text, box) for text, box in resolved if box is not None and _is_single_cell(box[1])]
        for cell_text, cell_box in cells:
            for range_text, range_box in ranges:
                if cell_box[0] == range_box[0] and _inside(cell_box[1], range_box[1]):
                    hits.append((cell_text, range_text))
    return hits


# --- detectors ---------------------------------------------------------------


def detect_total_mismatches(
    formula_wb,
    value_wb,
    formula_cells: list[dict],
    tolerance: float = 1e-6,
    names=None,
    budget=None,
) -> list[Finding]:
    """Two flavours of TOTAL_MISMATCH.

    * A total that adds a cell its own SUM range already covers is a double
      count; this is static and needs no cached values.
    * A bare ``=SUM(range)`` whose cached value disagrees with the numeric
      components is a stale or inconsistent calculation. Only bare sums are
      compared: ``AVERAGE``, ``COUNT``, or ``SUM(...)/1000`` legitimately differ
      from the component sum and must never be reported as defects.
    """
    findings: list[Finding] = []
    for cell in formula_cells:
        tick(budget)
        formula = cell["formula"]
        for cell_text, range_text in double_counted_cells(formula, cell["sheet"]):
            findings.append(
                Finding(
                    rule_id="TOTAL_MISMATCH",
                    severity="High",
                    error_confidence="Likely defect",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Total double-counts a cell inside its own range",
                    formula=formula,
                    evidence=[f"{formula} adds {cell_text}, which is already inside {range_text}."],
                    suggested_fix="Remove the duplicated term or shrink the range so each component is counted once.",
                )
            )

        toks = tokens(formula)
        range_text = _bare_sum_range(toks) if toks is not None else None
        if range_text is None:
            continue
        sheet_name, rest = split_sheet(range_text)
        box = boundaries(rest)
        if box is None and names is not None:
            resolved = names.resolve(rest, sheet_name or cell["sheet"])
            if len(resolved) == 1:
                sheet_name, resolved_ref = resolved[0]
                box = boundaries(resolved_ref)
        if box is None:
            continue
        range_sheet = find_sheet(value_wb, sheet_name or cell["sheet"])
        home_sheet = find_sheet(value_wb, cell["sheet"])
        if range_sheet is None or home_sheet is None:
            continue
        cached_total = _numeric(cell_value(value_wb[home_sheet], cell["row"], cell["col"]))
        if cached_total is None:
            continue
        value_ws = value_wb[range_sheet]
        min_col, min_row, max_col, max_row = box
        component_sum = 0.0
        numeric_count = 0
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                value = _numeric(cell_value(value_ws, row, col))
                if value is not None:
                    component_sum += value
                    numeric_count += 1
        allowed = max(tolerance, 1e-9 * abs(cached_total))
        if numeric_count and abs(cached_total - component_sum) > allowed:
            findings.append(
                Finding(
                    rule_id="TOTAL_MISMATCH",
                    severity="Critical",
                    error_confidence="Defect",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Stated total differs from referenced components",
                    formula=formula,
                    evidence=[
                        f"Cached value is {cached_total}; the numeric components of {range_text} sum to {component_sum}. "
                        "The cached value is stale (workbook saved without recalculation) or the calculation is inconsistent."
                    ],
                    impact={"estimated_delta": cached_total - component_sum},
                    suggested_fix="Recalculate the workbook and review the aggregate formula and referenced component range.",
                )
            )
    return findings


def _single_aggregate_box(formula: str, sheet: str, row: int, col: int, names) -> Box | None:
    toks = tokens(formula)
    if toks is None or _bare_sum_range(toks) is None:
        return None
    ranges = aggregate_ranges(formula, names=names, origin=(sheet, row, col))
    if len(ranges) != 1 or not ranges[0].bounded:
        return None
    ref = ranges[0]
    if ref.sheet is not None and ref.sheet.casefold() != sheet.casefold():
        return None
    return boundaries(ref.ref)


def _column_total_rows(formula: str, sheet: str, row: int, col: int, names) -> tuple[int, int] | None:
    """Row span when the formula is one vertical aggregate over its own column, ending above ``row``."""
    box = _single_aggregate_box(formula, sheet, row, col, names)
    if box is None:
        return None
    min_col, min_row, max_col, max_row = box
    if min_col != col or max_col != col or max_row >= row:
        return None
    return (min_row, max_row)


def _row_total_cols(formula: str, sheet: str, row: int, col: int, names) -> tuple[int, int] | None:
    """Column span when the formula is one horizontal aggregate over its own row, ending left of ``col``."""
    box = _single_aggregate_box(formula, sheet, row, col, names)
    if box is None:
        return None
    min_col, min_row, max_col, max_row = box
    if min_row != row or max_row != row or max_col >= col:
        return None
    return (min_col, max_col)


def detect_cross_foot_failures(
    formula_wb,
    value_wb,
    allowed_sheet_names: set[str] | None = None,
    tolerance: float = 1e-6,
    budget=None,
    names=None,
) -> list[Finding]:
    """Compare a table's grand total reached down its row totals vs across its column totals.

    A table is recognized from its formulas, not from adjacency, so stacked
    blocks that share a total column are not confused with one another: a run
    of two or more column totals (each a single vertical SUM over its own
    column, ending above the totals row) defines the columns, the union of
    their row spans defines the rows, and every one of those rows must carry
    a row total in the column just right of the run spanning exactly those
    columns. The corner cell's own value is never used. Value-gated: skips
    when any needed cached value is missing rather than guessing.
    """
    findings: list[Finding] = []
    for ws in formula_wb.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        value_title = find_sheet(value_wb, ws.title)
        if value_title is None:
            continue
        value_ws = value_wb[value_title]
        formulas: dict[int, dict[int, str]] = defaultdict(dict)
        for cell in iter_existing_cells(ws):
            text = formula_text(cell.value)
            if text is not None:
                formulas[cell.row][cell.column] = text

        for gr in sorted(formulas):
            tick(budget)
            spans = {
                col: span
                for col, text in formulas[gr].items()
                if (span := _column_total_rows(text, ws.title, gr, col, names)) is not None
            }
            if len(spans) < 2:
                continue
            # The corner may itself be a vertical SUM of the row totals (a grand
            # total), which looks exactly like one more column total. So every
            # column right after a column total is a candidate corner, and the
            # run is whatever contiguous column totals sit to its left.
            column_set = set(spans)
            for corner_col in sorted({col + 1 for col in column_set}):
                run: list[int] = []
                col = corner_col - 1
                while col in column_set:
                    run.append(col)
                    col -= 1
                run.reverse()
                if len(run) < 2:
                    continue
                first_col, last_col = run[0], run[-1]
                first_row = min(spans[col][0] for col in run)
                last_row = max(spans[col][1] for col in run)
                if last_row - first_row + 1 < 2:
                    continue
                table_rows = range(first_row, last_row + 1)
                if any(
                    _row_total_cols(formulas.get(r, {}).get(corner_col, ""), ws.title, r, corner_col, names)
                    != (first_col, last_col)
                    for r in table_rows
                ):
                    continue
                down = [_numeric(cell_value(value_ws, r, corner_col)) for r in table_rows]
                across = [_numeric(cell_value(value_ws, gr, col)) for col in run]
                if any(v is None for v in down) or any(v is None for v in across):
                    continue
                down_sum = sum(down)
                across_sum = sum(across)
                if abs(down_sum - across_sum) <= max(tolerance, 1e-9 * abs(down_sum)):
                    continue
                corner_letter = get_column_letter(corner_col)
                findings.append(
                    Finding(
                        rule_id="CROSS_FOOT_FAILURE",
                        severity="Critical",
                        error_confidence="Defect",
                        detection_mode="DET",
                        location=f"{ws.title}!{corner_letter}{gr}",
                        title="Row totals and column totals disagree",
                        evidence=[
                            f"Row totals {corner_letter}{first_row}:{corner_letter}{last_row} sum to {down_sum}; "
                            f"column totals {get_column_letter(first_col)}{gr}:{get_column_letter(last_col)}{gr} "
                            f"sum to {across_sum}."
                        ],
                        impact={"estimated_delta": down_sum - across_sum},
                        suggested_fix="Reconcile the totals row and totals column; one of the contributing aggregates is likely wrong.",
                    )
                )
    return findings
