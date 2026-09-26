# Eval inputs

## Bundled review fixtures

`evals/review-starter.json` uses three synthetic workbooks committed here:

- `inherited-budget.xlsx`: a copy of the bundled demo with omitted rows,
  duplicate components, a hardcoded total and a broken reference.
- `survey-averages.xlsx`: correct row and column averages with embedded
  numeric caches; these summaries must not be cross-footed as additive totals.
- `legacy-model.xlsx` and `legacy-config.json`: a broken reference, one
  suppressed rule and a one-finding cap; the remaining High finding must
  still fail the audit.

No downloads are needed for these cases. See `evals/README.md` for running
and recording model evaluations.

## Corpus-based task fixtures

The workbooks for `evals/evals.json` are not committed. Two come from SpreadsheetBench
(CC BY-SA 4.0, https://github.com/RUCKBReasoning/SpreadsheetBench) and one is
the bundled demo. Copy them here before running `evals/evals.json`:

```bash
python benchmarks/corpus/fetch.py spreadsheetbench
cp benchmarks/corpus/data/spreadsheetbench/files/all_data_912_v0.1/spreadsheet/CF_22493/3_CF_22493_input.xlsx evals/files/House_Budget.xlsx
cp benchmarks/corpus/data/spreadsheetbench/files/all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx evals/files/Ops_Tracker.xlsx
cp examples/demo_bad_budget.xlsx evals/files/Q3_Forecast.xlsx
```

Ground truth behind the expectations:

- `House_Budget.xlsx`: the auditor raises four `FORMULA_DRIFT` findings. Only
  `House Budget!F123` is a mistake: it sums column G under the "Total Spent"
  header, where its neighbours on row 123 each sum their own column. `C10`
  (Total Income), `Money In Checking Next Month!E61` (Total Left) and `L2`
  (under "Total Tax") differ from their neighbours by design.
- `Ops_Tracker.xlsx`: the real errors are `#VALUE!` in `formamspnc (7)!Q9:Q11`
  and `#REF!` in `I10:I11`. The 31 `HIDDEN_STRUCTURE_IN_TOTAL` findings describe
  one fact: 41 hidden helper columns. `C5` is one of three count cells
  (`B5:D5`), not drift.
- `Q3_Forecast.xlsx`: every finding is a seeded defect (see `examples/README.md`),
  spread over nine cells. Three of those cells each carry two findings.
