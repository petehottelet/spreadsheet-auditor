# Changelog

All notable changes to **Spreadsheet Auditor** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
