# Spreadsheet Auditor

`spreadsheet-auditor` is a portable Agent Skill and CLI toolkit for auditing existing spreadsheets for correctness defects. It checks formula errors, broken references, hardcoded values inside formulas, suspicious ranges, reconciliation mismatches, circular references, hidden structure, and selected data-hygiene risks.

The Skill is intentionally audit-first: it reports severity-ranked findings and optional annotations, but it does not rewrite the source workbook.

## Quick Start

Run the deterministic audit against an existing workbook:

```bash
python scripts/audit.py path/to/workbook.xlsx --out audit_report.md --json findings.json
```

Inspect runtime capabilities:

```bash
python scripts/audit.py --healthcheck
```

Build distributable Skill packages:

```bash
python scripts/build_dist.py
```

## Outputs

- Markdown report for human review.
- `findings.json` for reruns, CI, and downstream tooling.
- Optional annotated workbook when `--annotated` is provided.

## Dependencies

Required for `.xlsx` and `.xlsm` auditing:

- Python 3.11+
- `openpyxl`

Used when available:

- `defusedxml` for safer XML parsing through workbook dependencies.
- `networkx` for graph cycle detection.
- LibreOffice / `soffice` for recalculation.
- `PyYAML` for YAML config files.

## License

MIT
