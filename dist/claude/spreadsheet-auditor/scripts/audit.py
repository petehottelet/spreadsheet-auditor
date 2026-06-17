from __future__ import annotations

import argparse
import csv
import json
import platform
import sys
import tempfile
from collections import Counter
from pathlib import Path

from config_loader import allowed_sheets, apply_check_settings, load_config, sheet_is_allowed
from finding import Finding, assign_ids, sort_findings
from preflight import PreflightError, preflight
from recalc import recalc_if_available, soffice_path
from report import build_payload, render_markdown, write_json, write_markdown

AUDIT_VERSION = "0.1.0"
FAIL_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "None": 99}


def healthcheck() -> int:
    packages = {}
    for package in ["openpyxl", "pandas", "defusedxml", "networkx"]:
        try:
            module = __import__(package)
            packages[package] = getattr(module, "__version__", "installed")
        except Exception as exc:
            packages[package] = f"missing: {exc.__class__.__name__}"
    info = {
        "python": sys.version,
        "platform": platform.platform(),
        "packages": packages,
        "libreoffice": soffice_path(),
        "supported_file_types": [".xlsx", ".xlsm", ".csv"],
        "notes": [
            "networkx is optional at runtime; a DFS cycle fallback is used when missing.",
            "LibreOffice is optional; audit falls back to static/cached-value mode when missing.",
        ],
    }
    print(json.dumps(info, indent=2))
    return 0


def _package_available(package: str) -> bool:
    try:
        __import__(package)
        return True
    except Exception:
        return False


def audit_workbook(args: argparse.Namespace) -> tuple[dict, int]:
    from data_hygiene import detect_data_hygiene
    from formula_drift import detect_formula_drift, detect_hardcode_breaks
    from range_checks import detect_fragile_functions, detect_literal_constants, detect_range_issues
    from reconcile import detect_total_mismatches
    from suppressions import apply_suppressions, load_suppressions
    from workbook_inventory import formula_cells, inventory, load_workbooks, scan_live_errors

    input_path = Path(args.workbook)
    preflight_info = preflight(input_path)
    config = load_config(args.config)
    limitations: list[str] = []
    unsupported_features: set[str] = set()
    findings: list[Finding] = []

    if preflight_info["extension"] == ".csv":
        payload = audit_csv(input_path, preflight_info, config, args.ignore)
        return payload, exit_code(payload["findings"], args.fail_on, payload["coverage"]["limitations"])

    with tempfile.TemporaryDirectory(prefix="spreadsheet-auditor-audit-") as temp_dir:
        recalc_config = config.get("recalc") or {}
        recalc_enabled = recalc_config.get("enabled", True)
        recalc_timeout = args.recalc_timeout if args.recalc_timeout is not None else int(recalc_config.get("timeout_seconds", 60))
        if recalc_enabled:
            recalc = recalc_if_available(input_path, timeout_seconds=recalc_timeout, work_dir=temp_dir)
        else:
            recalc = {
                "status": "disabled",
                "path": str(input_path),
                "limitations": ["Recalculation disabled by config; using static analysis and cached values only."],
            }
        limitations.extend(recalc.get("limitations", []))
        if not _package_available("defusedxml"):
            limitations.append("defusedxml is not available; XML parsing relies on workbook library defaults in this runtime.")
        analysis_path = Path(recalc.get("path", input_path))
        recalc_status = recalc.get("status", "unknown")

        formula_wb, value_wb = load_workbooks(analysis_path)
        inv = inventory(input_path, formula_wb, value_wb, preflight_info)
        include, exclude = allowed_sheets(config)
        allowed_sheet_names = {
            ws.title for ws in formula_wb.worksheets if sheet_is_allowed(ws.title, include, exclude)
        }
        all_formulas = formula_cells(formula_wb)
        formulas = [cell for cell in all_formulas if cell["sheet"] in allowed_sheet_names]
        max_formulas = int((config.get("limits") or {}).get("max_formulas", 50000))
        if max_formulas > 0 and len(formulas) > max_formulas:
            limitations.append(f"Formula scan capped at {max_formulas} formulas by config.")
            formulas = formulas[:max_formulas]

        for loc, error_value in scan_live_errors(formula_wb, value_wb):
            sheet_name = loc.split("!", 1)[0]
            if sheet_name not in allowed_sheet_names:
                continue
            findings.append(
                Finding(
                    rule_id="LIVE_ERROR",
                    severity="Critical",
                    error_confidence="Defect",
                    detection_mode="DET",
                    location=loc,
                    title="Cell contains live spreadsheet error",
                    evidence=[f"Cell contains {error_value}."],
                    suggested_fix="Trace the formula precedent chain and resolve the underlying spreadsheet error.",
                )
            )

        findings.extend(detect_reference_issues(formula_wb, value_wb, formulas, unsupported_features))
        findings.extend(detect_formula_drift(formulas))
        findings.extend(detect_hardcode_breaks(formula_wb, allowed_sheet_names))
        findings.extend(detect_literal_constants(formulas))
        findings.extend(detect_fragile_functions(formulas))
        findings.extend(detect_range_issues(formula_wb, value_wb, formulas))
        findings.extend(detect_total_mismatches(formula_wb, value_wb, formulas))
        findings.extend(detect_data_hygiene(formula_wb, allowed_sheet_names))
        findings.extend(detect_cycles(formulas))

        findings = apply_check_settings(findings, config)
        suppressions = load_suppressions(config, args.ignore)
        findings = apply_suppressions(findings, suppressions)
        findings = sort_findings(findings)
        max_reported = int((config.get("limits") or {}).get("max_reported_findings", 200))
        if max_reported > 0 and len(findings) > max_reported:
            limitations.append(f"Findings output capped at {max_reported} findings by config.")
            findings = findings[:max_reported]
        assign_ids(findings)

        coverage = {
            "macros_present": inv["macros_present"],
            "macros_executed": False,
            "external_links_present": bool(inv["external_links"]) or any("[" in f["formula"] for f in formulas),
            "unsupported_features": sorted(unsupported_features),
            "limitations": limitations,
        }
        workbook_meta = {
            "path": str(input_path),
            "sha256": inv["sha256"],
            "sheets_analyzed": len(allowed_sheet_names),
            "formulas_scanned": len(formulas),
            "recalc_status": recalc_status,
        }
        payload = build_payload(AUDIT_VERSION, workbook_meta, coverage, findings)
        return payload, exit_code(payload["findings"], args.fail_on, limitations)


def audit_csv(path: Path, preflight_info: dict, config: dict | None = None, ignore_path: str | None = None) -> dict:
    from suppressions import apply_suppressions, load_suppressions

    findings: list[Finding] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        for row_idx, row in enumerate(reader, start=1):
            for col_idx, value in enumerate(row, start=1):
                if value != value.strip():
                    findings.append(
                        Finding(
                            rule_id="WHITESPACE_KEY",
                            severity="Medium",
                            error_confidence="Review",
                            detection_mode="DET",
                            location=f"CSV!R{row_idx}C{col_idx}",
                            title="CSV value has leading or trailing whitespace",
                            evidence=[f"Raw value is {value!r}."],
                            suggested_fix="Trim if this field is used as a key, label, or numeric input.",
                        )
                    )
    if config:
        findings = apply_check_settings(findings, config)
    findings = apply_suppressions(findings, load_suppressions(config, ignore_path))
    findings = sort_findings(findings)
    assign_ids(findings)
    return build_payload(
        AUDIT_VERSION,
        {
            "path": str(path),
            "sha256": preflight_info["sha256"],
            "sheets_analyzed": 1,
            "formulas_scanned": 0,
            "recalc_status": "not_applicable",
        },
        {
            "macros_present": False,
            "macros_executed": False,
            "external_links_present": False,
            "unsupported_features": [],
            "limitations": ["CSV audit is limited to data-hygiene checks."],
        },
        findings,
    )


def detect_reference_issues(formula_wb, value_wb, formulas: list[dict], unsupported_features: set[str]) -> list[Finding]:
    from formula_parser import extract_functions, extract_references
    from reference_resolver import cells_from_locations, expand_reference, reference_in_bounds

    findings: list[Finding] = []
    for cell in formulas:
        formula = cell["formula"]
        if "#REF!" in formula.upper():
            findings.append(
                Finding(
                    rule_id="BROKEN_REFERENCE",
                    severity="High",
                    error_confidence="Defect",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula contains deleted reference",
                    formula=formula,
                    evidence=["Formula text contains #REF!."],
                    suggested_fix="Restore the deleted reference or rebuild the formula from intended source cells.",
                )
            )
        if "[" in formula and "]" in formula:
            unsupported_features.add("external_workbook_links")
            findings.append(
                Finding(
                    rule_id="BROKEN_REFERENCE",
                    severity="High",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula references external workbook",
                    formula=formula,
                    evidence=["External workbook links are inventoried but not followed by default."],
                    suggested_fix="Provide linked workbooks or confirm the cached linked value is current.",
                )
            )
        if "@" in formula or reuses_structured_reference(formula):
            unsupported_features.add("structured_or_dynamic_references")

        funcs = extract_functions(formula)
        if funcs.intersection({"IFERROR", "IFNA"}):
            findings.append(
                Finding(
                    rule_id="IFERROR_MASK",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="HEUR",
                    location=cell["location"],
                    title="Formula may be masking an error",
                    formula=formula,
                    evidence=[f"Formula uses {', '.join(sorted(funcs.intersection({'IFERROR', 'IFNA'})))}."],
                    suggested_fix="Inspect the wrapped expression and confirm the error case is intentional.",
                )
            )

        for ref in extract_references(formula):
            ok, reason = reference_in_bounds(ref, cell["sheet"], formula_wb)
            if not ok:
                findings.append(
                    Finding(
                        rule_id="BROKEN_REFERENCE",
                        severity="High",
                        error_confidence="Likely defect",
                        detection_mode="DET",
                        location=cell["location"],
                        title="Formula reference cannot be resolved cleanly",
                        formula=formula,
                        evidence=[reason or f"Could not resolve {ref.raw}."],
                        suggested_fix="Review the reference target and restore the intended sheet/range.",
                    )
                )
                continue
            if not ref.is_range:
                refs = expand_reference(ref, cell["sheet"], limit=1)
                for ref_loc, ref_cell in cells_from_locations(formula_wb, refs):
                    if ref_cell.value is None:
                        findings.append(
                            Finding(
                                rule_id="BLANK_PRECEDENT",
                                severity="Medium",
                                error_confidence="Review",
                                detection_mode="DET",
                                location=cell["location"],
                                title="Formula references a blank precedent",
                                formula=formula,
                                evidence=[f"Referenced cell {ref_loc} is blank."],
                                suggested_fix="Confirm the blank precedent is intentional or update the formula to the correct input.",
                            )
                        )
    return findings


def reuses_structured_reference(formula: str) -> bool:
    text = formula.upper()
    return "[" in text and "]" in text and "!" not in text


def detect_cycles(formulas: list[dict]) -> list[Finding]:
    from dependency_graph import build_dependency_graph, find_cycles

    graph = build_dependency_graph(formulas)
    cycles = find_cycles(graph)
    findings: list[Finding] = []
    for cycle in cycles:
        if len(cycle) < 2:
            continue
        findings.append(
            Finding(
                rule_id="CIRCULAR_REFERENCE",
                severity="High",
                error_confidence="Likely defect",
                detection_mode="DET",
                location=cycle[0],
                title="Formula dependency cycle detected",
                evidence=[" -> ".join(cycle[:8])],
                suggested_fix="Confirm whether iterative calculation is intentional; otherwise break the circular dependency.",
            )
        )
    return findings


def exit_code(findings: list[dict], fail_on: str, limitations: list[str]) -> int:
    if fail_on == "None":
        return 2 if limitations else 0
    threshold = FAIL_ORDER.get(fail_on, 99)
    if any(FAIL_ORDER.get(finding["severity"], 99) <= threshold and not finding.get("suppressed") for finding in findings):
        return 1
    if limitations:
        return 2
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit an existing spreadsheet for correctness defects.")
    parser.add_argument("workbook", nargs="?", help="Path to .xlsx, .xlsm, or .csv workbook")
    parser.add_argument("--out", help="Markdown report output path")
    parser.add_argument("--json", dest="json_out", help="Findings JSON output path")
    parser.add_argument("--annotated", help="Optional annotated workbook output path")
    parser.add_argument("--config", help="Optional JSON, YAML, or YML config path")
    parser.add_argument("--ignore", default=".audit-ignore", help="Optional suppression file path")
    parser.add_argument("--fail-on", default="Critical", choices=["Critical", "High", "Medium", "Low", "None"])
    parser.add_argument("--recalc-timeout", type=int, default=None)
    parser.add_argument("--healthcheck", action="store_true")
    args = parser.parse_args(argv)

    if args.healthcheck:
        return healthcheck()
    if not args.workbook:
        parser.error("workbook is required unless --healthcheck is used")

    try:
        payload, code = audit_workbook(args)
    except PreflightError as exc:
        print(f"Preflight failed: {exc}", file=sys.stderr)
        return 4
    except Exception as exc:
        print(f"Internal audit error: {exc}", file=sys.stderr)
        return 5

    if args.json_out:
        write_json(payload, args.json_out)
    if args.out:
        write_markdown(payload, args.out)
    if args.annotated:
        from annotate import annotate_workbook

        annotate_workbook(args.workbook, args.annotated, payload["findings"])

    if not args.out and not args.json_out:
        print(render_markdown(payload))
    else:
        counts = Counter(f["severity"] for f in payload["findings"] if not f.get("suppressed"))
        print(
            f"Audit complete: {counts.get('Critical', 0)} Critical, "
            f"{counts.get('High', 0)} High, {counts.get('Medium', 0)} Medium, "
            f"{counts.get('Low', 0)} Low."
        )
    return code


if __name__ == "__main__":
    raise SystemExit(main())
