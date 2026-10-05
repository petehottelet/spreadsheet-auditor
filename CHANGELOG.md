# Changelog

All notable changes to **Spreadsheet Auditor** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **`DUPLICATE_KEY` reports a repeat only where a first-match lookup can
  return the wrong row.** It pooled every searched cell of a column, so a
  product label heading bins in several HLOOKUP blocks of a bay map was a
  "duplicate" although each HLOOKUP searches its own row. Each searched range
  is now read on its own, along its search direction. Within a range, repeats
  are left out when the lookup looks for the next occurrence
  (`MATCH(G5,$G6:$G28,0)` filled down), when three or more identical keys sit
  together as detail rows under one ID, when the occurrences return the same
  values (several countries sharing USD at rate 1), when every key repeats,
  three times or more on average (attendance marks, region names), or when a
  date beside each occurrence tells them apart (a material's validity
  periods, a dated log). A lookup anchored at the top that grows down
  (`MATCH(B5,$B$4:$B4,0)`) still reports repeats, since it returns the
  earliest occurrence.

## [0.4.0] - 2026-10-03

An audit that stops short now fails instead of passing, a mistake repeated
down a column is reported once, an accepted finding stays accepted when rows
move, and input the auditor cannot use says what to fix. Exit codes,
fingerprints and one default change; read **Upgrading from 0.3.0** first.

Download the Claude or Codex skill ZIP from the release assets, or upgrade
the CLI with `python -m pip install --upgrade spreadsheet-auditor`.

### Upgrading from 0.3.0

- **Exit codes.** A new exit 6 means the audit did not finish: a check
  failed or ran out of time, or `limits.max_formulas` or `limits.max_cells`
  skipped part of the workbook. It takes precedence over 1 and applies
  whatever `--fail-on` says; a workbook with 1,830 live errors audited under
  a 15-second budget used to report nothing and exit 0. Usage errors exit 4
  instead of 2, and so does input the auditor cannot use, which mostly exited
  5: a config mistake, a workbook, CSV, config or suppression file that
  cannot be read, a missing `--ignore` file, an output path that cannot be
  written. Exit 5 now means a bug in the auditor and prints the traceback. A
  CI step that fails only on 1 should fail on 4, 5 and 6 too.
- **Config is checked.** An unknown section, setting or rule name, a value
  of the wrong type, or an unknown check level used to be ignored, so the
  audit ran on defaults; it now exits 4 and names the nearest known name
  (`did you mean 'LIVE_ERROR'?`). Rule names and levels match in any case,
  an empty section is the same as leaving it out, and 50000.0 counts as
  50000. `scope.include_sheets` naming no sheet of the workbook exits 4, and
  sheet names the workbook lacks are coverage limitations.
- **Fingerprints changed.** A fingerprint hashes the flagged cell's content
  and its row and column labels instead of its address, so it stays the same
  when rows or columns are inserted. Fingerprint suppressions written for
  0.3.0 match nothing once: the report names each stale line and prints the
  line to use. SARIF carries the new value as
  `partialFingerprints["spreadsheetAuditor/v2"]`, so code-scanning alerts are
  opened afresh once.
- **`BLANK_PRECEDENT` is off by default.** None of its 25 sampled findings on
  SpreadsheetBench was a mistake: what remained were blanks that mean zero by
  design, such as one side of a debit/credit pair. Turn it on with
  `"checks": {"BLANK_PRECEDENT": "error"}` for data that must never have
  gaps.
- **A suppression must cover every cell of a finding.** A finding that
  stands for several cells (see **Changed**) is hidden only by a target that
  covers all of them, and the report says when a line covers some.
- **Output.** With `--json -`, stdout holds only the JSON and the summary
  goes to stderr. `--format` without `--out` prints that format rather than
  Markdown. `--annotated` needs an `.xlsx` or `.xlsm` workbook and a copy
  path with its extension.

### Added

- **Pinned suppressions.** `LIVE_ERROR Model!C5 fingerprint:<fp> <reason>`
  (in a config: `rule_id`, `range` and `fingerprint` together) accepts one
  finding. It keeps suppressing that finding after rows or columns move,
  never hides a different finding that lands on the address, and the report
  says when the finding has moved. When findings of a rule are alike in
  content and labels, the line also needs its address, and adding or fixing
  one of them makes the line stale rather than letting it pass to another.
  The Markdown report prints the pinned line under every finding, and each
  run names the pinned replacement for an unpinned one-cell line.
- **`--pin-suppressions`** rewrites the `--ignore` file after the audit: each
  unpinned one-cell line that matched becomes its pinned form, each pinned
  line whose finding moved gets its new address, and the rest of the file
  (comments, area lines, stale lines, newline style) is kept byte for byte.
  Every change is printed on stderr with the formula it was pinned to.
- `coverage.complete`, `coverage.incomplete` (reason, message and the rules
  not checked) and `coverage.finding_counts` (counts before the report cap)
  in the JSON; `members` on each finding, every cell it stands for; for an
  incomplete audit, a banner in the Markdown and HTML reports and
  `audit : INCOMPLETE` in `--summary`; in SARIF, `executionSuccessful`, tool
  execution notifications, and `relatedLocations` for the other cells of a
  finding. The annotated copy comments every cell of a finding.
- Coverage notes for a suppression that matches nothing, covers only some
  cells of a finding, follows an address a different finding could take, or
  whose finding has moved.
- CSVs saved by Excel as "CSV (Comma delimited)" (Windows-1252, noted in the
  limitations), UTF-16 and UTF-32 CSVs with a byte-order mark, and CSV fields
  over 128 KiB.
- stderr says why the exit code is not 0, even with `--quiet`.

### Changed

- **A mistake repeated down a column is one finding.** A formula filled down
  a column that errors in every row was one Critical finding per row: a
  SpreadsheetBench workbook whose lookup reads its own column reported 278
  for one column, and the report cap then hid the workbook's other findings.
  `LIVE_ERROR` now groups errors by sheet, error value and relative formula
  (and the same error typed as a value), and lists the cells an error spreads
  to, including those fed by an error cycle; `BROKEN_REFERENCE` groups `#REF!`
  and unresolved formulas by relative formula; `CIRCULAR_REFERENCE` groups
  cells that each reference only themselves; `NUMBERS_STORED_AS_TEXT` is one
  finding per column and kind; `DUPLICATE_KEY` is one finding per searched
  column; `HIDDEN_STRUCTURE_IN_TOTAL` is one finding per sheet for its hidden
  rows and one for its hidden columns, named as runs. Each finding sits at
  its top-left cell and lists the others.
- **The report cap keeps every rule.** `limits.max_reported_findings` kept
  the first findings in severity order, so one rule could take every place.
  Each rule now keeps its most severe finding, the remaining places go by
  severity, and the limitation note says how many findings of each rule were
  left out. `--summary` and the reports count before the cap ("5 Critical ...
  (3 of 6 shown)").
- **`IFERROR_MASK` reports only a failure passed off as data.** It flagged
  every `IFERROR` and `IFNA`, and on SpreadsheetBench about seven in ten were
  deliberate. It now reports a wrapper whose expression can really fail (a
  division, a lookup, an average, a text or date conversion, arithmetic on a
  cell) when the error comes back as something that reads as a real value: a
  number, a number written as text, a cell, or a calculation. `IFNA` counts
  only what returns `#N/A`; an error already absorbed by `ISNUMBER` or an
  inner `IFERROR`, a conversion that falls back to the text it read
  (`IFERROR(VALUE(A1),A1)`), a second lookup, a message, and `NA()` are not
  reported. Google Sheets placeholder formulas still are, with a fix of
  their own.
- `FORMULA_DRIFT` leaves summary cells alone when they are not part of the
  run beside them: a cell where the run's formula would add up only text
  labels (a link under "Total Tax" heading a column of names), and one of a
  row of summaries over the same block with their own criteria (counts of 1,
  2 and 3 over one range). A total aimed at the wrong column, and a broken
  member of a run that reads a shared table, are still reported.
- Numbers stored as text that every formula reading them converts first
  (`--A1`, `VALUE(A1)`, `A1*1`) are a Low, Info finding; a `SUM` or another
  unconverted reader keeps it High.
- `LITERAL_CONSTANT` reports a literal inside the value a rounding or
  formatting function works on: `=ROUND(A1*1.0725,2)` reports 1.0725, not the
  2. A 3 or 6 dividing `MONTH()` (quarters, halves) is not reported.
- CSV whitespace is one finding per column, a column padded throughout is a
  Low, Info export note (as for workbooks), whitespace-only cells are
  skipped, and the report cap applies to CSV audits too.
- `LIVE_ERROR` traces each group of sources once. For 8,000 failing lookups
  feeding a running total, its memory grew with the square of the rows (1.4 GB
  measured) and the audit time budget could not stop it; it now uses tens of
  megabytes, takes seconds, and polls the budget.
- Checks run formula integrity (live errors and broken references first) and
  the reconciliations before the grid scans, so a time budget that runs out
  drops the slower checks first.
- On SpreadsheetBench the auditor reports 3,434 findings instead of 11,123,
  no workbook reports more than before, and none reaches the report cap (22
  did). `LIVE_ERROR` reports 382 findings instead of 5,057, `IFERROR_MASK` 644
  instead of 1,763, `NUMBERS_STORED_AS_TEXT` 58 instead of 847,
  `WHITESPACE_KEY` 176 instead of 490 and `DUPLICATE_KEY` 69 instead of 647; rules the old cap crowded out now show
  (`LITERAL_CONSTANT` 1,342 from 1,015, `FORMULA_DRIFT` 172 from 124).
  Sampled precision is 80% (95% interval 75% to 84%), up from
  76%: `IFERROR_MASK` rose from 28% to 60%, while `DUPLICATE_KEY` came out
  at 24% on a sample dominated by composite keys and one family of inventory
  grids (see `benchmarks/real_world_precision.md`). On the modified EUSES
  corpus 537 of 695 injected faults are found at the faulty cell instead of
  528 (recall 77%), with none lost: the nine gained were in workbooks the old
  report cap had filled.

### Fixed

- A suppression covering part of a finding that stands for several cells
  hid all of them, and a headline output other than a finding's first cell
  did not raise its severity.
- A suppression that matches no finding is reported in the coverage
  limitations, unless its rule is turned off, its rule went unchecked in an
  incomplete audit, or its sheet is out of scope.
- `'Revenue Detail'!B1` in `.audit-ignore` was split at the space and
  suppressed findings on the sheet `Revenue`; quoted sheet names (with `''`
  for an apostrophe, and `!` inside the quotes) now parse, and an unquoted
  sheet name with a space is rejected with the quoted form to use. Rule IDs
  match in any case.
- A bare target that reads like a cell (`Q1`, `FY2025`) suppressed that
  address on every sheet; a target without `!` is now always a sheet name,
  as documented.
- Sheet names containing a comma (`P&L, 2025`) could not be suppressed or
  annotated, and their findings had no `cell` in the JSON.
- A defined name over a sheet whose name holds an apostrophe
  (`'Bob''s Data'!A1:A5`) was reported as a broken reference.
- A What-If data table cell got a new fingerprint on every run.
- `--annotated` no longer fails on a finding located at a whole column or row
  (no built-in rule reports one; a custom check could).
- `--out report.sarif.json` wrote findings JSON instead of SARIF, and
  `--recalc-timeout 0` was accepted.
- The source archive built by `scripts/build_dist.py --release` took every
  file under its folders, ignored local output included; it now holds only
  the files git tracks. Release archives are built from a clean checkout, so
  published ones were not affected.

## [0.3.0] - 2026-09-25

Audit existing Excel models with clearer answers and fewer false alarms.
Context cards help distinguish mistakes from intentional formulas, while
portable commands make the skill easier to adopt in Claude and Codex.

Download the Claude or Codex skill ZIP from the release assets, or upgrade
the CLI with `python -m pip install --upgrade spreadsheet-auditor`.

### Clearer audit results

- Review each candidate alongside its labels, formula, cached value and
  neighbors. Multiple findings at one cell become one issue to investigate.
- Interpret intentional totals, lookup patterns, identifiers and layout
  more precisely when checking formulas and data quality.
- Compare additive totals when cross-footing; correct averages and scaled
  sums remain clear of cross-foot errors.
- Retain active failures when reports are capped, and show findings by rule,
  severity and confidence in the audit summary.
- Follow published precision and recall evaluations to understand detector
  coverage and remaining limitations.

### Easier adoption

- Start audits from any project folder with valid skill metadata, fresh
  report outputs and clear guidance for restricted runtimes.
- Use context cards to trace a finding to neighboring cells or linked totals
  before suggesting a repair.
- Try ready-to-run task evaluations with bundled synthetic workbooks.
- Access installation guidance, licensing and security information with the
  distributed skill packages.

### Reliable workbook handling

- Preserve source workbooks and every requested output by checking that
  report and annotated-copy destinations are distinct.
- Keep every finding attached to a cell in annotated copies.
- Keep grid checks active when a stray cell extends the workbook's used range.
- Recalculate in an isolated LibreOffice profile with macros disabled while
  retaining the original formulas for static checks.
- Identify frozen Google Sheets placeholders and explain coverage limits.

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

[Unreleased]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/petehottelet/spreadsheet-auditor/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/petehottelet/spreadsheet-auditor/releases/tag/v0.1.0
