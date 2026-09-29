"""A mistake in the input exits 4 and says what to fix; a bug in the auditor exits 5 with its traceback."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

import pytest
from openpyxl import Workbook

from spreadsheet_auditor import audit


def _workbook(tmp_path: Path) -> Path:
    wb = Workbook()
    ws = wb.active
    ws.title = "Model"
    ws["A1"], ws["B1"] = "Revenue", 100
    ws["A2"], ws["B2"] = "Error", "=SUM(#REF!)"
    path = tmp_path / "model.xlsx"
    wb.save(path)
    return path


def _config(tmp_path: Path, text: str, name: str = "config.json") -> Path:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def _audit(tmp_path: Path, *args: str) -> int:
    ignore = tmp_path / "no-suppressions"
    ignore.touch()
    return audit.main([*args, "--quiet", "--ignore", str(ignore)])


def _json_audit(tmp_path: Path, source: Path, *args: str) -> dict:
    out = tmp_path / "findings.json"
    _audit(tmp_path, str(source), "--json", str(out), "--fail-on", "None", *args)
    return json.loads(out.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    ("config", "message"),
    [
        ('{"checks": {"LIVE_EROR": "off"}}', "Unknown rule 'LIVE_EROR' in config; did you mean 'LIVE_ERROR'?"),
        ('{"checks": {"Volatile_Functon": "off"}}', "did you mean 'VOLATILE_FUNCTION'?"),
        ('{"limit": {"max_formulas": 10}}', "Unknown section 'limit' in config; did you mean 'limits'?"),
        ('{"limits": {"max_finding": 10}}', "did you mean 'max_reported_findings'?"),
        ('{"limits": {"max_reported_findings": "200"}}', "limits.max_reported_findings must be a whole number"),
        ('{"recalc": {"timeout_seconds": 0}}', "recalc.timeout_seconds must be a whole number of 1 or more"),
        ('{"recalc": {"enabled": "no"}}', "recalc.enabled must be true or false, not 'no'"),
        ('{"checks": {"LIVE_ERROR": "maybe"}}', "checks.LIVE_ERROR must be true, false, or one of"),
        ('{"checks": ["LIVE_ERROR"]}', "'checks' must map rule names to settings"),
        ('{"suppressions": {"rule_id": "LIVE_ERROR"}}', "'suppressions' must be a list"),
        ('["checks"]', "must hold a mapping of sections"),
        ('{"checks": {"LIVE_ERROR": "off",}}', "is not valid JSON: Expecting property name enclosed in double quotes at line 1"),
        ("", "is not valid JSON"),
    ],
)
def test_a_config_mistake_exits_4_and_names_the_fix(tmp_path, capsys, config, message):
    code = _audit(tmp_path, str(_workbook(tmp_path)), "--config", str(_config(tmp_path, config)))
    err = capsys.readouterr().err
    assert code == 4, err
    assert err.startswith("Config error: ")
    assert message in err
    assert "Traceback" not in err


def test_a_json_syntax_error_names_its_line(tmp_path, capsys):
    config = _config(tmp_path, '{\n  "recalc": {"enabled": false}\n  "limits": {}\n}')
    assert _audit(tmp_path, str(_workbook(tmp_path)), "--config", str(config)) == 4
    assert "Expecting ',' delimiter at line 3, column 3" in capsys.readouterr().err


def test_a_missing_or_misnamed_config_exits_4(tmp_path, capsys):
    workbook = str(_workbook(tmp_path))
    assert _audit(tmp_path, workbook, "--config", str(tmp_path / "missing.json")) == 4
    assert "Config file not found:" in capsys.readouterr().err
    assert _audit(tmp_path, workbook, "--config", str(_config(tmp_path, "{}", "config.toml"))) == 4
    assert "must be .json, .yml or .yaml" in capsys.readouterr().err


def test_a_config_that_is_not_utf8_exits_4(tmp_path, capsys):
    config = tmp_path / "config.json"
    config.write_bytes('{"mode": "café"}'.encode("cp1252"))
    assert _audit(tmp_path, str(_workbook(tmp_path)), "--config", str(config)) == 4
    assert "is not UTF-8 text" in capsys.readouterr().err


def test_a_yaml_syntax_error_exits_4(tmp_path, capsys):
    pytest.importorskip("yaml")
    config = _config(tmp_path, "checks:\n  LIVE_ERROR: off\n limits: [\n", "config.yml")
    assert _audit(tmp_path, str(_workbook(tmp_path)), "--config", str(config)) == 4
    assert "is not valid YAML" in capsys.readouterr().err


def test_check_names_and_settings_match_in_any_case(tmp_path):
    workbook = _workbook(tmp_path)
    for checks in ({"live_error": "OFF"}, {"Live_Errors": False}):
        config = _config(tmp_path, json.dumps({"recalc": {"enabled": False}, "checks": checks}))
        payload = _json_audit(tmp_path, workbook, "--config", str(config))
        assert "LIVE_ERROR" not in {finding["rule_id"] for finding in payload["findings"]}, checks


def test_a_complete_valid_config_is_accepted(tmp_path):
    config = {
        "mode": "financial_model",
        "scope": {"include_sheets": ["Model"], "exclude_sheets": [], "headline_outputs": ["Model!B1"]},
        "materiality": {"absolute": 1000, "relative": 0.001, "percent_points": 0.1},
        "limits": {"max_cells": 0, "max_formulas": 100, "max_range_expansion_cells": 1000,
                   "max_reported_findings": 50, "timeout_seconds": 0},
        "recalc": {"enabled": False, "timeout_seconds": 30},
        "finance": {"enabled": True},
        "checks": {"LIVE_ERROR": "warn", "blank_precedent": True, "volatile_function": "off"},
        "suppressions": [],
    }
    path = _config(tmp_path, json.dumps(config))
    assert _audit(tmp_path, str(_workbook(tmp_path)), "--config", str(path)) == 0  # LIVE_ERROR is only a warning


def test_a_windows_1252_csv_is_audited_with_a_note(tmp_path, capsys):
    source = tmp_path / "export.csv"
    source.write_bytes("Name,Amount\r\ncafé ,10\r\nthé,20\r\n".encode("cp1252"))
    payload = _json_audit(tmp_path, source)
    assert any("read as Windows-1252" in note for note in payload["coverage"]["limitations"])
    [finding] = payload["findings"]
    assert finding["location"] == "CSV!R2C1"
    assert "'café '" in finding["evidence"][0]


def test_a_csv_in_neither_encoding_exits_4(tmp_path, capsys):
    source = tmp_path / "export.csv"
    source.write_bytes(b"Name,Amount\r\n\x81\x8d,10\r\n")  # bytes undefined in both UTF-8 and Windows-1252
    assert _audit(tmp_path, str(source)) == 4
    assert "Preflight failed: The CSV is neither UTF-8 nor Windows-1252" in capsys.readouterr().err


def test_a_suppression_file_that_is_not_utf8_exits_4(tmp_path, capsys):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_bytes("LIVE_ERROR Model!B2 accepted by José\n".encode("cp1252"))
    code = audit.main([str(_workbook(tmp_path)), "--quiet", "--ignore", str(ignore)])
    assert code == 4
    assert "is not UTF-8 text; save it as UTF-8" in capsys.readouterr().err


def test_a_workbook_whose_contents_do_not_parse_exits_4(tmp_path, capsys):
    source = tmp_path / "broken.xlsx"
    with zipfile.ZipFile(source, "w") as archive:
        archive.writestr("[Content_Types].xml", "not xml")
    assert _audit(tmp_path, str(source)) == 4
    err = capsys.readouterr().err
    assert err.startswith("Preflight failed: The workbook could not be read (")
    assert "save a copy, and audit the copy" in err


def test_a_folder_named_like_a_workbook_exits_4(tmp_path, capsys):
    folder = tmp_path / "model.xlsx"
    folder.mkdir()
    assert _audit(tmp_path, str(folder)) == 4
    assert f"Preflight failed: Could not read {folder}" in capsys.readouterr().err


def test_an_output_path_in_a_missing_folder_exits_4(tmp_path, capsys):
    report = tmp_path / "no-such-folder" / "report.md"
    assert _audit(tmp_path, str(_workbook(tmp_path)), "--out", str(report), "--fail-on", "None") == 4
    err = capsys.readouterr().err
    assert err.startswith("Could not write output: ")
    assert "Traceback" not in err


def test_a_bug_while_auditing_exits_5_with_its_traceback(tmp_path, monkeypatch, capsys):
    def broken(args):
        raise KeyError("sheet_index")

    monkeypatch.setattr(audit, "audit_workbook", broken)
    assert _audit(tmp_path, str(_workbook(tmp_path))) == 5
    err = capsys.readouterr().err
    assert "Internal audit error while auditing: KeyError: 'sheet_index'" in err
    assert "This is a bug in spreadsheet-auditor" in err
    assert "Traceback (most recent call last):" in err
    assert "in broken" in err


def test_a_bug_while_writing_output_exits_5_with_its_traceback(tmp_path, monkeypatch, capsys):
    def broken(*args, **kwargs):
        raise TypeError("render_markdown() got an unexpected keyword argument")

    monkeypatch.setattr(audit, "_write_report", broken)
    code = _audit(tmp_path, str(_workbook(tmp_path)), "--out", str(tmp_path / "report.md"), "--fail-on", "None")
    err = capsys.readouterr().err
    assert code == 5
    assert "Internal audit error while writing output: TypeError: render_markdown()" in err
    assert "Traceback (most recent call last):" in err
