from __future__ import annotations

import re
from collections import defaultdict

from finding import Finding
from workbook_inventory import location


NUMERIC_TEXT_RE = re.compile(r"^\s*[-+]?\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*$|^\s*[-+]?\d+(?:\.\d+)?\s*$")


def detect_data_hygiene(formula_wb, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(_numbers_stored_as_text(formula_wb, allowed_sheet_names))
    findings.extend(_whitespace_labels(formula_wb, allowed_sheet_names))
    findings.extend(_duplicate_keys(formula_wb, allowed_sheet_names))
    findings.extend(_merged_cells(formula_wb, allowed_sheet_names))
    return findings


def _numbers_stored_as_text(workbook, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for ws in workbook.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        for row in ws.iter_rows():
            for cell in row:
                value = cell.value
                if isinstance(value, str) and NUMERIC_TEXT_RE.match(value):
                    findings.append(
                        Finding(
                            rule_id="NUMBERS_STORED_AS_TEXT",
                            severity="High",
                            error_confidence="Likely defect",
                            detection_mode="DET",
                            location=location(ws.title, cell.row, cell.column),
                            title="Numeric-looking value stored as text",
                            evidence=[f"Cell contains text value {value!r}, which may be ignored by numeric formulas."],
                            suggested_fix="Convert the value to a number or confirm it is intentionally text.",
                        )
                    )
    return findings


def _whitespace_labels(workbook, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for ws in workbook.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        for row in ws.iter_rows():
            for cell in row:
                value = cell.value
                if isinstance(value, str) and value != value.strip():
                    findings.append(
                        Finding(
                            rule_id="WHITESPACE_KEY",
                            severity="Medium",
                            error_confidence="Review",
                            detection_mode="DET",
                            location=location(ws.title, cell.row, cell.column),
                            title="Text has leading or trailing whitespace",
                            evidence=[f"Raw value is {value!r}."],
                            suggested_fix="Trim the value if it is used as a lookup key or label.",
                        )
                    )
    return findings


def _duplicate_keys(workbook, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for ws in workbook.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        seen: dict[str, list[str]] = defaultdict(list)
        for row in range(1, ws.max_row + 1):
            value = ws.cell(row=row, column=1).value
            if isinstance(value, str) and value.strip():
                seen[value.strip().lower()].append(location(ws.title, row, 1))
        for key, locs in seen.items():
            if len(locs) > 1:
                findings.append(
                    Finding(
                        rule_id="DUPLICATE_KEY",
                        severity="Medium",
                        error_confidence="Review",
                        detection_mode="DET",
                        location=", ".join(locs[:5]),
                        title="Duplicate normalized key in first column",
                        evidence=[f"Normalized key {key!r} appears {len(locs)} times."],
                        suggested_fix="Confirm duplicate labels are intentional, especially if lookup formulas depend on this column.",
                    )
                )
    return findings


def _merged_cells(workbook, allowed_sheet_names: set[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for ws in workbook.worksheets:
        if allowed_sheet_names is not None and ws.title not in allowed_sheet_names:
            continue
        for merged in ws.merged_cells.ranges:
            findings.append(
                Finding(
                    rule_id="MERGED_CELL_IN_DATA_RANGE",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=f"{ws.title}!{merged}",
                    title="Merged cell region present",
                    evidence=["Merged cells can break sorting, filling, lookups, and aggregate interpretation."],
                    suggested_fix="Confirm the merge is only presentational and does not sit inside data used by formulas.",
                )
            )
    return findings
