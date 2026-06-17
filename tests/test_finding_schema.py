"""Tests for the enriched Finding contract introduced in v0.1.0."""

from __future__ import annotations

from spreadsheet_auditor.finding import Finding


def _f(location: str, rule_id: str = "BROKEN_REFERENCE") -> Finding:
    return Finding(
        rule_id=rule_id,
        severity="High",
        error_confidence="Defect",
        detection_mode="DET",
        location=location,
        title="t",
        evidence=["e"],
        suggested_fix="fix",
    )


def test_parses_sheet_cell_range_from_location():
    f = _f("Budget!B14")
    d = f.to_dict()
    assert d["sheet"] == "Budget"
    assert d["cell"] == "B14"
    assert d["range"] is None


def test_parses_range_form():
    f = _f("Budget!B2:B10")
    d = f.to_dict()
    assert d["sheet"] == "Budget"
    assert d["range"] == "B2:B10"
    assert d["cell"] is None


def test_handles_multi_location_string():
    f = _f("Model!A37, Model!A38", rule_id="DUPLICATE_KEY")
    d = f.to_dict()
    # primary anchor is the first location
    assert d["sheet"] == "Model"
    assert d["cell"] == "A37"


def test_fingerprint_is_stable_and_whitespace_invariant():
    a = _f("Sheet1!B2:B10")
    b = _f("  Sheet1 !  B2:B10  ")
    assert a.fingerprint == b.fingerprint


def test_fingerprint_differs_by_rule():
    a = _f("Sheet1!B2", rule_id="BROKEN_REFERENCE")
    b = _f("Sheet1!B2", rule_id="HARDCODE_IN_FORMULA_BLOCK")
    assert a.fingerprint != b.fingerprint


def test_aliases_present_in_dict():
    d = _f("Budget!A1").to_dict()
    assert d["mode"] == d["detection_mode"]
    assert d["confidence"] == d["error_confidence"]
    assert "fingerprint" in d
    assert "limitations" in d


def test_info_severity_is_accepted_by_sort():
    from spreadsheet_auditor.finding import sort_findings

    findings = [_f("Sheet1!A1")]
    info_finding = Finding(
        rule_id="INFO_NOTE",
        severity="Info",
        error_confidence="Review",
        detection_mode="HEUR",
        location="Sheet1!Z99",
        title="info",
        evidence=["e"],
        suggested_fix="n/a",
    )
    ordered = sort_findings(findings + [info_finding])
    assert ordered[-1] is info_finding
