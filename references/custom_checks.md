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
| `names`                | `NameTable` or `None`      | Defined names and structured table references resolved to A1 ranges. Pass it to `parse_formula` / `extract_references` as `names=` so `SUM(Revenue_FY)` and `Table1[Sales]` resolve. |
| `budget`               | `Budget` or `None`         | Cooperative deadline. Call `ctx.budget.tick()` once per row or formula in long loops; it raises `AuditTimeout` when `limits.timeout_seconds` has elapsed and the orchestrator records the interruption. |

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
- Long-running checks must poll the budget: call `ctx.budget.tick()` (or
  `spreadsheet_auditor.budget.tick(ctx.budget)`, which tolerates `None`) once
  per row or formula. When the global budget (`limits.timeout_seconds`,
  default 120) expires, `AuditTimeout` propagates to the orchestrator, which
  records a limitation and skips the remaining checks.
- Never materialize cells. `ws.cell()` and `ws[coord]` create missing cells
  and silently grow the used range; use `existing_cell` / `cell_value` from
  `spreadsheet_auditor.reference_resolver` and `iter_existing_cells` from
  `spreadsheet_auditor.workbook_inventory` instead.
- Parse formulas with `spreadsheet_auditor.formula_parser.parse_formula`
  rather than regular expressions; it is tokenizer-based and classifies
  references, functions, literals, names, tables, and external links.
- Detectors must be deterministic given the same input workbook + config so
  `fingerprint` matches across runs and suppressions stay stable.
