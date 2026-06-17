"""Smoke tests for the --summary/--quiet/--demo/--version flags."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "examples" / "demo_bad_budget.xlsx"


def _run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "spreadsheet_auditor", *args],
        capture_output=True,
        text=True,
    )


def test_version_flag():
    result = _run("--version")
    assert result.returncode == 0, result.stderr
    assert "spreadsheet-auditor" in result.stdout
    # version string should look like x.y.z
    parts = result.stdout.strip().split()[-1].split(".")
    assert len(parts) >= 2


def test_help_includes_exit_codes_section():
    result = _run("--help")
    assert result.returncode == 0
    assert "Exit codes:" in result.stdout
    assert "--summary" in result.stdout
    assert "--quiet" in result.stdout
    assert "--demo" in result.stdout
    assert "--format" in result.stdout


@pytest.mark.skipif(not DEMO.exists(), reason="demo workbook not generated yet")
def test_summary_against_demo():
    result = _run("--demo", "--summary")
    # demo is intentionally bad -> exit 1
    assert result.returncode == 1, result.stderr
    assert "workbook" in result.stdout
    assert "findings" in result.stdout
    assert "fail_on" in result.stdout


@pytest.mark.skipif(not DEMO.exists(), reason="demo workbook not generated yet")
def test_quiet_suppresses_stdout():
    result = _run("--demo", "--quiet")
    assert result.returncode == 1
    assert result.stdout == ""
