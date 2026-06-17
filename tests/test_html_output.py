"""HTML report contract."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from spreadsheet_auditor.finding import Finding
from spreadsheet_auditor.report import build_payload, render_html


def _payload():
    workbook_meta = {
        "path": "demo.xlsx",
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
        "limitations": ["LibreOffice unavailable in CI snapshot"],
    }
    findings = [
        Finding(
            rule_id="BROKEN_REFERENCE",
            severity="High",
            error_confidence="Defect",
            detection_mode="DET",
            location="Budget!B14",
            title="Formula contains deleted reference",
            evidence=["Formula text contains #REF!."],
            suggested_fix="Restore the deleted reference.",
            formula="=SUM(#REF!)",
        )
    ]
    return build_payload("0.1.0", workbook_meta, coverage, findings)


def test_render_html_contains_required_sections():
    html = render_html(_payload())
    assert html.startswith("<!doctype html>")
    assert "Spreadsheet Audit Report" in html
    assert "BROKEN_REFERENCE" in html
    assert "Budget!B14" in html
    # severity summary cards
    assert "class=\"card high\"" in html
    # disclaimer always present
    assert "Findings are defect candidates" in html


def test_render_html_is_self_contained_no_external_assets():
    html = render_html(_payload())
    assert re.search(r"<link\b[^>]*\bhref=\"https?://", html) is None
    assert re.search(r"<script\b", html) is None
    assert re.search(r"<img\b[^>]*\bsrc=\"https?://", html) is None


def test_html_escapes_user_content():
    payload = _payload()
    payload["findings"][0]["title"] = "<script>alert(1)</script>"
    html = render_html(payload)
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;" in html


def test_cli_format_html_writes_html_file(tmp_path):
    workbook = Path(__file__).resolve().parents[1] / "examples" / "demo_bad_budget.xlsx"
    if not workbook.exists():
        return  # demo not yet generated locally
    out = tmp_path / "report.html"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "spreadsheet_auditor",
            str(workbook),
            "--out",
            str(out),
            "--format",
            "html",
        ],
        capture_output=True,
        text=True,
    )
    # Findings produce exit code 1; that's expected for the bad demo.
    assert result.returncode in (0, 1), result.stderr
    text = out.read_text(encoding="utf-8")
    assert text.startswith("<!doctype html>")
    assert "Spreadsheet Audit Report" in text
