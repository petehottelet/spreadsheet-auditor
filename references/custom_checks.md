# Writing a Custom Check

The Spreadsheet Auditor runs *checks* registered in
[`spreadsheet_auditor/checks/`](../spreadsheet_auditor/checks/). Adding a new
detector is a three-step exercise: subclass `Check`, decorate it with
`@register`, drop the module into the package.

## Anatomy of a check

```python
from spreadsheet_auditor.checks import Check, CheckContext, register
from spreadsheet_auditor.finding import Finding


@register
class MyHardcodedYearCheck(Check):
    name = "hardcoded_year"
    description = "Flags formulas containing a literal year (1900..2099)."
    rule_ids = ("HARDCODED_YEAR",)
    mode = "HEUR"

    def run(self, ctx: CheckContext) -> list[Finding]:
        findings: list[Finding] = []
        for cell in ctx.formulas:
            formula = cell.get("formula", "")
            for token in formula.replace(",", " ").split():
                if token.isdigit() and 1900 <= int(token) <= 2099:
                    findings.append(
                        Finding(
                            rule_id="HARDCODED_YEAR",
                            severity="Low",
                            error_confidence="Review",
                            detection_mode="HEUR",
                            location=cell["location"],
                            title="Formula contains a literal year",
                            formula=formula,
                            evidence=[f"Literal year {token} in formula."],
                            suggested_fix="Consider replacing with a named input or YEAR(...) lookup.",
                        )
                    )
        return findings
```

## CheckContext

`CheckContext` carries everything a detector usually needs:

| Field                  | Type                       | Notes                                                |
| ---------------------- | -------------------------- | ---------------------------------------------------- |
| `workbook_path`        | `pathlib.Path`             | Original workbook (the source, not the temp copy).   |
| `formula_wb`           | `openpyxl.Workbook`        | Loaded with formulas (`data_only=False`).            |
| `value_wb`             | `openpyxl.Workbook`        | Loaded with cached values (`data_only=True`).        |
| `allowed_sheet_names`  | `set[str]`                 | Sheets that pass the config's scope filter.          |
| `formulas`             | `list[dict]`               | Formula cells with `sheet`, `row`, `col`, `location`, `formula`. |
| `config`               | `dict`                     | Parsed config (or `{}`).                             |
| `inventory`            | `dict`                     | Workbook inventory (macros, external links, sheets). |
| `unsupported_features` | `set[str]`                 | Append to this when a check encounters a feature it cannot reason about (e.g. dynamic arrays). |

## Severity, confidence, and mode conventions

- `severity`: one of `Critical`, `High`, `Medium`, `Low`, `Info`.
- `error_confidence`: `Defect` (proven wrong), `Likely defect` (very high
  confidence heuristic), `Review` (worth a second look), `Info` (purely
  informational).
- `detection_mode`: `DET` for deterministic checks, `HEUR` for heuristic ones.
  Heuristic findings should default to a confidence of `Review` unless you have
  strong evidence.

## Adding the check to the catalog

1. Add a row to [`references/check_catalog.md`](check_catalog.md) describing
   the new rule ID, severity, and short rationale.
2. If you want the check to be benchmark-tracked, add a seeded entry to
   [`benchmarks/seeded_defects.json`](../benchmarks/seeded_defects.json) and a
   matching defect in
   [`scripts/create_seeded_corpus.py`](../scripts/create_seeded_corpus.py).
3. Add a unit test under `tests/` exercising both positive and negative cases.

## Running just your check

For fast iteration, instantiate and run the check directly in a script or
REPL using `CheckContext`. The full orchestrator is in
`spreadsheet_auditor.audit.audit_workbook`; only the registry call there
needs to be reused.

## Performance contract

- Checks should respect `ctx.config.get("limits")` when they iterate broadly.
- Long-running checks should yield control frequently; the orchestrator does
  not enforce a per-check timeout but stops invoking further checks once the
  global timeout (`limits.timeout_seconds`) is exceeded.
- Detectors must be deterministic given the same input workbook + config so
  `fingerprint` matches across runs and suppressions stay stable.
