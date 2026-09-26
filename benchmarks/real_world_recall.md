# Recall on the modified EUSES corpus

Generated 2026-09-26T03:57:58+00:00. A fault counts as found when a finding covers the faulty cell in the seeded workbook and not in the original.

- Faults evaluated: 695 in 695 workbooks (10 could not be audited)
- Found at the faulty cell: 528 (**recall 0.76**); found on the same row or column: 530
- Median findings per seeded workbook: 7; per original: 6 (noise baseline on real spreadsheets)

| Fault type | Meaning | Faults | Found at cell | Found on line | Any finding at cell (incl. pre-existing) |
|---|---|---:|---:|---:|---:|
| AOR | arithmetic operator replaced | 139 | 93 | 93 | 114 |
| CRP | constant replaced | 81 | 68 | 68 | 80 |
| CRR | constant replaced by reference | 131 | 123 | 122 | 130 |
| CRS | constant replaced by shift | 69 | 57 | 57 | 57 |
| FFR | function replaced | 93 | 56 | 57 | 59 |
| FRC | formula replaced by constant | 104 | 80 | 80 | 83 |
| RFR | reference replaced | 61 | 41 | 43 | 43 |
| ROR | relational operator replaced | 17 | 10 | 10 | 10 |

Rules that hit injected faults:

- FORMULA_DRIFT: 448
- LITERAL_CONSTANT: 254
- RANGE_EXCLUSION: 25
- RANGE_LENGTH_MISMATCH: 2
- BLANK_PRECEDENT: 1
- LIVE_ERROR: 1
