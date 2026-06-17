# Spreadsheet Audit Report - demo_bad_budget.xlsx

## Executive Summary

- Tool version: `0.1.0` (run at 2026-06-17T03:25:07+00:00)
- Workbook SHA-256: `50ff284afb0c00b1aaf7b579a704fedbf0ef8ffb123bff1bd6d2dc6ee138b95f`
- Sheets analyzed: 2
- Formulas scanned: 28
- Recalculation status: unavailable
- Findings: 22 Critical, 35 High, 3 Medium, 0 Low, 0 Info
- Suppressed findings: 0

## Coverage And Limitations

- Macros present: False
- Macros executed: False
- External links present: False
- Limitation: LibreOffice/soffice not available; using static analysis and cached values only.
- Limitation: defusedxml is not available; XML parsing relies on workbook library defaults in this runtime.
- Limitation: Recalculation did not run; value-dependent checks (TOTAL_MISMATCH, CROSS_FOOT_FAILURE) rely on cached values and may be incomplete.

## Confirmed Findings

_Hard defects: the auditor is certain this is wrong._

### [HIGH] Formula contains deleted reference - BROKEN_REFERENCE

- ID: `BROKEN_REFERENCE-001`
- Location: `Budget!B14`
- Detection: DET; confidence: Defect
- Formula: `=SUM(#REF!)`
- Evidence: Formula text contains #REF!.
- Suggested fix: Restore the deleted reference or rebuild the formula from intended source cells.

## Likely Findings

_Strong defect candidates; review and confirm._

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-001`
- Location: `Budget!B11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B8)`
- Evidence: Budget!B2:B8 excludes adjacent above cell Budget!B1 with value 'Jan'.
- Suggested fix: Confirm whether Budget!B1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-002`
- Location: `Budget!B11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B8)`
- Evidence: Budget!B2:B8 excludes adjacent below cell Budget!B9 with value 300.
- Suggested fix: Confirm whether Budget!B9 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-003`
- Location: `Budget!B4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B3)`
- Evidence: Budget!B2:B3 excludes adjacent above cell Budget!B1 with value 'Jan'.
- Suggested fix: Confirm whether Budget!B1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-004`
- Location: `Budget!B6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B5)+B5`
- Evidence: Budget!B2:B5 excludes adjacent above cell Budget!B1 with value 'Jan'.
- Suggested fix: Confirm whether Budget!B1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-005`
- Location: `Budget!C11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C9)`
- Evidence: Budget!C2:C9 excludes adjacent above cell Budget!C1 with value 'Feb'.
- Suggested fix: Confirm whether Budget!C1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-006`
- Location: `Budget!C4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C3)`
- Evidence: Budget!C2:C3 excludes adjacent above cell Budget!C1 with value 'Feb'.
- Suggested fix: Confirm whether Budget!C1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-007`
- Location: `Budget!C6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C5)`
- Evidence: Budget!C2:C5 excludes adjacent above cell Budget!C1 with value 'Feb'.
- Suggested fix: Confirm whether Budget!C1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-008`
- Location: `Budget!D11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D9)`
- Evidence: Budget!D2:D9 excludes adjacent above cell Budget!D1 with value 'Mar'.
- Suggested fix: Confirm whether Budget!D1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-009`
- Location: `Budget!D4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D3)`
- Evidence: Budget!D2:D3 excludes adjacent above cell Budget!D1 with value 'Mar'.
- Suggested fix: Confirm whether Budget!D1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-010`
- Location: `Budget!D6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D5)`
- Evidence: Budget!D2:D5 excludes adjacent above cell Budget!D1 with value 'Mar'.
- Suggested fix: Confirm whether Budget!D1 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-011`
- Location: `Budget!E10`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B10:D10)`
- Evidence: Budget!B10:D10 excludes adjacent left cell Budget!A10 with value 'COGS total'.
- Suggested fix: Confirm whether Budget!A10 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-012`
- Location: `Budget!E11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B11:D11)`
- Evidence: Budget!B11:D11 excludes adjacent left cell Budget!A11 with value 'Grand total'.
- Suggested fix: Confirm whether Budget!A11 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-013`
- Location: `Budget!E12`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B12:D12)`
- Evidence: Budget!B12:D12 excludes adjacent left cell Budget!A12 with value 'Adjustment (hidden)'.
- Suggested fix: Confirm whether Budget!A12 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-014`
- Location: `Budget!E13`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B13:D13)`
- Evidence: Budget!B13:D13 excludes adjacent left cell Budget!A13 with value 'With adjustment'.
- Suggested fix: Confirm whether Budget!A13 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-015`
- Location: `Budget!E2`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:D2)`
- Evidence: Budget!B2:D2 excludes adjacent left cell Budget!A2 with value 'Subscriptions'.
- Suggested fix: Confirm whether Budget!A2 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-016`
- Location: `Budget!E3`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B3:D3)`
- Evidence: Budget!B3:D3 excludes adjacent left cell Budget!A3 with value 'Services'.
- Suggested fix: Confirm whether Budget!A3 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-017`
- Location: `Budget!E4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:D4)`
- Evidence: Budget!B4:D4 excludes adjacent left cell Budget!A4 with value 'Subtotal'.
- Suggested fix: Confirm whether Budget!A4 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-018`
- Location: `Budget!E5`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B5:D5)`
- Evidence: Budget!B5:D5 excludes adjacent left cell Budget!A5 with value 'Other revenue'.
- Suggested fix: Confirm whether Budget!A5 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-019`
- Location: `Budget!E6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Budget!B6:C6 excludes adjacent left cell Budget!A6 with value 'Revenue total'.
- Suggested fix: Confirm whether Budget!A6 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-020`
- Location: `Budget!E6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Budget!B6:C6 excludes adjacent right cell Budget!D6 with value '=SUM(D2:D5)'.
- Suggested fix: Confirm whether Budget!D6 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-021`
- Location: `Budget!E7`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B7:D7)`
- Evidence: Budget!B7:D7 excludes adjacent left cell Budget!A7 with value 'Hosting'.
- Suggested fix: Confirm whether Budget!A7 belongs in the aggregate, then extend the range if appropriate.

### [CRITICAL] Aggregation range appears to exclude adjacent data column - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-022`
- Location: `Budget!E8`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B8:D8)`
- Evidence: Budget!B8:D8 excludes adjacent left cell Budget!A8 with value 'Support staff'.
- Suggested fix: Confirm whether Budget!A8 belongs in the aggregate, then extend the range if appropriate.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-001`
- Location: `Budget!E10`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B10:D10)`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=3): =SUM(R-3C+0:R-1C+0)
- Evidence: This cell: =SUM(R+0C-3:R+0C-1)
- Evidence: Neighboring formulas: Budget!D10==SUM(D7:D9)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-002`
- Location: `Budget!E13`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B13:D13)`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=3): =R-2C+0+R-1C+0
- Evidence: This cell: =SUM(R+0C-3:R+0C-1)
- Evidence: Neighboring formulas: Budget!D13==D11+D12
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-003`
- Location: `Budget!E4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:D4)`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=3): =SUM(R-2C+0:R-1C+0)
- Evidence: This cell: =SUM(R+0C-3:R+0C-1)
- Evidence: Neighboring formulas: Budget!D4==SUM(D2:D3)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-004`
- Location: `Budget!E6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Formula differs from the dominant relative pattern in this column.
- Evidence: Dominant pattern (n=6): =SUM(R+0C-3:R+0C-1)
- Evidence: This cell: =SUM(R+0C-3:R+0C-2)
- Evidence: Neighboring formulas: Budget!E5==SUM(B5:D5); Budget!E7==SUM(B7:D7)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-001`
- Location: `Budget!B12`
- Detection: DET; confidence: Likely defect
- Evidence: Value 50 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-002`
- Location: `Budget!B5`
- Detection: DET; confidence: Likely defect
- Evidence: Value 150 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-003`
- Location: `Budget!B7`
- Detection: DET; confidence: Likely defect
- Evidence: Value 200 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-004`
- Location: `Budget!B8`
- Detection: DET; confidence: Likely defect
- Evidence: Value 600 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-005`
- Location: `Budget!B9`
- Detection: DET; confidence: Likely defect
- Evidence: Value 300 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-006`
- Location: `Budget!C12`
- Detection: DET; confidence: Likely defect
- Evidence: Value 60 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-007`
- Location: `Budget!C5`
- Detection: DET; confidence: Likely defect
- Evidence: Value 175 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-008`
- Location: `Budget!C7`
- Detection: DET; confidence: Likely defect
- Evidence: Value 210 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-009`
- Location: `Budget!C8`
- Detection: DET; confidence: Likely defect
- Evidence: Value 620 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-010`
- Location: `Budget!C9`
- Detection: DET; confidence: Likely defect
- Evidence: Value 320 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-011`
- Location: `Budget!D12`
- Detection: DET; confidence: Likely defect
- Evidence: Value 70 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-012`
- Location: `Budget!D5`
- Detection: DET; confidence: Likely defect
- Evidence: Value 200 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-013`
- Location: `Budget!D7`
- Detection: DET; confidence: Likely defect
- Evidence: Value 220 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-014`
- Location: `Budget!D8`
- Detection: DET; confidence: Likely defect
- Evidence: Value 640 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-015`
- Location: `Budget!D9`
- Detection: DET; confidence: Likely defect
- Evidence: Value 340 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-016`
- Location: `Budget!E9`
- Detection: DET; confidence: Likely defect
- Evidence: Value 999 sits between formulas in the same row or column.
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Numeric-looking value stored as text - NUMBERS_STORED_AS_TEXT

- ID: `NUMBERS_STORED_AS_TEXT-001`
- Location: `Budget!B20`
- Detection: DET; confidence: Likely defect
- Evidence: Cell contains text value '1,250', which may be ignored by numeric formulas.
- Suggested fix: Convert the value to a number or confirm it is intentionally text.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-001`
- Location: `Budget!B11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B8)`
- Evidence: Budget!B2:B8 includes row 4, labeled 'subtotal'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-002`
- Location: `Budget!B11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B8)`
- Evidence: Budget!B2:B8 includes row 6, labeled 'revenue total'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-003`
- Location: `Budget!B6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B2:B5)+B5`
- Evidence: Budget!B2:B5 includes row 4, labeled 'subtotal'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-004`
- Location: `Budget!C11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C9)`
- Evidence: Budget!C2:C9 includes row 4, labeled 'subtotal =sum(b2:b3)'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-005`
- Location: `Budget!C11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C9)`
- Evidence: Budget!C2:C9 includes row 6, labeled 'revenue total =sum(b2:b5)+b5'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-006`
- Location: `Budget!C6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(C2:C5)`
- Evidence: Budget!C2:C5 includes row 4, labeled 'subtotal =sum(b2:b3)'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-007`
- Location: `Budget!D11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D9)`
- Evidence: Budget!D2:D9 includes row 4, labeled 'subtotal =sum(b2:b3) =sum(c2:c3)'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-008`
- Location: `Budget!D11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D9)`
- Evidence: Budget!D2:D9 includes row 6, labeled 'revenue total =sum(b2:b5)+b5 =sum(c2:c5)'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-009`
- Location: `Budget!D6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(D2:D5)`
- Evidence: Budget!D2:D5 includes row 4, labeled 'subtotal =sum(b2:b3) =sum(c2:c3)'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-010`
- Location: `Budget!E10`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B10:D10)`
- Evidence: Budget!B10:D10 includes row 10, labeled 'cogs total'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-011`
- Location: `Budget!E11`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B11:D11)`
- Evidence: Budget!B11:D11 includes row 11, labeled 'grand total'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-012`
- Location: `Budget!E4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:D4)`
- Evidence: Budget!B4:D4 includes row 4, labeled 'subtotal'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

### [HIGH] Aggregation range appears to include subtotal or total row - RANGE_INCLUDES_SUBTOTAL

- ID: `RANGE_INCLUDES_SUBTOTAL-013`
- Location: `Budget!E6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Budget!B6:C6 includes row 6, labeled 'revenue total'.
- Suggested fix: Review the aggregate range and exclude subtotal/total rows unless intentionally double-counting.

## Review Findings

_Heuristic flags; worth a second look but may be intentional._

### [MEDIUM] Duplicate normalized key in first column - DUPLICATE_KEY

- ID: `DUPLICATE_KEY-001`
- Location: `Budget!A17, Budget!A18`
- Detection: DET; confidence: Review
- Evidence: Normalized key 'north' appears 2 times.
- Suggested fix: Confirm duplicate labels are intentional, especially if lookup formulas depend on this column.

### [MEDIUM] Aggregate includes hidden structure - HIDDEN_STRUCTURE_IN_TOTAL

- ID: `HIDDEN_STRUCTURE_IN_TOTAL-001`
- Location: `Budget!E12`
- Detection: DET; confidence: Review
- Formula: `=SUM(B12:D12)`
- Evidence: Budget!B12:D12 intersects hidden rows [12].
- Suggested fix: Confirm hidden inputs are intentional and disclosed in visible workbook documentation.

### [MEDIUM] Text has leading or trailing whitespace - WHITESPACE_KEY

- ID: `WHITESPACE_KEY-001`
- Location: `Budget!A18`
- Detection: DET; confidence: Review
- Evidence: Raw value is ' North '.
- Suggested fix: Trim the value if it is used as a lookup key or label.

## Suppressed Findings Summary

No suppressed findings.

## Recommended Next Steps

1. Start with the **Confirmed** section: every item there is a hard defect.
2. Walk the **Likely** section, comparing each flagged formula to its neighbors (drift findings include them inline).
3. Recalculate the workbook in Excel if value-dependent checks were skipped due to recalculation being unavailable.
4. Rerun the audit after fixes; keep suppressions only for intentional patterns with documented reasons.

## Non-Certification Disclaimer

This audit inspected formulas, ranges, workbook structure, hidden rows/columns/sheets, cached/recalculated values where available, and selected data-hygiene issues. It did not execute macros, validate external data sources, fully evaluate Power Query/Data Model objects, or certify business assumptions. Findings are defect candidates and likely errors, not a legal/accounting certification of correctness.
