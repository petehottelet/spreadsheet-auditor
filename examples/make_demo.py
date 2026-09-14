"""Generate the demo workbook plus its audit outputs.

Builds `examples/demo_bad_budget.xlsx` with a curated set of seeded defects,
then runs the auditor to refresh `demo_audit_report.md`, `demo_findings.json`,
`demo_audit_report.html`, and `demo_annotated.xlsx`.

Every cell in the workbook is otherwise correct, so every finding the auditor
reports against it should map to a seeded defect listed in
`benchmarks/seeded_defects.json`.

Run from the repo root:

    python examples/make_demo.py
    python examples/make_demo.py --workbook-only   # regenerate the .xlsx only
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
WORKBOOK = EXAMPLES / "demo_bad_budget.xlsx"
REPORT_MD = EXAMPLES / "demo_audit_report.md"
REPORT_HTML = EXAMPLES / "demo_audit_report.html"
FINDINGS_JSON = EXAMPLES / "demo_findings.json"
ANNOTATED = EXAMPLES / "demo_annotated.xlsx"
# Packaged copy that ships inside the wheel/skill so `--demo` works when the
# repo `examples/` directory is not on disk. Kept in sync from WORKBOOK below.
PACKAGED_DEMO = ROOT / "spreadsheet_auditor" / "demo" / "demo_bad_budget.xlsx"


def build_workbook() -> None:
    """Build a small budget workbook seeded with realistic-looking defects.

    Rows are labelled so reviewers can see why each finding is interesting.
    Seeded defects (see benchmarks/seeded_defects.json):

    * B6  adds B5 on top of SUM(B4:B5)      -> TOTAL_MISMATCH (double count), FORMULA_DRIFT
    * E6  sums B6:C6 instead of B6:D6       -> FORMULA_DRIFT in the total column
    * E9  literal 999 in the total column   -> HARDCODE_IN_FORMULA_BLOCK
    * B10 sums B7:B8 and drops Marketing    -> RANGE_EXCLUSION, FORMULA_DRIFT
    * row 12 hidden but feeds row 13        -> HIDDEN_STRUCTURE_IN_TOTAL
    * B14 =SUM(#REF!)                       -> BROKEN_REFERENCE, LIVE_ERROR (after recalc)
    * A17/A18 "North" and " North " keys    -> DUPLICATE_KEY, WHITESPACE_KEY
    * B20 "1,250" stored as text, summed    -> NUMBERS_STORED_AS_TEXT
    * E6 corner does not cross-foot         -> CROSS_FOOT_FAILURE (after recalc)
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Budget"

    ws.append(["Line item", "Jan", "Feb", "Mar", "Q1 total"])  # row 1
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = PatternFill("solid", fgColor="DDEBF7")

    ws.append(["Subscriptions", 1200, 1320, 1450, "=SUM(B2:D2)"])  # row 2
    ws.append(["Services", 800, 820, 900, "=SUM(B3:D3)"])  # row 3
    ws.append(["Subtotal", "=SUM(B2:B3)", "=SUM(C2:C3)", "=SUM(D2:D3)", "=SUM(B4:D4)"])  # row 4
    ws.append(["Other revenue", 150, 175, 200, "=SUM(B5:D5)"])  # row 5
    # Revenue total = subtotal + other revenue. B6 double-counts B5; E6 drops D6.
    ws.append(["Revenue total", "=SUM(B4:B5)+B5", "=SUM(C4:C5)", "=SUM(D4:D5)", "=SUM(B6:C6)"])  # row 6

    ws.append(["Hosting", 200, 210, 220, "=SUM(B7:D7)"])  # row 7
    ws.append(["Support staff", 600, 620, 640, "=SUM(B8:D8)"])  # row 8
    ws.append(["Marketing", 300, 320, 340, 999])  # row 9: hardcoded plug in the total column
    # COGS total. B10 stops at row 8 and silently drops Marketing.
    ws.append(["COGS total", "=SUM(B7:B8)", "=SUM(C7:C9)", "=SUM(D7:D9)", "=SUM(B10:D10)"])  # row 10
    ws.append(["Net", "=B6-B10", "=C6-C10", "=D6-D10", "=SUM(B11:D11)"])  # row 11

    # Hidden row that still feeds the row below it.
    ws.append(["Adjustment (hidden)", 50, 60, 70, "=SUM(B12:D12)"])  # row 12
    ws.row_dimensions[12].hidden = True
    ws.append(["With adjustment", "=B11+B12", "=C11+C12", "=D11+D12", "=SUM(B13:D13)"])  # row 13

    # Deleted reference.
    ws.append(["Stale link", "=SUM(#REF!)", None, None, None])  # row 14

    # Lookup table with a duplicate, whitespace-padded key.
    ws.append([])  # row 15
    ws.append(["Region", "Owner"])  # row 16
    ws.append(["North", "Alex"])  # row 17
    ws.append([" North ", "Sam"])  # row 18
    ws.append(["South", "Jess"])  # row 19

    # Number stored as text, consumed by a SUM on the summary sheet.
    ws.append(["Bonus pool", "1,250"])  # row 20

    summary = wb.create_sheet("Summary")
    summary["A1"] = "Headline KPI"
    summary["B1"] = "Total revenue"
    summary["C1"] = "=Budget!B6"  # depends on the double-counted row 6
    summary["A2"] = "Owner lookup"
    summary["B2"] = "North"
    summary["C2"] = "=VLOOKUP(B2,Budget!A17:B19,2,FALSE)"  # searches the duplicate keys
    summary["A3"] = "Bonus accrual"
    summary["B3"] = "Pool"
    summary["C3"] = "=SUM(Budget!B20:B20)"  # sums the text number and gets 0

    wb.save(WORKBOOK)
    PACKAGED_DEMO.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(WORKBOOK, PACKAGED_DEMO)


def _rel(path: Path) -> str:
    # Run the auditor with repo-relative paths so the committed outputs never
    # embed a maintainer's absolute directory.
    return path.relative_to(ROOT).as_posix()


def regenerate_outputs() -> int:
    cmd = [
        sys.executable,
        "-m",
        "spreadsheet_auditor",
        _rel(WORKBOOK),
        "--out",
        _rel(REPORT_MD),
        "--json",
        _rel(FINDINGS_JSON),
        "--annotated",
        _rel(ANNOTATED),
    ]
    # Auditor exits 1 when findings are present; that is the expected outcome
    # here because the demo workbook is intentionally broken.
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode not in (0, 1):
        sys.stderr.write(result.stderr)
        return result.returncode

    html_cmd = [
        sys.executable,
        "-m",
        "spreadsheet_auditor",
        _rel(WORKBOOK),
        "--out",
        _rel(REPORT_HTML),
        "--format",
        "html",
    ]
    html_result = subprocess.run(html_cmd, capture_output=True, text=True, cwd=ROOT)
    if html_result.returncode not in (0, 1):
        sys.stderr.write(html_result.stderr)
        return html_result.returncode
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    EXAMPLES.mkdir(parents=True, exist_ok=True)
    build_workbook()
    print(f"Wrote {WORKBOOK}")
    print(f"Synced packaged demo copy {PACKAGED_DEMO}")
    if "--workbook-only" in args:
        return 0
    code = regenerate_outputs()
    if code == 0:
        for path in [REPORT_MD, FINDINGS_JSON, ANNOTATED, REPORT_HTML]:
            if path.exists():
                print(f"Wrote {path}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
