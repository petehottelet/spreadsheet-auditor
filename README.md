<p align="center">
  <img src="project_logo.png" alt="Spreadsheet Auditor logo" width="360">
</p>

<h1 align="center">Spreadsheet Auditor</h1>

<p align="center">
  <strong>Audit existing Excel spreadsheets and financial models for correctness defects &mdash; formula errors, broken references, bad ranges, totals that don't reconcile, and data-quality risks.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/spreadsheet-auditor/"><img src="https://img.shields.io/pypi/v/spreadsheet-auditor.svg" alt="PyPI version"></a>
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/python-3.11%2B-blue.svg" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Claude%20%2B%20Codex-Agent%20Skill-orange.svg" alt="Claude + Codex Agent Skill">
  <img src="https://img.shields.io/badge/formats-.xlsx%20%7C%20.xlsm%20%7C%20.csv-lightgrey.svg" alt="Supported formats">
  <img src="https://img.shields.io/badge/output-md%20%7C%20json%20%7C%20html%20%7C%20sarif-blueviolet.svg" alt="Output formats">
</p>

---

`spreadsheet-auditor` is a portable [Agent Skill](https://agentskills.io/specification) for **Claude and Codex** (and a standalone command-line toolkit) that answers one question: **"Can I trust this spreadsheet?"**

Most spreadsheet tooling helps you *build* workbooks. This one *audits* a workbook you already have &mdash; often one you inherited &mdash; and returns a severity-ranked report of where it is likely wrong, fragile, or inconsistent. It is deterministic-first: bundled Python checks produce candidate findings with exact cell locations and evidence, so you are not eyeballing cells and guessing.

It is intentionally **audit-only**: it reports defects and optional annotations, but never silently rewrites, reformats, or "fixes" your source workbook.

> [!TIP]
> See the auditor in action without installing anything: open
> [`examples/demo_audit_report.md`](examples/demo_audit_report.md) or
> [`examples/demo_audit_report.html`](examples/demo_audit_report.html).

## Demo (60 seconds)

```bash
pip install "spreadsheet-auditor[all]"
spreadsheet-auditor --demo --summary
```

Or against a workbook of your own:

```bash
spreadsheet-auditor path/to/workbook.xlsx \
    --out audit_report.md \
    --json findings.json \
    --annotated audit_annotated.xlsx
```

A complete demo lives in [`examples/`](examples/) with a generator
([`examples/make_demo.py`](examples/make_demo.py)), the seeded workbook, and
the resulting report/JSON/HTML/annotated outputs ready to inspect.

## Why use it

- **Pre-send model review** &mdash; de-risk an LBO/DCF/budget model before it
  reaches an investment committee or counterparty.
- **"Find the error" debugging** &mdash; a number looks wrong and you need the
  cell, not a guess.
- **Inherited-model trust assessment** &mdash; you didn't build it; check
  whether it is trustworthy.
- **CI / batch gating** &mdash; fail a pipeline when a committed workbook has
  Critical defects (see
  [`examples/github-actions/`](examples/github-actions/)).
- **FP&A and month-end close** &mdash; catch reconciliation and range mistakes
  in recurring workbooks.

## What it detects

| Category | Checks |
|---|---|
| Formula integrity | live errors (`#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, ...), broken/deleted references, references to blank precedents, circular references, formula drift across a row/column, `IFERROR`/`IFNA` error masking |
| Hardcodes & inputs | numeric literals embedded in formulas, hardcoded plug values inside a formula block |
| Ranges | aggregate ranges that exclude adjacent data (off-by-one), ranges that include subtotal/total rows, inconsistent aggregate range lengths across peers, hidden rows/columns/sheets inside totals |
| Reconciliation | stated totals that differ from their components, row totals vs column totals that don't cross-foot |
| Logic & structure | volatile/fragile functions (`OFFSET`, `INDIRECT`, `NOW`, `RAND`, ...), whole-column references |
| Data hygiene | numbers stored as text, leading/trailing whitespace in keys/labels, duplicate lookup keys, merged cells inside data ranges |
| Finance (opt-in HEUR) | balance-sheet balance, sign convention on revenue/expense rows, quarterly period sequencing |

Each finding carries a detection mode (`DET` deterministic / `HEUR` heuristic),
an error-confidence level (`Defect` / `Likely defect` / `Review` / `Info`), a
severity, evidence, and a suggested fix. Full rule list:
[`references/check_catalog.md`](references/check_catalog.md).

The seeded-defect benchmark is published at
[`benchmarks/seeded_defects_matrix.md`](benchmarks/seeded_defects_matrix.md);
methodology at
[`references/benchmark_methodology.md`](references/benchmark_methodology.md).

## Install

```bash
pip install spreadsheet-auditor             # core + .xlsx/.xlsm/.csv audit
pip install "spreadsheet-auditor[all]"      # adds defusedxml, networkx, PyYAML
```

For local development:

```bash
git clone https://github.com/petehottelet/spreadsheet-auditor.git
cd spreadsheet-auditor
pip install -e ".[dev]"
spreadsheet-auditor --healthcheck
python -m pytest tests -q
```

Releases (signed source archive + Claude/Codex skill zips + SHA-256
checksums) are published from the
[Releases page](https://github.com/petehottelet/spreadsheet-auditor/releases).

## Run

```bash
# Quick look in the terminal
spreadsheet-auditor model.xlsx

# Write artifacts in every supported format
spreadsheet-auditor model.xlsx \
    --out report.md \
    --json findings.json \
    --annotated annotated.xlsx
spreadsheet-auditor model.xlsx --format html --out report.html
spreadsheet-auditor model.xlsx --format sarif --out report.sarif

# CI-friendly: one-screen summary + non-zero exit on High-or-worse
spreadsheet-auditor model.xlsx --summary --fail-on High

# Bundled demo for a 60-second tour
spreadsheet-auditor --demo --summary
```

See `spreadsheet-auditor --help` for the full flag reference, including
`--strict`, `--show-suppressed`, `--quiet`, `--config`, `--ignore`,
`--recalc-timeout`, and `--healthcheck --json`.

## Outputs

- **Markdown report** for human review, grouped by `Confirmed`/`Likely`/`Review`
  buckets so the worst items are easy to triage.
- **HTML report** for browser review or sharing with non-technical reviewers
  (self-contained, no network).
- **JSON findings** for reruns, CI, and downstream tooling. Validates against
  [`schemas/findings.schema.json`](schemas/findings.schema.json). Each finding
  carries a stable `fingerprint` for diffing across runs and for fingerprint-
  based suppression.
- **SARIF 2.1.0** for GitHub code scanning. See
  [`examples/github-actions/code-scanning.yml`](examples/github-actions/code-scanning.yml).
- **Annotated workbook copy** with comments at finding cells (`--annotated`).
  The source workbook is never modified.

## Exit codes

| Code | Meaning |
|---:|---|
| 0 | Completed; no findings at or above `--fail-on` |
| 1 | Completed; findings at or above `--fail-on` |
| 2 | Completed with coverage limitations (only with `--strict` or `--fail-on None`) |
| 3 | Healthcheck failed: required dependency missing |
| 4 | Preflight/security failure |
| 5 | Internal error |

Benign limitations (no recalculation engine, missing optional packages) do not
fail a normal run. Use `--strict` to surface them as exit code `2` in CI.

## Agent Skill usage

Drop the Claude/Codex zip from the release into your Skills folder, or load it
directly with [Cursor](https://cursor.com/) Skills. Ask the agent something
like:

> "Audit `Q3_Forecast.xlsx` and tell me what's wrong with it. Write the report
> to `audit_report.md` and produce an annotated copy."

The skill maps the request onto the bundled CLI invocation and surfaces the
findings inline.

## Configuration

Optional config file (JSON or YAML) controls scope, materiality, suppression,
performance limits, and which checks fire. Schema:
[`schemas/config.schema.json`](schemas/config.schema.json).

Example:

```yaml
scope:
  include_sheets: [Budget, Summary]
  headline_outputs: [Summary!C1, Summary!C2]
materiality:
  absolute: 1000.0
  relative: 0.001
finance:
  enabled: true        # turn on the finance HEUR pack
limits:
  max_formulas: 50000
  timeout_seconds: 120
  max_reported_findings: 200
checks:
  IFERROR_MASK: review   # warn instead of error
  LITERAL_CONSTANT: off
suppressions:
  - rule_id: BROKEN_REFERENCE
    range: Imports!A1:A100
    reason: External feed populated at runtime; cells start empty.
```

## Safety

Spreadsheet files are treated as untrusted input. Macros are inventoried but
never executed, external links are inventoried but never followed,
recalculation runs headless in an isolated profile, and the original workbook
is never overwritten. Details in
[`SECURITY.md`](SECURITY.md) and
[`references/limitations.md`](references/limitations.md).

## Limitations

Excel-specific behavior is approximated via LibreOffice. Value-dependent checks
(`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) require either recalculation
(LibreOffice/Calc) or cached values written by Excel. Dynamic arrays, data
tables, Power Query/Data Model, and macros are *inventoried but not executed*.
Full list:
[`references/limitations.md`](references/limitations.md).

Google Sheets: export to `.xlsx` and audit that. There is no native Sheets API
integration. See
[`references/google_sheets.md`](references/google_sheets.md) for a recipe.

## FAQ

**Does it fix my spreadsheet?** No. It reports defect candidates with
suggested fixes; applying changes is a separate, explicit step.

**Is this an accounting or audit certification?** No. It flags likely defects
and review items; it does not certify business, accounting, tax, or legal
correctness.

**Does it work without Excel installed?** Yes. It reads workbooks with
`openpyxl`. LibreOffice is optional and only used to refresh cached values for
value-dependent checks.

**Does it support Google Sheets?** Not directly. Export to `.xlsx` and audit
that.

**How are false positives handled?** Suppress them by `(rule_id, range, reason)`
or by `fingerprint`. A reason is required; suppressions missing a reason are
ignored and called out in the report's coverage limitations. Suppressed findings
stay in the JSON payload (auditable) but are hidden from the report unless
`--show-suppressed` is passed.

## Contributing

We welcome new checks, additional test workbooks, and benchmark improvements.
See [`CONTRIBUTING.md`](CONTRIBUTING.md) and
[`references/custom_checks.md`](references/custom_checks.md).

## License

MIT. See [`LICENSE`](LICENSE).

---

<sub>Topics: spreadsheet audit, excel auditor, xlsx, xlsm, financial model
review, formula error checker, reconciliation, cross-foot, range check,
circular reference detection, data quality, openpyxl, python, CLI, agent
skill, static analysis, claude, codex, FP&A, financial modeling, fpna.</sub>
