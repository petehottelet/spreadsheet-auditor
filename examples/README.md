# Demo

This folder contains a small, intentionally flawed workbook plus the audit
outputs the tool produces against it. Use it to:

1. **Show, not tell.** Open
   [demo_audit_report.md](demo_audit_report.md) (or
   [demo_audit_report.html](demo_audit_report.html)) to see the kind of finding
   the auditor catches, without running anything yourself.
2. **Try it locally** in under a minute (see below).
3. **Verify a fresh checkout** by regenerating the demo and diffing the result.

## Try the demo

```bash
pip install -e .[all]

# Regenerate the workbook + all outputs in one go
python examples/make_demo.py
```

Or run the audit yourself against the bundled workbook:

```bash
spreadsheet-auditor examples/demo_bad_budget.xlsx \
    --out examples/demo_audit_report.md \
    --json examples/demo_findings.json \
    --annotated examples/demo_annotated.xlsx
```

## What's in `demo_bad_budget.xlsx`

The workbook is a tiny budget with intentionally seeded defects covering every
acceptance class from the PRD:

| Defect                                  | Where in the workbook                          | Rule it triggers              |
| --------------------------------------- | ---------------------------------------------- | ----------------------------- |
| Broken / deleted reference              | `Budget!B14` (`=SUM(#REF!)`)                   | `BROKEN_REFERENCE`, `LIVE_ERROR` |
| Off-by-one `SUM` range                  | `Budget!B11` (stops at row 8 instead of row 9) | `RANGE_EXCLUSION`             |
| Formula drift                           | `Budget!F6` breaks the `F2:F10` pattern        | `FORMULA_DRIFT`               |
| Hardcoded value in a formula block      | `Budget!E9` (literal `999`)                    | `HARDCODE_IN_FORMULA_BLOCK`   |
| Total mismatch / reconciliation failure | `Budget!B6` (extra `+B5`)                      | `TOTAL_MISMATCH`              |
| Number stored as text                   | `Budget!B20` (`"1,250"`)                       | `NUMBERS_STORED_AS_TEXT`      |
| Duplicate key with whitespace           | `Budget!A17`/`A18` (`North` / ` North `)       | `DUPLICATE_KEY`, `WHITESPACE_KEY` |
| Hidden row in a total                   | `Budget!12` hidden, summed by `Budget!B13`     | `HIDDEN_STRUCTURE_IN_TOTAL`   |

The exact rule mix can shift between releases as the catalog grows; the
benchmark matrix in [`benchmarks/seeded_defects_matrix.md`](../benchmarks/seeded_defects_matrix.md)
is the authoritative source of detection coverage.

## Generated artifacts

`make_demo.py` produces:

- `demo_audit_report.md` - Markdown report.
- `demo_audit_report.html` - HTML report for browser review.
- `demo_findings.json` - machine-readable findings (validates against
  [`schemas/findings.schema.json`](../schemas/findings.schema.json)).
- `demo_annotated.xlsx` - a *copy* of the workbook with comments at finding
  cells. The original `demo_bad_budget.xlsx` is never modified.

## Screenshots

Visual proof lives in [`screenshots/`](screenshots/). See
[`screenshots/README.md`](screenshots/README.md) for the shot list and how to
recapture them.
