<p align="center">
  <img src="project_logo.png" alt="Spreadsheet Auditor logo" width="360">
</p>

<h1 align="center">Spreadsheet Auditor</h1>

<p align="center">
  <strong>Audit existing Excel spreadsheets and financial models for correctness defects &mdash; formula errors, broken references, bad ranges, totals that don't reconcile, and data-quality risks.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Claude%20%2B%20Codex-Agent%20Skill-orange.svg" alt="Claude + Codex Agent Skill">
  <img src="https://img.shields.io/badge/formats-.xlsx%20%7C%20.xlsm%20%7C%20.csv-lightgrey.svg" alt="Supported formats">
</p>

---

`spreadsheet-auditor` is a portable [Agent Skill](https://agentskills.io/specification) for **Claude and Codex** (plus a standalone command-line toolkit) that answers one question: **"Can I trust this spreadsheet?"**

Most spreadsheet tooling helps you *build* workbooks. This one *audits* a workbook you already have &mdash; often one you inherited &mdash; and returns a severity-ranked report of where it is likely wrong, fragile, or inconsistent. It is deterministic-first: bundled Python scripts produce candidate findings with exact cell locations and evidence, so you are not eyeballing cells and guessing.

It is intentionally **audit-only**: it reports defects and optional annotations, but never silently rewrites, reformats, or "fixes" your source workbook.

## Why use it

- **Pre-send model review** &mdash; de-risk an LBO/DCF/budget model before it reaches an investment committee or counterparty.
- **"Find the error" debugging** &mdash; a number looks wrong and you need the cell, not a guess.
- **Inherited-model trust assessment** &mdash; you didn't build it; check whether it is trustworthy.
- **CI / batch gating** &mdash; fail a pipeline when a committed workbook has Critical defects.
- **FP&A and month-end close** &mdash; catch reconciliation and range mistakes in recurring workbooks.

## What it detects

| Category | Checks |
|---|---|
| Formula integrity | live errors (`#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, ...), broken/deleted references, references to blank precedents, circular references, formula drift across a row/column, `IFERROR`/`IFNA` error masking |
| Hardcodes & inputs | numeric literals embedded in formulas, hardcoded plug values inside a formula block |
| Ranges | aggregate ranges that exclude adjacent data (off-by-one), ranges that include subtotal/total rows, inconsistent aggregate range lengths across peers, hidden rows/columns/sheets inside totals |
| Reconciliation | stated totals that differ from their components, row totals vs column totals that don't cross-foot |
| Logic & structure | volatile/fragile functions (`OFFSET`, `INDIRECT`, `NOW`, `RAND`, ...), whole-column references |
| Data hygiene | numbers stored as text, leading/trailing whitespace in keys/labels, duplicate lookup keys, merged cells inside data ranges |

Each finding carries a detection mode (`DET` deterministic / `HEUR` heuristic), an error-confidence level (`Defect` / `Likely defect` / `Review`), a severity, evidence, and a suggested fix. See [`references/check_catalog.md`](references/check_catalog.md) for the full rule list.

## Quick Start

```bash
python scripts/audit.py path/to/workbook.xlsx --out audit_report.md --json findings.json
```

Inspect runtime capabilities:

```bash
python scripts/audit.py --healthcheck
```

Build distributable Skill packages (Claude + Codex):

```bash
python scripts/build_dist.py
```

Run the test suite:

```bash
pip install -r requirements-dev.txt
python -m pytest tests -q
```

## Outputs

- Markdown report for human review.
- `findings.json` for reruns, CI, and downstream tooling (validates against [`schemas/findings.schema.json`](schemas/findings.schema.json)).
- Optional annotated workbook copy with comments at finding cells when `--annotated` is provided. The source workbook is never modified.

## Exit codes

| Code | Meaning |
|---:|---|
| 0 | Completed; no findings at or above `--fail-on` |
| 1 | Completed; findings at or above `--fail-on` |
| 2 | Completed with coverage limitations (only with `--strict` or `--fail-on None`) |
| 4 | Preflight/security failure |
| 5 | Internal error |

Benign limitations (no recalculation engine, missing optional packages) do not fail a normal run. Use `--strict` to surface them as exit code `2` in CI.

## Dependencies

Required for `.xlsx` and `.xlsm` auditing:

- Python 3.11+
- `openpyxl`

Used when available (the audit degrades gracefully without them):

- `defusedxml` for safer XML parsing.
- `networkx` for graph cycle detection (a DFS fallback is built in).
- LibreOffice / `soffice` for recalculation; without it, value-dependent checks (`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) rely on cached values and are reported as limited.
- `PyYAML` for YAML config files (JSON config works without it).

Install runtime deps with `pip install -r requirements.txt`, or dev/CI deps with `pip install -r requirements-dev.txt`.

## Safety

Spreadsheet files are treated as untrusted input. Macros are inventoried but never executed, external links are inventoried but never followed, recalculation runs headless in an isolated profile, and the original workbook is never overwritten. See [`references/limitations.md`](references/limitations.md).

## FAQ

**Does it fix my spreadsheet?** No. It reports defect candidates with suggested fixes; applying changes is a separate, explicit step.

**Is this an accounting or audit certification?** No. It flags likely defects and review items; it does not certify business, accounting, tax, or legal correctness.

**Does it work without Excel installed?** Yes. It reads workbooks with `openpyxl`. LibreOffice is optional and only used to refresh cached values for value-dependent checks.

**Does it support Google Sheets?** Not directly. Export to `.xlsx` and audit that.

## License

MIT

---

<sub>Topics: spreadsheet audit, excel auditor, xlsx, xlsm, financial model review, formula error checker, reconciliation, cross-foot, range check, circular reference detection, data quality, openpyxl, python, CLI, agent skill, static analysis.</sub>
