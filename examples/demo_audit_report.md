# Spreadsheet Audit Report - demo_bad_budget.xlsx

## Executive Summary

- Audit status: complete
- Tool version: `0.4.0` (run at 2026-10-01T04:14:12+00:00)
- Workbook SHA-256: `465648d14e4be9f83fb9f1559cd3a1c02942d4a07de1049635c0967ab411835c`
- Sheets analyzed: 2
- Formulas scanned: 30
- Recalculation status: completed
- Findings: 3 Critical, 7 High, 3 Medium, 0 Low, 0 Info
- Suppressed findings: 0

## Coverage And Limitations

- Macros present: False
- Macros executed: False
- External links present: False

## Confirmed Findings

_Hard defects: the auditor is certain this is wrong._

### [CRITICAL] Row totals and column totals disagree - CROSS_FOOT_FAILURE

- ID: `CROSS_FOOT_FAILURE-001`
- Location: `Budget!E6`
- Fingerprint: `1d6057391ddd5534`
- Detection: DET; confidence: Defect
- Evidence: Row totals E4:E5 sum to 7015.0; column totals B6:D6 sum to 7165.0.
- Impact: {"estimated_delta": -150.0}
- Suggested fix: Reconcile the totals row and totals column; one of the contributing aggregates is likely wrong.
- If intended, accept it in `.audit-ignore`: `CROSS_FOOT_FAILURE Budget!E6 fingerprint:1d6057391ddd5534 <reason>`

### [CRITICAL] Cell contains live spreadsheet error - LIVE_ERROR

- ID: `LIVE_ERROR-001`
- Location: `Budget!B14`
- Fingerprint: `25a6f1a375234871`
- Detection: DET; confidence: Defect
- Formula: `=SUM(#REF!)`
- Evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- Suggested fix: Trace the formula precedent chain and resolve the underlying spreadsheet error.
- If intended, accept it in `.audit-ignore`: `LIVE_ERROR Budget!B14 fingerprint:25a6f1a375234871 <reason>`

### [HIGH] Formula contains deleted reference - BROKEN_REFERENCE

- ID: `BROKEN_REFERENCE-001`
- Location: `Budget!B14`
- Fingerprint: `20794961a090cc88`
- Detection: DET; confidence: Defect
- Formula: `=SUM(#REF!)`
- Evidence: Formula text contains #REF!.
- Suggested fix: Restore the deleted reference or rebuild the formula from intended source cells.
- If intended, accept it in `.audit-ignore`: `BROKEN_REFERENCE Budget!B14 fingerprint:20794961a090cc88 <reason>`

## Likely Findings

_Strong defect candidates; review and confirm._

### [CRITICAL] Aggregation range appears to exclude adjacent data row - RANGE_EXCLUSION

- ID: `RANGE_EXCLUSION-001`
- Location: `Budget!B10`
- Fingerprint: `bc4764157bc642c4`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B7:B8)`
- Evidence: Budget!B7:B8 stops short of Budget!B9 (value 300), which sits below the range, between it and the total.
- Suggested fix: Confirm whether Budget!B9 belongs in the aggregate, then extend the range if appropriate.
- If intended, accept it in `.audit-ignore`: `RANGE_EXCLUSION Budget!B10 fingerprint:bc4764157bc642c4 <reason>`

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-001`
- Location: `Budget!B10`
- Fingerprint: `84425aadc6e1a0c9`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B7:B8)`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=2): =SUM(R[-3]C:R[-1]C)
- Evidence: This cell: =SUM(R[-3]C:R[-2]C)
- Evidence: Neighboring formulas: Budget!C10==SUM(C7:C9)
- Suggested fix: If this cell is the same kind of line as its neighbors, restore their pattern. A total, net or summary line differs by design: compare it with the other totals instead.
- If intended, accept it in `.audit-ignore`: `FORMULA_DRIFT Budget!B10 fingerprint:84425aadc6e1a0c9 <reason>`

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-002`
- Location: `Budget!B6`
- Fingerprint: `d2c8451808c1ab24`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:B5)+B5`
- Evidence: Formula differs from the dominant relative pattern in this row.
- Evidence: Dominant pattern (n=2): =SUM(R[-2]C:R[-1]C)
- Evidence: This cell: =SUM(R[-2]C:R[-1]C)+R[-1]C
- Evidence: Neighboring formulas: Budget!C6==SUM(C4:C5)
- Suggested fix: If this cell is the same kind of line as its neighbors, restore their pattern. A total, net or summary line differs by design: compare it with the other totals instead.
- If intended, accept it in `.audit-ignore`: `FORMULA_DRIFT Budget!B6 fingerprint:d2c8451808c1ab24 <reason>`

### [HIGH] Formula breaks neighboring pattern - FORMULA_DRIFT

- ID: `FORMULA_DRIFT-003`
- Location: `Budget!E6`
- Fingerprint: `a5bbd2d71e743d9d`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B6:C6)`
- Evidence: Formula differs from the dominant relative pattern in this column.
- Evidence: Dominant pattern (n=6): =SUM(RC[-3]:RC[-1])
- Evidence: This cell: =SUM(RC[-3]:RC[-2])
- Evidence: Neighboring formulas: Budget!E5==SUM(B5:D5); Budget!E7==SUM(B7:D7)
- Suggested fix: If this cell is the same kind of line as its neighbors, restore their pattern. A total, net or summary line differs by design: compare it with the other totals instead.
- If intended, accept it in `.audit-ignore`: `FORMULA_DRIFT Budget!E6 fingerprint:a5bbd2d71e743d9d <reason>`

### [HIGH] Hardcoded value inside formula block - HARDCODE_IN_FORMULA_BLOCK

- ID: `HARDCODE_IN_FORMULA_BLOCK-001`
- Location: `Budget!E9`
- Fingerprint: `24064dc98bd42f48`
- Detection: DET; confidence: Likely defect
- Evidence: Value 999 sits between Budget!E8 and Budget!E10, which share the pattern =SUM(RC[-3]:RC[-1]).
- Suggested fix: Confirm whether this is an intentional plug. If not, restore the formula pattern.
- If intended, accept it in `.audit-ignore`: `HARDCODE_IN_FORMULA_BLOCK Budget!E9 fingerprint:24064dc98bd42f48 <reason>`

### [HIGH] Numeric-looking value stored as text - NUMBERS_STORED_AS_TEXT

- ID: `NUMBERS_STORED_AS_TEXT-001`
- Location: `Budget!B20`
- Fingerprint: `66b0472a92d25f95`
- Detection: DET; confidence: Likely defect
- Evidence: Cell contains text value '1,250' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- Suggested fix: Convert the values to numbers or confirm they are intentionally text.
- If intended, accept it in `.audit-ignore`: `NUMBERS_STORED_AS_TEXT Budget!B20 fingerprint:66b0472a92d25f95 <reason>`

### [HIGH] Total double-counts a cell inside its own range - TOTAL_MISMATCH

- ID: `TOTAL_MISMATCH-001`
- Location: `Budget!B6`
- Fingerprint: `d8afb5cd595c8b70`
- Detection: DET; confidence: Likely defect
- Formula: `=SUM(B4:B5)+B5`
- Evidence: =SUM(B4:B5)+B5 adds B5, which is already inside B4:B5.
- Suggested fix: Remove the duplicated term or shrink the range so each component is counted once.
- If intended, accept it in `.audit-ignore`: `TOTAL_MISMATCH Budget!B6 fingerprint:d8afb5cd595c8b70 <reason>`

## Review Findings

_Heuristic flags; worth a second look but may be intentional._

### [MEDIUM] Duplicate key in lookup range - DUPLICATE_KEY

- ID: `DUPLICATE_KEY-001`
- Location: `Budget!A17, Budget!A18`
- Fingerprint: `84717e216a3276ea`
- Detection: DET; confidence: Review
- Evidence: Normalized key 'north' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- Suggested fix: Make the keys unique or confirm the lookup is meant to return the first match.
- If intended, accept it in `.audit-ignore`: `DUPLICATE_KEY Budget!A17 fingerprint:84717e216a3276ea <reason>`

### [MEDIUM] Formula inputs include hidden structure - HIDDEN_STRUCTURE_IN_TOTAL

- ID: `HIDDEN_STRUCTURE_IN_TOTAL-001`
- Location: `Budget!B13`
- Fingerprint: `b2710237f13d9290`
- Detection: DET; confidence: Review
- Formula: `=B11+B12`
- Evidence: Hidden row 12 on Budget feeds 3 visible formula(s): Budget!B13, Budget!C13, Budget!D13.
- Suggested fix: Confirm hidden inputs are intentional and disclosed in visible workbook documentation.
- If intended, accept it in `.audit-ignore`: `HIDDEN_STRUCTURE_IN_TOTAL Budget!B13 fingerprint:b2710237f13d9290 <reason>`

### [MEDIUM] Text has leading or trailing whitespace - WHITESPACE_KEY

- ID: `WHITESPACE_KEY-001`
- Location: `Budget!A18`
- Fingerprint: `c4ab97484aa84198`
- Detection: DET; confidence: Review
- Evidence: Raw value is ' North '; the other text values in this column are not padded.
- Suggested fix: Trim the values if they are used as lookup keys or labels.
- If intended, accept it in `.audit-ignore`: `WHITESPACE_KEY Budget!A18 fingerprint:c4ab97484aa84198 <reason>`

## Suppressed Findings Summary

No suppressed findings.

## Recommended Next Steps

1. Start with the **Confirmed** section: every item there is a hard defect.
2. Walk the **Likely** section, comparing each flagged formula to its neighbors (drift findings include them inline).
3. Recalculate the workbook in Excel if value-dependent checks were skipped due to recalculation being unavailable.
4. Rerun the audit after fixes; keep suppressions only for intentional patterns with documented reasons.

## Non-Certification Disclaimer

This audit inspected formulas, ranges, workbook structure, hidden rows/columns/sheets, cached/recalculated values where available, and selected data-hygiene issues. It did not execute macros, validate external data sources, fully evaluate Power Query/Data Model objects, or certify business assumptions. Findings are defect candidates and likely errors, not a legal/accounting certification of correctness.
