# Real-world corpus measurement

The seeded benchmark in `benchmarks/seeded_defects.json` answers "does each
rule fire on the defect it was built for?". It cannot answer the question a
reviewer actually asks: **when the auditor flags a cell in a workbook it has
never seen, how often is it right?** This harness answers that against public
corpora of real spreadsheets.

## Pipeline

```bash
python benchmarks/corpus/fetch.py spreadsheetbench          # ~100 MB, extracts to benchmarks/corpus/data/
python benchmarks/corpus/run_corpus.py spreadsheetbench     # audits every _input workbook, ~10 min on 4 workers
python benchmarks/corpus/sample.py spreadsheetbench         # 20 findings per rule -> samples/spreadsheetbench.md
#   ... label the cards in labels/spreadsheetbench.json ...
python benchmarks/corpus/report.py spreadsheetbench         # -> benchmarks/real_world_precision.md
```

`data/` and `results/` are gitignored. `samples/`, `labels/`, and the report
are committed, so the numbers are reproducible and the judgment calls are
reviewable.

## Corpora

See [`sources.json`](sources.json). SpreadsheetBench (CC BY-SA 4.0) is the
default precision corpus: 2,732 real Excel-forum workbooks, modern and
formula-heavy, saved by Excel so cached values are present. The modified
EUSES corpus adds recall: each workbook carries one injected formula fault at
a known cell. FUSE is registered for a future large-scale run.

## Labeling protocol

Each sampled finding gets a card: the formula, its cached value, row labels,
column header, a 5x5 neighbourhood, and the values inside and just outside
the first referenced range. Judge from the card:

- **TP**: the finding points at something a careful reviewer would want to
  look at, for the reason the rule gives. A deliberate plug is still a TP for
  `HARDCODE_IN_FORMULA_BLOCK`; the rule promises to surface plugs.
- **FP**: the rule misread the workbook (a label taken for data, a total
  that is not a total, a pattern that is not a pattern).
- **unsure**: the card is not enough to decide. Unsure labels are excluded
  from precision and reported separately.

Record a one-line reason for every label. Precision is TP / (TP + FP) with a
Wilson 95% interval; read the interval, not the point estimate.

## Keys

A sampled finding is keyed `<sha256[:12]>|<rule>|<location>`. Re-running the
corpus after a code change keeps every label whose workbook and finding are
unchanged and leaves new findings unlabeled, so the report shows exactly what
still needs a human look.
