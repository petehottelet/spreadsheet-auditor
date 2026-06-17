# Report Template

Every audit report should contain these sections:

1. Executive summary.
2. Coverage and limitations.
3. Critical findings.
4. High findings.
5. Medium / Review findings.
6. Low / convention findings.
7. Suppressed findings summary.
8. Recommended next steps.
9. Non-certification disclaimer.

## Required Finding Shape

```text
[SEVERITY] Title - RULE_ID
Location:  Sheet!A1
Formula:   =SUM(A1:A10)
Evidence:  Why the cell was flagged.
Impact:    Known or likely downstream impact.
Detection: DET or HEUR; confidence: Defect, Likely defect, or Review.
Fix:       Concrete suggested fix or review step.
```

## Standing Coverage Language

```text
This audit inspected formulas, ranges, workbook structure, hidden rows/columns/sheets,
cached/recalculated values where available, and selected data-hygiene issues. It did
not execute macros, validate external data sources, fully evaluate Power Query/Data
Model objects, or certify business assumptions. Findings are defect candidates and
likely errors, not a legal/accounting certification of correctness.
```

## Tone

Be direct and evidence-led. Say "appears to" or "review" when intent is uncertain. Do not claim the workbook is certified correct.
