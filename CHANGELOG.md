# Changelog

All notable changes to **Spreadsheet Auditor** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- **Precision pass on the deterministic checks.** A correct ten-row budget
  with a label column, a header row, subtotals, and a total column produced 23
  findings (11 Critical); it now produces none. Rule by rule:
  - `RANGE_EXCLUSION` only reports a plain number that sits between a total
    and the range it sums. Text labels, headers, dates, and formula rows never
    count as excluded data, and a total that lives elsewhere (another sheet or
    column, quarterly sub-sums) produces no exclusion finding.
  - `RANGE_INCLUDES_SUBTOTAL` fires only when the subtotal's own formula
    aggregates cells that are also inside the range (a real double count).
    "Subtotal + Other" totals stay quiet; a labeled row holding a constant is
    reported at Medium/Review. Subtotal columns are checked the same way.
  - `HARDCODE_IN_FORMULA_BLOCK` requires the constant to interrupt formulas
    that share one relative pattern on both sides, within a short gap, and
    exempts inputs that an adjacent subtotal sums. Every input beneath a
    subtotal used to be a "plug".
  - `FORMULA_DRIFT` exempts a row or column total that aggregates its own
    neighbors and no longer lets it dilute the majority pattern, so the total
    column of a budget is not drift while a genuine outlier beside it still is.
  - `TOTAL_MISMATCH` no longer reports `AVERAGE`, `COUNT`, or `SUM(...)/1000`
    as Confirmed defects. It now has two precise forms: a static double count
    (`=SUM(B2:B5)+B5`, `=SUM(B2:B5,B3)`) at High/Likely defect, and a bare
    `=SUM(range)` whose cached value disagrees with its components at
    Critical/Defect.
  - `HIDDEN_STRUCTURE_IN_TOTAL` reports once per hidden row, column, or sheet,
    listing the visible formulas it feeds; hidden sheets are now covered, as
    the README always claimed.
  - `LIVE_ERROR` reports once at the root cell and lists the cells the error
    propagates to instead of one Critical per dependent.
  - `NUMBERS_STORED_AS_TEXT` reports text numbers a formula reads (High) or
    that sit in a mostly numeric column (Medium); text numbers nothing
    consumes are not reported. `WHITESPACE_KEY` is limited to first-column
    labels and referenced cells, `DUPLICATE_KEY` to ranges that lookup
    functions search, and `MERGED_CELL_IN_DATA_RANGE` to merges inside
    formula-referenced ranges or tables. Title banners are no longer findings.
  - `BLANK_PRECEDENT` ignores references into entirely empty rows or columns.
- **Seed catalogs corrected.** Three benchmark "misses" were catalog errors
  (`Budget!F6` never existed, `Budget!B13` is not an aggregate, `Model!B16` had
  no adjacent excluded cell) and one seed (`Model!E5`) was itself a false
  positive. The demo workbook was rebuilt so that it is correct everywhere
  except its seeded defects, and both catalogs now list every finding the
  auditor reports against them. A new test fails CI when a seeded workbook
  produces any uncatalogued static finding or misses a seeded one.
- **Formula parsing no longer invents cell references.** The regex parser read
  function names such as `LOG10`, `DAYS360`, or `ATAN2` and the tails of names
  such as `EBITDA2025` as cell addresses, then materialized those cells while
  checking for blank precedents. A 12-row workbook could balloon to millions of
  scanned cells, run for minutes at several gigabytes, and emit bogus
  `BLANK_PRECEDENT` findings. Parsing now uses openpyxl's formula tokenizer
  (`spreadsheet_auditor/formula_parser.py`) and cell lookups never create cells
  (`reference_resolver.py`).
- **Circular references.** A total that includes its own cell (`=SUM(A1:A3)`
  in `A3`) was dropped when `networkx` was installed and reported only by the
  fallback DFS, so results depended on the environment. Cycles are now reported
  once per strongly connected component with an iterative algorithm: a
  filled-down self-inclusive total yields one finding instead of millions of
  elementary cycles, and dependency chains thousands of cells long no longer hit
  the recursion limit. Whole-column references (`SUM(A:A)`) take part in cycle
  detection.
- **Suppressions match by location, not by substring.** `Imports!A1` no longer
  hides `Imports!A10`, and the documented range form (`Imports!A1:A100`) now
  works. Whole columns/rows and bare sheet names are accepted; sheet names are
  case-insensitive. `scope.headline_outputs` uses the same matching.
- **Structured table references** (`Table1[Sales]`, `[@Sales]`) were reported
  as external workbook links and produced phantom blank-precedent findings.
  They now resolve against the workbook's tables; unresolvable ones surface as
  the `structured_references` coverage flag.
- **Defined names** resolve to their ranges instead of being ignored or
  misread; names defined as constants or formulas are recorded under the
  `unresolved_defined_names` coverage flag.
- **Array formulas** (legacy CSE and dynamic arrays) were invisible to every
  check with no coverage note. They are now parsed for references and counted,
  with an `array_formulas` coverage flag and a limitation note.
- `LITERAL_CONSTANT` no longer flags digits left behind after stripping a
  reference that shares a prefix with another (`=C3*C35` flagged `5`).
- Non-ASCII cell labels no longer crash report output on Windows when stdout is
  redirected; output streams are reconfigured to UTF-8 with replacement.
- Sheet names in references resolve case-insensitively, as in Excel.

### Changed

- **Default time budget.** `limits.timeout_seconds` now defaults to 120 and is
  polled inside every check, so a pathological workbook degrades to a partial
  report with a limitation note naming the interrupted check instead of running
  for hours. Set it to 0 to disable.
- Checks iterate the cells a sheet actually holds instead of the full bounding
  box, so sparse sheets no longer materialize millions of empty cells.
- `CheckContext` gained `names` (resolved defined names and tables) and
  `budget` (cooperative deadline); custom checks should call `budget.tick()`
  in long loops. See `references/custom_checks.md`.
- `FORMULA_DRIFT` normalization honours absolute markers (`$B$1` stays
  anchored), so rows that share an absolute anchor normalize to one pattern.
- New coverage flags: `array_formulas`, `structured_references`,
  `unresolved_defined_names`, `3d_references`, `unparseable_formulas`.
- `limits.max_range_expansion_cells` is accepted but ignored: ranges are
  resolved against an index of formula cells and are never dropped for size.

### Removed

- `networkx` is no longer used or listed as an optional dependency; the
  `graph` extra is gone and `[all]` installs `defusedxml` and `PyYAML` only.

## [0.1.0] - 2026-06-16

First public release. Establishes the audit-only contract, the deterministic
check catalog, the dual Agent Skill / standalone CLI distribution, and the
benchmark- and demo-backed evidence story.

### Added

- **Package layout** - importable `spreadsheet_auditor/` package; backward-compatible
  `scripts/audit.py` shim; `python -m spreadsheet_auditor` entry point.
- **Installable CLI** - `pyproject.toml` with `console_scripts` entry point
  `spreadsheet-auditor`. Extras: `[xml]`, `[graph]`, `[yaml]`, `[all]`, `[dev]`.
- **Detection rules** (deterministic unless noted):
  - Formula integrity: `LIVE_ERROR`, `BROKEN_REFERENCE`, `BLANK_PRECEDENT`,
    `CIRCULAR_REFERENCE`, `FORMULA_DRIFT`, `IFERROR_MASK` (HEUR).
  - Hardcodes: `LITERAL_CONSTANT`, `HARDCODE_IN_FORMULA_BLOCK`.
  - Ranges: `RANGE_EXCLUSION`, `RANGE_INCLUDES_SUBTOTAL`,
    `RANGE_LENGTH_MISMATCH`, `HIDDEN_STRUCTURE_IN_TOTAL`.
  - Reconciliation: `TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE` (value-dependent).
  - Structure: `VOLATILE_FUNCTION`, `WHOLE_COLUMN_REFERENCE`.
  - Data hygiene: `NUMBERS_STORED_AS_TEXT`, `WHITESPACE_KEY`, `DUPLICATE_KEY`,
    `MERGED_CELL_IN_DATA_RANGE`.
- **Outputs** - Markdown report, JSON findings (validated against
  `schemas/findings.schema.json`), HTML report, optional annotated workbook,
  SARIF for GitHub code scanning.
- **Report enrichments** - run metadata (`tool_version`, `timestamp`, `runtime`,
  `coverage`), severity-grouped report, stable finding fingerprints, drift
  evidence with neighboring formulas.
- **Suppression** - file-based and config-based suppression with required
  reasons; suppressed findings hidden by default, surfaced with
  `--show-suppressed`.
- **Config wiring** - `materiality`, `scope.headline_outputs`, and
  `limits.max_range_expansion_cells` now drive severity escalation; alias-aware
  check toggles in `[checks]`.
- **CLI ergonomics** - `--format markdown|json|html|sarif`, `--summary`,
  `--quiet`, `--show-suppressed`, `--demo`, `--strict`, improved `--healthcheck`
  with optional `--json` output.
- **Performance guardrails** - `limits.max_cells`, `limits.max_formulas`,
  `limits.timeout_seconds`, `limits.max_reported_findings` with explicit
  truncation reporting.
- **Plugin architecture** - `spreadsheet_auditor/checks/` registry; new checks
  can be added without editing the orchestrator.
- **Demo + benchmark** - `examples/demo_bad_budget.xlsx` with generated md/json/
  html/annotated outputs; `benchmarks/run_benchmark.py` producing
  `benchmarks/seeded_defects_matrix.md`.
- **CI** - `.github/workflows/ci.yml` runs metadata gate, healthcheck, tests,
  demo+benchmark regeneration, builds Claude/Codex skill packages, validates
  them, and uploads artifacts. `release.yml` produces tagged releases.
- **Docs** - rewritten `README.md`, `CONTRIBUTING.md`, `SECURITY.md`,
  `references/limitations.md`, `references/benchmark_methodology.md`.

### Packaging, distribution, and CI

- **PyPI publishing** - tagged releases publish the wheel and sdist to PyPI via
  trusted publishing (`release.yml` `pypi-publish` job).
- **Single-sourced version** - `pyproject.toml` reads the version dynamically
  from `spreadsheet_auditor.__version__`; the release workflow asserts the tag
  matches it.
- **Bundled demo workbook** - the demo ships inside the wheel and skill packages
  (`spreadsheet_auditor/demo/`), so `--demo` works from an installed package or
  an unpacked skill, not only from a repo checkout.
- **Bundled SARIF schema** - `schemas/sarif-2.1.0.schema.json`; SARIF output is
  validated against it (with date-time format checking) in the test suite.
- **Strict SARIF output** - `--format sarif` never silently falls back to
  generic JSON; on a rendering failure the CLI exits with code 5.
- **Suppression warnings** - malformed suppressions (missing reason or
  unparseable line) are surfaced as a coverage limitation instead of being
  dropped silently.
- **Hardened CI/release** - Python 3.11/3.12 test matrix, generator smoke
  tests, and validation of the installed wheel and unpacked Claude/Codex skills
  from a neutral working directory before publishing.

### Safety

- Source workbooks are never overwritten; annotation always writes to a
  separate file.
- Macros are inventoried but never executed; external workbook links are
  inventoried but never followed.
- LibreOffice recalculation runs headless in an isolated user profile.
- `defusedxml` is used when available; absence is recorded as a coverage
  limitation rather than a silent risk.

### Known Limitations

- Excel-specific behavior is approximated via LibreOffice; results may differ
  for dynamic arrays, data tables, Power Query/Data Model, and macros.
- Value-dependent checks (`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) require either
  recalculation (LibreOffice) or cached values written by Excel. Without these,
  the audit reports a coverage limitation rather than crashing.
- Findings are defect candidates and likely errors, not a legal, accounting,
  tax, or valuation certification.

[Unreleased]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/petehottelet/spreadsheet-auditor/releases/tag/v0.1.0
