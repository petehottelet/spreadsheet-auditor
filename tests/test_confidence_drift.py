"""Confidence-grouped report layout + drift neighbor evidence."""

from __future__ import annotations

from spreadsheet_auditor.finding import Finding
from spreadsheet_auditor.formula_drift import detect_formula_drift
from spreadsheet_auditor.report import build_payload, render_markdown


def test_row_drift_attaches_neighboring_formulas():
    cells = [
        {"sheet": "S", "row": 2, "col": 2, "location": "S!B2", "formula": "=A2+1"},
        {"sheet": "S", "row": 2, "col": 3, "location": "S!C2", "formula": "=B2+1"},
        {"sheet": "S", "row": 2, "col": 4, "location": "S!D2", "formula": "=B2*99"},  # drift
        {"sheet": "S", "row": 2, "col": 5, "location": "S!E2", "formula": "=D2+1"},
    ]
    findings = detect_formula_drift(cells)
    assert findings, "expected drift to fire"
    target = next(f for f in findings if f.location == "S!D2")
    evidence_text = " ".join(target.evidence)
    assert "Dominant pattern" in evidence_text
    # at least one neighbor is referenced by location
    assert "S!C2=" in evidence_text or "S!E2=" in evidence_text


def test_column_drift_attaches_neighboring_formulas():
    cells = [
        {"sheet": "S", "row": 2, "col": 2, "location": "S!B2", "formula": "=A2+1"},
        {"sheet": "S", "row": 3, "col": 2, "location": "S!B3", "formula": "=A3+1"},
        {"sheet": "S", "row": 4, "col": 2, "location": "S!B4", "formula": "=A4*5"},  # drift
        {"sheet": "S", "row": 5, "col": 2, "location": "S!B5", "formula": "=A5+1"},
    ]
    findings = detect_formula_drift(cells)
    target = next(f for f in findings if f.location == "S!B4")
    evidence_text = " ".join(target.evidence)
    assert "Dominant pattern" in evidence_text
    assert "Neighboring formulas" in evidence_text


def test_report_groups_findings_by_confidence_bucket():
    workbook_meta = {
        "path": "x.xlsx",
        "sha256": "abc",
        "sheets_analyzed": 1,
        "formulas_scanned": 1,
        "recalc_status": "completed",
    }
    coverage = {"macros_present": False, "macros_executed": False, "external_links_present": False, "unsupported_features": [], "limitations": []}
    findings = [
        Finding("LIVE_ERROR", "Critical", "Defect", "DET", "S!A1", "live", ["e"], "fix"),
        Finding("FORMULA_DRIFT", "High", "Likely defect", "DET", "S!A2", "drift", ["e"], "fix"),
        Finding("IFERROR_MASK", "Medium", "Review", "HEUR", "S!A3", "mask", ["e"], "fix"),
    ]
    payload = build_payload("0.1.0", workbook_meta, coverage, findings)
    md = render_markdown(payload)
    assert "## Confirmed Findings" in md
    assert "## Likely Findings" in md
    assert "## Review Findings" in md
    # confirmed comes before likely, likely before review
    confirmed_idx = md.index("## Confirmed Findings")
    likely_idx = md.index("## Likely Findings")
    review_idx = md.index("## Review Findings")
    assert confirmed_idx < likely_idx < review_idx
