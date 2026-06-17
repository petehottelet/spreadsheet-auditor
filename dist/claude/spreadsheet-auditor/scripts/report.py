from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from finding import SEVERITY_ORDER, sort_findings


DISCLAIMER = (
    "This audit inspected formulas, ranges, workbook structure, hidden rows/columns/sheets, "
    "cached/recalculated values where available, and selected data-hygiene issues. It did not "
    "execute macros, validate external data sources, fully evaluate Power Query/Data Model objects, "
    "or certify business assumptions. Findings are defect candidates and likely errors, not a "
    "legal/accounting certification of correctness."
)


def build_payload(audit_version: str, workbook_meta: dict, coverage: dict, findings) -> dict:
    return {
        "audit_version": audit_version,
        "workbook": workbook_meta,
        "coverage": coverage,
        "findings": [finding.to_dict() for finding in sort_findings(findings)],
    }


def write_json(payload: dict, path: str | Path) -> None:
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def render_markdown(payload: dict) -> str:
    findings = payload["findings"]
    active = [f for f in findings if not f.get("suppressed")]
    suppressed = [f for f in findings if f.get("suppressed")]
    counts = Counter(f["severity"] for f in active)
    workbook = payload["workbook"]
    coverage = payload["coverage"]

    lines = [
        f"# Spreadsheet Audit Report - {Path(workbook['path']).name}",
        "",
        "## Executive Summary",
        "",
        f"- Workbook SHA-256: `{workbook['sha256']}`",
        f"- Sheets analyzed: {workbook['sheets_analyzed']}",
        f"- Formulas scanned: {workbook['formulas_scanned']}",
        f"- Recalculation status: {workbook['recalc_status']}",
        f"- Findings: {counts.get('Critical', 0)} Critical, {counts.get('High', 0)} High, {counts.get('Medium', 0)} Medium, {counts.get('Low', 0)} Low",
        f"- Suppressed findings: {len(suppressed)}",
        "",
        "## Coverage And Limitations",
        "",
        f"- Macros present: {coverage.get('macros_present', False)}",
        f"- Macros executed: {coverage.get('macros_executed', False)}",
        f"- External links present: {coverage.get('external_links_present', False)}",
    ]
    if coverage.get("unsupported_features"):
        lines.append("- Unsupported features: " + ", ".join(coverage["unsupported_features"]))
    if coverage.get("limitations"):
        for limitation in coverage["limitations"]:
            lines.append(f"- Limitation: {limitation}")
    lines.append("")

    for severity in ["Critical", "High", "Medium", "Low"]:
        bucket = [f for f in active if f["severity"] == severity]
        heading = "Medium / Review Findings" if severity == "Medium" else f"{severity} Findings"
        lines.extend([f"## {heading}", ""])
        if not bucket:
            lines.extend(["No findings in this category.", ""])
            continue
        for finding in bucket:
            lines.extend(_render_finding(finding))

    lines.extend(["## Suppressed Findings Summary", ""])
    if suppressed:
        for finding in suppressed:
            lines.append(f"- `{finding['id']}` {finding['rule_id']} at {finding['location']}: {finding.get('impact', {}).get('suppression_reason', '')}")
    else:
        lines.append("No suppressed findings.")
    lines.extend(["", "## Recommended Next Steps", ""])
    if active:
        lines.append("1. Review Critical and High findings first, especially those on visible summary sheets.")
        lines.append("2. Recalculate the workbook in Excel if cached values were unavailable or LibreOffice was not available.")
        lines.append("3. Rerun the audit after fixes and keep suppressions only for intentional patterns with documented reasons.")
    else:
        lines.append("1. No active findings were detected by the configured checks. Review the coverage limitations before relying on this result.")
    lines.extend(["", "## Non-Certification Disclaimer", "", DISCLAIMER, ""])
    return "\n".join(lines)


def write_markdown(payload: dict, path: str | Path) -> None:
    Path(path).write_text(render_markdown(payload), encoding="utf-8")


def _render_finding(finding: dict) -> list[str]:
    lines = [
        f"### [{finding['severity'].upper()}] {finding['title']} - {finding['rule_id']}",
        "",
        f"- ID: `{finding['id']}`",
        f"- Location: `{finding['location']}`",
        f"- Detection: {finding['detection_mode']}; confidence: {finding['error_confidence']}",
    ]
    if finding.get("formula"):
        lines.append(f"- Formula: `{finding['formula']}`")
    for evidence in finding.get("evidence", []):
        lines.append(f"- Evidence: {evidence}")
    if finding.get("impact"):
        lines.append("- Impact: " + json.dumps(finding["impact"], ensure_ascii=True))
    lines.append(f"- Suggested fix: {finding['suggested_fix']}")
    lines.append("")
    return lines
