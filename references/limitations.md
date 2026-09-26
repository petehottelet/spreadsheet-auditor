# Limitations

`spreadsheet-auditor` is a static-first audit tool. It does not guarantee
Excel calculation parity, does not certify business or accounting
correctness, and is not a substitute for review by a human modeler.

Contents: [Calculation parity](#calculation-parity) ·
[Value-dependent checks](#value-dependent-checks) ·
[Workbook size and performance](#workbook-size-and-performance) ·
[Annotated copies](#annotated-copies) ·
[Always disclose when](#always-disclose-when) ·
[Security behavior](#security-behavior) ·
[Heuristic vs deterministic](#heuristic-vs-deterministic) ·
[Exit codes](#exit-codes) ·
[What this tool is not](#what-this-tool-is-not)

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

`CROSS_FOOT_FAILURE` and the cached-value form of `TOTAL_MISMATCH` need cached
or recalculated values. The double-count form of `TOTAL_MISMATCH` and
`LIVE_ERROR` for a formula that carries an error literal are inferred
statically and never wait for recalculation.

- **Excel users**: open the workbook, press `F9`, save. The auditor reads the
  fresh cached values and runs all value-dependent checks.
- **CI / headless users**: install LibreOffice. The audit converts the
  workbook headless inside a throwaway profile that is seeded to force a full
  recalculation on load (`OOXMLRecalcMode = 0`; LibreOffice's own default for
  Excel files is "never recalculate", which would silently keep stale cached
  values) and to never run macros (`MacroSecurityLevel = 3`). Only cached
  values are taken from the converted copy; formula text always comes from
  the original file, so LibreOffice's re-serialized formulas never reach the
  static checks.
- Without either, the report records:
  > Limitation: Recalculation did not run; value-dependent checks
  > (`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) rely on cached values and may be
  > incomplete.

## Workbook size and performance

- The audit is bounded by the `limits` block in your config:
  `max_cells`, `max_formulas`, `max_reported_findings`, `timeout_seconds`.
  Exceeded limits surface in `coverage.truncated`.
- `timeout_seconds` defaults to 120 and is polled inside every check. When it
  expires, the check in progress stops, the remaining checks are skipped, and
  the report carries a limitation note naming the check. Set it to 0 to
  disable the budget.
- Checks only visit cells the workbook actually contains, and references are
  resolved without materializing cells, so a formula that points far away
  from the data does not grow the scan.
- When `max_cells` is exceeded, the checks that walk the cell grid
  (`HARDCODE_IN_FORMULA_BLOCK`, `CROSS_FOOT_FAILURE`, the data-hygiene rules)
  are skipped and the limitation note says so; formula-based checks still run.
- `max_range_expansion_cells` is accepted for backward compatibility but no
  longer does anything: `CIRCULAR_REFERENCE` resolves ranges, including
  whole-column references, against an index of formula cells and never drops
  a reference for being large. Setting it produces a deprecation note in the
  report.

## Annotated copies

`--annotated` writes a separate copy through openpyxl, which does not
preserve drawings, charts, images, form controls, or embedded objects. The
audit counts those parts during preflight and, when any exist, records a
limitation and prints a warning so the copy is never mistaken for a
replacement of the original workbook.

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
  a coverage limitation so a dropped suppression is never silent. Suppression
  targets are matched by location (a cell, range, whole column/row, or sheet
  name), never by text prefix.

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

- `DET` rules fire on a fixed structural pattern and `HEUR` rules on a
  judgment call. Neither tag says how often a finding is right: on real
  workbooks `FORMULA_DRIFT` and `HARDCODE_IN_FORMULA_BLOCK` are right about
  three times in five. The trust table in
  [`check_catalog.md`](check_catalog.md) says how far to check each rule
  before acting on it.
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
