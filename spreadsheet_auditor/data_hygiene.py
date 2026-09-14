from __future__ import annotations

import re
from collections import defaultdict

from openpyxl.utils.cell import get_column_letter

from .budget import tick
from .finding import Finding
from .formula_parser import is_formula
from .reference_resolver import cell_value
from .referenced import ReferenceIndex
from .workbook_inventory import iter_existing_cells, location


NUMERIC_TEXT_RE = re.compile(r"^\s*[-+]?\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*$|^\s*[-+]?\d+(?:\.\d+)?\s*$")
# "0013", "045": a leading zero marks an identifier that must stay text.
LEADING_ZERO_RE = re.compile(r"^\s*[-+]?0\d")
MIN_NUMERIC_COLUMN = 3
# A column where this many values, and at least four in five of them, carry
# padding was padded by an export; it gets one note, not one finding per cell.
MIN_PADDED_COLUMN = 3


def _sheets(workbook, allowed_sheet_names: set[str] | None):
    for ws in workbook.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        yield ws


def _is_plain_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def detect_data_hygiene(
    formula_wb,
    allowed_sheet_names: set[str] | None = None,
    budget=None,
    formulas: list[dict] | None = None,
    names=None,
    index: ReferenceIndex | None = None,
) -> list[Finding]:
    """Data-hygiene findings, gated on what formulas actually consume.

    ``formulas`` (the workbook's formula inventory) lets the checks tell a
    number-as-text that a SUM silently skips from one nothing reads, a merged
    title banner from a merge inside a summed block, and a duplicate label
    from a duplicate lookup key.
    """
    if index is None:
        index = ReferenceIndex.from_formulas(formulas or [], names=names, budget=budget)
    findings: list[Finding] = []
    findings.extend(_numbers_stored_as_text(formula_wb, allowed_sheet_names, budget, index))
    findings.extend(_whitespace_labels(formula_wb, allowed_sheet_names, budget, index))
    findings.extend(_duplicate_keys(formula_wb, allowed_sheet_names, budget, index))
    findings.extend(_merged_cells(formula_wb, allowed_sheet_names, index, names))
    return findings


def _numbers_stored_as_text(workbook, allowed_sheet_names, budget, index: ReferenceIndex) -> list[Finding]:
    findings: list[Finding] = []
    for ws in _sheets(workbook, allowed_sheet_names):
        numeric_per_col: dict[int, int] = defaultdict(int)
        text_numbers: list = []
        for cell in iter_existing_cells(ws):
            tick(budget)
            value = cell.value
            if _is_plain_number(value):
                numeric_per_col[cell.column] += 1
            elif isinstance(value, str) and NUMERIC_TEXT_RE.match(value) and not LEADING_ZERO_RE.match(value):
                text_numbers.append(cell)
        text_per_col: dict[int, int] = defaultdict(int)
        for cell in text_numbers:
            text_per_col[cell.column] += 1
        for cell in text_numbers:
            value = cell.value
            loc = location(ws.title, cell.row, cell.column)
            if index.numeric_contains(ws.title, cell.row, cell.column):
                findings.append(
                    Finding(
                        rule_id="NUMBERS_STORED_AS_TEXT",
                        severity="High",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=loc,
                        title="Numeric-looking value stored as text",
                        evidence=[
                            f"Cell contains text value {value!r} and a formula consumes it as a number; "
                            "SUM-style functions skip text and arithmetic on it fails."
                        ],
                        suggested_fix="Convert the value to a number or confirm it is intentionally text.",
                    )
                )
            elif (
                numeric_per_col[cell.column] >= MIN_NUMERIC_COLUMN
                and numeric_per_col[cell.column] > text_per_col[cell.column]
            ):
                findings.append(
                    Finding(
                        rule_id="NUMBERS_STORED_AS_TEXT",
                        severity="Medium",
                        error_confidence="Review",
                        detection_mode="DET",
                        location=loc,
                        title="Numeric-looking text in a numeric column",
                        evidence=[
                            f"Cell contains text value {value!r} in a column that otherwise holds {numeric_per_col[cell.column]} numbers."
                        ],
                        suggested_fix="Convert the value to a number or confirm it is intentionally text.",
                    )
                )
    return findings


def _whitespace_labels(workbook, allowed_sheet_names, budget, index: ReferenceIndex) -> list[Finding]:
    """Padded keys and labels: the stray padded value, not the export artefact.

    A column where most text values carry the same padding came out of a
    fixed-width export and gets one note. A padded header, a label indented
    with leading spaces, and a whitespace-only spacer cell are presentation.
    What remains is the one padded value among clean ones, which a lookup or
    a criteria match silently misses.
    """
    findings: list[Finding] = []
    for ws in _sheets(workbook, allowed_sheet_names):
        text_cells: dict[int, list] = defaultdict(list)
        last_row: dict[int, int] = {}
        row_counts: dict[int, int] = defaultdict(int)
        for cell in iter_existing_cells(ws):
            tick(budget)
            value = cell.value
            if value is None:
                continue
            last_row[cell.column] = cell.row
            if not is_formula(value):
                row_counts[cell.row] += 1
            if isinstance(value, str) and not is_formula(value):
                text_cells[cell.column].append(cell)
        # The header band is the sheet's first occupied row, plus the second
        # when the first holds a lone title.
        top_rows = sorted(row_counts)[:2]
        header_rows = set(top_rows[:1])
        if len(top_rows) == 2 and row_counts[top_rows[0]] == 1:
            header_rows.add(top_rows[1])
        for col in sorted(text_cells):
            cells = text_cells[col]
            candidates = []
            for cell in cells:
                value = cell.value
                if value == value.strip() or not value.strip():
                    continue
                if cell.row in header_rows and last_row[col] > cell.row:
                    continue  # a title or header over data, not a key
                referenced = index.contains(ws.title, cell.row, cell.column)
                leading_only = value.rstrip() == value
                if leading_only and (len(value) - len(value.lstrip()) >= 2 or not referenced):
                    continue  # leading spaces indent a label; a single stray space on a key still counts
                if cell.column != 1 and not referenced:
                    continue
                candidates.append(cell)
            if not candidates:
                continue
            if len(candidates) >= MIN_PADDED_COLUMN and len(candidates) * 5 >= len(cells) * 4:
                lead = candidates[0]
                findings.append(
                    Finding(
                        rule_id="WHITESPACE_KEY",
                        severity="Low",
                        error_confidence="Info",
                        detection_mode="DET",
                        location=location(ws.title, lead.row, lead.column),
                        title="Column of padded text values",
                        evidence=[
                            f"{len(candidates)} of {len(cells)} text values in column {get_column_letter(col)} carry leading or "
                            f"trailing whitespace, for example {lead.value!r}; this looks like fixed-width padding from an export."
                        ],
                        suggested_fix="Trim the column if its values are matched against keys typed elsewhere.",
                    )
                )
                continue
            for cell in candidates:
                value = cell.value
                findings.append(
                    Finding(
                        rule_id="WHITESPACE_KEY",
                        severity="Medium",
                        error_confidence="Review",
                        detection_mode="DET",
                        location=location(ws.title, cell.row, cell.column),
                        title="Text has leading or trailing whitespace",
                        evidence=[f"Raw value is {value!r}; the other text values in this column are not padded."],
                        suggested_fix="Trim the value if it is used as a lookup key or label.",
                    )
                )
    return findings


def _duplicate_keys(workbook, allowed_sheet_names, budget, index: ReferenceIndex) -> list[Finding]:
    """Duplicate keys inside ranges that lookup-style functions search."""
    findings: list[Finding] = []
    for ws in _sheets(workbook, allowed_sheet_names):
        columns = index.lookup_columns(ws.title)
        if not columns:
            continue
        by_col: dict[int, dict[str, list[str]]] = {col: defaultdict(list) for col in columns}
        intervals = {col: index.lookup_intervals(ws.title, col) for col in columns}
        for cell in iter_existing_cells(ws):
            if cell.column not in by_col:
                continue
            tick(budget)
            value = cell.value
            if not (isinstance(value, str) and value.strip()):
                continue
            if not any(start <= cell.row <= end for start, end in intervals[cell.column]):
                continue
            by_col[cell.column][value.strip().lower()].append(location(ws.title, cell.row, cell.column))
        for col in columns:
            for key, locs in by_col[col].items():
                if len(locs) > 1:
                    findings.append(
                        Finding(
                            rule_id="DUPLICATE_KEY",
                            severity="Medium",
                            error_confidence="Review",
                            detection_mode="DET",
                            location=", ".join(locs[:5]),
                            title="Duplicate key in lookup range",
                            evidence=[
                                f"Normalized key {key!r} appears {len(locs)} times in a range searched by lookup formulas; only the first match is returned."
                            ],
                            suggested_fix="Make the keys unique or confirm the lookup is meant to return the first match.",
                        )
                    )
    return findings


def _inside_table(names, sheet: str, box: tuple[int, int, int, int]) -> bool:
    tables = getattr(names, "tables", None) or {}
    for info in tables.values():
        if info.sheet.casefold() != sheet.casefold():
            continue
        if info.min_col <= box[0] and info.min_row <= box[1] and info.max_col >= box[2] and info.max_row >= box[3]:
            return True
    return False


def _merged_cells(workbook, allowed_sheet_names, index: ReferenceIndex, names) -> list[Finding]:
    findings: list[Finding] = []
    for ws in _sheets(workbook, allowed_sheet_names):
        for merged in ws.merged_cells.ranges:
            box = (merged.min_col, merged.min_row, merged.max_col, merged.max_row)
            top_left = cell_value(ws, merged.min_row, merged.min_col)
            if not _is_plain_number(top_left):
                # A merged title, header, label, blank spacer, or a merged
                # formula in a totals row is presentation; only a merged
                # number is an input that a range read through the merge
                # sees as blanks.
                continue
            referenced = index.intersects_box(ws.title, box, ranges_only=True)
            if not referenced and not _inside_table(names, ws.title, box):
                continue
            findings.append(
                Finding(
                    rule_id="MERGED_CELL_IN_DATA_RANGE",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=f"{ws.title}!{merged}",
                    title="Merged cell region inside data used by formulas",
                    evidence=[
                        "Merged region lies inside a range that formulas read"
                        + ("" if referenced else " (a table")
                        + "; only its top-left cell holds a value, so aggregates and lookups over it see blanks."
                    ],
                    suggested_fix="Unmerge the cells or move the merge outside the data range.",
                )
            )
    return findings
