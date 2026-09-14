"""EUSES recall harness: properties parsing, original lookup, and hit attribution."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "benchmarks" / "corpus"))

import recall  # noqa: E402

PROPS = """# simple configuration file
# notation: worksheet!column!row

EXCEL_SHEET=..\\\\..\\\\spreadsheets\\\\cs101\\\\SEEDED\\\\ACT3_sec23_smith_1FAULTS_FAULTVERSION1.xls

CORRECT_OUTPUT_1=0!B!10
INCORRECT_OUTPUT_1=0!C!16
INCORRECT_OUTCELL_EXPECTED_VALUE_1=517.1666666666666

FAULTY_CELLS_1=0!C!16
FAULT_TYPE_1=RFR
"""


def test_parse_properties_extracts_path_and_faults():
    props = recall.parse_properties(PROPS)
    assert props["excel_sheet"] == "../../spreadsheets/cs101/SEEDED/ACT3_sec23_smith_1FAULTS_FAULTVERSION1.xls"
    assert props["faults"] == [{"sheet_index": 0, "col": "C", "row": 16, "type": "RFR"}]


def test_original_lookup_strips_the_fault_version(tmp_path):
    seeded = tmp_path / "cs101" / "SEEDED" / "ACT3_sec23_smith_1FAULTS_FAULTVERSION3.xls"
    seeded.parent.mkdir(parents=True)
    seeded.write_bytes(b"")
    original_dir = tmp_path / "cs101" / "original"
    original_dir.mkdir()
    assert recall.original_for(seeded) is None
    (original_dir / "ACT3_sec23_smith.xls").write_bytes(b"")
    assert recall.original_for(seeded) == original_dir / "ACT3_sec23_smith.xls"


def _finding(rule: str, location: str) -> dict:
    return {"rule_id": rule, "location": location}


def test_evaluate_attributes_hits_to_the_mutation():
    faults = [{"sheet_index": 0, "col": "C", "row": 16, "type": "RFR"}, {"sheet_index": 0, "col": "E", "row": 4, "type": "FRC"}]
    sheetnames = ["Sheet1"]
    seeded = [
        _finding("FORMULA_DRIFT", "Sheet1!C16"),  # direct hit, new in the seeded version
        _finding("LITERAL_CONSTANT", "Sheet1!C16"),  # also present in the original -> not attributable
        _finding("RANGE_EXCLUSION", "Sheet1!C20"),  # same column as C16 -> line hit
        _finding("HARDCODE_IN_FORMULA_BLOCK", "Sheet1!A4:F4"),  # range covering E4 -> direct hit
    ]
    original = [_finding("LITERAL_CONSTANT", "Sheet1!C16")]
    verdicts = recall.evaluate(faults, sheetnames, seeded, original)
    first, second = verdicts
    assert first["target"] == "Sheet1!C16"
    assert first["direct"] == ["FORMULA_DRIFT", "LITERAL_CONSTANT"]
    assert first["direct_attributable"] == ["FORMULA_DRIFT"]
    assert "RANGE_EXCLUSION" in first["line_attributable"]
    assert second["direct_attributable"] == ["HARDCODE_IN_FORMULA_BLOCK"]

    summary = recall.summarize(verdicts, [{"seeded": "x", "status": "ok", "seeded_findings": 4, "original_findings": 1}])
    assert summary["faults"] == 2 and summary["direct_attributable"] == 2 and summary["recall"] == 1.0
    assert summary["by_type"]["RFR"]["direct_attributable"] == 1
    text = recall.render_summary(summary, "now")
    assert "| RFR | reference replaced | 1 | 1 |" in text
