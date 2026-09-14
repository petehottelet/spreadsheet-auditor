# Check Catalog

Use this catalog to interpret `findings.json` emitted by `scripts/audit.py`.

## Detection Modes

- `DET`: deterministic candidate produced by code.
- `HEUR`: heuristic candidate requiring judgment.

## Confidence Levels

- `Defect`: very likely wrong (Confirmed bucket in the report).
- `Likely defect`: probably wrong or fragile (Likely bucket).
- `Review`: suspicious, needs confirmation (Review bucket).
- `Info`: informational notes (Info bucket; opt-in checks).

## Formula Integrity

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| LIVE_ERROR | DET | Critical | A cell contains or evaluates to an Excel error value such as `#REF!`, `#DIV/0!`, or `#VALUE!`. Reported once at the root cell; cells that merely inherit the error are listed as dependents. |
| BROKEN_REFERENCE | DET | High | A formula contains a deleted reference, missing sheet reference, unavailable external reference, or out-of-bounds target. |
| BLANK_PRECEDENT | DET | Medium | A formula references a blank cell whose row and column otherwise hold data. References into entirely empty rows or columns (future periods, spare inputs) are not reported. |
| CIRCULAR_REFERENCE | DET | High | Formula dependencies contain a cycle, including a total whose range includes its own cell. One finding per connected group of cells. |
| FORMULA_DRIFT | DET | High | A formula breaks the relative pattern used by neighboring formulas. A row or column total that aggregates its own neighbors is exempt and does not dilute the majority. |
| IFERROR_MASK | HEUR | Medium | `IFERROR` or `IFNA` may be hiding a real error. |

## Hardcodes And Inputs

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| LITERAL_CONSTANT | DET | Medium | A non-trivial numeric literal is embedded in a formula instead of referenced from an input cell. |
| HARDCODE_IN_FORMULA_BLOCK | DET | High | A constant interrupts a run of formulas that share one relative pattern on both sides of it. Inputs that an adjacent subtotal sums are not plugs. |

## Reference And Range Errors

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| RANGE_EXCLUSION | DET | Critical | A total stops short of a plain number that sits between the range and the total. Text labels, headers, dates, and formula rows never count as excluded data; totals placed elsewhere do not produce exclusion findings. |
| RANGE_INCLUDES_SUBTOTAL | DET | High | An aggregate range includes a subtotal row or column whose own formula aggregates cells that are also in the range (a double count). A labeled row holding a constant is reported at Medium/Review. "Subtotal + Other" totals stay quiet. |
| RANGE_LENGTH_MISMATCH | DET | High | Peer aggregate formulas use inconsistent range lengths. |
| HIDDEN_STRUCTURE_IN_TOTAL | DET | Medium | A hidden row, column, or sheet feeds visible formulas. One finding per hidden element, listing the formulas it feeds. |

## Reconciliation And Consistency

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| TOTAL_MISMATCH | DET | Critical | Either a total adds a cell that its own `SUM` range already covers (`=SUM(B2:B5)+B5`, static, High/Likely defect), or a bare `=SUM(range)` has a cached value that differs from its numeric components (stale or inconsistent calculation, Critical/Defect). Other aggregates such as `AVERAGE` or `SUM(...)/1000` are never compared. |
| CROSS_FOOT_FAILURE | DET | Critical | Row totals and column totals disagree in an explicit rectangular table. Value-dependent; requires cached or recalculated values. |

## Logic, Structure, And Data Hygiene

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| VOLATILE_FUNCTION | DET | Medium | Formula uses volatile or fragile functions such as `OFFSET`, `INDIRECT`, `RAND`, or `NOW`. |
| WHOLE_COLUMN_REFERENCE | DET | Medium | Formula references an entire row or column. |
| NUMBERS_STORED_AS_TEXT | DET | High | Numeric-looking text inside a range that a formula reads (High/Likely defect), or in a column that otherwise holds numbers (Medium/Review). Text numbers nothing consumes are not reported. |
| WHITESPACE_KEY | DET | Medium | First-column labels or formula-referenced cells have leading/trailing whitespace. |
| DUPLICATE_KEY | DET | Medium | Duplicate normalized keys inside a range that lookup-style functions search. |
| MERGED_CELL_IN_DATA_RANGE | DET | Medium | A merged region lies inside a range that formulas read or inside a table. Presentational merges (titles, banners) are not reported. |

## Finance-Specific (opt-in)

These checks are off by default. Enable them by setting `finance.enabled: true`
in your config; they are intentionally label-driven heuristics and report
`Review`-confidence findings only.

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| BALANCE_SHEET_BALANCE | HEUR | Medium | "Total Assets" disagrees with "Total Liabilities + Equity" on the same sheet. |
| SIGN_CONVENTION | HEUR | Medium | Row labelled as expense/cost has a positive value (or vice versa for revenue). |
| PERIOD_MISMATCH | HEUR | Medium | Quarterly column headers (e.g. `Q1 2024 -> Q3 2024`) skip a period. |
