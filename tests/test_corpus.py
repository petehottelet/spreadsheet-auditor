"""Integration test: run the auditor against the seeded corpus and assert findings."""

import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
CORPUS = ROOT / "assets" / "test_corpus"
WORKBOOK = CORPUS / "seeded_defects" / "seeded-defects.xlsx"
EXPECTED = CORPUS / "expected_findings" / "seeded-defects.json"


@pytest.fixture(scope="module")
def audit_payload(tmp_path_factory) -> dict:
    out = tmp_path_factory.mktemp("audit") / "findings.json"
    result = subprocess.run(
        [sys.executable, str(SCRIPTS / "audit.py"), str(WORKBOOK), "--json", str(out)],
        capture_output=True,
        text=True,
    )
    assert result.returncode in (0, 1), f"audit failed: {result.stderr}"
    return json.loads(out.read_text(encoding="utf-8"))


def _produced(payload: dict) -> dict:
    produced = defaultdict(set)
    for finding in payload["findings"]:
        produced[finding["rule_id"]].add(finding["location"])
    return produced


def test_static_findings_present(audit_payload):
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    produced = _produced(audit_payload)
    missing = []
    for rule_id, locations in expected["static_expected"].items():
        for location in locations:
            if location not in produced.get(rule_id, set()):
                missing.append(f"{rule_id} @ {location}")
    assert not missing, f"Missing expected findings: {missing}"


def test_value_dependent_findings_when_recalc_completed(audit_payload):
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    value_dependent = expected.get("value_dependent_expected", {})
    if audit_payload["workbook"]["recalc_status"] != "completed":
        pytest.skip("Recalculation unavailable; value-dependent checks not exercised.")
    produced = _produced(audit_payload)
    missing = []
    for rule_id, locations in value_dependent.items():
        for location in locations:
            if location not in produced.get(rule_id, set()):
                missing.append(f"{rule_id} @ {location}")
    assert not missing, f"Missing value-dependent findings: {missing}"


def test_findings_match_schema(audit_payload):
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads((ROOT / "schemas" / "findings.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=audit_payload, schema=schema)
