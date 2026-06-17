from __future__ import annotations

from openpyxl.utils.cell import range_boundaries

from finding import Finding
from range_checks import aggregate_ranges


def _numeric(value) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def detect_total_mismatches(formula_wb, value_wb, formula_cells: list[dict], tolerance: float = 1e-6) -> list[Finding]:
    findings: list[Finding] = []
    for cell in formula_cells:
        ranges = aggregate_ranges(cell["formula"])
        if len(ranges) != 1:
            continue
        ref = ranges[0]
        sheet = ref.sheet or cell["sheet"]
        if sheet not in value_wb.sheetnames:
            continue
        value_ws = value_wb[sheet]
        formula_value_ws = value_wb[cell["sheet"]]
        cached_total = _numeric(formula_value_ws[cell["coord"]].value)
        if cached_total is None:
            continue
        try:
            min_col, min_row, max_col, max_row = range_boundaries(ref.ref)
        except ValueError:
            continue
        component_sum = 0.0
        numeric_count = 0
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                value = _numeric(value_ws.cell(row=row, column=col).value)
                if value is not None:
                    component_sum += value
                    numeric_count += 1
        if numeric_count and abs(cached_total - component_sum) > tolerance:
            findings.append(
                Finding(
                    rule_id="TOTAL_MISMATCH",
                    severity="Critical",
                    error_confidence="Defect",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Stated total differs from referenced components",
                    formula=cell["formula"],
                    evidence=[f"Cached value is {cached_total}; recomputed referenced components sum to {component_sum}."],
                    impact={"estimated_delta": cached_total - component_sum},
                    suggested_fix="Recalculate the workbook and review the aggregate formula and referenced component range.",
                )
            )
    return findings
