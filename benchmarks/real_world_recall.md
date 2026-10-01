# Recall on the modified EUSES corpus

Generated 2026-10-01T03:54:08+00:00. A fault counts as found when a finding covers the faulty cell in the seeded workbook and not in the original.

- Faults evaluated: 695 in 695 workbooks (10 could not be audited)
- Found at the faulty cell: 537 (**recall 0.773**); found on the same row or column: 545
- Median findings per seeded workbook: 6; per original: 5 (noise baseline on real spreadsheets)

| Fault type | Meaning | Faults | Found at cell | Found on line | Any finding at cell (incl. pre-existing) |
|---|---|---:|---:|---:|---:|
| AOR | arithmetic operator replaced | 139 | 95 | 96 | 113 |
| CRP | constant replaced | 81 | 69 | 71 | 81 |
| CRR | constant replaced by reference | 131 | 124 | 125 | 131 |
| CRS | constant replaced by shift | 69 | 57 | 57 | 57 |
| FFR | function replaced | 93 | 58 | 59 | 60 |
| FRC | formula replaced by constant | 104 | 83 | 84 | 86 |
| RFR | reference replaced | 61 | 41 | 43 | 43 |
| ROR | relational operator replaced | 17 | 10 | 10 | 10 |

Rules that hit injected faults:

- FORMULA_DRIFT: 457
- LITERAL_CONSTANT: 261
- RANGE_EXCLUSION: 25
- RANGE_LENGTH_MISMATCH: 2
- LIVE_ERROR: 1
