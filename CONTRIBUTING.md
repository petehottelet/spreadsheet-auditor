# Contributing

Thanks for considering a contribution! Spreadsheet Auditor is an audit-only
project; the bar for new checks is *deterministic, evidence-backed, and
benchmarked*. This guide explains how to add one safely.

## Quick start

```bash
git clone https://github.com/petehottelet/spreadsheet-auditor.git
cd spreadsheet-auditor
pip install -e ".[dev]"
spreadsheet-auditor --healthcheck
python -m pytest tests -q
```

Optional: install LibreOffice so value-dependent checks
(`TOTAL_MISMATCH`, `CROSS_FOOT_FAILURE`) can run.

```bash
# macOS
brew install --cask libreoffice

# Debian/Ubuntu
sudo apt-get install -y libreoffice-calc

# Windows
winget install --id TheDocumentFoundation.LibreOffice
```

## Project layout

```
spreadsheet_auditor/         # importable package
  audit.py                   # orchestrator + CLI entry point
  cli.py                     # console_scripts re-export
  checks/                    # plug-in check registry
    base.py                  # Check, CheckContext, register()
    formula_integrity.py
    ranges.py
    reconciliation.py
    data_hygiene.py
    finance.py               # opt-in HEUR pack
  finding.py                 # Finding dataclass + fingerprints
  report.py                  # markdown / html / payload rendering
  sarif.py                   # SARIF 2.1.0 output
  ...
scripts/                     # CLI shim + build/validate tools
  audit.py                   # backward-compat wrapper
  build_dist.py              # builds Claude/Codex skill zips
  quick_validate.py          # validates SKILL.md metadata
examples/                    # demo workbook, generated outputs, GH Actions
benchmarks/                  # seeded-defect matrix + methodology
references/                  # rule catalog, custom-check guide, limitations
schemas/                     # JSON schemas for config + findings
tests/                       # pytest suite (also runs in CI)
```

## Adding a new check

1. **Write the detector** in
   [`spreadsheet_auditor/checks/`](spreadsheet_auditor/checks/). Follow the
   pattern documented in
   [`references/custom_checks.md`](references/custom_checks.md): subclass
   `Check`, declare `rule_ids`/`name`/`mode`, implement `run`.
2. **Document the rule** in
   [`references/check_catalog.md`](references/check_catalog.md) with severity,
   mode, and a one-line description.
3. **Seed a benchmark workbook**. Add at least one positive case to
   [`scripts/create_seeded_corpus.py`](scripts/create_seeded_corpus.py) or
   [`examples/make_demo.py`](examples/make_demo.py), and add a matching entry
   to [`benchmarks/seeded_defects.json`](benchmarks/seeded_defects.json).
4. **Add unit tests** under `tests/` covering both the positive case and at
   least one realistic negative case (to prevent false positives).
5. **Regenerate artifacts**:
   ```bash
   python scripts/create_seeded_corpus.py
   python examples/make_demo.py
   python benchmarks/run_benchmark.py
   ```
6. **Run the full suite**:
   ```bash
   python -m pytest tests -q
   ```

## Coding conventions

- Python 3.11+.
- Type hints on public functions.
- No silent failures: every coverage gap must show up in
  `coverage.limitations` so the report stays honest.
- Detectors must be deterministic given the same input workbook + config so
  that `fingerprint` matches across runs.
- Don't add dependencies for marginal checks. Prefer `openpyxl` primitives.
- Heuristic checks default to `Review` confidence and HEUR mode. Default
  severity is `Medium` unless you can justify higher.
- Never write to the source workbook. Use a temp directory for any
  intermediate artifacts.

## Pull request checklist

- [ ] Tests pass locally (`python -m pytest tests -q`).
- [ ] `spreadsheet-auditor --healthcheck` still reports `Status: ready`.
- [ ] `python scripts/quick_validate.py .` passes.
- [ ] `python benchmarks/run_benchmark.py` regenerates and the matrix shows
      the new check as `detected`.
- [ ] If you changed user-visible behavior, update
      [`CHANGELOG.md`](CHANGELOG.md) under `## [Unreleased]`.
- [ ] If you changed the output schema, update
      [`schemas/findings.schema.json`](schemas/findings.schema.json) and any
      affected tests.
- [ ] If you added a new CLI flag, document it in `--help`, the README, and
      the GitHub Actions example.

## Releasing

Releases are tag-triggered. Pushing a tag like `v0.2.0` runs the release
workflow, which builds the source archive plus Claude/Codex skill zips, emits
SHA-256 checksums, attaches everything to the GitHub Release, and publishes the
wheel + sdist to PyPI via trusted publishing.

A maintainer typically:

1. Updates [`CHANGELOG.md`](CHANGELOG.md): moves entries from `Unreleased`
   into a new dated `## [vX.Y.Z]` section.
2. Bumps `__version__` in
   [`spreadsheet_auditor/__init__.py`](spreadsheet_auditor/__init__.py). This is
   the single source of truth: [`pyproject.toml`](pyproject.toml) reads the
   version dynamically from it, so there is nothing else to edit.
3. Regenerates demo and benchmark artifacts so the committed copies match the
   release (`python examples/make_demo.py && python benchmarks/run_benchmark.py`).
4. Commits, tags `vX.Y.Z`, and pushes the tag.

The version in the tag must match `__version__`; the release workflow asserts
this before building.

## Code of conduct

Be kind. Assume good intent. Discuss code, not contributors. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/) implicitly.
