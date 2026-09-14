# Spreadsheet Audit Report - demo_bad_budget.xlsx

## Executive Summary

- Tool version: `0.1.0` (run at 2026-09-14T02:52:10+00:00)
- Workbook SHA-256: `9fcd67e466bbfbda3686e8f22a151b4186538f599654e526fafbf351c69e369e`
- Sheets analyzed: 2
- Formulas scanned: 30
- Recalculation status: unavailable
- Findings: 1 Critical, 7 High, 3 Medium, 0 Low, 0 Info
- Suppressed findings: 0

## Coverage And Limitations

- Macros present: False
- Macros executed: False
- External links present: False
- Limitation: LibreOffice/soffice not available; using static analysis and cached values only.
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
- Location: `Budget!B10`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B7:B8)`
- Evidence: Budget!B7:B8 stops short of Budget!B9 (value 300), which sits below the range, between it and the total.
- Suggested fix: Confirm whether Budget!B9 belongs in the aggregate, then extend the range if appropriate.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-001`
- Location: `Budget!B10`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B7:B8)`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=2): =SUM(R[-3]C:R[-1]C)
- Evidence: This cell: =SUM(R[-3]C:R[-2]C)
- Evidence: Neighboring formulas: Budget!C10==SUM(C7:C9)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-002`
- Location: `Budget!B6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:B5)+B5`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=2): =SUM(R[-2]C:R[-1]C)
- Evidence: This cell: =SUM(R[-2]C:R[-1]C)+R[-1]C
- Evidence: Neighboring formulas: Budget!C6==SUM(C4:C5)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-003`
- Location: `Budget!E6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Formula differs from the dominant relative pattern in this column.
- Evidence: Dominant pattern (n=6): =SUM(RC[-3]:RC[-1])
- Evidence: This cell: =SUM(RC[-3]:RC[-2])
- Evidence: Neighboring formulas: Budget!E5==SUM(B5:D5); Budget!E7==SUM(B7:D7)
- Suggested fix: Compare this formula to adjacent formulas and restore the intended relative references.

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-001`
- Location: `Budget!E9`
- Detection: DET; confidence: Likely defect
- Evidence: Value 999 sits between Budget!E8 and Budget!E10, which share the pattern =SUM(RC[-3]:RC[-1]).
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.

### [HIGH] Numeric-looking value stored as text - NUMBERS_STORED_AS_TEXT

- ID: `NUMBERS_STORED_AS_TEXT-001`
- Location: `Budget!B20`
- Detection: DET; confidence: Likely defect
- Evidence: Cell contains text value '1,250' and is referenced by a formula; numeric functions such as SUM ignore text.
- Suggested fix: Convert the value to a number or confirm it is intentionally text.

### [HIGH] Total double-counts a cell inside its own range - TOTAL_MISMATCH

- ID: `TOTAL_MISMATCH-001`
- Location: `Budget!B6`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:B5)+B5`
- Evidence: =SUM(B4:B5)+B5 adds B5, which is already inside B4:B5.
- Suggested fix: Remove the duplicated term or shrink the range so each component is counted once.

## Review Findings

_Heuristic flags; worth a second look but may be intentional._

### [MEDIUM] Duplicate key in lookup range - DUPLICATE_KEY

- ID: `DUPLICATE_KEY-001`
- Location: `Budget!A17, Budget!A18`
- Detection: DET; confidence: Review
- Evidence: Normalized key 'north' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- Suggested fix: Make the keys unique or confirm the lookup is meant to return the first match.

### [MEDIUM] Formula inputs include hidden structure - HIDDEN_STRUCTURE_IN_TOTAL

- ID: `HIDDEN_STRUCTURE_IN_TOTAL-001`
- Location: `Budget!B13`
- Detection: DET; confidence: Review
- Formula: `=B11+B12`
- Evidence: Hidden row 12 on Budget feeds 3 visible formula(s): Budget!B13, Budget!C13, Budget!D13.
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
