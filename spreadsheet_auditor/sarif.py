"""SARIF 2.1.0 output for GitHub code scanning.

The mapping treats each Spreadsheet Auditor `Finding` as a SARIF result. The
workbook is the artifact (`artifactLocation.uri`), and the sheet + cell are
encoded inside the result message and in `properties.sheet`/`cell`/`range`.
GitHub's code-scanning UI does not natively render `.xlsx` line-level
artifacts, so each result also points at line 1 of the workbook so it renders
as a single line annotation in PR diffs.

Severity is mapped to SARIF `level` (`error`/`warning`/`note`) and the
auditor's own severity is preserved in `properties.severity`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SARIF_VERSION = "2.1.0"
SARIF_SCHEMA = (
    "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json"
)

_SEVERITY_TO_LEVEL = {
    "Critical": "error",
    "High": "error",
    "Medium": "warning",
    "Low": "note",
    "Info": "note",
}


def _rules_from_findings(findings: list[dict]) -> list[dict]:
    seen: dict[str, dict] = {}
    for f in findings:
        rule_id = f.get("rule_id")
        if not rule_id or rule_id in seen:
            continue
        seen[rule_id] = {
            "id": rule_id,
            "name": rule_id,
            "shortDescription": {"text": _short_description(rule_id)},
            "fullDescription": {"text": _short_description(rule_id)},
            "defaultConfiguration": {"level": _SEVERITY_TO_LEVEL.get(f.get("severity"), "note")},
            "helpUri": "https://github.com/petehottelet/spreadsheet-auditor/blob/main/references/check_catalog.md",
        }
    return list(seen.values())


def _short_description(rule_id: str) -> str:
    # Conservative human-readable label derived from the rule id; we keep this
    # cheap rather than maintaining a separate catalog.
    return rule_id.replace("_", " ").title()


def _result(finding: dict, workbook_uri: str) -> dict:
    rule_id = finding.get("rule_id", "UNKNOWN")
    severity = finding.get("severity", "Low")
    location = finding.get("location") or ""
    sheet = finding.get("sheet")
    cell = finding.get("cell")
    range_ = finding.get("range")
    fingerprint = finding.get("fingerprint")
    message = (
        f"{finding.get('title') or rule_id} ({rule_id}) at {location}.\n"
        f"Evidence: {' | '.join(finding.get('evidence') or [])}.\n"
        f"Suggested fix: {finding.get('suggested_fix') or 'See report.'}"
    )
    result: dict[str, Any] = {
        "ruleId": rule_id,
        "level": _SEVERITY_TO_LEVEL.get(severity, "note"),
        "message": {"text": message},
        "locations": [
            {
                "physicalLocation": {
                    "artifactLocation": {"uri": workbook_uri},
                    "region": {"startLine": 1, "startColumn": 1},
                },
                "logicalLocations": [
                    {
                        "name": location,
                        "kind": "cell",
                    }
                ],
            }
        ],
        "properties": {
            "severity": severity,
            "confidence": finding.get("error_confidence"),
            "mode": finding.get("detection_mode"),
            "sheet": sheet,
            "cell": cell,
            "range": range_,
        },
    }
    if fingerprint:
        result["partialFingerprints"] = {"spreadsheetAuditor/v1": fingerprint}
    return result


def render_sarif(payload: dict) -> dict:
    findings = [f for f in payload.get("findings", []) if not f.get("suppressed")]
    workbook = payload.get("workbook", {})
    workbook_uri = Path(workbook.get("path", "workbook.xlsx")).as_posix()
    tool_version = payload.get("tool_version") or payload.get("audit_version") or "unknown"
    rules = _rules_from_findings(findings)

    run = {
        "tool": {
            "driver": {
                "name": "spreadsheet-auditor",
                "version": tool_version,
                "informationUri": "https://github.com/petehottelet/spreadsheet-auditor",
                "rules": rules,
            }
        },
        "results": [_result(f, workbook_uri) for f in findings],
        "originalUriBaseIds": {},
        "artifacts": [
            {
                "location": {"uri": workbook_uri},
                "sourceLanguage": "spreadsheet",
            }
        ],
        "invocations": [
            {
                "executionSuccessful": True,
                "endTimeUtc": payload.get("timestamp"),
            }
        ],
    }
    return {
        "version": SARIF_VERSION,
        "$schema": SARIF_SCHEMA,
        "runs": [run],
    }


def write_sarif(payload: dict, path: str | Path) -> None:
    Path(path).write_text(json.dumps(render_sarif(payload), indent=2), encoding="utf-8")
