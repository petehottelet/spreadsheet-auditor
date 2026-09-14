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
| BROKEN_REFERENCE | DET | High | A formula contains a deleted reference (`#REF!`), a missing sheet reference, or an out-of-bounds target. Links to an external workbook are inventoried as one Low/Info finding per source workbook per sheet, listing the linked cells. |
| BLANK_PRECEDENT | DET | Medium | A formula uses a blank cell in arithmetic, as a lookup key, or in a date or rounding function without testing it for blank, and the blank is a gap in a column that is at least three-quarters filled around it, on a row that holds data. Positional uses (`ROW`, `COLUMNS`), guarded uses (`=""`, `ISBLANK`, comparisons, `IFERROR`), blank-tolerant functions (`SUM`, `MIN`, `MAX`, `&`), rows whose inputs are all blank (a day off on a timesheet), half-filled ledger columns, and template rows are not reported. |
| CIRCULAR_REFERENCE | DET | High | Formula dependencies contain a cycle, including a total whose range includes its own cell. One finding per connected group of cells. References that only feed `ROW`, `ROWS`, `COLUMN`, `COLUMNS`, `ISREF`, `AREAS` or `CELL` are not dependencies, so a filled-down `ROWS(A$1:A3)` counter and the `CELL("filename",A1)` sheet-name idiom are not cycles. |
| FORMULA_DRIFT | DET | High | A formula breaks the relative pattern used by neighboring formulas. A row or column total that aggregates its own neighbors is exempt and does not dilute the majority. A cell that agrees with a formula above or below it (a different column by design, judged on exact pattern, or on shape when it is a structurally different formula), the seed cell of a chain (an opening balance, year 0 of a projection), and a totals row where one column sums and the next averages the same block are not drift. |
| IFERROR_MASK | HEUR | Medium | `IFERROR` or `IFNA` may be hiding a real error. One finding per formula pattern per sheet, listing the other cells that share it. |

## Hardcodes And Inputs

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| LITERAL_CONSTANT | DET | Medium | A non-trivial numeric literal is embedded in a formula instead of referenced from an input cell. Literals in structural argument slots (a `VLOOKUP` column index, a `MID` length, a `WEEKDAY` type, date parts, rounding digits) and unit constants (60, 3600) are skipped. One finding per formula pattern per sheet. |
| HARDCODE_IN_FORMULA_BLOCK | DET | High | A constant interrupts a run of formulas that share one relative pattern on both sides of it. Inputs that an adjacent subtotal sums are not plugs, and neither is a constant whose own row or column is a line of constants between two lines of formulas (an input column between two running-sum columns; one of the four corner cells may itself hold a plug or a total). A text label between the two formulas ends the block. |

## Reference And Range Errors

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| RANGE_EXCLUSION | DET | Critical | A total stops short of a plain number that sits between the range and the total. Text labels, headers, dates, and formula rows never count as excluded data; totals placed elsewhere and expanding running-total ranges (`$A$2:A2`) do not produce exclusion findings. |
| RANGE_INCLUDES_SUBTOTAL | DET | High | An aggregate range includes a subtotal row or column whose own formula aggregates cells that are also in the range (a double count). "Subtotal + Other" totals and labeled rows or columns of constants (a total carried forward) stay quiet. |
| RANGE_LENGTH_MISMATCH | DET | High | Peer aggregate formulas use inconsistent range lengths. One-cell aggregates (links such as `SUM(G5:G5)`) and peers whose ranges cover disjoint groups (debits beside credits) are not compared. |
| HIDDEN_STRUCTURE_IN_TOTAL | DET | Medium | A hidden row, column, or sheet feeds visible formulas. Hidden rows that feed the same formulas are reported together, listing the formulas they feed. `AGGREGATE` options 1/3/5/7 and `SUBTOTAL` 101-111 skip hidden rows by definition and are not dependents. |

## Reconciliation And Consistency

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| TOTAL_MISMATCH | DET | Critical | Either a total adds a cell that its own `SUM` range already covers (`=SUM(B2:B5)+B5`, static, High/Likely defect), or a bare `=SUM(range)` has a cached value that differs from its numeric components (stale or inconsistent calculation, Critical/Defect). Other aggregates such as `AVERAGE` or `SUM(...)/1000` are never compared. |
| CROSS_FOOT_FAILURE | DET | Critical | Row totals and column totals disagree in a rectangular table recognized from its formulas: a run of column totals defines the columns and rows, and each of those rows must carry a row total spanning exactly those columns. Stacked blocks sharing a total column are not confused. Value-dependent; requires cached or recalculated values. |

## Logic, Structure, And Data Hygiene

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| VOLATILE_FUNCTION | DET | Medium | Formula uses `OFFSET`, `INDIRECT`, `RAND` or `RANDBETWEEN`; one finding per formula pattern per sheet. `TODAY` and `NOW` are the normal way to age a date and get one Low/Info note per sheet. |
| WHOLE_COLUMN_REFERENCE | DET | Medium | A whole-column or whole-row reference is evaluated as an array: a comparison or arithmetic on it, `IF`, `SUMPRODUCT`, or `LOOKUP(2,1/(...))`. `COUNTIF`, `SUMIF`, `VLOOKUP`, `MATCH` and `INDEX` over whole columns bound themselves to the used range and are not reported, even inside an array formula. One finding per formula pattern per sheet. |
| NUMBERS_STORED_AS_TEXT | DET | High | Numeric-looking text that a formula consumes as a number (arithmetic, or a bare argument of a `SUM`-style function; High/Likely defect), or in a column that otherwise holds numbers (Medium/Review). Text with a leading zero (an identifier), and text that lookups, criteria, comparisons or `DATE` read, are not reported. |
| WHITESPACE_KEY | DET | Medium | A padded value among clean ones in a first-column label or a formula-referenced cell (Medium/Review). A column where at least three values, and four in five of them, are padded gets one Low/Info note (fixed-width export padding). Headers over data (the first row, or the second under a lone title), indentation of two or more leading spaces, and whitespace-only cells are not reported; a single stray leading space on a key still is. |
| DUPLICATE_KEY | DET | Medium | Duplicate normalized keys in the column a first-match lookup searches: the first column of a `VLOOKUP` table, the first row of an `HLOOKUP` table, or the lookup array of `MATCH`, `XMATCH`, `XLOOKUP` or `LOOKUP`. Criteria ranges of `SUMIF`/`COUNTIF`-style functions are not keys. |
| MERGED_CELL_IN_DATA_RANGE | DET | Medium | A merged region whose top-left cell holds a number lies inside a range that formulas read, or inside a table. Merged titles, headers, labels, blank spacers, merged formulas (net lines, ratios in totals rows), and merges that formulas only address directly are not reported. |

## Finance-Specific (opt-in)

These checks are off by default. Enable them by setting `finance.enabled: true`
in your config; they are intentionally label-driven heuristics and report
`Review`-confidence findings only.

| Rule ID | Mode | Default severity | Description |
|---|---:|---:|---|
| BALANCE_SHEET_BALANCE | HEUR | Medium | "Total Assets" disagrees with "Total Liabilities + Equity" on the same sheet. |
| SIGN_CONVENTION | HEUR | Medium | Row labelled as expense/cost has a positive value (or vice versa for revenue). |
| PERIOD_MISMATCH | HEUR | Medium | Quarterly column headers (e.g. `Q1 2024 -> Q3 2024`) skip a period. |
