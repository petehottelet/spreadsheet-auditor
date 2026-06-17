# Limitations

`spreadsheet-auditor` is a static-first audit tool. It does not guarantee
Excel calculation parity, does not certify business or accounting
correctness, and is not a substitute for review by a human modeler.

## Calculation parity

The auditor reads workbooks with [`openpyxl`](https://openpyxl.readthedocs.io/)
and (when available) recalculates them with headless LibreOffice. LibreOffice
Calc implements the vast majority of Excel functions, but differences remain:

- **Dynamic arrays** (`FILTER`, `SORT`, `UNIQUE`, `SEQUENCE`, `XLOOKUP`'s
  array-aware forms): support is partial; spill behavior may differ. Findings
  about cells inside spilled ranges may be off.
- **Data tables** (`Data -> What-If Analysis -> Data Table`): the auditor
  reads the cached values but does not resolve the input/result mapping.
- **Power Query / Data Model**: not refreshed. Connections and queries are
  visible as cell formulas but their actual outputs reflect whatever was
  cached the last time the workbook was opened in Excel.
- **Pivot tables**: read as cached values. No formula-level checks apply
  inside the pivot region itself.
- **Add-ins, UDFs, and VBA-based functions**: not executed. Cells calling
  them surface as `#NAME?` errors if Excel did not cache a value.
- **Structured table references** (e.g. `Table1[Column]`): parsed as
  references where unambiguous; complex structured references are reported
  as `unsupported_features.structured_or_dynamic_references` in coverage.
- **`@` implicit intersection operator**: marked as an unsupported feature in
  coverage.

## Value-dependent checks

`TOTAL_MISMATCH` and `CROSS_FOOT_FAILURE` need cached or recalculated values:

- **Excel users**: open the workbook, press `F9`, save. The auditor reads the
  fresh cached values and runs all value-dependent checks.
- **CI / headless users**: install LibreOffice. The audit invokes
  `soffice --headless --calc --convert-to xlsx` to refresh values inside an
  isolated profile.
- Without either, the report records:
  > Limitation: Recalculation did not run; value-dependent checks
  > (`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) rely on cached values and may be
  > incomplete.

## Workbook size and performance

- The audit is bounded by the `limits` block in your config:
  `max_cells`, `max_formulas`, `max_reported_findings`, `timeout_seconds`.
  Exceeded limits surface in `coverage.truncated`.
- Very large dependency graphs may exceed `max_range_expansion_cells` for
  `CIRCULAR_REFERENCE`; expand the limit or accept the truncation note.

## Always disclose when

- LibreOffice recalculation is unavailable or fails.
- Cached values are stale or missing.
- External workbooks are referenced but not available.
- Formulas use unsupported syntax, dynamic arrays, data tables, structured
  references, Power Query, Data Model, add-ins, UDFs, or macros.
- Runtime limits cause expensive graph or range checks to be skipped.
- The workbook is password-protected or corrupt.
- Suppressions hide findings; the report's summary always shows the
  suppressed count. Every suppression requires a reason; malformed
  suppressions (missing reason, unparseable line) are ignored and reported as
  a coverage limitation so a dropped suppression is never silent.

Never execute macros. Never follow external links without explicit user
approval and sandbox controls.

## Security behavior

- Macros/VBA are inventoried and never executed. LibreOffice recalculation
  runs headless in an isolated profile.
- External workbook links are inventoried and reported, never followed by
  default.
- XML parsing uses `defusedxml` when available. When it is missing the audit
  continues but records a coverage limitation noting that XML parsing relied
  on library defaults.
- Preflight checks archive structure and uncompressed size to reduce
  zip-bomb risk, and never overwrites the source workbook.

See [`SECURITY.md`](../SECURITY.md) for the full threat model.

## Heuristic vs deterministic

- `DET` rules are deterministic: they fire on a structural pattern that is
  almost always wrong. False positives are bugs and we will fix them.
- `HEUR` rules require judgement. They default to `Review` confidence and
  should be inspected before action; their false-positive rate is openly
  documented in the seeded benchmark
  ([`benchmarks/seeded_defects_matrix.md`](../benchmarks/seeded_defects_matrix.md)).
- The opt-in `finance.*` checks (`BALANCE_SHEET_BALANCE`,
  `SIGN_CONVENTION`, `PERIOD_MISMATCH`) are label-driven heuristics; they are
  off unless you set `finance.enabled: true` in your config.

## Exit codes

| Code | Meaning |
|---:|---|
| 0 | Completed; no findings at or above the `--fail-on` threshold |
| 1 | Completed; findings at or above the `--fail-on` threshold |
| 2 | Completed with coverage limitations, only when `--strict` or `--fail-on None` is set |
| 3 | Healthcheck failed: required dependency missing |
| 4 | Preflight/security failure (unreadable, unsupported, oversized, or invalid input) |
| 5 | Internal audit error |

Benign limitations such as missing recalculation or optional packages do not
fail a normal run; use `--strict` to surface them as exit code `2` in CI.

## What this tool is **not**

- A spreadsheet builder. It never writes to your source workbook.
- An accounting or audit certification. It flags candidates, not conclusions.
- A semantic correctness checker. It does not know whether your business
  logic is the right business logic; only whether the formulas implementing
  it are structurally sound.
- A static analyzer for VBA code. Macros are inventoried but their bodies
  are not parsed.
