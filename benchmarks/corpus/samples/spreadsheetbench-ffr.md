# Finding cards: spreadsheetbench

Generated 2026-09-14T16:37:24+00:00 from benchmarks\corpus\results\spreadsheetbench-ffr with seed 7, up to 25 per rule and 2 per workbook.

Label each card in `labels/<source>.json` as `TP` (the auditor is right), `FP` (it is wrong), or `unsure`, with a one-line reason.

## BLANK_PRECEDENT

### `ada3dc9b0be1|BLANK_PRECEDENT|EXCELHELP!AF14`

- workbook: `all_data_912_v0.1/spreadsheet/39946/3_39946_input.xlsx`
- location: `EXCEL HELP!AF14`  severity: Medium  confidence: Review
- formula: `=G14-AE14`
- evidence: Referenced cell EXCEL HELP!G14 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: ["''", "''"]; column header: ''; used range: A1:AF23
- neighbourhood: AE12: '=SUM(K12:AD12)' -> 595.068493150685 | AF12: '=G12-AE12' -> 604.931506849315 | AE13: '=SUM(K13:AD13)' -> 1000 | AF13: '=G13-AE13' -> 0 | AE14: '=SUM(K14:AD14)' -> 0 | AF14: '=G14-AE14' -> 0 | AE15: '=SUM(K15:AD15)' -> 496.438356164383 | AF15: '=G15-AE15' -> 703.561643835617 | AE16: '=SUM(K16:AD16)' -> 1200 | AF16: '=G16-AE16' -> 0

### `5cd8c4fe9805|BLANK_PRECEDENT|DATA!R3|c76034`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!K3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 11 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 14 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 5 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -29

### `a3b766273873|BLANK_PRECEDENT|GLDetails!G7`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/3_601-4_input.xlsx`
- location: `GL Details!G7`  severity: Medium  confidence: Review
- formula: `=+E7-F7`
- evidence: Referenced cell GL Details!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: E5: 70 | G5: '=+E5-F5' -> None | E6: 70 | G6: '=+E6-F6' -> None | F7: 402.5 | G7: '=+E7-F7' -> None | E8: 1001 | G8: '=+E8-F8' -> None | E9: 28.07 | G9: '=+E9-F9' -> None

### `6afa97343321|BLANK_PRECEDENT|AHMED!E4`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/1_91-3_input.xlsx`
- location: `AHMED!E4`  severity: Medium  confidence: Review
- formula: `=E3+C4-D4`
- evidence: Referenced cell AHMED!D4 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH PR '"]; column header: ''; used range: A1:F12
- neighbourhood: D2: -10000 | E2: -10000 | D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None

### `3f7694b32e64|BLANK_PRECEDENT|2023!H7`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/1_68-47_input.xlsx`
- location: `2023!H7`  severity: Medium  confidence: Review
- formula: `=D7-E7+F7-G7`
- evidence: Referenced cell 2023!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -100000; row labels: ["'NAG/BP/22-20/2'", "'XXXXX'"]; column header: ''; used range: A1:N144
- neighbourhood: F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0 | H9: '=D9-E9+F9-G9' -> -87852.58 | I9: '=IF(C9="","",IF(COUNTIF(C9, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J9: '=((COUNTIF(H:H,H9)-COUNTIF(H:H,-H9))>=COUNTIF($H$7:H9,H9))*ISNUMBE... -> 0

### `f3f1d8b1312d|BLANK_PRECEDENT|denomination!E14`

- workbook: `all_data_912_v0.1/spreadsheet/3911/1_3911_input.xlsx`
- location: `denomination!E14`  severity: Medium  confidence: Review
- formula: `=+C14*D14`
- evidence: Referenced cell denomination!D14 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB22
- neighbourhood: C12: 'DENOMINATION' | D12: 'COUNT' | E12: 'AMOUNT' | C13: 1000 | D13: 87 | E13: '=+C13*D13' -> 87000 | C14: 500 | E14: '=+C14*D14' -> 0 | C15: 200 | D15: 11 | E15: '=+C15*D15' -> 2200 | C16: 100 | D16: 4 | E16: '=+C16*D16' -> 400

### `125be9ba2e04|BLANK_PRECEDENT|DATA!R3|c76034`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!K3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AM8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 11 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 14 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 5 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -29

### `5cd8c4fe9805|BLANK_PRECEDENT|DATA!R3|0eae78`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!P3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 11 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 14 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 5 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -29

### `125be9ba2e04|BLANK_PRECEDENT|DATA!R3|0eae78`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!P3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AM8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 11 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 14 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 5 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -29

### `95fdf876027b|BLANK_PRECEDENT|DATA!R3|0eae78`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!P3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 10 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 16 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 6 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -28.5

### `fdad7150c0c3|BLANK_PRECEDENT|2023!H6`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/2_68-47_input.xlsx`
- location: `2023!H6`  severity: Medium  confidence: Review
- formula: `=D6-E6+F6-G6`
- evidence: Referenced cell 2023!D6 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -66567.50000000745; row labels: []; column header: "'Variance'"; used range: A1:N144
- neighbourhood: F4: 'XYZ' | H4: 'Variance' | F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0

### `dd8e0d8d4758|BLANK_PRECEDENT|2023!H7`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/3_68-47_input.xlsx`
- location: `2023!H7`  severity: Medium  confidence: Review
- formula: `=D7-E7+F7-G7`
- evidence: Referenced cell 2023!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -100000; row labels: ["'NAG/BP/22-20/2'", "'XXXXX'"]; column header: ''; used range: A1:N144
- neighbourhood: F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0 | H9: '=D9-E9+F9-G9' -> -87852.58 | I9: '=IF(C9="","",IF(COUNTIF(C9, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J9: '=((COUNTIF(H:H,H9)-COUNTIF(H:H,-H9))>=COUNTIF($H$7:H9,H9))*ISNUMBE... -> 0

### `6afa97343321|BLANK_PRECEDENT|AHMED!E5`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/1_91-3_input.xlsx`
- location: `AHMED!E5`  severity: Medium  confidence: Review
- formula: `=E4+C5-D5`
- evidence: Referenced cell AHMED!D5 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'SALES'"]; column header: ''; used range: A1:F12
- neighbourhood: D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None

### `81a183f28e17|BLANK_PRECEDENT|EXCELHELP!AF14`

- workbook: `all_data_912_v0.1/spreadsheet/39946/2_39946_input.xlsx`
- location: `EXCEL HELP!AF14`  severity: Medium  confidence: Review
- formula: `=G14-AE14`
- evidence: Referenced cell EXCEL HELP!G14 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: ["''", "''"]; column header: ''; used range: A1:AF23
- neighbourhood: AE12: '=SUM(K12:AD12)' -> 595.068493150685 | AF12: '=G12-AE12' -> 604.931506849315 | AE13: '=SUM(K13:AD13)' -> 1000 | AF13: '=G13-AE13' -> 0 | AE14: '=SUM(K14:AD14)' -> 0 | AF14: '=G14-AE14' -> 0 | AE15: '=SUM(K15:AD15)' -> 496.438356164383 | AF15: '=G15-AE15' -> 703.561643835617 | AE16: '=SUM(K16:AD16)' -> 1200 | AF16: '=G16-AE16' -> 0

### `0233c00701a4|BLANK_PRECEDENT|AHMED!E5`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/3_91-3_input.xlsx`
- location: `AHMED!E5`  severity: Medium  confidence: Review
- formula: `=E4+C5-D5`
- evidence: Referenced cell AHMED!D5 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'SALES'"]; column header: ''; used range: A1:F12
- neighbourhood: D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None

### `95fdf876027b|BLANK_PRECEDENT|DATA!R3|c76034`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!K3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 10 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 16 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 6 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -28.5

### `0233c00701a4|BLANK_PRECEDENT|AHMED!E4`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/3_91-3_input.xlsx`
- location: `AHMED!E4`  severity: Medium  confidence: Review
- formula: `=E3+C4-D4`
- evidence: Referenced cell AHMED!D4 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH PR '"]; column header: ''; used range: A1:F12
- neighbourhood: D2: -10000 | E2: -10000 | D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None

### `dd8e0d8d4758|BLANK_PRECEDENT|2023!H6`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/3_68-47_input.xlsx`
- location: `2023!H6`  severity: Medium  confidence: Review
- formula: `=D6-E6+F6-G6`
- evidence: Referenced cell 2023!D6 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -66567.50000000745; row labels: []; column header: "'Variance'"; used range: A1:N144
- neighbourhood: F4: 'XYZ' | H4: 'Variance' | F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0

### `81a183f28e17|BLANK_PRECEDENT|EXCELHELP!AF11`

- workbook: `all_data_912_v0.1/spreadsheet/39946/2_39946_input.xlsx`
- location: `EXCEL HELP!AF11`  severity: Medium  confidence: Review
- formula: `=G11-AE11`
- evidence: Referenced cell EXCEL HELP!G11 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: ["''", "''"]; column header: ''; used range: A1:AF23
- neighbourhood: AE9: '=SUM(K9:AD9)' -> 142.072602739726 | AF9: '=G9-AE9' -> 144.427397260274 | AE10: '=SUM(K10:AD10)' -> 1665 | AF10: '=G10-AE10' -> -832.5 | AE11: '=SUM(K11:AD11)' -> 0 | AF11: '=G11-AE11' -> 0 | AE12: '=SUM(K12:AD12)' -> 595.068493150685 | AF12: '=G12-AE12' -> 604.931506849315 | AE13: '=SUM(K13:AD13)' -> 1000 | AF13: '=G13-AE13' -> 0

### `5989e352c77e|BLANK_PRECEDENT|AHMED!E4`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/2_91-3_input.xlsx`
- location: `AHMED!E4`  severity: Medium  confidence: Review
- formula: `=E3+C4-D4`
- evidence: Referenced cell AHMED!D4 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH PR '"]; column header: ''; used range: A1:F12
- neighbourhood: D2: -10000 | E2: -10000 | D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None

### `5989e352c77e|BLANK_PRECEDENT|AHMED!E5`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/2_91-3_input.xlsx`
- location: `AHMED!E5`  severity: Medium  confidence: Review
- formula: `=E4+C5-D5`
- evidence: Referenced cell AHMED!D5 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'SALES'"]; column header: ''; used range: A1:F12
- neighbourhood: D3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=D3+D7+D8' -> None | C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None

### `ab03f9015e49|BLANK_PRECEDENT|GLDetails!G7`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/2_601-4_input.xlsx`
- location: `GL Details!G7`  severity: Medium  confidence: Review
- formula: `=+E7-F7`
- evidence: Referenced cell GL Details!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: E5: 70 | G5: '=+E5-F5' -> None | E6: 70 | G6: '=+E6-F6' -> None | F7: 402.5 | G7: '=+E7-F7' -> None | E8: 1000 | G8: '=+E8-F8' -> None | E9: 28.07 | G9: '=+E9-F9' -> None

### `3f7694b32e64|BLANK_PRECEDENT|2023!H6`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/1_68-47_input.xlsx`
- location: `2023!H6`  severity: Medium  confidence: Review
- formula: `=D6-E6+F6-G6`
- evidence: Referenced cell 2023!D6 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -66567.50000000745; row labels: []; column header: "'Variance'"; used range: A1:N144
- neighbourhood: F4: 'XYZ' | H4: 'Variance' | F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0

### `c5f93923f23e|BLANK_PRECEDENT|GLDetails!G7`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/1_601-4_input.xlsx`
- location: `GL Details!G7`  severity: Medium  confidence: Review
- formula: `=+E7-F7`
- evidence: Referenced cell GL Details!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: E5: 70 | G5: '=+E5-F5' -> None | E6: 70 | G6: '=+E6-F6' -> None | F7: 402.5 | G7: '=+E7-F7' -> None | E8: 1000 | G8: '=+E8-F8' -> None | E9: 28.06 | G9: '=+E9-F9' -> None

### `fdad7150c0c3|BLANK_PRECEDENT|2023!H7`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/2_68-47_input.xlsx`
- location: `2023!H7`  severity: Medium  confidence: Review
- formula: `=D7-E7+F7-G7`
- evidence: Referenced cell 2023!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: -100000; row labels: ["'NAG/BP/22-20/2'", "'XXXXX'"]; column header: ''; used range: A1:N144
- neighbourhood: F5: 'Debit' | G5: 'Credit' | I5: 'Remarks' | G6: -40438868.37 | H6: '=D6-E6+F6-G6' -> -66567.50000000745 | G7: 212104 | H7: '=D7-E7+F7-G7' -> -100000 | I7: '=IF(C7="","",IF(COUNTIF(C7, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J7: '=((COUNTIF(H:H,H7)-COUNTIF(H:H,-H7))>=COUNTIF($H$7:H7,H7))*ISNUMBE... -> 0 | H8: '=D8-E8+F8-G8' -> 68129 | I8: '=IF(C8="","",IF(COUNTIF(C8, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J8: '=((COUNTIF(H:H,H8)-COUNTIF(H:H,-H8))>=COUNTIF($H$7:H8,H8))*ISNUMBE... -> 0 | H9: '=D9-E9+F9-G9' -> -87852.58 | I9: '=IF(C9="","",IF(COUNTIF(C9, "*AFS/FSTC"),"Corresponding Entry", IF... -> None | J9: '=((COUNTIF(H:H,H9)-COUNTIF(H:H,-H9))>=COUNTIF($H$7:H9,H9))*ISNUMBE... -> 0

## BROKEN_REFERENCE

### `3ccd5643c7a2|BROKEN_REFERENCE|Sheet1!B1`

- workbook: `all_data_912_v0.1/spreadsheet/56637/3_56637_input.xlsx`
- location: `Sheet1!B1`  severity: Low  confidence: Info
- formula: `=VLOOKUP(D1,'[1]Order Data'!$A:$B,2,FALSE)`
- evidence: 7 cell(s) on Sheet1 link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Sheet1!B1, Sheet1!C3, Sheet1!D3, Sheet1!E3, Sheet1!F3, Sheet1!G3, Sheet1!H3.
- cached value: 'Period 3/ Wk3'; row labels: ["'Period/Week'"]; column header: ''; used range: A1:Q110
- neighbourhood: A1: 'Period/Week' | B1: "=VLOOKUP(D1,'[1]Order Data'!$A:$B,2,FALSE)" -> 'Period 3/ Wk3' | C1: 'Week' | D1: 2021-04-11 00:00:00 | A2: 'DOW' | B2: 'Mon' | C2: 'Tue' | D2: 'Wed' | A3: 'Orders' | B3: 300.5398 | C3: "=VLOOKUP($B$1,'[1]Order Data'!$B:$J,4,FALSE)" -> 261.7022 | D3: "=VLOOKUP($B$1,'[1]Order Data'!$B:$J,5,FALSE)" -> 261.7022

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G12`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G12`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E10: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G10: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E11: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G11: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E12: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G12: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E13: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G13: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E14: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G14: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!D12`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D12`  severity: High  confidence: Defect
- formula: `=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY14/100),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: C10: '=IF(AND(B10>0,$AW12>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D10: '=IF(AND(B10>0,$AW12>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | F10: '=IF(AND(NOT(ISBLANK(E10)),B10>0,$AW12>0),IFERROR(E10/B10,""),"")' -> None | C11: '=IF(AND(B11>0,$AW13>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D11: '=IF(AND(B11>0,$AW13>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | F11: '=IF(AND(NOT(ISBLANK(E11)),B11>0,$AW13>0),IFERROR(E11/B11,""),"")' -> None | C12: '=IF(AND(B12>0,$AW14>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D12: '=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | F12: '=IF(AND(NOT(ISBLANK(E12)),B12>0,$AW14>0),IFERROR(E12/B12,""),"")' -> None | C13: '=IF(AND(B13>0,$AW15>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A15,$BD$4:$B... -> None | D13: '=IF(AND(B13>0,$AW15>0),IFERROR(_xlfn.XLOOKUP($A15,$BD$4:$BD$82,$BF... -> None | F13: '=IF(AND(NOT(ISBLANK(E13)),B13>0,$AW15>0),IFERROR(E13/B13,""),"")' -> None | B14: '=IF(IFERROR(INDEX(\'[1]UPS & Billing Data\'!$B$3:$BL$81,MATCH($A16... -> None | C14: '=IF(AND(B14>0,$AW16>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A16,$BD$4:$B... -> None | D14: '=IF(AND(B14>0,$AW16>0),IFERROR(_xlfn.XLOOKUP($A16,$BD$4:$BD$82,$BF... -> None | F14: '=IF(AND(NOT(ISBLANK(E14)),B14>0,$AW16>0),IFERROR(E14/B14,""),"")' -> None

### `b230bc5037bf|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A27`

- workbook: `all_data_912_v0.1/spreadsheet/47699/3_47699_input.xlsx`
- location: `Prev working day Quote (2)!A27`  severity: High  confidence: Defect
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7 | A27: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B27: 'Oscar' | C27: 7

### `8734ff2c3db4|BROKEN_REFERENCE|Sheet1!C14`

- workbook: `all_data_912_v0.1/spreadsheet/50631/1_50631_input.xlsx`
- location: `Sheet1!C14`  severity: High  confidence: Defect
- formula: `=IFERROR(INDEX(#REF!,MATCH(B14,#REF!,0)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: B12: '=IF($B$3+ROWS($B$7:$B12)-1<=$F$3,$B$3+ROWS($B$7:$B12)-1,"")' -> 2021-09-06 00:00:00 | C12: '=IFERROR(INDEX(#REF!,MATCH(B12,#REF!,0)),"")' -> None | D12: '=IF($B$3+ROWS($B$7:$D43)-1<=$F$3,$B$3+ROWS($B$7:$D43)-1,"")' -> 2021-10-07 00:00:00 | B13: '=IF($B$3+ROWS($B$7:$B13)-1<=$F$3,$B$3+ROWS($B$7:$B13)-1,"")' -> 2021-09-07 00:00:00 | C13: '=IFERROR(INDEX(#REF!,MATCH(B13,#REF!,0)),"")' -> None | D13: '=IF($B$3+ROWS($B$7:$D44)-1<=$F$3,$B$3+ROWS($B$7:$D44)-1,"")' -> 2021-10-08 00:00:00 | B14: '=IF($B$3+ROWS($B$7:$B14)-1<=$F$3,$B$3+ROWS($B$7:$B14)-1,"")' -> 2021-09-08 00:00:00 | C14: '=IFERROR(INDEX(#REF!,MATCH(B14,#REF!,0)),"")' -> None | D14: '=IF($B$3+ROWS($B$7:$D45)-1<=$F$3,$B$3+ROWS($B$7:$D45)-1,"")' -> 2021-10-09 00:00:00 | B15: '=IF($B$3+ROWS($B$7:$B15)-1<=$F$3,$B$3+ROWS($B$7:$B15)-1,"")' -> 2021-09-09 00:00:00 | C15: '=IFERROR(INDEX(#REF!,MATCH(B15,#REF!,0)),"")' -> None | D15: '=IF($B$3+ROWS($B$7:$D46)-1<=$F$3,$B$3+ROWS($B$7:$D46)-1,"")' -> 2021-10-10 00:00:00 | B16: '=IF($B$3+ROWS($B$7:$B16)-1<=$F$3,$B$3+ROWS($B$7:$B16)-1,"")' -> 2021-09-10 00:00:00 | C16: '=IFERROR(INDEX(#REF!,MATCH(B16,#REF!,0)),"")' -> None | D16: '=IF($B$3+ROWS($B$7:$D47)-1<=$F$3,$B$3+ROWS($B$7:$D47)-1,"")' -> 2021-10-11 00:00:00

### `2069bdc39cd5|BROKEN_REFERENCE|Result!J1`

- workbook: `all_data_912_v0.1/spreadsheet/55085/1_55085_input.xlsx`
- location: `Result!J1`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:L13
- neighbourhood: J1: '=#REF!' -> '#REF!' | K1: '=J1' -> '#REF!' | L1: '=#REF!' -> '#REF!' | H2: 'Mango' | I2: 'Banana' | J2: 'Apple' | K2: 'Mango' | L2: 'Banana' | H3: '=G3' -> 'Shrawan' | I3: '=H3' -> 'Shrawan' | J3: 'Bhadra' | K3: '=J3' -> 'Bhadra' | L3: '=K3' -> 'Bhadra'

### `b230bc5037bf|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A24|c4cae6`

- workbook: `all_data_912_v0.1/spreadsheet/47699/3_47699_input.xlsx`
- location: `Prev working day Quote (2)!A24`  severity: Low  confidence: Info
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: 4 cell(s) on Prev working day Quote (2) link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Prev working day Quote (2)!A24, Prev working day Quote (2)!A25, Prev working day Quote (2)!A26, Prev working day Quote (2)!A27.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A22: False | B22: 'Oscar' | C22: 7 | A23: True | B23: 'Oscar' | C23: 7 | A24: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B24: 'Oscar' | C24: 7 | A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7

### `acb548947286|BROKEN_REFERENCE|Statistics!G31`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G31`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E29: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G29: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E30: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G30: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E31: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G31: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E32: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G32: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E33: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G33: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!B14|521f6a`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!B14`  severity: Low  confidence: Info
- formula: `=IF(IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),"")=0,"",IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),""))`
- evidence: 1 cell(s) on Sheet1 link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Sheet1!B14.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: A12: 2023-12-11 00:00:00 | C12: '=IF(AND(B12>0,$AW14>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D12: '=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A13: 2023-12-18 00:00:00 | C13: '=IF(AND(B13>0,$AW15>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A15,$BD$4:$B... -> None | D13: '=IF(AND(B13>0,$AW15>0),IFERROR(_xlfn.XLOOKUP($A15,$BD$4:$BD$82,$BF... -> None | A14: 2023-12-25 00:00:00 | B14: '=IF(IFERROR(INDEX(\'[1]UPS & Billing Data\'!$B$3:$BL$81,MATCH($A16... -> None | C14: '=IF(AND(B14>0,$AW16>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A16,$BD$4:$B... -> None | D14: '=IF(AND(B14>0,$AW16>0),IFERROR(_xlfn.XLOOKUP($A16,$BD$4:$BD$82,$BF... -> None

### `acb548947286|BROKEN_REFERENCE|Statistics!G55`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G55`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E53: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G53: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E54: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G54: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E55: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G55: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E56: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G56: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E57: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G57: "=COUNTIF('WK1'!B22:B2020,Statistics!$A$3)" -> 0

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G49`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G49`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G47: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G48: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E49: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G49: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E50: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G50: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E51: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G51: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `5d8557dfb652|BROKEN_REFERENCE|July-KPIs!B13`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!B13`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A13),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A11: '=IF(ROWS(A$6:A11)>DAY(J$13),"",J$12+ROWS(A$6:A11)-1)' -> 2021-07-09 00:00:00 | B11: '=IFERROR(VLOOKUP(($C$1&"|"&A11),#REF!,2,0),"")' -> None | A12: '=IF(ROWS(A$6:A12)>DAY(J$13),"",J$12+ROWS(A$6:A12)-1)' -> 2021-07-10 00:00:00 | B12: '=IFERROR(VLOOKUP(($C$1&"|"&A12),#REF!,2,0),"")' -> None | A13: '=IF(ROWS(A$6:A13)>DAY(J$13),"",J$12+ROWS(A$6:A13)-1)' -> 2021-07-11 00:00:00 | B13: '=IFERROR(VLOOKUP(($C$1&"|"&A13),#REF!,2,0),"")' -> None | A14: '=IF(ROWS(A$6:A14)>DAY(J$13),"",J$12+ROWS(A$6:A14)-1)' -> 2021-07-12 00:00:00 | B14: '=IFERROR(VLOOKUP(($C$1&"|"&A14),#REF!,2,0),"")' -> None | A15: '=IF(ROWS(A$6:A15)>DAY(J$13),"",J$12+ROWS(A$6:A15)-1)' -> 2021-07-13 00:00:00 | B15: '=IFERROR(VLOOKUP(($C$1&"|"&A15),#REF!,2,0),"")' -> None

### `74d967658eee|BROKEN_REFERENCE|Sheet1!AN53`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!AN53`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:21)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: AN51: '=IFERROR(LARGE(#REF!,ROWS($1:19)),"")' -> None | AN52: '=IFERROR(LARGE(#REF!,ROWS($1:20)),"")' -> None | AN53: '=IFERROR(LARGE(#REF!,ROWS($1:21)),"")' -> None | AN54: '=IFERROR(LARGE(#REF!,ROWS($1:22)),"")' -> None | AN55: '=IFERROR(LARGE(#REF!,ROWS($1:23)),"")' -> None

### `7bd972dd1e37|BROKEN_REFERENCE|July-KPIs!B25`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!B25`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A25),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A23: '=IF(ROWS(A$6:A23)>DAY(J$13),"",J$12+ROWS(A$6:A23)-1)' -> 2021-07-19 00:00:00 | B23: '=IFERROR(VLOOKUP(($C$1&"|"&A23),#REF!,2,0),"")' -> None | A24: '=IF(ROWS(A$6:A24)>DAY(J$13),"",J$12+ROWS(A$6:A24)-1)' -> 2021-07-20 00:00:00 | B24: '=IFERROR(VLOOKUP(($C$1&"|"&A24),#REF!,2,0),"")' -> None | A25: '=IF(ROWS(A$6:A25)>DAY(J$13),"",J$12+ROWS(A$6:A25)-1)' -> 2021-07-21 00:00:00 | B25: '=IFERROR(VLOOKUP(($C$1&"|"&A25),#REF!,2,0),"")' -> None | A26: '=IF(ROWS(A$6:A26)>DAY(J$13),"",J$12+ROWS(A$6:A26)-1)' -> 2021-07-22 00:00:00 | B26: '=IFERROR(VLOOKUP(($C$1&"|"&A26),#REF!,2,0),"")' -> None | A27: '=IF(ROWS(A$6:A27)>DAY(J$13),"",J$12+ROWS(A$6:A27)-1)' -> 2021-07-23 00:00:00 | B27: '=IFERROR(VLOOKUP(($C$1&"|"&A27),#REF!,2,0),"")' -> None

### `1ee00a60f590|BROKEN_REFERENCE|Sheet1!AN63`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!AN63`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:31)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: AN61: '=IFERROR(LARGE(#REF!,ROWS($1:29)),"")' -> None | AN62: '=IFERROR(LARGE(#REF!,ROWS($1:30)),"")' -> None | AN63: '=IFERROR(LARGE(#REF!,ROWS($1:31)),"")' -> None | AN64: '=IFERROR(LARGE(#REF!,ROWS($1:32)),"")' -> None

### `358921c3a973|BROKEN_REFERENCE|Sheet1!K6`

- workbook: `all_data_912_v0.1/spreadsheet/48685/2_48685_input.xlsx`
- location: `Sheet1!K6`  severity: High  confidence: Defect
- formula: `=IF(E6="","",E6+#REF!)`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:K12
- neighbourhood: K4: '=IF(E4="","",E4+K1)' -> 4:22:46 | I5: 426 | J5: 0 | K5: '=IF(E5="","",E5+K3)' -> None | K6: '=IF(E6="","",E6+#REF!)' -> None | K7: '=IF(E7="","",E7+K4)' -> 6:57:46 | I8: 62 | J8: 2610 | K8: '=IF(E8="","",E8+K5)' -> None

### `552f4c55b2df|BROKEN_REFERENCE|OrderSheetFinal!E6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!E6`  severity: Low  confidence: Info
- formula: `=IFERROR(VLOOKUP(B6,[1]P1!$B$55:$K$62,10,FALSE),0)`
- evidence: 1119 cell(s) on Order Sheet Final link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Order Sheet Final!E6, Order Sheet Final!G6, Order Sheet Final!H6, Order Sheet Final!I6, Order Sheet Final!J6, Order Sheet Final!K6, Order Sheet Final!L6, Order Sheet Final!M6, ....
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'P1'"; used range: A1:AS37
- neighbourhood: E4: '=SUM(E6:E33)' -> 0 | F4: '=SUM(F6:F33)' -> 12 | G4: '=SUM(G6:G33)' -> 0 | C5: 'Stock Description' | D5: 'Location' | E5: 'P1' | F5: 'P2' | G5: 'P3.1' | C6: '600mm Cantilever Arm Slotted' | D6: 'N2' | E6: '=IFERROR(VLOOKUP(B6,[1]P1!$B$55:$K$62,10,FALSE),0)' -> 0 | F6: 3 | G6: "=IFERROR(VLOOKUP(B6,'[1]P3.1'!$B$59:$K$71,10,FALSE),0)" -> 0 | C7: 'M10 Square Washers' | D7: 'P1' | E7: '=IFERROR(VLOOKUP(B7,[1]P1!$B$55:$K$62,10,FALSE),0)' -> 0 | F7: '=IFERROR(VLOOKUP(B7,[1]P2!$B$55:$K$65,10,FALSE),0)' -> 0 | G7: "=IFERROR(VLOOKUP(B7,'[1]P3.1'!$B$59:$K$71,10,FALSE),0)" -> 0 | C8: 'M-Series Pipe Clamp 100mm' | D8: 'N5' | E8: '=IFERROR(VLOOKUP(B8,[1]P1!$B$55:$K$62,10,FALSE),0)' -> 0 | F8: '=IFERROR(VLOOKUP(B8,[1]P2!$B$55:$K$65,10,FALSE),0)' -> 0 | G8: "=IFERROR(VLOOKUP(B8,'[1]P3.1'!$B$59:$K$71,10,FALSE),0)" -> 0

### `5d8557dfb652|BROKEN_REFERENCE|July-KPIs!B26`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!B26`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A26),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A24: '=IF(ROWS(A$6:A24)>DAY(J$13),"",J$12+ROWS(A$6:A24)-1)' -> None | B24: '=IFERROR(VLOOKUP(($C$1&"|"&A24),#REF!,2,0),"")' -> None | A25: '=IF(ROWS(A$6:A25)>DAY(J$13),"",J$12+ROWS(A$6:A25)-1)' -> None | B25: '=IFERROR(VLOOKUP(($C$1&"|"&A25),#REF!,2,0),"")' -> None | A26: '=IF(ROWS(A$6:A26)>DAY(J$13),"",J$12+ROWS(A$6:A26)-1)' -> None | B26: '=IFERROR(VLOOKUP(($C$1&"|"&A26),#REF!,2,0),"")' -> None | A27: '=IF(ROWS(A$6:A27)>DAY(J$13),"",J$12+ROWS(A$6:A27)-1)' -> None | B27: '=IFERROR(VLOOKUP(($C$1&"|"&A27),#REF!,2,0),"")' -> None | A28: '=IF(ROWS(A$6:A28)>DAY(J$13),"",J$12+ROWS(A$6:A28)-1)' -> None | B28: '=IFERROR(VLOOKUP(($C$1&"|"&A28),#REF!,2,0),"")' -> None

### `6d5548493a93|BROKEN_REFERENCE|July-KPIs!B24`

- workbook: `all_data_912_v0.1/spreadsheet/1726/1_1726_input.xlsx`
- location: `July-KPIs!B24`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A24),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A22: '=IF(ROWS(A$6:A22)>DAY(J$13),"",J$12+ROWS(A$6:A22)-1)' -> 2024-07-26 00:00:00 | B22: '=IFERROR(VLOOKUP(($C$1&"|"&A22),#REF!,2,0),"")' -> None | A23: '=IF(ROWS(A$6:A23)>DAY(J$13),"",J$12+ROWS(A$6:A23)-1)' -> 2024-07-27 00:00:00 | B23: '=IFERROR(VLOOKUP(($C$1&"|"&A23),#REF!,2,0),"")' -> None | A24: '=IF(ROWS(A$6:A24)>DAY(J$13),"",J$12+ROWS(A$6:A24)-1)' -> 2024-07-28 00:00:00 | B24: '=IFERROR(VLOOKUP(($C$1&"|"&A24),#REF!,2,0),"")' -> None | A25: '=IF(ROWS(A$6:A25)>DAY(J$13),"",J$12+ROWS(A$6:A25)-1)' -> 2024-07-29 00:00:00 | B25: '=IFERROR(VLOOKUP(($C$1&"|"&A25),#REF!,2,0),"")' -> None | A26: '=IF(ROWS(A$6:A26)>DAY(J$13),"",J$12+ROWS(A$6:A26)-1)' -> 2024-07-30 00:00:00 | B26: '=IFERROR(VLOOKUP(($C$1&"|"&A26),#REF!,2,0),"")' -> None

### `26752d8b4632|BROKEN_REFERENCE|Sheet1!B13`

- workbook: `all_data_912_v0.1/spreadsheet/49237/3_49237_input.xlsx`
- location: `Sheet1!B13`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: ["'Letter Dates'"]; column header: "'Joe George Veteran\\n8675309 Lane NE\\nJenny, MN 12345'"; used range: A1:L27
- neighbourhood: A11: 'Letter Name' | A12: 'VBMS-A Remarks' | A13: 'Letter Dates' | B13: '=#REF!' -> '#REF!' | A14: 'Letter Dates' | A15: 'Calculator Name'

### `4717419de1d0|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A25`

- workbook: `all_data_912_v0.1/spreadsheet/47699/2_47699_input.xlsx`
- location: `Prev working day Quote (2)!A25`  severity: High  confidence: Defect
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A23: True | B23: 'Oscar' | C23: 7 | A24: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B24: 'Oscar' | C24: 7 | A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7 | A27: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B27: 'Oscar' | C27: 7

### `4717419de1d0|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A26`

- workbook: `all_data_912_v0.1/spreadsheet/47699/2_47699_input.xlsx`
- location: `Prev working day Quote (2)!A26`  severity: High  confidence: Defect
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A24: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B24: 'Oscar' | C24: 7 | A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7 | A27: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B27: 'Oscar' | C27: 7

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G19`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G19`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E17: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G17: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E18: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G18: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E19: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G19: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E20: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G20: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E21: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G21: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `fccec3fdfd0f|BROKEN_REFERENCE|Streets!G3`

- workbook: `all_data_912_v0.1/spreadsheet/13284/3_13284_input.xlsx`
- location: `Streets!G3`  severity: Low  confidence: Info
- formula: `=IFERROR(VLOOKUP(E3,[1]Assistente!R6:S23,2,0)," ")`
- evidence: 2 cell(s) on Streets link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Streets!G3, Streets!G4.
- cached value: ' '; row labels: ["'Avenida Braz De Pina'", "'Mario'"]; column header: "'Observação'"; used range: A1:G26
- neighbourhood: E1: 'Área' | F1: 'Assistente' | G1: 'Observação' | F2: 'Paulo Mauricio' | F3: 'Mario' | G3: '=IFERROR(VLOOKUP(E3,[1]Assistente!R6:S23,2,0)," ")' -> ' ' | F4: 'Celia' | G4: '=IFERROR(VLOOKUP(E4,[1]Assistente!R7:S24,2,0)," ")' -> ' ' | F5: 'Sonia'

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G39`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G39`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G37: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G38: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E39: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G39: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G40: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G41: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

## CIRCULAR_REFERENCE

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F21`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F21`  severity: High  confidence: Likely defect
- evidence: Test!F21 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,2,0),"")' -> None | E19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,3,0),"")' -> None | F19: '=IF(OR(B19="PRG/FLY",B19="PRG/TVL",B19="FLY1",B19="TVL1",B19="PRG/... -> None | G19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,5,0),"")' -> None | D20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,2,0),"")' -> None | E20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,3,0),"")' -> None | F20: '=IF(OR(B20="PRG/FLY",B20="PRG/TVL",B20="FLY1",B20="TVL1",B20="PRG/... -> None | G20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,5,0),"")' -> None | D21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,2,0),"")' -> None | E21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,3,0),"")' -> None | F21: '=IF(OR(B21="PRG/FLY",B21="PRG/TVL",B21="FLY1",B21="TVL1",B21="PRG/... -> None | G21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,5,0),"")' -> None | D22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,2,0),"")' -> None | E22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,3,0),"")' -> None | F22: '=IF(OR(B22="PRG/FLY",B22="PRG/TVL",B22="FLY1",B22="TVL1",B22="PRG/... -> None | G22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,5,0),"")' -> None | D23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,2,0),"")' -> None | E23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,3,0),"")' -> None | F23: '=IF(OR(B23="PRG/FLY",B23="PRG/TVL",B23="FLY1",B23="TVL1",B23="PRG/... -> None | G23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,5,0),"")' -> None

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F11`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F11`  severity: High  confidence: Likely defect
- evidence: Test!F11 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,2,0),"")' -> None | E9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,3,0),"")' -> None | F9: '=IF(OR(B9="PRG/FLY",B9="PRG/TVL",B9="FLY1",B9="TVL1",B9="PRG/FLY-C... -> None | G9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,5,0),"")' -> None | D10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,2,0),"")' -> None | E10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,3,0),"")' -> None | F10: '=IF(OR(B10="PRG/FLY",B10="PRG/TVL",B10="FLY1",B10="TVL1",B10="PRG/... -> None | G10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,5,0),"")' -> None | D11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,2,0),"")' -> None | E11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,3,0),"")' -> None | F11: '=IF(OR(B11="PRG/FLY",B11="PRG/TVL",B11="FLY1",B11="TVL1",B11="PRG/... -> None | G11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,5,0),"")' -> None | D12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,2,0),"")' -> None | E12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,3,0),"")' -> None | F12: '=IF(OR(B12="PRG/FLY",B12="PRG/TVL",B12="FLY1",B12="TVL1",B12="PRG/... -> None | G12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,5,0),"")' -> None | D13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,2,0),"")' -> None | E13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,3,0),"")' -> None | F13: '=IF(OR(B13="PRG/FLY",B13="PRG/TVL",B13="FLY1",B13="TVL1",B13="PRG/... -> None | G13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,5,0),"")' -> None

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F21`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F21`  severity: High  confidence: Likely defect
- evidence: Test!F21 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,2,0),"")' -> None | E19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,3,0),"")' -> None | F19: '=IF(OR(B19="PRG/FLY",B19="PRG/TVL",B19="FLY1",B19="TVL1",B19="PRG/... -> None | G19: '=IFERROR(VLOOKUP(C19,DATA!$A:$E,5,0),"")' -> None | D20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,2,0),"")' -> None | E20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,3,0),"")' -> None | F20: '=IF(OR(B20="PRG/FLY",B20="PRG/TVL",B20="FLY1",B20="TVL1",B20="PRG/... -> None | G20: '=IFERROR(VLOOKUP(C20,DATA!$A:$E,5,0),"")' -> None | D21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,2,0),"")' -> None | E21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,3,0),"")' -> None | F21: '=IF(OR(B21="PRG/FLY",B21="PRG/TVL",B21="FLY1",B21="TVL1",B21="PRG/... -> None | G21: '=IFERROR(VLOOKUP(C21,DATA!$A:$E,5,0),"")' -> None | D22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,2,0),"")' -> None | E22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,3,0),"")' -> None | F22: '=IF(OR(B22="PRG/FLY",B22="PRG/TVL",B22="FLY1",B22="TVL1",B22="PRG/... -> None | G22: '=IFERROR(VLOOKUP(C22,DATA!$A:$E,5,0),"")' -> None | D23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,2,0),"")' -> None | E23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,3,0),"")' -> None | F23: '=IF(OR(B23="PRG/FLY",B23="PRG/TVL",B23="FLY1",B23="TVL1",B23="PRG/... -> None | G23: '=IFERROR(VLOOKUP(C23,DATA!$A:$E,5,0),"")' -> None

### `92f8bf691072|CIRCULAR_REFERENCE|Test!F48`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F48`  severity: High  confidence: Likely defect
- evidence: Test!F48 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,2,0),"")' -> None | E46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,3,0),"")' -> None | F46: '=IF(OR(B46="PRG/FLY",B46="PRG/TVL",B46="FLY1",B46="TVL1",B46="PRG/... -> None | G46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,5,0),"")' -> None | D47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,2,0),"")' -> None | E47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,3,0),"")' -> None | F47: '=IF(OR(B47="PRG/FLY",B47="PRG/TVL",B47="FLY1",B47="TVL1",B47="PRG/... -> None | G47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,5,0),"")' -> None | D48: '=IFERROR(VLOOKUP(C48,DATA!$A:$E,2,0),"")' -> None | E48: '=IFERROR(VLOOKUP(C48,DATA!$A:$E,3,0),"")' -> None | F48: '=IF(OR(B48="PRG/FLY",B48="PRG/TVL",B48="FLY1",B48="TVL1",B48="PRG/... -> None | G48: '=IFERROR(VLOOKUP(C48,DATA!$A:$E,5,0),"")' -> None | D49: '=IFERROR(VLOOKUP(C49,DATA!$A:$E,2,0),"")' -> None | E49: '=IFERROR(VLOOKUP(C49,DATA!$A:$E,3,0),"")' -> None | F49: '=IF(OR(B49="PRG/FLY",B49="PRG/TVL",B49="FLY1",B49="TVL1",B49="PRG/... -> None | G49: '=IFERROR(VLOOKUP(C49,DATA!$A:$E,5,0),"")' -> None | D50: '=IFERROR(VLOOKUP(C50,DATA!$A:$E,2,0),"")' -> None | E50: '=IFERROR(VLOOKUP(C50,DATA!$A:$E,3,0),"")' -> None | F50: '=IF(OR(B50="PRG/FLY",B50="PRG/TVL",B50="FLY1",B50="TVL1",B50="PRG/... -> None | G50: '=IFERROR(VLOOKUP(C50,DATA!$A:$E,5,0),"")' -> None

### `92f8bf691072|CIRCULAR_REFERENCE|Test!F37`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F37`  severity: High  confidence: Likely defect
- evidence: Test!F37 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,2,0),"")' -> None | E35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,3,0),"")' -> None | F35: '=IF(OR(B35="PRG/FLY",B35="PRG/TVL",B35="FLY1",B35="TVL1",B35="PRG/... -> None | G35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,5,0),"")' -> None | D36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,2,0),"")' -> None | E36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,3,0),"")' -> None | F36: '=IF(OR(B36="PRG/FLY",B36="PRG/TVL",B36="FLY1",B36="TVL1",B36="PRG/... -> None | G36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,5,0),"")' -> None | D37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,2,0),"")' -> None | E37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,3,0),"")' -> None | F37: '=IF(OR(B37="PRG/FLY",B37="PRG/TVL",B37="FLY1",B37="TVL1",B37="PRG/... -> None | G37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,5,0),"")' -> None | D38: '=IFERROR(VLOOKUP(C38,DATA!$A:$E,2,0),"")' -> None | E38: '=IFERROR(VLOOKUP(C38,DATA!$A:$E,3,0),"")' -> None | F38: '=IF(OR(B38="PRG/FLY",B38="PRG/TVL",B38="FLY1",B38="TVL1",B38="PRG/... -> None | G38: '=IFERROR(VLOOKUP(C38,DATA!$A:$E,5,0),"")' -> None | D39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,2,0),"")' -> None | E39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,3,0),"")' -> None | F39: '=IF(OR(B39="PRG/FLY",B39="PRG/TVL",B39="FLY1",B39="TVL1",B39="PRG/... -> None | G39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,5,0),"")' -> None

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F45`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F45`  severity: High  confidence: Likely defect
- evidence: Test!F45 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,2,0),"")' -> None | E43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,3,0),"")' -> None | F43: '=IF(OR(B43="PRG/FLY",B43="PRG/TVL",B43="FLY1",B43="TVL1",B43="PRG/... -> None | G43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,5,0),"")' -> None | D44: '=IFERROR(VLOOKUP(C44,DATA!$A:$E,2,0),"")' -> None | E44: '=IFERROR(VLOOKUP(C44,DATA!$A:$E,3,0),"")' -> None | F44: '=IF(OR(B44="PRG/FLY",B44="PRG/TVL",B44="FLY1",B44="TVL1",B44="PRG/... -> None | G44: '=IFERROR(VLOOKUP(C44,DATA!$A:$E,5,0),"")' -> None | D45: '=IFERROR(VLOOKUP(C45,DATA!$A:$E,2,0),"")' -> None | E45: '=IFERROR(VLOOKUP(C45,DATA!$A:$E,3,0),"")' -> None | F45: '=IF(OR(B45="PRG/FLY",B45="PRG/TVL",B45="FLY1",B45="TVL1",B45="PRG/... -> None | G45: '=IFERROR(VLOOKUP(C45,DATA!$A:$E,5,0),"")' -> None | D46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,2,0),"")' -> None | E46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,3,0),"")' -> None | F46: '=IF(OR(B46="PRG/FLY",B46="PRG/TVL",B46="FLY1",B46="TVL1",B46="PRG/... -> None | G46: '=IFERROR(VLOOKUP(C46,DATA!$A:$E,5,0),"")' -> None | D47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,2,0),"")' -> None | E47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,3,0),"")' -> None | F47: '=IF(OR(B47="PRG/FLY",B47="PRG/TVL",B47="FLY1",B47="TVL1",B47="PRG/... -> None | G47: '=IFERROR(VLOOKUP(C47,DATA!$A:$E,5,0),"")' -> None

### `21bdc0943b23|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/1_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `70a7680e9819|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/3_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `0a3eeb22d16c|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/2_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

## DUPLICATE_KEY

### `1c06477fced9|DUPLICATE_KEY|URNlookup!K530,URNlookup!K532`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `URN lookup!K530, URN lookup!K532`  severity: Medium  confidence: Review
- evidence: Normalized key 'bb12 0jd' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'BB12 0JD'; row labels: ["'Wellfield Drive'", "'Burnley'"]; column header: "'BB11 4RB'"; used range: A1:X1461
- neighbourhood: J528: 'Burnley' | K528: 'BB10 2NH' | L528: 'Open' | J529: 'Burnley' | K529: 'BB11 4RB' | L529: 'Open' | J530: 'Burnley' | K530: 'BB12 0JD' | L530: 'Open' | J531: 'Burnley' | K531: 'BB12 6HZ' | L531: 'Closed' | J532: 'Burnley' | K532: 'BB12 0JD' | L532: 'Open'

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A311,RS.Food!A312`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A311, RS.Food!A312`  severity: Medium  confidence: Review
- evidence: Normalized key 'berries' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Berries'; row labels: []; column header: "'Beef'"; used range: A1:W607
- neighbourhood: A309: 'Banana' | B309: 0 | C309: 0 | A310: 'Beef' | B310: 0 | C310: 0 | A311: 'Berries' | B311: 0 | C311: 0 | A312: 'Berries' | B312: 0 | C312: 0 | A313: 'Black Pudding' | B313: 0 | C313: 0

### `3211215352e9|DUPLICATE_KEY|Grouping!A4,Grouping!A6`

- workbook: `all_data_912_v0.1/spreadsheet/7902/2_7902_input.xlsx`
- location: `Grouping!A4, Grouping!A6`  severity: Medium  confidence: Review
- evidence: Normalized key 'group c' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Group C'; row labels: []; column header: "'Group B'"; used range: A1:I7
- neighbourhood: A2: 'Group A' | C2: 0.1 | A3: 'Group B' | C3: 0.1 | A4: 'Group C' | C4: 0.05 | A5: 'Group B' | B5: 'Material X' | C5: 0.12 | A6: 'Group C' | B6: 'Material Y' | C6: 0.05

### `21865bab73e8|DUPLICATE_KEY|RS.Food!A447,RS.Food!A448`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!A447, RS.Food!A448`  severity: Medium  confidence: Review
- evidence: Normalized key 'sourdough' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Sourdough'; row labels: []; column header: "'Soft'"; used range: A1:W607
- neighbourhood: A445: 'Soft' | B445: 0 | C445: 0 | A446: 'Soft' | B446: 0 | C446: 0 | A447: 'Sourdough' | B447: 0 | C447: 0 | A448: 'Sourdough' | B448: 0 | C448: 0 | A449: 'Soya Milk' | B449: 0 | C449: 0

### `d49eeac3b8af|DUPLICATE_KEY|Sheet1!B12,Sheet1!B15,Sheet1!B16,Sheet1!B18,Sheet1!B19`

- workbook: `all_data_912_v0.1/spreadsheet/59902/2_59902_input.xlsx`
- location: `Sheet1!B12, Sheet1!B15, Sheet1!B16, Sheet1!B18, Sheet1!B19`  severity: Medium  confidence: Review
- evidence: Normalized key 'donald' appears 9 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Donald'; row labels: []; column header: "'Bob'"; used range: A1:H28
- neighbourhood: A10: 2008-08-31 00:00:00 | B10: 'Bob' | C10: '=A10-INDEX($A$4:$A9,MATCH(B10,$B$4:$B9,0),1)' -> 2 | A11: 2008-08-31 00:00:00 | B11: 'Bob' | C11: '=A11-INDEX($A$4:$A10,MATCH(B11,$B$4:$B10,0),1)' -> 2 | A12: 2008-08-31 00:00:00 | B12: 'Donald' | C12: '=A12-INDEX($A$4:$A11,MATCH(B12,$B$4:$B11,0),1)' -> '#N/A' | A13: 2008-09-12 00:00:00 | B13: 'Jane' | C13: '=A13-INDEX($A$4:$A12,MATCH(B13,$B$4:$B12,0),1)' -> 14 | A14: 2008-09-12 00:00:00 | B14: 'Bob' | C14: '=A14-INDEX($A$4:$A13,MATCH(B14,$B$4:$B13,0),1)' -> 14

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A463,RS.Food!A464`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A463, RS.Food!A464`  severity: Medium  confidence: Review
- evidence: Normalized key 'tomatoes' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Tomatoes'; row labels: []; column header: "'Tomato'"; used range: A1:W607
- neighbourhood: A461: 'Tomato' | B461: 0 | C461: 0 | A462: 'Tomato' | B462: 0 | C462: 0 | A463: 'Tomatoes' | B463: 0 | C463: 0 | A464: 'Tomatoes' | B464: 0 | C464: 0 | A465: 'Turkey Bacon' | B465: 0 | C465: 0

### `dcb4821e417e|DUPLICATE_KEY|Sheet1!A12,Sheet1!A13,Sheet1!A14,Sheet1!A15`

- workbook: `all_data_912_v0.1/spreadsheet/49118/3_49118_input.xlsx`
- location: `Sheet1!A12, Sheet1!A13, Sheet1!A14, Sheet1!A15`  severity: Medium  confidence: Review
- evidence: Normalized key '44524kem545' appears 4 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '44524KEM545'; row labels: []; column header: "'44525WOL205'"; used range: A1:D15
- neighbourhood: A10: '44525WOL205' | C10: 26.63 | A11: '44525WOL205' | C11: 26.17 | A12: '44524KEM545' | C12: 27.41 | A13: '44524KEM545' | C13: 27.24 | A14: '44524KEM545' | C14: 26.84

### `ac9c457a4aed|DUPLICATE_KEY|URNlookup!K886,URNlookup!K1435`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `URN lookup!K886, URN lookup!K1435`  severity: Medium  confidence: Review
- evidence: Normalized key 'yo17 8la' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'YO17 8LA'; row labels: ["'Rillington'", "'Malton'"]; column header: "'YO19 6PF'"; used range: A1:X1461
- neighbourhood: J884: 'Malton' | K884: 'YO17 9BG' | L884: 'Open' | I885: 'Coppergate' | J885: 'York' | K885: 'YO19 6PF' | L885: 'Open' | J886: 'Malton' | K886: 'YO17 8LA' | L886: 'Closed' | J887: 'Filey' | K887: 'YO14 9LU' | L887: 'Open' | J888: 'Selby' | K888: 'YO8 9BG' | L888: 'Open'

### `1c06477fced9|DUPLICATE_KEY|URNlookup!K688,URNlookup!K1204`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `URN lookup!K688, URN lookup!K1204`  severity: Medium  confidence: Review
- evidence: Normalized key 'bb7 4qs' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'BB7 4QS'; row labels: ["'Grindleton'", "'Clitheroe'"]; column header: "'BB18 5EN'"; used range: A1:X1461
- neighbourhood: J686: 'Skelmersdale' | K686: 'WN8 8LQ' | L686: 'Open' | J687: 'Barnoldswick' | K687: 'BB18 5EN' | L687: 'Open' | J688: 'Clitheroe' | K688: 'BB7 4QS' | L688: 'Open' | J689: 'Clitheroe' | K689: 'BB7 3JE' | L689: 'Open' | J690: 'Clitheroe' | K690: 'BB7 4NP' | L690: 'Open'

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K1015,URNlookup!K1439`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K1015, URN lookup!K1439`  severity: Medium  confidence: Review
- evidence: Normalized key 'yo21 1ux' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'YO21 1UX'; row labels: ["'Egton Bridge'", "'Whitby'"]; column header: "'YO62 4DE'"; used range: A1:X1461
- neighbourhood: J1013: 'Harrogate' | K1013: 'HG1 4AP' | L1013: 'Closed' | J1014: 'York' | K1014: 'YO62 4DE' | L1014: 'Closed' | J1015: 'Whitby' | K1015: 'YO21 1UX' | L1015: 'Closed' | J1016: 'Malton' | K1016: 'YO17 7DB' | L1016: 'Closed' | J1017: 'Pickering' | K1017: 'YO18 8AR' | L1017: 'Closed'

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K338,URNlookup!K1164`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K338, URN lookup!K1164`  severity: Medium  confidence: Review
- evidence: Normalized key 'pr2 6ee' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'PR2 6EE'; row labels: ["'Ribbleton'", "'Preston'"]; column header: "'PR1 5RU'"; used range: A1:X1461
- neighbourhood: J336: 'Preston' | K336: 'PR1 6HP' | L336: 'Open' | J337: 'Preston' | K337: 'PR1 5RU' | L337: 'Open' | J338: 'Preston' | K338: 'PR2 6EE' | L338: 'Open' | J339: 'Preston' | K339: 'PR2 2BN' | L339: 'Open' | J340: 'Preston' | K340: 'PR2 1TU' | L340: 'Open'

### `ac9c457a4aed|DUPLICATE_KEY|URNlookup!K803,URNlookup!K1423`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `URN lookup!K803, URN lookup!K1423`  severity: Medium  confidence: Review
- evidence: Normalized key 'yo11 1hs' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'YO11 1HS'; row labels: ["'Friargate'", "'Scarborough'"]; column header: "'YO11 3LG'"; used range: A1:X1461
- neighbourhood: J801: 'Scarborough' | K801: 'YO12 6NQ' | L801: 'Open' | J802: 'Scarborough' | K802: 'YO11 3LG' | L802: 'Closed' | J803: 'Scarborough' | K803: 'YO11 1HS' | L803: 'Closed' | J804: 'Scarborough' | K804: 'YO12 7DD' | L804: 'Open' | J805: 'Scarborough' | K805: 'YO12 6LP' | L805: 'Open'

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A285,RS.Food!A286`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A285, RS.Food!A286`  severity: Medium  confidence: Review
- evidence: Normalized key 'all' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'All'; row labels: []; column header: "'ADD'"; used range: A1:W607
- neighbourhood: A283: '------------' | B283: 0 | C283: 0 | A284: 'ADD' | B284: 0 | C284: 0 | A285: 'All' | B285: 0 | C285: 0 | A286: 'All' | B286: 0 | C286: 0 | A287: 'All Bran' | B287: 0 | C287: 0

### `6bc9e1c652db|DUPLICATE_KEY|Sheet2!B11,Sheet2!B20`

- workbook: `all_data_912_v0.1/spreadsheet/52216/1_52216_input.xlsx`
- location: `Sheet2!B11, Sheet2!B20`  severity: Medium  confidence: Review
- evidence: Normalized key 'telco' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Telco'; row labels: ["'Regional'"]; column header: "'Salaries & Wages'"; used range: A1:G20
- neighbourhood: A9: 'Regional' | B9: 'R&M' | A10: 'Regional' | B10: 'Salaries & Wages' | A11: 'Regional' | B11: 'Telco' | A12: 'Metro' | B12: 'Advertising & Marketing' | C12: 9.09 | D12: 7.76 | A13: 'Metro' | B13: 'Electricity'

### `d49eeac3b8af|DUPLICATE_KEY|Sheet1!B6,Sheet1!B9,Sheet1!B13,Sheet1!B17,Sheet1!B22`

- workbook: `all_data_912_v0.1/spreadsheet/59902/2_59902_input.xlsx`
- location: `Sheet1!B6, Sheet1!B9, Sheet1!B13, Sheet1!B17, Sheet1!B22`  severity: Medium  confidence: Review
- evidence: Normalized key 'jane' appears 5 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Jane'; row labels: []; column header: "'Bob'"; used range: A1:H28
- neighbourhood: A4: 'Date' | B4: 'Name' | C4: 'Days Since Sale' | A5: 2008-08-29 00:00:00 | B5: 'Bob' | C5: '=A5-INDEX($A$4:$A4,MATCH(B5,$B$4:$B4,0),1)' -> '#N/A' | A6: 2008-08-29 00:00:00 | B6: 'Jane' | C6: '=A6-INDEX($A$4:$A5,MATCH(B6,$B$4:$B5,0),1)' -> '#N/A' | A7: 2008-08-30 00:00:00 | B7: 'Bob' | C7: '=A7-INDEX($A$4:$A6,MATCH(B7,$B$4:$B6,0),1)' -> 1 | A8: 2008-08-30 00:00:00 | B8: 'Bob' | C8: '=A8-INDEX($A$4:$A7,MATCH(B8,$B$4:$B7,0),1)' -> 1

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A333,RS.Food!A334`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A333, RS.Food!A334`  severity: Medium  confidence: Review
- evidence: Normalized key 'cold milk' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Cold Milk'; row labels: []; column header: "'Coco Pops'"; used range: A1:W607
- neighbourhood: A331: 'Coconut Milk' | B331: 0 | C331: 0 | A332: 'Coco Pops' | B332: 0 | C332: 0 | A333: 'Cold Milk' | B333: 0 | C333: 0 | A334: 'Cold Milk' | B334: 0 | C334: 0 | A335: 'Cornflakes' | B335: 0 | C335: 0

### `21865bab73e8|DUPLICATE_KEY|RS.Food!A467,RS.Food!A468`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!A467, RS.Food!A468`  severity: Medium  confidence: Review
- evidence: Normalized key 'vanilla' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Vanilla'; row labels: []; column header: "'Vanilia'"; used range: A1:W607
- neighbourhood: A465: 'Turkey Bacon' | B465: 0 | C465: 0 | A466: 'Vanilia' | B466: 0 | C466: 0 | A467: 'Vanilla' | B467: 0 | C467: 0 | A468: 'Vanilla' | B468: 0 | C468: 0 | A469: 'Veg Sausage' | B469: 0 | C469: 0

### `55d45b916f0d|DUPLICATE_KEY|Sheet1!A11,Sheet1!A23`

- workbook: `all_data_912_v0.1/spreadsheet/48799/2_48799_input.xlsx`
- location: `Sheet1!A11, Sheet1!A23`  severity: Medium  confidence: Review
- evidence: Normalized key 'j' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'J'; row labels: []; column header: "'I'"; used range: A1:D25
- neighbourhood: A9: 'H' | B9: 3.47 | C9: 4.7766 | A10: 'I' | B10: 6.72 | C10: 2.94 | A11: 'J' | B11: 8.86 | C11: 5.97 | A12: 'K' | B12: 20.54 | C12: 9.0042 | A13: 'L' | B13: 9.54 | C13: 5.5044

### `f367b87c90dd|DUPLICATE_KEY|Sheet1!D4,Sheet1!D8`

- workbook: `all_data_912_v0.1/spreadsheet/59185/3_59185_input.xlsx`
- location: `Sheet1!D4, Sheet1!D8`  severity: Medium  confidence: Review
- evidence: Normalized key 'qc hold' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'QC HOLD'; row labels: []; column header: ''; used range: A1:P22
- neighbourhood: B2: 'GNB Splits' | D2: 'CBV/WBNB mix' | E2: 'Pb' | F2: 'PB/CBV mix' | B3: 1026 | C3: 1192 | D3: 4116 | E3: 1102 | F3: 2166 | D4: 'QC HOLD' | B6: 'CBV Splits' | C6: 'Pb Splits' | D6: 'CBV/WBNB mix' | F6: 'PB/CBV'

### `b7d670f8a092|DUPLICATE_KEY|Sheet1!A9,Sheet1!A21`

- workbook: `all_data_912_v0.1/spreadsheet/48799/1_48799_input.xlsx`
- location: `Sheet1!A9, Sheet1!A21`  severity: Medium  confidence: Review
- evidence: Normalized key 'h' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'H'; row labels: []; column header: "'G'"; used range: A1:D25
- neighbourhood: A7: 'F ' | B7: 6.2 | C7: 7.458 | A8: 'G' | B8: 4.62 | C8: 4.461 | A9: 'H' | B9: 3.47 | C9: 4.7766 | A10: 'I' | B10: 6.72 | C10: 2.94 | A11: 'J' | B11: 8.86 | C11: 5.97

### `2bdd3699e805|DUPLICATE_KEY|Sheet2!A3,Sheet2!A4,Sheet2!A5,Sheet2!A6,Sheet2!A7`

- workbook: `all_data_912_v0.1/spreadsheet/52216/2_52216_input.xlsx`
- location: `Sheet2!A3, Sheet2!A4, Sheet2!A5, Sheet2!A6, Sheet2!A7`  severity: Medium  confidence: Review
- evidence: Normalized key 'regional' appears 9 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Regional'; row labels: []; column header: ''; used range: A1:G20
- neighbourhood: C1: 1 | A3: 'Regional' | B3: 'Advertising & Marketing' | C3: 3.5 | A4: 'Regional' | B4: 'Electricity' | C4: 1.24 | A5: 'Regional' | B5: 'Insurance' | C5: 2.56

### `b9f3fd76f8c0|DUPLICATE_KEY|Grouping!A4,Grouping!A6`

- workbook: `all_data_912_v0.1/spreadsheet/7902/1_7902_input.xlsx`
- location: `Grouping!A4, Grouping!A6`  severity: Medium  confidence: Review
- evidence: Normalized key 'group c' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Group C'; row labels: []; column header: "'Group B'"; used range: A1:I7
- neighbourhood: A2: 'Group A' | C2: 0 | A3: 'Group B' | C3: 0.1 | A4: 'Group C' | C4: 0.05 | A5: 'Group B' | B5: 'Material X' | C5: 0.12 | A6: 'Group C' | B6: 'Material Y' | C6: 0.05

### `55d45b916f0d|DUPLICATE_KEY|Sheet1!A8,Sheet1!A20`

- workbook: `all_data_912_v0.1/spreadsheet/48799/2_48799_input.xlsx`
- location: `Sheet1!A8, Sheet1!A20`  severity: Medium  confidence: Review
- evidence: Normalized key 'g' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'G'; row labels: []; column header: "'F '"; used range: A1:D25
- neighbourhood: A6: 'E' | B6: 7.8 | C6: 6.282 | A7: 'F ' | B7: 6.2 | C7: 7.458 | A8: 'G' | B8: 4.62 | C8: 4.461 | A9: 'H' | B9: 3.47 | C9: 4.7766 | A10: 'I' | B10: 6.72 | C10: 2.94

### `852b58472b57|DUPLICATE_KEY|Sheet1!D4,Sheet1!D8`

- workbook: `all_data_912_v0.1/spreadsheet/59185/1_59185_input.xlsx`
- location: `Sheet1!D4, Sheet1!D8`  severity: Medium  confidence: Review
- evidence: Normalized key 'qc hold' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'QC HOLD'; row labels: []; column header: ''; used range: A1:P24
- neighbourhood: B2: 'GNB Splits' | D2: 'CBV/WBNB mix' | E2: 'Pb' | F2: 'PB/CBV mix' | B3: 1026 | C3: 1192 | D3: 4116 | E3: 1102 | F3: 2166 | D4: 'QC HOLD' | B6: 'CBV Splits' | C6: 'Pb Splits' | D6: 'CBV/WBNB mix' | F6: 'PB/CBV'

### `3db55cfd98cc|DUPLICATE_KEY|Sheet2!B10,Sheet2!B19`

- workbook: `all_data_912_v0.1/spreadsheet/52216/3_52216_input.xlsx`
- location: `Sheet2!B10, Sheet2!B19`  severity: Medium  confidence: Review
- evidence: Normalized key 'salaries & wages' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Salaries & Wages'; row labels: ["'Regional'"]; column header: "'R&M'"; used range: A1:G20
- neighbourhood: A8: 'Regional' | B8: 'Rates' | A9: 'Regional' | B9: 'R&M' | A10: 'Regional' | B10: 'Salaries & Wages' | A11: 'Regional' | B11: 'Telco' | A12: 'Metro' | B12: 'Advertising & Marketing' | C12: 9.09 | D12: 7.76

## FORMULA_DRIFT

### `1ee00a60f590|FORMULA_DRIFT|Sheet1!N294`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!N294`  severity: High  confidence: Likely defect
- formula: `=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=18): =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90,RC[-7]>=300),RC[-7],""),"")
- evidence: This cell: =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90120,RC[-7]>=300),RC[-7],""),"")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: L292: '=IFERROR(IF(I291>=12,IF($J291<=120,0+SUBSTITUTE(IF($D292>=150,","&... -> None | M292: '=IFERROR(IF(I291>=12,IF($J291<=140,0+SUBSTITUTE(IF($D292>=175,","&... -> None | N292: '=IF(I291>=12,IF(AND(J291<=90,G292>=300),G292,""),"")' -> None | O292: '=IF(I291>=12,IF(AND(J291<=120,G292>=400),G292,""),"")' -> None | P292: '=IF(I291>=12,IF(AND(J291<=145,G292>=500),G292,""),"")' -> None | L293: '=IFERROR(IF(I292>=12,IF($J292<=120,0+SUBSTITUTE(IF($D293>=150,","&... -> None | M293: '=IFERROR(IF(I292>=12,IF($J292<=140,0+SUBSTITUTE(IF($D293>=175,","&... -> None | N293: '=IF(I292>=12,IF(AND(J292<=90,G293>=300),G293,""),"")' -> None | O293: '=IF(I292>=12,IF(AND(J292<=120,G293>=400),G293,""),"")' -> None | P293: '=IF(I292>=12,IF(AND(J292<=145,G293>=500),G293,""),"")' -> None | L294: '=IFERROR(IF(I293>=12,IF($J293<=120,0+SUBSTITUTE(IF($D294>=150,","&... -> None | M294: '=IFERROR(IF(I293>=12,IF($J293<=140,0+SUBSTITUTE(IF($D294>=175,","&... -> None | N294: '=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")' -> None | O294: '=IF(I293>=12,IF(AND(J293<=120,G294>=400),G294,""),"")' -> None | P294: '=IF(I293>=12,IF(AND(J293<=145,G294>=500),G294,""),"")' -> None | L295: '=IFERROR(IF(I294>=12,IF($J294<=120,0+SUBSTITUTE(IF($D295>=150,","&... -> None | M295: '=IFERROR(IF(I294>=12,IF($J294<=140,0+SUBSTITUTE(IF($D295>=175,","&... -> None | L296: '=IFERROR(IF(I295>=12,IF($J295<=120,0+SUBSTITUTE(IF($D296>=150,","&... -> None | M296: '=IFERROR(IF(I295>=12,IF($J295<=140,0+SUBSTITUTE(IF($D296>=175,","&... -> None | N296: '=IF(I295>=12,IF(AND(J295<=120,G296>=300),G296,""),"")' -> None

### `f8ace651bacd|FORMULA_DRIFT|EXCELHELP!O12`

- workbook: `all_data_912_v0.1/spreadsheet/39946/1_39946_input.xlsx`
- location: `EXCEL HELP!O12`  severity: High  confidence: Likely defect
- formula: `=$G$12/$J$12*(O4-17)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =R12C7/R12C10*R[-8]C
- evidence: This cell: =R12C7/R12C10*(R[-8]C-17)
- cached value: 46.027397260274; row labels: []; column header: ''; used range: A1:AF23
- neighbourhood: M10: '=G10' -> 832.5 | O12: '=$G$12/$J$12*(O4-17)' -> 46.027397260274 | P12: '=$G$12/$J$12*P4' -> 101.917808219178 | Q12: '=$G$12/$J$12*Q4' -> 92.0547945205479 | N13: '=G13' -> 1000

### `19dfd5dbcec5|FORMULA_DRIFT|formamspnc(7)!AT5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!AT5`  severity: High  confidence: Likely defect
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(B5:P5,B$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =RC[-15]
- evidence: This cell: =_XLFN.IFNA(LOOKUP(1,0/COUNTIFS(RC[-44]:RC[-30],R1C[-44]+{1,0,-1}),{1,0,-1}),"")
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range B5:P5: values ['0', '0', '3', 'None', 'None', 'None', 'None', '0', 'None', 'None', 'None', 'None']; beyond: {'left': "A5: '1 ext,1st 1 ext'", 'right': 'Q5: None'}
- neighbourhood: AV3: 626 | AT5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(B5:P5,B$1+{1,0,-1}),{1,0,-1}),"") ... -> None | AR6: '=SUM(AE6:AN6)' -> 5 | AS6: '=CONCATENATE(AE6,",",AF6,",",AG6,",",AH6,",",AI6,",",AJ6,",",AK6,"... -> '0,0,1,4,-2,0,0,-1,3,0,-2,0,1' | AT6: '=AE6' -> 0 | AU6: '=AF6+AT6' -> 0 | AV6: '=SUM(AE6:AG6)' -> 1 | AR7: '=SUM(AE7:AN7)' -> 3 | AS7: '=CONCATENATE(AE7,",",AF7,",",AG7,",",AH7,",",AI7,",",AJ7,",",AK7,"... -> '-1,1,1,-2,1,0,1,2,-2,2,-1,... | AT7: '=AE7' -> -1 | AU7: '=AF7+AT7' -> 0 | AV7: '=SUM(AE7:AG7)' -> 1

### `c202b154985b|FORMULA_DRIFT|Sheet1!AH6`

- workbook: `all_data_912_v0.1/spreadsheet/34469/3_34469_input.xlsx`
- location: `Sheet1!AH6`  severity: High  confidence: Likely defect
- formula: `=IF(AND($C$6:$AF$6="0,5",$C$6:$AF$6="1"),SUM($C$6:$AF$6),0)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=9): =COUNTIF(RC3:RC33,R5C)+0.5*COUNTIF(RC3:RC33,R5C&"H")+0.5*COUNTIF(RC3:RC33,"H"&R5C)
- evidence: This cell: =IF(AND(R6C3:R6C32="0,5",R6C3:R6C32="1"),SUM(R6C3:R6C32),0)
- cached value: 0; row labels: ["'Emp 1'"]; column header: "'Totals'"; used range: A1:AK15
- range $C$6:$AF$6: values ['1', 'None', 'None', '0.5', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '1']; beyond: {'left': "B6: 'Emp 1'", 'right': 'AG6: None'}
- neighbourhood: AF4: 'Sa' | AG4: '=IF(AG5="","",INDEX({"Su";"M";"Tu";"W";"Th";"F";"Sa"},WEEKDAY(AG5,... -> None | AF5: 2023-09-30 00:00:00 | AG5: '=IF(MONTH($AD5+3)>MONTH($C$5),"",$AD5+3)' -> None | AH6: '=IF(AND($C$6:$AF$6="0,5",$C$6:$AF$6="1"),SUM($C$6:$AF$6),0) {array... -> 0 | AH7: '=COUNTIF($C7:$AG7,AH$5)+0.5*COUNTIF($C7:$AG7,AH$5&"H")+0.5*COUNTIF... -> 0 | AH8: '=COUNTIF($C8:$AG8,AH$5)+0.5*COUNTIF($C8:$AG8,AH$5&"H")+0.5*COUNTIF... -> 0

### `b0189d43ef5f|FORMULA_DRIFT|DATABASECountries!F4`

- workbook: `all_data_912_v0.1/spreadsheet/37462/2_37462_input.xlsx`
- location: `DATABASE Countries!F4`  severity: High  confidence: Likely defect
- formula: `=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=240): =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C2:R36C2)
- evidence: This cell: =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C3:R36C3)
- cached value: '#VALUE!'; row labels: ["'India'", "'Afghanistan'"]; column header: "'Revenue'"; used range: A1:J244
- range $A$4:$A$36: values ["'India'", "'United Kingdom'", "'Afghanistan'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "A3: 'Country'", 'below': 'A37: None'}
- neighbourhood: E2: 'TOTAL' | F2: '=SUM(F4:F83)' -> '#VALUE!' | E3: 'Countries' | F3: 'Revenue' | D4: 1 | E4: 'Afghanistan' | F4: '=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36) {array F4}' -> '#VALUE!' | H4: 'TOP 1' | D5: '=D4+1' -> 2 | E5: 'Albania' | F5: '=SUMPRODUCT(ISNUMBER(SEARCH(E5,$A$4:$A$36))*$B$4:$B$36) {array F5}' -> 0 | H5: 'TOP 2' | D6: '=D5+1' -> 3 | E6: 'Algeria' | F6: '=SUMPRODUCT(ISNUMBER(SEARCH(E6,$A$4:$A$36))*$B$4:$B$36) {array F6}' -> 0 | H6: 'TOP 3'

### `f065dc30ad2b|FORMULA_DRIFT|Sheet1!BI23`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/2_CF_6540_input.xlsx`
- location: `Sheet1!BI23`  severity: High  confidence: Likely defect
- formula: `=525*1.5`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=3): =RC[-3]*1.5
- evidence: This cell: =525*1.5
- cached value: 787.5; row labels: ["'Technical Officer '"]; column header: ''; used range: A1:CL123
- neighbourhood: BG23: 525 | BH23: 525 | BI23: '=525*1.5' -> 787.5 | BG24: 21.75 | BH24: 22.75 | BI24: '=BF24*1.5' -> 32.625 | BG25: 21.75 | BH25: 22.75 | BI25: '=BF25*1.5' -> 32.625

### `a67205f1d2d7|FORMULA_DRIFT|Sheet1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/49246/3_49246_input.xlsx`
- location: `Sheet1!B3`  severity: High  confidence: Likely defect
- formula: `=IF(A3="",VLOOKUP(A3,$J$1:$K$4,2,0))`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=12): =VLOOKUP(RC[-1],R1C10:R4C11,2,0)
- evidence: This cell: =IF(RC[-1]="",VLOOKUP(RC[-1],R1C10:R4C11,2,0))
- cached value: '#N/A'; row labels: ["''"]; column header: ''; used range: A1:K15
- range $J$1:$K$4: values ["'Outlet #'", "'Outlet'", '1062929', "'Restaurant F'", '7195746', "'Restaurant B'", '7195753', "'Restaurant C'"]; beyond: {}
- neighbourhood: A1: 'Outlet Number' | B1: 'Outlet ' | C1: 'Time\n' | D1: 'Date' | A2: 1062929 | B2: '=VLOOKUP(A2,$J$1:$K$4,2,0)' -> 'Restaurant F' | C2: 'Lunch' | D2: '22OCT2021' | A3: '' | B3: '=IF(A3="",VLOOKUP(A3,$J$1:$K$4,2,0))' -> '#N/A' | C3: 'Lunch' | D3: '22OCT2021' | A4: '' | B4: '=VLOOKUP(A4,$J$1:$K$4,2,0)' -> '#N/A' | C4: 'Dinner' | D4: '22OCT2021' | A5: '' | B5: '=VLOOKUP(A5,$J$1:$K$4,2,0)' -> '#N/A' | C5: 'Dinner' | D5: '22OCT2021'

### `4ea284d68c01|FORMULA_DRIFT|Sheet1!Y4`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!Y4`  severity: High  confidence: Likely defect
- formula: `=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=16): =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1],"0")
- evidence: This cell: =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1]," ")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: Z2: '=CONCATENATE(A2," ",B2," ")' -> 'AA AB' | AA2: 'High Scratch Game #1' | W3: '=IF(AND(I2>=12,G3>0),ROUNDDOWN(SUM(200-J2)*0.9,0)+V3," ")' -> None | X3: '=SUM(G3)' -> 291 | Y3: '=IF(AND(I2>=12,G3>0),SUM(ROUNDDOWN(SUM(200-J2)*0.9,0)*3)+X3," ")' -> None | AA3: 'High Scratch Game #2' | W4: '=IF(AND(I3>=12,G4>0),ROUNDDOWN(SUM(200-J3)*0.9,0)+V4," ")' -> ' ' | X4: '=SUM(G4)' -> 372 | Y4: '=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")' -> None | AA4: 'High Scratch Game #3' | W5: '=IF(AND(I4>=12,G5>0),ROUNDDOWN(SUM(200-J4)*0.9,0)+V5," ")' -> ' ' | X5: '=SUM(G5)' -> 0 | Y5: '=IF(AND(I4>=12,G5>0),SUM(ROUNDDOWN(SUM(200-J4)*0.9,0)*3)+X5,"0")' -> '0' | AA5: 'High Scratch Game #4' | W6: '=IF(AND(I5>=12,G6>0),ROUNDDOWN(SUM(200-J5)*0.9,0)+V6," ")' -> ' ' | X6: '=SUM(G6)' -> 340 | Y6: '=IF(AND(I5>=12,G6>0),SUM(ROUNDDOWN(SUM(200-J5)*0.9,0)*3)+X6,"0")' -> '0' | AA6: 'High Scratch Game #5'

### `bc56a9f2824a|FORMULA_DRIFT|Total(2)!E31`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!E31`  severity: High  confidence: Likely defect
- formula: `=SUM(B31*0.5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =IFERROR(VLOOKUP(RC8,R27C10:R35C12,3,0)*RC3,0)
- evidence: This cell: =SUM(RC[-3]*0.5)
- cached value: 900; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C' | C32: '=(B32*12)/12' -> 3000 | D32: '=SUM(C32-E32)' -> 1050 | E32: '=IFERROR(VLOOKUP($H32,$J$27:$L$35,3,0)*$C32,0)' -> 1950 | F32: 44589 | G32: 'C' | C33: '=(B33*12)/12' -> 2400 | D33: '=SUM(C33-E33)' -> 480 | E33: '=IFERROR(VLOOKUP($H33,$J$27:$L$35,3,0)*$C33,0)' -> 1920

### `74d967658eee|FORMULA_DRIFT|Sheet1!N294`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!N294`  severity: High  confidence: Likely defect
- formula: `=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=18): =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90,RC[-7]>=300),RC[-7],""),"")
- evidence: This cell: =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90120,RC[-7]>=300),RC[-7],""),"")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: L292: '=IFERROR(IF(I291>=12,IF($J291<=120,0+SUBSTITUTE(IF($D292>=150,","&... -> None | M292: '=IFERROR(IF(I291>=12,IF($J291<=140,0+SUBSTITUTE(IF($D292>=175,","&... -> None | N292: '=IF(I291>=12,IF(AND(J291<=90,G292>=300),G292,""),"")' -> None | O292: '=IF(I291>=12,IF(AND(J291<=120,G292>=400),G292,""),"")' -> None | P292: '=IF(I291>=12,IF(AND(J291<=145,G292>=500),G292,""),"")' -> None | L293: '=IFERROR(IF(I292>=12,IF($J292<=120,0+SUBSTITUTE(IF($D293>=150,","&... -> None | M293: '=IFERROR(IF(I292>=12,IF($J292<=140,0+SUBSTITUTE(IF($D293>=175,","&... -> None | N293: '=IF(I292>=12,IF(AND(J292<=90,G293>=300),G293,""),"")' -> None | O293: '=IF(I292>=12,IF(AND(J292<=120,G293>=400),G293,""),"")' -> None | P293: '=IF(I292>=12,IF(AND(J292<=145,G293>=500),G293,""),"")' -> None | L294: '=IFERROR(IF(I293>=12,IF($J293<=120,0+SUBSTITUTE(IF($D294>=150,","&... -> None | M294: '=IFERROR(IF(I293>=12,IF($J293<=140,0+SUBSTITUTE(IF($D294>=175,","&... -> None | N294: '=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")' -> None | O294: '=IF(I293>=12,IF(AND(J293<=120,G294>=400),G294,""),"")' -> None | P294: '=IF(I293>=12,IF(AND(J293<=145,G294>=500),G294,""),"")' -> None | L295: '=IFERROR(IF(I294>=12,IF($J294<=120,0+SUBSTITUTE(IF($D295>=150,","&... -> None | M295: '=IFERROR(IF(I294>=12,IF($J294<=140,0+SUBSTITUTE(IF($D295>=175,","&... -> None | L296: '=IFERROR(IF(I295>=12,IF($J295<=120,0+SUBSTITUTE(IF($D296>=150,","&... -> None | M296: '=IFERROR(IF(I295>=12,IF($J295<=140,0+SUBSTITUTE(IF($D296>=175,","&... -> None | N296: '=IF(I295>=12,IF(AND(J295<=120,G296>=300),G296,""),"")' -> None

### `e1683f0529fe|FORMULA_DRIFT|MoneyInCheckingNextMonth!L2`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/3_CF_22493_input.xlsx`
- location: `Money In Checking Next Month!L2`  severity: High  confidence: Likely defect
- formula: `=M14`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =SUM(R[2]C:R[9]C)
- evidence: This cell: =R[12]C[1]
- cached value: 0; row labels: ["'18th'", "'Automatically Paid'"]; column header: "'Total Tax'"; used range: A1:BJ103
- neighbourhood: K1: 'Legend' | L1: 'Total Tax' | M1: 'Monthly Income' | N1: 'Total Income' | K2: 'Automatically Paid' | L2: '=M14' -> 0 | M2: '=SUM(M4:M11)' -> 8128.84 | N2: '=SUM(N4:N11)' -> 0 | K3: "Same Am't Monthly" | K4: 'Varies By Month' | L4: 'Larry RRB' | M4: 3546.86 | N4: '=SUM(O4:Z4)' -> 0

### `5c702dac6268|FORMULA_DRIFT|Tabelle1!Q17`

- workbook: `all_data_912_v0.1/spreadsheet/42058/3_42058_input.xlsx`
- location: `Tabelle1!Q17`  severity: High  confidence: Likely defect
- formula: `=AVERAGE(E17:P17)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=8): =SUM(RC[-12]:RC[-1])
- evidence: This cell: =AVERAGE(RC[-12]:RC[-1])
- cached value: '#DIV/0!'; row labels: ["'planned'"]; column header: ''; used range: A1:Q18
- range E17:P17: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': "D17: '=AVERAGE(E17:I17)'", 'right': "Q17: '=AVERAGE(E17:P17)'"}
- neighbourhood: O15: 0.35 | P15: 0.4 | Q15: '=SUM(E15:P15)' -> 4.23 | Q16: '=SUM(E16:P16)' -> 1.266 | Q17: '=AVERAGE(E17:P17)' -> '#DIV/0!'

### `1303e2ce7522|FORMULA_DRIFT|Summary!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17111/1_17111_input.xlsx`
- location: `Summary!B2`  severity: High  confidence: Likely defect
- formula: `=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary!$B$1)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=4): =SUMIFS(SHEET1!C[2]:C[2],SHEET1!C:C,SUMMARY!RC[-1],SHEET1!C[1]:C[1],SUMMARY!R1C2)
- evidence: This cell: =SUMIFS(SHEET1!C4:C4,SHEET1!C2:C2,SUMMARY!RC1,SHEET1!C3:C3,SUMMARY!R1C2)
- cached value: 200; row labels: ["'neha'"]; column header: "'HD'"; used range: A1:F9
- neighbourhood: A1: 'Name' | B1: 'HD' | C1: 'SD' | A2: 'neha' | B2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 200 | C2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 698 | A3: 'rahul' | B3: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A3,Sheet1!C:C,Summary!$B$1)' -> 1126 | C3: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A3,Sheet1!$C:$C,Summary... -> 131 | A4: 'mohit' | B4: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A4,Sheet1!C:C,Summary!$B$1)' -> 954 | C4: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A4,Sheet1!$C:$C,Summary... -> 586

### `fa447aaa15b1|FORMULA_DRIFT|Sheet1!C5`

- workbook: `all_data_912_v0.1/spreadsheet/56576/2_56576_input.xlsx`
- location: `Sheet1!C5`  severity: High  confidence: Likely defect
- formula: `=SUM(D5:J5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=30): =IFERROR(AVERAGE(RC5,RC6,RC7,RC8,RC9),"")
- evidence: This cell: =SUM(RC[1]:RC[7])
- cached value: 5; row labels: ["'Wins (1=win)'"]; column header: "'Weekly Average'"; used range: A1:J36
- range D5:J5: values ["'Let go'", '1', '1', '1', '1', '1', "'Let Go'"]; beyond: {'left': "C5: '=SUM(D5:J5)'", 'right': 'K5: None'}
- neighbourhood: A3: 'Element' | A4: 'Name' | A5: 'Wins (1=win)' | C5: '=SUM(D5:J5)' -> 5 | D5: 'Let go' | E5: 1 | B6: '=RANK(C6,$C$6:$C$35,0)' -> 26 | C6: '=IFERROR(AVERAGE($E6,$F6,$G6,$H6,$I6),"")' -> 117425.6 | D6: 7031 | E6: 98818 | B7: '=RANK(C7,$C$6:$C$35,0)' -> 3 | C7: '=IFERROR(AVERAGE($E7,$F7,$G7,$H7,$I7),"")' -> 268081.8 | D7: 98341 | E7: 217719

### `e82a4e0e50b2|FORMULA_DRIFT|DATABASECountries!F4`

- workbook: `all_data_912_v0.1/spreadsheet/37462/1_37462_input.xlsx`
- location: `DATABASE Countries!F4`  severity: High  confidence: Likely defect
- formula: `=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=240): =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C2:R36C2)
- evidence: This cell: =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C3:R36C3)
- cached value: '#VALUE!'; row labels: ["'India'", "'Afghanistan'"]; column header: "'Revenue'"; used range: A1:J244
- range $A$4:$A$36: values ["'India'", "'United Kingdom'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "A3: 'Country'", 'below': 'A37: None'}
- neighbourhood: E2: 'TOTAL' | F2: '=SUM(F4:F83)' -> '#VALUE!' | E3: 'Countries' | F3: 'Revenue' | D4: 1 | E4: 'Afghanistan' | F4: '=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36) {array F4}' -> '#VALUE!' | H4: 'TOP 1' | D5: '=D4+1' -> 2 | E5: 'Albania' | F5: '=SUMPRODUCT(ISNUMBER(SEARCH(E5,$A$4:$A$36))*$B$4:$B$36) {array F5}' -> 0 | H5: 'TOP 2' | D6: '=D5+1' -> 3 | E6: 'Algeria' | F6: '=SUMPRODUCT(ISNUMBER(SEARCH(E6,$A$4:$A$36))*$B$4:$B$36) {array F6}' -> 0 | H6: 'TOP 3'

### `970db979d624|FORMULA_DRIFT|formamspnc(7)!CO5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!CO5`  severity: High  confidence: Likely defect
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=12): =_XLFN.IFNA(LOOKUP(1,0/COUNTIFS(RC[-62]:RC[-32],R1C[-62]+{1,0,-1}),{1,0,-1}),"")
- evidence: This cell: =_XLFN.IFNA(LOOKUP(1,0/COUNTIFS(RC[-62]:RC[-50],R1C[-62]+{1,0,-1}),{1,0,-1}),"")
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AQ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AR5: None'}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CM6: '=IF(COUNTIF(BX6:CJ6,0)>3,COUNTIF(BX6:CJ6,0),"")' -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CM7: '=IF(COUNTIF(BX7:CJ7,0)>3,COUNTIF(BX7:CJ7,0),"")' -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `19ea38afb413|FORMULA_DRIFT|Sheet1!G9`

- workbook: `all_data_912_v0.1/spreadsheet/33094/3_33094_input.xlsx`
- location: `Sheet1!G9`  severity: High  confidence: Likely defect
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =R[-1]C/R7C2
- evidence: This cell: =SUMIF([1]SHEET2!$A$4:$A$1000,RC1,[1]SHEET2!L$4:L$1000)
- cached value: 0; row labels: ["'Employee3'"]; column header: ''; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: E7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!J$4:J$1000)' -> 0 | F7: 25 | G7: 25 | H7: 25 | I7: 17 | E8: '=E7/$B$7' -> 0 | F8: '=F7/$B$7' -> 0.625 | G8: '=G7/$B$7' -> 0.625 | H8: '=H7/$B$7' -> 0.625 | I8: '=I7/$B$7' -> 0.425 | E9: 10 | F9: 8 | G9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)' -> 0 | H9: 6 | I9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!N$4:N$1000)' -> 0 | E10: '=E9/$B$7' -> 0.25 | F10: '=F9/$B$7' -> 0.2 | G10: '=G9/$B$7' -> 0 | H10: '=H9/$B$7' -> 0.15 | I10: '=I9/$B$7' -> 0

### `59dd5b78ebc8|FORMULA_DRIFT|results!J95`

- workbook: `all_data_912_v0.1/spreadsheet/54490/3_54490_input.xlsx`
- location: `results!J95`  severity: High  confidence: Likely defect
- formula: `=AVERAGEIFS(J$3:J$92,$B$3:$B$92,$B95,J$3:J$92,">0")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=23): =AVERAGEIFS(R3C:R92C,R3C2:R92C2,RC2,R3C:R92C,"<>0")
- evidence: This cell: =AVERAGEIFS(R3C:R92C,R3C2:R92C2,RC2,R3C:R92C,">0")
- cached value: 164.0667711688; row labels: ["'Night'"]; column header: ''; used range: A1:Z98
- range J$3:J$92: values ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']; beyond: {'above': "J2: 'T48 - Manual Machine Bay 10'", 'below': 'J93: None'}
- neighbourhood: H95: '=AVERAGEIFS(H$3:H$92,$B$3:$B$92,$B95,H$3:H$92,"<>0")' -> 224.850649409023 | I95: '=AVERAGEIFS(I$3:I$92,$B$3:$B$92,$B95,I$3:I$92,"<>0")' -> 200.9453718133 | J95: '=AVERAGEIFS(J$3:J$92,$B$3:$B$92,$B95,J$3:J$92,">0")' -> 164.0667711688 | K95: '=AVERAGEIFS(K$3:K$92,$B$3:$B$92,$B95,K$3:K$92,"<>0")' -> 177.786353113753 | L95: '=AVERAGEIFS(L$3:L$92,$B$3:$B$92,$B95,L$3:L$92,"<>0")' -> 225.939188673497 | H96: '=AVERAGEIFS(H$3:H$92,$B$3:$B$92,$B96,H$3:H$92,"<>0")' -> 196.656578295161 | I96: '=AVERAGEIFS(I$3:I$92,$B$3:$B$92,$B96,I$3:I$92,"<>0")' -> 160.950022336386 | J96: '=AVERAGEIFS(J$3:J$92,$B$3:$B$92,$B96,J$3:J$92,"<>0")' -> '#DIV/0!' | K96: '=AVERAGEIFS(K$3:K$92,$B$3:$B$92,$B96,K$3:K$92,"<>0")' -> 147.87329171428 | L96: '=AVERAGEIFS(L$3:L$92,$B$3:$B$92,$B96,L$3:L$92,"<>0")' -> 137.059294871795 | H97: '=AVERAGEIFS(H$3:H$92,$B$3:$B$92,$B97,H$3:H$92,"<>0")' -> 216.541498007442 | I97: '=AVERAGEIFS(I$3:I$92,$B$3:$B$92,$B97,I$3:I$92,"<>0")' -> 223.695632195464 | J97: '=AVERAGEIFS(J$3:J$92,$B$3:$B$92,$B97,J$3:J$92,"<>0")' -> 191.977668724718 | K97: '=AVERAGEIFS(K$3:K$92,$B$3:$B$92,$B97,K$3:K$92,"<>0")' -> 295.502890145071 | L97: '=AVERAGEIFS(L$3:L$92,$B$3:$B$92,$B97,L$3:L$92,"<>0")' -> 208.505453216723

### `d3575a4dff7b|FORMULA_DRIFT|HouseBudget!C10`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/2_CF_22493_input.xlsx`
- location: `House Budget!C10`  severity: High  confidence: Likely defect
- formula: `=C61`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=8): =MONEY IN CHECKING NEXT MONTH!R[2]C[10]
- evidence: This cell: =R[51]C
- cached value: 8128.84; row labels: ["'Total Income'"]; column header: ''; used range: A1:AG123
- neighbourhood: B8: "='Money In Checking Next Month'!L10" -> 'Misc' | C8: "='Money In Checking Next Month'!M10" -> 0 | E8: '=B70' -> 'Burial Insurance (Lincoln ... | B9: "='Money In Checking Next Month'!L11" -> 'Misc' | C9: "='Money In Checking Next Month'!M11" -> 0 | E9: '=B71' -> 'Capital Ona/Walmart' | B10: 'Total Income' | C10: '=C61' -> 8128.84 | E10: '=B72' -> 'Care Credit (Synchrony)' | E11: '=B73' -> 'Comenity Bank (Good Sams)' | E12: '=B74' -> 'Dental Insurane (MetLife)'

### `6c3f8788f84d|FORMULA_DRIFT|Sheet1!U4`

- workbook: `all_data_912_v0.1/spreadsheet/14240/2_14240_input.xlsx`
- location: `Sheet1!U4`  severity: High  confidence: Likely defect
- formula: `=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=71): =SUMPRODUCT((R4C1:R75C1=RC19)*(R4C2:R75C2=R3C)*(R3C3:R3C16=RC20),R4C3:R75C16)
- evidence: This cell: =SUMPRODUCT((RC[-20]:R[71]C[-20]=RC[-3])*(RC[-19]:R[71]C[-19]=RC[-2])*R[-1]C[-18]:R[-1]C[-8],RC[-18]:R[71]C[-8]=RC[-1])
- cached value: '#VALUE!'; row labels: ["'Individual'", "'3M-25yrs'"]; column header: ''; used range: A1:U75
- range A4:A75: values ["'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'"]; beyond: {'above': "A3: '00 To 35'", 'below': 'A76: None'}
- neighbourhood: S3: 'Members' | T3: 'Sum Insured' | S4: 200000 | T4: '3M-25yrs' | U4: '=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)' -> '#VALUE!' | S5: 150000 | T5: '26-40yrs' | U5: '=SUMPRODUCT(($A$4:$A$75=$S5)*($B$4:$B$75=U$3)*($C$3:$P$3=$T5),$C$4... -> 0 | S6: 150000 | T6: '41-45yrs' | U6: '=SUMPRODUCT(($A$4:$A$75=$S6)*($B$4:$B$75=U$3)*($C$3:$P$3=$T6),$C$4... -> 0

### `c5ab9001d952|FORMULA_DRIFT|YTDBudget&Summary!G22`

- workbook: `all_data_912_v0.1/spreadsheet/55392/1_55392_input.xlsx`
- location: `YTD Budget & Summary!G22`  severity: High  confidence: Likely defect
- formula: `=YearToDateTable[[#Totals],[Remaining Rs.]]/YearToDateTable[[#Totals],[Budget]]`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=18): =IFERROR(YEARTODATETABLE[[#THIS ROW],[REMAINING RS.]]/YEARTODATETABLE[[#THIS ROW],[BUDGET]],"")
- evidence: This cell: =YEARTODATETABLE[[#TOTALS],[REMAINING RS.]]/YEARTODATETABLE[[#TOTALS],[BUDGET]]
- cached value: 1; row labels: ["'Total'"]; column header: ''; used range: A1:G22
- neighbourhood: F20: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> None | G20: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> None | F21: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> None | G21: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> None | E22: '=SUBTOTAL(109,YearToDateTable[Budget])' -> 1290000 | F22: '=SUBTOTAL(109,YearToDateTable[Remaining Rs.])' -> 1290000 | G22: '=YearToDateTable[[#Totals],[Remaining Rs.]]/YearToDateTable[[#Tota... -> 1

### `d216c973ba67|FORMULA_DRIFT|Malaga!Q5`

- workbook: `all_data_912_v0.1/spreadsheet/40809/1_40809_input.xlsx`
- location: `Malaga!Q5`  severity: High  confidence: Likely defect
- formula: `=G4`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =R[-2]C[-5]
- evidence: This cell: =R[-1]C[-10]
- cached value: 799; row labels: ["'**SINGLE SUPPLEMENT'", "'Golfer'"]; column header: ''; used range: A1:AJ57
- neighbourhood: O3: '=A3' -> 'Wednesday 11th October to ... | O4: '7 nights All-Inclusive, Transfers, 4... | O5: 'Golfer' | Q5: '=G4' -> 799 | O6: 'Non-Golfer' | Q6: '=L4' -> 449 | O7: '=J5' -> '**SINGLE SUPPLEMENT' | Q7: '=L5' -> 1044

### `e1683f0529fe|FORMULA_DRIFT|HouseBudget!C10`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/3_CF_22493_input.xlsx`
- location: `House Budget!C10`  severity: High  confidence: Likely defect
- formula: `=C61`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=8): =MONEY IN CHECKING NEXT MONTH!R[2]C[10]
- evidence: This cell: =R[51]C
- cached value: 8128.84; row labels: ["'Total Income'"]; column header: ''; used range: A1:AG123
- neighbourhood: B8: "='Money In Checking Next Month'!L10" -> 'Misc' | C8: "='Money In Checking Next Month'!M10" -> 0 | E8: '=B70' -> 'Burial Insurance (Lincoln ... | B9: "='Money In Checking Next Month'!L11" -> 'Misc' | C9: "='Money In Checking Next Month'!M11" -> 0 | E9: '=B71' -> 'Capital Ona/Walmart' | B10: 'Total Income' | C10: '=C61' -> 8128.84 | E10: '=B72' -> 'Care Credit (Synchrony)' | E11: '=B73' -> 'Comenity Bank (Good Sams)' | E12: '=B74' -> 'Dental Insurane (MetLife)'

### `a1e653eaaddb|FORMULA_DRIFT|Sheet1!E9`

- workbook: `all_data_912_v0.1/spreadsheet/38655/2_38655_input.xlsx`
- location: `Sheet1!E9`  severity: High  confidence: Likely defect
- formula: `=+DB($C$4,$C$5,$C$6,E8)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =+DB(R4C3,R5C3,R6C3,R[-1]C,1)
- evidence: This cell: =+DB(R4C3,R5C3,R6C3,R[-1]C)
- cached value: 0; row labels: []; column header: ''; used range: A1:Q12
- neighbourhood: C8: 1 | D8: 2 | E8: 3 | F8: 4 | C9: '=+DB($C$4,$C$5,$C$6,C8,1)' -> 460071.236361904 | D9: '=+DB($C$4,$C$5,$C$6,D8,1)' -> 5060783.59998094 | E9: '=+DB($C$4,$C$5,$C$6,E8)' -> 0

### `88d3a985a51a|FORMULA_DRIFT|Tabelle1!Q17`

- workbook: `all_data_912_v0.1/spreadsheet/42058/1_42058_input.xlsx`
- location: `Tabelle1!Q17`  severity: High  confidence: Likely defect
- formula: `=AVERAGE(E17:P17)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=8): =SUM(RC[-12]:RC[-1])
- evidence: This cell: =AVERAGE(RC[-12]:RC[-1])
- cached value: '#DIV/0!'; row labels: ["'planned'"]; column header: ''; used range: A1:Q18
- range E17:P17: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': "D17: '=AVERAGE(E17:I17)'", 'right': "Q17: '=AVERAGE(E17:P17)'"}
- neighbourhood: O15: 0.35 | P15: 0.4 | Q15: '=SUM(E15:P15)' -> 4.23 | Q16: '=SUM(E16:P16)' -> 1.266 | Q17: '=AVERAGE(E17:P17)' -> '#DIV/0!'

## HARDCODE_IN_FORMULA_BLOCK

### `e5094a660f5e|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D93`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/2_395-48_input.xlsx`
- location: `Sheet1!D93`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D92 and Sheet1!D94, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'PENA BRYAN'", "'HERRERA CRISTOBAL'"]; column header: ''; used range: A1:D302
- neighbourhood: B91: 'RIVERA SANTOS' | C91: 'PAYERAS EDGAR' | D91: '=IF(AND(A91=1,B91=C91),1,"")' -> None | B92: 'LOPEZ DAVID CARLOS' | C92: 'ANTONGEORGI WILLIAM JR' | D92: '=IF(AND(A92=1,B92=C92),1,"")' -> None | B93: 'PENA BRYAN' | C93: 'HERRERA CRISTOBAL' | D93: 1 | D94: '=IF(AND(A94=1,B94=C94),1,"")' -> None | D95: '=IF(AND(A95=1,B95=C95),1,"")' -> None

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!G4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!G4`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!F4 and Sheet1!I4, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: E2: 'MBQ' | F2: 'Diff' | G2: 'Actual' | H2: 'MBQ' | I2: 'Diff' | E3: 2 | F3: '=D3-E3' -> 0 | G3: 1 | H3: 2 | I3: '=G3-H3' -> -1 | E4: 2 | F4: '=D4-E4' -> 1 | G4: 2 | H4: 2 | I4: '=G4-H4' -> 0 | E5: 2 | F5: -1 | G5: 3 | H5: 2 | I5: -1 | E6: 1 | F6: '=D6-E6' -> 4 | G6: 5 | H6: 1 | I6: '=G6-H6' -> 4

### `e5094a660f5e|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D83`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/2_395-48_input.xlsx`
- location: `Sheet1!D83`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D82 and Sheet1!D84, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'RIVERA SANTOS'", "'OROZCO IRVING'"]; column header: ''; used range: A1:D302
- neighbourhood: B81: 'ALVARADO F T' | C81: 'ALVARADO F T' | D81: '=IF(AND(A81=1,B81=C81),1,"")' -> None | B82: 'TERRERO PEDRO M' | C82: 'AYUSO ARMANDO' | D82: '=IF(AND(A82=1,B82=C82),1,"")' -> None | B83: 'RIVERA SANTOS' | C83: 'OROZCO IRVING' | D83: 1 | B84: 'AYUSO ARMANDO' | C84: 'PEREIRA TIAGO' | D84: '=IF(AND(A84=1,B84=C84),1,"")' -> None | B85: 'ESPINOZA ASSAEL' | C85: 'MONROY FRANCISCO' | D85: '=IF(AND(A85=1,B85=C85),1,"")' -> None

### `bc56a9f2824a|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C27`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!C27`  severity: High  confidence: Likely defect
- evidence: Value 2300 sits between Total (2)!C25 and Total (2)!C28, which share the pattern =(RC[-1]*12)/12.
- cached value: 2300; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A25: 18 | B25: 2800 | C25: '=(B25*12)/12' -> 2800 | D25: '=SUM(C25-E25)' -> 1120 | E25: 1680 | A26: 19 | B26: 2400 | C26: 2300 | D26: '=SUM(C26-E26)' -> 1100 | E26: '=SUM(B26*0.5)' -> 1200 | A27: 20 | B27: 2400 | C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | A28: 21 | B28: 2055 | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | A29: 22 | B29: 2300 | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840

### `6116800fac3b|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D4`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/1_395-48_input.xlsx`
- location: `Sheet1!D4`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D3 and Sheet1!D5, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'PENA BRYAN'", "'ALVARADO F T'"]; column header: ''; used range: A1:D302
- neighbourhood: B3: 'OROZCO IRVING' | C3: 'ROMAN EVIN A' | D3: '=IF(AND(A3=1,B3=C3),1,"")' -> None | B4: 'PENA BRYAN' | C4: 'ALVARADO F T' | D4: 1 | B5: 'AMADOR SILVIO RUIZ' | C5: 'AYUSO ARMANDO' | D5: '=IF(AND(A5=1,B5=C5),1,"")' -> None | B6: 'ESPINOZA ASSAEL' | C6: 'ROMAN EVIN A' | D6: '=IF(AND(A6=1,B6=C6),1,"")' -> None

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!F5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!F5`  severity: High  confidence: Likely defect
- evidence: Value -1 sits between Sheet1!F4 and Sheet1!F6, which share the pattern =RC[-2]-RC[-1].
- cached value: -1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: D3: 2 | E3: 2 | F3: 1 | G3: 1 | H3: 2 | D4: 3 | E4: 2 | F4: '=D4-E4' -> 1 | G4: 2 | H4: 2 | D5: 1 | E5: 2 | F5: -1 | G5: 3 | H5: 2 | D6: 5 | E6: 1 | F6: '=D6-E6' -> 4 | G6: 5 | H6: 1 | D7: 2 | E7: 3 | F7: '=D7-E7' -> -1 | G7: 2 | H7: 3

### `09478d797a42|HARDCODE_IN_FORMULA_BLOCK|BankBalance!C4`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Bank Balance!C4`  severity: High  confidence: Likely defect
- evidence: Value 2000 sits between Bank Balance!C3 and Bank Balance!C5, which share the pattern =IF(AND(JOURNAL ENTRIES!R[3]C8="debit",JOURNAL ENTRIES!R[3]C5=BANK BALANCE!R2C),JOURNAL ENTRIES!R[3]C6,"").
- cached value: 2000; row labels: []; column header: ''; used range: A1:AL3000
- neighbourhood: A2: 'Date' | B2: 'Ref/Invoice/Cheque No.' | C2: 'Document Charges' | D2: 'Loan Capital Recovery' | E2: 'Loan Interest Recovery' | A3: "=+'Journal Entries'!B6" -> 2021-03-21 00:00:00 | B3: "=+'Journal Entries'!I6" -> 'N/A' | C3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> 2000 | D3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> None | E3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> None | A4: "=+'Journal Entries'!B7" -> 2021-03-21 00:00:00 | B4: "=+'Journal Entries'!I7" -> 456798 | C4: 2000 | D4: '=IF(AND(\'Journal Entries\'!$H7="debit",\'Journal Entries\'!$E7=\'... -> None | E4: '=IF(AND(\'Journal Entries\'!$H7="debit",\'Journal Entries\'!$E7=\'... -> None | A5: "=+'Journal Entries'!B8" -> 2021-03-26 00:00:00 | B5: "=+'Journal Entries'!I8" -> 0 | C5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | D5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | E5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | A6: "=+'Journal Entries'!B9" -> 2021-03-26 00:00:00 | B6: "=+'Journal Entries'!I9" -> 0 | C6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None | D6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None | E6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!Q4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!Q4`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!O4 and Sheet1!R4, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: O2: 'Diff' | P2: 'Actual' | Q2: 'MBQ' | R2: 'Diff' | O3: '=M3-N3' -> 0 | P3: 2 | Q3: 2 | R3: '=P3-Q3' -> 0 | O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0

### `b495a5e6f4d1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!T3`

- workbook: `all_data_912_v0.1/spreadsheet/57354/2_57354_input.xlsx`
- location: `Sheet1!T3`  severity: High  confidence: Likely defect
- evidence: Value 29868 sits between Sheet1!Q3 and Sheet1!U3, which share the pattern =RC[-1]-RC[-3].
- cached value: 29868; row labels: ["'a'"]; column header: "'REVENUE'"; used range: A1:U11
- neighbourhood: R1: 2020-06-01 00:00:00 | R2: 'SPEND' | S2: 'SALES' | T2: 'REVENUE' | U2: 'GP' | R3: 23225.96 | S3: 528 | T3: 29868 | U3: '=T3-R3' -> 6642.04

### `711b43c06db1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!T3`

- workbook: `all_data_912_v0.1/spreadsheet/57354/1_57354_input.xlsx`
- location: `Sheet1!T3`  severity: High  confidence: Likely defect
- evidence: Value 29868 sits between Sheet1!Q3 and Sheet1!U3, which share the pattern =RC[-1]-RC[-3].
- cached value: 29868; row labels: ["'a'"]; column header: "'REVENUE'"; used range: A1:U11
- neighbourhood: R1: 2020-06-01 00:00:00 | R2: 'SPEND' | S2: 'SALES' | T2: 'REVENUE' | U2: 'GP' | R3: 23225.96 | S3: 528 | T3: 29868 | U3: '=T3-R3' -> 6642.04

### `643562b8c3e5|HARDCODE_IN_FORMULA_BLOCK|Sheet1!H9`

- workbook: `all_data_912_v0.1/spreadsheet/33094/1_33094_input.xlsx`
- location: `Sheet1!H9`  severity: High  confidence: Likely defect
- evidence: Value 6 sits between Sheet1!H8 and Sheet1!H10, which share the pattern =R[-1]C/R7C2.
- cached value: 6; row labels: ["'Employee3'"]; column header: ''; used range: A1:Z10
- neighbourhood: F7: 25 | G7: 25 | H7: 25 | I7: 17 | J7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!O$4:O$1000)' -> 0 | F8: '=F7/$B$7' -> 0.625 | G8: '=G7/$B$7' -> 0.625 | H8: '=H7/$B$7' -> 0.625 | I8: '=I7/$B$7' -> 0.425 | J8: '=J7/$B$7' -> 0 | F9: 8 | G9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)' -> 0 | H9: 6 | I9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!N$4:N$1000)' -> 0 | J9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!O$4:O$1000)' -> 0 | F10: '=F9/$B$7' -> 0.2 | G10: '=G9/$B$7' -> 0 | H10: '=H9/$B$7' -> 0.15 | I10: '=I9/$B$7' -> 0 | J10: '=J9/$B$7' -> 0

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!P4`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!O4 and Sheet1!R4, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: N2: 'MBQ' | O2: 'Diff' | P2: 'Actual' | Q2: 'MBQ' | R2: 'Diff' | N3: 2 | O3: '=M3-N3' -> 0 | P3: 2 | Q3: 2 | R3: '=P3-Q3' -> 0 | N4: 2 | O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | N5: 6 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | N6: 0 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0

### `3a2b74c70f66|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C16`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!C16`  severity: High  confidence: Likely defect
- evidence: Value 1400 sits between Total (2)!C15 and Total (2)!C17, which share the pattern =(RC[-1]*12)/12.
- cached value: 1400; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A14: 7 | B14: 2100 | C14: '=(B14*12)/12' -> 2100 | D14: '=SUM(C14-E14)' -> 1050 | E14: 1050 | A15: 8 | B15: 1800 | C15: '=(B15*12)/12' -> 1800 | D15: '=SUM(C15-E15)' -> 360 | E15: 1440 | A16: 9 | B16: 2600 | C16: 1400 | D16: '=SUM(C16-E16)' -> 560 | E16: 840 | A17: 10 | B17: 1700 | C17: '=(B17*12)/12' -> 1700 | D17: '=SUM(C17-E17)' -> 680 | E17: 1020 | A18: 11 | B18: 1674 | C18: '=(B18*12)/12' -> 1674 | D18: '=SUM(C18-E18)' -> 669.6 | E18: 1004.4

### `5ec32da9071e|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C26`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!C26`  severity: High  confidence: Likely defect
- evidence: Value 2300 sits between Total (2)!C25 and Total (2)!C28, which share the pattern =(RC[-1]*12)/12.
- cached value: 2300; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A24: 17 | B24: 2400 | C24: '=(B24*12)/12' -> 2400 | D24: '=SUM(C24-E24)' -> 960 | E24: 1440 | A25: 18 | B25: 2800 | C25: '=(B25*12)/12' -> 2800 | D25: '=SUM(C25-E25)' -> 1120 | E25: 1680 | A26: 19 | B26: 2400 | C26: 2300 | D26: '=SUM(C26-E26)' -> 1100 | E26: '=SUM(B26*0.5)' -> 1200 | A27: 20 | B27: 2400 | C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | A28: 21 | B28: 2055 | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!M4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!M4`  severity: High  confidence: Likely defect
- evidence: Value 3 sits between Sheet1!L4 and Sheet1!O4, which share the pattern =RC[-2]-RC[-1].
- cached value: 3; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: K2: 'MBQ' | L2: 'Diff' | M2: 'Actual' | N2: 'MBQ' | O2: 'Diff' | K3: 2 | L3: '=J3-K3' -> 0 | M3: 2 | N3: 2 | O3: '=M3-N3' -> 0 | K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | O4: '=M4-N4' -> 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | O5: -1 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | O6: '=M6-N6' -> 5

### `8b7bb50b3697|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C30`

- workbook: `all_data_912_v0.1/spreadsheet/35207/2_35207_input.xlsx`
- location: `Sheet1!C30`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/29/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A28: '1/27/1890' | B28: 0.0141 | A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899

### `5ec32da9071e|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C27`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!C27`  severity: High  confidence: Likely defect
- evidence: Value 2300 sits between Total (2)!C25 and Total (2)!C28, which share the pattern =(RC[-1]*12)/12.
- cached value: 2300; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A25: 18 | B25: 2800 | C25: '=(B25*12)/12' -> 2800 | D25: '=SUM(C25-E25)' -> 1120 | E25: 1680 | A26: 19 | B26: 2400 | C26: 2300 | D26: '=SUM(C26-E26)' -> 1100 | E26: '=SUM(B26*0.5)' -> 1200 | A27: 20 | B27: 2400 | C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | A28: 21 | B28: 2055 | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | A29: 22 | B29: 2300 | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840

### `8b7bb50b3697|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C31`

- workbook: `all_data_912_v0.1/spreadsheet/35207/2_35207_input.xlsx`
- location: `Sheet1!C31`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/30/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899 | A33: '2/1/1890' | B33: 0.0001807 | C33: 0

### `70f5a8fe58e1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C31`

- workbook: `all_data_912_v0.1/spreadsheet/35207/1_35207_input.xlsx`
- location: `Sheet1!C31`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/30/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899 | A33: '2/1/1890' | B33: 0.0001807 | C33: 0

### `2ed80e0ee4cd|HARDCODE_IN_FORMULA_BLOCK|DRP!N20`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!N20`  severity: High  confidence: Likely defect
- evidence: Value 12 sits between DRP!L20 and DRP!O20, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 12; row labels: ["'RRM1'", "'CV1'"]; column header: ''; used range: A1:O23
- neighbourhood: L18: '=I18+J18-K18' -> None | O18: '=L18+M18-N18' -> None | L19: '=I19+J19-K19' -> None | M19: 10 | O19: '=L19+M19-N19' -> None | L20: '=I20+J20-K20' -> None | N20: 12 | O20: '=L20+M20-N20' -> None | L21: '=I21+J21-K21' -> None | O21: '=L21+M21-N21' -> None | L22: '=I22+J22-K22' -> None | O22: '=L22+M22-N22' -> None

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!L5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!L5`  severity: High  confidence: Likely defect
- evidence: Value -1 sits between Sheet1!L4 and Sheet1!L6, which share the pattern =RC[-2]-RC[-1].
- cached value: -1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: J3: 2 | K3: 2 | L3: '=J3-K3' -> 0 | M3: 2 | N3: 2 | J4: 3 | K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | J5: 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | J7: 2 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3

### `f5521bffa45f|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D53`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D53`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D52 and Sheet1!D55, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'DURAN F'", "'ALVARADO F T'"]; column header: ''; used range: A1:D302
- neighbourhood: B51: 'RIVERA SANTOS' | C51: 'ROMAN EVIN A' | D51: '=IF(AND(A51=1,B51=C51),1,"")' -> None | B52: 'ANTONGEORGI WILLIAM JR' | C52: 'MARTINEZ CATALINO' | D52: '=IF(AND(A52=1,B52=C52),1,"")' -> None | B53: 'DURAN F' | C53: 'ALVARADO F T' | D53: 1 | B54: 'ALVARADO F T' | B55: 'LOPEZ DAVID CARLOS' | D55: '=IF(AND(A55=1,B55=C55),1,"")' -> None

### `f5521bffa45f|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D48`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D48`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D47 and Sheet1!D49, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'MARTINEZ CATALINO'", "'BRAVO J'"]; column header: ''; used range: A1:D302
- neighbourhood: B46: 'TERRERO PEDRO M' | C46: 'TERRERO PEDRO M' | D46: '=IF(AND(A46=1,B46=C46),1,"")' -> None | B47: 'PENA BRYAN' | C47: 'PENA BRYAN' | D47: '=IF(AND(A47=1,B47=C47),1,"")' -> None | B48: 'MARTINEZ CATALINO' | C48: 'BRAVO J' | D48: 1 | B49: 'MONROY FRANCISCO' | C49: 'FREY KYLE' | D49: '=IF(AND(A49=1,B49=C49),1,"")' -> None | B50: 'MONROY FRANCISCO' | C50: 'MONROY FRANCISCO' | D50: '=IF(AND(A50=1,B50=C50),1,"")' -> None

### `6d6fc1caeb06|HARDCODE_IN_FORMULA_BLOCK|DRP!N20`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/1_175-10_input.xlsx`
- location: `DRP!N20`  severity: High  confidence: Likely defect
- evidence: Value 12 sits between DRP!L20 and DRP!O20, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 12; row labels: ["'RRM1'", "'CV1'"]; column header: ''; used range: A1:O23
- neighbourhood: L18: '=I18+J18-K18' -> None | O18: '=L18+M18-N18' -> None | L19: '=I19+J19-K19' -> None | M19: 10 | O19: '=L19+M19-N19' -> None | L20: '=I20+J20-K20' -> None | N20: 12 | O20: '=L20+M20-N20' -> None | L21: '=I21+J21-K21' -> None | O21: '=L21+M21-N21' -> None | L22: '=I22+J22-K22' -> None | O22: '=L22+M22-N22' -> None

### `b495a5e6f4d1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!S3`

- workbook: `all_data_912_v0.1/spreadsheet/57354/2_57354_input.xlsx`
- location: `Sheet1!S3`  severity: High  confidence: Likely defect
- evidence: Value 528 sits between Sheet1!Q3 and Sheet1!U3, which share the pattern =RC[-1]-RC[-3].
- cached value: 528; row labels: ["'a'"]; column header: "'SALES'"; used range: A1:U11
- neighbourhood: R1: 2020-06-01 00:00:00 | Q2: 'GP' | R2: 'SPEND' | S2: 'SALES' | T2: 'REVENUE' | U2: 'GP' | Q3: '=P3-N3' -> 6406 | R3: 23225.96 | S3: 528 | T3: 29868 | U3: '=T3-R3' -> 6642.04

## HIDDEN_STRUCTURE_IN_TOTAL

### `a3ce241a69c4|HIDDEN_STRUCTURE_IN_TOTAL|Admin&Settings!U5`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/3_118-8_input.xlsx`
- location: `Admin & Settings!U5`  severity: Medium  confidence: Review
- formula: `=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*7)+T5-WEEKDAY(DATE(Schedule!$B$6,Q5,1))+IF(T5<WEEKDAY(DATE(Schedule!$B$6,Q5,1)),7,0))`
- evidence: Hidden column B on Schedule feeds 70 visible formula(s): Admin & Settings!U5, Admin & Settings!U6, Admin & Settings!U7, Admin & Settings!U8, Admin & Settings!U9, Admin & Settings!U10, Admin & Settings!U11, Admin & Settings!U12, ....
- cached value: 2023-01-16 00:00:00; row labels: ["'Duration'", "'ML King Day'"]; column header: "'Date'"; used range: A1:X80
- neighbourhood: S4: 'Week' | T4: 'Weekday' | U4: 'Date' | V4: 'When / Notes' | S5: 3 | T5: 2 | U5: '=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*... -> 2023-01-16 00:00:00 | V5: 'January 1' | S6: 3 | T6: 2 | U6: '=IF(OR(OR(Q6="",S6=""),T6=""),"",(DATE(Schedule!$B$6,Q6,1)+(S6-1)*... -> 2023-02-20 00:00:00 | V6: 'The 3rd Monday in January' | S7: 2 | T7: 1 | U7: '=IF(OR(OR(Q7="",S7=""),T7=""),"",(DATE(Schedule!$B$6,Q7,1)+(S7-1)*... -> 2023-05-14 00:00:00 | V7: '2nd Sunday in May'

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|c9282e`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column V on formamspnc (7) feeds 103 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!O6, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> '1' | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> None

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!BF5|19187f`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!BF5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column Z on formamspnc (7) feeds 100 visible formula(s): formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: "'m3'"; used range: A1:ED48610
- range P5:AB5: values ['None', 'None', "'1 ext,1st 1 ext'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'O5: \'=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A",...', 'right': 'AC5: None'}
- neighbourhood: BD3: 'm1' | BE3: 'm2' | BF3: 'm3' | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BH3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),2) {array BH3}' -> '#NUM!' | BD5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(L5:Z5,L$1+{1,0,-1}),{1,0,-1}),"") ... -> None | BE5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")... -> None | BF5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")... -> None | BD6: '=SUM(AE6:AO6)' -> 3 | BE6: '=SUM(AE6:AP6)' -> 3 | BF6: '=SUM(AE6:AQ6)' -> 4 | BG6: '=IF(COUNTIF(AT6:AY6,0)>2,"a","")' -> None | BH6: 'e' | BD7: '=SUM(AE7:AO7)' -> 2 | BE7: '=SUM(AE7:AP7)' -> 2 | BF7: '=SUM(AE7:AQ7)' -> 3 | BG7: '=IF(COUNTIF(AT7:AY7,0)>2,"a","")' -> 'a' | BH7: '=IF(OR(BF7=0,BE7=0),"e",IF(OR(AND(BE7=0,BF7=0),AND(BD7=0,BE7=0)),"... -> 'b'

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22, 23, 24, 25, 26, 27, 28, 29 and 469 more on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CP5|e422d0`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!CP5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden columns AZ, BA, BB, BC, BD, BE on formamspnc (7) feed 20 visible formula(s): formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, formamspnc (7)!CW5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AF5:BJ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AE5: None', 'right': "BK5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:A..."}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CR5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AH5:BL5,AH$1+{1,0,-1}),{1,0,-1}),"... -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `ac9c457a4aed|HIDDEN_STRUCTURE_IN_TOTAL|Compiledandlocatedschoolsda!B2`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!B2`  severity: Medium  confidence: Review
- formula: `=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$1461,0))`
- evidence: Hidden rows 2, 3, 4, 5, 6, 7, 8, 9 and 1451 more on URN lookup feed 12 visible formula(s): Compiled and located schools da!B2, Compiled and located schools da!B3, Compiled and located schools da!B4, Compiled and located schools da!B5, Compiled and located schools da!B6, Compiled and located schools da!B7, Compiled and located schools da!B8, Compiled and located schools da!B9, ....
- cached value: '#N/A'; row labels: []; column header: "'DFES check'"; used range: A1:AJ1419
- range 'URN lookup'!$D$2:$D$1461: values ['2001', '2004', '2005', '2008', '2010', '2014', '2019', '2020', '2027', '2028', '2032', '2033']; beyond: {'above': "D1: 'ESTAB'", 'below': 'D1462: None'}
- neighbourhood: A1: 'URN' | B1: 'DFES check' | C1: 'DfE Number' | D1: 'County' | B2: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$146... -> '#N/A' | D2: 'Cumbria' | B3: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L3,'URN lookup'!$K$2:$K$146... -> '#N/A' | D3: 'Cumbria' | B4: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L4,'URN lookup'!$K$2:$K$146... -> '#N/A' | D4: 'Cumbria'

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|b6cb85`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AF on formamspnc (7) feeds 68 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, formamspnc (7)!BQ5, formamspnc (7)!BR5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> None | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> None

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!BV5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!BV5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AD5:AP5,AD$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AP on formamspnc (7) feeds 31 visible formula(s): formamspnc (7)!BV5, formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AD5:AP5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AC5: None', 'right': 'AQ5: None'}
- neighbourhood: BT5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AB5:AN5,AB$1+{1,0,-1}),{1,0,-1}),"... -> None | BU5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AC5:AO5,AC$1+{1,0,-1}),{1,0,-1}),"... -> None | BV5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AD5:AP5,AD$1+{1,0,-1}),{1,0,-1}),"... -> None | BT6: '=IF(IF(ISBLANK(AB$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-AB... -> 0 | BU6: '=IF(IF(ISBLANK(AC$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-AC... -> -1 | BV6: '=IF(IF(ISBLANK(AD$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-AD... -> 3 | BW6: '=IF(IF(ISBLANK(AE$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-AE... -> None | BX6: '=BJ6' -> 0 | BT7: '=IF(IF(ISBLANK(AB$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-AB... -> 1 | BU7: '=IF(IF(ISBLANK(AC$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-AC... -> 0 | BV7: '=IF(IF(ISBLANK(AD$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-AD... -> -1 | BW7: '=IF(IF(ISBLANK(AE$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-AE... -> 3 | BX7: '=BJ7' -> 1

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|c96edb`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AN on formamspnc (7) feeds 62 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BT5, formamspnc (7)!BU5, formamspnc (7)!BV5, formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> None | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> '1'

### `b55280430702|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25`

- workbook: `all_data_912_v0.1/spreadsheet/57989/3_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden rows 12, 17 on Sheet1 feed 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, ....
- cached value: 0; row labels: ["'Driver 19'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 19' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 15' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 16' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `ef479c030de6|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|61d632`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AY on Sheet1 feeds 20 visible formula(s): Sheet1!D4, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, Sheet1!D8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `158be0e0e878|HIDDEN_STRUCTURE_IN_TOTAL|Employee3!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/1_382-29_input.xlsx`
- location: `Employee 3!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden row 23 on Employee 3 feeds 24 visible formula(s): Employee 3!U3, Employee 3!AB5, Employee 3!AB6, Employee 3!AB7, Employee 3!AB8, Employee 3!AB9, Employee 3!AB10, Employee 3!AB11, ....
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `fd82a768c064|HIDDEN_STRUCTURE_IN_TOTAL|Employee2!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/3_382-29_input.xlsx`
- location: `Employee 2!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden row 23 on Employee 2 feeds 24 visible formula(s): Employee 2!U3, Employee 2!AB5, Employee 2!AB6, Employee 2!AB7, Employee 2!AB8, Employee 2!AB9, Employee 2!AB10, Employee 2!AB11, ....
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `ea1e0839ce78|HIDDEN_STRUCTURE_IN_TOTAL|Here!A2`

- workbook: `all_data_912_v0.1/spreadsheet/58114/2_58114_input.xlsx`
- location: `Here!A2`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!A2="","",Sheet1!A2)`
- evidence: Hidden sheet 'Sheet1' feeds 834 visible formula(s): Here!A2, Here!B2, Here!C2, Here!D2, Here!E2, Here!F2, Here!A3, Here!B3, ....
- cached value: 1; row labels: []; column header: "'#'"; used range: A1:J140
- neighbourhood: A1: '#' | B1: 'ID' | C1: 'First Name' | A2: '=IF(Sheet1!A2="","",Sheet1!A2)' -> 1 | B2: '=IF(Sheet1!B2="","",Sheet1!B2)' -> 'TA32785655' | C2: '=IF(Sheet1!C2="","",Sheet1!C2)' -> 'Tbnor' | A3: '=IF(Sheet1!A3="","",Sheet1!A3)' -> 2 | B3: '=IF(Sheet1!B3="","",Sheet1!B3)' -> 'SA12442673' | C3: '=IF(Sheet1!C3="","",Sheet1!C3)' -> 'Abo' | A4: '=IF(Sheet1!A4="","",Sheet1!A4)' -> 3 | B4: '=IF(Sheet1!B4="","",Sheet1!B4)' -> 'AA21259159' | C4: '=IF(Sheet1!C4="","",Sheet1!C4)' -> 'Tbra'

### `6fd6aa9b279e|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!Q3`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `Sheet1!Q3`  severity: Medium  confidence: Review
- formula: `=M3`
- evidence: Hidden column M on Sheet1 feeds 999 visible formula(s): Sheet1!Q3, Sheet1!Q4, Sheet1!Q5, Sheet1!Q6, Sheet1!Q7, Sheet1!Q8, Sheet1!Q9, Sheet1!Q10, ....
- cached value: 'MOHAK'; row labels: ["'90*100'", "'STITCHING'"]; column header: "'BY WHOM'"; used range: A1:Y1001
- neighbourhood: P1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" PRESS BILL")' -> 'OCTOBER-2021 PRESS BILL' | O2: 'DATE' | P2: 'PARTY NAME' | Q2: 'BY WHOM' | R2: 'CH. NO.' | S2: 'QUALITY' | O3: '=A3' -> 2021-10-02 00:00:00 | P3: '=B3' -> 'STORE' | Q3: '=M3' -> 'MOHAK' | R3: '=C3' -> 1055 | S3: '=E3' -> 0 | O4: '=A4' -> 2021-10-02 00:00:00 | P4: '=B4' -> 'STORE' | Q4: '=M4' -> 'MOHAK' | R4: '=C4' -> 1055 | S4: '=E4' -> 'NEW NAKSHI' | O5: '=A5' -> 2021-10-02 00:00:00 | P5: '=B5' -> 'STORE' | Q5: '=M5' -> 'MOHAK' | R5: '=C5' -> 1055 | S5: '=E5' -> 'NEW NAKSHI'

### `a556b2a52595|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|61d632`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AY on Sheet1 feeds 20 visible formula(s): Sheet1!D4, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, Sheet1!D8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `fd82a768c064|HIDDEN_STRUCTURE_IN_TOTAL|Employee3!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/3_382-29_input.xlsx`
- location: `Employee 3!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden row 23 on Employee 3 feeds 24 visible formula(s): Employee 3!U3, Employee 3!AB5, Employee 3!AB6, Employee 3!AB7, Employee 3!AB8, Employee 3!AB9, Employee 3!AB10, Employee 3!AB11, ....
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `d2a515f35dce|HIDDEN_STRUCTURE_IN_TOTAL|Admin&Settings!U5`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Admin & Settings!U5`  severity: Medium  confidence: Review
- formula: `=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*7)+T5-WEEKDAY(DATE(Schedule!$B$6,Q5,1))+IF(T5<WEEKDAY(DATE(Schedule!$B$6,Q5,1)),7,0))`
- evidence: Hidden column B on Schedule feeds 70 visible formula(s): Admin & Settings!U5, Admin & Settings!U6, Admin & Settings!U7, Admin & Settings!U8, Admin & Settings!U9, Admin & Settings!U10, Admin & Settings!U11, Admin & Settings!U12, ....
- cached value: 2023-01-16 00:00:00; row labels: ["'Duration'", "'ML King Day'"]; column header: "'Date'"; used range: A1:X80
- neighbourhood: S4: 'Week' | T4: 'Weekday' | U4: 'Date' | V4: 'When / Notes' | S5: 3 | T5: 2 | U5: '=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*... -> 2023-01-16 00:00:00 | V5: 'January 1' | S6: 3 | T6: 2 | U6: '=IF(OR(OR(Q6="",S6=""),T6=""),"",(DATE(Schedule!$B$6,Q6,1)+(S6-1)*... -> 2023-02-20 00:00:00 | V6: 'The 3rd Monday in January' | S7: 2 | T7: 1 | U7: '=IF(OR(OR(Q7="",S7=""),T7=""),"",(DATE(Schedule!$B$6,Q7,1)+(S7-1)*... -> 2023-05-14 00:00:00 | V7: '2nd Sunday in May'

### `7dfe4964af12|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|eaab5a`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AW on Sheet1 feeds 42 visible formula(s): Sheet1!D4, Sheet1!C5, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `7dfe4964af12|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|61d632`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AY on Sheet1 feeds 20 visible formula(s): Sheet1!D4, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, Sheet1!D8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `7f9746d5c513|HIDDEN_STRUCTURE_IN_TOTAL|EXAMPLE!I13`

- workbook: `all_data_912_v0.1/spreadsheet/58656/3_58656_input.xlsx`
- location: `EXAMPLE!I13`  severity: Medium  confidence: Review
- formula: `=D13-D12`
- evidence: Hidden row 12 on EXAMPLE feeds 2 visible formula(s): EXAMPLE!I13, EXAMPLE!J13.
- cached value: 7; row labels: ["'3'", "'n'"]; column header: ''; used range: A1:K36
- neighbourhood: G11: 'M' | H11: 2021-03-20 11:37:00 | I11: '=D11-D10' -> 8 | J11: '=IF(G11="n","1",J10+I11)' -> 17 | G12: 'G' | H12: 2021-03-20 11:37:00 | I12: '=D12-D11' -> 7 | J12: '=IF(G12="n","1",J11+I12)' -> 24 | G13: 'n' | H13: 2021-03-20 11:37:00 | I13: '=D13-D12' -> 7 | J13: '=IF(G13="n","1",J12+I13)' -> '1' | G14: 'T' | H14: 2021-03-20 11:37:00 | I14: '=D14-D13' -> 8 | J14: '=IF(G14="n","1",J13+I14)' -> 9 | G15: 'M' | H15: 2021-03-20 11:37:00 | I15: '=D15-D14' -> 7 | J15: '=IF(G15="n","1",J14+I15)' -> 16

### `ab88bab5d14b|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H4`

- workbook: `all_data_912_v0.1/spreadsheet/50154/2_50154_input.xlsx`
- location: `Sheet1!H4`  severity: Medium  confidence: Review
- formula: `=SUM(G4,F4)`
- evidence: Hidden columns F, G on Sheet1 feed 11 visible formula(s): Sheet1!H4, Sheet1!H5, Sheet1!H6, Sheet1!H7, Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, ....
- cached value: 7.66666666666667; row labels: ["'Winter Guard #1'", "'Y'"]; column header: "'Final Score'"; used range: A1:O15
- neighbourhood: F3: 'Splash page points' | G3: 'AVG' | H3: 'Final Score' | F4: '=IF(D4="Y",1,0)' -> 1 | G4: '=AVERAGE(B4:C4,E4)' -> 6.66666666666667 | H4: '=SUM(G4,F4)' -> 7.66666666666667 | F5: '=IF(D5="Y",1,0)' -> 0 | G5: '=AVERAGE(B5:C5,E5)' -> 6.33333333333333 | H5: '=SUM(G5,F5)' -> 6.33333333333333 | F6: '=IF(D6="Y",1,0)' -> 1 | G6: '=AVERAGE(B6:C6,E6)' -> 6.66666666666667 | H6: '=SUM(G6,F6)' -> 7.66666666666667

### `3ee4d6f069b6|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!N3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Daily Numbers!N3`  severity: Medium  confidence: Review
- formula: `=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Errors!$B:$B,"="&$B3,Errors!$AB:$AB,"="&$G3,Errors!$AB:$AB,"="&$H3,Errors!$AB:$AB,"="&$I3,Errors!$AB:$AB,"="&$J3)`
- evidence: Hidden rows 2, 3, 4, 5, 6, 7, 8, 9 and 493 more on Errors feed 110 visible formula(s): Daily Numbers!N3, Daily Numbers!O3, Daily Numbers!P3, Daily Numbers!Q3, Daily Numbers!R3, Daily Numbers!N4, Daily Numbers!O4, Daily Numbers!P4, ....
- cached value: 0; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'II'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | P2: 'IT' | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 28599 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | P3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | P4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | P5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `69355e1eb76d|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!N3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Daily Numbers!N3`  severity: Medium  confidence: Review
- formula: `=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Errors!$B:$B,"="&$B3,Errors!$AB:$AB,"="&$G3,Errors!$AB:$AB,"="&$H3,Errors!$AB:$AB,"="&$I3,Errors!$AB:$AB,"="&$J3)`
- evidence: Hidden rows 2, 3, 4, 5, 6, 7, 8, 9 and 493 more on Errors feed 110 visible formula(s): Daily Numbers!N3, Daily Numbers!O3, Daily Numbers!P3, Daily Numbers!Q3, Daily Numbers!R3, Daily Numbers!N4, Daily Numbers!O4, Daily Numbers!P4, ....
- cached value: 0; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'II'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | P2: 'IT' | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | P3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | P4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | P5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `9b7879bd3308|HIDDEN_STRUCTURE_IN_TOTAL|Here!I2`

- workbook: `all_data_912_v0.1/spreadsheet/58147/1_58147_input.xlsx`
- location: `Here!I2`  severity: Medium  confidence: Review
- formula: `=1&" - "&F2`
- evidence: Hidden column F on Here feeds 2 visible formula(s): Here!I2, Here!I6.
- cached value: '1 - Tbnor, Cadigan - TA32785655'; row labels: []; column header: "'Extract'"; used range: A1:J140
- neighbourhood: G1: 'Letter' | H1: 'First Name' | I1: 'Extract' | J1: 'Outcome' | G2: '=LEFT(F2,1)' -> 'T' | H2: '=1&" - "&C2' -> '1 - Tbnor' | I2: '=1&" - "&F2' -> '1 - Tbnor, Cadigan - TA327... | J2: 'Tbnor, Cadigan' | G3: '=LEFT(F3,1)' -> 'A' | H3: '=C4' -> 'Tbra' | I3: 'Tbra, Cadle - AA21259159' | J3: 'Tbra, Cadle' | G4: '=LEFT(F4,1)' -> 'T' | H4: '=C7' -> 'Tbrahame' | I4: 'Tbrahame, Cadogan - LB71531251' | J4: 'Tbrahame, Cadogan'

## IFERROR_MASK

### `95fdf876027b|IFERROR_MASK|RESULTS1!U26`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!U26`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">=10000000",Table1[FLOAT],"<20000000")>=10,AVERAGEIFS(Table1[POINTS],Table1[MARKET CAP],"<100000000",Table1[FLOAT],">=10000000",Table1[FLOAT],"<20000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Profit %'", "'< 100M'"]; column header: "'10-20M'"; used range: A1:X80
- neighbourhood: S25: '3-5M' | T25: '5-10M' | U25: '10-20M' | V25: '20-50M' | W25: '50-100M' | S26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `f97f2feedd64|IFERROR_MASK|RESULTS1!Q22`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!Q22`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=3000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">1000000",Table1[FLOAT],"<=3000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: P20: 'ENTRY' | Q20: '1-3M' | R20: '3-5M' | S20: '5-10M' | P21: '< 100M' | Q21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | P22: '100-500M' | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P23: '500M-1B' | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P24: '1B <' | Q24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `f97f2feedd64|IFERROR_MASK|RESULTS1!Q24`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!Q24`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'> 4 pt'", "'1B <'"]; column header: ''; used range: A1:W67
- neighbourhood: P22: '100-500M' | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P23: '500M-1B' | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P24: '1B <' | Q24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | P26: 'WIN %' | Q26: '1-3M' | R26: '3-5M' | S26: '5-10M'

### `125be9ba2e04|IFERROR_MASK|RESULTS1!U3`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!U3`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5x20",IF(COUNTIFS(Table1[MAX GAIN],R$2)>=5,Table1[POINTS]))),10%),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'All-TIME (5)'"]; column header: "'>= 7'"; used range: A1:X80
- neighbourhood: S2: '>= 5' | T2: '>= 6' | U2: '>= 7' | V2: '>= 8' | W2: '>= 9' | S3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!T8`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!T8`  severity: Medium  confidence: Review
- formula: `=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",Table1[PM MAX GAP],"<100%",Table1[SETUP],$P8),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are RESULTS 1!T9, RESULTS 1!T10, RESULTS 1!T11, RESULTS 1!T12.
- cached value: 0; row labels: ["'PMH'"]; column header: "'75-100%'"; used range: A1:W67
- neighbourhood: R7: '20-50%' | S7: '50-75%' | T7: '75-100%' | U7: '100-150%' | V7: '150-200%' | R8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0 | R9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0 | R10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0

### `5780cbbcbe94|IFERROR_MASK|Calc!C10`

- workbook: `all_data_912_v0.1/spreadsheet/55979/1_55979_input.xlsx`
- location: `Calc!C10`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP($A$10,Supplier_1!A2:D10,3,FALSE),IFERROR(VLOOKUP($A$10,Supplier_2!A2:D10,3,FALSE),IFERROR(VLOOKUP($A$10,Supplier_3!A2:D10,3,FALSE),"")))`
- evidence: Formula uses IFERROR.
- cached value: 25; row labels: ["'A1111107'"]; column header: "'PL-code'"; used range: A1:F10
- range Supplier_1!A2:D10: values ["'A1111101'", "'TEST 1'", '23', '58', "'A1111102'", "'TEST2'", '23', '62', "'A1111103'", "'TEST 3'", '23', '14']; beyond: {}
- neighbourhood: A9: 'ITEM' | B9: 'NAME' | C9: 'PL-code' | D9: 'PRICE' | E9: 'Discount' | A10: 'A1111107' | B10: '=IFERROR(VLOOKUP($A$10,Supplier_1!A2:D10,2,FALSE),IFERROR(VLOOKUP(... -> 'TEST 7' | C10: '=IFERROR(VLOOKUP($A$10,Supplier_1!A2:D10,3,FALSE),IFERROR(VLOOKUP(... -> 25 | D10: '=IFERROR(VLOOKUP($A$10,Supplier_1!A2:D10,4,FALSE),IFERROR(VLOOKUP(... -> 65 | E10: '=IFERROR(VLOOKUP($C$10,Discount_S1!A2:B5,2,FALSE),IFERROR(VLOOKUP(... -> 0.25

### `86bd0c65882c|IFERROR_MASK|Sheet1!K9`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!K9`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($S$2:$S$124,MATCH($A9,$Q$2:$Q124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 82; row labels: []; column header: ''; used range: A1:BE279
- range $S$2:$S$124: values ['75', '76', '91', '78', '79', '87', '85', '82', '81', '88', '75', '76']; beyond: {'above': "S1: 'Age'", 'below': 'S125: None'}
- neighbourhood: J7: '=IFERROR(INDEX($R$2:$R$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 1934-01-27 00:00:00 | K7: '=IFERROR(INDEX($S$2:$S$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 87 | L7: '=IF(K7<85,"75-84",">85")' -> '>85' | M7: '=IFERROR(INDEX($T$2:$T$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 'Male' | J8: '=IFERROR(INDEX($R$2:$R$124,MATCH($A8,$Q$2:$Q124,0)),0)' -> 1935-05-08 00:00:00 | K8: '=IFERROR(INDEX($S$2:$S$124,MATCH($A8,$Q$2:$Q124,0)),0)' -> 85 | L8: '=IF(K8<85,"75-84",">85")' -> '>85' | M8: '=IFERROR(INDEX($T$2:$T$124,MATCH($A8,$Q$2:$Q124,0)),0)' -> 'Male' | J9: '=IFERROR(INDEX($R$2:$R$124,MATCH($A9,$Q$2:$Q124,0)),0)' -> 1938-08-05 00:00:00 | K9: '=IFERROR(INDEX($S$2:$S$124,MATCH($A9,$Q$2:$Q124,0)),0)' -> 82 | L9: '=IF(K9<85,"75-84",">85")' -> '75-84' | M9: '=IFERROR(INDEX($T$2:$T$124,MATCH($A9,$Q$2:$Q124,0)),0)' -> 'Female' | J10: '=IFERROR(INDEX($R$2:$R$124,MATCH($A10,$Q$2:$Q124,0)),0)' -> 1940-01-05 00:00:00 | K10: '=IFERROR(INDEX($S$2:$S$124,MATCH($A10,$Q$2:$Q124,0)),0)' -> 81 | L10: '=IF(K10<85,"75-84",">85")' -> '75-84' | M10: '=IFERROR(INDEX($T$2:$T$124,MATCH($A10,$Q$2:$Q124,0)),0)' -> 'Female' | J11: '=IFERROR(INDEX($R$2:$R$124,MATCH($A11,$Q$2:$Q124,0)),0)' -> 1932-08-05 00:00:00 | K11: '=IFERROR(INDEX($S$2:$S$124,MATCH($A11,$Q$2:$Q124,0)),0)' -> 88 | L11: '=IF(K11<85,"75-84",">85")' -> '>85' | M11: '=IFERROR(INDEX($T$2:$T$124,MATCH($A11,$Q$2:$Q124,0)),0)' -> 'Male'

### `7149679332c0|IFERROR_MASK|RESULTS1!R15`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!R15`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),0)`
- evidence: Formula uses IFERROR.
- cached value: 2; row labels: ["'ANNUALIZED GAIN CALCULATOR'", "'< 100M'"]; column header: "'3-5M'"; used range: A1:W67
- neighbourhood: P14: 'TRADES' | Q14: '1-3M' | R14: '3-5M' | S14: '5-10M' | T14: '10-20M' | P15: '< 100M' | Q15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 1 | R15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 2 | S15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 6 | T15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 3 | P16: '100-500M' | Q16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 3 | R16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | S16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 3 | T16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 5 | P17: '500M-1B' | Q17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | R17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | S17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | T17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!S33`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!S33`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[POINTS G/L],Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Greatest sequence of negative trades'", "'< 100M'"]; column header: "'5-10M'"; used range: A1:W67
- neighbourhood: Q32: '1-3M' | R32: '3-5M' | S32: '5-10M' | T32: '10-20M' | U32: '20-50M' | Q33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `125be9ba2e04|IFERROR_MASK|RESULTS1!V4`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!V4`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5x20",IF((Table1[WEEK]>=MAX(Table1[WEEK])-9),Table1[POINTS]))),10%),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Last 10 Wk '"]; column header: ''; used range: A1:X80
- neighbourhood: T2: '>= 6' | U2: '>= 7' | V2: '>= 8' | W2: '>= 9' | X2: '>= 10' | T3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None | X3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=10,IF(Table1[EXIT REASON]="... -> None | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None | X4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=10,IF(Table1[EXIT REASON]="... -> None | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | W5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF(Table1[EXIT REASON]="5... -> None | X5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=10,IF(Table1[EXIT REASON]="... -> None

### `5cd8c4fe9805|IFERROR_MASK|RESULTS1!W16`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!W16`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: U14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | X15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `95fdf876027b|IFERROR_MASK|RESULTS1!W8`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!W8`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000"),"")`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: ["'Vacation or other days w/ no trading'", "'< 100M'"]; column header: "'50-100M'"; used range: A1:X80
- neighbourhood: U7: '10-20M' | V7: '20-50M' | W7: '50-100M' | X7: '100M <' | U8: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | V8: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | W8: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | X8: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | U9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | V9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | W9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | X9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | U10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | V10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | W10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | X10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0

### `5cd8c4fe9805|IFERROR_MASK|RESULTS1!V22`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!V22`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")>=10,COUNTIFS(Table1[POINTS],">0",Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")/COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: T20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | X21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `506d9df5a3af|IFERROR_MASK|TaskAssesment!A4`

- workbook: `all_data_912_v0.1/spreadsheet/46444/1_46444_input.xlsx`
- location: `Task Assesment!A4`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkDays!$A$2:$A$100000=$B4),ROW([2]tblWorkDays!$D$2:$D$100000)-1,""),ROWS($A$1:$A$1))),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Task Assesment!A5, Task Assesment!A6.
- cached value: 2018-11-09 00:00:00; row labels: []; column header: "'Dates'"; used range: A1:L6
- neighbourhood: A3: 'Dates' | B3: 'Date code' | C3: 'Activity ID' | A4: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B4: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 24 | C4: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 68 | A5: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B5: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 25 | C5: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 69 | A6: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B6: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 25 | C6: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 69

### `6fd6aa9b279e|IFERROR_MASK|PAYMENT!E13`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `PAYMENT!E13`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT SUM(J) WHERE F= '""&$A13&""' AND G= '""&$B13&""' AND H='""&C13&""' AND I='""&D13&""'  LABEL SUM(J)'' ""),"""")"),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: []; column header: ''; used range: A1:L1001
- neighbourhood: E11: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F11: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | E12: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F12: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | E13: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F13: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | E14: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F14: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None

### `552f4c55b2df|IFERROR_MASK|OrderSheetFinal!AI6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!AI6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AI7, Order Sheet Final!AI8, Order Sheet Final!AI9, Order Sheet Final!AI10, Order Sheet Final!AI11, Order Sheet Final!AI12, Order Sheet Final!AI13, Order Sheet Final!AI14, ....
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'C14.1'"; used range: A1:AS37
- neighbourhood: AG4: '=SUM(AG6:AG33)' -> 9 | AH4: '=SUM(AH6:AH33)' -> 0 | AI4: '=SUM(AI6:AI33)' -> 0 | AJ4: '=SUM(AJ6:AJ33)' -> 0 | AK4: '=SUM(AK6:AK33)' -> 0 | AG5: 'C11' | AH5: 'C12' | AI5: 'C14.1' | AJ5: 'C14.2' | AK5: 'D1' | AG6: '=IFERROR(VLOOKUP(B6,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH6: '=IFERROR(VLOOKUP(B6,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI6: "=IFERROR(VLOOKUP(B6,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ6: "=IFERROR(VLOOKUP(B6,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK6: '=IFERROR(VLOOKUP(B6,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AG7: '=IFERROR(VLOOKUP(B7,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH7: '=IFERROR(VLOOKUP(B7,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI7: "=IFERROR(VLOOKUP(B7,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ7: "=IFERROR(VLOOKUP(B7,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK7: '=IFERROR(VLOOKUP(B7,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AG8: '=IFERROR(VLOOKUP(B8,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH8: '=IFERROR(VLOOKUP(B8,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI8: "=IFERROR(VLOOKUP(B8,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ8: "=IFERROR(VLOOKUP(B8,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK8: '=IFERROR(VLOOKUP(B8,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0

### `86bd0c65882c|IFERROR_MASK|Sheet1!J3`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!J3`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($R$2:$R$124,MATCH($A3,$Q$2:$Q124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 1944-04-11 00:00:00; row labels: []; column header: ''; used range: A1:BE279
- range $R$2:$R$124: values ['1946-03-11 00:00:00', '1944-04-11 00:00:00', '1930-06-17 00:00:00', '1942-07-08 00:00:00', '1941-10-15 00:00:00', '1934-01-27 00:00:00', '1935-05-08 00:00:00', '1938-08-05 00:00:00', '1940-01-05 00:00:00', '1932-08-05 00:00:00', '1945-04-08 00:00:00', '1944-06-26 00:00:00']; beyond: {'above': "R1: 'Date of Birth'", 'below': 'R125: None'}
- neighbourhood: H1: 'ICU > 3 Days ( GERI ICU TRANSFER)' | I1: 'High Risk ( MANUAL INPUT )' | J1: 'Date of Birth  ( GERIATRIC SURG LOG ... | K1: 'Age  ( GERIATRIC SURG LOG W)  ' | L1: 'Age range ( CALCULATION)' | J2: '=IFERROR(INDEX($R$2:$R$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 1946-03-11 00:00:00 | K2: '=IFERROR(INDEX($S$2:$S$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 75 | L2: '=IF(K2<85,"75-84",">85")' -> '75-84' | J3: '=IFERROR(INDEX($R$2:$R$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 1944-04-11 00:00:00 | K3: '=IFERROR(INDEX($S$2:$S$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 76 | L3: '=IF(K3<85,"75-84",">85")' -> '75-84' | J4: '=IFERROR(INDEX($R$2:$R$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 1930-06-17 00:00:00 | K4: '=IFERROR(INDEX($S$2:$S$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 91 | L4: '=IF(K4<85,"75-84",">85")' -> '>85' | J5: '=IFERROR(INDEX($R$2:$R$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 1942-07-08 00:00:00 | K5: '=IFERROR(INDEX($S$2:$S$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 78 | L5: '=IF(K5<85,"75-84",">85")' -> '75-84'

### `bbedb77c52c6|IFERROR_MASK|Foglio1!A8`

- workbook: `all_data_912_v0.1/spreadsheet/239-15/3_239-15_input.xlsx`
- location: `Foglio1!A8`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(B8<>"",A7+1,""),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 50 cells on this sheet; the others are Foglio1!A9, Foglio1!A10, Foglio1!A11, Foglio1!A12, Foglio1!A13, Foglio1!A14, Foglio1!A15, Foglio1!A16, ....
- cached value: 2; row labels: []; column header: ''; used range: A1:R57
- neighbourhood: B6: 'date' | A7: 1 | B7: 2022-06-20 00:00:00 | A8: '=IFERROR(IF(B8<>"",A7+1,""),"")' -> 2 | B8: 2022-02-02 00:00:00 | A9: '=IFERROR(IF(B9<>"",A8+1,""),"")' -> 3 | B9: 2022-08-08 00:00:00 | A10: '=IFERROR(IF(B10<>"",A9+1,""),"")' -> 4 | B10: 2022-09-09 00:00:00

### `15704c37deb1|IFERROR_MASK|Sheet1!E2`

- workbook: `all_data_912_v0.1/spreadsheet/59791/3_59791_input.xlsx`
- location: `Sheet1!E2`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(LEFT(K2,6)="Closed","N/A - Closed Position",IF(OR(K2="",K2="RF"),SUM(D2*ROUND(H2,2),K2),"N/A - Check Row Inputs")),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Sheet1!E3, Sheet1!E4.
- cached value: 2.1939; row labels: []; column header: "'Current Profit/Loss'"; used range: A1:L4
- neighbourhood: C1: 'Current Price' | D1: 'Current Points' | E1: 'Current Profit/Loss' | F1: 'Latest Stop' | G1: 'Stop Distance' | C2: 500 | D2: '=IF(LEN(K2)>2,"NA - Closed Position",IF(I2="Long",C2-A2,A2-C2))' -> 73.13 | E2: '=IFERROR(IF(LEFT(K2,6)="Closed","N/A - Closed Position",IF(OR(K2="... -> 2.1939 | G2: 72.03 | C3: 1010 | D3: '=IF(LEN(K3)>2,"NA - Closed Position",IF(I3="Long",C3-A3,A3-C3))' -> -51 | E3: '=IFERROR(IF(LEFT(K3,6)="Closed","N/A - Closed Position",IF(OR(K3="... -> -59.16 | G3: 172 | C4: 265 | D4: '=IF(LEN(K4)>2,"NA - Closed Position",IF(I4="Long",C4-A4,A4-C4))' -> -18.8 | E4: '=IFERROR(IF(LEFT(K4,6)="Closed","N/A - Closed Position",IF(OR(K4="... -> -0.564 | G4: 6356

### `5a98e72c8ee6|IFERROR_MASK|JournalEntries!E39`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Journal Entries!E39`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(H39,Sheet1!B34:C73,2,0),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 10 cells on this sheet; the others are Journal Entries!E40, Journal Entries!E41, Journal Entries!E42, Journal Entries!E43, Journal Entries!E44, Journal Entries!E45, Journal Entries!E46, Journal Entries!E47, ....
- cached value: None; row labels: []; column header: ''; used range: A1:R3000
- range Sheet1!B34:C73: values ["'Third Party Loans '", "'WG/CR/033'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {}
- neighbourhood: C37: '=IFERROR(VLOOKUP($E37,Sheet1!$B$2:$C$96,2,0),"")' -> None | D37: '=IFERROR(VLOOKUP($E37,Sheet1!$B$2:$D$96,3,0),"")' -> None | E37: '=IFERROR(VLOOKUP(H37,Sheet1!B34:C71,2,0),"")' -> None | C38: '=IFERROR(VLOOKUP($E38,Sheet1!$B$2:$C$96,2,0),"")' -> None | D38: '=IFERROR(VLOOKUP($E38,Sheet1!$B$2:$D$96,3,0),"")' -> None | E38: '=IFERROR(VLOOKUP(H38,Sheet1!B34:C72,2,0),"")' -> None | C39: '=IFERROR(VLOOKUP($E39,Sheet1!$B$2:$C$96,2,0),"")' -> None | D39: '=IFERROR(VLOOKUP($E39,Sheet1!$B$2:$D$96,3,0),"")' -> None | E39: '=IFERROR(VLOOKUP(H39,Sheet1!B34:C73,2,0),"")' -> None | C40: '=IFERROR(VLOOKUP($E40,Sheet1!$B$2:$C$96,2,0),"")' -> None | D40: '=IFERROR(VLOOKUP($E40,Sheet1!$B$2:$D$96,3,0),"")' -> None | E40: '=IFERROR(VLOOKUP(H40,Sheet1!B35:C74,2,0),"")' -> None | C41: '=IFERROR(VLOOKUP($E41,Sheet1!$B$2:$C$96,2,0),"")' -> None | D41: '=IFERROR(VLOOKUP($E41,Sheet1!$B$2:$D$96,3,0),"")' -> None | E41: '=IFERROR(VLOOKUP(H41,Sheet1!B36:C75,2,0),"")' -> None

### `40397a4736e1|IFERROR_MASK|Test!D3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!D3`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 56 cells on this sheet; the others are Test!D4, Test!D5, Test!D6, Test!D7, Test!D8, Test!D9, Test!D10, Test!D11, ....
- cached value: 'AAA'; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: B3: 'PRG/FLY' | C3: 1010 | D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | B4: 'FLY' | C4: 1015 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | B5: 'FLY' | C5: 1013 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None

### `7149679332c0|IFERROR_MASK|RESULTS1!U28`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!U28`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")/COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Wins'", "'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: S26: '5-10M' | T26: '10-20M' | U26: '20-50M' | V26: '50-100M' | W26: '100M <' | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> 0.8125

### `2bdd3699e805|IFERROR_MASK|INPUTS!G15`

- workbook: `all_data_912_v0.1/spreadsheet/52216/2_52216_input.xlsx`
- location: `INPUTS!G15`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),MATCH(INPUTS!G3,Sheet2!C1:G1,0)),0)`
- evidence: Formula uses IFNA.
- cached value: 0.88; row labels: ["'Advertising & Marketing'"]; column header: ''; used range: A1:L23
- range Sheet2!C3:G20: values ['3.5', '3.17', '4.28', '4.29', '0.88', '1.24', '1.8', '1.78', '1.4', '1.72', '2.56', '2.53']; beyond: {}
- neighbourhood: E15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 4.28 | F15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 4.29 | G15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 0.88 | E16: '=_xlfn.IFNA(INDEX(Sheet2!E3:I20,MATCH(INPUTS!C14,Sheet2!C3:C20,0),... -> 0 | F16: '=_xlfn.IFNA(INDEX(Sheet2!F3:J20,MATCH(INPUTS!D14,Sheet2!D3:D20,0),... -> 0 | G16: '=_xlfn.IFNA(INDEX(Sheet2!G3:K20,MATCH(INPUTS!E14,Sheet2!E3:E20,0),... -> 0

### `d2a515f35dce|IFERROR_MASK|InvoiceTemplate!O8`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Invoice Template!O8`  severity: Medium  confidence: Review
- formula: `=IFERROR(J5+O7,"")`
- evidence: Formula uses IFERROR.
- cached value: 2023-04-30 00:00:00; row labels: ["'Due Date'"]; column header: ''; used range: A1:AQ50
- neighbourhood: N6: 'Labor Rate' | O6: 40 | N7: 'Term (days)' | O7: '=IF(J6="Due on Receipt",0,RIGHT(J6,2))' -> '30' | N8: 'Due Date' | O8: '=IFERROR(J5+O7,"")' -> 2023-04-30 00:00:00

### `91da76d6511e|IFERROR_MASK|Sheet1!B7`

- workbook: `all_data_912_v0.1/spreadsheet/45030/1_45030_input.xlsx`
- location: `Sheet1!B7`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($E$7:$E$19,MATCH(C7,$E$7:$E$19,0)),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 22 cells on this sheet; the others are Sheet1!B8, Sheet1!B9, Sheet1!B10, Sheet1!B11, Sheet1!B12, Sheet1!B13, Sheet1!B14, Sheet1!B15, ....
- cached value: None; row labels: []; column header: "'Tier'"; used range: A1:F28
- range $E$7:$E$19: values ['1000', '750', '500', '350', '250', '200', '150', '100', '75', '50', '40', '30']; beyond: {'above': "E6: 'At Least'", 'below': 'E20: None'}
- neighbourhood: B6: 'Tier' | C6: 'Cost' | B7: '=IFERROR(INDEX($E$7:$E$19,MATCH(C7,$E$7:$E$19,0)),"")' -> None | C7: 134 | B8: '=IFERROR(INDEX($E$7:$E$19,MATCH(C8,$E$7:$E$19,0)),"")' -> 0 | C8: 0 | B9: '=IFERROR(INDEX($E$7:$E$19,MATCH(C9,$E$7:$E$19,0)),"")' -> 0 | C9: 0

## LITERAL_CONSTANT

### `0dace778d55f|LITERAL_CONSTANT|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/59511/2_59511_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- formula: `=A2+1001`
- evidence: Non-trivial numeric literal(s) found: 1001.
- cached value: 1001; row labels: []; column header: ''; used range: A1:F13
- neighbourhood: A2: 0 | B2: 1000 | C2: 1 | A3: '=A2+1001' -> 1001 | B3: '=B2+1000' -> 2000 | C3: 2 | A4: '=A3+1000' -> 2001 | B4: '=B3+1000' -> 3000 | C4: 3 | A5: '=A4+1000' -> 3001 | B5: '=B4+1000' -> 4000 | C5: 4

### `ecefab75d6ce|LITERAL_CONSTANT|Calendar!B145`

- workbook: `all_data_912_v0.1/spreadsheet/57716/1_57716_input.xlsx`
- location: `Calendar!B145`  severity: Medium  confidence: Review
- formula: `=Days+8+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(Calendar11Year,Calendar11MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 8.
- cached value: 2021-02-08 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B143: '=Days+1+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(... -> 2021-02-01 00:00:00 | C143: 2021-02-02 00:00:00 | D143: 2021-02-03 00:00:00 | B145: '=Days+8+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(... -> 2021-02-08 00:00:00 | C145: 2021-02-09 00:00:00 | D145: 2021-02-10 00:00:00 | B147: '=Days+15+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE... -> 2021-02-15 00:00:00 | C147: 2021-02-16 00:00:00 | D147: 2021-02-17 00:00:00

### `4c7bcaeccab8|LITERAL_CONSTANT|Deal8!G18`

- workbook: `all_data_912_v0.1/spreadsheet/55060/3_55060_input.xlsx`
- location: `Deal 8!G18`  severity: Medium  confidence: Review
- formula: `=IF(I9="Yes",MIN(250,D10*0.025),IF(I9="No",MIN(750,D10*0.05),""))`
- evidence: Non-trivial numeric literal(s) found: 250, 0.025, 750, 0.05.
- cached value: 750; row labels: ["'Power Bonus'"]; column header: "'PIF Month'"; used range: A1:ABB24
- neighbourhood: G18: '=IF(I9="Yes",MIN(250,D10*0.025),IF(I9="No",MIN(750,D10*0.05),""))' -> 750 | G19: '=D12*0.075' -> 375 | G20: '=IF(D11=1995,400,IF(D11=1395,200,IF(D11=995,100,IF(D11="None",0,"$... -> 200

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!J14`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!J14`  severity: Medium  confidence: Review
- formula: `=IF(ROW()>=15,$J13-1,MAX(Table1[WEEK]))`
- evidence: Non-trivial numeric literal(s) found: 15.
- evidence: The same relative formula appears in 10 cells on this sheet; the others are RESULTS 1!J15, RESULTS 1!J16, RESULTS 1!J17, RESULTS 1!J18, RESULTS 1!J19, RESULTS 1!J20, RESULTS 1!J21, RESULTS 1!J22, ....
- cached value: 202114; row labels: []; column header: "'WEEK'"; used range: A1:W67
- neighbourhood: J12: 'WEEKLY' | K12: '=TRIMMEAN(Table2[TRADES],20%)' -> 5.75 | L12: '=TRIMMEAN(Table2[WIN %],20%)' -> '#DIV/0!' | J13: 'WEEK' | K13: 'TRADES' | L13: 'WIN %' | J14: '=IF(ROW()>=15,$J13-1,MAX(Table1[WEEK]))' -> 202114 | K14: '=COUNTIF(Table1[WEEK],$J14)' -> 3 | L14: '=COUNTIFS(Table1[POINTS G/L],">0",Table1[WEEK],J14)/COUNTIFS(Table... -> 0.666666666666667 | J15: '=IF(ROW()>=15,$J14-1,MAX(Table1[WEEK]))' -> 202113 | K15: '=COUNTIF(Table1[WEEK],$J15)' -> 4 | L15: '=COUNTIFS(Table1[POINTS G/L],">0",Table1[WEEK],J15)/COUNTIFS(Table... -> 0.5 | H16: 'ATI' | J16: '=IF(ROW()>=15,$J15-1,MAX(Table1[WEEK]))' -> 202112 | K16: '=COUNTIF(Table1[WEEK],$J16)' -> 6 | L16: '=COUNTIFS(Table1[POINTS G/L],">0",Table1[WEEK],J16)/COUNTIFS(Table... -> 1

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!T29`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!T29`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=20000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=20000000")/COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=20000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Points /s (Net)'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `aa0e60ece0f5|LITERAL_CONSTANT|master!E2`

- workbook: `all_data_912_v0.1/spreadsheet/47933/3_47933_input.xlsx`
- location: `master!E2`  severity: Medium  confidence: Review
- formula: `=IF(B2<37.5,"2",)*IF(B2>37.5,"D2,1.5,")`
- evidence: Non-trivial numeric literal(s) found: 37.5, 37.5.
- evidence: The same relative formula appears in 153 cells on this sheet; the others are master!E3, master!E4, master!E5, master!E6, master!E7, master!E8, master!E9, master!E10, ....
- cached value: '#VALUE!'; row labels: []; column header: "'Sum'"; used range: A1:E154
- neighbourhood: C1: 'Amount' | D1: 'Rate' | E1: 'Sum' | C2: '=INDEX(amount!A:A,MATCH(A2,amount!B:B,0))' -> 38708.8160515694 | D2: '=ROUND(C2/52/B2,2)' -> 18.61 | E2: '=IF(B2<37.5,"2",)*IF(B2>37.5,"D2,1.5,")' -> '#VALUE!' | C3: '=INDEX(amount!A:A,MATCH(A3,amount!B:B,0))' -> 47055.5719703303 | D3: '=ROUND(C3/52/B3,2)' -> 22.62 | E3: '=IF(B3<37.5,"2",)*IF(B3>37.5,"D2,1.5,")' -> '#VALUE!' | C4: '=INDEX(amount!A:A,MATCH(A4,amount!B:B,0))' -> 73564.5089645619 | D4: '=ROUND(C4/52/B4,2)' -> 33.29 | E4: '=IF(B4<37.5,"2",)*IF(B4>37.5,"D2,1.5,")' -> '#VALUE!'

### `ecefab75d6ce|LITERAL_CONSTANT|Calendar!B97`

- workbook: `all_data_912_v0.1/spreadsheet/57716/1_57716_input.xlsx`
- location: `Calendar!B97`  severity: Medium  confidence: Review
- formula: `=Days+36+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(Calendar7Year,Calendar7MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 36.
- cached value: 2020-11-02 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B95: '=Days+29+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(C... -> 2020-10-26 00:00:00 | C95: 2020-10-27 00:00:00 | D95: 2020-10-28 00:00:00 | B97: '=Days+36+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(C... -> 2020-11-02 00:00:00 | C97: 2020-11-03 00:00:00 | D97: 'Notes:' | B99: '=YEAR(DATE(Calendar7Year,Calendar7MonthOption+1,1))' -> 2020 | C99: '=TEXT(DATE(Calendar7Year,Calendar7MonthOption+1,1),"mmmm")' -> 'November'

### `30faaaeef9ee|LITERAL_CONSTANT|RESULTS1!S21`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!S21`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'PM Consolidation'", "'< 100M'"]; column header: "'5-10M'"; used range: A1:W67
- neighbourhood: Q20: '1-3M' | R20: '3-5M' | S20: '5-10M' | T20: '10-20M' | U20: '20-50M' | Q21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `74d967658eee|LITERAL_CONSTANT|Sheet1!O22`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!O22`  severity: Medium  confidence: Review
- formula: `=IF(I20>=12,IF(AND(J20<=120,G22>=400),G22,""),"")`
- evidence: Non-trivial numeric literal(s) found: 120, 400.
- evidence: The same relative formula appears in 2 cells on this sheet; the others are Sheet1!O317.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: M20: '=IFERROR(IF(I19>=12,IF($J19<=140,0+SUBSTITUTE(IF($D20>=175,","&$D2... -> None | N20: '=IF(I19>=12,IF(AND(J19<=90,G20>=300),G20,""),"")' -> None | O20: '=IF(I19>=12,IF(AND(J19<=120,G20>=400),G20,""),"")' -> None | P20: '=IF(I19>=12,IF(AND(J19<=145,G20>=500),G20,""),"")' -> None | Q20: '=IF(I19>=12,IF(AND(J19<=175,G20>=600),G20,""),"")' -> None | M21: '=IFERROR(IF(I20>=12,IF($J20<=140,0+SUBSTITUTE(IF($D21>=175,","&$D2... -> None | N21: '=IF(I20>=12,IF(AND(J20<=90,G21>=300),G21,""),"")' -> None | Q21: '=IF(I20>=12,IF(AND(J20<=175,G21>=600),G21,""),"")' -> None | M22: '=IFERROR(IF(I21>=12,IF($J21<=140,0+SUBSTITUTE(IF($D22>=175,","&$D2... -> None | N22: '=IF(I21>=12,IF(AND(J21<=90,G22>=300),G22,""),"")' -> None | O22: '=IF(I20>=12,IF(AND(J20<=120,G22>=400),G22,""),"")' -> None | P22: '=IF(I20>=12,IF(AND(J20<=145,G22>=500),G22,""),"")' -> None | Q22: '=IF(I21>=12,IF(AND(J21<=175,G22>=600),G22,""),"")' -> None | M23: '=IFERROR(IF(I22>=12,IF($J22<=140,0+SUBSTITUTE(IF($D23>=175,","&$D2... -> None | N23: '=IF(I22>=12,IF(AND(J22<=120,G23>=300),G23,""),"")' -> None | Q23: '=IF(I22>=12,IF(AND(J22<=175,G23>=600),G23,""),"")' -> None | M24: '=IFERROR(IF(I23>=12,IF($J23<=140,0+SUBSTITUTE(IF($D24>=175,","&$D2... -> None | N24: '=IF(I23>=12,IF(AND(J23<=90,G24>=300),G24,""),"")' -> None | O24: '=IF(I23>=12,IF(AND(J23<=120,G24>=400),G24,""),"")' -> None | P24: '=IF(I23>=12,IF(AND(J23<=145,G24>=500),G24,""),"")' -> None | Q24: '=IF(I23>=12,IF(AND(J23<=175,G24>=600),G24,""),"")' -> None

### `95fdf876027b|LITERAL_CONSTANT|RESULTS1!T16`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!T16`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: R14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!S3`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!S3`  severity: Medium  confidence: Review
- formula: `=TRIMMEAN(IF(Table1[MAX GAIN]>=6,Table1[POINTS G/L]),10%)`
- evidence: Non-trivial numeric literal(s) found: 6.
- cached value: 5.89777777777778; row labels: ["'All-TIME'"]; column header: "'>= 6'"; used range: A1:W67
- neighbourhood: Q2: '>= 4' | R2: '>= 5' | S2: '>= 6' | T2: '>= 7' | U2: '>= 8' | Q3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=4,Table1[POINTS G/L]),10%) {array Q3}' -> 4.779375 | R3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=5,Table1[POINTS G/L]),10%) {array R3}' -> 5.20833333333333 | S3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=6,Table1[POINTS G/L]),10%) {array S3}' -> 5.89777777777778 | T3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=7,Table1[POINTS G/L]),10%) {array T3}' -> 7.165 | U3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=8,Table1[POINTS G/L]),10%) {array U3}' -> 9.11 | Q4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF((Table1[WEEK]>=MAX(Tab... -> 4.779375 | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.20833333333333 | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.89777777777778 | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 7.165 | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 9.11 | Q5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF((Table1[WEEK]>=MAX(Tab... -> 4.646 | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.22571428571429 | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.83833333333333 | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B107`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B107`  severity: Medium  confidence: Review
- formula: `=Days+22+DATE(Calendar8Year,Calendar8MonthOption,1)-WEEKDAY(DATE(Calendar8Year,Calendar8MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 22.
- cached value: 2020-11-16 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B105: '=Days+15+DATE(Calendar8Year,Calendar8MonthOption,1)-WEEKDAY(DATE(C... -> 2020-11-09 00:00:00 | C105: 2020-11-10 00:00:00 | D105: 2020-11-11 00:00:00 | B107: '=Days+22+DATE(Calendar8Year,Calendar8MonthOption,1)-WEEKDAY(DATE(C... -> 2020-11-16 00:00:00 | C107: 2020-11-17 00:00:00 | D107: 2020-11-18 00:00:00 | B109: '=Days+29+DATE(Calendar8Year,Calendar8MonthOption,1)-WEEKDAY(DATE(C... -> 2020-11-23 00:00:00 | C109: 2020-11-24 00:00:00 | D109: 2020-11-25 00:00:00

### `a40f5412bbae|LITERAL_CONSTANT|ATTENDENCE!E6`

- workbook: `all_data_912_v0.1/spreadsheet/11276/2_11276_input.xlsx`
- location: `ATTENDENCE!E6`  severity: Medium  confidence: Review
- formula: `=17-12`
- evidence: Non-trivial numeric literal(s) found: 17.
- cached value: 5; row labels: ["'Neeraj Sachar'"]; column header: "'PH'"; used range: A1:AS20
- neighbourhood: C4: 'NAMES' | D4: 'PO' | E4: 'PH' | F4: 2015-10-19 00:00:00 | G4: 2015-10-22 00:00:00 | C6: 'Neeraj Sachar' | D6: '=18-1' -> 17 | E6: '=17-12' -> 5 | F6: '=IF(F3="F","O","P")' -> 'P' | G6: '=IF(G3="F","O","P")' -> 'P' | F8: 'IN' | G8: 'Induction programe'

### `1ee00a60f590|LITERAL_CONSTANT|Sheet1!Y86`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!Y86`  severity: Medium  confidence: Review
- formula: `=IF(AND(I126>=12,G86>0),SUM(ROUNDDOWN(SUM(200-J126)*0.9,0)*3)+X86,"0")`
- evidence: Non-trivial numeric literal(s) found: 200, 3.
- cached value: '0'; row labels: ["'EE'", "'AE'"]; column header: ''; used range: A1:CJ782
- neighbourhood: W84: '=IF(AND(I83>=12,G84>0),ROUNDDOWN(SUM(200-J83)*0.9,0)+V84,"0")' -> '0' | X84: '=SUM(G84)' -> 0 | Y84: '=IF(AND(I83>=12,G84>0),SUM(ROUNDDOWN(SUM(200-J83)*0.9,0)*3)+X84,"0")' -> '0' | X85: '=SUM(G85)' -> 0 | W86: '=IF(AND(I126>=12,G86>0),ROUNDDOWN(SUM(200-J126)*0.9,0)+V86,"0")' -> '0' | X86: '=SUM(G86)' -> 0 | Y86: '=IF(AND(I126>=12,G86>0),SUM(ROUNDDOWN(SUM(200-J126)*0.9,0)*3)+X86,... -> '0' | Z86: '=CONCATENATE(A86," ",B86," ")' -> 'EE AE' | W87: '=IF(AND(I86>=12,G87>0),ROUNDDOWN(SUM(200-J86)*0.9,0)+V87,"0")' -> '0' | X87: '=SUM(G87)' -> 342 | Y87: '=IF(AND(I86>=12,G87>0),SUM(ROUNDDOWN(SUM(200-J86)*0.9,0)*3)+X87,"0")' -> '0' | W88: '=IF(AND(I87>=12,G88>0),ROUNDDOWN(SUM(200-J87)*0.9,0)+V88,"0")' -> '0' | X88: '=SUM(G88)' -> 0 | Y88: '=IF(AND(I87>=12,G88>0),SUM(ROUNDDOWN(SUM(200-J87)*0.9,0)*3)+X88,"0")' -> '0'

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!S28`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!S28`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")/COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Wins'", "'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: Q26: '1-3M' | R26: '3-5M' | S26: '5-10M' | T26: '10-20M' | U26: '20-50M' | Q27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `5124d0617e42|LITERAL_CONSTANT|example!C8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!C8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(1,5)`
- evidence: Non-trivial numeric literal(s) found: 5.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!C9, example!C10, example!C11, example!C12.
- cached value: 4; row labels: ["'Egg'"]; column header: "'IZHAR'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | B8: 'Egg' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 10 | E8: '=RANDBETWEEN(10,15)' -> 13 | B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 6 | E9: '=RANDBETWEEN(10,15)' -> 14 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 4 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15

### `19dfd5dbcec5|LITERAL_CONSTANT|formamspnc(7)!I11`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!I11`  severity: Medium  confidence: Review
- formula: `=IF(AND(NOT(BH11=""),NOT(#REF!=""),NOT(#REF!="")),7,IF(AND(NOT(BH11=""),NOT(#REF!="")),6,IF(AND(AR11=0,BH11="b"),"X",IF(AR11=0,"Y",""))))`
- evidence: Non-trivial numeric literal(s) found: 6.
- cached value: '#REF!'; row labels: ["'13c/18c/20c/25c/28c/32c/34c/37c/41c/49c/58c/63c/69c(1 ex..."]; column header: ''; used range: A1:ED48610
- neighbourhood: G9: '=IF(AND(OR(F9=1,F9=2),OR(BH9="b",BH9="c",BH9=1)),1,IF(AND(OR(AD9=$... -> None | H9: '=IF(OR(AND(K9="D",L9="E",M9="F"),AND(ISNUMBER(BI9),G9=2)),"H",IF(O... -> None | I9: '=IF(AND(NOT(BH9=""),NOT(BH10=""),NOT(BH11="")),7,IF(AND(NOT(BH9=""... -> None | J9: '=IF(AND(OR(H9="h",AND(K9="d",L9="e"),AND(L9="e",M9="f"),AND(K9="d"... -> None | K9: '=IF(AND(AE9=0,AF9=0,ISNUMBER(BI9)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> 'D' | G10: '=IF(AND(OR(F10=1,F10=2),OR(BH10="b",BH10="c",BH10=1)),1,IF(AND(OR(... -> None | H10: '=IF(OR(AND(K10="D",L10="E",M10="F"),AND(ISNUMBER(BI10),G10=2)),"H"... -> None | I10: '=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10... -> '#REF!' | J10: '=IF(AND(OR(H10="h",AND(K10="d",L10="e"),AND(L10="e",M10="f"),AND(K... -> None | K10: '=IF(AND(AE10=0,AF10=0,ISNUMBER(BI10)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None | G11: '=IF(AND(OR(F11=1,F11=2),OR(BH11="b",BH11="c",BH11=1)),1,IF(AND(OR(... -> None | H11: '=IF(OR(AND(K11="D",L11="E",M11="F"),AND(ISNUMBER(BI11),G11=2)),"H"... -> None | I11: '=IF(AND(NOT(BH11=""),NOT(#REF!=""),NOT(#REF!="")),7,IF(AND(NOT(BH1... -> '#REF!' | J11: '=IF(AND(OR(H11="h",AND(K11="d",L11="e"),AND(L11="e",M11="f"),AND(K... -> None | K11: '=IF(AND(AE11=0,AF11=0,ISNUMBER(BI11)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None

### `902b5e29897a|LITERAL_CONSTANT|LeadTimes!K8`

- workbook: `all_data_912_v0.1/spreadsheet/47741/1_47741_input.xlsx`
- location: `Lead Times!K8`  severity: Medium  confidence: Review
- formula: `=WORKDAY(K5,18,K15:K20)`
- evidence: Non-trivial numeric literal(s) found: 18.
- cached value: 2022-12-01 00:00:00; row labels: ["'FULL CUSTOM'"]; column header: ''; used range: A1:O31
- range K15:K20: values ['2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00']; beyond: {'above': 'K14: 2021-12-31 00:00:00', 'below': 'K21: None'}
- neighbourhood: J7: 'STANDARD' | K7: '=WORKDAY(K5,10,K15:K20)' -> 2022-11-17 00:00:00 | L7: '-' | M7: '=WORKDAY(K5,10,K15:K20)' -> 2022-11-17 00:00:00 | J8: 'FULL CUSTOM' | K8: '=WORKDAY(K5,18,K15:K20)' -> 2022-12-01 00:00:00 | L8: '-' | M8: '=WORKDAY(K5,18,K15:K20)' -> 2022-12-01 00:00:00 | J9: 'ELECTRONICS' | K9: '=WORKDAY(K5,3,K15:K20)' -> 2022-11-08 00:00:00 | L9: '-' | M9: '=WORKDAY(K5,5,K15:K20)' -> 2022-11-10 00:00:00

### `5d8557dfb652|LITERAL_CONSTANT|July-KPIs!F20`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!F20`  severity: Medium  confidence: Review
- formula: `=MAX(0,((F16-4.5)/0.1)*10)`
- evidence: Non-trivial numeric literal(s) found: 4.5, 0.1, 10.
- cached value: '#DIV/0!'; row labels: []; column header: "'Bonus'"; used range: A1:T3212
- neighbourhood: E18: '=IFERROR(((C18*1.3)+(D18*1))/((B18)),"0")' -> '0' | F18: 'Bonus' | E19: '=IFERROR(((C19*1.3)+(D19*1))/((B19)),"0")' -> '0' | E20: '=IFERROR(((C20*1.3)+(D20*1))/((B20)),"0")' -> '0' | F20: '=MAX(0,((F16-4.5)/0.1)*10)' -> '#DIV/0!' | E21: '=IFERROR(((C21*1.3)+(D21*1))/((B21)),"0")' -> '0' | E22: '=IFERROR(((C22*1.3)+(D22*1))/((B22)),"0")' -> '0'

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B117`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B117`  severity: Medium  confidence: Review
- formula: `=Days+8+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(Calendar9Year,Calendar9MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 8.
- cached value: 2020-12-07 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B115: '=Days+1+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(Ca... -> 2020-11-30 00:00:00 | C115: 2020-12-01 00:00:00 | D115: 2020-12-02 00:00:00 | B117: '=Days+8+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(Ca... -> 2020-12-07 00:00:00 | C117: 2020-12-08 00:00:00 | D117: 2020-12-09 00:00:00 | B119: '=Days+15+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-14 00:00:00 | C119: 2020-12-15 00:00:00 | D119: 2020-12-16 00:00:00

### `2f9a764eab30|LITERAL_CONSTANT|Sheet1!J6`

- workbook: `all_data_912_v0.1/spreadsheet/52541/1_52541_input.xlsx`
- location: `Sheet1!J6`  severity: Medium  confidence: Review
- formula: `=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row],[Over Due Days]]<90,"Call Customer","Bad Debts"))`
- evidence: Non-trivial numeric literal(s) found: 90.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are Sheet1!J7, Sheet1!J8, Sheet1!J9, Sheet1!J10.
- cached value: 'Bad Debts'; row labels: ["'ARON'"]; column header: "'Remarks'"; used range: A1:J13
- neighbourhood: H5: 'Amount Outstanding' | I5: 'Over Due Days' | J5: 'Remarks' | H6: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 25000 | I6: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1171 | J6: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | H7: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 22000 | I7: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1143 | J7: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | H8: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> -3000 | I8: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1138 | J8: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts'

### `74d967658eee|LITERAL_CONSTANT|Sheet1!O3`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!O3`  severity: Medium  confidence: Review
- formula: `=IF(I2>=12,IF(AND(J2<=120,G3>=400),G3,""),"")`
- evidence: Non-trivial numeric literal(s) found: 120, 400.
- evidence: The same relative formula appears in 304 cells on this sheet; the others are Sheet1!O4, Sheet1!O5, Sheet1!O6, Sheet1!O7, Sheet1!O8, Sheet1!O9, Sheet1!O10, Sheet1!O11, ....
- cached value: None; row labels: []; column header: "'120 Avg w/400 Series'"; used range: A1:CJ782
- neighbourhood: M1: '140 Avg w/175 Gm' | N1: '90 Avg w/300 Series' | O1: '120 Avg w/400 Series' | P1: '145 Avg w/500 Series' | Q1: '175 Avg w/600 Series' | M3: '=IFERROR(IF(I2>=12,IF($J2<=140,0+SUBSTITUTE(IF($D3>=175,","&$D3,""... -> None | N3: '=IF(I2>=12,IF(AND(J2<=90,G3>=300),G3,""),"")' -> None | O3: '=IF(I2>=12,IF(AND(J2<=120,G3>=400),G3,""),"")' -> None | P3: '=IF(I2>=12,IF(AND(J2<=145,G3>=500),G3,""),"")' -> None | Q3: '=IF(I2>=12,IF(AND(J2>=175,G3>=600),G3,""),"")' -> None | M4: '=IFERROR(IF(I3>=12,IF($J3<=140,0+SUBSTITUTE(IF($D4>=175,","&$D4,""... -> None | N4: '=IF(I3>=12,IF(AND(J3<=90,G4>=300),G4,""),"")' -> None | O4: '=IF(I3>=12,IF(AND(J3<=120,G4>=400),G4,""),"")' -> None | P4: '=IF(I3>=12,IF(AND(J3<=145,G4>=500),G4,""),"")' -> None | Q4: '=IF(I3>=12,IF(AND(J3<=175,G4>=600),G4,""),"")' -> None | M5: '=IFERROR(IF(I4>=12,IF($J4<=140,0+SUBSTITUTE(IF($D5>=175,","&$D5,""... -> None | N5: '=IF(I4>=12,IF(AND(J4<=90,G5>=300),G5,""),"")' -> None | O5: '=IF(I4>=12,IF(AND(J4<=120,G5>=400),G5,""),"")' -> None | P5: '=IF(I4>=12,IF(AND(J4<=145,G5>=500),G5,""),"")' -> None | Q5: '=IF(I4>=12,IF(AND(J4<=175,G5>=600),G5,""),"")' -> None

### `968835ee4407|LITERAL_CONSTANT|TEST_SHEET!M19`

- workbook: `all_data_912_v0.1/spreadsheet/53994/2_53994_input.xlsx`
- location: `TEST_SHEET!M19`  severity: Medium  confidence: Review
- formula: `=35*10`
- evidence: Non-trivial numeric literal(s) found: 35, 10.
- cached value: 350; row labels: ["'Time (Mins)'"]; column header: "'S1'"; used range: A1:W37
- neighbourhood: K17: 'Machine' | L17: 'M1' | M17: 'M1' | N17: 'M3' | O17: 'M3' | K18: 'Person' | L18: 'S1' | M18: 'S1' | N18: 'S2' | O18: 'S2' | K19: 'Time (Mins)' | L19: 100 | M19: '=35*10' -> 350 | N19: 120 | O19: 100 | K20: 'Machine' | L20: 'M1' | M20: 'M1' | N20: 'M3' | O20: 'M3' | K21: 'Person' | L21: 'S1' | M21: 'S1' | N21: 'S2' | O21: 'S2'

### `c2ca64fa3433|LITERAL_CONSTANT|גיליון1!C6`

- workbook: `all_data_912_v0.1/spreadsheet/10747/2_10747_input.xlsx`
- location: `גיליון1!C6`  severity: Medium  confidence: Review
- formula: `=+C3*0.8`
- evidence: Non-trivial numeric literal(s) found: 0.8.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are גיליון1!D6, גיליון1!E6, גיליון1!F6.
- cached value: -4240; row labels: []; column header: ''; used range: A1:L8
- neighbourhood: A4: 2012 | B4: 101010 | C4: '=+C3*2' -> -10600 | D4: '=+D3*2' -> 24000 | E4: '=+E3*2' -> 4000 | A5: 2011 | B5: 101010 | C5: '=+C4*1.1' -> -11660.000000000002 | D5: '=+D4*1.1' -> 26400.000000000004 | E5: '=+E4*1.1' -> 4400 | A6: 2013 | B6: 202020 | C6: '=+C3*0.8' -> -4240 | D6: '=+D3*0.8' -> 9600 | E6: '=+E3*0.8' -> 1600 | A7: 2012 | B7: 202020 | C7: '=+C6*2' -> -8480 | D7: '=+D6*2' -> 19200 | E7: '=+E6*2' -> 3200 | A8: 2011 | B8: 202020 | C8: '=+C7*1.1' -> -9328 | D8: '=+D7*1.1' -> 21120 | E8: '=+E7*1.1' -> 3520.0000000000005

### `125be9ba2e04|LITERAL_CONSTANT|RESULTS1!T20`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!T20`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,COUNTIFS(Table1[POINTS],">0",Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")/COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'ATI'", "'< 100M'"]; column header: "'5-10M'"; used range: A1:X80
- neighbourhood: R19: '1-3M' | S19: '3-5M' | T19: '5-10M' | U19: '10-20M' | V19: '20-50M' | R20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

## LIVE_ERROR

### `be2f958d4b41|LIVE_ERROR|Sort!K47`

- workbook: `all_data_912_v0.1/spreadsheet/59932/2_59932_input.xlsx`
- location: `Sort!K47`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2005_Q4'"]; column header: ''; used range: A1:T147
- neighbourhood: I45: "=VLOOKUP($B45,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 748 | J45: "=VLOOKUP($B45,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.1099999999999999 | K45: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A45,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L45: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A45,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M45: '=D45*P45' -> '#VALUE!' | I46: "=VLOOKUP($B46,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 1006 | J46: "=VLOOKUP($B46,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.32 | K46: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A46,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L46: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A46,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M46: '=D46*P46' -> '#VALUE!' | I47: "=VLOOKUP($B47,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 1328 | J47: "=VLOOKUP($B47,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.55 | K47: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A47,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L47: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A47,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M47: '=D47*P47' -> '#VALUE!' | I48: "=VLOOKUP($B48,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 1600 | J48: "=VLOOKUP($B48,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.8500000000000003 | K48: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A48,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L48: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A48,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M48: '=D48*P48' -> '#VALUE!' | I49: "=VLOOKUP($B49,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 1722 | J49: "=VLOOKUP($B49,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.98 | K49: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A49,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L49: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A49,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M49: '=D49*P49' -> '#VALUE!'

### `f7cdf83fda03|LIVE_ERROR|Data!H23`

- workbook: `all_data_912_v0.1/spreadsheet/510-3/2_510-3_input.xlsx`
- location: `Data!H23`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'\\u202d02'", "'19\\u202c'"]; column header: "'#VALUE!'"; used range: A1:H78
- neighbourhood: F21: 9 | G21: '19\u202c' | H21: '#VALUE!' | F22: 9 | G22: '19\u202c' | H22: '#VALUE!' | F23: 9 | G23: '19\u202c' | H23: '#VALUE!' | F24: 9 | G24: '19\u202c' | H24: '#VALUE!' | F25: 9 | G25: '19\u202c' | H25: '#VALUE!'

### `192a19040f63|LIVE_ERROR|Sheettwo!E145`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E145`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0042135770'"]; column header: ''; used range: A1:G6234
- neighbourhood: C143: '0D' | D143: '0000000410' | E143: '=VLOOKUP(G143,Suppliers2[],2,FALSE)' -> '#N/A' | F143: '009905' | G143: '70263016' | C144: '1D' | D144: '0041565853' | E144: '=VLOOKUP(G144,Suppliers2[],2,FALSE)' -> '#N/A' | F144: '009942' | G144: '70263016' | C145: '1D' | D145: '0042135770' | E145: '=VLOOKUP(G145,Suppliers2[],2,FALSE)' -> '#N/A' | F145: '009960' | G145: '31759000' | C146: '1D' | D146: '0042135771' | E146: '=VLOOKUP(G146,Suppliers2[],2,FALSE)' -> '#N/A' | F146: '010077' | G146: '88713000' | C147: '2D' | D147: '0000042415' | E147: '=VLOOKUP(G147,Suppliers2[],2,FALSE)' -> '#N/A' | F147: '010102' | G147: '70263016'

### `e3e5ae270e30|LIVE_ERROR|Sheet1!BJ5`

- workbook: `all_data_912_v0.1/spreadsheet/52450/2_52450_input.xlsx`
- location: `Sheet1!BJ5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 8 dependent cell(s): Sheet1!BJ4, Sheet1!P4, Sheet1!P5, Sheet1!S4, Sheet1!S5, Sheet1!T4, Sheet1!T5, Sheet1!V4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Wind'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: BH4: '=IF($H5="",0,IF($H5<"",SUM(BH5:BH104)))' -> '#VALUE!' | BI4: '=IF($H5="",0,IF($H5<"",SUM(BI5:BI104)))' -> '#VALUE!' | BJ4: '=IF($H5="",0,IF($H5<"",SUM(BJ5:BJ104)))' -> '#VALUE!' | BK4: '=IF($H5="",0,IF($H5<"",SUM(BK5:BK104)))' -> '#VALUE!' | BL4: '=IF($H5="",0,IF($H5<"",SUM(BL5:BL104)))' -> '#VALUE!' | BH5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BH$1,\'[1]X... -> '#VALUE!' | BI5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BH6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BH$1,\'[1]X... -> '#VALUE!' | BI6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BH7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BH$1,\'[1]X... -> '#VALUE!' | BI7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!'

### `e3e5ae270e30|LIVE_ERROR|Sheet1!BN7`

- workbook: `all_data_912_v0.1/spreadsheet/52450/2_52450_input.xlsx`
- location: `Sheet1!BN7`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 8 dependent cell(s): Sheet1!BN4, Sheet1!P4, Sheet1!P7, Sheet1!S4, Sheet1!S7, Sheet1!T4, Sheet1!T7, Sheet1!V4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Tornado'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: BL5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BN5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BN$1,\'[1]X... -> '#VALUE!' | BO5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BO$1,\'[1]X... -> '#VALUE!' | BP5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BP$1,\'[1]X... -> '#VALUE!' | BL6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BN6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BN$1,\'[1]X... -> '#VALUE!' | BO6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BO$1,\'[1]X... -> '#VALUE!' | BP6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BP$1,\'[1]X... -> '#VALUE!' | BL7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BN7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BN$1,\'[1]X... -> '#VALUE!' | BO7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BO$1,\'[1]X... -> '#VALUE!' | BP7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BP$1,\'[1]X... -> '#VALUE!' | BL8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BN8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BN$1,\'[1]X... -> '#VALUE!' | BO8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BO$1,\'[1]X... -> '#VALUE!' | BP8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BP$1,\'[1]X... -> '#VALUE!' | BL9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BN9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BN$1,\'[1]X... -> '#VALUE!' | BO9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BO$1,\'[1]X... -> '#VALUE!' | BP9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BP$1,\'[1]X... -> '#VALUE!'

### `8734ff2c3db4|LIVE_ERROR|Sheet1!H32`

- workbook: `all_data_912_v0.1/spreadsheet/50631/1_50631_input.xlsx`
- location: `Sheet1!H32`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: F30: '=IF($B$3+ROWS($B$7:$F61)-1<=$F$3,$B$3+ROWS($B$7:$F61)-1,"")' -> 2021-10-25 00:00:00 | H30: '=IF($B$3+ROWS($B$7:$B30)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B30)-1,""))' -> '#VALUE!' | F31: '=IF($B$3+ROWS($B$7:$F62)-1<=$F$3,$B$3+ROWS($B$7:$F62)-1,"")' -> 2021-10-26 00:00:00 | H31: '=IF($B$3+ROWS($B$7:$B31)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B31)-1,""))' -> '#VALUE!' | F32: '=IF($B$3+ROWS($B$7:$F63)-1<=$F$3,$B$3+ROWS($B$7:$F63)-1,"")' -> 2021-10-27 00:00:00 | H32: '=IF($B$3+ROWS($B$7:$B32)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B32)-1,""))' -> '#VALUE!' | F33: '=IF($B$3+ROWS($B$7:$F64)-1<=$F$3,$B$3+ROWS($B$7:$F64)-1,"")' -> 2021-10-28 00:00:00 | H33: '=IF($B$3+ROWS($B$7:$B33)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B33)-1,""))' -> '#VALUE!' | F34: '=IF($B$3+ROWS($B$7:$F65)-1<=$F$3,$B$3+ROWS($B$7:$F65)-1,"")' -> 2021-10-29 00:00:00 | H34: '=IF($B$3+ROWS($B$7:$B34)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B34)-1,""))' -> '#VALUE!'

### `aa0e60ece0f5|LIVE_ERROR|master!E102`

- workbook: `all_data_912_v0.1/spreadsheet/47933/3_47933_input.xlsx`
- location: `master!E102`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C100: '=INDEX(amount!A:A,MATCH(A100,amount!B:B,0))' -> 23640.9923628951 | D100: '=ROUND(C100/52/B100,2)' -> 10.7 | E100: '=IF(B100<37.5,"2",)*IF(B100>37.5,"D2,1.5,")' -> '#VALUE!' | C101: '=INDEX(amount!A:A,MATCH(A101,amount!B:B,0))' -> 22735.2254928666 | D101: '=ROUND(C101/52/B101,2)' -> 10.29 | E101: '=IF(B101<37.5,"2",)*IF(B101>37.5,"D2,1.5,")' -> '#VALUE!' | C102: '=INDEX(amount!A:A,MATCH(A102,amount!B:B,0))' -> 80535.4273187908 | D102: '=ROUND(C102/52/B102,2)' -> 36.44 | E102: '=IF(B102<37.5,"2",)*IF(B102>37.5,"D2,1.5,")' -> '#VALUE!' | C103: '=INDEX(amount!A:A,MATCH(A103,amount!B:B,0))' -> 47750.2404609572 | D103: '=ROUND(C103/52/B103,2)' -> 24.49 | E103: '=IF(B103<37.5,"2",)*IF(B103>37.5,"D2,1.5,")' -> 0 | C104: '=INDEX(amount!A:A,MATCH(A104,amount!B:B,0))' -> 96488.3707955549 | D104: '=ROUND(C104/52/B104,2)' -> 43.66 | E104: '=IF(B104<37.5,"2",)*IF(B104>37.5,"D2,1.5,")' -> '#VALUE!'

### `79139a88c691|LIVE_ERROR|Sheet1!AM9`

- workbook: `all_data_912_v0.1/spreadsheet/52450/1_52450_input.xlsx`
- location: `Sheet1!AM9`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 1 dependent cell(s): Sheet1!AM4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Trainer'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: AK7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!' | AL7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AL$1,\'[1]X... -> '#VALUE!' | AM7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AK8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!' | AL8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AL$1,\'[1]X... -> '#VALUE!' | AM8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AK9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!' | AL9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AL$1,\'[1]X... -> '#VALUE!' | AM9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AK10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]... -> None | AL10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AL$1,\'[1]... -> None | AM10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]... -> None | AN10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]... -> None | AO10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]... -> None | AK11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]... -> None | AL11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AL$1,\'[1]... -> None | AM11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]... -> None | AN11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]... -> None | AO11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]... -> None

### `3f7694b32e64|LIVE_ERROR|2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/1_68-47_input.xlsx`
- location: `2023!J2`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'InterCompany 2023'"]; column header: ''; used range: A1:N144
- neighbourhood: J1: '=COUNTIF(H:H,-H7)=1' -> True | K1: '=AND(ISNUMBER(H7),SUMPRODUCT(--(ABS($H$7:$H$140)=ABS(H7)))>1)' -> True | J2: '=SMALL(IF($H$7:$H$140=-H7,1),COUNTIF($H$7:H7,H7))' -> '#VALUE!' | H4: 'Variance'

### `b230bc5037bf|LIVE_ERROR|PrevworkingdayQuote(2)!A26`

- workbook: `all_data_912_v0.1/spreadsheet/47699/3_47699_input.xlsx`
- location: `Prev working day Quote (2)!A26`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A24: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B24: 'Oscar' | C24: 7 | A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7 | A27: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B27: 'Oscar' | C27: 7

### `1f2994e91d0b|LIVE_ERROR|Sheet1!D147`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/1_189-9_input.xlsx`
- location: `Sheet1!D147`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'LB0689'"]; column header: ''; used range: A1:E613
- neighbourhood: B145: 2015-11-30 00:00:00 | C145: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D145: '=INT(C145)-INT(B145)' -> '#VALUE!' | B146: 2015-11-30 00:00:00 | C146: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D146: '=INT(C146)-INT(B146)' -> '#VALUE!' | B147: 2013-04-01 00:00:00 | C147: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D147: '=INT(C147)-INT(B147)' -> '#VALUE!' | B148: 2014-10-31 00:00:00 | C148: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D148: '=INT(C148)-INT(B148)' -> '#VALUE!' | B149: 2013-04-01 00:00:00 | C149: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D149: '=INT(C149)-INT(B149)' -> '#VALUE!'

### `0e8785562296|LIVE_ERROR|COVER!C21`

- workbook: `all_data_912_v0.1/spreadsheet/56915/2_56915_input.xlsx`
- location: `COVER!C21`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'        STUFF 1'"]; column header: ''; used range: A1:E23
- neighbourhood: A19: '    COST OF GOODS SOLD' | A20: '      STUFF' | A21: '        STUFF 1' | B21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> 1705 | C21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> '#N/A' | D21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> '#N/A' | E21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> '#N/A' | A22: '        STUFF 2' | B22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> -95.6776850726545 | C22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> '#N/A' | D22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> '#N/A' | E22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> '#N/A' | A23: '        STUFF 3' | B23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> 3658.20212926082 | C23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> '#N/A' | D23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> '#N/A' | E23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> '#N/A'

### `a94eb6a7585f|LIVE_ERROR|HR!AM5`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !AM5`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 2 dependent cell(s): HR !AM24, HR !BE5. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'May-July'", "'Month 1'"]; column header: ''; used range: A1:GT37
- neighbourhood: AK3: '=SUM(N3+V3+AD3)' -> '#REF!' | AL3: 2019-09-01 00:00:00 | AM3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | AN3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | AO3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | AL4: 2019-09-01 00:00:00 | AM4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | AN4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | AO4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | AL5: 2019-09-01 00:00:00 | AM5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | AN5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | AO5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | AL7: 2019-09-01 00:00:00 | AM7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | AN7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | AO7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!'

### `9792181a96d9|LIVE_ERROR|Exp-DB!E9`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/1_524-31_input.xlsx`
- location: `Exp-DB!E9`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'dining out'", "'BEST BUY #269 SPRINGFIELD VAUS'"]; column header: ''; used range: A1:G53
- neighbourhood: D7: 'BARNES&NOBLE.COM-B 800-843-2665 NY' | E7: '=VLOOKUP(D7 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G7: '=INDEX(cats,MATCH("*"&D7&"*",exDB,0))' -> '#N/A' | D8: 'BARNESNOBLE 6646 Loisd Springfield V... | E8: '=VLOOKUP(D8 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G8: '=INDEX(cats,MATCH("*"&D8&"*",exDB,0))' -> '#N/A' | D9: 'BEST BUY #269 SPRINGFIELD VAUS' | E9: '=VLOOKUP(D9 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G9: '=INDEX(cats,MATCH("*"&D9&"*",exDB,0))' -> '#N/A' | D10: 'BESTBUY.COM 8882378289 MN' | E10: '=VLOOKUP(D10 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G10: '=INDEX(cats,MATCH("*"&D10&"*",exDB,0))' -> '#N/A' | D11: 'BESTBUY.COM 8882378289 MN' | E11: '=VLOOKUP(D11 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G11: '=INDEX(cats,MATCH("*"&D11&"*",exDB,0))' -> '#N/A'

### `a94eb6a7585f|LIVE_ERROR|HR!BT7`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !BT7`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 1 dependent cell(s): HR !BT24. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'N/A'", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: BS5: 2019-12-01 00:00:00 | BT5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BU5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BV5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BS7: 2019-12-01 00:00:00 | BT7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BU7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BV7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BS8: '=BS7' -> 2019-12-01 00:00:00 | BT8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BU8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BV8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!'

### `30c6f4937476|LIVE_ERROR|HR!BJ10`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !BJ10`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 1 dependent cell(s): HR !BJ24. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'Yes'", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: BH8: 2019-11-01 00:00:00 | BI8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BJ8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BK8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BL8: '=BB8' -> '#REF!' | BH10: 2019-11-01 00:00:00 | BI10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | BJ10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | BK10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | BL10: '=BB10' -> '#REF!' | BH11: 2019-11-01 00:00:00 | BI11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | BJ11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | BK11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | BL11: '=BB11' -> 'Yes' | BH12: 2019-11-01 00:00:00 | BI12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BJ12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BK12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BL12: '=BB12' -> '#REF!'

### `f7cdf83fda03|LIVE_ERROR|Data!H5`

- workbook: `all_data_912_v0.1/spreadsheet/510-3/2_510-3_input.xlsx`
- location: `Data!H5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'\\u202d00'", "'08\\u202c'"]; column header: "'#VALUE!'"; used range: A1:H78
- neighbourhood: F3: 0 | G3: '08\u202c' | H3: '#VALUE!' | F4: 0 | G4: '08\u202c' | H4: '#VALUE!' | F5: 0 | G5: '08\u202c' | H5: '#VALUE!' | F6: 0 | G6: '08\u202c' | H6: '#VALUE!' | F7: 2 | G7: '15\u202c' | H7: '#VALUE!'

### `93e74f622cb1|LIVE_ERROR|Sheet1!B13`

- workbook: `all_data_912_v0.1/spreadsheet/57743/2_57743_input.xlsx`
- location: `Sheet1!B13`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'4GXCD010AC6HUA'"]; column header: ''; used range: A1:D19
- neighbourhood: A11: '4GXCC017AC6HUA' | B11: '=INDEX(D:D,MATCH(A11,C:C,0)) {array B11}' -> '#N/A' | C11: '2AYTXVH3H1836A' | D11: 55.35 | A12: '4GXCD008AC6HUA' | B12: '=INDEX(D:D,MATCH(A12,C:C,0)) {array B12}' -> '#N/A' | C12: '2AYTXVH3G2436A' | D12: 71.75 | A13: '4GXCD010AC6HUA' | B13: '=INDEX(D:D,MATCH(A13,C:C,0)) {array B13}' -> '#N/A' | C13: '2AYTXVH3H4248A' | D13: 55.35 | A14: '4GXCD018AC6HUA' | B14: '=INDEX(D:D,MATCH(A14,C:C,0)) {array B14}' -> '#N/A' | C14: '2AYTXVH3H6060A' | D14: 55.35 | A15: '4MXC8512A10N0A' | B15: '=INDEX(D:D,MATCH(A15,C:C,0)) {array B15}' -> '#N/A' | C15: '4AYTXVH3G2436A' | D15: 53.3

### `30c6f4937476|LIVE_ERROR|HR!AY10`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !AY10`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 1 dependent cell(s): HR !AY24. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'N/A'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: AW8: '=AW7' -> 2019-10-01 00:00:00 | AX8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | AY8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | AZ8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BA8: '=AQ8' -> '#REF!' | AW10: 2019-10-01 00:00:00 | AX10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | AY10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | AZ10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | BA10: '=AQ10' -> '#REF!' | AW11: '=AW10' -> 2019-10-01 00:00:00 | AX11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | AY11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | AZ11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | BA11: '=AQ11' -> '#REF!' | AW12: 2019-10-01 00:00:00 | AX12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AY12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AZ12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BA12: '=AQ12' -> '#REF!'

### `0eccd3d05dde|LIVE_ERROR|Type2!J17`

- workbook: `all_data_912_v0.1/spreadsheet/53068/2_53068_input.xlsx`
- location: `Type 2!J17`  severity: Critical  confidence: Defect
- evidence: Cell contains #DIV/0!.
- cached value: '#DIV/0!'; row labels: ["'Base Salary for PS'"]; column header: ''; used range: A1:S27
- neighbourhood: H15: '=$F$4/$M$4' -> 119.277108433735 | I15: '=$F$4/$M$4' -> 119.277108433735 | J15: '=$F$4/$M$4' -> 119.277108433735 | K15: '=$F$4/$M$4' -> 119.277108433735 | L15: '=$F$4/$M$4' -> 119.277108433735 | H16: '=H15*H13' -> 2624.09638554217 | I16: '=I15*I13' -> 2624.09638554217 | J16: '=J15*J13' -> 2504.81927710843 | K16: '=K15*K13' -> 2504.81927710843 | L16: '=L15*L13' -> 2504.81927710843 | H17: '=H16/$I$4' -> '#DIV/0!' | I17: '=I16/$I$4' -> '#DIV/0!' | J17: '=J16/$I$4' -> '#DIV/0!' | K17: '=K16/$I$4' -> '#DIV/0!' | L17: '=L16/$I$4' -> '#DIV/0!'

### `192a19040f63|LIVE_ERROR|Sheettwo!E263`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E263`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0086112400'"]; column header: ''; used range: A1:G6234
- neighbourhood: C261: '1D' | D261: '0085458023' | E261: '=VLOOKUP(G261,Suppliers2[],2,FALSE)' -> '#N/A' | F261: '017962' | G261: '33325152' | C262: '7D' | D262: '0000000856' | E262: '=VLOOKUP(G262,Suppliers2[],2,FALSE)' -> '#N/A' | F262: '018075' | G262: '88713000' | C263: '1D' | D263: '0086112400' | E263: '=VLOOKUP(G263,Suppliers2[],2,FALSE)' -> '#N/A' | F263: '018147' | G263: '44533388' | C264: '1D' | D264: '0086236500' | E264: '=VLOOKUP(G264,Suppliers2[],2,FALSE)' -> '#N/A' | F264: '018227' | G264: '65958987' | C265: '3D' | D265: '0086240822' | E265: '=VLOOKUP(G265,Suppliers2[],2,FALSE)' -> '#N/A' | F265: '018502' | G265: '70263016'

### `a4ee03c3468a|LIVE_ERROR|HR!BJ7`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !BJ7`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 1 dependent cell(s): HR !BJ24. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'Yes'", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: BH5: 2019-11-01 00:00:00 | BI5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BJ5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BK5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BL5: '=BB5' -> 'Yes' | BH7: 2019-11-01 00:00:00 | BI7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BJ7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BK7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BL7: '=BB7' -> '#REF!' | BH8: 2019-11-01 00:00:00 | BI8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BJ8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BK8: "=INDEX(#REF!,MATCH('HR '!$A8,#REF!,0))" -> '#REF!' | BL8: '=BB8' -> '#REF!'

### `7cc6b0fe1206|LIVE_ERROR|Sort!L78`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!L78`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2013_Q3'"]; column header: ''; used range: A1:T147
- neighbourhood: J76: "=VLOOKUP($B76,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 32.260000000000005 | K76: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A76,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L76: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A76,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M76: '=D76*P76' -> '#VALUE!' | N76: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A76,'[1]<2030Cal'!$M$12:$M$... -> '#VALUE!' | J77: "=VLOOKUP($B77,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 21.4 | K77: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A77,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L77: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A77,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M77: '=D77*P77' -> '#VALUE!' | N77: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A77,'[1]<2030Cal'!$M$12:$M$... -> '#VALUE!' | J78: "=VLOOKUP($B78,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 13.149999999999999 | K78: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A78,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L78: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A78,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M78: '=D78*P78' -> '#VALUE!' | N78: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A78,'[1]<2030Cal'!$M$12:$M$... -> '#VALUE!' | J79: "=VLOOKUP($B79,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 5.66 | K79: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A79,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L79: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A79,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M79: '=D79*P79' -> '#VALUE!' | N79: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A79,'[1]<2030Cal'!$M$12:$M$... -> '#VALUE!' | J80: "=VLOOKUP($B80,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 5.76 | K80: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A80,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L80: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A80,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M80: '=D80*P80' -> '#VALUE!' | N80: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A80,'[1]<2030Cal'!$M$12:$M$... -> '#VALUE!'

### `fd54be33aa9b|LIVE_ERROR|Exp-DB!G37`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/3_524-31_input.xlsx`
- location: `Exp-DB!G37`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'water'", "'POS Adjustment - BEST BUY 0000 SPRINGFIELD VA'"]; column header: ''; used range: A1:G53
- neighbourhood: E35: '=VLOOKUP(D35 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G35: '=INDEX(cats,MATCH("*"&D35&"*",exDB,0))' -> '#N/A' | E36: '=VLOOKUP(D36 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G36: '=INDEX(cats,MATCH("*"&D36&"*",exDB,0))' -> '#N/A' | E37: '=VLOOKUP(D37 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G37: '=INDEX(cats,MATCH("*"&D37&"*",exDB,0))' -> '#N/A' | E38: '=VLOOKUP(D38 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G38: '=INDEX(cats,MATCH("*"&D38&"*",exDB,0))' -> '#N/A' | E39: '=VLOOKUP(D39 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G39: '=INDEX(cats,MATCH("*"&D39&"*",exDB,0))' -> '#N/A'

### `d207f4db35f5|LIVE_ERROR|Sheet1!K5`

- workbook: `all_data_912_v0.1/spreadsheet/48685/3_48685_input.xlsx`
- location: `Sheet1!K5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'A1'", "'PartA1'"]; column header: ''; used range: A1:K12
- neighbourhood: I3: 'Bom QtyReq' | J3: 'InStock' | K3: 'SubTotal' | K4: '=IF(E4="","",E4+K1)' -> 5:22:46 | I5: 426 | J5: 0 | K5: '=IF(E5="","",E5+K3)' -> '#VALUE!' | K6: '=IF(E6="","",E6+#REF!)' -> None | K7: '=IF(E7="","",E7+K4)' -> None

## NUMBERS_STORED_AS_TEXT

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A1031`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A1031`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2721' in a column that otherwise holds 1547 numbers.
- cached value: '2721'; row labels: []; column header: "'2720'"; used range: A1:K2802
- neighbourhood: A1029: '2719' | B1029: '2500074660' | C1029: 2018-09-10 00:00:00 | A1030: '2720' | B1030: '2500074660' | C1030: 2018-09-10 00:00:00 | A1031: '2721' | B1031: '2500074660' | C1031: 2018-09-10 00:00:00 | A1032: '2722' | B1032: '2500074660' | C1032: 2018-09-10 00:00:00 | A1033: '1455' | B1033: 1500006150 | C1033: 2018-09-11 00:00:00

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1086`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1086`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1605' in a column that otherwise holds 1547 numbers.
- cached value: '1605'; row labels: []; column header: "'1596'"; used range: A1:K2802
- neighbourhood: A1084: '1588' | B1084: 1500006150 | C1084: 2018-10-02 00:00:00 | A1085: '1596' | B1085: 1500006150 | C1085: 2018-10-02 00:00:00 | A1086: '1605' | B1086: 1500006150 | C1086: 2018-10-02 00:00:00 | A1087: '1618' | B1087: 1500006150 | C1087: 2018-10-02 00:00:00 | A1088: '1619' | B1088: 1500006150 | C1088: 2018-10-02 00:00:00

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet2!E29`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet2!E29`  severity: Medium  confidence: Review
- evidence: Cell contains text value '15334' in a column that otherwise holds 55 numbers.
- cached value: '15334'; row labels: ["'O2'", "'2G'"]; column header: "'Serving Cells'"; used range: A1:Z168
- neighbourhood: D27: '4G' | E27: 102403 | F27: 122134 | G27: 113432 | C28: 'Network ' | D28: 'Generation' | E28: 'Serving Cells' | C29: 'O2' | D29: '2G' | E29: '15334' | D30: '3G' | E30: '40045' | F30: '50045' | D31: '4G' | E31: 134333352

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1030`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1030`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2720' in a column that otherwise holds 1547 numbers.
- cached value: '2720'; row labels: []; column header: "'2719'"; used range: A1:K2802
- neighbourhood: A1028: '2718' | B1028: '2500074660' | C1028: 2018-09-10 00:00:00 | A1029: '2719' | B1029: '2500074660' | C1029: 2018-09-10 00:00:00 | A1030: '2720' | B1030: '2500074660' | C1030: 2018-09-10 00:00:00 | A1031: '2721' | B1031: '2500074660' | C1031: 2018-09-10 00:00:00 | A1032: '2722' | B1032: '2500074660' | C1032: 2018-09-10 00:00:00

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A1012`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A1012`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1479' in a column that otherwise holds 1547 numbers.
- cached value: '1479'; row labels: []; column header: "'1469'"; used range: A1:K2802
- neighbourhood: A1010: '1466' | B1010: 1500006150 | C1010: 2018-09-08 00:00:00 | A1011: '1469' | B1011: 1500006150 | C1011: 2018-09-08 00:00:00 | A1012: '1479' | B1012: 1500006150 | C1012: 2018-09-08 00:00:00 | A1013: '1451' | B1013: 1500006150 | C1013: 2018-09-10 00:00:00 | A1014: '1453' | B1014: 1500006150 | C1014: 2018-09-10 00:00:00

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A114`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A114`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1255' in a column that otherwise holds 1547 numbers.
- cached value: '1255'; row labels: []; column header: "'1095'"; used range: A1:K2802
- neighbourhood: A112: '1094' | B112: 2500072970 | C112: 2018-03-08 00:00:00 | A113: '1095' | B113: 2500072970 | C113: 2018-03-08 00:00:00 | A114: '1255' | B114: 4500041932 | C114: 2018-03-08 00:00:00 | A115: '1256' | B115: 4500041932 | C115: 2018-03-08 00:00:00 | A116: '1040' | B116: 2500072620 | C116: 2018-03-12 00:00:00

### `9ea22c621bf1|NUMBERS_STORED_AS_TEXT|Sheet1!A13`

- workbook: `all_data_912_v0.1/spreadsheet/15671/3_15671_input.xlsx`
- location: `Sheet1!A13`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313335259935' in a column that otherwise holds 250 numbers.
- cached value: '911313335259935'; row labels: []; column header: "'913313327497499'"; used range: A1:A269
- neighbourhood: A11: '913313327497567' | A12: '913313327497499' | A13: '911313335259935' | A14: '911313335263142' | A15: '911313335259896'

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A1018`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A1018`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1475' in a column that otherwise holds 1547 numbers.
- cached value: '1475'; row labels: []; column header: "'1474'"; used range: A1:K2802
- neighbourhood: A1016: '1463' | B1016: 1500006150 | C1016: 2018-09-10 00:00:00 | A1017: '1474' | B1017: 1500006150 | C1017: 2018-09-10 00:00:00 | A1018: '1475' | B1018: 1500006150 | C1018: 2018-09-10 00:00:00 | A1019: '1482' | B1019: 1500006150 | C1019: 2018-09-10 00:00:00 | A1020: '1496' | B1020: 1500006150 | C1020: 2018-09-10 00:00:00

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet2!H52`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet2!H52`  severity: Medium  confidence: Review
- evidence: Cell contains text value '34113' in a column that otherwise holds 33 numbers.
- cached value: '34113'; row labels: ["'3G'"]; column header: ''; used range: A1:Z168
- neighbourhood: F51: 20214 | G51: 21111 | H51: 25443 | I51: 34301 | J51: 33005 | F52: 22323 | G52: 33025 | H52: '34113' | F53: 122314104 | G53: '134045314' | F54: 24102 | G54: 24101 | H54: 43531

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!F60`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!F60`  severity: Medium  confidence: Review
- evidence: Cell contains text value '13421' in a column that otherwise holds 47 numbers.
- cached value: '13421'; row labels: ["'O2'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D58: '4G' | E58: 1035203 | D59: 'Generation' | E59: 'Serving Cells' | D60: '2G' | E60: 13411 | F60: '13421' | G60: 11153 | H60: 21430 | D61: '3G' | E61: '14532' | F61: '33332' | G61: 51242 | H61: 55233 | D62: '4G' | E62: 135134244

### `9ea22c621bf1|NUMBERS_STORED_AS_TEXT|Sheet1!A4`

- workbook: `all_data_912_v0.1/spreadsheet/15671/3_15671_input.xlsx`
- location: `Sheet1!A4`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313323763534' in a column that otherwise holds 250 numbers.
- cached value: '913313323763534'; row labels: []; column header: "'913313331477314'"; used range: A1:A269
- neighbourhood: A2: '913313331154234' | A3: '913313331477314' | A4: '913313323763534' | A5: '913313323763473' | A6: '913313329226819'

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!E17`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!E17`  severity: Medium  confidence: Review
- evidence: Cell contains text value '51221' in a column that otherwise holds 55 numbers.
- cached value: '51221'; row labels: ["'H3'", "'3G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D15: '3G' | E15: 2204 | D16: '4G' | E16: 14454001 | F16: 14454004 | G16: 14454010 | C17: 'H3' | D17: '3G' | E17: '51221' | F17: 40341 | D18: '4G' | E18: 141213 | F18: 141223 | G18: 141222 | C19: 'Network ' | D19: 'Generation' | E19: 'Serving Cells'

### `7e6034cae12d|NUMBERS_STORED_AS_TEXT|Sheet1!A14`

- workbook: `all_data_912_v0.1/spreadsheet/15671/2_15671_input.xlsx`
- location: `Sheet1!A14`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313335263142' in a column that otherwise holds 250 numbers.
- cached value: '911313335263142'; row labels: []; column header: "'911313335259935'"; used range: A1:A269
- neighbourhood: A12: '913313327497499' | A13: '911313335259935' | A14: '911313335263142' | A15: '911313335259896' | A16: '911313317514666'

### `7e6034cae12d|NUMBERS_STORED_AS_TEXT|Sheet1!A8`

- workbook: `all_data_912_v0.1/spreadsheet/15671/2_15671_input.xlsx`
- location: `Sheet1!A8`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313329228226' in a column that otherwise holds 250 numbers.
- cached value: '913313329228226'; row labels: []; column header: "'913313343567715'"; used range: A1:A269
- neighbourhood: A6: '913313329226819' | A7: '913313343567715' | A8: '913313329228226' | A9: '911313318355914' | A10: '913313327498337'

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet2!F34`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet2!F34`  severity: Medium  confidence: Review
- evidence: Cell contains text value '21252' in a column that otherwise holds 47 numbers.
- cached value: '21252'; row labels: ["'3G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D32: 'Generation' | E32: 'Serving Cells' | D33: '2G' | E33: 23222 | F33: 33222 | D34: '3G' | E34: 13230 | F34: '21252' | G34: 22402 | D35: '4G' | E35: 135242504 | F35: 135242502 | G35: 135242501 | H35: 135242344 | D36: '2G' | E36: 1341 | F36: '23342' | G36: 52553 | H36: 51212

### `1a12611d45b2|NUMBERS_STORED_AS_TEXT|Sheet1!A6`

- workbook: `all_data_912_v0.1/spreadsheet/15671/1_15671_input.xlsx`
- location: `Sheet1!A6`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313329226819' in a column that otherwise holds 250 numbers.
- cached value: '913313329226819'; row labels: []; column header: "'913313323763473'"; used range: A1:A269
- neighbourhood: A4: '913313323763536' | A5: '913313323763473' | A6: '913313329226819' | A7: '913313343567715' | A8: '913313329228226'

### `1a12611d45b2|NUMBERS_STORED_AS_TEXT|Sheet1!A17`

- workbook: `all_data_912_v0.1/spreadsheet/15671/1_15671_input.xlsx`
- location: `Sheet1!A17`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313335263334' in a column that otherwise holds 250 numbers.
- cached value: '911313335263334'; row labels: []; column header: "'911313317514666'"; used range: A1:A269
- neighbourhood: A15: '911313335259896' | A16: '911313317514666' | A17: '911313335263334' | A18: '911313335263168' | A19: '911313335263133'

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet1!F26`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet1!F26`  severity: Medium  confidence: Review
- evidence: Cell contains text value '32131' in a column that otherwise holds 45 numbers.
- cached value: '32131'; row labels: ["'3'", "'3G'"]; column header: ''; used range: A1:J168
- neighbourhood: D24: '3G' | E24: 32334 | F24: 32333 | G24: 32332 | H24: 44321 | D25: '4G' | E25: '10415013\n 15124012' | F25: 10450000 | G25: 10450002 | H25: 10450003 | D26: '3G' | E26: 21450 | F26: '32131' | G26: '32134' | H26: 34115 | D27: '4G' | E27: 102403 | F27: 122134 | G27: 113432 | H27: 113303 | D28: 'Generation' | E28: 'Serving Cells'

### `4cb669285990|NUMBERS_STORED_AS_TEXT|Sheet1!I8`

- workbook: `all_data_912_v0.1/spreadsheet/418-25/2_418-25_input.xlsx`
- location: `Sheet1!I8`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1771 ' in a column that otherwise holds 7 numbers.
- cached value: '1771 '; row labels: ["'MQ-818YEJ'", "'Purchase Ordering'"]; column header: "'2391  Sammy'"; used range: A1:I27
- neighbourhood: I6: '1791 REFUND ' | I7: '2391  Sammy' | I8: '1771 ' | I9: '1611  Sammy jonker' | I10: '2002 jW 78 WF GP'

### `38689259b288|NUMBERS_STORED_AS_TEXT|Sheet2!E2`

- workbook: `all_data_912_v0.1/spreadsheet/453-49/2_453-49_input.xlsx`
- location: `Sheet2!E2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '7460118' in a column that otherwise holds 5 numbers.
- cached value: '7460118'; row labels: ["'PPL2122075'"]; column header: "'Batch'"; used range: A1:M7
- neighbourhood: C1: 'SLoc' | D1: 'S' | E1: 'Batch' | F1: 'S' | G1: 'Special Stock Number' | E2: '7460118' | E3: 7460987 | E4: 1234567

### `a3b766273873|NUMBERS_STORED_AS_TEXT|GLDetails!A11`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/3_601-4_input.xlsx`
- location: `GL Details!A11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '322115' in a column that otherwise holds 9 numbers.
- cached value: '322115'; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: A9: 102985 | C9: 299030 | A10: 102985 | C10: 122200 | A11: '322115' | C11: 108250

### `7094b0a39fbe|NUMBERS_STORED_AS_TEXT|Sheet2!E2`

- workbook: `all_data_912_v0.1/spreadsheet/453-49/3_453-49_input.xlsx`
- location: `Sheet2!E2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '7460118' in a column that otherwise holds 5 numbers.
- cached value: '7460118'; row labels: ["'PPL2122075'"]; column header: "'Batch'"; used range: A1:M7
- neighbourhood: C1: 'SLoc' | D1: 'S' | E1: 'Batch' | F1: 'S' | G1: 'Special Stock Number' | E2: '7460118' | E3: 7460987 | E4: 1234567

### `8985b82c7663|NUMBERS_STORED_AS_TEXT|Sheet1!C1`

- workbook: `all_data_912_v0.1/spreadsheet/94-28/3_94-28_input.xlsx`
- location: `Sheet1!C1`  severity: Medium  confidence: Review
- evidence: Cell contains text value '\xa087682.95' in a column that otherwise holds 3 numbers.
- cached value: '\xa087682.95'; row labels: []; column header: ''; used range: A1:C4
- neighbourhood: C1: '\xa087682.95' | C2: 3.6 | C3: 314257.6

### `f9a4a862417e|NUMBERS_STORED_AS_TEXT|Sheet1!A6`

- workbook: `all_data_912_v0.1/spreadsheet/53117/3_53117_input.xlsx`
- location: `Sheet1!A6`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1065414' in a column that otherwise holds 22 numbers.
- cached value: '1065414'; row labels: []; column header: "'1065414'"; used range: A1:G27
- neighbourhood: A4: '1065414' | B4: 4160 | C4: 'Japan' | A5: '1065414' | B5: 432.84 | C5: 'Canada' | A6: '1065414' | B6: 4995 | C6: 'Canada' | A7: 1001130 | B7: 141500 | C7: 'Canada' | A8: 1001130 | B8: 1122 | C8: 'Canada'

### `35eccaaedf70|NUMBERS_STORED_AS_TEXT|Sheet1!A4`

- workbook: `all_data_912_v0.1/spreadsheet/53117/2_53117_input.xlsx`
- location: `Sheet1!A4`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1065414' in a column that otherwise holds 22 numbers.
- cached value: '1065414'; row labels: []; column header: "'1065414'"; used range: A1:G27
- neighbourhood: A2: 1065414 | B2: 333.33 | C2: 'US' | A3: '1065414' | B3: -4160 | C3: 'Canada' | A4: '1065414' | B4: 4160 | C4: 'US' | A5: '1065414' | B5: 432.84 | C5: 'Canada' | A6: '1065414' | B6: 4995 | C6: 'Canada'

## RANGE_EXCLUSION

### `070be904b648|RANGE_EXCLUSION|Vat!I24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/2_49859_input.xlsx`
- location: `Vat!I24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(I12:I19)`
- evidence: Vat!I12:I19 stops short of Vat!I20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range I12:I19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'I11: 6', 'below': 'I20: 0'}
- neighbourhood: G22: 1 | H22: 0 | I22: 0 | J22: 1 | G23: 1 | H23: 0 | I23: 0 | J23: 1 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4 | I24: '=SUM(I12:I19)' -> 4 | J24: '=SUM(J16:J23)' -> 4 | K24: '=SUM(K12:K23)' -> 0

### `b4e955369429|RANGE_EXCLUSION|Vat!I24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/3_49859_input.xlsx`
- location: `Vat!I24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(I12:I19)`
- evidence: Vat!I12:I19 stops short of Vat!I20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range I12:I19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'I11: 6', 'below': 'I20: 0'}
- neighbourhood: G22: 1 | H22: 0 | I22: 0 | J22: 1 | G23: 1 | H23: 0 | I23: 0 | J23: 1 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4 | I24: '=SUM(I12:I19)' -> 4 | J24: '=SUM(J16:J23)' -> 4 | K24: '=SUM(K12:K23)' -> 0

### `b4e955369429|RANGE_EXCLUSION|Vat!F24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/3_49859_input.xlsx`
- location: `Vat!F24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(F12:F19)`
- evidence: Vat!F12:F19 stops short of Vat!F20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range F12:F19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'F11: 3', 'below': 'F20: 0'}
- neighbourhood: D22: 0 | E22: 0 | F22: 0 | G22: 1 | H22: 0 | D23: 0 | E23: 0 | F23: 0 | G23: 1 | H23: 0 | D24: '=SUM(D12:D23)' -> 4 | E24: '=SUM(E12:E23)' -> 4 | F24: '=SUM(F12:F19)' -> 4 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4

### `070be904b648|RANGE_EXCLUSION|Vat!F24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/2_49859_input.xlsx`
- location: `Vat!F24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(F12:F19)`
- evidence: Vat!F12:F19 stops short of Vat!F20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range F12:F19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'F11: 3', 'below': 'F20: 0'}
- neighbourhood: D22: 0 | E22: 0 | F22: 0 | G22: 1 | H22: 0 | D23: 0 | E23: 0 | F23: 0 | G23: 1 | H23: 0 | D24: '=SUM(D12:D23)' -> 4 | E24: '=SUM(E12:E23)' -> 4 | F24: '=SUM(F12:F19)' -> 4 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4

## RANGE_LENGTH_MISMATCH

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!I152`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!I152`  severity: High  confidence: Likely defect
- formula: `=COUNT(D150:F152)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D150:F152: values ['108', '110', '95', '106', '106', '88', '126', '125', '116']; beyond: {}
- neighbourhood: G150: '=SUM(D150:F150)' -> 313 | H150: '=SUM(G150:G150)' -> 313 | I150: '=COUNT(D150:F150)' -> 3 | J150: '=IF(I150=0,0,(ROUNDDOWN(H150/I150,0)))' -> 104 | K150: '=IFERROR(IF(I149>=12,IF($J149<=100,0+SUBSTITUTE(IF($D150>=125,","&... -> None | G151: '=SUM(D151:F151)' -> 300 | H151: '=SUM(G150:G151)' -> 613 | I151: '=COUNT(D150:F151)' -> 6 | J151: '=IF(I151=0,0,(ROUNDDOWN(H151/I151,0)))' -> 102 | K151: '=IFERROR(IF(I150>=12,IF($J150<=100,0+SUBSTITUTE(IF($D151>=125,","&... -> None | G152: '=SUM(D152:F152)' -> 367 | H152: '=SUM(G150:G152)' -> 980 | I152: '=COUNT(D150:F152)' -> 9 | J152: '=IF(I152=0,0,(ROUNDDOWN(H152/I152,0)))' -> 108 | K152: '=IFERROR(IF(I151>=12,IF($J151<=100,0+SUBSTITUTE(IF($D152>=125,","&... -> None | G153: '=SUM(D153:F153)' -> 334 | H153: '=SUM(G150:G153)' -> 1314 | I153: '=COUNT(D150:F153)' -> 12 | J153: '=IF(I153=0,0,(ROUNDDOWN(H153/I153,0)))' -> 109 | K153: '=IFERROR(IF(I152>=12,IF($J152<=100,0+SUBSTITUTE(IF($D153>=125,","&... -> None | G154: '=SUM(D154:F154)' -> 371 | H154: '=SUM(G150:G154)' -> 1685 | I154: '=COUNT(D150:F154)' -> 15 | J154: '=IF(I154=0,0,(ROUNDDOWN(H154/I154,0)))' -> 112 | K154: '=IFERROR(IF(I153>=12,IF($J153<=100,0+SUBSTITUTE(IF($D154>=125,","&... -> None

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!I5`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!I5`  severity: High  confidence: Likely defect
- formula: `=COUNT(D3:F5)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 6; row labels: []; column header: ''; used range: A1:CJ782
- range D3:F5: values ['97', '97', '97', '123', '125', '124', 'None', 'None', 'None']; beyond: {}
- neighbourhood: G3: '=SUM(D3:F3)' -> 291 | H3: '=SUM(G3:G3)' -> 291 | I3: 3 | J3: '=IF(I3=0,0,(ROUNDDOWN(H3/I3,0)))' -> 97 | K3: '=IFERROR(IF(I2>=12,IF($J2<=100,0+SUBSTITUTE(IF($D3>=125,","&$D3,""... -> None | G4: '=SUM(D4:F4)' -> 372 | H4: '=SUM(G3:G4)' -> 663 | I4: '=COUNT(D3:F4)' -> 6 | J4: '=IF(I4=0,0,(ROUNDDOWN(H4/I4,0)))' -> 110 | K4: '=IFERROR(IF(I3>=12,IF($J3<=100,0+SUBSTITUTE(IF($D4>=125,","&$D4,""... -> None | G5: '=SUM(D5:F5)' -> 0 | H5: '=SUM(G3:G5)' -> 663 | I5: '=COUNT(D3:F5)' -> 6 | J5: '=IF(I5=0,0,(ROUNDDOWN(H5/I5,0)))' -> 110 | K5: '=IFERROR(IF(I4>=12,IF($J4<=100,0+SUBSTITUTE(IF($D5>=125,","&$D5,""... -> None | G6: '=SUM(D6:F6)' -> 340 | H6: '=SUM(G3:G6)' -> 1003 | I6: '=COUNT(D3:F6)' -> 9 | J6: '=IF(I6=0,0,(ROUNDDOWN(H6/I6,0)))' -> 111 | K6: '=IFERROR(IF(I5>=12,IF($J5<=100,0+SUBSTITUTE(IF($D6>=125,","&$D6,""... -> None | G7: '=SUM(D7:F7)' -> 302 | H7: '=SUM(G3:G7)' -> 1305 | I7: '=COUNT(D3:F7)' -> 12 | J7: '=IF(I7=0,0,(ROUNDDOWN(H7/I7,0)))' -> 108 | K7: '=IFERROR(IF(I6>=12,IF($J6<=100,0+SUBSTITUTE(IF($D7>=125,","&$D7,""... -> None

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I194`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I194`  severity: High  confidence: Likely defect
- formula: `=COUNT(D192:F194)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 0; row labels: []; column header: ''; used range: A1:CJ782
- range D192:F194: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {}
- neighbourhood: G192: '=SUM(D192:F192)' -> 0 | H192: '=SUM(G192:G192)' -> 0 | I192: '=COUNT(D192:F192)' -> 0 | J192: '=IF(I192=0,0,(ROUNDDOWN(H192/I192,0)))' -> 0 | K192: '=IFERROR(IF(I191>=12,IF($J191<=100,0+SUBSTITUTE(IF($D192>=125,","&... -> None | G193: '=SUM(D193:F193)' -> 0 | H193: '=SUM(G192:G193)' -> 0 | I193: '=COUNT(D192:F193)' -> 0 | J193: '=IF(I193=0,0,(ROUNDDOWN(H193/I193,0)))' -> 0 | K193: '=IFERROR(IF(I192>=12,IF($J192<=100,0+SUBSTITUTE(IF($D193>=125,","&... -> None | G194: '=SUM(D194:F194)' -> 0 | H194: '=SUM(G192:G194)' -> 0 | I194: '=COUNT(D192:F194)' -> 0 | J194: '=IF(I194=0,0,(ROUNDDOWN(H194/I194,0)))' -> 0 | K194: '=IFERROR(IF(I193>=12,IF($J193<=100,0+SUBSTITUTE(IF($D194>=125,","&... -> None | G195: '=SUM(D195:F195)' -> 0 | H195: '=SUM(G192:G195)' -> 0 | I195: '=COUNT(D192:F195)' -> 0 | J195: '=IF(I195=0,0,(ROUNDDOWN(H195/I195,0)))' -> 0 | K195: '=IFERROR(IF(I194>=12,IF($J194<=100,0+SUBSTITUTE(IF($D195>=125,","&... -> None | G196: '=SUM(D196:F196)' -> 0 | H196: '=SUM(G192:G196)' -> 0 | I196: '=COUNT(D192:F196)' -> 0 | J196: '=IF(I196=0,0,(ROUNDDOWN(H196/I196,0)))' -> 0 | K196: '=IFERROR(IF(I195>=12,IF($J195<=100,0+SUBSTITUTE(IF($D196>=125,","&... -> None

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!I278`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!I278`  severity: High  confidence: Likely defect
- formula: `=COUNT(D276:F278)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D276:F278: values ['132', '109', '111', '122', '128', '129', '138', '133', '107']; beyond: {}
- neighbourhood: G276: '=SUM(D276:F276)' -> 352 | H276: '=SUM(G276)' -> 352 | I276: '=COUNT(D276:F276)' -> 3 | J276: '=IF(I276=0,0,(ROUNDDOWN(H276/I276,0)))' -> 117 | K276: '=IFERROR(IF(I275>=12,IF($J275<=100,0+SUBSTITUTE(IF($D276>=125,","&... -> None | G277: '=SUM(D277:F277)' -> 379 | H277: '=SUM(G276:G277)' -> 731 | I277: '=COUNT(D276:F277)' -> 6 | J277: '=IF(I277=0,0,(ROUNDDOWN(H277/I277,0)))' -> 121 | K277: '=IFERROR(IF(I276>=12,IF($J276<=100,0+SUBSTITUTE(IF($D277>=125,","&... -> None | G278: '=SUM(D278:F278)' -> 378 | H278: '=SUM(G276:G278)' -> 1109 | I278: '=COUNT(D276:F278)' -> 9 | J278: '=IF(I278=0,0,(ROUNDDOWN(H278/I278,0)))' -> 123 | K278: '=IFERROR(IF(I277>=12,IF($J277<=100,0+SUBSTITUTE(IF($D278>=125,","&... -> None | G279: '=SUM(D279:F279)' -> 384 | H279: '=SUM(G276:G279)' -> 1493 | I279: '=COUNT(D276:F279)' -> 12 | J279: '=IF(I279=0,0,(ROUNDDOWN(H279/I279,0)))' -> 124 | K279: '=IFERROR(IF(I278>=12,IF($J278<=100,0+SUBSTITUTE(IF($D279>=125,","&... -> None | G280: '=SUM(D280:F280)' -> 458 | H280: '=SUM(G276:G280)' -> 1951 | I280: '=COUNT(D276:F280)' -> 15 | J280: '=IF(I280=0,0,(ROUNDDOWN(H280/I280,0)))' -> 130 | K280: '=IFERROR(IF(I279>=12,IF($J279<=100,0+SUBSTITUTE(IF($D280>=125,","&... -> None

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!I215`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!I215`  severity: High  confidence: Likely defect
- formula: `=COUNT(D213:F215)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D213:F215: values ['114', '97', '124', '113', '128', '98', '127', '114', '116']; beyond: {}
- neighbourhood: G213: '=SUM(D213:F213)' -> 335 | H213: '=SUM(G213:G213)' -> 335 | I213: '=COUNT(D213:F213)' -> 3 | J213: '=IF(I213=0,0,(ROUNDDOWN(H213/I213,0)))' -> 111 | K213: '=IFERROR(IF(I212>=12,IF($J212<=100,0+SUBSTITUTE(IF($D213>=125,","&... -> None | G214: '=SUM(D214:F214)' -> 339 | H214: '=SUM(G213:G214)' -> 674 | I214: '=COUNT(D213:F214)' -> 6 | J214: '=IF(I214=0,0,(ROUNDDOWN(H214/I214,0)))' -> 112 | K214: '=IFERROR(IF(I213>=12,IF($J213<=100,0+SUBSTITUTE(IF($D214>=125,","&... -> None | G215: '=SUM(D215:F215)' -> 357 | H215: '=SUM(G213:G215)' -> 1031 | I215: '=COUNT(D213:F215)' -> 9 | J215: '=IF(I215=0,0,(ROUNDDOWN(H215/I215,0)))' -> 114 | K215: '=IFERROR(IF(I214>=12,IF($J214<=100,0+SUBSTITUTE(IF($D215>=125,","&... -> None | G216: '=SUM(D216:F216)' -> 309 | H216: '=SUM(G213:G216)' -> 1340 | I216: '=COUNT(D213:F216)' -> 12 | J216: '=IF(I216=0,0,(ROUNDDOWN(H216/I216,0)))' -> 111 | K216: '=IFERROR(IF(I215>=12,IF($J215<=100,0+SUBSTITUTE(IF($D216>=125,","&... -> None | G217: '=SUM(D217:F217)' -> 329 | H217: '=SUM(G213:G217)' -> 1669 | I217: '=COUNT(D213:F217)' -> 15 | J217: '=IF(I217=0,0,(ROUNDDOWN(H217/I217,0)))' -> 111 | K217: '=IFERROR(IF(I216>=12,IF($J216<=100,0+SUBSTITUTE(IF($D217>=125,","&... -> None

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I26`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I26`  severity: High  confidence: Likely defect
- formula: `=COUNT(D24:F26)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D24:F26: values ['149', '105', '123', '100', '131', '122', '130', '130', '130']; beyond: {}
- neighbourhood: G24: '=SUM(D24:F24)' -> 377 | H24: '=SUM(G24:G24)' -> 377 | I24: '=COUNT(D24:F24)' -> 3 | J24: '=IF(I24=0,0,(ROUNDDOWN(H24/I24,0)))' -> 125 | K24: '=IFERROR(IF(I23>=12,IF($J23<=100,0+SUBSTITUTE(IF($D24>=125,","&$D2... -> None | G25: '=SUM(D25:F25)' -> 353 | H25: '=SUM(G24:G25)' -> 730 | I25: '=COUNT(D24:F25)' -> 6 | J25: '=IF(I25=0,0,(ROUNDDOWN(H25/I25,0)))' -> 121 | K25: '=IFERROR(IF(I24>=12,IF($J24<=100,0+SUBSTITUTE(IF($D25>=125,","&$D2... -> None | G26: '=SUM(D26:F26)' -> 390 | H26: '=SUM(G24:G26)' -> 1120 | I26: '=COUNT(D24:F26)' -> 9 | J26: '=IF(I26=0,0,(ROUNDDOWN(H26/I26,0)))' -> 124 | K26: '=IFERROR(IF(I25>=12,IF($J25<=100,0+SUBSTITUTE(IF($D26>=125,","&$D2... -> None | G27: '=SUM(D27:F27)' -> 322 | H27: '=SUM(G24:G27)' -> 1442 | I27: '=COUNT(D24:F27)' -> 12 | J27: '=IF(I27=0,0,(ROUNDDOWN(H27/I27,0)))' -> 120 | K27: '=IFERROR(IF(I26>=12,IF($J26<=100,0+SUBSTITUTE(IF($D27>=125,","&$D2... -> None | G28: '=SUM(D28:F28)' -> 337 | H28: '=SUM(G24:G28)' -> 1779 | I28: '=COUNT(D24:F28)' -> 15 | J28: '=IF(I28=0,0,(ROUNDDOWN(H28/I28,0)))' -> 118 | K28: '=IFERROR(IF(I27>=12,IF($J27<=100,0+SUBSTITUTE(IF($D28>=125,","&$D2... -> None

## VOLATILE_FUNCTION

### `3a4af9c80244|VOLATILE_FUNCTION|Sheet1!D3`

- workbook: `all_data_912_v0.1/spreadsheet/57376/3_57376_input.xlsx`
- location: `Sheet1!D3`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(50,750)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 50 cells on this sheet; the others are Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, Sheet1!D10, Sheet1!D11, ....
- cached value: 608; row labels: []; column header: "'rang_val'"; used range: A1:G30002
- neighbourhood: C2: 'rang_id' | D2: 'rang_val' | E2: 'start date' | F2: 'end date' | C3: '=_xlfn.SEQUENCE(30000,,1001,1) {array C3:C30002}' -> 1001 | D3: '=RANDBETWEEN(50,750)' -> 608 | E3: 2021-01-03 00:00:00 | F3: '=RANDBETWEEN(E3+14,E3+RAND()*100)' -> 2021-01-21 00:00:00 | C4: 1002 | D4: '=RANDBETWEEN(50,750)' -> 323 | E4: 2021-01-02 00:00:00 | F4: '=RANDBETWEEN(E4+14,E4+RAND()*100)' -> 2021-01-29 00:00:00 | C5: 1003 | D5: '=RANDBETWEEN(50,750)' -> 516 | E5: 2021-01-02 00:00:00 | F5: '=RANDBETWEEN(E5+14,E5+RAND()*100)' -> 2021-03-11 00:00:00

### `97867082584b|VOLATILE_FUNCTION|Sheet1!K1`

- workbook: `all_data_912_v0.1/spreadsheet/51894/2_51894_input.xlsx`
- location: `Sheet1!K1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!K1.
- cached value: 2024-05-29 00:00:00; row labels: ["'CM Target'", '"Today\'s Date"']; column header: ''; used range: A1:K11
- neighbourhood: J1: "Today's Date" | K1: '=TODAY()' -> 2024-05-29 00:00:00

### `3a4af9c80244|VOLATILE_FUNCTION|Sheet1!F3`

- workbook: `all_data_912_v0.1/spreadsheet/57376/3_57376_input.xlsx`
- location: `Sheet1!F3`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(E3+14,E3+RAND()*100)`
- evidence: Function(s) found: RAND, RANDBETWEEN.
- evidence: The same relative formula appears in 50 cells on this sheet; the others are Sheet1!F4, Sheet1!F5, Sheet1!F6, Sheet1!F7, Sheet1!F8, Sheet1!F9, Sheet1!F10, Sheet1!F11, ....
- cached value: 2021-01-21 00:00:00; row labels: []; column header: "'end date'"; used range: A1:G30002
- neighbourhood: D2: 'rang_val' | E2: 'start date' | F2: 'end date' | G2: 'duration_amount_available' | D3: '=RANDBETWEEN(50,750)' -> 608 | E3: 2021-01-03 00:00:00 | F3: '=RANDBETWEEN(E3+14,E3+RAND()*100)' -> 2021-01-21 00:00:00 | G3: '=DATEDIF(E3,F3,"D")+1' -> 19 | D4: '=RANDBETWEEN(50,750)' -> 323 | E4: 2021-01-02 00:00:00 | F4: '=RANDBETWEEN(E4+14,E4+RAND()*100)' -> 2021-01-29 00:00:00 | G4: '=DATEDIF(E4,F4,"D")+1' -> 28 | D5: '=RANDBETWEEN(50,750)' -> 516 | E5: 2021-01-02 00:00:00 | F5: '=RANDBETWEEN(E5+14,E5+RAND()*100)' -> 2021-03-11 00:00:00 | G5: '=DATEDIF(E5,F5,"D")+1' -> 69

### `b4bb29667c08|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/48930/1_48930_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")`
- evidence: 16 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!E2, Sheet1!D3, Sheet1!E3, Sheet1!D4, Sheet1!E4, Sheet1!D5, Sheet1!E5, ....
- cached value: 7; row labels: ["'Matthew'", "'PK'"]; column header: "'Age'"; used range: A1:E9
- neighbourhood: B1: 'Grade' | C1: 'Birth Date' | D1: 'Age' | E1: 'KDG Year' | B2: 'PK' | C2: 2016-09-11 00:00:00 | D2: '=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")' -> 7 | E2: '=YEAR(TODAY())+(5-D2)' -> 2022 | B3: 'PK' | C3: 2017-02-22 00:00:00 | D3: '=IF(C3,DATEDIF(C3,TODAY(),"Y"),"")' -> 7 | E3: '=YEAR(TODAY())+(5-D3)' -> 2022 | B4: 'PK' | C4: 2016-12-13 00:00:00 | D4: '=IF(C4,DATEDIF(C4,TODAY(),"Y"),"")' -> 7 | E4: '=YEAR(TODAY())+(5-D4)' -> 2022

### `9d7ac18c8fd7|VOLATILE_FUNCTION|Extract!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/3_444-27_input.xlsx`
- location: `Extract!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 5 formula(s) on Extract use TODAY or NOW, so their results change with the clock: Extract!H2, Extract!H3, Extract!H4, Extract!H5, Extract!H6.
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:U13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 13859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `5a98e72c8ee6|VOLATILE_FUNCTION|YTDBudget&Summary!G2`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `YTD Budget & Summary!G2`  severity: Low  confidence: Info
- formula: `=YEAR(TODAY())`
- evidence: 1 formula(s) on YTD Budget & Summary use TODAY or NOW, so their results change with the clock: YTD Budget & Summary!G2.
- cached value: 2024; row labels: ["'ACTUAL vs. BUDGET YTD'", "'YEAR'"]; column header: ''; used range: A1:G22
- neighbourhood: F2: 'YEAR' | G2: '=YEAR(TODAY())' -> 2024 | E3: 'Budget' | F3: 'Remaining Rs.' | G3: 'Remaining %' | E4: 100000 | F4: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> 100000 | G4: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> 1

### `565bd65adf32|VOLATILE_FUNCTION|Example!C1`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3575/2_CF_3575_input.xlsx`
- location: `Example!C1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Example use TODAY or NOW, so their results change with the clock: Example!C1.
- cached value: 2024-05-27 00:00:00; row labels: []; column header: ''; used range: A1:BA85
- neighbourhood: C1: '=TODAY()' -> 2024-05-27 00:00:00 | B2: 'Example'

### `0a1e0f59bad2|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/45181/1_45181_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=C2-TODAY()`
- evidence: 19 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: -398; row labels: []; column header: "'Days left to return books'"; used range: A1:I20
- neighbourhood: B1: 'Date Picked UP' | C1: 'Date Drop Off' | D1: 'Days left to return books' | B2: 2022-04-29 00:00:00 | C2: '=B2+365' -> 2023-04-29 00:00:00 | D2: '=C2-TODAY()' -> -398 | B3: 2022-04-30 00:00:00 | C3: '=B3+365' -> 2023-04-30 00:00:00 | D3: '=C3-TODAY()' -> -397 | B4: 2022-05-01 00:00:00 | C4: '=B4+365' -> 2023-05-01 00:00:00 | D4: '=C4-TODAY()' -> -396

### `cb86e8d7c651|VOLATILE_FUNCTION|Sheet1!K1`

- workbook: `all_data_912_v0.1/spreadsheet/51894/3_51894_input.xlsx`
- location: `Sheet1!K1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!K1.
- cached value: 2024-05-29 00:00:00; row labels: ["'CM Target'", '"Today\'s Date"']; column header: ''; used range: A1:K11
- neighbourhood: J1: "Today's Date" | K1: '=TODAY()' -> 2024-05-29 00:00:00

### `c4229dd05b85|VOLATILE_FUNCTION|example!F8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!F8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(15,20)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!F9, example!F10, example!F11, example!F12.
- cached value: 18; row labels: ["'Egg'"]; column header: "'NOOR'"; used range: A1:O18
- neighbourhood: D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 20 | H8: '=RANDBETWEEN(25,30)' -> 28 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 15 | G9: '=RANDBETWEEN(20,25)' -> 20 | H9: '=RANDBETWEEN(25,30)' -> 30 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 19 | G10: '=RANDBETWEEN(20,25)' -> 25 | H10: '=RANDBETWEEN(25,30)' -> 30

### `5635b3c618d2|VOLATILE_FUNCTION|example!E8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/3_56996_input.xlsx`
- location: `example!E8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(10,15)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!E9, example!E10, example!E11, example!E12.
- cached value: 11; row labels: ["'Egg'"]; column header: "'AMIN'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | C8: '=RANDBETWEEN(1,5)' -> 2 | D8: '=RANDBETWEEN(5,10)' -> 7 | E8: '=RANDBETWEEN(10,15)' -> 11 | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 25 | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 5 | E9: '=RANDBETWEEN(10,15)' -> 10 | F9: '=RANDBETWEEN(15,20)' -> 19 | G9: '=RANDBETWEEN(20,25)' -> 22 | C10: '=RANDBETWEEN(1,5)' -> 5 | D10: '=RANDBETWEEN(5,10)' -> 7 | E10: '=RANDBETWEEN(10,15)' -> 11 | F10: '=RANDBETWEEN(15,20)' -> 17 | G10: '=RANDBETWEEN(20,25)' -> 23

### `201fbe2f5c4e|VOLATILE_FUNCTION|Sheet1!F14`

- workbook: `all_data_912_v0.1/spreadsheet/13894/3_13894_input.xlsx`
- location: `Sheet1!F14`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(ucode,SMALL(IF(MATCH(ucode,ucode,0)=ROW(INDIRECT("1:"&ROWS(ucode))),MATCH(ucode,ucode,0),""),ROW(INDIRECT("1:"&ROWS(ucode))))),"")`
- evidence: Function(s) found: INDIRECT.
- cached value: '8424.20.00ACMECHINA'; row labels: []; column header: "'IFERROR(INDEX(ucode;SMALL(IF(MATCH(ucode;ucode;0)=ROW(IN..."; used range: A1:K25
- neighbourhood: F12: 'IFERROR(INDEX(ucode;SMALL(IF(MATCH(u... | F14: '=IFERROR(INDEX(ucode,SMALL(IF(MATCH(ucode,ucode,0)=ROW(INDIRECT("1... -> '8424.20.00ACMECHINA' | G14: 1 | F15: '5620.30.00YYYYFRANCE' | G15: 2 | F16: '3424.20.00ACMECHINA' | G16: 3

### `3bdd8dbbaf67|VOLATILE_FUNCTION|Dati!CF12`

- workbook: `all_data_912_v0.1/spreadsheet/55912/3_55912_input.xlsx`
- location: `Dati!CF12`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1))*(#REF!="SI"))`
- evidence: Function(s) found: OFFSET.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are Dati!CG12, Dati!CF17, Dati!CG17.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:CJ40
- neighbourhood: CF12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CG12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CF13: '=1-(CF12/AG2)' -> '#REF!' | CG13: '=1-(CG12/AG2)' -> '#REF!' | CF14: '=1/CF13' -> '#REF!' | CG14: '=1/CG13' -> '#REF!'

### `026595829753|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/54640/1_54640_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=DATEDIF(C2,TODAY(),"D")`
- evidence: 17 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: 1900-02-13 00:00:00; row labels: []; column header: ''; used range: A1:D18
- neighbourhood: C1: 'Start Date' | C2: 2024-04-16 00:00:00 | D2: '=DATEDIF(C2,TODAY(),"D")' -> 1900-02-13 00:00:00 | C3: 2024-04-16 00:00:00 | D3: '=DATEDIF(C3,TODAY(),"D")' -> 1900-02-13 00:00:00 | C4: 2024-04-16 00:00:00 | D4: '=DATEDIF(C4,TODAY(),"D")' -> 1900-02-13 00:00:00

### `5124d0617e42|VOLATILE_FUNCTION|example!G8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!G8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(20,25)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!G9, example!G10, example!G11, example!G12.
- cached value: 25; row labels: ["'Egg'"]; column header: "'SHAMS'"; used range: A1:O18
- neighbourhood: E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 15 | G8: '=RANDBETWEEN(20,25)' -> 25 | H8: '=RANDBETWEEN(25,30)' -> 26 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 16 | G9: '=RANDBETWEEN(20,25)' -> 21 | H9: '=RANDBETWEEN(25,30)' -> 26 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 15 | G10: '=RANDBETWEEN(20,25)' -> 21 | H10: '=RANDBETWEEN(25,30)' -> 28

### `2f9a764eab30|VOLATILE_FUNCTION|Sheet1!I6`

- workbook: `all_data_912_v0.1/spreadsheet/52541/1_52541_input.xlsx`
- location: `Sheet1!I6`  severity: Low  confidence: Info
- formula: `=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[#This Row],[Due Date]])`
- evidence: 5 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!I6, Sheet1!I7, Sheet1!I8, Sheet1!I9, Sheet1!I10.
- cached value: 1171; row labels: ["'ARON'"]; column header: "'Over Due Days'"; used range: A1:J13
- neighbourhood: G5: 'Due Date' | H5: 'Amount Outstanding' | I5: 'Over Due Days' | J5: 'Remarks' | G6: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-03-16 00:00:00 | H6: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 25000 | I6: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1171 | J6: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | G7: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-04-13 00:00:00 | H7: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 22000 | I7: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1143 | J7: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | G8: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-04-18 00:00:00 | H8: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> -3000 | I8: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1138 | J8: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts'

### `a3bf35bf624c|VOLATILE_FUNCTION|ContactList!I1`

- workbook: `all_data_912_v0.1/spreadsheet/41589/2_41589_input.xlsx`
- location: `Contact List!I1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Contact List use TODAY or NOW, so their results change with the clock: Contact List!I1.
- cached value: 2024-05-29 00:00:00; row labels: ["'CONTACT LIST'"]; column header: ''; used range: A1:K34
- neighbourhood: I1: '=TODAY()' -> 2024-05-29 00:00:00 | G3: 'Date of Initial Contact' | H3: 'Last Contact' | I3: 'Regular Contact' | J3: 'Action' | K3: 'Notes'

### `4ca51e9feb33|VOLATILE_FUNCTION|Sheet1!E4`

- workbook: `all_data_912_v0.1/spreadsheet/37900/1_37900_input.xlsx`
- location: `Sheet1!E4`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!E4.
- cached value: 2024-05-22 00:00:00; row labels: ["'Value'", "'Current Date'"]; column header: ''; used range: A1:G16
- neighbourhood: D4: 'Current Date' | E4: '=TODAY()' -> 2024-05-22 00:00:00 | D5: 'Current Value'

### `09478d797a42|VOLATILE_FUNCTION|YTDBudget&Summary!G2`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `YTD Budget & Summary!G2`  severity: Low  confidence: Info
- formula: `=YEAR(TODAY())`
- evidence: 1 formula(s) on YTD Budget & Summary use TODAY or NOW, so their results change with the clock: YTD Budget & Summary!G2.
- cached value: 2024; row labels: ["'ACTUAL vs. BUDGET YTD'", "'YEAR'"]; column header: ''; used range: A1:G22
- neighbourhood: F2: 'YEAR' | G2: '=YEAR(TODAY())' -> 2024 | E3: 'Budget' | F3: 'Remaining Rs.' | G3: 'Remaining %' | E4: 100000 | F4: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> 100000 | G4: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> 1

### `c4229dd05b85|VOLATILE_FUNCTION|example!H8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!H8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(25,30)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!H9, example!H10, example!H11, example!H12.
- cached value: 28; row labels: ["'Egg'"]; column header: "'AHSAN'"; used range: A1:O18
- neighbourhood: F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | J7: 'Product' | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 20 | H8: '=RANDBETWEEN(25,30)' -> 28 | J8: 'Egg' | F9: '=RANDBETWEEN(15,20)' -> 15 | G9: '=RANDBETWEEN(20,25)' -> 20 | H9: '=RANDBETWEEN(25,30)' -> 30 | J9: 'Milk' | F10: '=RANDBETWEEN(15,20)' -> 19 | G10: '=RANDBETWEEN(20,25)' -> 25 | H10: '=RANDBETWEEN(25,30)' -> 30 | J10: 'Masala'

### `5124d0617e42|VOLATILE_FUNCTION|example!D8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!D8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(5,10)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!D9, example!D10, example!D11, example!D12.
- cached value: 10; row labels: ["'Egg'"]; column header: "'INAM'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | B8: 'Egg' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 10 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 15 | B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 6 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 16 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 4 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 15

### `2b144ac2a52b|VOLATILE_FUNCTION|Data!I10`

- workbook: `all_data_912_v0.1/spreadsheet/118-10/1_118-10_input.xlsx`
- location: `Data!I10`  severity: Low  confidence: Info
- formula: `=IF(H10>0,TODAY()-(A10),"")`
- evidence: 14 formula(s) on Data use TODAY or NOW, so their results change with the clock: Data!I10, Data!I11, Data!I18, Data!I19, Data!I27, Data!I28, Data!I29, Data!I30, ....
- cached value: None; row labels: []; column header: ''; used range: A1:I46
- neighbourhood: I10: '=IF(H10>0,TODAY()-(A10),"")' -> None | I11: '=IF(H11>0,TODAY()-(A11),"")' -> None

### `0bffec63dc84|VOLATILE_FUNCTION|Purchases!M2`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/1_CF_3712_input.xlsx`
- location: `Purchases!M2`  severity: Low  confidence: Info
- formula: `=IF(K2="Yes", "DONE", IF(ISBLANK(G2), "", H2-TODAY() & " day(s) remaining"))`
- evidence: 402 formula(s) on Purchases use TODAY or NOW, so their results change with the clock: Purchases!M2, Purchases!M3, Purchases!M4, Purchases!M5, Purchases!M6, Purchases!M7, Purchases!M8, Purchases!M9, ....
- cached value: '-14 day(s) remaining'; row labels: ["'No'", "'Yes'"]; column header: "'Days to pay'"; used range: A1:M441
- neighbourhood: K1: 'Invoice paid' | L1: 'Received' | M1: 'Days to pay' | K2: 'No' | L2: 'Yes' | M2: '=IF(K2="Yes", "DONE", IF(ISBLANK(G2), "", H2-TODAY() & " day(s) re... -> '-14 day(s) remaining' | K3: 'No' | L3: 'No' | M3: '=IF(K3="Yes", "DONE", IF(ISBLANK(G3), "", H3-TODAY() & " day(s) re... -> '6 day(s) remaining' | K4: 'No' | L4: 'No' | M4: '=IF(K4="Yes", "DONE", IF(ISBLANK(G4), "", H4-TODAY() & " day(s) re... -> '193 day(s) remaining'

### `29a79f5a27e4|VOLATILE_FUNCTION|Sheet1!C2`

- workbook: `all_data_912_v0.1/spreadsheet/49196/1_49196_input.xlsx`
- location: `Sheet1!C2`  severity: Low  confidence: Info
- formula: `=LEFT(K2,2)&"/"&MID(K2,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K2,FIND(" ",K2,1),6)`
- evidence: 46 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!C2, Sheet1!C3, Sheet1!C4, Sheet1!C5, Sheet1!C6, Sheet1!C7, Sheet1!C8, Sheet1!C9, ....
- cached value: '21/11/24 14:28'; row labels: []; column header: "'Start Time'"; used range: A1:L47
- neighbourhood: C1: 'Start Time' | D1: 'Month' | E1: 'Week' | C2: '=LEFT(K2,2)&"/"&MID(K2,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K2,FIND(" "... -> '21/11/24 14:28' | D2: '=TEXT(C2,"mmm")' -> 'Nov' | E2: '=WEEKNUM(C2,21)' -> 47 | C3: '=LEFT(K3,2)&"/"&MID(K3,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K3,FIND(" "... -> '22/11/24 06:00' | D3: '=TEXT(C3,"mmm")' -> 'Nov' | E3: '=WEEKNUM(C3,21)' -> 47 | C4: '=LEFT(K4,2)&"/"&MID(K4,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K4,FIND(" "... -> '23/11/24 06:00' | D4: '=TEXT(C4,"mmm")' -> 'Nov' | E4: '=WEEKNUM(C4,21)' -> 47

### `bcd47f3628af|VOLATILE_FUNCTION|Sheet1!L3`

- workbook: `all_data_912_v0.1/spreadsheet/44296/2_44296_input.xlsx`
- location: `Sheet1!L3`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- evidence: The same relative formula appears in 357 cells on this sheet; the others are Sheet1!M3, Sheet1!N3, Sheet1!O3, Sheet1!P3, Sheet1!Q3, Sheet1!R3, Sheet1!L4, Sheet1!M4, ....
- cached value: 0.561513270073679; row labels: ["'AK'"]; column header: ''; used range: A1:R53
- neighbourhood: K1: 'Year' | L1: 2015 | M1: 2016 | N1: 2017 | L3: '=RAND()' -> 0.561513270073679 | M3: '=RAND()' -> 0.672473799766201 | N3: '=RAND()' -> 0.579225282046277 | L4: '=RAND()' -> 0.997457002728795 | M4: '=RAND()' -> 0.605066734576938 | N4: '=RAND()' -> 0.259930977097773 | L5: '=RAND()' -> 0.798004815574318 | M5: '=RAND()' -> 0.117483841342598 | N5: '=RAND()' -> 0.224026799638861

## WHITESPACE_KEY

### `da1e266217a2|WHITESPACE_KEY|Sheet1!A22`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/1_CF_6540_input.xlsx`
- location: `Sheet1!A22`  severity: Medium  confidence: Review
- evidence: Raw value is 'Senior Technical Officer '; the other text values in this column are not padded.
- cached value: 'Senior Technical Officer '; row labels: []; column header: "'Principal Technical Officer '"; used range: A1:CL123
- neighbourhood: A20: 'Site Access Manager (SAM) ' | A21: 'Principal Technical Officer ' | A22: 'Senior Technical Officer ' | A23: 'Technical Officer ' | A24: 'Track Chargeman'

### `ac9c457a4aed|WHITESPACE_KEY|Compiledandlocatedschoolsda!L7`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!L7`  severity: Medium  confidence: Review
- evidence: Raw value is ' LA11 7RD'; the other text values in this column are not padded.
- cached value: ' LA11 7RD'; row labels: ["' Allithwaite'", "' Grange-Over-Sands'"]; column header: "' CA13 9BH'"; used range: A1:AJ1419
- neighbourhood: L5: ' CA13 9BH' | M5: 'Mr' | N5: 'A' | L6: ' CA13 9BH' | M6: 'Mrs' | N6: 'N' | L7: ' LA11 7RD' | M7: 'Mrs' | N7: 'G' | L8: ' CA15 6QG' | M8: 'Mr' | N8: 'D' | L9: ' CA9 3UF' | M9: 'Ms' | N9: 'S'

### `c561c810150e|WHITESPACE_KEY|Sheet1!B36`

- workbook: `all_data_912_v0.1/spreadsheet/54675/2_54675_input.xlsx`
- location: `Sheet1!B36`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Angela McConnell '"; used range: A1:F2452
- neighbourhood: A34: 4 | B34: 'Gary Stoddard, Angela McConnell ' | A35: 4 | B35: 'Angela McConnell ' | A36: 4 | B36: 'Angela McConnell ' | A37: 4 | B37: 'Building Services, Phyllis McFadyen,... | A38: 4 | B38: 'Building Services'

### `9324c9b68159|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/36764/2_36764_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Raw value is 'To be actioned                                    '; the other text values in this column are not padded.
- cached value: 'To be actioned                                    '; row labels: []; column header: "'5) Breakdown of products below'"; used range: A1:D3
- neighbourhood: A1: '5) Breakdown of products below' | C1: 'UK purchases' | A2: 'To be actioned                      ... | B2: 223 | C2: 0 | A3: 'To be actioned                      ... | B3: 138

### `b3b8477b9402|WHITESPACE_KEY|Sheet1!A93`

- workbook: `all_data_912_v0.1/spreadsheet/290-27/1_290-27_input.xlsx`
- location: `Sheet1!A93`  severity: Medium  confidence: Review
- evidence: Raw value is 'GG '; the other text values in this column are not padded.
- cached value: 'GG '; row labels: []; column header: "'NAME'"; used range: A1:I139
- neighbourhood: A91: 'NAME' | B91: 'GG 2' | C91: 'Clm 4000n2l' | A93: 'GG ' | B93: 2020-08-29 00:00:00 | C93: 'GG 2' | A95: 'SWEET SARAH BEAR'

### `2c8a67813f0c|WHITESPACE_KEY|Sheet1!A21`

- workbook: `all_data_912_v0.1/spreadsheet/57590/1_57590_input.xlsx`
- location: `Sheet1!A21`  severity: Medium  confidence: Review
- evidence: Raw value is 'Rejected '; the other text values in this column are not padded.
- cached value: 'Rejected '; row labels: []; column header: "'Accept'"; used range: A1:M37
- neighbourhood: A19: 'Status' | B19: 'Status Cost' | C19: 'Total Debit Notes' | A20: 'Accept' | B20: 15214.4 | C20: 2 | A21: 'Rejected ' | B21: 0 | C21: 0 | A22: 'On Hold' | B22: 0 | C22: 0

### `53fb4bf35e11|WHITESPACE_KEY|Sheet1!A87`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/3_CF_6540_input.xlsx`
- location: `Sheet1!A87`  severity: Medium  confidence: Review
- evidence: Raw value is 'Concrete Finisher '; the other text values in this column are not padded.
- cached value: 'Concrete Finisher '; row labels: []; column header: "'Concreter '"; used range: A1:CL123
- neighbourhood: A85: 'Steel Fixer ' | A86: 'Concreter ' | A87: 'Concrete Finisher ' | A88: 'Shuttering Carpenter ' | A89: 'Bricklayer'

### `cc14175a29f0|WHITESPACE_KEY|Sheet1!A49`

- workbook: `all_data_912_v0.1/spreadsheet/368-44/2_368-44_input.xlsx`
- location: `Sheet1!A49`  severity: Medium  confidence: Review
- evidence: Raw value is 'COUNTER       Clock In/Clock Out '; the other text values in this column are not padded.
- cached value: 'COUNTER       Clock In/Clock Out '; row labels: []; column header: "'*** Total Hours   Reg/OT  ***'"; used range: A1:J87
- neighbourhood: A47: 'COUNTER       Reg Hours/OT Hours' | B47: 23.23 | C47: 0 | A48: '*** Total Hours   Reg/OT  ***' | B48: 23.23 | C48: 0 | A49: 'COUNTER       Clock In/Clock Out ' | B49: 10:15:00 | C49: 09:29:00 | A50: '-------------------------' | A51: 'Grand Totals'

### `16655eaea0b3|WHITESPACE_KEY|Sheet1!A14`

- workbook: `all_data_912_v0.1/spreadsheet/368-44/1_368-44_input.xlsx`
- location: `Sheet1!A14`  severity: Medium  confidence: Review
- evidence: Raw value is 'COUNTER       Clock In/Clock Out '; the other text values in this column are not padded.
- cached value: 'COUNTER       Clock In/Clock Out '; row labels: []; column header: "'*** Total Hours   Reg/OT  ***'"; used range: A1:J87
- neighbourhood: A12: 'COUNTER       Reg Hours/OT Hours' | B12: 23.23 | C12: 0 | A13: '*** Total Hours   Reg/OT  ***' | B13: 23.23 | C13: 0 | A14: 'COUNTER       Clock In/Clock Out ' | B14: 10:15:00 | C14: 09:29:00 | A15: '-------------------------' | A16: 'Employee# 7   LAURYN_F8796' | B16: 'TOTAL' | C16: 'TOTAL'

### `b2d0d6365d71|WHITESPACE_KEY|Sheet1!B20`

- workbook: `all_data_912_v0.1/spreadsheet/54675/1_54675_input.xlsx`
- location: `Sheet1!B20`  severity: Medium  confidence: Review
- evidence: Raw value is 'Building Services, Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Building Services, Angela McConnell '; row labels: []; column header: "'Sandy Ross'"; used range: A1:F2452
- neighbourhood: A18: 4 | B18: 'Sandy Ross' | A19: 4 | B19: 'Sandy Ross' | A20: 4 | B20: 'Building Services, Angela McConnell ' | A21: 4 | B21: 'Angela McConnell ' | A22: 4 | B22: 'Building Services'

### `53fb4bf35e11|WHITESPACE_KEY|Sheet1!A57`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/3_CF_6540_input.xlsx`
- location: `Sheet1!A57`  severity: Medium  confidence: Review
- evidence: Raw value is 'OLEC 1 '; the other text values in this column are not padded.
- cached value: 'OLEC 1 '; row labels: []; column header: "'Assistant Electrician'"; used range: A1:CL123
- neighbourhood: A55: 'Approved Electrician ' | A56: 'Assistant Electrician' | A57: 'OLEC 1 ' | A58: 'OLEC 2' | A59: 'OLEC 3'

### `73e7e7a73a78|WHITESPACE_KEY|Sheet1!A4`

- workbook: `all_data_912_v0.1/spreadsheet/56855/2_56855_input.xlsx`
- location: `Sheet1!A4`  severity: Medium  confidence: Review
- evidence: Raw value is '14:41\n16:47\n'; the other text values in this column are not padded.
- cached value: '14:41\n16:47\n'; row labels: []; column header: "'14:40\\n16:47'"; used range: A1:B4
- neighbourhood: A3: '14:40\n16:47' | B3: '=RIGHT(A3,5)-LEFT(A3,5)' -> 0.0881944444444444 | A4: '14:41\n16:47\n' | B4: '=RIGHT(A4,5)-LEFT(A4,5)' -> '#VALUE!'

### `b2d0d6365d71|WHITESPACE_KEY|Sheet1!B12`

- workbook: `all_data_912_v0.1/spreadsheet/54675/1_54675_input.xlsx`
- location: `Sheet1!B12`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Building Services'"; used range: A1:F2452
- neighbourhood: A10: 4 | B10: 'Lynn Meek, Sandy Ross, Kirsty Mcdonald' | A11: 4 | B11: 'Building Services' | A12: 4 | B12: 'Angela McConnell ' | A13: 4 | B13: 'Angela McConnell ' | A14: 4 | B14: 'Phyllis McFadyen'

### `1c06477fced9|WHITESPACE_KEY|Compiledandlocatedschoolsda!L6`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `Compiled and located schools da!L6`  severity: Medium  confidence: Review
- evidence: Raw value is ' CA13 9BH'; the other text values in this column are not padded.
- cached value: ' CA13 9BH'; row labels: ["'Slatefell Drive'", "' Cockermouth'"]; column header: "' CA13 9BH'"; used range: A1:AJ1419
- neighbourhood: L4: ' CA1 1JB' | M4: 'Mr' | N4: 'K' | L5: ' CA13 9BH' | M5: 'Mr' | N5: 'A' | L6: ' CA13 9BH' | M6: 'Mrs' | N6: 'N' | L7: ' LA11 7RD' | M7: 'Mrs' | N7: 'G' | L8: ' CA15 6QG' | M8: 'Mr' | N8: 'D'

### `34ca77355303|WHITESPACE_KEY|ProductList!A4`

- workbook: `all_data_912_v0.1/spreadsheet/32895/3_32895_input.xlsx`
- location: `Product List!A4`  severity: Medium  confidence: Review
- evidence: Raw value is 'PLASTIC ICING 1KG '; the other text values in this column are not padded.
- cached value: 'PLASTIC ICING 1KG '; row labels: []; column header: "'Product'"; used range: A1:C14
- neighbourhood: A3: 'Product' | B3: 'Code' | C3: 'Opening Balance' | A4: 'PLASTIC ICING 1KG ' | B4: 'B001' | C4: 100 | A5: 'PLASTIC ICING 500G' | B5: 'B002' | C5: 40 | A6: 'FINO WHIP 5KG ' | B6: 'B003' | C6: 90

### `da1e266217a2|WHITESPACE_KEY|Sheet1!A14`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/1_CF_6540_input.xlsx`
- location: `Sheet1!A14`  severity: Medium  confidence: Review
- evidence: Raw value is 'Lookout  '; the other text values in this column are not padded.
- cached value: 'Lookout  '; row labels: []; column header: "'Hand Signaller '"; used range: A1:CL123
- neighbourhood: A12: 'Strapman Assistant' | A13: 'Hand Signaller ' | A14: 'Lookout  ' | A15: 'Machine Controller' | A16: 'Crane Controller'

### `09478d797a42|WHITESPACE_KEY|Sheet1!B34`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Sheet1!B34`  severity: Medium  confidence: Review
- evidence: Raw value is 'Third Party Loans '; the other text values in this column are not padded.
- cached value: 'Third Party Loans '; row labels: []; column header: "'Owners Capital'"; used range: A1:G34
- neighbourhood: B32: 'Other Incomes' | C32: 'WG/CR/031' | D32: 'P & L' | B33: 'Owners Capital' | C33: 'WG/CR/032' | D33: 'Equity Capital' | B34: 'Third Party Loans ' | C34: 'WG/CR/033' | D34: 'Debt Capital'

### `50e95eddd565|WHITESPACE_KEY|Sheet1!A11`

- workbook: `all_data_912_v0.1/spreadsheet/50472/2_50472_input.xlsx`
- location: `Sheet1!A11`  severity: Medium  confidence: Review
- evidence: Raw value is '205035 Accrued Social Charges '; the other text values in this column are not padded.
- cached value: '205035 Accrued Social Charges '; row labels: []; column header: "'606270 Acc. Social Charges - Expense '"; used range: A1:A17
- neighbourhood: A10: '606270 Acc. Social Charges - Expense ' | A11: '205035 Accrued Social Charges ' | A13: '606270 Acc. Social Charges - Expense '

### `34ca77355303|WHITESPACE_KEY|Inventory!A10`

- workbook: `all_data_912_v0.1/spreadsheet/32895/3_32895_input.xlsx`
- location: `Inventory!A10`  severity: Medium  confidence: Review
- evidence: Raw value is 'WHIPPET 5KG '; the other text values in this column are not padded.
- cached value: 'WHIPPET 5KG '; row labels: []; column header: "'FINOWHIP250G'"; used range: A1:C16
- neighbourhood: A8: 'FINOWHIP 500G' | B8: 'B005' | C8: 0 | A9: 'FINOWHIP250G' | B9: 'B006' | A10: 'WHIPPET 5KG ' | B10: 'B007' | A11: 'WHIPPET 1KG' | B11: 'B008' | A12: 'WHIPPET 500G' | B12: 'B009'

### `f065dc30ad2b|WHITESPACE_KEY|Sheet1!A22`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/2_CF_6540_input.xlsx`
- location: `Sheet1!A22`  severity: Medium  confidence: Review
- evidence: Raw value is 'Senior Technical Officer '; the other text values in this column are not padded.
- cached value: 'Senior Technical Officer '; row labels: []; column header: "'Principal Technical Officer '"; used range: A1:CL123
- neighbourhood: A20: 'Site Access Manager (SAM) ' | A21: 'Principal Technical Officer ' | A22: 'Senior Technical Officer ' | A23: 'Technical Officer ' | A24: 'Track Chargeman'

### `f065dc30ad2b|WHITESPACE_KEY|Sheet1!A30`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/2_CF_6540_input.xlsx`
- location: `Sheet1!A30`  severity: Medium  confidence: Review
- evidence: Raw value is 'Cutter/Burner '; the other text values in this column are not padded.
- cached value: 'Cutter/Burner '; row labels: []; column header: "'Crane Controller'"; used range: A1:CL123
- neighbourhood: A28: 'Setting Out Surveyor ' | A29: 'Crane Controller' | A30: 'Cutter/Burner ' | A31: 'Welders (team of 2) Inc. eqpt' | A32: 'Welding Inspector '

### `fd3bd0e9c845|WHITESPACE_KEY|Sheet1!B55`

- workbook: `all_data_912_v0.1/spreadsheet/54675/3_54675_input.xlsx`
- location: `Sheet1!B55`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Sandy Ross'"; used range: A1:F2452
- neighbourhood: A53: 4 | B53: 'Building Services' | A54: 4 | B54: 'Sandy Ross' | A55: 4 | B55: 'Angela McConnell ' | A56: 4 | B56: 'Jacqueline Doyle' | A57: 4 | B57: 'Sandy Ross, Lynn Meek'

### `cc14175a29f0|WHITESPACE_KEY|Sheet1!A9`

- workbook: `all_data_912_v0.1/spreadsheet/368-44/2_368-44_input.xlsx`
- location: `Sheet1!A9`  severity: Medium  confidence: Review
- evidence: Raw value is 'COUNTER       Clock In/Clock Out '; the other text values in this column are not padded.
- cached value: 'COUNTER       Clock In/Clock Out '; row labels: []; column header: "'*** Total Hours   Reg/OT  ***'"; used range: A1:J87
- neighbourhood: A7: 'COUNTER       Reg Hours/OT Hours' | B7: 23.25 | C7: 0 | A8: '*** Total Hours   Reg/OT  ***' | B8: 23.25 | C8: 0 | A9: 'COUNTER       Clock In/Clock Out ' | B9: 10:14:00 | C9: 09:29:00 | A10: '-------------------------' | A11: 'Employee# 4   MOHMED_M9858' | B11: 'TOTAL' | C11: 'TOTAL'

### `c561c810150e|WHITESPACE_KEY|Sheet1!B49`

- workbook: `all_data_912_v0.1/spreadsheet/54675/2_54675_input.xlsx`
- location: `Sheet1!B49`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Angela McConnell '"; used range: A1:F2452
- neighbourhood: A47: 4 | B47: 'Angela McConnell ' | A48: 4 | B48: 'Angela McConnell ' | A49: 4 | B49: 'Angela McConnell ' | A50: 4 | B50: 'Angela McConnell ' | A51: 4 | B51: 'Angela McConnell , Sandy Ross'

### `1354a93ef2de|WHITESPACE_KEY|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/48354/1_48354_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- evidence: Raw value is 'operating an international flight '; the other text values in this column are not padded.
- cached value: 'operating an international flight '; row labels: ["'N/A'"]; column header: "'ContactType'"; used range: A1:D6
- neighbourhood: A1: 'D or I' | B1: 'ContactType' | A2: 'N/A' | B2: 'operating an international flight ' | D2: '=IF(B2="domestic",“D”,IF(B2="international",“I”,“N/A”)) {array D2}' -> '#NAME?' | A3: 'N/A' | B3: 'operating a domestic flight' | D3: '=IF(B3="domestic",“D”,IF(B3="international",“I”,“N/A”)) {array D3}' -> '#NAME?' | A4: 'N/A' | B4: 'jumpseating (domestic)' | D4: '=IF(B4="domestic",“D”,IF(B4="international",“I”,“N/A”)) {array D4}' -> '#NAME?'

## WHOLE_COLUMN_REFERENCE

### `61bf2143f38b|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/2_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, ....
- cached value: '#VALUE!'; row labels: ["'F100066'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100066' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `321c9048065c|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/3_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, ....
- cached value: 'PEPEPEPEPE'; row labels: ["'YES'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N2}' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N3}' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N4}' -> 'PEPEPEPEPE'

### `87c4744e15aa|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/1_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, ....
- cached value: '#VALUE!'; row labels: ["'F100063'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!J2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!J3, Volym P5_P6_2023!J4, Volym P5_P6_2023!J5, Volym P5_P6_2023!J6, Volym P5_P6_2023!J7, Volym P5_P6_2023!J8, Volym P5_P6_2023!J9, Volym P5_P6_2023!J10.
- cached value: '200000003,200000005'; row labels: ["'ABC2'"]; column header: "'Source list Agreement (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I5`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!I5`  severity: Medium  confidence: Review
- formula: `=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C,""))),"ÅÅÅÅ-MM-DD")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are Volym P5_P6_2023!I6, Volym P5_P6_2023!I7, Volym P5_P6_2023!I8, Volym P5_P6_2023!I9, Volym P5_P6_2023!I10.
- cached value: '#VALUE!'; row labels: ["'ABC3'"]; column header: ''; used range: A1:K10
- neighbourhood: G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007' | G5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I5: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C... -> '#VALUE!' | J5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I6: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!D:D,""))... -> '200000008' | K6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!E:E,""))... -> '460000008' | G7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I7: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!D:D,""))... -> '200000009' | K7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!E:E,""))... -> '460000009'

### `8738ef8d70bc|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/2_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, ....
- cached value: 2014-04-28 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-28 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-03-24 00:00:00

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '44926,45657'; row labels: ["'ABC2'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `d7cd8ee7e5c8|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/3_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, ....
- cached value: 2014-04-08 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-08 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-12-24 00:00:00

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '46022,45657,45291'; row labels: ["'ABC1'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000000 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000000 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '46022,45657,45291' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000001,200000002,200000... | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000001,460000002,460000... | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `5358e587d475|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/1_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, ....
- cached value: 2014-04-08 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-08 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-03-24 00:00:00

### `740614797bbb|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/1_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, ....
- cached value: 'PEPEPEPEPE'; row labels: ["'YES'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N2}' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N3}' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N4}' -> 'PEPEPEPEPE'

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!K2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!K2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!K3, Volym P5_P6_2023!K4, Volym P5_P6_2023!K5, Volym P5_P6_2023!K6, Volym P5_P6_2023!K7, Volym P5_P6_2023!K8, Volym P5_P6_2023!K9, Volym P5_P6_2023!K10.
- cached value: '460000001,460000002,460000000'; row labels: ["'ABC1'"]; column header: "'Source list Vendor (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '46022,45657,45291' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000001,200000002,200000... | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000001,460000002,460000... | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '44926,45657'; row labels: ["'ABC2'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007'

### `be6378a48fb9|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/2_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `b31624554d1c|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7000 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `286f4ae7ac70|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/3_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, ....
- cached value: '#VALUE!'; row labels: ["'F100063'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `0e309a2a0da6|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/2_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, ....
- cached value: 'PEPEPEPEPE'; row labels: ["'no'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE'

### `47eb61dd533e|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'
