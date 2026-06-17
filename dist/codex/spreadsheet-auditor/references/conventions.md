# Spreadsheet Conventions

Audit against these conventions when the workbook appears to be a financial model or analytical workbook.

- Inputs should be separated from formulas.
- Formulas should reference assumption cells instead of embedding non-trivial literals.
- Projection formulas should be consistent across periods unless a visible transition explains the change.
- Totals should include the full data block and exclude subtotals unless explicitly intended.
- Hidden rows, hidden columns, and hidden sheets should not silently affect visible headline outputs.
- Hardcodes should have a source note, comment, or nearby label.
- Workbooks should have no live formula errors on delivery.
- Circular references should be explicit and documented if intentionally used.
- External links should be disclosed.

These conventions are heuristics, not laws. Use workbook labels and surrounding structure before calling a pattern wrong.
