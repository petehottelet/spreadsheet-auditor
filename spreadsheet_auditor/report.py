from __future__ import annotations

import json
import platform
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from .finding import SEVERITY_ORDER, sort_findings


DISCLAIMER = (
    "This audit inspected formulas, ranges, workbook structure, hidden rows/columns/sheets, "
    "cached/recalculated values where available, and selected data-hygiene issues. It did not "
    "execute macros, validate external data sources, fully evaluate Power Query/Data Model objects, "
    "or certify business assumptions. Findings are defect candidates and likely errors, not a "
    "legal/accounting certification of correctness."
)


def _safe_version(module_name: str) -> str | None:
    try:
        return getattr(__import__(module_name), "__version__", None)
    except Exception:
        return None


def _collect_runtime(coverage: dict | None = None) -> dict:
    coverage = coverage or {}
    libreoffice_version = coverage.get("libreoffice_version")
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "openpyxl": _safe_version("openpyxl"),
        "defusedxml": _safe_version("defusedxml"),
        "networkx": _safe_version("networkx"),
        "libreoffice": libreoffice_version,
    }


def _normalize_coverage(coverage: dict) -> dict:
    """Produce a structured `coverage` block that doesn't lose the legacy keys."""
    recalculation = {
        "status": coverage.get("recalc_status"),
        "limitations": [
            note
            for note in coverage.get("limitations", [])
            if "recalc" in note.lower() or "libreoffice" in note.lower()
        ],
    }
    macros = {
        "present": bool(coverage.get("macros_present", False)),
        "executed": bool(coverage.get("macros_executed", False)),
    }
    external_links = {
        "present": bool(coverage.get("external_links_present", False)),
        "followed": False,
    }
    out = dict(coverage)
    out.setdefault("recalculation", recalculation)
    out.setdefault("macros", macros)
    out.setdefault("external_links", external_links)
    return out


def build_payload(audit_version: str, workbook_meta: dict, coverage: dict, findings) -> dict:
    normalized_coverage = _normalize_coverage(coverage)
    recalc_block = normalized_coverage.setdefault("recalculation", {})
    if not recalc_block.get("status"):
        recalc_block["status"] = workbook_meta.get("recalc_status")
    return {
        "audit_version": audit_version,
        "tool_version": audit_version,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "runtime": _collect_runtime(coverage),
        "workbook": workbook_meta,
        "coverage": normalized_coverage,
        "findings": [finding.to_dict() for finding in sort_findings(findings)],
    }


def write_json(payload: dict, path: str | Path) -> None:
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


CONFIDENCE_BUCKETS = [
    ("Confirmed", "Defect", "Hard defects: the auditor is certain this is wrong."),
    ("Likely", "Likely defect", "Strong defect candidates; review and confirm."),
    ("Review", "Review", "Heuristic flags; worth a second look but may be intentional."),
    ("Info", "Info", "Informational notes (e.g. opt-in finance heuristics)."),
]


def _confidence_bucket(value: str) -> str:
    for bucket, confidence, _ in CONFIDENCE_BUCKETS:
        if confidence == value:
            return bucket
    return "Review"


def render_markdown(payload: dict, show_suppressed: bool = False) -> str:
    findings = payload["findings"]
    suppressed = [f for f in findings if f.get("suppressed")]
    if show_suppressed:
        active = list(findings)
    else:
        active = [f for f in findings if not f.get("suppressed")]
    counts = Counter(f["severity"] for f in active)
    workbook = payload["workbook"]
    coverage = payload["coverage"]
    timestamp = payload.get("timestamp")
    tool_version = payload.get("tool_version") or payload.get("audit_version")

    lines = [
        f"# Spreadsheet Audit Report - {Path(workbook['path']).name}",
        "",
        "## Executive Summary",
        "",
        f"- Tool version: `{tool_version}`" + (f" (run at {timestamp})" if timestamp else ""),
        f"- Workbook SHA-256: `{workbook['sha256']}`",
        f"- Sheets analyzed: {workbook['sheets_analyzed']}",
        f"- Formulas scanned: {workbook['formulas_scanned']}",
        f"- Recalculation status: {workbook['recalc_status']}",
        f"- Findings: {counts.get('Critical', 0)} Critical, {counts.get('High', 0)} High, {counts.get('Medium', 0)} Medium, {counts.get('Low', 0)} Low, {counts.get('Info', 0)} Info",
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

    by_bucket: dict[str, list[dict]] = defaultdict(list)
    for finding in active:
        bucket = _confidence_bucket(finding.get("error_confidence", "Review"))
        by_bucket[bucket].append(finding)

    for bucket, _confidence, description in CONFIDENCE_BUCKETS:
        items = by_bucket.get(bucket, [])
        if not items and bucket == "Info":
            continue
        lines.append(f"## {bucket} Findings")
        lines.append("")
        lines.append(f"_{description}_")
        lines.append("")
        if not items:
            lines.extend(["No findings in this category.", ""])
            continue
        # Within a bucket, sort by severity then rule.
        items_sorted = sorted(items, key=lambda f: (SEVERITY_ORDER.get(f["severity"], 99), f["rule_id"], f["location"]))
        for finding in items_sorted:
            lines.extend(_render_finding(finding))

    lines.extend(["## Suppressed Findings Summary", ""])
    if suppressed:
        for finding in suppressed:
            lines.append(f"- `{finding['id']}` {finding['rule_id']} at {finding['location']}: {finding.get('impact', {}).get('suppression_reason', '')}")
    else:
        lines.append("No suppressed findings.")
    lines.extend(["", "## Recommended Next Steps", ""])
    if active:
        lines.append("1. Start with the **Confirmed** section: every item there is a hard defect.")
        lines.append("2. Walk the **Likely** section, comparing each flagged formula to its neighbors (drift findings include them inline).")
        lines.append("3. Recalculate the workbook in Excel if value-dependent checks were skipped due to recalculation being unavailable.")
        lines.append("4. Rerun the audit after fixes; keep suppressions only for intentional patterns with documented reasons.")
    else:
        lines.append("1. No active findings were detected by the configured checks. Review the coverage limitations before relying on this result.")
    lines.extend(["", "## Non-Certification Disclaimer", "", DISCLAIMER, ""])
    return "\n".join(lines)


def write_markdown(payload: dict, path: str | Path, show_suppressed: bool = False) -> None:
    Path(path).write_text(render_markdown(payload, show_suppressed=show_suppressed), encoding="utf-8")


def _html_escape(value: object) -> str:
    import html as _html

    return _html.escape("" if value is None else str(value), quote=True)


_HTML_STYLES = """
:root {
  color-scheme: light;
  --bg: #ffffff;
  --fg: #111827;
  --muted: #4b5563;
  --border: #e5e7eb;
  --card-bg: #f9fafb;
  --critical: #b91c1c;
  --high: #c2410c;
  --medium: #92400e;
  --low: #1f2937;
  --info: #1d4ed8;
  --pill-bg: #e0e7ff;
  --pill-fg: #1e3a8a;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 32px clamp(16px, 4vw, 64px);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: var(--bg);
  color: var(--fg);
  line-height: 1.5;
}
h1, h2, h3 { line-height: 1.25; }
h1 { font-size: 1.8rem; margin-bottom: 0.25rem; }
h2 { font-size: 1.25rem; margin-top: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.subtitle { color: var(--muted); margin-top: 0; margin-bottom: 1.5rem; }
.summary { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 1.5rem; }
.summary .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; padding: 12px 14px; }
.summary .card .label { font-size: 0.85rem; color: var(--muted); }
.summary .card .value { font-size: 1.4rem; font-weight: 600; }
.summary .card.critical .value { color: var(--critical); }
.summary .card.high .value { color: var(--high); }
.summary .card.medium .value { color: var(--medium); }
.summary .card.low .value { color: var(--low); }
.summary .card.info .value { color: var(--info); }
.finding { background: var(--card-bg); border: 1px solid var(--border); border-left: 6px solid var(--low); border-radius: 8px; padding: 14px 18px; margin-bottom: 14px; }
.finding.critical { border-left-color: var(--critical); }
.finding.high { border-left-color: var(--high); }
.finding.medium { border-left-color: var(--medium); }
.finding.info { border-left-color: var(--info); }
.finding-header { display: flex; flex-wrap: wrap; gap: 8px; align-items: baseline; }
.finding-header h3 { margin: 0; font-size: 1.05rem; flex: 1; }
.pill { display: inline-block; padding: 1px 8px; border-radius: 999px; background: var(--pill-bg); color: var(--pill-fg); font-size: 0.78rem; }
.meta { color: var(--muted); font-size: 0.85rem; margin: 4px 0 8px; }
.evidence, .fix { margin: 6px 0; }
.evidence li { margin: 2px 0; }
code { background: rgba(0,0,0,0.04); padding: 1px 4px; border-radius: 4px; font-size: 0.9em; }
pre code { display: block; padding: 8px; overflow-x: auto; }
.disclaimer { margin-top: 2rem; padding: 14px 18px; border: 1px dashed var(--border); border-radius: 8px; color: var(--muted); font-size: 0.9rem; }
table.limits { border-collapse: collapse; font-size: 0.9rem; }
table.limits td, table.limits th { border: 1px solid var(--border); padding: 4px 8px; text-align: left; }
"""


def _render_html_finding(finding: dict) -> str:
    severity = (finding.get("severity") or "Low").lower()
    title = _html_escape(finding.get("title"))
    rule_id = _html_escape(finding.get("rule_id"))
    location = _html_escape(finding.get("location"))
    detection_mode = _html_escape(finding.get("detection_mode"))
    confidence = _html_escape(finding.get("error_confidence"))
    fingerprint = _html_escape(finding.get("fingerprint", ""))
    formula = finding.get("formula")
    evidence = finding.get("evidence") or []
    suggested = _html_escape(finding.get("suggested_fix"))
    finding_id = _html_escape(finding.get("id"))

    formula_block = (
        f"<div class=\"formula\"><code>{_html_escape(formula)}</code></div>" if formula else ""
    )
    evidence_block = ""
    if evidence:
        items = "".join(f"<li>{_html_escape(item)}</li>" for item in evidence)
        evidence_block = f"<div class=\"evidence\"><strong>Evidence:</strong><ul>{items}</ul></div>"
    fingerprint_block = (
        f"<span class=\"pill\" title=\"Stable fingerprint\">fp:{fingerprint}</span>"
        if fingerprint
        else ""
    )
    return (
        f"<article class=\"finding {severity}\">"
        f"<div class=\"finding-header\">"
        f"<h3>{title}</h3>"
        f"<span class=\"pill\">{rule_id}</span>"
        f"<span class=\"pill\">{detection_mode}</span>"
        f"<span class=\"pill\">{confidence}</span>"
        f"{fingerprint_block}"
        f"</div>"
        f"<p class=\"meta\">ID <code>{finding_id}</code> &middot; Location <code>{location}</code></p>"
        f"{formula_block}"
        f"{evidence_block}"
        f"<p class=\"fix\"><strong>Suggested fix:</strong> {suggested}</p>"
        f"</article>"
    )


def render_html(payload: dict, show_suppressed: bool = False) -> str:
    findings = payload["findings"]
    suppressed = [f for f in findings if f.get("suppressed")]
    if show_suppressed:
        active = list(findings)
    else:
        active = [f for f in findings if not f.get("suppressed")]
    counts = Counter(f["severity"] for f in active)
    workbook = payload["workbook"]
    coverage = payload["coverage"]

    severity_keys = ["Critical", "High", "Medium", "Low", "Info"]
    summary_cards = "".join(
        f"<div class=\"card {sev.lower()}\"><div class=\"label\">{sev}</div>"
        f"<div class=\"value\">{counts.get(sev, 0)}</div></div>"
        for sev in severity_keys
    )

    findings_sections = []
    for severity in severity_keys:
        bucket = [f for f in active if f.get("severity") == severity]
        if not bucket and severity == "Info":
            continue
        heading = "Medium / Review Findings" if severity == "Medium" else f"{severity} Findings"
        if not bucket:
            findings_sections.append(f"<h2>{heading}</h2><p>No findings in this category.</p>")
            continue
        cards = "\n".join(_render_html_finding(f) for f in bucket)
        findings_sections.append(f"<h2>{heading}</h2>{cards}")

    suppressed_section = ""
    if suppressed:
        rows = "".join(
            "<li><code>"
            + _html_escape(f.get("id"))
            + "</code> "
            + _html_escape(f.get("rule_id"))
            + " at <code>"
            + _html_escape(f.get("location"))
            + "</code> &mdash; "
            + _html_escape(f.get("impact", {}).get("suppression_reason", "(no reason)"))
            + "</li>"
            for f in suppressed
        )
        suppressed_section = f"<h2>Suppressed</h2><ul>{rows}</ul>"

    coverage_rows = [
        ("Workbook", workbook.get("path")),
        ("SHA-256", workbook.get("sha256")),
        ("Sheets analyzed", workbook.get("sheets_analyzed")),
        ("Formulas scanned", workbook.get("formulas_scanned")),
        ("Recalculation", workbook.get("recalc_status")),
        ("Macros present", coverage.get("macros_present", False)),
        ("External links present", coverage.get("external_links_present", False)),
    ]
    coverage_table = (
        "<table class=\"limits\">"
        + "".join(
            f"<tr><th>{_html_escape(k)}</th><td>{_html_escape(v)}</td></tr>"
            for k, v in coverage_rows
        )
        + "</table>"
    )
    limitations = coverage.get("limitations") or []
    limitations_block = ""
    if limitations:
        items = "".join(f"<li>{_html_escape(item)}</li>" for item in limitations)
        limitations_block = f"<h3>Limitations</h3><ul>{items}</ul>"

    title = _html_escape(Path(workbook.get("path", "workbook")).name)
    tool_version = _html_escape(payload.get("tool_version", payload.get("audit_version", "")))
    timestamp = _html_escape(payload.get("timestamp", ""))

    return (
        "<!doctype html>"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>Spreadsheet Audit Report - {title}</title>"
        f"<style>{_HTML_STYLES}</style>"
        "</head><body>"
        f"<h1>Spreadsheet Audit Report</h1>"
        f"<p class=\"subtitle\">{title} &middot; spreadsheet-auditor {tool_version} &middot; {timestamp}</p>"
        f"<div class=\"summary\">{summary_cards}</div>"
        f"<h2>Coverage</h2>{coverage_table}{limitations_block}"
        + "".join(findings_sections)
        + suppressed_section
        + f"<div class=\"disclaimer\">{_html_escape(DISCLAIMER)}</div>"
        "</body></html>"
    )


def write_html(payload: dict, path: str | Path, show_suppressed: bool = False) -> None:
    Path(path).write_text(render_html(payload, show_suppressed=show_suppressed), encoding="utf-8")


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
