"""Run-metadata contract for audit payloads."""

from __future__ import annotations

from datetime import datetime

from spreadsheet_auditor.finding import Finding
from spreadsheet_auditor.report import build_payload


def _payload():
    workbook_meta = {
        "path": "workbook.xlsx",
        "sha256": "deadbeef",
        "sheets_analyzed": 1,
        "formulas_scanned": 1,
        "recalc_status": "completed",
    }
    coverage = {
        "macros_present": False,
        "macros_executed": False,
        "external_links_present": False,
        "unsupported_features": [],
        "limitations": [],
    }
    findings = [
        Finding(
            rule_id="LIVE_ERROR",
            severity="Critical",
            error_confidence="Defect",
            detection_mode="DET",
            location="Sheet1!A1",
            title="x",
            evidence=["e"],
            suggested_fix="f",
        )
    ]
    return build_payload("0.1.0", workbook_meta, coverage, findings)


def test_payload_includes_tool_version_timestamp_runtime():
    payload = _payload()
    assert payload["tool_version"] == "0.1.0"
    assert payload["audit_version"] == "0.1.0"
    timestamp = payload["timestamp"]
    # ISO-8601 UTC, e.g. "2026-06-16T20:01:00+00:00"
    assert datetime.fromisoformat(timestamp)
    runtime = payload["runtime"]
    assert "python" in runtime
    assert "platform" in runtime
    assert "openpyxl" in runtime


def test_coverage_block_is_normalized_with_structured_subkeys():
    payload = _payload()
    cov = payload["coverage"]
    assert cov["recalculation"]["status"] == "completed"
    assert cov["macros"] == {"present": False, "executed": False}
    assert cov["external_links"]["present"] is False
    assert cov["external_links"]["followed"] is False
    # Legacy keys preserved for backward compat
    assert cov["macros_present"] is False
    assert cov["external_links_present"] is False


def test_payload_validates_against_findings_schema():
    """The payload must continue to validate against the published schema."""
    import json
    from pathlib import Path

    try:
        from jsonschema import validate
    except Exception:
        return  # jsonschema is dev-only; skip when not installed

    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "findings.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validate(_payload(), schema)
