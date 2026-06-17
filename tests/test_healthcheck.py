"""Healthcheck output contract."""

from __future__ import annotations

import json
import subprocess
import sys


def test_human_healthcheck_succeeds():
    result = subprocess.run(
        [sys.executable, "-m", "spreadsheet_auditor", "--healthcheck"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Spreadsheet Auditor Healthcheck" in result.stdout
    assert "Status:" in result.stdout
    assert "openpyxl" in result.stdout


def test_json_healthcheck_succeeds():
    result = subprocess.run(
        [sys.executable, "-m", "spreadsheet_auditor", "--healthcheck", "--json"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["tool_version"]
    assert {"name", "status", "version"} <= set(data["required_packages"][0].keys())
    assert data["recalculation_mode"] in {"available", "cached_values_only"}
    assert data["macro_execution"] == "disabled"
    assert data["external_links"] == "inventoried_only"


def test_missing_optional_is_warning_not_error():
    """Optional deps may be missing locally; status should still be 'ready'
    unless a *required* dep is gone."""
    result = subprocess.run(
        [sys.executable, "-m", "spreadsheet_auditor", "--healthcheck", "--json"],
        capture_output=True,
        text=True,
    )
    data = json.loads(result.stdout)
    assert data["status"] == "ready"
