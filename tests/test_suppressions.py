"""Suppression file and config behavior."""

from __future__ import annotations

from spreadsheet_auditor.finding import Finding
from spreadsheet_auditor.report import build_payload, render_markdown
from spreadsheet_auditor.suppressions import apply_suppressions, load_suppressions


def _make_finding(rule_id: str = "BROKEN_REFERENCE", location: str = "Sheet1!B14") -> Finding:
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


def test_ignore_file_requires_reason(tmp_path):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text(
        "\n".join(
            [
                "# Comment line",
                "BROKEN_REFERENCE Sheet1!B14",  # missing reason -> dropped
                "BROKEN_REFERENCE Sheet1!B14 acknowledged in audit",
            ]
        ),
        encoding="utf-8",
    )
    suppressions = load_suppressions(None, str(ignore))
    assert len(suppressions) == 1
    assert suppressions[0]["reason"] == "acknowledged in audit"


def test_apply_by_fingerprint(tmp_path):
    finding = _make_finding()
    fp = finding.fingerprint
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text(f"fingerprint:{fp} test fingerprint suppression\n", encoding="utf-8")
    suppressions = load_suppressions(None, str(ignore))
    assert suppressions[0]["fingerprint"] == fp
    apply_suppressions([finding], suppressions)
    assert finding.suppressed is True
    assert finding.impact["suppression_reason"] == "test fingerprint suppression"


def test_apply_by_rule_and_range():
    finding = _make_finding(location="Budget!B14")
    apply_suppressions(
        [finding],
        [{"rule_id": "BROKEN_REFERENCE", "range": "Budget!B14", "reason": "known"}],
    )
    assert finding.suppressed is True


def test_apply_skips_when_missing_reason_in_config():
    finding = _make_finding()
    apply_suppressions(
        [finding],
        load_suppressions({"suppressions": [{"rule_id": "BROKEN_REFERENCE", "range": "Sheet1!B14"}]}, None),
    )
    assert finding.suppressed is False  # missing reason -> dropped


def test_missing_reason_in_config_emits_warning():
    warnings: list[str] = []
    load_suppressions(
        {"suppressions": [{"rule_id": "BROKEN_REFERENCE", "range": "Sheet1!B14"}]},
        None,
        warnings=warnings,
    )
    assert len(warnings) == 1
    assert "missing required 'reason'" in warnings[0]


def test_malformed_ignore_line_emits_warning(tmp_path):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text("BROKEN_REFERENCE Sheet1!B14\n", encoding="utf-8")  # no reason
    warnings: list[str] = []
    suppressions = load_suppressions(None, str(ignore), warnings=warnings)
    assert suppressions == []
    assert len(warnings) == 1
    assert ".audit-ignore:1" in warnings[0]


def test_report_hides_suppressed_by_default_but_shows_with_flag():
    workbook_meta = {"path": "x.xlsx", "sha256": "abc", "sheets_analyzed": 1, "formulas_scanned": 1, "recalc_status": "completed"}
    coverage = {"macros_present": False, "macros_executed": False, "external_links_present": False, "unsupported_features": [], "limitations": []}
    suppressed = _make_finding(location="Sheet1!X1")
    suppressed.suppressed = True
    suppressed.impact["suppression_reason"] = "known"
    active = _make_finding(location="Sheet1!Y1")
    payload = build_payload("0.1.0", workbook_meta, coverage, [suppressed, active])

    md_default = render_markdown(payload)
    assert "Sheet1!Y1" in md_default
    # Suppressed details appear only in the suppressed summary, not the main sections.
    assert md_default.count("Sheet1!X1") <= 1

    md_show = render_markdown(payload, show_suppressed=True)
    assert md_show.count("Sheet1!X1") >= 2
