# Changelog

All notable changes to **Spreadsheet Auditor** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **Real-world corpus harness** (`benchmarks/corpus/`): a registry of public
  spreadsheet corpora, a parallel runner that audits every workbook and
  records crashes and timeouts, a seeded stratified sampler that renders each
  finding as a context card, a labels file, and a report generator that
  publishes per-rule precision with Wilson 95% intervals to
  `benchmarks/real_world_precision.md`. `recall.py` measures recall on the
  modified EUSES corpus, whose workbooks each carry one injected formula fault
  at a known cell, attributing a hit only when the finding is absent from the
  unmodified original. A manual `corpus.yml` workflow runs either corpus in CI
  with LibreOffice installed.
- **Real-world precision report** (`benchmarks/real_world_precision.md`): the
  auditor run over all 2,729 SpreadsheetBench input workbooks, with 394
  findings sampled across the 18 rules that fired, labeled with a reason
  each. Against 0.2.0 as released the overall precision was 36% (Wilson 95%
  interval 32% to 41%), with `LIVE_ERROR` and `BROKEN_REFERENCE` at 100% and
  `BLANK_PRECEDENT`, `CIRCULAR_REFERENCE`, `FORMULA_DRIFT`, `WHITESPACE_KEY`
  and `MERGED_CELL_IN_DATA_RANGE` at 8% or below. After the changes below the
  same corpus yields 11,126 findings (from 48,281) at 76% precision (71% to
  81%), judged on a fresh sample of 337 findings with the same protocol; the
  report carries a per-rule before/after table.

### Changed

Every rule below was re-scoped from what the labeled sample showed its
false positives had in common; the seeded benchmark is unchanged.

- **Parser context**: each reference now records the function and argument
  it sits in, whether an operator touches it, and whether the formula tests
  it for blank; positional references (`ROW`, `ROWS`, `COLUMN`, `COLUMNS`,
  `ISREF`, `AREAS`) are no longer dependencies.
- **CIRCULAR_REFERENCE**: `ROWS(A$6:A8)` counters and `COLUMNS($D7:AA7)`
  are not cycles (23 of 25 sampled findings). A deliberate
  `IFERROR(1/(1/F8),"")` self-reference is still reported.
- **BLANK_PRECEDENT**: fires only when a blank is used in arithmetic, as a
  lookup key, or in a date or rounding function, the formula never tests it
  for blank, and the blank is a gap in an otherwise filled column; guarded
  formulas, template rows, mirror links, sparse ledger columns and
  blank-tolerant aggregates are quiet (24 of 25 sampled findings were these).
- **FORMULA_DRIFT**: a cell that agrees with its formula neighbours on the
  other axis is a different column by design, and the seed of a chain (an
  opening balance, year 0) is expected to differ; a `#REF!` majority is not a
  pattern.
- **HARDCODE_IN_FORMULA_BLOCK**: an input column or row between two lines
  of formulas sharing a pattern (running sums, unit x quantity) is not a
  plug; a text label between the two formulas ends the block.
- **BROKEN_REFERENCE**: external workbook links are one Low/Info finding per
  source per sheet instead of a High finding per cell.
- **DUPLICATE_KEY**: only the searched column of a first-match lookup is a
  key column (`VLOOKUP` first column, `HLOOKUP` first row, the lookup array
  of `MATCH`/`XMATCH`/`XLOOKUP`/`LOOKUP`); `SUMIF`/`COUNTIF` criteria ranges
  and `VLOOKUP` return columns are not.
- **NUMBERS_STORED_AS_TEXT**: the High variant requires a formula that
  consumes the cell as a number; leading-zero identifiers are never
  reported. The numeric-column variant was right 10 times out of 10 and is
  unchanged.
- **WHITESPACE_KEY**: headers over data, leading-space indentation and
  whitespace-only cells are skipped; a column padded by an export gets one
  Low/Info note instead of a finding per cell.
- **MERGED_CELL_IN_DATA_RANGE**: only a merged number or formula read
  through a range reference counts; merged titles, headers, labels and cells
  that formulas address directly are presentation (0 of 25 sampled findings
  were data).
- **WHOLE_COLUMN_REFERENCE**: reported only where the column is evaluated as
  an array (a comparison, arithmetic, `IF`, `SUMPRODUCT`, `LOOKUP(2,1/...)`,
  array formulas); `COUNTIF`, `VLOOKUP`, `MATCH` and `INDEX` over `A:A` are
  bounded by Excel and are quiet.
- **VOLATILE_FUNCTION**: `TODAY`/`NOW` become one Low/Info note per sheet;
  `RAND`, `RANDBETWEEN`, `OFFSET`, `INDIRECT` stay Medium.
- **LITERAL_CONSTANT**: literals in structural argument slots (column
  indexes, match types, string positions, date parts, rounding digits) and
  the unit constants 60 and 3600 are skipped.
- **HIDDEN_STRUCTURE_IN_TOTAL**: `AGGREGATE` options 1/3/5/7 and `SUBTOTAL`
  101-111 skip hidden rows by definition; hidden rows feeding the same
  formulas are reported together.
- **RANGE_EXCLUSION**: expanding running-total ranges (`$A$9:A9`) are not
  totals. **RANGE_INCLUDES_SUBTOTAL**: a labeled column of constants (a total
  carried forward) is no longer reported. **RANGE_LENGTH_MISMATCH**: one-cell
  aggregates are links, and sums over disjoint column groups are not peers.
- **Grouping**: `IFERROR_MASK`, `LITERAL_CONSTANT`, `VOLATILE_FUNCTION` and
  `WHOLE_COLUMN_REFERENCE` report once per formula pattern per sheet, at the
  first cell, with the other cells listed as evidence, instead of once per
  cell.
- **Second pass**, from labeling the re-audited corpus: `CELL("filename",A1)`
  in A1 is not a cycle; a compared column inside `SUMPRODUCT` is not numeric
  consumption; an input column keeps its status when the neighbouring
  formula line holds a plug or a SUM row; a label column that links every
  second row of another sheet, and a totals row mixing `SUM` and `AVERAGE`,
  are not drift; merged formulas (title formulas, net lines) are
  presentation; a header under a lone title row and two-space indentation
  are not padded keys while a single stray leading space still is; an array
  formula that only hands a whole column to `INDEX` is quiet; `COUNTIF`-style
  criteria literals are not assumptions; `BLANK_PRECEDENT` skips rows whose
  inputs are all blank and needs three of four surrounding cells filled.
- **Google Sheets placeholders**: formulas of the form
  `IFERROR(__xludf.DUMMYFUNCTION("..."), cached value)` set the coverage flag
  `google_sheets_placeholders` and a limitation note, since those cells are
  frozen values.
- **Performance**: `parse_formula` results are cached per name table, so the
  checks parse each formula once instead of once per check (the slowest
  corpus workbook spent 88 of 113 seconds parsing).

## [0.2.0] - 2026-09-13

The precision release. The formula parser, cycle detection, suppressions, and
runtime guards were rebuilt; every deterministic check was re-scoped to fire
only on evidence a reviewer would accept; the seed catalogs and the demo
workbook were corrected; and LibreOffice recalculation is now forced and kept
away from the static checks. A correct ten-row budget went from 23 findings
to none, the demo from 63 findings to 13 (all seeded), and the benchmark from
3 misses and 76 uncatalogued findings to 0 and 0. Dropping the unused
`networkx` dependency removes the `graph` extra, hence the minor bump.

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
- **Recalculation is real, and it cannot corrupt the static checks.**
  LibreOffice defaults to "never recalculate" for Excel files, so a headless
  conversion kept whatever Excel had cached. The isolated profile is now
  seeded with `OOXMLRecalcMode = 0` (force recalculation) and
  `MacroSecurityLevel = 3` (macros never run). Static checks read formula text
  from the original workbook; the converted copy only supplies cached values,
  so LibreOffice's re-serialized `=SUM(#ref!)` no longer reaches the parser.
  Lower-case error literals parse in any case.
- **`LIVE_ERROR` no longer waits for recalculation** when a formula carries
  an error literal outside any error-handling function: `=SUM(#REF!)`
  evaluates to an error whatever its inputs, so it is reported statically.
- **`limits.max_cells` now does what it says.** Exceeding it skips the checks
  that walk the cell grid and the limitation note names them; before, the
  note claimed a cap that never happened. Setting the deprecated
  `limits.max_range_expansion_cells` produces a note instead of silence.
- **Annotated copies warn about what they drop.** Preflight counts drawings,
  charts, images, and controls; when `--annotated` would lose any, the report
  carries a limitation and the CLI prints a warning.
- Generated reports, JSON, SARIF, the benchmark matrix, and the corpus
  expectations are written with LF newlines on every platform, and the demo
  outputs use repository-relative paths instead of a maintainer's directory.
- CI lints for unused imports and undefined names, and uploads the
  LibreOffice-backed demo and benchmark outputs as a `regenerated-artifacts`
  bundle so the committed copies can always come from a run with
  recalculation available.
- The release workflow's PyPI publish job now grants `actions: read` and
  `contents: read`; its job-level `permissions` block had reset them to none,
  so `actions/download-artifact` failed with 403 before anything was uploaded.
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

[Unreleased]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/petehottelet/spreadsheet-auditor/releases/tag/v0.1.0
