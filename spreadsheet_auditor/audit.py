from __future__ import annotations

import argparse
import contextlib
import csv
import importlib.resources
import json
import platform
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

from . import __version__
from .budget import AuditTimeout, Budget
from .config_loader import allowed_sheets, apply_check_settings, load_config, sheet_is_allowed
from .finding import Finding, assign_ids, sort_findings
from .locations import location_matches
from .names import NameTable
from .preflight import PreflightError, preflight
from .recalc import recalc_if_available, soffice_path
from .report import (
    build_payload,
    render_html,
    render_markdown,
    write_html,
    write_json,
    write_markdown,
)

AUDIT_VERSION = __version__
FAIL_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "None": 99}


REQUIRED_PACKAGES = ["openpyxl"]
OPTIONAL_PACKAGES = ["defusedxml", "yaml"]


def _probe_package(package: str) -> dict:
    try:
        module = __import__(package)
        return {
            "name": package,
            "status": "installed",
            "version": getattr(module, "__version__", "unknown"),
        }
    except Exception:
        return {"name": package, "status": "missing", "version": None}


def collect_healthcheck() -> dict:
    required = [_probe_package(pkg) for pkg in REQUIRED_PACKAGES]
    optional = [_probe_package(pkg) for pkg in OPTIONAL_PACKAGES]
    libreoffice_path = soffice_path()
    libreoffice = {
        "path": libreoffice_path,
        "status": "found" if libreoffice_path else "missing",
    }
    recalculation_mode = "available" if libreoffice_path else "cached_values_only"
    missing_required = [pkg["name"] for pkg in required if pkg["status"] == "missing"]
    return {
        "tool_version": AUDIT_VERSION,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "required_packages": required,
        "optional_packages": optional,
        "libreoffice": libreoffice,
        "recalculation_mode": recalculation_mode,
        "macro_execution": "disabled",
        "external_links": "inventoried_only",
        "supported_file_types": [".xlsx", ".xlsm", ".csv"],
        "status": "ready" if not missing_required else "missing_required_dependencies",
        "missing_required": missing_required,
    }


def _render_healthcheck(info: dict) -> str:
    lines = [
        f"Spreadsheet Auditor Healthcheck (v{info['tool_version']})",
        "",
        f"Python: {info['python']} OK",
    ]
    for pkg in info["required_packages"]:
        status = "OK" if pkg["status"] == "installed" else "MISSING"
        version = pkg["version"] or "n/a"
        lines.append(f"{pkg['name']}: {pkg['status']} ({version}) {status}")
    for pkg in info["optional_packages"]:
        if pkg["status"] == "installed":
            lines.append(f"{pkg['name']}: installed ({pkg['version']}) OK")
        else:
            lines.append(f"{pkg['name']}: not installed (optional)")
    if info["libreoffice"]["status"] == "found":
        lines.append(f"LibreOffice: found at {info['libreoffice']['path']} OK")
    else:
        lines.append("LibreOffice: not installed (optional; value-dependent checks limited)")
    lines.append(f"Recalculation mode: {info['recalculation_mode']}")
    lines.append(f"Macro execution: {info['macro_execution']}")
    lines.append(f"External links: {info['external_links']}")
    lines.append("")
    if info["missing_required"]:
        lines.append(f"Status: missing required dependencies: {', '.join(info['missing_required'])}")
    else:
        lines.append("Status: ready")
    return "\n".join(lines)


def healthcheck(as_json: bool = False) -> int:
    info = collect_healthcheck()
    if as_json:
        print(json.dumps(info, indent=2))
    else:
        print(_render_healthcheck(info))
    return 0 if not info["missing_required"] else 3


def _package_available(package: str) -> bool:
    try:
        __import__(package)
        return True
    except Exception:
        return False


def audit_workbook(args: argparse.Namespace) -> tuple[dict, int]:
    from .suppressions import apply_suppressions, load_suppressions
    from .workbook_inventory import (
        formula_cells,
        inventory,
        load_workbook_formulas,
        load_workbook_values,
    )

    input_path = Path(args.workbook)
    preflight_info = preflight(input_path)
    config = load_config(args.config)
    limitations: list[str] = []
    unsupported_features: set[str] = set()
    findings: list[Finding] = []
    truncated = {"formulas": False, "findings": False, "cells": False, "timeout": False}
    start_time = time.monotonic()
    limits_config = config.get("limits") or {}
    timeout_seconds = int(limits_config.get("timeout_seconds", 0) or 0)
    budget = Budget(timeout_seconds, start=start_time)

    def _note_timeout(detail: str) -> None:
        if not truncated["timeout"]:
            truncated["timeout"] = True
            limitations.append(f"Audit timeout of {timeout_seconds}s exceeded; {detail}")

    if preflight_info["extension"] == ".csv":
        payload = audit_csv(input_path, preflight_info, config, args.ignore)
        return payload, exit_code(
            payload["findings"], args.fail_on, payload["coverage"]["limitations"], strict=args.strict
        )

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

        # Static checks always read the original workbook so formula text is
        # exactly what the author wrote; LibreOffice re-serializes formulas
        # (for example ``=SUM(#ref!)``) in its converted copy. That copy, when
        # recalculation ran, only supplies cached values.
        formula_wb = load_workbook_formulas(input_path)
        value_wb = load_workbook_values(analysis_path)
        inv = inventory(input_path, formula_wb, value_wb, preflight_info)
        include, exclude = allowed_sheets(config)
        allowed_sheet_names = {
            ws.title for ws in formula_wb.worksheets if sheet_is_allowed(ws.title, include, exclude)
        }
        if "max_range_expansion_cells" in limits_config:
            limitations.append(
                "limits.max_range_expansion_cells is deprecated and ignored; ranges are resolved "
                "exactly against the formula index, so no reference is dropped for being large."
            )
        if getattr(args, "annotated", None) and preflight_info.get("drawing_parts"):
            limitations.append(
                f"The annotated copy is written by openpyxl, which does not preserve drawings, charts, "
                f"images, or form controls; this workbook contains {preflight_info['drawing_parts']} "
                "such part(s) that the copy will drop. Keep the original workbook as the master."
            )
        # Cell-count guardrail (cheap to compute).
        max_cells = int(limits_config.get("max_cells", 1_000_000) or 0)
        total_cells = 0
        for ws in formula_wb.worksheets:
            if ws.title not in allowed_sheet_names:
                continue
            total_cells += int(ws.max_row or 0) * int(ws.max_column or 0)
        grid_scan_allowed = True
        if max_cells > 0 and total_cells > max_cells:
            truncated["cells"] = True
            grid_scan_allowed = False
            limitations.append(
                f"Cell scan capped: workbook reports {total_cells} cells, exceeding the configured "
                f"max_cells={max_cells}; cell-grid checks (HARDCODE_IN_FORMULA_BLOCK, CROSS_FOOT_FAILURE, "
                "data hygiene) were skipped. Formula-based checks still ran."
            )

        all_formulas = formula_cells(formula_wb)
        formulas = [cell for cell in all_formulas if cell["sheet"] in allowed_sheet_names]
        max_formulas = int(limits_config.get("max_formulas", 50000))
        if max_formulas > 0 and len(formulas) > max_formulas:
            truncated["formulas"] = True
            limitations.append(f"Formula scan capped at {max_formulas} formulas by config.")
            formulas = formulas[:max_formulas]

        from .checks import CheckContext, checks as registered_checks

        names = NameTable.from_workbook(formula_wb)
        array_formulas = int(inv.get("array_formulas", 0) or 0)
        if array_formulas:
            unsupported_features.add("array_formulas")
            limitations.append(
                f"{array_formulas} array formula(s) were parsed for references only; "
                "array and spill semantics are not evaluated."
            )
        ctx = CheckContext(
            workbook_path=input_path,
            formula_wb=formula_wb,
            value_wb=value_wb,
            allowed_sheet_names=allowed_sheet_names,
            formulas=formulas,
            config=config,
            inventory=inv,
            unsupported_features=unsupported_features,
            names=names,
            budget=budget,
            grid_scan_allowed=grid_scan_allowed,
        )
        for check_cls in registered_checks():
            check_name = getattr(check_cls, "name", "") or check_cls.__name__
            if budget.expired():
                _note_timeout(f"'{check_name}' and remaining checks were skipped.")
                break
            check = check_cls()
            try:
                findings.extend(check.run(ctx))
            except AuditTimeout:
                _note_timeout(f"'{check_name}' was interrupted and remaining checks were skipped.")
                break
            except Exception as exc:
                limitations.append(
                    f"Check '{check_name}' raised an exception and was skipped: {exc!r}"
                )

        findings = _dedupe_range_length_with_drift(findings)
        if recalc_status != "completed":
            limitations.append(
                "Recalculation did not run; value-dependent checks (TOTAL_MISMATCH, CROSS_FOOT_FAILURE) "
                "rely on cached values and may be incomplete."
            )

        findings = apply_impact_escalation(findings, config)
        findings = apply_check_settings(findings, config)
        suppressions = load_suppressions(config, args.ignore, warnings=limitations)
        findings = apply_suppressions(findings, suppressions)
        findings = sort_findings(findings)
        max_reported = int(limits_config.get("max_reported_findings", 200))
        if max_reported > 0 and len(findings) > max_reported:
            truncated["findings"] = True
            limitations.append(f"Findings output capped at {max_reported} findings by config.")
            findings = findings[:max_reported]
        assign_ids(findings)

        coverage = {
            "macros_present": inv["macros_present"],
            "macros_executed": False,
            "external_links_present": bool(inv["external_links"]) or "external_workbook_links" in unsupported_features,
            "unsupported_features": sorted(unsupported_features),
            "limitations": limitations,
            "truncated": truncated,
            "elapsed_seconds": round(time.monotonic() - start_time, 3),
        }
        workbook_meta = {
            "path": input_path.as_posix(),
            "sha256": inv["sha256"],
            "sheets_analyzed": len(allowed_sheet_names),
            "formulas_scanned": len(formulas),
            "recalc_status": recalc_status,
        }
        payload = build_payload(AUDIT_VERSION, workbook_meta, coverage, findings)
        return payload, exit_code(payload["findings"], args.fail_on, limitations, strict=args.strict)


def audit_csv(path: Path, preflight_info: dict, config: dict | None = None, ignore_path: str | None = None) -> dict:
    from .suppressions import apply_suppressions, load_suppressions

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
    csv_limitations = ["CSV audit is limited to data-hygiene checks."]
    if config:
        findings = apply_check_settings(findings, config)
    findings = apply_suppressions(
        findings, load_suppressions(config, ignore_path, warnings=csv_limitations)
    )
    findings = sort_findings(findings)
    assign_ids(findings)
    return build_payload(
        AUDIT_VERSION,
        {
            "path": Path(path).as_posix(),
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
            "limitations": csv_limitations,
        },
        findings,
    )


def detect_reference_issues(
    formula_wb,
    value_wb,
    formulas: list[dict],
    unsupported_features: set[str],
    names=None,
    budget=None,
) -> list[Finding]:
    from .formula_parser import parse_formula
    from .reference_resolver import boundaries, existing_cell, find_sheet, reference_in_bounds
    from .workbook_inventory import iter_existing_cells

    occupancy: dict[str, tuple[set[int], set[int]]] = {}

    def occupied(title: str) -> tuple[set[int], set[int]]:
        if title not in occupancy:
            rows: set[int] = set()
            cols: set[int] = set()
            for existing in iter_existing_cells(formula_wb[title]):
                if existing.value is not None:
                    rows.add(existing.row)
                    cols.add(existing.column)
            occupancy[title] = (rows, cols)
        return occupancy[title]

    findings: list[Finding] = []
    for cell in formulas:
        if budget is not None:
            budget.tick()
        formula = cell["formula"]
        parsed = parse_formula(formula, names=names, origin=(cell["sheet"], cell["row"], cell["col"]))
        if parsed.parse_error:
            unsupported_features.add("unparseable_formulas")
            continue
        if parsed.deleted_reference:
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
        if parsed.external_references:
            unsupported_features.add("external_workbook_links")
            shown = ", ".join(parsed.external_references[:5])
            findings.append(
                Finding(
                    rule_id="BROKEN_REFERENCE",
                    severity="High",
                    error_confidence="Review",
                    detection_mode="DET",
                    location=cell["location"],
                    title="Formula references external workbook",
                    formula=formula,
                    evidence=[f"External workbook links are inventoried but not followed by default: {shown}."],
                    suggested_fix="Provide linked workbooks or confirm the cached linked value is current.",
                )
            )
        if parsed.unresolved_structured:
            unsupported_features.add("structured_references")
        if parsed.three_d_references:
            unsupported_features.add("3d_references")
        if parsed.implicit_intersection or parsed.spill:
            unsupported_features.add("structured_or_dynamic_references")
        if parsed.unresolved_names and not parsed.functions.intersection({"LET", "LAMBDA"}):
            unsupported_features.add("unresolved_defined_names")

        masks = parsed.functions.intersection({"IFERROR", "IFNA"})
        if masks:
            findings.append(
                Finding(
                    rule_id="IFERROR_MASK",
                    severity="Medium",
                    error_confidence="Review",
                    detection_mode="HEUR",
                    location=cell["location"],
                    title="Formula may be masking an error",
                    formula=formula,
                    evidence=[f"Formula uses {', '.join(sorted(masks))}."],
                    suggested_fix="Inspect the wrapped expression and confirm the error case is intentional.",
                )
            )

        for ref in parsed.references:
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
            if ref.is_range or not ref.bounded:
                continue
            box = boundaries(ref.ref)
            if box is None:
                continue
            title = find_sheet(formula_wb, ref.sheet or cell["sheet"])
            if title is None:
                continue
            target = existing_cell(formula_wb[title], box[1], box[0])
            if target is None or target.value is None:
                occupied_rows, occupied_cols = occupied(title)
                if box[1] not in occupied_rows or box[0] not in occupied_cols:
                    # An entirely empty row or column is unused space (future
                    # periods, spare inputs), not a broken link.
                    continue
                findings.append(
                    Finding(
                        rule_id="BLANK_PRECEDENT",
                        severity="Medium",
                        error_confidence="Review",
                        detection_mode="DET",
                        location=cell["location"],
                        title="Formula references a blank precedent",
                        formula=formula,
                        evidence=[f"Referenced cell {title}!{ref.ref} is blank."],
                        suggested_fix="Confirm the blank precedent is intentional or update the formula to the correct input.",
                    )
                )
    return findings


def _dedupe_range_length_with_drift(findings: list[Finding]) -> list[Finding]:
    drift_locations = {f.location for f in findings if f.rule_id == "FORMULA_DRIFT"}
    return [
        f
        for f in findings
        if not (f.rule_id == "RANGE_LENGTH_MISMATCH" and f.location in drift_locations)
    ]


def apply_impact_escalation(findings: list[Finding], config: dict) -> list[Finding]:
    """Escalate findings that feed configured headline outputs or exceed materiality.

    Activates scope.headline_outputs and materiality config and records impact
    flags on each affected finding.
    """
    from .materiality import escalate, exceeds_materiality

    scope = config.get("scope") or {}
    headline_outputs = list(scope.get("headline_outputs") or [])
    materiality = config.get("materiality") or {}
    absolute = float(materiality.get("absolute", 1000.0))
    relative = float(materiality.get("relative", 0.001))

    for finding in findings:
        should_escalate = False

        if any(location_matches(finding.location, target) for target in headline_outputs):
            finding.impact["feeds_headline_output"] = True
            should_escalate = True

        delta = finding.impact.get("estimated_delta") if isinstance(finding.impact, dict) else None
        if delta is not None and exceeds_materiality(delta, absolute=absolute, relative=relative):
            finding.impact["materiality_exceeded"] = True
            should_escalate = True

        if should_escalate:
            finding.severity = escalate(finding.severity)

    return findings


def detect_cycles(
    formulas: list[dict],
    expansion_limit: int | None = None,
    names=None,
    extents: dict[str, tuple[int, int]] | None = None,
    budget=None,
) -> list[Finding]:
    """Report one CIRCULAR_REFERENCE finding per cyclic dependency component.

    ``expansion_limit`` is accepted for backward compatibility and ignored; see
    :func:`spreadsheet_auditor.dependency_graph.build_dependency_graph`.
    """
    from .dependency_graph import build_dependency_graph, find_cycles

    graph = build_dependency_graph(formulas, names=names, extents=extents, budget=budget)
    findings: list[Finding] = []
    for members in find_cycles(graph):
        if len(members) == 1:
            title = "Formula references its own cell"
            evidence = [
                f"{members[0]} depends on itself, for example a total whose range includes the total cell."
            ]
        else:
            title = "Formula dependency cycle detected"
            shown = " -> ".join(members[:8]) + (" -> ..." if len(members) > 8 else "")
            evidence = [f"{len(members)} cells depend on each other in a cycle: {shown}"]
        findings.append(
            Finding(
                rule_id="CIRCULAR_REFERENCE",
                severity="High",
                error_confidence="Likely defect",
                detection_mode="DET",
                location=members[0],
                title=title,
                evidence=evidence,
                suggested_fix="Confirm whether iterative calculation is intentional; otherwise break the circular dependency.",
            )
        )
    return findings


def _infer_format(path: str | None, explicit: str | None) -> str:
    if explicit:
        return explicit
    if not path:
        return "markdown"
    lower = path.lower()
    if lower.endswith((".html", ".htm")):
        return "html"
    if lower.endswith(".json"):
        return "json"
    if lower.endswith(".sarif") or lower.endswith(".sarif.json"):
        return "sarif"
    return "markdown"


def _write_report(
    payload: dict,
    path: str,
    explicit_format: str | None,
    show_suppressed: bool = False,
) -> None:
    fmt = _infer_format(path, explicit_format)
    if fmt == "html":
        write_html(payload, path, show_suppressed=show_suppressed)
    elif fmt == "json":
        write_json(payload, path)
    elif fmt == "sarif":
        # SARIF is a strict, validated format. If rendering fails we must NOT
        # silently write generic findings JSON to a .sarif path; that would make
        # the run look successful while emitting an invalid SARIF file. Let the
        # exception propagate so the CLI exits with code 5.
        from .sarif import write_sarif

        write_sarif(payload, path)
    else:
        write_markdown(payload, path, show_suppressed=show_suppressed)


def exit_code(findings: list[dict], fail_on: str, limitations: list[str], strict: bool = False) -> int:
    threshold = FAIL_ORDER.get(fail_on, 99)
    if fail_on != "None" and any(
        FAIL_ORDER.get(finding["severity"], 99) <= threshold and not finding.get("suppressed")
        for finding in findings
    ):
        return 1
    # Benign limitations (no recalc, missing optional packages) are expected on a
    # clean run and must not fail CI. Only surface them as exit code 2 when the
    # caller explicitly opts in via --strict or --fail-on None.
    if (strict or fail_on == "None") and limitations:
        return 2
    return 0


EPILOG = """\
Exit codes:
  0  No findings at or above --fail-on (default Critical), or --fail-on None.
  1  Findings at or above --fail-on were detected.
  2  --strict (or --fail-on None) and coverage limitations were present
     (e.g. recalculation unavailable, defusedxml missing).
  3  Healthcheck failed: required dependencies missing.
  4  Preflight error: workbook is unreadable or has the wrong shape.
  5  Internal auditor error. Re-run with the same arguments and attach
     stderr to a bug report.

Examples:
  spreadsheet-auditor model.xlsx --out report.md --json findings.json
  spreadsheet-auditor model.xlsx --format html --out report.html
  spreadsheet-auditor model.xlsx --summary
  spreadsheet-auditor --demo
  spreadsheet-auditor --healthcheck --json
"""


def _summary_lines(payload: dict, fail_on: str) -> list[str]:
    findings = [f for f in payload["findings"] if not f.get("suppressed")]
    counts = Counter(f["severity"] for f in findings)
    coverage = payload.get("coverage", {})
    workbook = payload.get("workbook", {})
    lines = [
        f"workbook   : {workbook.get('path')}",
        f"sheets     : {workbook.get('sheets_analyzed')}",
        f"formulas   : {workbook.get('formulas_scanned')}",
        f"recalc     : {workbook.get('recalc_status')}",
        "findings   : "
        + ", ".join(
            f"{counts.get(sev, 0)} {sev}" for sev in ("Critical", "High", "Medium", "Low", "Info")
        ),
        f"fail_on    : {fail_on}",
    ]
    limitations = coverage.get("limitations") or []
    if limitations:
        lines.append("limitations:")
        for note in limitations:
            lines.append(f"  - {note}")
    return lines


def _configure_streams() -> None:
    """Never let a non-ASCII cell label crash report output on a legacy console encoding."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        encoding = (getattr(stream, "encoding", "") or "").replace("-", "").lower()
        try:
            if encoding == "utf8":
                reconfigure(errors="replace")
            else:
                reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):  # pragma: no cover - exotic streams
            pass


def main(argv: list[str] | None = None) -> int:
    _configure_streams()
    parser = argparse.ArgumentParser(
        prog="spreadsheet-auditor",
        description="Audit an existing spreadsheet for correctness defects.",
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("workbook", nargs="?", help="Path to .xlsx, .xlsm, or .csv workbook (omit when using --healthcheck or --demo)")
    parser.add_argument("--out", help="Report output path. Format inferred from extension or --format.")
    parser.add_argument(
        "--json",
        dest="json_out",
        nargs="?",
        const="-",
        default=None,
        help=(
            "Findings JSON output path. Pass '-' (or no value) to write JSON to stdout. "
            "With --healthcheck, --json (no value) emits the machine-readable healthcheck report."
        ),
    )
    parser.add_argument("--annotated", help="Optional annotated workbook output path. The source workbook is never modified.")
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "html", "sarif"],
        default=None,
        dest="report_format",
        help="Report format. Inferred from --out extension when omitted.",
    )
    parser.add_argument("--config", help="Optional JSON, YAML, or YML config path")
    parser.add_argument("--ignore", default=".audit-ignore", help="Suppression file path (default '.audit-ignore').")
    parser.add_argument(
        "--fail-on",
        default="Critical",
        choices=["Critical", "High", "Medium", "Low", "None"],
        help="Lowest severity that causes a non-zero exit code (default: Critical).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 2 when coverage limitations are present (e.g. recalculation unavailable).",
    )
    parser.add_argument(
        "--show-suppressed",
        action="store_true",
        help="Render suppressed findings in the report instead of hiding them.",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print a one-screen summary (counts, coverage, limitations) instead of the full report.",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress all stdout output. Useful in CI when only the exit code matters.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Audit the bundled demo workbook (examples/demo_bad_budget.xlsx). Useful for a 60-second tour.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"spreadsheet-auditor {__version__}",
    )
    parser.add_argument("--recalc-timeout", type=int, default=None, help="Override recalculation timeout in seconds.")
    parser.add_argument("--healthcheck", action="store_true", help="Report environment/runtime readiness and exit.")
    args = parser.parse_args(argv)

    if args.healthcheck:
        return healthcheck(as_json=args.json_out is not None)

    with contextlib.ExitStack() as stack:
        if args.demo:
            demo_path = stack.enter_context(_resolve_demo_workbook())
            if demo_path is None:
                print(
                    "Demo workbook not found. Generate it with `python examples/make_demo.py`.",
                    file=sys.stderr,
                )
                return 4
            args.workbook = str(demo_path)

        if not args.workbook:
            parser.error("workbook is required unless --healthcheck or --demo is used")

        try:
            payload, code = audit_workbook(args)
        except PreflightError as exc:
            print(f"Preflight failed: {exc}", file=sys.stderr)
            return 4
        except Exception as exc:
            print(f"Internal audit error: {exc}", file=sys.stderr)
            return 5

        try:
            if args.json_out:
                if args.json_out == "-":
                    if not args.quiet:
                        print(json.dumps(payload, indent=2))
                else:
                    write_json(payload, args.json_out)
            if args.out:
                _write_report(payload, args.out, args.report_format, show_suppressed=args.show_suppressed)
            if args.annotated:
                from .annotate import annotate_workbook

                annotate_workbook(args.workbook, args.annotated, payload["findings"])
                for note in payload.get("coverage", {}).get("limitations", []):
                    if note.startswith("The annotated copy"):
                        print(f"Warning: {note}", file=sys.stderr)
        except Exception as exc:
            print(f"Failed to write output: {exc}", file=sys.stderr)
            return 5

        if args.quiet:
            return code

        if args.summary:
            for line in _summary_lines(payload, args.fail_on):
                print(line)
            return code

        if not args.out and not args.json_out:
            if args.report_format == "html":
                print(render_html(payload, show_suppressed=args.show_suppressed))
            elif args.report_format == "json":
                print(json.dumps(payload, indent=2))
            else:
                print(render_markdown(payload, show_suppressed=args.show_suppressed))
        elif not args.out and args.json_out == "-":
            # already printed JSON above; nothing else to do
            pass
        else:
            counts = Counter(f["severity"] for f in payload["findings"] if not f.get("suppressed"))
            print(
                f"Audit complete: {counts.get('Critical', 0)} Critical, "
                f"{counts.get('High', 0)} High, {counts.get('Medium', 0)} Medium, "
                f"{counts.get('Low', 0)} Low."
            )
        return code


@contextlib.contextmanager
def _resolve_demo_workbook():
    """Yield a filesystem path to the bundled demo workbook, or ``None``.

    Resolution order:

    1. A repository checkout (``examples/demo_bad_budget.xlsx`` next to the
       package or under the current working directory) so development uses the
       canonical copy.
    2. The packaged resource ``spreadsheet_auditor/demo/demo_bad_budget.xlsx``
       so installed wheels and unpacked skill packages work too.

    Yielded as a context manager because the packaged resource may live inside a
    zip and must be materialized via :func:`importlib.resources.as_file`; the
    real path stays valid for the lifetime of the ``with`` block. Callers (recalc,
    annotation) re-open the path, so the context must wrap the whole audit.
    """
    for candidate in (
        Path(__file__).resolve().parents[1] / "examples" / "demo_bad_budget.xlsx",
        Path.cwd() / "examples" / "demo_bad_budget.xlsx",
    ):
        if candidate.exists():
            yield candidate
            return
    try:
        resource = importlib.resources.files("spreadsheet_auditor.demo") / "demo_bad_budget.xlsx"
        if resource.is_file():
            with importlib.resources.as_file(resource) as path:
                yield path
                return
    except (ModuleNotFoundError, FileNotFoundError):
        pass
    yield None


if __name__ == "__main__":
    raise SystemExit(main())
