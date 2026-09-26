"""Fingerprints follow the flagged cell's content, not its address."""

from __future__ import annotations

import json
from pathlib import Path

from openpyxl import Workbook

from spreadsheet_auditor import audit
from spreadsheet_auditor.finding import Finding
from spreadsheet_auditor.identity import assign_identities


def _model(path: Path, offset: int = 0, new_error_row: int | None = None) -> Path:
    """Nine labeled lines with an accepted #REF! on line 5, shifted down by ``offset`` rows."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Model"
    for line in range(1, 10):
        ws.cell(line + offset, 1, f"Line {line}")
        ws.cell(line + offset, 2, line * 100)
    ws.cell(5 + offset, 3, "=SUM(#REF!)")
    if new_error_row:
        ws.cell(new_error_row, 3, "=B1/#REF!")
    wb.save(path)
    return path


def _audit(workbook: Path, ignore: Path) -> dict:
    out = workbook.with_suffix(".json")
    audit.main([str(workbook), "--json", str(out), "--quiet", "--ignore", str(ignore), "--fail-on", "None"])
    return json.loads(out.read_text(encoding="utf-8"))


def _by_rule(payload: dict, rule: str) -> list[dict]:
    return [f for f in payload["findings"] if f["rule_id"] == rule]


def test_fingerprint_suppression_survives_a_row_insert_and_does_not_hide_a_new_error(tmp_path):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text("", encoding="utf-8")
    before = _audit(_model(tmp_path / "v1.xlsx"), ignore)
    [accepted] = _by_rule(before, "LIVE_ERROR")
    assert accepted["location"] == "Model!C5"
    ignore.write_text(f"fingerprint:{accepted['fingerprint']} accepted: legacy link, FIN-12\n", encoding="utf-8")

    # A title row goes in above the model; a new #REF! is typed at C5.
    after = _audit(_model(tmp_path / "v2.xlsx", offset=1, new_error_row=5), ignore)
    live = {f["location"]: f for f in _by_rule(after, "LIVE_ERROR")}
    assert live["Model!C6"]["suppressed"] is True
    assert live["Model!C6"]["fingerprint"] == accepted["fingerprint"]
    assert live["Model!C5"]["suppressed"] is False
    assert not [note for note in after["coverage"]["limitations"] if "matched no finding" in note]


def test_a_stale_suppression_is_reported(tmp_path):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text(
        "LIVE_ERROR Model!C5 accepted: legacy link\n"
        "LIVE_ERROR Model!C7 fixed long ago\n"
        "fingerprint:0123456789abcdef a finding that no longer exists\n",
        encoding="utf-8",
    )
    payload = _audit(_model(tmp_path / "v1.xlsx"), ignore)
    stale = [note for note in payload["coverage"]["limitations"] if "matched no finding" in note]
    assert len(stale) == 2
    assert ".audit-ignore:2): LIVE_ERROR Model!C7" in stale[0]
    assert ".audit-ignore:3): fingerprint:0123456789abcdef" in stale[1]


def test_suppressions_that_could_not_match_stay_quiet(tmp_path):
    ignore = tmp_path / ".audit-ignore"
    ignore.write_text("LITERAL_CONSTANT Model!D5 house rate\n", encoding="utf-8")
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"checks": {"LITERAL_CONSTANT": "off"}}), encoding="utf-8")
    workbook = _model(tmp_path / "v1.xlsx")
    out = tmp_path / "f.json"
    audit.main([str(workbook), "--json", str(out), "--quiet", "--ignore", str(ignore), "--config", str(config)])
    limitations = json.loads(out.read_text(encoding="utf-8"))["coverage"]["limitations"]
    assert not [note for note in limitations if "matched no finding" in note]


def _finding(location: str) -> Finding:
    return Finding("FORMULA_DRIFT", "High", "Likely defect", "DET", location, "t", ["e"], "fix")


def test_identity_is_content_plus_label_numbered_in_sheet_order():
    wb = Workbook()
    ws = wb.active
    ws.title = "S"
    for row in (2, 3, 4):
        ws.cell(row, 1, "Same label")
        ws.cell(row, 3, f"=A{row}*B{row}")
    ws.cell(5, 1, "Other label")
    ws.cell(5, 3, "=A5*B5")
    findings = [_finding("S!C4"), _finding("S!C2"), _finding("S!C5"), _finding("S!C3")]
    assign_identities(findings, wb)
    by_location = {f.location: f.identity for f in findings}
    assert by_location["S!C2"].endswith("|=RC[-2]*RC[-1]|1")
    assert by_location["S!C3"].endswith("|2") and by_location["S!C4"].endswith("|3")
    assert by_location["S!C5"] == "s|Other label|=RC[-2]*RC[-1]|1"
    # A location outside the workbook keeps the location-based fingerprint.
    elsewhere = _finding("Gone!A1")
    assign_identities([elsewhere], wb)
    assert elsewhere.identity is None and elsewhere.fingerprint == _finding("Gone!A1").fingerprint
