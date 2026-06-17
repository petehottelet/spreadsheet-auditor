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
| LIVE_ERROR | DET | Critical | A cell contains or evaluates to an Excel error value such as `#REF!`, `#DIV/0!`, or `#VALUE!`. |
| BROKEN_REFERENCE | DET | High | A formula contains a deleted reference, missing sheet reference, unavailable external reference, or out-of-bounds target. |
| BLANK_PRECEDENT | DET | Medium | A formula references a blank cell in a calculation path. |
| CIRCULAR_REFERENCE | DET | High | Formula dependencies contain a cycle. |
| FORMULA_DRIFT | DET | High | A formula breaks the relative pattern used by neighboring formulas. |
| IFERROR_MASK | HEUR | Medium | `IFERROR` or `IFNA` may be hiding a real error. |

## Hardcodes And Inputs

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| LITERAL_CONSTANT | DET | Medium | A non-trivial numeric literal is embedded in a formula instead of referenced from an input cell. |
| HARDCODE_IN_FORMULA_BLOCK | DET | High | A constant appears inside a row or column that otherwise contains formulas. |

## Reference And Range Errors

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| RANGE_EXCLUSION | DET | Critical | An aggregate range appears to omit adjacent data. |
| RANGE_INCLUDES_SUBTOTAL | DET | High | An aggregate range appears to include a subtotal, total, or header row. |
| RANGE_LENGTH_MISMATCH | DET | High | Peer aggregate formulas use inconsistent range lengths. |
| HIDDEN_STRUCTURE_IN_TOTAL | DET | Medium | Hidden rows, columns, or sheets intersect formula inputs. |

## Reconciliation And Consistency

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| TOTAL_MISMATCH | DET | Critical | A cached/recalculated total differs from the sum of referenced components. |
| CROSS_FOOT_FAILURE | DET | Critical | Row totals and column totals disagree in an explicit rectangular table. Value-dependent; requires cached or recalculated values. |

## Logic, Structure, And Data Hygiene

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| VOLATILE_FUNCTION | DET | Medium | Formula uses volatile or fragile functions such as `OFFSET`, `INDIRECT`, `RAND`, or `NOW`. |
| WHOLE_COLUMN_REFERENCE | DET | Medium | Formula references an entire row or column. |
| NUMBERS_STORED_AS_TEXT | DET | High | Numeric-looking text appears in a numeric region. |
| WHITESPACE_KEY | DET | Medium | Labels or keys have leading/trailing whitespace. |
| DUPLICATE_KEY | DET | Medium | Duplicate normalized labels or keys may break lookups. |
| MERGED_CELL_IN_DATA_RANGE | DET | Medium | Merged cells intersect a used data range. |

## Finance-Specific (opt-in)

These checks are off by default. Enable them by setting `finance.enabled: true`
in your config; they are intentionally label-driven heuristics and report
`Review`-confidence findings only.

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| BALANCE_SHEET_BALANCE | HEUR | Medium | "Total Assets" disagrees with "Total Liabilities + Equity" on the same sheet. |
| SIGN_CONVENTION | HEUR | Medium | Row labelled as expense/cost has a positive value (or vice versa for revenue). |
| PERIOD_MISMATCH | HEUR | Medium | Quarterly column headers (e.g. `Q1 2024 -> Q3 2024`) skip a period. |
