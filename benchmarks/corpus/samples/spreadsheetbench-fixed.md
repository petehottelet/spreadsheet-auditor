# Finding cards: spreadsheetbench

Generated 2026-09-14T07:09:13+00:00 from benchmarks\corpus\results\spreadsheetbench-fixed with seed 7, up to 25 per rule and 2 per workbook.

Label each card in `labels/<source>.json` as `TP` (the auditor is right), `FP` (it is wrong), or `unsure`, with a one-line reason.

## BLANK_PRECEDENT

### `6ed6a011684e|BLANK_PRECEDENT|Example!D9|e15415`

- workbook: `all_data_912_v0.1/spreadsheet/37615/3_37615_input.xlsx`
- location: `Example!D9`  severity: Medium  confidence: Review
- formula: `=C9-B9`
- evidence: Referenced cell Example!C9 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0:00:00; row labels: []; column header: ''; used range: A1:F44
- neighbourhood: B7: 07:00:00 | C7: 15:00:00 | D7: '=C7-B7' -> 8:00:00 | E7: 2 | B8: 04:00:00 | C8: 11:00:00 | D8: '=C8-B8' -> 7:00:00 | E8: 1 | D9: '=C9-B9' -> 0:00:00 | E9: 0 | D10: '=C10-B10' -> 0:00:00 | E10: 0 | B11: 08:30:00 | C11: 16:45:00 | D11: '=C11-B11' -> 8:15:00 | E11: 0

### `d7e27f29097e|BLANK_PRECEDENT|Malaga!F16|21ed4d`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!F16`  severity: Medium  confidence: Review
- formula: `=IF(C16="","",IF(D16="G",$G$4-E16,IF(D16="N/G",$L$4-E16,IF(D16="S/S",$L$5-E16))))`
- evidence: Referenced cell Malaga!E16 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: []; column header: ''; used range: A1:AJ57
- neighbourhood: D14: 'N/G' | E14: 50 | F14: '=IF(C14="","",IF(D14="G",$G$4-E14,IF(D14="N/G",$L$4-E14,IF(D14="S/... -> 399 | H14: 17 | D15: 'G' | E15: 0 | F15: '=IF(C15="","",IF(D15="G",$G$4-E15,IF(D15="N/G",$L$4-E15,IF(D15="S/... -> 799 | H15: 18 | F16: '=IF(C16="","",IF(D16="G",$G$4-E16,IF(D16="N/G",$L$4-E16,IF(D16="S/... -> None | H16: 19 | D17: 'S/S' | E17: 0 | F17: '=IF(C17="","",IF(D17="G",$G$4-E17,IF(D17="N/G",$L$4-E17,IF(D17="S/... -> 1044 | H17: 20 | D18: 'G' | E18: 36 | F18: '=IF(C18="","",IF(D18="G",$G$4-E18,IF(D18="N/G",$L$4-E18,IF(D18="S/... -> 763 | H18: 21

### `6d6fc1caeb06|BLANK_PRECEDENT|DRP!L2`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/1_175-10_input.xlsx`
- location: `DRP!L2`  severity: Medium  confidence: Review
- formula: `=I2+J2-K2`
- evidence: Referenced cell DRP!J2 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'RE1'", "'RS1'"]; column header: "'NET'"; used range: A1:O23
- neighbourhood: J1: 'BUYING' | K1: 'SELLING' | L1: 'NET' | M1: 'BUYING' | N1: 'SELLING' | L2: '=I2+J2-K2' -> None | M2: 0 | N2: 0 | J3: 400 | K3: 20 | L3: '=I3+J3-K3' -> None | M3: 400 | N3: 20 | J4: 60 | K4: 20 | L4: '=I4+J4-K4' -> None | N4: 20

### `ada3dc9b0be1|BLANK_PRECEDENT|EXCELHELP!AF14`

- workbook: `all_data_912_v0.1/spreadsheet/39946/3_39946_input.xlsx`
- location: `EXCEL HELP!AF14`  severity: Medium  confidence: Review
- formula: `=G14-AE14`
- evidence: Referenced cell EXCEL HELP!G14 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: ["''", "''"]; column header: ''; used range: A1:AF23
- neighbourhood: AE12: '=SUM(K12:AD12)' -> 595.068493150685 | AF12: '=G12-AE12' -> 604.931506849315 | AE13: '=SUM(K13:AD13)' -> 1000 | AF13: '=G13-AE13' -> 0 | AE14: '=SUM(K14:AD14)' -> 0 | AF14: '=G14-AE14' -> 0 | AE15: '=SUM(K15:AD15)' -> 496.438356164383 | AF15: '=G15-AE15' -> 703.561643835617 | AE16: '=SUM(K16:AD16)' -> 1200 | AF16: '=G16-AE16' -> 0

### `6ed6a011684e|BLANK_PRECEDENT|Example!D15|7b794e`

- workbook: `all_data_912_v0.1/spreadsheet/37615/3_37615_input.xlsx`
- location: `Example!D15`  severity: Medium  confidence: Review
- formula: `=C15-B15`
- evidence: Referenced cell Example!B15 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0:00:00; row labels: []; column header: ''; used range: A1:F44
- neighbourhood: B13: 11:00:00 | C13: 16:00:00 | D13: '=C13-B13' -> 5:00:00 | E13: 1 | B14: 09:00:00 | C14: 16:30:00 | D14: '=C14-B14' -> 7:30:00 | E14: 1 | D15: '=C15-B15' -> 0:00:00 | E15: 0 | D16: '=C16-B16' -> 0:00:00 | E16: 0 | D17: '=C17-B17' -> 0:00:00 | E17: 0

### `5989e352c77e|BLANK_PRECEDENT|OMRAAN!E4`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/2_91-3_input.xlsx`
- location: `OMRAAN!E4`  severity: Medium  confidence: Review
- formula: `=E3+C4-D4`
- evidence: Referenced cell OMRAAN!D4 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH PR '"]; column header: ''; used range: A1:F12
- neighbourhood: D2: -2000 | E2: -2000 | C3: 10000 | E3: '=E2+C3-D3' -> None | F3: '=C3+C4+C9' -> None | C4: 500 | E4: '=E3+C4-D4' -> None | D5: 2000 | E5: '=E4+C5-D5' -> None | D6: 2500 | E6: '=E5+C6-D6' -> None | F6: '=D2+D6+D7' -> None

### `a3b766273873|BLANK_PRECEDENT|GLDetails!G7`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/3_601-4_input.xlsx`
- location: `GL Details!G7`  severity: Medium  confidence: Review
- formula: `=+E7-F7`
- evidence: Referenced cell GL Details!E7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: E5: 70 | G5: '=+E5-F5' -> None | E6: 70 | G6: '=+E6-F6' -> None | F7: 402.5 | G7: '=+E7-F7' -> None | E8: 1001 | G8: '=+E8-F8' -> None | E9: 28.07 | G9: '=+E9-F9' -> None

### `2ed80e0ee4cd|BLANK_PRECEDENT|DRP!I2`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!I2`  severity: Medium  confidence: Review
- formula: `=G2-H2`
- evidence: Referenced cell DRP!H2 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'RE1'", "'A'"]; column header: "'NET'"; used range: A1:O23
- neighbourhood: G1: 'BUYING' | H1: 'SELLING' | I1: 'NET' | J1: 'BUYING' | K1: 'SELLING' | G2: 20 | I2: '=G2-H2' -> None | G3: 400 | H3: 20 | I3: '=G3-H3' -> None | J3: 400 | K3: 20 | G4: 60 | H4: 20 | I4: '=G4-H4' -> None | J4: 60 | K4: 20

### `3466007fd64d|BLANK_PRECEDENT|Example!D17|f74512`

- workbook: `all_data_912_v0.1/spreadsheet/37615/2_37615_input.xlsx`
- location: `Example!D17`  severity: Medium  confidence: Review
- formula: `=C17-B17`
- evidence: Referenced cell Example!B17 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0:00:00; row labels: []; column header: ''; used range: A1:F44
- neighbourhood: D15: '=C15-B15' -> 0:00:00 | E15: 0 | D16: '=C16-B16' -> 0:00:00 | E16: 0 | D17: '=C17-B17' -> 0:00:00 | E17: 0 | B18: 08:15:00 | C18: 12:00:00 | D18: '=C18-B18' -> 3:45:00 | E18: 1 | B19: 07:55:00 | C19: 13:25:00 | D19: '=C19-B19' -> 5:30:00 | E19: 1

### `5989e352c77e|BLANK_PRECEDENT|ALI!E5`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/2_91-3_input.xlsx`
- location: `ALI!E5`  severity: Medium  confidence: Review
- formula: `=E4+C5-D5`
- evidence: Referenced cell ALI!D5 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'SALES'"]; column header: ''; used range: A1:F24
- neighbourhood: D3: 20000 | E3: '=E2+C3-D3' -> None | C4: 2000 | E4: '=E3+C4-D4' -> None | C5: 2500 | E5: '=E4+C5-D5' -> None | D6: 2000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None

### `0233c00701a4|BLANK_PRECEDENT|ALI!E6`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/3_91-3_input.xlsx`
- location: `ALI!E6`  severity: Medium  confidence: Review
- formula: `=E5+C6-D6`
- evidence: Referenced cell ALI!C6 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH DM'"]; column header: ''; used range: A1:F24
- neighbourhood: C4: 2000 | E4: '=E3+C4-D4' -> None | C5: 2500 | E5: '=E4+C5-D5' -> None | D6: 2000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None | D8: 3000 | E8: '=E7+C8-D8' -> None

### `6afa97343321|BLANK_PRECEDENT|AHMED!E6`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/1_91-3_input.xlsx`
- location: `AHMED!E6`  severity: Medium  confidence: Review
- formula: `=E5+C6-D6`
- evidence: Referenced cell AHMED!C6 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH DM'"]; column header: ''; used range: A1:F12
- neighbourhood: C4: 15000 | E4: '=E3+C4-D4' -> None | F4: '=C4+C10' -> None | C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None | D8: 3000 | E8: '=E7+C8-D8' -> None

### `6afa97343321|BLANK_PRECEDENT|ALI!E4`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/1_91-3_input.xlsx`
- location: `ALI!E4`  severity: Medium  confidence: Review
- formula: `=E3+C4-D4`
- evidence: Referenced cell ALI!D4 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'CASH PR '"]; column header: ''; used range: A1:F24
- neighbourhood: C2: 20000 | E2: 20000 | D3: 20000 | E3: '=E2+C3-D3' -> None | C4: 2000 | E4: '=E3+C4-D4' -> None | C5: 2500 | E5: '=E4+C5-D5' -> None | D6: 2000 | E6: '=E5+C6-D6' -> None

### `7b15ef0c0d8c|BLANK_PRECEDENT|data!G28|1e5926`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!G28`  severity: Medium  confidence: Review
- formula: `=TEXT(F28-E28,"h:mm:ss")`
- evidence: Referenced cell data!E28 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: '0:00:00'; row labels: ["'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: E26: 11:42:24 | F26: 11:47:48 | E27: 13:10:27 | F27: 14:35:03 | G28: '=TEXT(F28-E28,"h:mm:ss")' -> '0:00:00' | H28: '=HOUR(E28)+MINUTE(E28)/60+SECOND(E28)/3600' -> 0 | I28: '=HOUR(F28)+MINUTE(F28)/60+SECOND(F28)/3600' -> 0 | E29: 12:58:21 | F29: 13:18:19 | G29: '=TEXT(F29-E29,"h:mm:ss")' -> '0:19:58' | H29: '=HOUR(E29)+MINUTE(E29)/60+SECOND(E29)/3600' -> 12.9725 | I29: '=HOUR(F29)+MINUTE(F29)/60+SECOND(F29)/3600' -> 13.3052777777778 | E30: 13:35:01 | F30: 14:21:31 | G30: '=TEXT(F30-E30,"h:mm:ss")' -> '0:46:30' | H30: '=HOUR(E30)+MINUTE(E30)/60+SECOND(E30)/3600' -> 13.5836111111111 | I30: '=HOUR(F30)+MINUTE(F30)/60+SECOND(F30)/3600' -> 14.3586111111111

### `4eee00e05d38|BLANK_PRECEDENT|Example!F42`

- workbook: `all_data_912_v0.1/spreadsheet/37615/1_37615_input.xlsx`
- location: `Example!F42`  severity: Medium  confidence: Review
- formula: `=SUM(D42*E42)`
- evidence: Referenced cell Example!E42 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:F44
- neighbourhood: D42: 57.2 | F42: '=SUM(D42*E42)' -> 0 | D43: 28.6 | F43: '=SUM(D43*E43)' -> 0 | E44: 'Total invoice:' | F44: '=SUM(F42:F43)' -> 0

### `3466007fd64d|BLANK_PRECEDENT|Example!F43`

- workbook: `all_data_912_v0.1/spreadsheet/37615/2_37615_input.xlsx`
- location: `Example!F43`  severity: Medium  confidence: Review
- formula: `=SUM(D43*E43)`
- evidence: Referenced cell Example!E43 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:F44
- neighbourhood: D42: 57.2 | F42: '=SUM(D42*E42)' -> 0 | D43: 28.6 | F43: '=SUM(D43*E43)' -> 0 | E44: 'Total invoice:' | F44: '=SUM(F42:F43)' -> 0

### `c21a65d89062|BLANK_PRECEDENT|data!G28|1e5926`

- workbook: `all_data_912_v0.1/spreadsheet/56225/1_56225_input.xlsx`
- location: `data!G28`  severity: Medium  confidence: Review
- formula: `=TEXT(F28-E28,"h:mm:ss")`
- evidence: Referenced cell data!E28 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: '0:00:00'; row labels: ["'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: E26: 11:42:24 | F26: 11:47:48 | E27: 13:10:27 | F27: 14:35:03 | G28: '=TEXT(F28-E28,"h:mm:ss")' -> '0:00:00' | H28: '=HOUR(E28)+MINUTE(E28)/60+SECOND(E28)/3600' -> 0 | I28: '=HOUR(F28)+MINUTE(F28)/60+SECOND(F28)/3600' -> 0 | E29: 12:58:21 | F29: 13:18:19 | G29: '=TEXT(F29-E29,"h:mm:ss")' -> '0:19:58' | H29: '=HOUR(E29)+MINUTE(E29)/60+SECOND(E29)/3600' -> 12.9725 | I29: '=HOUR(F29)+MINUTE(F29)/60+SECOND(F29)/3600' -> 13.3052777777778 | E30: 13:35:01 | F30: 14:21:31 | G30: '=TEXT(F30-E30,"h:mm:ss")' -> '0:46:30' | H30: '=HOUR(E30)+MINUTE(E30)/60+SECOND(E30)/3600' -> 13.5836111111111 | I30: '=HOUR(F30)+MINUTE(F30)/60+SECOND(F30)/3600' -> 14.3586111111111

### `738a64e94c99|BLANK_PRECEDENT|DRP!L2`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/2_175-10_input.xlsx`
- location: `DRP!L2`  severity: Medium  confidence: Review
- formula: `=I2+J2-K2`
- evidence: Referenced cell DRP!J2 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'RE1'", "'RS1'"]; column header: "'NET'"; used range: A1:O23
- neighbourhood: J1: 'BUYING' | K1: 'SELLING' | L1: 'NET' | M1: 'BUYING' | N1: 'SELLING' | L2: '=I2+J2-K2' -> None | M2: 0 | N2: 0 | J3: 400 | K3: 20 | L3: '=I3+J3-K3' -> None | M3: 400 | N3: 20 | J4: 60 | K4: 20 | L4: '=I4+J4-K4' -> None | N4: 20

### `c21a65d89062|BLANK_PRECEDENT|data!G28|940b37`

- workbook: `all_data_912_v0.1/spreadsheet/56225/1_56225_input.xlsx`
- location: `data!G28`  severity: Medium  confidence: Review
- formula: `=TEXT(F28-E28,"h:mm:ss")`
- evidence: Referenced cell data!F28 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: '0:00:00'; row labels: ["'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: E26: 11:42:24 | F26: 11:47:48 | E27: 13:10:27 | F27: 14:35:03 | G28: '=TEXT(F28-E28,"h:mm:ss")' -> '0:00:00' | H28: '=HOUR(E28)+MINUTE(E28)/60+SECOND(E28)/3600' -> 0 | I28: '=HOUR(F28)+MINUTE(F28)/60+SECOND(F28)/3600' -> 0 | E29: 12:58:21 | F29: 13:18:19 | G29: '=TEXT(F29-E29,"h:mm:ss")' -> '0:19:58' | H29: '=HOUR(E29)+MINUTE(E29)/60+SECOND(E29)/3600' -> 12.9725 | I29: '=HOUR(F29)+MINUTE(F29)/60+SECOND(F29)/3600' -> 13.3052777777778 | E30: 13:35:01 | F30: 14:21:31 | G30: '=TEXT(F30-E30,"h:mm:ss")' -> '0:46:30' | H30: '=HOUR(E30)+MINUTE(E30)/60+SECOND(E30)/3600' -> 13.5836111111111 | I30: '=HOUR(F30)+MINUTE(F30)/60+SECOND(F30)/3600' -> 14.3586111111111

### `5cd8c4fe9805|BLANK_PRECEDENT|DATA!R3|599def`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!I3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 11 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 14 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 5 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -29

### `7b15ef0c0d8c|BLANK_PRECEDENT|data!G28|940b37`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!G28`  severity: Medium  confidence: Review
- formula: `=TEXT(F28-E28,"h:mm:ss")`
- evidence: Referenced cell data!F28 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: '0:00:00'; row labels: ["'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: E26: 11:42:24 | F26: 11:47:48 | E27: 13:10:27 | F27: 14:35:03 | G28: '=TEXT(F28-E28,"h:mm:ss")' -> '0:00:00' | H28: '=HOUR(E28)+MINUTE(E28)/60+SECOND(E28)/3600' -> 0 | I28: '=HOUR(F28)+MINUTE(F28)/60+SECOND(F28)/3600' -> 0 | E29: 12:58:21 | F29: 13:18:19 | G29: '=TEXT(F29-E29,"h:mm:ss")' -> '0:19:58' | H29: '=HOUR(E29)+MINUTE(E29)/60+SECOND(E29)/3600' -> 12.9725 | I29: '=HOUR(F29)+MINUTE(F29)/60+SECOND(F29)/3600' -> 13.3052777777778 | E30: 13:35:01 | F30: 14:21:31 | G30: '=TEXT(F30-E30,"h:mm:ss")' -> '0:46:30' | H30: '=HOUR(E30)+MINUTE(E30)/60+SECOND(E30)/3600' -> 13.5836111111111 | I30: '=HOUR(F30)+MINUTE(F30)/60+SECOND(F30)/3600' -> 14.3586111111111

### `6d6fc1caeb06|BLANK_PRECEDENT|DRP!I2`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/1_175-10_input.xlsx`
- location: `DRP!I2`  severity: Medium  confidence: Review
- formula: `=G2-H2`
- evidence: Referenced cell DRP!H2 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'RE1'", "'RS1'"]; column header: "'NET'"; used range: A1:O23
- neighbourhood: G1: 'BUYING' | H1: 'SELLING' | I1: 'NET' | J1: 'BUYING' | K1: 'SELLING' | G2: 11 | I2: '=G2-H2' -> None | G3: 400 | H3: 20 | I3: '=G3-H3' -> None | J3: 400 | K3: 20 | G4: 60 | H4: 20 | I4: '=G4-H4' -> None | J4: 60 | K4: 20

### `0233c00701a4|BLANK_PRECEDENT|AHMED!E7`

- workbook: `all_data_912_v0.1/spreadsheet/91-3/3_91-3_input.xlsx`
- location: `AHMED!E7`  severity: Medium  confidence: Review
- formula: `=E6+C7-D7`
- evidence: Referenced cell AHMED!C7 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'PURCHASE '"]; column header: ''; used range: A1:F12
- neighbourhood: C5: 15000 | E5: '=E4+C5-D5' -> None | D6: 5000 | E6: '=E5+C6-D6' -> None | D7: 2500 | E7: '=E6+C7-D7' -> None | D8: 3000 | E8: '=E7+C8-D8' -> None | C9: 25000 | E9: '=E8+C9-D9' -> None

### `95fdf876027b|BLANK_PRECEDENT|DATA!R3|0eae78`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `DATA!R3`  severity: Medium  confidence: Review
- formula: `=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Table1[[#This Row],[ADD 2 SIZE]])-Table1[[#This Row],[EXIT 1 SIZE]]`
- evidence: Referenced cell DATA!P3 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: 200; row labels: ["'XYZ'", "'Long'"]; column header: ''; used range: A1:AJ8
- neighbourhood: P1: 'EXIT 1 SIZE' | Q1: 'EXIT 2' | R1: 'EXIT 2 SIZE' | S1: 'MAX GAIN' | T1: 'POINTS' | P2: 100 | Q2: 10 | R2: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 800 | S2: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | Q3: 16 | R3: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 200 | S3: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> 3 | P4: 300 | Q4: 6 | R4: '=(Table1[[#This Row],[SIZE]]+Table1[[#This Row],[ADD 1 SIZE]]+Tabl... -> 700 | S4: '=Table1[[#This Row],[HIGH]]-Table1[[#This Row],[ENTRY]]' -> -9 | T4: '=IF(ISBLANK(Table1[[#This Row],[EXIT 1]]),Table1[[#This Row],[EXIT... -> -28.5

### `d7e27f29097e|BLANK_PRECEDENT|Malaga!M12|d1ba0b`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!M12`  severity: Medium  confidence: Review
- formula: `=IF(J12="","",IF(K12="G",$G$4-L12,IF(K12="N/G",$L$4-L12,IF(K12="S/S",$L$5-L12))))`
- evidence: Referenced cell Malaga!L12 is blank although the cells around it in its column hold data, and the formula uses it without testing for a blank.
- cached value: None; row labels: ["'DONNELLY (Rob)'", "'N/G'"]; column header: ''; used range: A1:AJ57
- neighbourhood: K10: 'G' | L10: 0 | M10: '=IF(J10="","",IF(K10="G",$G$4-L10,IF(K10="N/G",$L$4-L10,IF(K10="S/... -> 799 | O10: '=H7' -> 'La Cala Europa & Santa Mon... | K11: 'G' | L11: 0 | M11: '=IF(J11="","",IF(K11="G",$G$4-L11,IF(K11="N/G",$L$4-L11,IF(K11="S/... -> 799 | O11: '=C8' -> 'NAME' | M12: '=IF(J12="","",IF(K12="G",$G$4-L12,IF(K12="N/G",$L$4-L12,IF(K12="S/... -> None | O12: '=IF(C9="","",C9)' -> 'CURT (Kellie)' | K13: 'N/G' | L13: 0 | M13: '=IF(J13="","",IF(K13="G",$G$4-L13,IF(K13="N/G",$L$4-L13,IF(K13="S/... -> 449 | O13: '=IF(C10="","",C10)' -> 'CURT (Sean)' | K14: 'G' | L14: 0 | M14: '=IF(J14="","",IF(K14="G",$G$4-L14,IF(K14="N/G",$L$4-L14,IF(K14="S/... -> 799 | O14: '=IF(C11="","",C11)' -> 'DONNELLY (Louise)'

## BROKEN_REFERENCE

### `84b858fcb37f|BROKEN_REFERENCE|Sheet1!C11`

- workbook: `all_data_912_v0.1/spreadsheet/14240/1_14240_input.xlsx`
- location: `Sheet1!C11`  severity: Low  confidence: Info
- formula: `=+[1]BA!$AE$10`
- evidence: 270 cell(s) on Sheet1 link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Sheet1!C11, Sheet1!D11, Sheet1!E11, Sheet1!F11, Sheet1!G11, Sheet1!H11, Sheet1!I11, Sheet1!J11, ....
- cached value: 3507; row labels: ["'2Adults'"]; column header: ''; used range: A1:U75
- neighbourhood: A9: 'Individual' | B9: 750000 | C9: 6688 | D9: 8945 | E9: 11683 | A10: 'Individual' | B10: 1000000 | C10: 8160 | D10: 10913 | E10: 14252 | A11: '2Adults' | B11: 200000 | C11: '=+[1]BA!$AE$10' -> 3507 | D11: '=+[1]BA!$AE$11' -> 4925 | E11: '=+[1]BA!$AE$12' -> 6464 | A12: '2Adults' | B12: 300000 | C12: '=+[1]BA!$AE$19' -> 4959 | D12: '=+[1]BA!$AE$20' -> 6645 | E12: '=+[1]BA!$AE$21' -> 9098 | A13: '2Adults' | B13: 400000 | C13: '=+[1]BA!$AE$28' -> 6498 | D13: '=+[1]BA!$AE$29' -> 7695 | E13: '=+[1]BA!$AE$30' -> 11730

### `acb548947286|BROKEN_REFERENCE|Statistics!G44`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G44`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G42: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G43: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G44: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G45: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G46: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!C6`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!C6`  severity: High  confidence: Defect
- formula: `=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY8,0),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A4: 2023-10-16 00:00:00 | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | A5: 2023-10-23 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None

### `5d8557dfb652|BROKEN_REFERENCE|July-KPIs!B36`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!B36`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A36),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A34: '=IF(ROWS(A$6:A34)>DAY(J$13),"",J$12+ROWS(A$6:A34)-1)' -> None | B34: '=IFERROR(VLOOKUP(($C$1&"|"&A34),#REF!,2,0),"")' -> None | A35: '=IF(ROWS(A$6:A35)>DAY(J$13),"",J$12+ROWS(A$6:A35)-1)' -> None | B35: '=IFERROR(VLOOKUP(($C$1&"|"&A35),#REF!,2,0),"")' -> None | A36: '=IF(ROWS(A$6:A36)>DAY(J$13),"",J$12+ROWS(A$6:A36)-1)' -> None | B36: '=IFERROR(VLOOKUP(($C$1&"|"&A36),#REF!,2,0),"")' -> None

### `5b3e1270b4b8|BROKEN_REFERENCE|Sheet1!A18`

- workbook: `all_data_912_v0.1/spreadsheet/382-10/1_382-10_input.xlsx`
- location: `Sheet1!A18`  severity: High  confidence: Defect
- formula: `=IFERROR(#REF!/#REF!,0)`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:A18
- neighbourhood: A16: 4.4 | A17: 4.5 | A18: '=IFERROR(#REF!/#REF!,0)' -> None

### `7dfe4964af12|BROKEN_REFERENCE|Sheet1!C7`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!C7`  severity: High  confidence: Defect
- formula: `=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY9,0),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A5: 2023-11-06 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A9: 2023-11-20 00:00:00 | C9: '=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D9: '=IF(AND(B9>0,$AW11>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None

### `74d967658eee|BROKEN_REFERENCE|Sheet1!AN57`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!AN57`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:25)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: ["'4/26.2021'"]; column header: ''; used range: A1:CJ782
- neighbourhood: AN55: '=IFERROR(LARGE(#REF!,ROWS($1:23)),"")' -> None | AN56: '=IFERROR(LARGE(#REF!,ROWS($1:24)),"")' -> None | AN57: '=IFERROR(LARGE(#REF!,ROWS($1:25)),"")' -> None | AN58: '=IFERROR(LARGE(#REF!,ROWS($1:26)),"")' -> None | AN59: '=IFERROR(LARGE(#REF!,ROWS($1:27)),"")' -> None

### `a556b2a52595|BROKEN_REFERENCE|Sheet1!C6`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!C6`  severity: High  confidence: Defect
- formula: `=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY8,0),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A4: 2023-10-16 00:00:00 | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | A5: 2023-10-23 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None

### `c2c1c9ef2579|BROKEN_REFERENCE|formamspnc(7)!I10`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!I10`  severity: High  confidence: Defect
- formula: `=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10=""),NOT(BH11="")),6,IF(AND(AR10=0,BH10="b"),"X",IF(AR10=0,"Y",""))))`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: ["'14c/19c/21c/24c/28c/36c/39c/50c/55c/58c/66c/70c(1 ext 1u..."]; column header: ''; used range: A1:ED48610
- neighbourhood: G8: '=IF(AND(OR(F8=1,F8=2),OR(BH8="b",BH8="c",BH8=1)),1,IF(AND(OR(AD8=$... -> None | H8: '=IF(OR(AND(K8="D",L8="E",M8="F"),AND(ISNUMBER(BI8),G8=2)),"H",IF(O... -> None | I8: '=IF(AND(NOT(BH8=""),NOT(BH9=""),NOT(BH10="")),7,IF(AND(NOT(BH8="")... -> None | J8: '=IF(AND(OR(H8="h",AND(K8="d",L8="e"),AND(L8="e",M8="f"),AND(K8="d"... -> None | K8: '=IF(AND(AE8=0,AF8=0,ISNUMBER(BI8)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> None | G9: '=IF(AND(OR(F9=1,F9=2),OR(BH9="b",BH9="c",BH9=1)),1,IF(AND(OR(AD9=$... -> None | H9: '=IF(OR(AND(K9="D",L9="E",M9="F"),AND(ISNUMBER(BI9),G9=2)),"H",IF(O... -> None | I9: '=IF(AND(NOT(BH9=""),NOT(BH10=""),NOT(BH11="")),7,IF(AND(NOT(BH9=""... -> None | J9: '=IF(AND(OR(H9="h",AND(K9="d",L9="e"),AND(L9="e",M9="f"),AND(K9="d"... -> None | K9: '=IF(AND(AE9=0,AF9=0,ISNUMBER(BI9)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> 'D' | G10: '=IF(AND(OR(F10=1,F10=2),OR(BH10="b",BH10="c",BH10=1)),1,IF(AND(OR(... -> None | H10: '=IF(OR(AND(K10="D",L10="E",M10="F"),AND(ISNUMBER(BI10),G10=2)),"H"... -> None | I10: '=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10... -> '#REF!' | J10: '=IF(AND(OR(H10="h",AND(K10="d",L10="e"),AND(L10="e",M10="f"),AND(K... -> None | K10: '=IF(AND(AE10=0,AF10=0,ISNUMBER(BI10)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None | G11: '=IF(AND(OR(F11=1,F11=2),OR(BH11="b",BH11="c",BH11=1)),1,IF(AND(OR(... -> None | H11: '=IF(OR(AND(K11="D",L11="E",M11="F"),AND(ISNUMBER(BI11),G11=2)),"H"... -> None | I11: '=IF(AND(NOT(BH11=""),NOT(#REF!=""),NOT(#REF!="")),7,IF(AND(NOT(BH1... -> '#REF!' | J11: '=IF(AND(OR(H11="h",AND(K11="d",L11="e"),AND(L11="e",M11="f"),AND(K... -> None | K11: '=IF(AND(AE11=0,AF11=0,ISNUMBER(BI11)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None

### `8734ff2c3db4|BROKEN_REFERENCE|Sheet1!C12`

- workbook: `all_data_912_v0.1/spreadsheet/50631/1_50631_input.xlsx`
- location: `Sheet1!C12`  severity: High  confidence: Defect
- formula: `=IFERROR(INDEX(#REF!,MATCH(B12,#REF!,0)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: B10: '=IF($B$3+ROWS($B$7:$B10)-1<=$F$3,$B$3+ROWS($B$7:$B10)-1,"")' -> 2021-09-04 00:00:00 | C10: '=IFERROR(INDEX(#REF!,MATCH(B10,#REF!,0)),"")' -> None | D10: '=IF($B$3+ROWS($B$7:$D41)-1<=$F$3,$B$3+ROWS($B$7:$D41)-1,"")' -> 2021-10-05 00:00:00 | B11: '=IF($B$3+ROWS($B$7:$B11)-1<=$F$3,$B$3+ROWS($B$7:$B11)-1,"")' -> 2021-09-05 00:00:00 | C11: '=IFERROR(INDEX(#REF!,MATCH(B11,#REF!,0)),"")' -> None | D11: '=IF($B$3+ROWS($B$7:$D42)-1<=$F$3,$B$3+ROWS($B$7:$D42)-1,"")' -> 2021-10-06 00:00:00 | B12: '=IF($B$3+ROWS($B$7:$B12)-1<=$F$3,$B$3+ROWS($B$7:$B12)-1,"")' -> 2021-09-06 00:00:00 | C12: '=IFERROR(INDEX(#REF!,MATCH(B12,#REF!,0)),"")' -> None | D12: '=IF($B$3+ROWS($B$7:$D43)-1<=$F$3,$B$3+ROWS($B$7:$D43)-1,"")' -> 2021-10-07 00:00:00 | B13: '=IF($B$3+ROWS($B$7:$B13)-1<=$F$3,$B$3+ROWS($B$7:$B13)-1,"")' -> 2021-09-07 00:00:00 | C13: '=IFERROR(INDEX(#REF!,MATCH(B13,#REF!,0)),"")' -> None | D13: '=IF($B$3+ROWS($B$7:$D44)-1<=$F$3,$B$3+ROWS($B$7:$D44)-1,"")' -> 2021-10-08 00:00:00 | B14: '=IF($B$3+ROWS($B$7:$B14)-1<=$F$3,$B$3+ROWS($B$7:$B14)-1,"")' -> 2021-09-08 00:00:00 | C14: '=IFERROR(INDEX(#REF!,MATCH(B14,#REF!,0)),"")' -> None | D14: '=IF($B$3+ROWS($B$7:$D45)-1<=$F$3,$B$3+ROWS($B$7:$D45)-1,"")' -> 2021-10-09 00:00:00

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G18`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G18`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E16: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G16: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E17: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G17: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E18: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G18: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E19: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G19: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E20: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G20: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `6d5548493a93|BROKEN_REFERENCE|July-KPIs!B12`

- workbook: `all_data_912_v0.1/spreadsheet/1726/1_1726_input.xlsx`
- location: `July-KPIs!B12`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A12),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A10: '=IF(ROWS(A$6:A10)>DAY(J$13),"",J$12+ROWS(A$6:A10)-1)' -> 2024-07-14 00:00:00 | B10: '=IFERROR(VLOOKUP(($C$1&"|"&A10),#REF!,2,0),"")' -> None | A11: '=IF(ROWS(A$6:A11)>DAY(J$13),"",J$12+ROWS(A$6:A11)-1)' -> 2024-07-15 00:00:00 | B11: '=IFERROR(VLOOKUP(($C$1&"|"&A11),#REF!,2,0),"")' -> None | A12: '=IF(ROWS(A$6:A12)>DAY(J$13),"",J$12+ROWS(A$6:A12)-1)' -> 2024-07-16 00:00:00 | B12: '=IFERROR(VLOOKUP(($C$1&"|"&A12),#REF!,2,0),"")' -> None | A13: '=IF(ROWS(A$6:A13)>DAY(J$13),"",J$12+ROWS(A$6:A13)-1)' -> 2024-07-17 00:00:00 | B13: '=IFERROR(VLOOKUP(($C$1&"|"&A13),#REF!,2,0),"")' -> None | A14: '=IF(ROWS(A$6:A14)>DAY(J$13),"",J$12+ROWS(A$6:A14)-1)' -> 2024-07-18 00:00:00 | B14: '=IFERROR(VLOOKUP(($C$1&"|"&A14),#REF!,2,0),"")' -> None

### `1ee00a60f590|BROKEN_REFERENCE|Sheet1!AN55`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!AN55`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:23)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: AN53: '=IFERROR(LARGE(#REF!,ROWS($1:21)),"")' -> None | AN54: '=IFERROR(LARGE(#REF!,ROWS($1:22)),"")' -> None | AN55: '=IFERROR(LARGE(#REF!,ROWS($1:23)),"")' -> None | AN56: '=IFERROR(LARGE(#REF!,ROWS($1:24)),"")' -> None | AN57: '=IFERROR(LARGE(#REF!,ROWS($1:25)),"")' -> None

### `7dfe4964af12|BROKEN_REFERENCE|Sheet1!C5`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!C5`  severity: High  confidence: Defect
- formula: `=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER(MATCH(#REF!,$BE$2:$BV$2,0)),ISNUMBER(MATCH($BF$5,UPPER($BE$3:$BV$3),0))),INDEX($BE$3:$BV$81,MATCH(#REF!,$BD$3:$BD$81,0),MATCH(#REF!,$BE$2:$BV$2,0)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: "'Goal #'"; used range: A1:BR82
- range $BD$3:$BD$81: values ["'Date'", '2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'BD2: None', 'below': 'BD82: None'}
- neighbourhood: A3: 'Week ' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | A4: 2023-10-16 00:00:00 | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | A5: 2023-11-06 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!D6`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D6`  severity: High  confidence: Defect
- formula: `=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY8/100),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | F7: 0.0867052023121387 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | F8: '=IF(AND(NOT(ISBLANK(E8)),B8>0,$AW10>0),IFERROR(E8/B8,""),"")' -> None

### `acb548947286|BROKEN_REFERENCE|Statistics!G52`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G52`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E50: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G50: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E51: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G51: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E52: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G52: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E53: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G53: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E54: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G54: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G30`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G30`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G28: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E29: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G29: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E30: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G30: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E31: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G31: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E32: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G32: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `b230bc5037bf|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A24|0dcee9`

- workbook: `all_data_912_v0.1/spreadsheet/47699/3_47699_input.xlsx`
- location: `Prev working day Quote (2)!A24`  severity: High  confidence: Defect
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A22: False | B22: 'Oscar' | C22: 7 | A23: True | B23: 'Oscar' | C23: 7 | A24: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B24: 'Oscar' | C24: 7 | A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G52`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G52`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E50: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G50: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E51: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G51: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E52: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G52: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E53: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G53: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E54: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G54: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `40c4eca66328|BROKEN_REFERENCE|Sheet1!C15`

- workbook: `all_data_912_v0.1/spreadsheet/50631/2_50631_input.xlsx`
- location: `Sheet1!C15`  severity: High  confidence: Defect
- formula: `=IFERROR(INDEX(#REF!,MATCH(B15,#REF!,0)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: B13: '=IF($B$3+ROWS($B$7:$B13)-1<=$F$3,$B$3+ROWS($B$7:$B13)-1,"")' -> 2021-10-07 00:00:00 | C13: '=IFERROR(INDEX(#REF!,MATCH(B13,#REF!,0)),"")' -> None | D13: '=IF($B$3+ROWS($B$7:$D44)-1<=$F$3,$B$3+ROWS($B$7:$D44)-1,"")' -> 2021-11-07 00:00:00 | B14: '=IF($B$3+ROWS($B$7:$B14)-1<=$F$3,$B$3+ROWS($B$7:$B14)-1,"")' -> 2021-10-08 00:00:00 | C14: '=IFERROR(INDEX(#REF!,MATCH(B14,#REF!,0)),"")' -> None | D14: '=IF($B$3+ROWS($B$7:$D45)-1<=$F$3,$B$3+ROWS($B$7:$D45)-1,"")' -> 2021-11-08 00:00:00 | B15: '=IF($B$3+ROWS($B$7:$B15)-1<=$F$3,$B$3+ROWS($B$7:$B15)-1,"")' -> 2021-10-09 00:00:00 | C15: '=IFERROR(INDEX(#REF!,MATCH(B15,#REF!,0)),"")' -> None | D15: '=IF($B$3+ROWS($B$7:$D46)-1<=$F$3,$B$3+ROWS($B$7:$D46)-1,"")' -> 2021-11-09 00:00:00 | B16: '=IF($B$3+ROWS($B$7:$B16)-1<=$F$3,$B$3+ROWS($B$7:$B16)-1,"")' -> 2021-10-10 00:00:00 | C16: '=IFERROR(INDEX(#REF!,MATCH(B16,#REF!,0)),"")' -> None | D16: '=IF($B$3+ROWS($B$7:$D47)-1<=$F$3,$B$3+ROWS($B$7:$D47)-1,"")' -> 2021-11-10 00:00:00 | B17: '=IF($B$3+ROWS($B$7:$B17)-1<=$F$3,$B$3+ROWS($B$7:$B17)-1,"")' -> 2021-10-11 00:00:00 | C17: '=IFERROR(INDEX(#REF!,MATCH(B17,#REF!,0)),"")' -> None | D17: '=IF($B$3+ROWS($B$7:$D48)-1<=$F$3,$B$3+ROWS($B$7:$D48)-1,"")' -> 2021-11-11 00:00:00

### `7bd972dd1e37|BROKEN_REFERENCE|July-KPIs!B19`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!B19`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A19),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A17: '=IF(ROWS(A$6:A17)>DAY(J$13),"",J$12+ROWS(A$6:A17)-1)' -> 2021-07-13 00:00:00 | B17: '=IFERROR(VLOOKUP(($C$1&"|"&A17),#REF!,2,0),"")' -> None | A18: '=IF(ROWS(A$6:A18)>DAY(J$13),"",J$12+ROWS(A$6:A18)-1)' -> 2021-07-14 00:00:00 | B18: '=IFERROR(VLOOKUP(($C$1&"|"&A18),#REF!,2,0),"")' -> None | A19: '=IF(ROWS(A$6:A19)>DAY(J$13),"",J$12+ROWS(A$6:A19)-1)' -> 2021-07-15 00:00:00 | B19: '=IFERROR(VLOOKUP(($C$1&"|"&A19),#REF!,2,0),"")' -> None | A20: '=IF(ROWS(A$6:A20)>DAY(J$13),"",J$12+ROWS(A$6:A20)-1)' -> 2021-07-16 00:00:00 | B20: '=IFERROR(VLOOKUP(($C$1&"|"&A20),#REF!,2,0),"")' -> None | A21: '=IF(ROWS(A$6:A21)>DAY(J$13),"",J$12+ROWS(A$6:A21)-1)' -> 2021-07-17 00:00:00 | B21: '=IFERROR(VLOOKUP(($C$1&"|"&A21),#REF!,2,0),"")' -> None

### `4ea284d68c01|BROKEN_REFERENCE|Sheet1!AN59`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!AN59`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:27)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: AN57: '=IFERROR(LARGE(#REF!,ROWS($1:25)),"")' -> None | AN58: '=IFERROR(LARGE(#REF!,ROWS($1:26)),"")' -> None | AN59: '=IFERROR(LARGE(#REF!,ROWS($1:27)),"")' -> None | AN60: '=IFERROR(LARGE(#REF!,ROWS($1:28)),"")' -> None | AN61: '=IFERROR(LARGE(#REF!,ROWS($1:29)),"")' -> None

### `5d8557dfb652|BROKEN_REFERENCE|July-KPIs!B35`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!B35`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A35),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A33: '=IF(ROWS(A$6:A33)>DAY(J$13),"",J$12+ROWS(A$6:A33)-1)' -> None | B33: '=IFERROR(VLOOKUP(($C$1&"|"&A33),#REF!,2,0),"")' -> None | A34: '=IF(ROWS(A$6:A34)>DAY(J$13),"",J$12+ROWS(A$6:A34)-1)' -> None | B34: '=IFERROR(VLOOKUP(($C$1&"|"&A34),#REF!,2,0),"")' -> None | A35: '=IF(ROWS(A$6:A35)>DAY(J$13),"",J$12+ROWS(A$6:A35)-1)' -> None | B35: '=IFERROR(VLOOKUP(($C$1&"|"&A35),#REF!,2,0),"")' -> None | A36: '=IF(ROWS(A$6:A36)>DAY(J$13),"",J$12+ROWS(A$6:A36)-1)' -> None | B36: '=IFERROR(VLOOKUP(($C$1&"|"&A36),#REF!,2,0),"")' -> None

### `4ea284d68c01|BROKEN_REFERENCE|Sheet1!AN49`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!AN49`  severity: High  confidence: Defect
- formula: `=IFERROR(LARGE(#REF!,ROWS($1:17)),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: AN49: '=IFERROR(LARGE(#REF!,ROWS($1:17)),"")' -> None | AN50: '=IFERROR(LARGE(#REF!,ROWS($1:18)),"")' -> None | AN51: '=IFERROR(LARGE(#REF!,ROWS($1:19)),"")' -> None

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G43`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G43`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G41: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G42: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G43: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G44: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G45: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

## CIRCULAR_REFERENCE

### `92f8bf691072|CIRCULAR_REFERENCE|Test!F12`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F12`  severity: High  confidence: Likely defect
- evidence: Test!F12 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,2,0),"")' -> None | E10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,3,0),"")' -> None | F10: '=IF(OR(B10="PRG/FLY",B10="PRG/TVL",B10="FLY1",B10="TVL1",B10="PRG/... -> None | G10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,5,0),"")' -> None | D11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,2,0),"")' -> None | E11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,3,0),"")' -> None | F11: '=IF(OR(B11="PRG/FLY",B11="PRG/TVL",B11="FLY1",B11="TVL1",B11="PRG/... -> None | G11: '=IFERROR(VLOOKUP(C11,DATA!$A:$E,5,0),"")' -> None | D12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,2,0),"")' -> None | E12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,3,0),"")' -> None | F12: '=IF(OR(B12="PRG/FLY",B12="PRG/TVL",B12="FLY1",B12="TVL1",B12="PRG/... -> None | G12: '=IFERROR(VLOOKUP(C12,DATA!$A:$E,5,0),"")' -> None | D13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,2,0),"")' -> None | E13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,3,0),"")' -> None | F13: '=IF(OR(B13="PRG/FLY",B13="PRG/TVL",B13="FLY1",B13="TVL1",B13="PRG/... -> None | G13: '=IFERROR(VLOOKUP(C13,DATA!$A:$E,5,0),"")' -> None | D14: '=IFERROR(VLOOKUP(C14,DATA!$A:$E,2,0),"")' -> None | E14: '=IFERROR(VLOOKUP(C14,DATA!$A:$E,3,0),"")' -> None | F14: '=IF(OR(B14="PRG/FLY",B14="PRG/TVL",B14="FLY1",B14="TVL1",B14="PRG/... -> None | G14: '=IFERROR(VLOOKUP(C14,DATA!$A:$E,5,0),"")' -> None

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F35`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F35`  severity: High  confidence: Likely defect
- evidence: Test!F35 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,2,0),"")' -> None | E33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,3,0),"")' -> None | F33: '=IF(OR(B33="PRG/FLY",B33="PRG/TVL",B33="FLY1",B33="TVL1",B33="PRG/... -> None | G33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,5,0),"")' -> None | D34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,2,0),"")' -> None | E34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,3,0),"")' -> None | F34: '=IF(OR(B34="PRG/FLY",B34="PRG/TVL",B34="FLY1",B34="TVL1",B34="PRG/... -> None | G34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,5,0),"")' -> None | D35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,2,0),"")' -> None | E35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,3,0),"")' -> None | F35: '=IF(OR(B35="PRG/FLY",B35="PRG/TVL",B35="FLY1",B35="TVL1",B35="PRG/... -> None | G35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,5,0),"")' -> None | D36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,2,0),"")' -> None | E36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,3,0),"")' -> None | F36: '=IF(OR(B36="PRG/FLY",B36="PRG/TVL",B36="FLY1",B36="TVL1",B36="PRG/... -> None | G36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,5,0),"")' -> None | D37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,2,0),"")' -> None | E37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,3,0),"")' -> None | F37: '=IF(OR(B37="PRG/FLY",B37="PRG/TVL",B37="FLY1",B37="TVL1",B37="PRG/... -> None | G37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,5,0),"")' -> None

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F31`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F31`  severity: High  confidence: Likely defect
- evidence: Test!F31 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,2,0),"")' -> None | E29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,3,0),"")' -> None | F29: '=IF(OR(B29="PRG/FLY",B29="PRG/TVL",B29="FLY1",B29="TVL1",B29="PRG/... -> None | G29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,5,0),"")' -> None | D30: '=IFERROR(VLOOKUP(C30,DATA!$A:$E,2,0),"")' -> None | E30: '=IFERROR(VLOOKUP(C30,DATA!$A:$E,3,0),"")' -> None | F30: '=IF(OR(B30="PRG/FLY",B30="PRG/TVL",B30="FLY1",B30="TVL1",B30="PRG/... -> None | G30: '=IFERROR(VLOOKUP(C30,DATA!$A:$E,5,0),"")' -> None | D31: '=IFERROR(VLOOKUP(C31,DATA!$A:$E,2,0),"")' -> None | E31: '=IFERROR(VLOOKUP(C31,DATA!$A:$E,3,0),"")' -> None | F31: '=IF(OR(B31="PRG/FLY",B31="PRG/TVL",B31="FLY1",B31="TVL1",B31="PRG/... -> None | G31: '=IFERROR(VLOOKUP(C31,DATA!$A:$E,5,0),"")' -> None | D32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,2,0),"")' -> None | E32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,3,0),"")' -> None | F32: '=IF(OR(B32="PRG/FLY",B32="PRG/TVL",B32="FLY1",B32="TVL1",B32="PRG/... -> None | G32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,5,0),"")' -> None | D33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,2,0),"")' -> None | E33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,3,0),"")' -> None | F33: '=IF(OR(B33="PRG/FLY",B33="PRG/TVL",B33="FLY1",B33="TVL1",B33="PRG/... -> None | G33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,5,0),"")' -> None

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F3`  severity: High  confidence: Likely defect
- evidence: Test!F3 depends on itself, for example a total whose range includes the total cell.
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'OOO' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:25:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `70a7680e9819|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/3_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F27`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F27`  severity: High  confidence: Likely defect
- evidence: Test!F27 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D25: '=IFERROR(VLOOKUP(C25,DATA!$A:$E,2,0),"")' -> None | E25: '=IFERROR(VLOOKUP(C25,DATA!$A:$E,3,0),"")' -> None | F25: '=IF(OR(B25="PRG/FLY",B25="PRG/TVL",B25="FLY1",B25="TVL1",B25="PRG/... -> None | G25: '=IFERROR(VLOOKUP(C25,DATA!$A:$E,5,0),"")' -> None | D26: '=IFERROR(VLOOKUP(C26,DATA!$A:$E,2,0),"")' -> None | E26: '=IFERROR(VLOOKUP(C26,DATA!$A:$E,3,0),"")' -> None | F26: '=IF(OR(B26="PRG/FLY",B26="PRG/TVL",B26="FLY1",B26="TVL1",B26="PRG/... -> None | G26: '=IFERROR(VLOOKUP(C26,DATA!$A:$E,5,0),"")' -> None | D27: '=IFERROR(VLOOKUP(C27,DATA!$A:$E,2,0),"")' -> None | E27: '=IFERROR(VLOOKUP(C27,DATA!$A:$E,3,0),"")' -> None | F27: '=IF(OR(B27="PRG/FLY",B27="PRG/TVL",B27="FLY1",B27="TVL1",B27="PRG/... -> None | G27: '=IFERROR(VLOOKUP(C27,DATA!$A:$E,5,0),"")' -> None | D28: '=IFERROR(VLOOKUP(C28,DATA!$A:$E,2,0),"")' -> None | E28: '=IFERROR(VLOOKUP(C28,DATA!$A:$E,3,0),"")' -> None | F28: '=IF(OR(B28="PRG/FLY",B28="PRG/TVL",B28="FLY1",B28="TVL1",B28="PRG/... -> None | G28: '=IFERROR(VLOOKUP(C28,DATA!$A:$E,5,0),"")' -> None | D29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,2,0),"")' -> None | E29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,3,0),"")' -> None | F29: '=IF(OR(B29="PRG/FLY",B29="PRG/TVL",B29="FLY1",B29="TVL1",B29="PRG/... -> None | G29: '=IFERROR(VLOOKUP(C29,DATA!$A:$E,5,0),"")' -> None

### `92f8bf691072|CIRCULAR_REFERENCE|Test!F35`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F35`  severity: High  confidence: Likely defect
- evidence: Test!F35 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,2,0),"")' -> None | E33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,3,0),"")' -> None | F33: '=IF(OR(B33="PRG/FLY",B33="PRG/TVL",B33="FLY1",B33="TVL1",B33="PRG/... -> None | G33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,5,0),"")' -> None | D34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,2,0),"")' -> None | E34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,3,0),"")' -> None | F34: '=IF(OR(B34="PRG/FLY",B34="PRG/TVL",B34="FLY1",B34="TVL1",B34="PRG/... -> None | G34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,5,0),"")' -> None | D35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,2,0),"")' -> None | E35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,3,0),"")' -> None | F35: '=IF(OR(B35="PRG/FLY",B35="PRG/TVL",B35="FLY1",B35="TVL1",B35="PRG/... -> None | G35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,5,0),"")' -> None | D36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,2,0),"")' -> None | E36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,3,0),"")' -> None | F36: '=IF(OR(B36="PRG/FLY",B36="PRG/TVL",B36="FLY1",B36="TVL1",B36="PRG/... -> None | G36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,5,0),"")' -> None | D37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,2,0),"")' -> None | E37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,3,0),"")' -> None | F37: '=IF(OR(B37="PRG/FLY",B37="PRG/TVL",B37="FLY1",B37="TVL1",B37="PRG/... -> None | G37: '=IFERROR(VLOOKUP(C37,DATA!$A:$E,5,0),"")' -> None

### `9c38434cffc6|CIRCULAR_REFERENCE|BRE!Q2`

- workbook: `all_data_912_v0.1/spreadsheet/342-46/2_342-46_input.xlsx`
- location: `BRE!Q2`  severity: High  confidence: Likely defect
- evidence: BRE!Q2 depends on itself, for example a total whose range includes the total cell.
- cached value: 'BRE'; row labels: ["'BR PE - '", "'BRE'"]; column header: "'Branch'"; used range: A1:Q2
- neighbourhood: Q1: 'Branch' | Q2: '=MID(CELL("filename",Q2),FIND("]",CELL("filename",Q2))+1,255)' -> 'BRE'

### `a6f136b4462b|CIRCULAR_REFERENCE|BRE!Q2`

- workbook: `all_data_912_v0.1/spreadsheet/342-46/3_342-46_input.xlsx`
- location: `BRE!Q2`  severity: High  confidence: Likely defect
- evidence: BRE!Q2 depends on itself, for example a total whose range includes the total cell.
- cached value: 'BRE'; row labels: ["'BR PE - '", "'BRE'"]; column header: "'Branch'"; used range: A1:Q2
- neighbourhood: Q1: 'Branch' | Q2: '=MID(CELL("filename",Q2),FIND("]",CELL("filename",Q2))+1,255)' -> 'BRE'

### `21bdc0943b23|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/1_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `b9a46fca8da1|CIRCULAR_REFERENCE|BRE!Q2`

- workbook: `all_data_912_v0.1/spreadsheet/342-46/1_342-46_input.xlsx`
- location: `BRE!Q2`  severity: High  confidence: Likely defect
- evidence: BRE!Q2 depends on itself, for example a total whose range includes the total cell.
- cached value: 'BRE'; row labels: ["'BR PE - '", "'BRE'"]; column header: "'Branch'"; used range: A1:Q2
- neighbourhood: Q1: 'Branch' | Q2: '=MID(CELL("filename",Q2),FIND("]",CELL("filename",Q2))+1,255)' -> 'BRE'

### `0a3eeb22d16c|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/2_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

## DUPLICATE_KEY

### `1c06477fced9|DUPLICATE_KEY|URNlookup!K1044,URNlookup!K1407`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `URN lookup!K1044, URN lookup!K1407`  severity: Medium  confidence: Review
- evidence: Normalized key 'dl10 7da' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'DL10 7DA'; row labels: ["'Darlington Road'", "'Richmond'"]; column header: "'YO12 5LH'"; used range: A1:X1461
- neighbourhood: J1042: 'Selby' | K1042: 'YO8 4HT' | L1042: 'Open' | J1043: 'Scarborough' | K1043: 'YO12 5LH' | L1043: 'Closed' | J1044: 'Richmond' | K1044: 'DL10 7DA' | L1044: 'Closed' | J1045: 'Skipton' | K1045: 'BD23 1PL' | L1045: 'Open' | J1046: 'Harrogate' | K1046: 'HG2 8PT' | L1046: 'Open'

### `ac9c457a4aed|DUPLICATE_KEY|URNlookup!K1072,URNlookup!K1437`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `URN lookup!K1072, URN lookup!K1437`  severity: Medium  confidence: Review
- evidence: Normalized key 'hg5 0dq' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'HG5 0DQ'; row labels: ["'Park Lane'", "'Knaresborough'"]; column header: "'YO12 4HA'"; used range: A1:X1461
- neighbourhood: J1070: 'Northallerton' | K1070: 'DL7 9QW' | L1070: 'Open' | J1071: 'Scarborough' | K1071: 'YO12 4HA' | L1071: 'Open' | J1072: 'Knaresborough' | K1072: 'HG5 0DQ' | L1072: 'Closed' | J1073: 'Harrogate' | K1073: 'HG2 7LW' | L1073: 'Open' | J1074: 'Skipton' | K1074: 'BD23 2DB' | L1074: 'Open'

### `eba9bd965a28|DUPLICATE_KEY|ZORD!A5,ZORD!A7`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `ZORD!A5, ZORD!A7`  severity: Medium  confidence: Review
- evidence: Normalized key 'abc2' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'ABC2'; row labels: []; column header: "'ABC1'"; used range: A1:E15
- neighbourhood: A3: 'ABC1' | B3: 2021-01-01 00:00:00 | C3: 2024-12-31 00:00:00 | A4: 'ABC1' | B4: 2022-01-07 00:00:00 | C4: 2023-12-31 00:00:00 | A5: 'ABC2' | B5: 2021-01-01 00:00:00 | C5: 2022-12-31 00:00:00 | A6: 'ABC3' | B6: 2021-10-01 00:00:00 | C6: 2024-12-01 00:00:00 | A7: 'ABC2' | B7: 2021-10-01 00:00:00 | C7: 2024-12-31 00:00:00

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A20,RS.Food!A443`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A20, RS.Food!A443`  severity: Medium  confidence: Review
- evidence: Normalized key 'smoked salmon scrambled eggs bri' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Smoked Salmon Scrambled Eggs Bri'; row labels: []; column header: "'Eggs Benedict'"; used range: A1:W607
- neighbourhood: A18: 'Pancakes' | B18: 1092 | C18: 0.00700178186371788 | A19: 'Eggs Benedict' | B19: 1064 | C19: 0.00682224899541742 | A20: 'Smoked Salmon Scrambled Eggs Bri' | B20: 966 | C20: 0.00619388395636582 | A21: 'Mixed Pastry' | B21: 850 | C21: 0.00545010493054963 | A22: 'Chinese Brkfst' | B22: 792 | C22: 0.00507821541764154

### `ac9c457a4aed|DUPLICATE_KEY|URNlookup!K38,URNlookup!K1420`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `URN lookup!K38, URN lookup!K1420`  severity: Medium  confidence: Review
- evidence: Normalized key 'ca26 3xa' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'CA26 3XA'; row labels: ["'Arlecdon Primary School'", "'FRIZINGTON'"]; column header: "'CA14 4ES'"; used range: A1:X1461
- neighbourhood: J36: 'Workington' | K36: 'CA14 3JG' | L36: 'Open' | J37: 'Workington' | K37: 'CA14 4ES' | L37: 'Open' | I38: 'Arlecdon Primary School' | J38: 'FRIZINGTON' | K38: 'CA26 3XA' | L38: 'Closed' | J39: 'Egremont' | K39: 'CA22 2LT' | L39: 'Open' | J40: 'Frizington' | K40: 'CA26 3PF' | L40: 'Open'

### `21865bab73e8|DUPLICATE_KEY|RS.Food!A577,RS.Food!A598`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!A577, RS.Food!A598`  severity: Medium  confidence: Review
- evidence: Normalized key 'small mixed nuts amen' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Small Mixed Nuts AMEN'; row labels: []; column header: "'Small Gugelhupf AMEN'"; used range: A1:W607
- neighbourhood: A575: 'Small Fruit Skewers AMEN' | B575: 0 | C575: 0 | A576: 'Small Gugelhupf AMEN' | B576: 0 | C576: 0 | A577: 'Small Mixed Nuts AMEN' | B577: 0 | C577: 0 | A578: 'Small Sliced Fruit AMEN' | B578: 0 | C578: 0 | A579: 'Small Sliced Fruit AMEN' | B579: 0 | C579: 0

### `852b58472b57|DUPLICATE_KEY|Sheet1!D2,Sheet1!D6`

- workbook: `all_data_912_v0.1/spreadsheet/59185/1_59185_input.xlsx`
- location: `Sheet1!D2, Sheet1!D6`  severity: Medium  confidence: Review
- evidence: Normalized key 'cbv/wbnb mix' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'CBV/WBNB mix'; row labels: ["'WBNB Splits'", "'GNB Splits'"]; column header: "'Mill Inventory'"; used range: A1:P24
- neighbourhood: D1: 'Mill Inventory' | B2: 'GNB Splits' | D2: 'CBV/WBNB mix' | E2: 'Pb' | F2: 'PB/CBV mix' | B3: 1026 | C3: 1192 | D3: 4116 | E3: 1102 | F3: 2166 | D4: 'QC HOLD'

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K802,URNlookup!K1387`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K802, URN lookup!K1387`  severity: Medium  confidence: Review
- evidence: Normalized key 'yo11 3lg' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'YO11 3LG'; row labels: ["'Eastfield'", "'Scarborough'"]; column header: "'YO12 6NQ'"; used range: A1:X1461
- neighbourhood: J800: 'Pickering' | K800: 'YO18 8SA' | L800: 'Open' | J801: 'Scarborough' | K801: 'YO12 6NQ' | L801: 'Open' | J802: 'Scarborough' | K802: 'YO11 3LG' | L802: 'Closed' | J803: 'Scarborough' | K803: 'YO11 1HS' | L803: 'Closed' | J804: 'Scarborough' | K804: 'YO12 7DD' | L804: 'Open'

### `1c06477fced9|DUPLICATE_KEY|URNlookup!K341,URNlookup!K617`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `URN lookup!K341, URN lookup!K617`  severity: Medium  confidence: Review
- evidence: Normalized key 'pr2 3yp' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'PR2 3YP'; row labels: ["'Ingol'", "'Preston'"]; column header: "'PR2 1TU'"; used range: A1:X1461
- neighbourhood: J339: 'Preston' | K339: 'PR2 2BN' | L339: 'Open' | J340: 'Preston' | K340: 'PR2 1TU' | L340: 'Open' | J341: 'Preston' | K341: 'PR2 3YP' | L341: 'Open' | J342: 'Barnoldswick' | K342: 'BB18 6UD' | L342: 'Open' | J343: 'Barnoldswick' | K343: 'BB18 6SJ' | L343: 'Open'

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K972,URNlookup!K1010`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K972, URN lookup!K1010`  severity: Medium  confidence: Review
- evidence: Normalized key 'hg4 2es' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'HG4 2ES'; row labels: ["'Church Lane'", "'Ripon'"]; column header: "'HG4 1LT'"; used range: A1:X1461
- neighbourhood: J970: 'Harrogate' | K970: 'HG3 3AY' | L970: 'Open' | J971: 'Ripon' | K971: 'HG4 1LT' | L971: 'Open' | J972: 'Ripon' | K972: 'HG4 2ES' | L972: 'Open' | J973: 'York' | K973: 'YO51 9LY' | L973: 'Open' | J974: 'Ripon' | K974: 'HG4 3PJ' | L974: 'Open'

### `21865bab73e8|DUPLICATE_KEY|RS.Food!A381,RS.Food!A382`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!A381, RS.Food!A382`  severity: Medium  confidence: Review
- evidence: Normalized key 'mixed toast' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Mixed Toast'; row labels: []; column header: "'Mixed Pastries'"; used range: A1:W607
- neighbourhood: A379: 'Med Well' | B379: 0 | C379: 0 | A380: 'Mixed Pastries' | B380: 0 | C380: 0 | A381: 'Mixed Toast' | B381: 0 | C381: 0 | A382: 'Mixed Toast' | B382: 0 | C382: 0 | A383: 'Mushroom' | B383: 0 | C383: 0

### `ff0beb280ebe|DUPLICATE_KEY|Sheet1!G7,Sheet1!G9,Sheet1!G11,Sheet1!G13,Sheet1!G14`

- workbook: `all_data_912_v0.1/spreadsheet/59902/3_59902_input.xlsx`
- location: `Sheet1!G7, Sheet1!G9, Sheet1!G11, Sheet1!G13, Sheet1!G14`  severity: Medium  confidence: Review
- evidence: Normalized key 'donald' appears 9 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Donald'; row labels: ["'Bob'"]; column header: "'Jane'"; used range: A1:H28
- neighbourhood: F5: 2008-09-26 00:00:00 | G5: 'Donald' | H5: '=IFERROR(F5-INDEX($F6:$F28,MATCH(G5,$G6:$G28,0),1),"")' -> 5 | F6: 2008-09-26 00:00:00 | G6: 'Jane' | H6: '=IFERROR(F6-INDEX($F7:$F29,MATCH(G6,$G7:$G29,0),1),"")' -> 7 | F7: 2008-09-21 00:00:00 | G7: 'Donald' | H7: '=IFERROR(F7-INDEX($F8:$F30,MATCH(G7,$G8:$G30,0),1),"")' -> 1 | F8: 2008-09-21 00:00:00 | G8: 'Bob' | H8: '=IFERROR(F8-INDEX($F9:$F31,MATCH(G8,$G9:$G31,0),1),"")' -> 1 | F9: 2008-09-20 00:00:00 | G9: 'Donald' | H9: '=IFERROR(F9-INDEX($F10:$F32,MATCH(G9,$G10:$G32,0),1),"")' -> 1

### `852b58472b57|DUPLICATE_KEY|Sheet1!K2,Sheet1!K6,Sheet1!K10`

- workbook: `all_data_912_v0.1/spreadsheet/59185/1_59185_input.xlsx`
- location: `Sheet1!K2, Sheet1!K6, Sheet1!K10`  severity: Medium  confidence: Review
- evidence: Normalized key 'wbnb' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'WBNB'; row labels: ["'Pb floor sweep'", "'WBNB'"]; column header: ''; used range: A1:P24
- neighbourhood: J1: 'Date:' | I2: 'Pb floor sweep' | J2: 'WBNB' | K2: 'WBNB' | L2: 'BT' | I3: 2540 | J3: 1000 | K3: 4416 | L3: 1940 | L4: 'BT Splits'

### `f0d026f067a4|DUPLICATE_KEY|Sheet1!B6,Sheet1!B8`

- workbook: `all_data_912_v0.1/spreadsheet/59185/2_59185_input.xlsx`
- location: `Sheet1!B6, Sheet1!B8`  severity: Medium  confidence: Review
- evidence: Normalized key 'cbv splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'CBV Splits'; row labels: ["'WBNB Splits'"]; column header: ''; used range: A1:P22
- neighbourhood: D4: 'QC HOLD' | A6: 'WBNB Splits' | B6: 'CBV Splits' | C6: 'Pb Splits' | D6: 'CBV/WBNB mix' | A7: 2246 | B7: 198 | C7: 1904 | D7: 2948 | B8: 'CBV Splits' | D8: 'QC hold'

### `ff0beb280ebe|DUPLICATE_KEY|Sheet1!B9,Sheet1!B11,Sheet1!B15,Sheet1!B16,Sheet1!B18`

- workbook: `all_data_912_v0.1/spreadsheet/59902/3_59902_input.xlsx`
- location: `Sheet1!B9, Sheet1!B11, Sheet1!B15, Sheet1!B16, Sheet1!B18`  severity: Medium  confidence: Review
- evidence: Normalized key 'donald' appears 10 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Donald'; row labels: []; column header: "'Jane'"; used range: A1:H28
- neighbourhood: A7: 2008-08-30 00:00:00 | B7: 'Bob' | C7: '=A7-INDEX($A$4:$A6,MATCH(B7,$B$4:$B6,0),1)' -> 1 | A8: 2008-08-30 00:00:00 | B8: 'Jane' | C8: '=A8-INDEX($A$4:$A7,MATCH(B8,$B$4:$B7,0),1)' -> 1 | A9: 2008-08-31 00:00:00 | B9: 'Donald' | C9: '=A9-INDEX($A$4:$A8,MATCH(B9,$B$4:$B8,0),1)' -> '#N/A' | A10: 2008-08-31 00:00:00 | B10: 'Bob' | C10: '=A10-INDEX($A$4:$A9,MATCH(B10,$B$4:$B9,0),1)' -> 2 | A11: 2008-08-31 00:00:00 | B11: 'Donald' | C11: '=A11-INDEX($A$4:$A10,MATCH(B11,$B$4:$B10,0),1)' -> 0

### `b4c2169bf692|DUPLICATE_KEY|Sheet1!A2,Sheet1!A3,Sheet1!A4,Sheet1!A5`

- workbook: `all_data_912_v0.1/spreadsheet/49118/2_49118_input.xlsx`
- location: `Sheet1!A2, Sheet1!A3, Sheet1!A4, Sheet1!A5`  severity: Medium  confidence: Review
- evidence: Normalized key '44525aph235' appears 4 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '44525APH235'; row labels: []; column header: "'ID'"; used range: A1:D15
- neighbourhood: A1: 'ID' | B1: 'Min' | C1: 'Data' | A2: '44525APH235' | C2: 26.5 | A3: '44525APH235' | C3: 26.98 | A4: '44525APH235' | C4: 26.71

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A281,RS.Food!A282,RS.Food!A297`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A281, RS.Food!A282, RS.Food!A297`  severity: Medium  confidence: Review
- evidence: Normalized key 'anchovies' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Anchovies'; row labels: []; column header: "'Pineapple'"; used range: A1:W607
- neighbourhood: A279: 'Peppers' | B279: 10.5 | C279: 6.73248256126719e-05 | A280: 'Pineapple' | B280: 10.5 | C280: 6.73248256126719e-05 | A281: 'Anchovies' | B281: 7 | C281: 4.48832170751146e-05 | A282: 'Anchovies' | B282: 3.5 | C282: 2.24416085375573e-05 | A283: '------------' | B283: 0 | C283: 0

### `f367b87c90dd|DUPLICATE_KEY|Sheet1!J2,Sheet1!J6,Sheet1!J10`

- workbook: `all_data_912_v0.1/spreadsheet/59185/3_59185_input.xlsx`
- location: `Sheet1!J2, Sheet1!J6, Sheet1!J10`  severity: Medium  confidence: Review
- evidence: Normalized key 'wbnb' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'WBNB'; row labels: ["'KBD rerun'", "'Pb floor sweep'"]; column header: "'Date:'"; used range: A1:P22
- neighbourhood: J1: 'Date:' | H2: 'KBD rerun' | I2: 'Pb floor sweep' | J2: 'WBNB' | K2: 'WBNB' | L2: 'BT' | H3: 772 | I3: 2540 | J3: 10 | K3: 10 | L3: 1940 | L4: 'BT Splits'

### `e499130decde|DUPLICATE_KEY|Attendance!D5,Attendance!D6,Attendance!D7,Attendance!D8`

- workbook: `all_data_912_v0.1/spreadsheet/51313/3_51313_input.xlsx`
- location: `Attendance!D5, Attendance!D6, Attendance!D7, Attendance!D8`  severity: Medium  confidence: Review
- evidence: Normalized key 'p' appears 4 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'p'; row labels: ["'Moe'"]; column header: "'a'"; used range: A1:F8
- neighbourhood: B3: '=COUNTIF(D3:F3,"P")' -> 0 | C3: '=COUNTIF(D3:F3,"A")' -> 1 | D3: 'a' | B4: '=COUNTIF(D4:F4,"P")' -> 0 | C4: '=COUNTIF(D4:F4,"A")' -> 1 | D4: 'a' | B5: '=COUNTIF(D5:F5,"P")' -> 1 | C5: '=COUNTIF(D5:F5,"A")' -> 0 | D5: 'p' | B6: '=COUNTIF(D6:F6,"P")' -> 1 | C6: '=COUNTIF(D6:F6,"A")' -> 0 | D6: 'p' | B7: '=COUNTIF(D7:F7,"P")' -> 1 | C7: '=COUNTIF(D7:F7,"A")' -> 0 | D7: 'p'

### `a4becd1e83e9|DUPLICATE_KEY|Sheet1!A13,Sheet1!A25`

- workbook: `all_data_912_v0.1/spreadsheet/48799/3_48799_input.xlsx`
- location: `Sheet1!A13, Sheet1!A25`  severity: Medium  confidence: Review
- evidence: Normalized key 'l' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'L'; row labels: []; column header: "'K'"; used range: A1:D25
- neighbourhood: A11: 'J' | B11: 8.86 | C11: 5.97 | A12: 'K' | B12: 20.54 | C12: 9.0042 | A13: 'L' | B13: 9.54 | C13: 5.5044 | A14: 'M' | B14: 7.56 | C14: 5.091 | A15: 'N' | B15: 14.61 | C15: 7.1142

### `3db55cfd98cc|DUPLICATE_KEY|Sheet2!B9,Sheet2!B18`

- workbook: `all_data_912_v0.1/spreadsheet/52216/3_52216_input.xlsx`
- location: `Sheet2!B9, Sheet2!B18`  severity: Medium  confidence: Review
- evidence: Normalized key 'r&m' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'R&M'; row labels: ["'Regional'"]; column header: "'Rates'"; used range: A1:G20
- neighbourhood: A7: 'Regional' | B7: 'Printing & Postage' | A8: 'Regional' | B8: 'Rates' | A9: 'Regional' | B9: 'R&M' | A10: 'Regional' | B10: 'Salaries & Wages' | A11: 'Regional' | B11: 'Telco'

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A381,RS.Food!A382`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A381, RS.Food!A382`  severity: Medium  confidence: Review
- evidence: Normalized key 'mixed toast' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Mixed Toast'; row labels: []; column header: "'Mixed Pastries'"; used range: A1:W607
- neighbourhood: A379: 'Med Well' | B379: 0 | C379: 0 | A380: 'Mixed Pastries' | B380: 0 | C380: 0 | A381: 'Mixed Toast' | B381: 0 | C381: 0 | A382: 'Mixed Toast' | B382: 0 | C382: 0 | A383: 'Mushroom' | B383: 0 | C383: 0

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A307,RS.Food!A308,RS.Food!A309`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A307, RS.Food!A308, RS.Food!A309`  severity: Medium  confidence: Review
- evidence: Normalized key 'banana' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Banana'; row labels: []; column header: "'Baked Beans'"; used range: A1:W607
- neighbourhood: A305: 'Bacon Crispy' | B305: 0 | C305: 0 | A306: 'Baked Beans' | B306: 0 | C306: 0 | A307: 'Banana' | B307: 0 | C307: 0 | A308: 'Banana' | B308: 0 | C308: 0 | A309: 'Banana' | B309: 0 | C309: 0

### `10ace2be6dbc|DUPLICATE_KEY|Sheet1!G8,Sheet1!G10,Sheet1!G16,Sheet1!G20,Sheet1!G22`

- workbook: `all_data_912_v0.1/spreadsheet/59902/1_59902_input.xlsx`
- location: `Sheet1!G8, Sheet1!G10, Sheet1!G16, Sheet1!G20, Sheet1!G22`  severity: Medium  confidence: Review
- evidence: Normalized key 'bob' appears 7 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Bob'; row labels: ["'Jane'"]; column header: "'Donald'"; used range: A1:H28
- neighbourhood: F6: 2008-09-26 00:00:00 | G6: 'Jane' | H6: '=IFERROR(F6-INDEX($F7:$F29,MATCH(G6,$G7:$G29,0),1),"")' -> 7 | F7: 2008-09-21 00:00:00 | G7: 'Donald' | H7: '=IFERROR(F7-INDEX($F8:$F30,MATCH(G7,$G8:$G30,0),1),"")' -> 1 | F8: 2008-09-21 00:00:00 | G8: 'Bob' | H8: '=IFERROR(F8-INDEX($F9:$F31,MATCH(G8,$G9:$G31,0),1),"")' -> 1 | F9: 2008-09-20 00:00:00 | G9: 'Donald' | H9: '=IFERROR(F9-INDEX($F10:$F32,MATCH(G9,$G10:$G32,0),1),"")' -> 1 | F10: 2008-09-20 00:00:00 | G10: 'Bob' | H10: '=IFERROR(F10-INDEX($F11:$F33,MATCH(G10,$G11:$G33,0),1),"")' -> 6

### `d49eeac3b8af|DUPLICATE_KEY|Sheet1!G7,Sheet1!G9,Sheet1!G11,Sheet1!G13,Sheet1!G14`

- workbook: `all_data_912_v0.1/spreadsheet/59902/2_59902_input.xlsx`
- location: `Sheet1!G7, Sheet1!G9, Sheet1!G11, Sheet1!G13, Sheet1!G14`  severity: Medium  confidence: Review
- evidence: Normalized key 'donald' appears 9 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Donald'; row labels: ["'Bob'"]; column header: "'Jane'"; used range: A1:H28
- neighbourhood: F5: 2008-09-26 00:00:00 | G5: 'Donald' | H5: '=IFERROR(F5-INDEX($F6:$F28,MATCH(G5,$G6:$G28,0),1),"")' -> 5 | F6: 2008-09-26 00:00:00 | G6: 'Jane' | H6: '=IFERROR(F6-INDEX($F7:$F29,MATCH(G6,$G7:$G29,0),1),"")' -> 7 | F7: 2008-09-21 00:00:00 | G7: 'Donald' | H7: '=IFERROR(F7-INDEX($F8:$F30,MATCH(G7,$G8:$G30,0),1),"")' -> 1 | F8: 2008-09-21 00:00:00 | G8: 'Bob' | H8: '=IFERROR(F8-INDEX($F9:$F31,MATCH(G8,$G9:$G31,0),1),"")' -> 1 | F9: 2008-09-20 00:00:00 | G9: 'Donald' | H9: '=IFERROR(F9-INDEX($F10:$F32,MATCH(G9,$G10:$G32,0),1),"")' -> 1

## FORMULA_DRIFT

### `81b42e5e2d2e|FORMULA_DRIFT|Total!A23`

- workbook: `all_data_912_v0.1/spreadsheet/11842/2_11842_input.xlsx`
- location: `Total!A23`  severity: High  confidence: Likely defect
- formula: `=Jan!A42`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[19]C[31]+FEB!R[19]C[31]+MAR!R[19]C[31]+APR!R[19]C[31]+MAY!R[19]C[31]+JUN!R[19]C[31]+JUL!R[19]C[31]+AUG!R[19]C[31]+SEP!R[19]C[31]+OCT!R[19]C[31]+NOV!R[19]C[31]+DEC!R[19]C[31]+JAN!R[20]C[31]+FEB!R[20]C[31]+MAR!R[20]C[31]+APR!R[20]C[31]+MAY!R[20]C[31]+JUN!R[20]C[31]+JUL!R[20]C[31]+AUG!R[20]C[31]+SEP!R[20]C[31]+OCT!R[20]C[31]+NOV!R[20]C[31]+DEC!R[20]C[31])/2
- evidence: This cell: =JAN!R[19]C
- cached value: 0; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A21: '=Jan!A38' -> 0 | B21: '=(Jan!AG38+Feb!AG38+Mar!AG38+Apr!AG38+May!AG38+Jun!AG38+Jul!AG38+A... -> 0 | C21: '=(Jan!AH38+Feb!AH38+Mar!AH38+Apr!AH38+May!AH38+Jun!AH38+Jul!AH38+A... -> 0 | A22: '=Jan!A40' -> 0 | B22: '=(Jan!AG40+Feb!AG40+Mar!AG40+Apr!AG40+May!AG40+Jun!AG40+Jul!AG40+A... -> 0 | C22: '=(Jan!AH40+Feb!AH40+Mar!AH40+Apr!AH40+May!AH40+Jun!AH40+Jul!AH40+A... -> 0 | A23: '=Jan!A42' -> 0 | B23: '=(Jan!AG42+Feb!AG42+Mar!AG42+Apr!AG42+May!AG42+Jun!AG42+Jul!AG42+A... -> 0 | C23: '=(Jan!AH42+Feb!AH42+Mar!AH42+Apr!AH42+May!AH42+Jun!AH42+Jul!AH42+A... -> 0 | A24: '=Jan!A44' -> 0 | B24: '=(Jan!AG44+Feb!AG44+Mar!AG44+Apr!AG44+May!AG44+Jun!AG44+Jul!AG44+A... -> 0 | C24: '=(Jan!AH44+Feb!AH44+Mar!AH44+Apr!AH44+May!AH44+Jun!AH44+Jul!AH44+A... -> 0 | A25: '=Jan!A46' -> 0 | B25: '=(Jan!AG46+Feb!AG46+Mar!AG46+Apr!AG46+May!AG46+Jun!AG46+Jul!AG46+A... -> 0 | C25: '=(Jan!AH46+Feb!AH46+Mar!AH46+Apr!AH46+May!AH46+Jun!AH46+Jul!AH46+A... -> 0

### `7deacb0c30f0|FORMULA_DRIFT|Sheet1!C7`

- workbook: `all_data_912_v0.1/spreadsheet/183-8/1_183-8_input.xlsx`
- location: `Sheet1!C7`  severity: High  confidence: Likely defect
- formula: `=SUM(C3:C6)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AVERAGE(R[-4]C:R[-1]C)
- evidence: This cell: =SUM(R[-4]C:R[-1]C)
- cached value: 1176448932; row labels: []; column header: ''; used range: A1:N43
- range C3:C6: values ['271486433', '263336524', '310016060', '331609915']; beyond: {'above': 'C2: None', 'below': "C7: '=SUM(C3:C6)'"}
- neighbourhood: B5: '2019-2020' | C5: 310016060 | D5: 20.32 | E5: 97.16 | B6: '2018-2019' | C6: 331609915 | D6: 21.93 | E6: 98.31 | C7: '=SUM(C3:C6)' -> 1176448932 | D7: '=AVERAGE(D3:D6)' -> 19.51 | E7: '=AVERAGE(E3:E6)' -> 97.1125 | A9: 'b' | B9: '2021-2022' | C9: 3989840 | D9: 15.18 | E9: 67.55

### `81b42e5e2d2e|FORMULA_DRIFT|Total!A16`

- workbook: `all_data_912_v0.1/spreadsheet/11842/2_11842_input.xlsx`
- location: `Total!A16`  severity: High  confidence: Likely defect
- formula: `=Jan!A28`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[12]C[31]+FEB!R[12]C[31]+MAR!R[12]C[31]+APR!R[12]C[31]+MAY!R[12]C[31]+JUN!R[12]C[31]+JUL!R[12]C[31]+AUG!R[12]C[31]+SEP!R[12]C[31]+OCT!R[12]C[31]+NOV!R[12]C[31]+DEC!R[12]C[31]+JAN!R[13]C[31]+FEB!R[13]C[31]+MAR!R[13]C[31]+APR!R[13]C[31]+MAY!R[13]C[31]+JUN!R[13]C[31]+JUL!R[13]C[31]+AUG!R[13]C[31]+SEP!R[13]C[31]+OCT!R[13]C[31]+NOV!R[13]C[31]+DEC!R[13]C[31])/2
- evidence: This cell: =JAN!R[12]C
- cached value: 0; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A14: '=Jan!A24' -> 'RESHMA KHOLKAR' | B14: '=(Jan!AG24+Feb!AG24+Mar!AG24+Apr!AG24+May!AG24+Jun!AG24+Jul!AG24+A... -> 0 | C14: '=(Jan!AH24+Feb!AH24+Mar!AH24+Apr!AH24+May!AH24+Jun!AH24+Jul!AH24+A... -> 0 | A15: '=Jan!A26' -> 0 | B15: '=(Jan!AG26+Feb!AG26+Mar!AG26+Apr!AG26+May!AG26+Jun!AG26+Jul!AG26+A... -> 0 | C15: '=(Jan!AH26+Feb!AH26+Mar!AH26+Apr!AH26+May!AH26+Jun!AH26+Jul!AH26+A... -> 0 | A16: '=Jan!A28' -> 0 | B16: '=(Jan!AG28+Feb!AG28+Mar!AG28+Apr!AG28+May!AG28+Jun!AG28+Jul!AG28+A... -> 0 | C16: '=(Jan!AH28+Feb!AH28+Mar!AH28+Apr!AH28+May!AH28+Jun!AH28+Jul!AH28+A... -> 0 | A17: '=Jan!A30' -> 0 | B17: '=(Jan!AG30+Feb!AG30+Mar!AG30+Apr!AG30+May!AG30+Jun!AG30+Jul!AG30+A... -> 0 | C17: '=(Jan!AH30+Feb!AH30+Mar!AH30+Apr!AH30+May!AH30+Jun!AH30+Jul!AH30+A... -> 0 | A18: '=Jan!A32' -> 0 | B18: '=(Jan!AG32+Feb!AG32+Mar!AG32+Apr!AG32+May!AG32+Jun!AG32+Jul!AG32+A... -> 0 | C18: '=(Jan!AH32+Feb!AH32+Mar!AH32+Apr!AH32+May!AH32+Jun!AH32+Jul!AH32+A... -> 0

### `47eb61dd533e|FORMULA_DRIFT|TEST!R7`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!R7`  severity: High  confidence: Likely defect
- formula: `=P7-Q7`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=146): =RC[-3]+RC[-5]-RC[-1]
- evidence: This cell: =RC[-2]-RC[-1]
- cached value: 3014.35; row labels: ["'Starting Balance'", "'W'"]; column header: "'Balance'"; used range: A1:S1004
- neighbourhood: P6: 30000 | Q6: 'Withdrawal' | R6: 'Balance' | P7: '=O7+M7' -> 3014.35 | Q7: '=IF((M7+O7)>$P$6,$P$1,0)' -> 0 | R7: '=P7-Q7' -> 3014.35 | S7: '=SUM(Q7:Q13)' -> 0 | P8: '=O8+M8' -> 4821.71 | Q8: '=IF((M8+O8)>$P$6,$P$1,0)' -> 0 | R8: '=O8+M8-Q8' -> 4821.71 | P9: '=O9+M9' -> 7350 | Q9: '=IF((M9+O9)>$P$6,$P$1,0)' -> 0 | R9: '=O9+M9-Q9' -> 7350

### `470111f62d4c|FORMULA_DRIFT|Total!A7`

- workbook: `all_data_912_v0.1/spreadsheet/11842/1_11842_input.xlsx`
- location: `Total!A7`  severity: High  confidence: Likely defect
- formula: `=Jan!A10`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[3]C[31]+FEB!R[3]C[31]+MAR!R[3]C[31]+APR!R[3]C[31]+MAY!R[3]C[31]+JUN!R[3]C[31]+JUL!R[3]C[31]+AUG!R[3]C[31]+SEP!R[3]C[31]+OCT!R[3]C[31]+NOV!R[3]C[31]+DEC!R[3]C[31]+JAN!R[4]C[31]+FEB!R[4]C[31]+MAR!R[4]C[31]+APR!R[4]C[31]+MAY!R[4]C[31]+JUN!R[4]C[31]+JUL!R[4]C[31]+AUG!R[4]C[31]+SEP!R[4]C[31]+OCT!R[4]C[31]+NOV!R[4]C[31]+DEC!R[4]C[31])/2
- evidence: This cell: =JAN!R[3]C
- cached value: 'SHATRUDHAN MAHATO'; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A5: '=Jan!A6' -> 'PETER NORONHA' | B5: '=(Jan!AG6+Feb!AG6+Mar!AG6+Apr!AG6+May!AG6+Jun!AG6+Jul!AG6+Aug!AG6+... -> 2 | C5: '=(Jan!AH6+Feb!AH6+Mar!AH6+Apr!AH6+May!AH6+Jun!AH6+Jul!AH6+Aug!AH6+... -> 0 | A6: '=Jan!A8' -> 'SHYAMBALI PAL' | B6: '=(Jan!AG8+Feb!AG8+Mar!AG8+Apr!AG8+May!AG8+Jun!AG8+Jul!AG8+Aug!AG8+... -> 1 | C6: '=(Jan!AH8+Feb!AH8+Mar!AH8+Apr!AH8+May!AH8+Jun!AH8+Jul!AH8+Aug!AH8+... -> 0 | A7: '=Jan!A10' -> 'SHATRUDHAN MAHATO' | B7: '=(Jan!AG10+Feb!AG10+Mar!AG10+Apr!AG10+May!AG10+Jun!AG10+Jul!AG10+A... -> 0 | C7: '=(Jan!AH10+Feb!AH10+Mar!AH10+Apr!AH10+May!AH10+Jun!AH10+Jul!AH10+A... -> 0 | A8: '=Jan!A12' -> 'RAVINDRA V. GOVEKAR' | B8: '=(Jan!AG12+Feb!AG12+Mar!AG12+Apr!AG12+May!AG12+Jun!AG12+Jul!AG12+A... -> 0 | C8: '=(Jan!AH12+Feb!AH12+Mar!AH12+Apr!AH12+May!AH12+Jun!AH12+Jul!AH12+A... -> 0 | A9: '=Jan!A14' -> 'DEEPAK WARPE' | B9: '=(Jan!AG14+Feb!AG14+Mar!AG14+Apr!AG14+May!AG14+Jun!AG14+Jul!AG14+A... -> 0 | C9: '=(Jan!AH14+Feb!AH14+Mar!AH14+Apr!AH14+May!AH14+Jun!AH14+Jul!AH14+A... -> 0

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

### `d01aaa205624|FORMULA_DRIFT|MoneyInCheckingNextMonth!L2`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/1_CF_22493_input.xlsx`
- location: `Money In Checking Next Month!L2`  severity: High  confidence: Likely defect
- formula: `=M14`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =SUM(R[2]C:R[9]C)
- evidence: This cell: =R[12]C[1]
- cached value: 0; row labels: ["'18th'", "'Automatically Paid'"]; column header: "'Total Tax'"; used range: A1:BJ103
- neighbourhood: K1: 'Legend' | L1: 'Total Tax' | M1: 'Monthly Income' | N1: 'Total Income' | K2: 'Automatically Paid' | L2: '=M14' -> 0 | M2: '=SUM(M4:M11)' -> 8128.84 | N2: '=SUM(N4:N11)' -> 0 | K3: "Same Am't Monthly" | K4: 'Varies By Month' | L4: 'Larry RRB' | M4: 3546.86 | N4: '=SUM(O4:Z4)' -> 0

### `470111f62d4c|FORMULA_DRIFT|Total!A5`

- workbook: `all_data_912_v0.1/spreadsheet/11842/1_11842_input.xlsx`
- location: `Total!A5`  severity: High  confidence: Likely defect
- formula: `=Jan!A6`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[1]C[31]+FEB!R[1]C[31]+MAR!R[1]C[31]+APR!R[1]C[31]+MAY!R[1]C[31]+JUN!R[1]C[31]+JUL!R[1]C[31]+AUG!R[1]C[31]+SEP!R[1]C[31]+OCT!R[1]C[31]+NOV!R[1]C[31]+DEC!R[1]C[31]+JAN!R[2]C[31]+FEB!R[2]C[31]+MAR!R[2]C[31]+APR!R[2]C[31]+MAY!R[2]C[31]+JUN!R[2]C[31]+JUL!R[2]C[31]+AUG!R[2]C[31]+SEP!R[2]C[31]+OCT!R[2]C[31]+NOV!R[2]C[31]+DEC!R[2]C[31])/2
- evidence: This cell: =JAN!R[1]C
- cached value: 'PETER NORONHA'; row labels: []; column header: "'NAME'"; used range: A1:Z26
- neighbourhood: A4: 'NAME' | B4: 'P' | C4: 'ODK' | A5: '=Jan!A6' -> 'PETER NORONHA' | B5: '=(Jan!AG6+Feb!AG6+Mar!AG6+Apr!AG6+May!AG6+Jun!AG6+Jul!AG6+Aug!AG6+... -> 2 | C5: '=(Jan!AH6+Feb!AH6+Mar!AH6+Apr!AH6+May!AH6+Jun!AH6+Jul!AH6+Aug!AH6+... -> 0 | A6: '=Jan!A8' -> 'SHYAMBALI PAL' | B6: '=(Jan!AG8+Feb!AG8+Mar!AG8+Apr!AG8+May!AG8+Jun!AG8+Jul!AG8+Aug!AG8+... -> 1 | C6: '=(Jan!AH8+Feb!AH8+Mar!AH8+Apr!AH8+May!AH8+Jun!AH8+Jul!AH8+Aug!AH8+... -> 0 | A7: '=Jan!A10' -> 'SHATRUDHAN MAHATO' | B7: '=(Jan!AG10+Feb!AG10+Mar!AG10+Apr!AG10+May!AG10+Jun!AG10+Jul!AG10+A... -> 0 | C7: '=(Jan!AH10+Feb!AH10+Mar!AH10+Apr!AH10+May!AH10+Jun!AH10+Jul!AH10+A... -> 0

### `902b5e29897a|FORMULA_DRIFT|LeadTimes!B6`

- workbook: `all_data_912_v0.1/spreadsheet/47741/1_47741_input.xlsx`
- location: `Lead Times!B6`  severity: High  confidence: Likely defect
- formula: `=WORKDAY(B4,18,K14:K21)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =WORKDAY(R[-2]C,18,R[9]C[9]:R[15]C[9])
- evidence: This cell: =WORKDAY(R[-2]C,18,R[8]C[9]:R[15]C[9])
- cached value: 2022-01-21 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range K14:K21: values ['2021-12-31 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None']; beyond: {'above': 'K13: None', 'below': 'K22: None'}
- neighbourhood: B4: '=INDEX(calendar,ndx+0) {array B4:H4}' -> 2021-12-27 00:00:00 | C4: 2021-12-28 00:00:00 | D4: 2021-12-29 00:00:00 | B5: '=_xlfn.TEXTJOIN("-",,WORKDAY(B4,10,K14:K20),WORKDAY(B4,12,K14:K20))' -> '44572-44574' | C5: '=WORKDAY(C4,10,L14:L20)' -> 2022-01-12 00:00:00 | D5: '=WORKDAY(D4,10,M14:M20)' -> 2022-01-13 00:00:00 | B6: '=WORKDAY(B4,18,K14:K21)' -> 2022-01-21 00:00:00 | C6: '=WORKDAY(C4,18,L15:L21)' -> 2022-01-21 00:00:00 | D6: '=WORKDAY(D4,18,M15:M21)' -> 2022-01-24 00:00:00 | B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22' | B8: '=INDEX(calendar,ndx+1) {array B8:H8}' -> 2022-01-03 00:00:00 | C8: 2022-01-04 00:00:00 | D8: 2022-01-05 00:00:00

### `0574dfb01ae0|FORMULA_DRIFT|Summary!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17111/3_17111_input.xlsx`
- location: `Summary!B2`  severity: High  confidence: Likely defect
- formula: `=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary!$B$1)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=4): =SUMIFS(SHEET1!C[2]:C[2],SHEET1!C:C,SUMMARY!RC[-1],SHEET1!C[1]:C[1],SUMMARY!R1C2)
- evidence: This cell: =SUMIFS(SHEET1!C4:C4,SHEET1!C2:C2,SUMMARY!RC1,SHEET1!C3:C3,SUMMARY!R1C2)
- cached value: 200; row labels: ["'neha'"]; column header: "'HD'"; used range: A1:F9
- neighbourhood: A1: 'Name' | B1: 'HD' | C1: 'SD' | A2: 'neha' | B2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 200 | C2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 698 | A3: 'rahul' | B3: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A3,Sheet1!C:C,Summary!$B$1)' -> 1126 | C3: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A3,Sheet1!$C:$C,Summary... -> 131 | A4: 'mohit' | B4: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A4,Sheet1!C:C,Summary!$B$1)' -> 954 | C4: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A4,Sheet1!$C:$C,Summary... -> 586

### `589c38846e3c|FORMULA_DRIFT|Total!A11`

- workbook: `all_data_912_v0.1/spreadsheet/11842/3_11842_input.xlsx`
- location: `Total!A11`  severity: High  confidence: Likely defect
- formula: `=Jan!A18`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[7]C[31]+FEB!R[7]C[31]+MAR!R[7]C[31]+APR!R[7]C[31]+MAY!R[7]C[31]+JUN!R[7]C[31]+JUL!R[7]C[31]+AUG!R[7]C[31]+SEP!R[7]C[31]+OCT!R[7]C[31]+NOV!R[7]C[31]+DEC!R[7]C[31]+JAN!R[8]C[31]+FEB!R[8]C[31]+MAR!R[8]C[31]+APR!R[8]C[31]+MAY!R[8]C[31]+JUN!R[8]C[31]+JUL!R[8]C[31]+AUG!R[8]C[31]+SEP!R[8]C[31]+OCT!R[8]C[31]+NOV!R[8]C[31]+DEC!R[8]C[31])/2
- evidence: This cell: =JAN!R[7]C
- cached value: 'JOEL FERNANDES'; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A9: '=Jan!A14' -> 'DEEPAK WARPE' | B9: '=(Jan!AG14+Feb!AG14+Mar!AG14+Apr!AG14+May!AG14+Jun!AG14+Jul!AG14+A... -> 0 | C9: '=(Jan!AH14+Feb!AH14+Mar!AH14+Apr!AH14+May!AH14+Jun!AH14+Jul!AH14+A... -> 0 | A10: '=Jan!A16' -> 'RAVINDRA G. GOVEKAR' | B10: '=(Jan!AG16+Feb!AG16+Mar!AG16+Apr!AG16+May!AG16+Jun!AG16+Jul!AG16+A... -> 0 | C10: '=(Jan!AH16+Feb!AH16+Mar!AH16+Apr!AH16+May!AH16+Jun!AH16+Jul!AH16+A... -> 0 | A11: '=Jan!A18' -> 'JOEL FERNANDES' | B11: '=(Jan!AG18+Feb!AG18+Mar!AG18+Apr!AG18+May!AG18+Jun!AG18+Jul!AG18+A... -> 0 | C11: '=(Jan!AH18+Feb!AH18+Mar!AH18+Apr!AH18+May!AH18+Jun!AH18+Jul!AH18+A... -> 0 | A12: '=Jan!A20' -> 'RUZAR VAZ' | B12: '=(Jan!AG20+Feb!AG20+Mar!AG20+Apr!AG20+May!AG20+Jun!AG20+Jul!AG20+A... -> 0 | C12: '=(Jan!AH20+Feb!AH20+Mar!AH20+Apr!AH20+May!AH20+Jun!AH20+Jul!AH20+A... -> 0 | A13: '=Jan!A22' -> 'DHARMENDRA KUMAR' | B13: '=(Jan!AG22+Feb!AG22+Mar!AG22+Apr!AG22+May!AG22+Jun!AG22+Jul!AG22+A... -> 0 | C13: '=(Jan!AH22+Feb!AH22+Mar!AH22+Apr!AH22+May!AH22+Jun!AH22+Jul!AH22+A... -> 0

### `589c38846e3c|FORMULA_DRIFT|Total!A12`

- workbook: `all_data_912_v0.1/spreadsheet/11842/3_11842_input.xlsx`
- location: `Total!A12`  severity: High  confidence: Likely defect
- formula: `=Jan!A20`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[8]C[31]+FEB!R[8]C[31]+MAR!R[8]C[31]+APR!R[8]C[31]+MAY!R[8]C[31]+JUN!R[8]C[31]+JUL!R[8]C[31]+AUG!R[8]C[31]+SEP!R[8]C[31]+OCT!R[8]C[31]+NOV!R[8]C[31]+DEC!R[8]C[31]+JAN!R[9]C[31]+FEB!R[9]C[31]+MAR!R[9]C[31]+APR!R[9]C[31]+MAY!R[9]C[31]+JUN!R[9]C[31]+JUL!R[9]C[31]+AUG!R[9]C[31]+SEP!R[9]C[31]+OCT!R[9]C[31]+NOV!R[9]C[31]+DEC!R[9]C[31])/2
- evidence: This cell: =JAN!R[8]C
- cached value: 'RUZAR VAZ'; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A10: '=Jan!A16' -> 'RAVINDRA G. GOVEKAR' | B10: '=(Jan!AG16+Feb!AG16+Mar!AG16+Apr!AG16+May!AG16+Jun!AG16+Jul!AG16+A... -> 0 | C10: '=(Jan!AH16+Feb!AH16+Mar!AH16+Apr!AH16+May!AH16+Jun!AH16+Jul!AH16+A... -> 0 | A11: '=Jan!A18' -> 'JOEL FERNANDES' | B11: '=(Jan!AG18+Feb!AG18+Mar!AG18+Apr!AG18+May!AG18+Jun!AG18+Jul!AG18+A... -> 0 | C11: '=(Jan!AH18+Feb!AH18+Mar!AH18+Apr!AH18+May!AH18+Jun!AH18+Jul!AH18+A... -> 0 | A12: '=Jan!A20' -> 'RUZAR VAZ' | B12: '=(Jan!AG20+Feb!AG20+Mar!AG20+Apr!AG20+May!AG20+Jun!AG20+Jul!AG20+A... -> 0 | C12: '=(Jan!AH20+Feb!AH20+Mar!AH20+Apr!AH20+May!AH20+Jun!AH20+Jul!AH20+A... -> 0 | A13: '=Jan!A22' -> 'DHARMENDRA KUMAR' | B13: '=(Jan!AG22+Feb!AG22+Mar!AG22+Apr!AG22+May!AG22+Jun!AG22+Jul!AG22+A... -> 0 | C13: '=(Jan!AH22+Feb!AH22+Mar!AH22+Apr!AH22+May!AH22+Jun!AH22+Jul!AH22+A... -> 0 | A14: '=Jan!A24' -> 'RESHMA KHOLKAR' | B14: '=(Jan!AG24+Feb!AG24+Mar!AG24+Apr!AG24+May!AG24+Jun!AG24+Jul!AG24+A... -> 0 | C14: '=(Jan!AH24+Feb!AH24+Mar!AH24+Apr!AH24+May!AH24+Jun!AH24+Jul!AH24+A... -> 0

### `28278a05f541|FORMULA_DRIFT|Sheet1!K7`

- workbook: `all_data_912_v0.1/spreadsheet/32255/2_32255_input.xlsx`
- location: `Sheet1!K7`  severity: High  confidence: Likely defect
- formula: `=SUM(K4:K5)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =SUM(R[-3]C:R[-1]C)
- evidence: This cell: =SUM(R[-3]C:R[-2]C)
- cached value: 100.00000000000001; row labels: ["'Total'"]; column header: ''; used range: A1:K13
- range K4:K5: values ['16.666666666666668', '83.33333333333334']; beyond: {'above': "K3: '% Total Less BE'", 'below': 'K6: None'}
- neighbourhood: I5: '=SUM(B2:B30000)' -> 5 | J5: '=SUM(I5/I7%)' -> 41.66666666666667 | K5: '=SUM(I5/I8%)' -> 83.33333333333334 | I6: '=SUM(D2:D30000)' -> 6 | J6: '=SUM(I6/I7%)' -> 50 | I7: '=SUM(I4:I6)' -> 12 | J7: '=SUM(J4:J6)' -> 100 | K7: '=SUM(K4:K5)' -> 100.00000000000001 | I8: '=SUM(I4:I5)' -> 6

### `0c0e0e5f0156|FORMULA_DRIFT|Sheet1!F7`

- workbook: `all_data_912_v0.1/spreadsheet/49237/2_49237_input.xlsx`
- location: `Sheet1!F7`  severity: High  confidence: Likely defect
- formula: `=LEFT(F10)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =PROPER(R[-1]C[-1])
- evidence: This cell: =LEFT(R[3]C)
- cached value: None; row labels: ["'AEW Date (Use DOC)'"]; column header: ''; used range: A1:L27
- neighbourhood: E5: '=LEFT(E19,FIND(" ",E19)-1)' -> 'Joe' | E6: '=LEFT(MID(E9,1,1)&MID(E9,2,1)&MID(E9,3,1)&MID(E9,4,1),2*LEN(E9))' -> 'Geor' | F6: '=PROPER(E5)' -> 'Joe' | G6: 'Reopen AEW' | E7: '=RIGHT(E19,LEN(E19)-FIND("*",SUBSTITUTE(E19," ","*",LEN(E19)-LEN(S... -> 'Veteran' | F7: '=LEFT(F10)' -> None | F8: '=PROPER(E7)' -> 'Veteran' | G8: '21-22, 214' | E9: '=TRIM(MID(E19,LEN(E5)+1,LEN(E19)-LEN(E5&E7)))' -> 'George'

### `d3575a4dff7b|FORMULA_DRIFT|MoneyInCheckingNextMonth!E61`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/2_CF_22493_input.xlsx`
- location: `Money In Checking Next Month!E61`  severity: High  confidence: Likely defect
- formula: `=C60-E60`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=14): =IF(HOUSE BUDGET!R[63]C[1]="","",HOUSE BUDGET!R[63]C[1])
- evidence: This cell: =R[-1]C[-2]-R[-1]C
- cached value: 2681.2300000000005; row labels: ["'Total Left'", "'Total Left'"]; column header: ''; used range: A1:BJ103
- neighbourhood: C59: 522 | E59: '=IF(\'House Budget\'!F122="","",\'House Budget\'!F122)' -> 0 | C60: '=SUM(C2:C59)' -> 6406.9400000000005 | D60: 'Total Bills' | E60: '=SUM(E2:E59)' -> 3725.71 | C61: '=C103-C60' -> -6406.9400000000005 | D61: 'Total Left' | E61: '=C60-E60' -> 2681.2300000000005

### `7c3edf13b7c6|FORMULA_DRIFT|Malaga!O22`

- workbook: `all_data_912_v0.1/spreadsheet/40809/2_40809_input.xlsx`
- location: `Malaga!O22`  severity: High  confidence: Likely defect
- formula: `=IF(C19="","",C19)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =IF(R[-3]C[-11]="","",R[-3]C[-11])
- evidence: This cell: =IF(R[-3]C[-12]="","",R[-3]C[-12])
- cached value: 'MARVESLEY (Pamela)*'; row labels: []; column header: ''; used range: A1:AJ57
- neighbourhood: O20: '=IF(C17="","",C17)' -> 'LOOM (Scott)' | P20: '=IF(E17="","",E17)' -> 0 | Q20: '=IF(F17="","",F17)' -> 1044 | O21: '=IF(C18="","",C18)' -> 'MARVESLEY (John)' | P21: '=IF(E18="","",E18)' -> 36 | Q21: '=IF(F18="","",F18)' -> 763 | O22: '=IF(C19="","",C19)' -> 'MARVESLEY (Pamela)*' | P22: '=IF(E19="","",E19)' -> 35 | Q22: '=IF(F19="","",F19)' -> 414 | O23: '=IF(J9="","",J9)' -> 'MITCHELL (Alan)' | P23: '=IF(L9="","",L9)' -> 0 | Q23: '=IF(M9="","",M9)' -> 799 | O24: '=IF(J10="","",J10)' -> 'PEARCE (Steve)' | P24: '=IF(L10="","",L10)' -> 0 | Q24: '=IF(M10="","",M10)' -> 799

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

### `6d26dcd54bfa|FORMULA_DRIFT|Sheet1!C43`

- workbook: `all_data_912_v0.1/spreadsheet/183-8/2_183-8_input.xlsx`
- location: `Sheet1!C43`  severity: High  confidence: Likely defect
- formula: `=SUM(C39:C42)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AVERAGE(R[-4]C:R[-1]C)
- evidence: This cell: =SUM(R[-4]C:R[-1]C)
- cached value: 1058517622; row labels: []; column header: ''; used range: A1:N43
- range C39:C42: values ['230800173', '228343263', '302641031', '296733155']; beyond: {'above': 'C38: None', 'below': "C43: '=SUM(C39:C42)'"}
- neighbourhood: B41: '2019-2020' | C41: 302641031 | D41: 22.5975 | E41: 93.36375 | B42: '2018-2019' | C42: 296733155 | D42: 23.22 | E42: 93.35749999999999 | C43: '=SUM(C39:C42)' -> 1058517622 | D43: '=AVERAGE(D39:D42)' -> 20.179375 | E43: '=AVERAGE(E39:E42)' -> 92.24781249999998

### `9cc23579ce3a|FORMULA_DRIFT|DATACARS!B24`

- workbook: `all_data_912_v0.1/spreadsheet/58829/3_58829_input.xlsx`
- location: `DATA CARS!B24`  severity: High  confidence: Likely defect
- formula: `=Afschrijving!B4`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AFSCHRIJVING!R[-20]C[10]
- evidence: This cell: =AFSCHRIJVING!R[-20]C
- cached value: 0.73496; row labels: ["'DISCOUNT'"]; column header: ''; used range: A1:F32
- neighbourhood: A22: 'FIRST REGISTARTION' | B22: 2017-05-01 00:00:00 | C22: 2018-05-01 00:00:00 | D22: 2019-05-01 00:00:00 | A23: 'DATE TO BUY' | B23: 2022-05-01 00:00:00 | C23: 2022-05-01 00:00:00 | D23: 2022-05-01 00:00:00 | A24: 'DISCOUNT' | B24: '=Afschrijving!B4' -> 0.73496 | C24: '=Afschrijving!M4' -> 0.665 | D24: '=Afschrijving!N4' -> 0.56998

### `0bffec63dc84|FORMULA_DRIFT|Purchases!H5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/1_CF_3712_input.xlsx`
- location: `Purchases!H5`  severity: High  confidence: Likely defect
- formula: `=IF(ISBLANK(G5), "", G5 + 14)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=400): =IF(ISBLANK(RC[-1]),"",RC[-1]+30)
- evidence: This cell: =IF(ISBLANK(RC[-1]),"",RC[-1]+14)
- cached value: 2024-09-09 00:00:00; row labels: ["'Pasjeshouder'", "'Overig'"]; column header: ''; used range: A1:M441
- neighbourhood: F3: '=(C3*E3)+D3' -> 127 | G3: 2024-03-24 00:00:00 | H3: '=IF(ISBLANK(G3), "", G3 + 30)' -> 2024-04-23 00:00:00 | I3: 'BIOP003' | J3: 'Microbes' | F4: '=(C4*E4)+D4' -> 127 | G4: 2024-09-27 00:00:00 | H4: '=IF(ISBLANK(G4), "", G4 + 30)' -> 2024-10-27 00:00:00 | I4: 'BIOP002' | J4: 'Plasmids' | F5: '=(C5*E5)+D5' -> 29.6 | G5: 2024-08-26 00:00:00 | H5: '=IF(ISBLANK(G5), "", G5 + 14)' -> 2024-09-09 00:00:00 | I5: 'BIOP001' | J5: 'Office' | F6: '=(C6*E6)+D6' -> 0 | H6: '=IF(ISBLANK(G6), "", G6 + 30)' -> None | F7: '=(C7*E7)+D7' -> 0 | H7: '=IF(ISBLANK(G7), "", G7 + 30)' -> None

### `6f6f318a8f93|FORMULA_DRIFT|LeadTimes!B9`

- workbook: `all_data_912_v0.1/spreadsheet/47741/3_47741_input.xlsx`
- location: `Lead Times!B9`  severity: High  confidence: Likely defect
- formula: `=WORKDAY(B8,10,K14:K24)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =WORKDAY(R[-1]C,10,R[9]C[9]:R[15]C[9])
- evidence: This cell: =WORKDAY(R[-1]C,10,R[5]C[9]:R[15]C[9])
- cached value: 2022-01-17 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range K14:K24: values ['2021-12-05 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None', 'None', 'None', 'None']; beyond: {'above': 'K13: None', 'below': 'K25: None'}
- neighbourhood: B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22' | B8: '=INDEX(calendar,ndx+1) {array B8:H8}' -> 2022-01-03 00:00:00 | C8: 2022-01-04 00:00:00 | D8: 2022-01-05 00:00:00 | B9: '=WORKDAY(B8,10,K14:K24)' -> 2022-01-17 00:00:00 | C9: '=WORKDAY(C8,10,L18:L24)' -> 2022-01-18 00:00:00 | D9: '=WORKDAY(D8,10,M18:M24)' -> 2022-01-19 00:00:00 | B10: '=WORKDAY(B8,18,K19:K25)' -> 2022-01-27 00:00:00 | C10: '=WORKDAY(C8,18,L19:L25)' -> 2022-01-28 00:00:00 | D10: '=WORKDAY(D8,18,M19:M25)' -> 2022-01-31 00:00:00 | B11: '1/6/22-1/10/22' | C11: '1/7/22-1/11/22' | D11: '1/10/22-1/12/22'

### `7dfe4964af12|FORMULA_DRIFT|Sheet1!G14`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!G14`  severity: High  confidence: Likely defect
- formula: `=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(E14/B14,""),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =IF(AND(NOT(ISBLANK(RC[-2])),RC[-5]>0,R[2]C49>0),IFERROR(RC[-2]/RC[-5],""),"")
- evidence: This cell: =IF(AND(NOT(ISBLANK(R[2]C14)),R[2]C11>0,R[2]C49>0),IFERROR(RC[-2]/RC[-5],""),"")
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: F12: '=IF(AND(NOT(ISBLANK(E12)),B12>0,$AW14>0),IFERROR(E12/B12,""),"")' -> None | G12: '=IF(AND(NOT(ISBLANK(E12)),B12>0,$AW14>0),IFERROR(E12/B12,""),"")' -> None | H12: '=IF(AND(NOT(ISBLANK($N14)),$K14>0,$AW14>0),IFERROR(F12/D12,""),"")' -> None | I12: '=IF(MAX(G12,H12)=0,"",MAX(G12,H12))' -> None | F13: '=IF(AND(NOT(ISBLANK(E13)),B13>0,$AW15>0),IFERROR(E13/B13,""),"")' -> None | G13: '=IF(AND(NOT(ISBLANK(E13)),B13>0,$AW15>0),IFERROR(E13/B13,""),"")' -> None | H13: '=IF(AND(NOT(ISBLANK($N15)),$K15>0,$AW15>0),IFERROR(F13/D13,""),"")' -> None | I13: '=IF(MAX(G13,H13)=0,"",MAX(G13,H13))' -> None | F14: '=IF(AND(NOT(ISBLANK(E14)),B14>0,$AW16>0),IFERROR(E14/B14,""),"")' -> None | G14: '=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(E14/B14,""),"")' -> None | H14: '=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(F14/D14,""),"")' -> None | I14: '=IF(MAX(G14,H14)=0,"",MAX(G14,H14))' -> None

### `7deacb0c30f0|FORMULA_DRIFT|Sheet1!C13`

- workbook: `all_data_912_v0.1/spreadsheet/183-8/1_183-8_input.xlsx`
- location: `Sheet1!C13`  severity: High  confidence: Likely defect
- formula: `=SUM(C9:C12)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AVERAGE(R[-4]C:R[-1]C)
- evidence: This cell: =SUM(R[-4]C:R[-1]C)
- cached value: 20404870; row labels: []; column header: ''; used range: A1:N43
- range C9:C12: values ['3989840', '4163703', '6184548', '6066779']; beyond: {'above': 'C8: None', 'below': "C13: '=SUM(C9:C12)'"}
- neighbourhood: B11: '2019-2020' | C11: 6184548 | D11: 23.53 | E11: 94.57 | B12: '2018-2019' | C12: 6066779 | D12: 23.33 | E12: 87.39 | C13: '=SUM(C9:C12)' -> 20404870 | D13: '=AVERAGE(D9:D12)' -> 19.47 | E13: '=AVERAGE(E9:E12)' -> 83.8925 | A15: 'c' | B15: '2021-2022' | C15: 20750626 | D15: 15.98 | E15: 98.22

### `f3998880f231|FORMULA_DRIFT|Sheet1!C7`

- workbook: `all_data_912_v0.1/spreadsheet/183-8/3_183-8_input.xlsx`
- location: `Sheet1!C7`  severity: High  confidence: Likely defect
- formula: `=SUM(C3:C6)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AVERAGE(R[-4]C:R[-1]C)
- evidence: This cell: =SUM(R[-4]C:R[-1]C)
- cached value: 1176448932; row labels: []; column header: ''; used range: A1:N43
- range C3:C6: values ['271486433', '263336524', '310016060', '331609915']; beyond: {'above': 'C2: None', 'below': "C7: '=SUM(C3:C6)'"}
- neighbourhood: B5: '2019-2020' | C5: 310016060 | D5: 20.32 | E5: 97.16 | B6: '2018-2019' | C6: 331609915 | D6: 21.93 | E6: 98.31 | C7: '=SUM(C3:C6)' -> 1176448932 | D7: '=AVERAGE(D3:D6)' -> 22.03 | E7: '=AVERAGE(E3:E6)' -> 94.1125 | A9: 'b' | B9: '2021-2022' | C9: 3989840 | D9: 15.18 | E9: 67.55

### `6d26dcd54bfa|FORMULA_DRIFT|Sheet1!C37`

- workbook: `all_data_912_v0.1/spreadsheet/183-8/2_183-8_input.xlsx`
- location: `Sheet1!C37`  severity: High  confidence: Likely defect
- formula: `=SUM(C33:C36)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AVERAGE(R[-4]C:R[-1]C)
- evidence: This cell: =SUM(R[-4]C:R[-1]C)
- cached value: 695925113; row labels: []; column header: ''; used range: A1:N43
- range C33:C36: values ['182867835', '164654673', '169183110', '179219495']; beyond: {'above': 'C32: None', 'below': "C37: '=SUM(C33:C36)'"}
- neighbourhood: B35: '2019-2020' | C35: 169183110 | D35: 33.365 | E35: 84.95333333333333 | B36: '2018-2019' | C36: 179219495 | D36: 35.693333333333335 | E36: 85.64 | C37: '=SUM(C33:C36)' -> 695925113 | D37: '=AVERAGE(D33:D36)' -> 27.834583333333335 | E37: '=AVERAGE(E33:E36)' -> 91.83833333333332 | A39: 'g' | B39: '2021-2022' | C39: 230800173 | D39: 17.48 | E39: 90.94

## HARDCODE_IN_FORMULA_BLOCK

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!M6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!M6`  severity: High  confidence: Likely defect
- evidence: Value 5 sits between Sheet1!L6 and Sheet1!O6, which share the pattern =RC[-2]-RC[-1].
- cached value: 5; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | O4: '=M4-N4' -> 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | O5: -1 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | O6: '=M6-N6' -> 5 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3 | O7: '=M7-N7' -> -1 | K8: 2 | L8: '=J8-K8' -> -2 | M8: 0 | N8: 2 | O8: '=M8-N8' -> -2

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!L5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!L5`  severity: High  confidence: Likely defect
- evidence: Value -1 sits between Sheet1!L4 and Sheet1!L6, which share the pattern =RC[-2]-RC[-1].
- cached value: -1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: J3: 2 | K3: 2 | L3: '=J3-K3' -> 0 | M3: 2 | N3: 2 | J4: 3 | K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | J5: 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | J7: 2 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3

### `6d6fc1caeb06|HARDCODE_IN_FORMULA_BLOCK|DRP!M7`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/1_175-10_input.xlsx`
- location: `DRP!M7`  severity: High  confidence: Likely defect
- evidence: Value 100 sits between DRP!L7 and DRP!O7, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 100; row labels: ["'RM1'", "'RC1'"]; column header: ''; used range: A1:O23
- neighbourhood: L5: '=I5+J5-K5' -> None | O5: '=L5+M5-N5' -> None | K6: '=SUM(K2:K5)' -> None | L6: '=SUM(L2:L5)' -> None | M6: '=SUM(M2:M5)' -> None | N6: '=SUM(N2:N5)' -> None | O6: '=SUM(O2:O5)' -> None | K7: 10 | L7: '=I7+J7-K7' -> None | M7: 100 | N7: 10 | O7: '=L7+M7-N7' -> None | K8: 5 | L8: '=I8+J8-K8' -> None | M8: 600 | N8: 5 | O8: '=L8+M8-N8' -> None | L9: '=I9+J9-K9' -> None | M9: 125 | O9: '=L9+M9-N9' -> None

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!P4`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!O4 and Sheet1!R4, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: N2: 'MBQ' | O2: 'Diff' | P2: 'Actual' | Q2: 'MBQ' | R2: 'Diff' | N3: 2 | O3: '=M3-N3' -> 0 | P3: 2 | Q3: 2 | R3: '=P3-Q3' -> 0 | N4: 2 | O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | N5: 6 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | N6: 0 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0

### `5ec32da9071e|HARDCODE_IN_FORMULA_BLOCK|Total(2)!E29`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!E29`  severity: High  confidence: Likely defect
- evidence: Value 1840 sits between Total (2)!E27 and Total (2)!E31, which share the pattern =SUM(RC[-3]*0.5).
- cached value: 1840; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | F27: 44589 | G27: 'C' | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | F28: 44576 | G28: 'N' | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C'

### `3a2b74c70f66|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C27`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!C27`  severity: High  confidence: Likely defect
- evidence: Value 2300 sits between Total (2)!C25 and Total (2)!C28, which share the pattern =(RC[-1]*12)/12.
- cached value: 2300; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A25: 18 | B25: 2800 | C25: '=(B25*12)/12' -> 2800 | D25: '=SUM(C25-E25)' -> 1120 | E25: 1680 | A26: 19 | B26: 2400 | C26: 2300 | D26: '=SUM(C26-E26)' -> 1100 | E26: '=SUM(B26*0.5)' -> 1200 | A27: 20 | B27: 2400 | C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | A28: 21 | B28: 2055 | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | A29: 22 | B29: 2300 | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840

### `738a64e94c99|HARDCODE_IN_FORMULA_BLOCK|DRP!M10`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/2_175-10_input.xlsx`
- location: `DRP!M10`  severity: High  confidence: Likely defect
- evidence: Value 131 sits between DRP!L10 and DRP!O10, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 131; row labels: ["'RM1'", "'RC1'"]; column header: ''; used range: A1:O23
- neighbourhood: K8: 5 | L8: '=I8+J8-K8' -> None | M8: 600 | N8: 5 | O8: '=L8+M8-N8' -> None | L9: '=I9+J9-K9' -> None | M9: 125 | O9: '=L9+M9-N9' -> None | L10: '=I10+J10-K10' -> None | M10: 131 | O10: '=L10+M10-N10' -> None | K11: '=SUM(K7:K10)' -> None | L11: '=SUM(L7:L10)' -> None | M11: '=SUM(M7:M10)' -> None | N11: '=SUM(N7:N10)' -> None | O11: '=SUM(O7:O10)' -> None | L12: '=I12+J12-K12' -> None | O12: '=L12+M12-N12' -> None

### `0c97a580a8e1|HARDCODE_IN_FORMULA_BLOCK|MonthlyTrans!AB67`

- workbook: `all_data_912_v0.1/spreadsheet/598-14/3_598-14_input.xlsx`
- location: `Monthly Trans!AB67`  severity: High  confidence: Likely defect
- evidence: Value 2020 sits between Monthly Trans!AB66 and Monthly Trans!AB68, which share the pattern =IF(TABLE1[[#THIS ROW],[DATE]]>0,TEXT(TABLE1[[#THIS ROW],[DATE]],"YYYY"),"").
- cached value: 2020; row labels: ["'Sep'"]; column header: ''; used range: A1:AC79
- neighbourhood: AA65: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> 'Sep' | AB65: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> '2020' | AC65: 2020-09-20 00:00:00 | AA66: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> 'Sep' | AB66: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> '2020' | AC66: 2020-09-21 00:00:00 | AA67: 'Sep' | AB67: 2020 | AC67: 2020-09-22 00:00:00 | AA68: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> None | AB68: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> None | AA69: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> None | AB69: '=IF(Table1[[#This Row],[Date]]>0,TEXT(Table1[[#This Row],[Date]],"... -> None

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!G6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!G6`  severity: High  confidence: Likely defect
- evidence: Value 5 sits between Sheet1!F6 and Sheet1!I6, which share the pattern =RC[-2]-RC[-1].
- cached value: 5; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: E4: 2 | F4: '=D4-E4' -> 1 | G4: 2 | H4: 2 | I4: '=G4-H4' -> 0 | E5: 2 | F5: -1 | G5: 3 | H5: 2 | I5: -1 | E6: 1 | F6: '=D6-E6' -> 4 | G6: 5 | H6: 1 | I6: '=G6-H6' -> 4 | E7: 3 | F7: '=D7-E7' -> -1 | G7: 2 | H7: 3 | I7: '=G7-H7' -> -1 | E8: 2 | F8: '=D8-E8' -> -2 | G8: 0 | H8: 2 | I8: '=G8-H8' -> -2

### `b495a5e6f4d1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!T3`

- workbook: `all_data_912_v0.1/spreadsheet/57354/2_57354_input.xlsx`
- location: `Sheet1!T3`  severity: High  confidence: Likely defect
- evidence: Value 29868 sits between Sheet1!Q3 and Sheet1!U3, which share the pattern =RC[-1]-RC[-3].
- cached value: 29868; row labels: ["'a'"]; column header: "'REVENUE'"; used range: A1:U11
- neighbourhood: R1: 2020-06-01 00:00:00 | R2: 'SPEND' | S2: 'SALES' | T2: 'REVENUE' | U2: 'GP' | R3: 23225.96 | S3: 528 | T3: 29868 | U3: '=T3-R3' -> 6642.04

### `3a2b74c70f66|HARDCODE_IN_FORMULA_BLOCK|Total(2)!E30`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!E30`  severity: High  confidence: Likely defect
- evidence: Value 925 sits between Total (2)!E27 and Total (2)!E31, which share the pattern =SUM(RC[-3]*0.5).
- cached value: 925; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | F28: 44576 | G28: 'N' | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C' | C32: '=(B32*12)/12' -> 3000 | D32: '=SUM(C32-E32)' -> 1050 | E32: '=IFERROR(VLOOKUP($H32,$J$27:$L$35,3,0)*$C32,0)' -> 1950 | F32: 44589 | G32: 'C'

### `6116800fac3b|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D16`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/1_395-48_input.xlsx`
- location: `Sheet1!D16`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D15 and Sheet1!D17, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'TERRERO PEDRO M'", "'MONROY FRANCISCO'"]; column header: ''; used range: A1:D302
- neighbourhood: B14: 'PENA BRYAN' | C14: 'ESPINOZA ASSAEL' | D14: '=IF(AND(A14=1,B14=C14),1,"")' -> None | B15: 'RODRIGUEZ JOSE ELIAS' | C15: 'RODRIGUEZ JOSE ELIAS' | D15: '=IF(AND(A15=1,B15=C15),1,"")' -> None | B16: 'TERRERO PEDRO M' | C16: 'MONROY FRANCISCO' | D16: 1 | B17: 'HERRERA HUGO' | C17: 'HARVEY B' | D17: '=IF(AND(A17=1,B17=C17),1,"")' -> None | B18: 'RODRIGUEZ JOSE ELIAS' | C18: 'RODRIGUEZ JOSE ELIAS' | D18: '=IF(AND(A18=1,B18=C18),1,"")' -> None

### `f6618f3a869c|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E4`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/3_191-40_input.xlsx`
- location: `Sheet1!E4`  severity: High  confidence: Likely defect
- evidence: Value 114.8 sits between Sheet1!D4 and Sheet1!F4, which share the pattern =RC[-2]+RC[-1].
- cached value: 114.8; row labels: ["'MERCY MERCY'"]; column header: ''; used range: A1:L250
- neighbourhood: C2: 112.8 | D2: 700 | E2: 114.5 | F2: '=D2+E2' -> 814.5 | G2: 2 | C3: 112.6 | D3: 900 | E3: 114.3 | F3: '=D3+E3' -> 1014.3 | G3: 2 | C4: 112.6 | D4: '=B4+C4' -> 224.7 | E4: 114.8 | F4: '=D4+E4' -> 339.5 | G4: 2 | C5: 112.4 | D5: '=B5+C5' -> 224.5 | E5: 111.7 | F5: '=D5+E5' -> 336.2 | G5: 2 | C6: 111.3 | D6: '=B6+C6' -> 221.5 | E6: 110.6 | F6: '=D6+E6' -> 332.1 | G6: 2

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!J4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!J4`  severity: High  confidence: Likely defect
- evidence: Value 3 sits between Sheet1!I4 and Sheet1!L4, which share the pattern =RC[-2]-RC[-1].
- cached value: 3; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: H2: 'MBQ' | I2: 'Diff' | J2: 'Actual' | K2: 'MBQ' | L2: 'Diff' | H3: 2 | I3: '=G3-H3' -> -1 | J3: 2 | K3: 2 | L3: '=J3-K3' -> 0 | H4: 2 | I4: '=G4-H4' -> 0 | J4: 3 | K4: 5 | L4: '=J4-K4' -> -2 | H5: 2 | I5: -1 | J5: 1 | K5: 7 | L5: -1 | H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4

### `738a64e94c99|HARDCODE_IN_FORMULA_BLOCK|DRP!N20`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/2_175-10_input.xlsx`
- location: `DRP!N20`  severity: High  confidence: Likely defect
- evidence: Value 12 sits between DRP!L20 and DRP!O20, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 12; row labels: ["'RRM1'", "'CV1'"]; column header: ''; used range: A1:O23
- neighbourhood: L18: '=I18+J18-K18' -> None | O18: '=L18+M18-N18' -> None | L19: '=I19+J19-K19' -> None | M19: 10 | O19: '=L19+M19-N19' -> None | L20: '=I20+J20-K20' -> None | N20: 12 | O20: '=L20+M20-N20' -> None | L21: '=I21+J21-K21' -> None | O21: '=L21+M21-N21' -> None | L22: '=I22+J22-K22' -> None | O22: '=L22+M22-N22' -> None

### `c05e60f72c61|HARDCODE_IN_FORMULA_BLOCK|Dati!AB25`

- workbook: `all_data_912_v0.1/spreadsheet/55912/2_55912_input.xlsx`
- location: `Dati!AB25`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Dati!AB24 and Dati!AB26, which share the pattern =IF(OR(RC18="-",RC18="\"),RC19+RC20," ").
- cached value: 1; row labels: ["'GOL'", "'-'"]; column header: ''; used range: A1:CJ40
- neighbourhood: AA23: '=IF(OR($R23="-",$R23="\\"),$U23+$V23," ")' -> 6 | AB23: '=IF(OR($R23="-",$R23="\\"),$S23+$T23," ")' -> 3 | AC23: '=IF(OR($R23="-",$R23="\\"),IF($AB23>0,"YES","NO")," ")' -> 'YES' | AA24: '=IF(OR($R24="-",$R24="\\"),$U24+$V24," ")' -> 6 | AB24: '=IF(OR($R24="-",$R24="\\"),$S24+$T24," ")' -> 3 | AC24: '=IF(OR($R24="-",$R24="\\"),IF($AB24>0,"YES","NO")," ")' -> 'YES' | AB25: 1 | AC25: '=IF(OR($R25="-",$R25="\\"),IF($AB25>0,"YES","NO")," ")' -> 'YES' | AA26: '=IF(OR($R26="-",$R26="\\"),$U26+$V26," ")' -> 1 | AB26: '=IF(OR($R26="-",$R26="\\"),$S26+$T26," ")' -> 0 | AC26: '=IF(OR($R26="-",$R26="\\"),IF($AB26>0,"YES","NO")," ")' -> 'NO' | AA27: '=IF(OR($R27="-",$R27="\\"),$U27+$V27," ")' -> 1 | AB27: '=IF(OR($R27="-",$R27="\\"),$S27+$T27," ")' -> 0 | AC27: '=IF(OR($R27="-",$R27="\\"),IF($AB27>0,"YES","NO")," ")' -> 'NO'

### `8b7bb50b3697|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C31`

- workbook: `all_data_912_v0.1/spreadsheet/35207/2_35207_input.xlsx`
- location: `Sheet1!C31`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/30/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899 | A33: '2/1/1890' | B33: 0.0001807 | C33: 0

### `2ed80e0ee4cd|HARDCODE_IN_FORMULA_BLOCK|DRP!N7`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!N7`  severity: High  confidence: Likely defect
- evidence: Value 10 sits between DRP!L7 and DRP!O7, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 10; row labels: ["'RM1'", "'RC1'"]; column header: ''; used range: A1:O23
- neighbourhood: L5: '=I5+J5-K5' -> None | O5: '=L5+M5-N5' -> None | L6: '=SUM(L2:L5)' -> None | M6: '=SUM(M2:M5)' -> None | N6: '=SUM(N2:N5)' -> None | O6: '=SUM(O2:O5)' -> None | L7: '=I7+J7-K7' -> None | M7: 100 | N7: 10 | O7: '=L7+M7-N7' -> None | L8: '=I8+J8-K8' -> None | M8: 600 | N8: 5 | O8: '=L8+M8-N8' -> None | L9: '=I9+J9-K9' -> None | M9: 125 | O9: '=L9+M9-N9' -> None

### `e5094a660f5e|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D73`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/2_395-48_input.xlsx`
- location: `Sheet1!D73`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D71 and Sheet1!D74, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'PENA BRYAN'", "'GONZALEZ RICARDO'"]; column header: ''; used range: A1:D302
- neighbourhood: B71: 'AMADOR SILVIO RUIZ' | C71: 'OROZCO KEVIN E' | D71: '=IF(AND(A71=1,B71=C71),1,"")' -> None | B72: 'ESPINOZA ASSAEL' | C72: 'ANTONGEORGI WILLIAM JR' | D72: 1 | B73: 'PENA BRYAN' | C73: 'GONZALEZ RICARDO' | D73: 1 | B74: 'ANTONGEORGI WILLIAM JR' | C74: 'ANTONGEORGI WILLIAM JR' | D74: '=IF(AND(A74=1,B74=C74),1,"")' -> None | B75: 'TERRERO PEDRO M' | C75: 'HERRERA CRISTOBAL' | D75: '=IF(AND(A75=1,B75=C75),1,"")' -> None

### `7b15ef0c0d8c|HARDCODE_IN_FORMULA_BLOCK|data!K25`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!K25`  severity: High  confidence: Likely defect
- evidence: Value 1.5 sits between data!K24 and data!K28, which share the pattern =SUM(RC[-2]-RC[-3]).
- cached value: 1.5; row labels: ["'TREvor bock'", "'unit has a miss'"]; column header: ''; used range: A1:O48
- neighbourhood: I23: '=HOUR(F23)+MINUTE(F23)/60+SECOND(F23)/3600' -> 16.5180555555556 | K23: '=SUM(I23-H23)' -> 1.51222222222222 | I24: '=HOUR(F24)+MINUTE(F24)/60+SECOND(F24)/3600' -> 9.875 | K24: '=SUM(I24-H24)' -> 1.48638888888889 | K25: 1.5

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!Q6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!Q6`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!O6 and Sheet1!R6, which share the pattern =RC[-2]-RC[-1].
- cached value: 1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0 | O7: '=M7-N7' -> -1 | P7: 2 | Q7: 3 | R7: '=P7-Q7' -> -1 | O8: '=M8-N8' -> -2 | P8: 0 | Q8: 2 | R8: '=P8-Q8' -> -2

### `6116800fac3b|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D48`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/1_395-48_input.xlsx`
- location: `Sheet1!D48`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D47 and Sheet1!D49, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'MARTINEZ CATALINO'", "'BRAVO J'"]; column header: ''; used range: A1:D302
- neighbourhood: B46: 'TERRERO PEDRO M' | C46: 'TERRERO PEDRO M' | D46: '=IF(AND(A46=1,B46=C46),1,"")' -> None | B47: 'PENA BRYAN' | C47: 'PENA BRYAN' | D47: '=IF(AND(A47=1,B47=C47),1,"")' -> None | B48: 'MARTINEZ CATALINO' | C48: 'BRAVO J' | D48: 1 | B49: 'MONROY FRANCISCO' | C49: 'FREY KYLE' | D49: '=IF(AND(A49=1,B49=C49),1,"")' -> None | B50: 'MONROY FRANCISCO' | C50: 'MONROY FRANCISCO' | D50: '=IF(AND(A50=1,B50=C50),1,"")' -> None

### `09478d797a42|HARDCODE_IN_FORMULA_BLOCK|BankBalance!C4`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Bank Balance!C4`  severity: High  confidence: Likely defect
- evidence: Value 2000 sits between Bank Balance!C3 and Bank Balance!C5, which share the pattern =IF(AND(JOURNAL ENTRIES!R[3]C8="debit",JOURNAL ENTRIES!R[3]C5=BANK BALANCE!R2C),JOURNAL ENTRIES!R[3]C6,"").
- cached value: 2000; row labels: []; column header: ''; used range: A1:AL3000
- neighbourhood: A2: 'Date' | B2: 'Ref/Invoice/Cheque No.' | C2: 'Document Charges' | D2: 'Loan Capital Recovery' | E2: 'Loan Interest Recovery' | A3: "=+'Journal Entries'!B6" -> 2021-03-21 00:00:00 | B3: "=+'Journal Entries'!I6" -> 'N/A' | C3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> 2000 | D3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> None | E3: '=IF(AND(\'Journal Entries\'!$H6="debit",\'Journal Entries\'!$E6=\'... -> None | A4: "=+'Journal Entries'!B7" -> 2021-03-21 00:00:00 | B4: "=+'Journal Entries'!I7" -> 456798 | C4: 2000 | D4: '=IF(AND(\'Journal Entries\'!$H7="debit",\'Journal Entries\'!$E7=\'... -> None | E4: '=IF(AND(\'Journal Entries\'!$H7="debit",\'Journal Entries\'!$E7=\'... -> None | A5: "=+'Journal Entries'!B8" -> 2021-03-26 00:00:00 | B5: "=+'Journal Entries'!I8" -> 0 | C5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | D5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | E5: '=IF(AND(\'Journal Entries\'!$H8="debit",\'Journal Entries\'!$E8=\'... -> None | A6: "=+'Journal Entries'!B9" -> 2021-03-26 00:00:00 | B6: "=+'Journal Entries'!I9" -> 0 | C6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None | D6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None | E6: '=IF(AND(\'Journal Entries\'!$H9="debit",\'Journal Entries\'!$E9=\'... -> None

### `711b43c06db1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!T3`

- workbook: `all_data_912_v0.1/spreadsheet/57354/1_57354_input.xlsx`
- location: `Sheet1!T3`  severity: High  confidence: Likely defect
- evidence: Value 29868 sits between Sheet1!Q3 and Sheet1!U3, which share the pattern =RC[-1]-RC[-3].
- cached value: 29868; row labels: ["'a'"]; column header: "'REVENUE'"; used range: A1:U11
- neighbourhood: R1: 2020-06-01 00:00:00 | R2: 'SPEND' | S2: 'SALES' | T2: 'REVENUE' | U2: 'GP' | R3: 23225.96 | S3: 528 | T3: 29868 | U3: '=T3-R3' -> 6642.04

### `cae038ac83e8|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E3`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/2_191-40_input.xlsx`
- location: `Sheet1!E3`  severity: High  confidence: Likely defect
- evidence: Value 114.3 sits between Sheet1!D3 and Sheet1!F3, which share the pattern =RC[-2]+RC[-1].
- cached value: 114.3; row labels: ["'BRITTLE AND YOO'"]; column header: ''; used range: A1:L250
- neighbourhood: C1: 114.4 | D1: '=B1+C1' -> 230 | E1: 110.8 | F1: '=D1+E1' -> 340.8 | G1: 2 | C2: 112.8 | D2: 1000 | E2: 114.5 | F2: '=D2+E2' -> 1114.5 | G2: 2 | C3: 112.6 | D3: '=B3+C3' -> 224.8 | E3: 114.3 | F3: '=D3+E3' -> 339.1 | G3: 2 | C4: 112.6 | D4: '=B4+C4' -> 224.7 | E4: 114.8 | F4: '=D4+E4' -> 339.5 | G4: 2 | C5: 112.4 | D5: '=B5+C5' -> 224.5 | E5: 111.7 | F5: '=D5+E5' -> 336.2 | G5: 2

## HIDDEN_STRUCTURE_IN_TOTAL

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|ac6dc9`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AO on formamspnc (7) feeds 44 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BU5, formamspnc (7)!BV5, formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> None | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> '1'

### `a556b2a52595|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|eaab5a`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AW on Sheet1 feeds 42 visible formula(s): Sheet1!D4, Sheet1!C5, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CO5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!CO5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AQ on formamspnc (7) feeds 31 visible formula(s): formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AQ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AR5: None'}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CM6: '=IF(COUNTIF(BX6:CJ6,0)>3,COUNTIF(BX6:CJ6,0),"")' -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CM7: '=IF(COUNTIF(BX7:CJ7,0)>3,COUNTIF(BX7:CJ7,0),"")' -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|ac6dc9`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AO on formamspnc (7) feeds 44 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BU5, formamspnc (7)!BV5, formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> '1' | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> None

### `ab88bab5d14b|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H4`

- workbook: `all_data_912_v0.1/spreadsheet/50154/2_50154_input.xlsx`
- location: `Sheet1!H4`  severity: Medium  confidence: Review
- formula: `=SUM(G4,F4)`
- evidence: Hidden columns F, G on Sheet1 feed 11 visible formula(s): Sheet1!H4, Sheet1!H5, Sheet1!H6, Sheet1!H7, Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, ....
- cached value: 7.66666666666667; row labels: ["'Winter Guard #1'", "'Y'"]; column header: "'Final Score'"; used range: A1:O15
- neighbourhood: F3: 'Splash page points' | G3: 'AVG' | H3: 'Final Score' | F4: '=IF(D4="Y",1,0)' -> 1 | G4: '=AVERAGE(B4:C4,E4)' -> 6.66666666666667 | H4: '=SUM(G4,F4)' -> 7.66666666666667 | F5: '=IF(D5="Y",1,0)' -> 0 | G5: '=AVERAGE(B5:C5,E5)' -> 6.33333333333333 | H5: '=SUM(G5,F5)' -> 6.33333333333333 | F6: '=IF(D6="Y",1,0)' -> 1 | G6: '=AVERAGE(B6:C6,E6)' -> 6.66666666666667 | H6: '=SUM(G6,F6)' -> 7.66666666666667

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CP5|7ba3a8`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!CP5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AS on formamspnc (7) feeds 12 visible formula(s): formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, formamspnc (7)!CW5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AF5:BJ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AE5: None', 'right': "BK5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:A..."}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CR5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AH5:BL5,AH$1+{1,0,-1}),{1,0,-1}),"... -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `ef479c030de6|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|eaab5a`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AW on Sheet1 feeds 42 visible formula(s): Sheet1!D4, Sheet1!C5, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!BF5|35c025`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!BF5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column X on formamspnc (7) feeds 98 visible formula(s): formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: "'m3'"; used range: A1:ED48610
- range P5:AB5: values ['None', 'None', "'1 ext,1st 1 ext'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'O5: \'=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A",...', 'right': 'AC5: None'}
- neighbourhood: BD3: 'm1' | BE3: 'm2' | BF3: 'm3' | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BH3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),2) {array BH3}' -> '#NUM!' | BD5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(L5:Z5,L$1+{1,0,-1}),{1,0,-1}),"") ... -> None | BE5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")... -> None | BF5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")... -> None | BD6: '=SUM(AE6:AO6)' -> 3 | BE6: '=SUM(AE6:AP6)' -> 3 | BF6: '=SUM(AE6:AQ6)' -> 4 | BG6: '=IF(COUNTIF(AT6:AY6,0)>2,"a","")' -> None | BD7: '=SUM(AE7:AO7)' -> 2 | BE7: '=SUM(AE7:AP7)' -> 2 | BF7: '=SUM(AE7:AQ7)' -> 3 | BG7: '=IF(COUNTIF(AT7:AY7,0)>2,"a","")' -> 'a' | BH7: '=IF(OR(BF7=0,BE7=0),"e",IF(OR(AND(BE7=0,BF7=0),AND(BD7=0,BE7=0)),"... -> 'b'

### `9b7879bd3308|HIDDEN_STRUCTURE_IN_TOTAL|Here!I2`

- workbook: `all_data_912_v0.1/spreadsheet/58147/1_58147_input.xlsx`
- location: `Here!I2`  severity: Medium  confidence: Review
- formula: `=1&" - "&F2`
- evidence: Hidden column F on Here feeds 2 visible formula(s): Here!I2, Here!I6.
- cached value: '1 - Tbnor, Cadigan - TA32785655'; row labels: []; column header: "'Extract'"; used range: A1:J140
- neighbourhood: G1: 'Letter' | H1: 'First Name' | I1: 'Extract' | J1: 'Outcome' | G2: '=LEFT(F2,1)' -> 'T' | H2: '=1&" - "&C2' -> '1 - Tbnor' | I2: '=1&" - "&F2' -> '1 - Tbnor, Cadigan - TA327... | J2: 'Tbnor, Cadigan' | G3: '=LEFT(F3,1)' -> 'A' | H3: '=C4' -> 'Tbra' | I3: 'Tbra, Cadle - AA21259159' | J3: 'Tbra, Cadle' | G4: '=LEFT(F4,1)' -> 'T' | H4: '=C7' -> 'Tbrahame' | I4: 'Tbrahame, Cadogan - LB71531251' | J4: 'Tbrahame, Cadogan'

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22, 23, 24, 25, 26, 27, 28, 29 and 469 more on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `09478d797a42|HIDDEN_STRUCTURE_IN_TOTAL|MonthlyExpensesSummary!E6`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Monthly Expenses Summary!E6`  severity: Medium  confidence: Review
- formula: `=IFERROR(SUMPRODUCT(('Journal Entries'!$C$6:$C$3000='Monthly Expenses Summary'!$B6)*('Journal Entries'!$B$6:$B$3000<>"")*(MONTH('Journal Entries'!$B$6:$B$3000)=MONTH(E$4&0))*(YEAR('Journal Entries'!$B$6:$B$3000)='Monthly Expenses Summary'!$R$2)*('Journal Entries'!$F$6:$F$3000)),"")`
- evidence: Hidden row 2 on Monthly Expenses Summary feeds 480 visible formula(s): Monthly Expenses Summary!E6, Monthly Expenses Summary!F6, Monthly Expenses Summary!G6, Monthly Expenses Summary!H6, Monthly Expenses Summary!I6, Monthly Expenses Summary!J6, Monthly Expenses Summary!K6, Monthly Expenses Summary!L6, ....
- cached value: 0; row labels: ["'Building Rent'"]; column header: "'January'"; used range: A1:R65
- range 'Journal Entries'!$C$6:$C$3000: values ["'WG/CR/027'", "'WG/CR/001'", "'WG/CR/006'", "'WG/CR/006'", "'WG/CR/008'", "'WG/CR/006'", "'WG/CR/007'", "'WG/CR/003'", "'WG/CR/001'", "'WG/CR/027'", "'WG/CR/028'", "'WG/CR/029'"]; beyond: {'above': "C5: 'Item Code'", 'below': 'C3001: None'}
- neighbourhood: C4: 'Final Acc. Entry' | D4: 'Account Title' | E4: 'January' | F4: 'February' | G4: 'March' | D5: 'Expenses' | C6: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D6: 'Building Rent' | E6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 35000 | C7: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D7: 'Electricity' | E7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | C8: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D8: 'Fuel' | E8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 2000

### `ea1e0839ce78|HIDDEN_STRUCTURE_IN_TOTAL|Here!A2`

- workbook: `all_data_912_v0.1/spreadsheet/58114/2_58114_input.xlsx`
- location: `Here!A2`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!A2="","",Sheet1!A2)`
- evidence: Hidden sheet 'Sheet1' feeds 834 visible formula(s): Here!A2, Here!B2, Here!C2, Here!D2, Here!E2, Here!F2, Here!A3, Here!B3, ....
- cached value: 1; row labels: []; column header: "'#'"; used range: A1:J140
- neighbourhood: A1: '#' | B1: 'ID' | C1: 'First Name' | A2: '=IF(Sheet1!A2="","",Sheet1!A2)' -> 1 | B2: '=IF(Sheet1!B2="","",Sheet1!B2)' -> 'TA32785655' | C2: '=IF(Sheet1!C2="","",Sheet1!C2)' -> 'Tbnor' | A3: '=IF(Sheet1!A3="","",Sheet1!A3)' -> 2 | B3: '=IF(Sheet1!B3="","",Sheet1!B3)' -> 'SA12442673' | C3: '=IF(Sheet1!C3="","",Sheet1!C3)' -> 'Abo' | A4: '=IF(Sheet1!A4="","",Sheet1!A4)' -> 3 | B4: '=IF(Sheet1!B4="","",Sheet1!B4)' -> 'AA21259159' | C4: '=IF(Sheet1!C4="","",Sheet1!C4)' -> 'Tbra'

### `3ee4d6f069b6|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!N3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Daily Numbers!N3`  severity: Medium  confidence: Review
- formula: `=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Errors!$B:$B,"="&$B3,Errors!$AB:$AB,"="&$G3,Errors!$AB:$AB,"="&$H3,Errors!$AB:$AB,"="&$I3,Errors!$AB:$AB,"="&$J3)`
- evidence: Hidden rows 2, 3, 4, 5, 6, 7, 8, 9 and 493 more on Errors feed 110 visible formula(s): Daily Numbers!N3, Daily Numbers!O3, Daily Numbers!P3, Daily Numbers!Q3, Daily Numbers!R3, Daily Numbers!N4, Daily Numbers!O4, Daily Numbers!P4, ....
- cached value: 0; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'II'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | P2: 'IT' | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 28599 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | P3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | P4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | P5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CO5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!CO5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AQ on formamspnc (7) feeds 31 visible formula(s): formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AQ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AR5: None'}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CM6: '=IF(COUNTIF(BX6:CJ6,0)>3,COUNTIF(BX6:CJ6,0),"")' -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CM7: '=IF(COUNTIF(BX7:CJ7,0)>3,COUNTIF(BX7:CJ7,0),"")' -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `ef479c030de6|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|61d632`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AY on Sheet1 feeds 20 visible formula(s): Sheet1!D4, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, Sheet1!D8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `69355e1eb76d|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22, 23, 24, 25, 26, 27, 28, 29 and 469 more on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `86313189897d|HIDDEN_STRUCTURE_IN_TOTAL|DATACARS!B24`

- workbook: `all_data_912_v0.1/spreadsheet/58829/1_58829_input.xlsx`
- location: `DATA CARS!B24`  severity: Medium  confidence: Review
- formula: `=Afschrijving!B4`
- evidence: Hidden sheet 'Afschrijving' feeds 4 visible formula(s): DATA CARS!B24, DATA CARS!C24, DATA CARS!D24, DATA CARS!E24.
- cached value: 0.73496; row labels: ["'DISCOUNT'"]; column header: ''; used range: A1:F32
- neighbourhood: A22: 'FIRST REGISTARTION' | B22: 2017-05-01 00:00:00 | C22: 2018-05-01 00:00:00 | D22: 2019-05-01 00:00:00 | A23: 'DATE TO BUY' | B23: 2022-05-01 00:00:00 | C23: 2022-05-01 00:00:00 | D23: 2022-05-01 00:00:00 | A24: 'DISCOUNT' | B24: '=Afschrijving!B4' -> 0.73496 | C24: '=Afschrijving!M4' -> 0.665 | D24: '=Afschrijving!N4' -> 0.56998

### `447f9eaa5b6c|HIDDEN_STRUCTURE_IN_TOTAL|Employee2!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/2_382-29_input.xlsx`
- location: `Employee 2!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden row 23 on Employee 2 feeds 24 visible formula(s): Employee 2!U3, Employee 2!AB5, Employee 2!AB6, Employee 2!AB7, Employee 2!AB8, Employee 2!AB9, Employee 2!AB10, Employee 2!AB11, ....
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `9cc23579ce3a|HIDDEN_STRUCTURE_IN_TOTAL|DATACARS!B24`

- workbook: `all_data_912_v0.1/spreadsheet/58829/3_58829_input.xlsx`
- location: `DATA CARS!B24`  severity: Medium  confidence: Review
- formula: `=Afschrijving!B4`
- evidence: Hidden sheet 'Afschrijving' feeds 4 visible formula(s): DATA CARS!B24, DATA CARS!C24, DATA CARS!D24, DATA CARS!E24.
- cached value: 0.73496; row labels: ["'DISCOUNT'"]; column header: ''; used range: A1:F32
- neighbourhood: A22: 'FIRST REGISTARTION' | B22: 2017-05-01 00:00:00 | C22: 2018-05-01 00:00:00 | D22: 2019-05-01 00:00:00 | A23: 'DATE TO BUY' | B23: 2022-05-01 00:00:00 | C23: 2022-05-01 00:00:00 | D23: 2022-05-01 00:00:00 | A24: 'DISCOUNT' | B24: '=Afschrijving!B4' -> 0.73496 | C24: '=Afschrijving!M4' -> 0.665 | D24: '=Afschrijving!N4' -> 0.56998

### `7dfe4964af12|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|61d632`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AY on Sheet1 feeds 20 visible formula(s): Sheet1!D4, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, Sheet1!D8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `447f9eaa5b6c|HIDDEN_STRUCTURE_IN_TOTAL|Employee1!V3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/2_382-29_input.xlsx`
- location: `Employee 1!V3`  severity: Medium  confidence: Review
- formula: `=$B24`
- evidence: Hidden row 24 on Employee 1 feeds 23 visible formula(s): Employee 1!V3, Employee 1!AB6, Employee 1!AB7, Employee 1!AB8, Employee 1!AB9, Employee 1!AB10, Employee 1!AB11, Employee 1!AB12, ....
- cached value: 'Test 20'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | X3: '=$B26' -> 'Test 22' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | X4: 'V' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X' | X5: 'X'

### `5a98e72c8ee6|HIDDEN_STRUCTURE_IN_TOTAL|MonthlyExpensesSummary!E6`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Monthly Expenses Summary!E6`  severity: Medium  confidence: Review
- formula: `=IFERROR(SUMPRODUCT(('Journal Entries'!$C$6:$C$3000='Monthly Expenses Summary'!$B6)*('Journal Entries'!$B$6:$B$3000<>"")*(MONTH('Journal Entries'!$B$6:$B$3000)=MONTH(E$4&0))*(YEAR('Journal Entries'!$B$6:$B$3000)='Monthly Expenses Summary'!$R$2)*('Journal Entries'!$F$6:$F$3000)),"")`
- evidence: Hidden row 2 on Monthly Expenses Summary feeds 480 visible formula(s): Monthly Expenses Summary!E6, Monthly Expenses Summary!F6, Monthly Expenses Summary!G6, Monthly Expenses Summary!H6, Monthly Expenses Summary!I6, Monthly Expenses Summary!J6, Monthly Expenses Summary!K6, Monthly Expenses Summary!L6, ....
- cached value: 0; row labels: ["'Building Rent'"]; column header: "'January'"; used range: A1:R65
- range 'Journal Entries'!$C$6:$C$3000: values ["'WG/CR/027'", "'WG/CR/001'", "'WG/CR/006'", "'WG/CR/006'", "'WG/CR/008'", "'WG/CR/006'", "'WG/CR/007'", "'WG/CR/003'", "'WG/CR/001'", "'WG/CR/027'", "'WG/CR/028'", "'WG/CR/029'"]; beyond: {'above': "C5: 'Item Code'", 'below': 'C3001: None'}
- neighbourhood: C4: 'Final Acc. Entry' | D4: 'Account Title' | E4: 'January' | F4: 'February' | G4: 'March' | D5: 'Expenses' | C6: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D6: 'Building Rent' | E6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 35000 | C7: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D7: 'Electricity' | E7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | C8: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D8: 'Fuel' | E8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 2000

### `d2a515f35dce|HIDDEN_STRUCTURE_IN_TOTAL|Admin&Settings!U5`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Admin & Settings!U5`  severity: Medium  confidence: Review
- formula: `=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*7)+T5-WEEKDAY(DATE(Schedule!$B$6,Q5,1))+IF(T5<WEEKDAY(DATE(Schedule!$B$6,Q5,1)),7,0))`
- evidence: Hidden column B on Schedule feeds 70 visible formula(s): Admin & Settings!U5, Admin & Settings!U6, Admin & Settings!U7, Admin & Settings!U8, Admin & Settings!U9, Admin & Settings!U10, Admin & Settings!U11, Admin & Settings!U12, ....
- cached value: 2023-01-16 00:00:00; row labels: ["'Duration'", "'ML King Day'"]; column header: "'Date'"; used range: A1:X80
- neighbourhood: S4: 'Week' | T4: 'Weekday' | U4: 'Date' | V4: 'When / Notes' | S5: 3 | T5: 2 | U5: '=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*... -> 2023-01-16 00:00:00 | V5: 'January 1' | S6: 3 | T6: 2 | U6: '=IF(OR(OR(Q6="",S6=""),T6=""),"",(DATE(Schedule!$B$6,Q6,1)+(S6-1)*... -> 2023-02-20 00:00:00 | V6: 'The 3rd Monday in January' | S7: 2 | T7: 1 | U7: '=IF(OR(OR(Q7="",S7=""),T7=""),"",(DATE(Schedule!$B$6,Q7,1)+(S7-1)*... -> 2023-05-14 00:00:00 | V7: '2nd Sunday in May'

### `d7bb3bd8958a|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25`

- workbook: `all_data_912_v0.1/spreadsheet/57989/1_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden rows 12, 17 on Sheet1 feed 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, ....
- cached value: 0; row labels: ["'Driver 1'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 1' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 2' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 1 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 3' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 1 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `7dfe4964af12|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H8`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!H8`  severity: Medium  confidence: Review
- formula: `=IF(AND(NOT(ISBLANK($N10)),$K10>0,$AW10>0),IFERROR(F8/D8,""),"")`
- evidence: Hidden column N on Sheet1 feeds 8 visible formula(s): Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, Sheet1!H12, Sheet1!H13, Sheet1!G14, Sheet1!H14.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: F6: 0.0818713450292398 | G6: 0.0818713450292398 | H6: 0.909681611435997 | I6: 0.909681611435997 | F7: 0.0867052023121387 | G7: 0.0867052023121387 | H7: 0.867052023121387 | I7: 0.867052023121387 | F8: '=IF(AND(NOT(ISBLANK(E8)),B8>0,$AW10>0),IFERROR(E8/B8,""),"")' -> None | G8: '=IF(AND(NOT(ISBLANK(E8)),B8>0,$AW10>0),IFERROR(E8/B8,""),"")' -> None | H8: '=IF(AND(NOT(ISBLANK($N10)),$K10>0,$AW10>0),IFERROR(F8/D8,""),"")' -> None | I8: '=IF(MAX(G8,H8)=0,"",MAX(G8,H8))' -> None | F9: '=IF(AND(NOT(ISBLANK(E9)),B9>0,$AW11>0),IFERROR(E9/B9,""),"")' -> None | G9: '=IF(AND(NOT(ISBLANK(E9)),B9>0,$AW11>0),IFERROR(E9/B9,""),"")' -> None | H9: '=IF(AND(NOT(ISBLANK($N11)),$K11>0,$AW11>0),IFERROR(F9/D9,""),"")' -> None | I9: '=IF(MAX(G9,H9)=0,"",MAX(G9,H9))' -> None | F10: '=IF(AND(NOT(ISBLANK(E10)),B10>0,$AW12>0),IFERROR(E10/B10,""),"")' -> None | G10: '=IF(AND(NOT(ISBLANK(E10)),B10>0,$AW12>0),IFERROR(E10/B10,""),"")' -> None | H10: '=IF(AND(NOT(ISBLANK($N12)),$K12>0,$AW12>0),IFERROR(F10/D10,""),"")' -> None | I10: '=IF(MAX(G10,H10)=0,"",MAX(G10,H10))' -> None

## IFERROR_MASK

### `57d001666bfd|IFERROR_MASK|Sheet1!E8`

- workbook: `all_data_912_v0.1/spreadsheet/52964/1_52964_input.xlsx`
- location: `Sheet1!E8`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($AG$2:$AG$124,MATCH($A8,$AA$2:$AA124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:BE279
- range $AG$2:$AG$124: values ['13', '6', '1', '3', '2', '3', '2', '6', '8', '3', '2', '1']; beyond: {'above': "AG1: 'LoS'", 'below': 'AG125: None'}
- neighbourhood: D6: '=IF(COUNTIF(AF6,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E6: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A6,$AA$2:$AA124,0)),0)' -> 0 | F6: '=IF(E6>14,E6,"N/A")' -> 'N/A' | D7: '=IF(COUNTIF(AF7,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E7: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A7,$AA$2:$AA124,0)),0)' -> 0 | F7: '=IF(E7>14,E7,"N/A")' -> 'N/A' | D8: '=IF(COUNTIF(AF8,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E8: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A8,$AA$2:$AA124,0)),0)' -> 0 | F8: '=IF(E8>14,E8,"N/A")' -> 'N/A' | D9: '=IF(COUNTIF(AF9,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E9: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A9,$AA$2:$AA124,0)),0)' -> 0 | F9: '=IF(E9>14,E9,"N/A")' -> 'N/A' | D10: '=IF(COUNTIF(AF10,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E10: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A10,$AA$2:$AA124,0)),0)' -> 0 | F10: '=IF(E10>14,E10,"N/A")' -> 'N/A'

### `c2c1c9ef2579|IFERROR_MASK|formamspnc(7)!BE5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!BE5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Formula uses IFNA.
- evidence: The same relative formula appears in 2 cells on this sheet; the others are formamspnc (7)!BF5.
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: "'m2'"; used range: A1:ED48610
- range O5:AA5: values ['None', 'None', 'None', "'1 ext,1st 1 ext'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'N5: None', 'right': 'AB5: None'}
- neighbourhood: BD3: 'm1' | BE3: 'm2' | BF3: 'm3' | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BC5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(K5:Y5,K$1+{1,0,-1}),{1,0,-1}),"") ... -> None | BD5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(L5:Z5,L$1+{1,0,-1}),{1,0,-1}),"") ... -> None | BE5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")... -> None | BF5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")... -> None | BC6: '=SUM(AE6:AN6)' -> 5 | BD6: '=SUM(AE6:AO6)' -> 3 | BE6: '=SUM(AE6:AP6)' -> 3 | BF6: '=SUM(AE6:AQ6)' -> 4 | BG6: '=IF(COUNTIF(AT6:AY6,0)>2,"a","")' -> None | BC7: '=SUM(AE7:AN7)' -> 3 | BD7: '=SUM(AE7:AO7)' -> 2 | BE7: '=SUM(AE7:AP7)' -> 2 | BF7: '=SUM(AE7:AQ7)' -> 3 | BG7: '=IF(COUNTIF(AT7:AY7,0)>2,"a","")' -> 'a'

### `f97f2feedd64|IFERROR_MASK|RESULTS1!W27`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!W27`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">100000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],"<100000000",Table1[FLOAT],">100000000")/COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">100000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Trades'", "'< 100M'"]; column header: "'100M <'"; used range: A1:W67
- neighbourhood: U26: '20-50M' | V26: '50-100M' | W26: '100M <' | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `6741b8e20874|IFERROR_MASK|OrderSheetFinal!AJ6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!AJ6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AJ7, Order Sheet Final!AJ8, Order Sheet Final!AJ9, Order Sheet Final!AJ10, Order Sheet Final!AJ11, Order Sheet Final!AJ12, Order Sheet Final!AJ13, Order Sheet Final!AJ14, ....
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'C14.2'"; used range: A1:AS37
- neighbourhood: AH4: '=SUM(AH6:AH33)' -> 0 | AI4: '=SUM(AI6:AI33)' -> 0 | AJ4: '=SUM(AJ6:AJ33)' -> 0 | AK4: '=SUM(AK6:AK33)' -> 0 | AL4: '=SUM(AL6:AL33)' -> 10 | AH5: 'C12' | AI5: 'C14.1' | AJ5: 'C14.2' | AK5: 'D1' | AL5: 'D2' | AH6: '=IFERROR(VLOOKUP(B6,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI6: "=IFERROR(VLOOKUP(B6,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ6: "=IFERROR(VLOOKUP(B6,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK6: '=IFERROR(VLOOKUP(B6,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL6: '=IFERROR(VLOOKUP(B6,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0 | AH7: '=IFERROR(VLOOKUP(B7,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI7: "=IFERROR(VLOOKUP(B7,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ7: "=IFERROR(VLOOKUP(B7,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK7: '=IFERROR(VLOOKUP(B7,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL7: '=IFERROR(VLOOKUP(B7,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 2 | AH8: '=IFERROR(VLOOKUP(B8,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI8: "=IFERROR(VLOOKUP(B8,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ8: "=IFERROR(VLOOKUP(B8,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK8: '=IFERROR(VLOOKUP(B8,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL8: '=IFERROR(VLOOKUP(B8,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0

### `57d001666bfd|IFERROR_MASK|Sheet1!K5`

- workbook: `all_data_912_v0.1/spreadsheet/52964/1_52964_input.xlsx`
- location: `Sheet1!K5`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($S$2:$S$124,MATCH($A5,$Q$2:$Q124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 78; row labels: []; column header: ''; used range: A1:BE279
- range $S$2:$S$124: values ['75', '76', '91', '78', '79', '87', '85', '82', '81', '88', '75', '76']; beyond: {'above': "S1: 'Age'", 'below': 'S125: None'}
- neighbourhood: J3: '=IFERROR(INDEX($R$2:$R$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 1944-04-11 00:00:00 | K3: '=IFERROR(INDEX($S$2:$S$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 76 | L3: '=IF(K3<85,"75-84",">85")' -> '75-84' | M3: '=IFERROR(INDEX($T$2:$T$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 'Male' | J4: '=IFERROR(INDEX($R$2:$R$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 1930-06-17 00:00:00 | K4: '=IFERROR(INDEX($S$2:$S$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 91 | L4: '=IF(K4<85,"75-84",">85")' -> '>85' | M4: '=IFERROR(INDEX($T$2:$T$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 'Female' | J5: '=IFERROR(INDEX($R$2:$R$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 1942-07-08 00:00:00 | K5: '=IFERROR(INDEX($S$2:$S$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 78 | L5: '=IF(K5<85,"75-84",">85")' -> '75-84' | M5: '=IFERROR(INDEX($T$2:$T$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 'Male' | J6: '=IFERROR(INDEX($R$2:$R$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 1941-10-15 00:00:00 | K6: '=IFERROR(INDEX($S$2:$S$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 79 | L6: '=IF(K6<85,"75-84",">85")' -> '75-84' | M6: '=IFERROR(INDEX($T$2:$T$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 'Female' | J7: '=IFERROR(INDEX($R$2:$R$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 1934-01-27 00:00:00 | K7: '=IFERROR(INDEX($S$2:$S$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 87 | L7: '=IF(K7<85,"75-84",">85")' -> '>85' | M7: '=IFERROR(INDEX($T$2:$T$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 'Male'

### `d2a515f35dce|IFERROR_MASK|InvoicePayments!K16`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Invoice Payments!K16`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[#This Row],[Due Date]]<30,"1 - 30 Days",IF(TD-T_INV3[[#This Row],[Due Date]]<60,"31 - 60 Days",IF(TD-T_INV3[[#This Row],[Due Date]]<90,"61 - 90 Days","91+ Days"))),""),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 8 cells on this sheet; the others are Invoice Payments!K17, Invoice Payments!K18, Invoice Payments!K19, Invoice Payments!K20, Invoice Payments!K21, Invoice Payments!K22, Invoice Payments!K23.
- cached value: None; row labels: ["'Anita Withers'"]; column header: "'Past Due Age'"; used range: A1:S72
- neighbourhood: I14: 'Green colored columns are automatica... | I15: 'Outstanding Amount' | J15: 'Status' | K15: 'Past Due Age' | L15: 'Selected' | M15: 'PDF' | I16: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 0 | J16: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAID IN FULL' | K16: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> None | L16: '=IFERROR(IF(_xlfn.AGGREGATE(3,5,T_INV3[[#This Row],[Outstanding Am... -> 1 | I17: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 400 | J17: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAST DUE' | K17: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> '91+ Days' | L17: '=IFERROR(IF(_xlfn.AGGREGATE(3,5,T_INV3[[#This Row],[Outstanding Am... -> 1 | I18: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 76.04 | J18: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAST DUE' | K18: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> '91+ Days' | L18: '=IFERROR(IF(_xlfn.AGGREGATE(3,5,T_INV3[[#This Row],[Outstanding Am... -> 1 | M18: '1003 - Mark Mason'

### `e143b38f6648|IFERROR_MASK|Sheet1!B14`

- workbook: `all_data_912_v0.1/spreadsheet/42181/3_42181_input.xlsx`
- location: `Sheet1!B14`  severity: Medium  confidence: Review
- formula: `=SUM(IFERROR(IF(ISNUMBER(FIND(A13,$I$4:$I$10)),VALUE(LEFT($I$4:$I$10,FIND(A13,$I$4:$I$10)-1)),0),0))`
- evidence: Formula uses IFERROR.
- cached value: 3; row labels: ["'Partial Note'"]; column header: ''; used range: A1:I42
- range $I$4:$I$10: values ["'Note (blah blah ...", "'1 Note'", 'None', "'Note'", "'2 Notes'", 'None', 'None']; beyond: {'above': "I3: 'Notes'", 'below': 'I11: None'}
- neighbourhood: A13: 'Note' | B13: '=SUMIF($I$4:$I$10,"*"&A13&"*",$B$4:$B$10)' -> 17 | A14: 'Partial Note' | B14: '=SUM(IFERROR(IF(ISNUMBER(FIND(A13,$I$4:$I$10)),VALUE(LEFT($I$4:$I$... -> 3

### `783ba9a086e8|IFERROR_MASK|OrderSheetFinal!AB6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!AB6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]C5'!$B$57:$K$71,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AB7, Order Sheet Final!AB8, Order Sheet Final!AB9, Order Sheet Final!AB10, Order Sheet Final!AB11, Order Sheet Final!AB12, Order Sheet Final!AB13, Order Sheet Final!AB14, ....
- cached value: 1; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'C5'"; used range: A1:AS37
- neighbourhood: Z4: '=SUM(Z6:Z33)' -> 0 | AA4: '=SUM(AA6:AA33)' -> 0 | AB4: '=SUM(AB6:AB33)' -> 10 | AC4: '=SUM(AC6:AC33)' -> 0 | AD4: '=SUM(AD6:AD33)' -> 0 | Z5: 'C4.1' | AA5: 'C4.2' | AB5: 'C5' | AC5: 'C6.1' | AD5: 'C6.2' | Z6: "=IFERROR(VLOOKUP(B6,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA6: "=IFERROR(VLOOKUP(B6,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB6: "=IFERROR(VLOOKUP(B6,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 1 | AC6: "=IFERROR(VLOOKUP(B6,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD6: "=IFERROR(VLOOKUP(B6,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z7: "=IFERROR(VLOOKUP(B7,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA7: "=IFERROR(VLOOKUP(B7,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB7: "=IFERROR(VLOOKUP(B7,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 1 | AC7: "=IFERROR(VLOOKUP(B7,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD7: "=IFERROR(VLOOKUP(B7,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z8: "=IFERROR(VLOOKUP(B8,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA8: "=IFERROR(VLOOKUP(B8,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB8: "=IFERROR(VLOOKUP(B8,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 0 | AC8: "=IFERROR(VLOOKUP(B8,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD8: "=IFERROR(VLOOKUP(B8,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0

### `74d967658eee|IFERROR_MASK|Sheet1!BF9`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!BF9`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($AF$2:$AF$33,MATCH($BE9,$AG$2:$AG$33,0))," ")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are Sheet1!BF10, Sheet1!BF11, Sheet1!BF12, Sheet1!BF13, Sheet1!BF14, Sheet1!BF15, Sheet1!BF16, Sheet1!BF17, ....
- cached value: None; row labels: ["'90 Avg w/300 Series #8'", "'120 Avg w/400 Series #8'"]; column header: ''; used range: A1:CJ782
- range $AF$2:$AF$33: values ["'AA AB'", "'BB BA'", "'CC CA'", "'DD AD'", "'EE AE'", "'FF AF'", "'GG AG'", "'HH AH'", "'II AI'", "'JJ AJ'", "'KK AK'", "'LL AL'"]; beyond: {'above': "AF1: 'Full Name List'", 'below': 'AF34: None'}
- neighbourhood: BD7: '=IF(BC7="","",SMALL(IF(INDEX($O$2:$O$526,,MATCH(LEFT(BB7,FIND("#",... -> 264 | BE7: '=IFERROR(CEILING(BD7/21,1)," ")' -> 13 | BF7: '=INDEX($AF$2:$AF$33,MATCH($BE7,$AG$2:$AG$33,0))' -> 'MM AM' | BG7: '145 Avg w/500 Series #6' | BH7: '=IFERROR(LARGE($P$2:$P$600,ROW(BH6)),(""))' -> None | BD8: '=IF(BC8="","",SMALL(IF(INDEX($O$2:$O$526,,MATCH(LEFT(BB8,FIND("#",... -> 33 | BE8: '=IFERROR(CEILING(BD8/21,1)," ")' -> 2 | BF8: '=INDEX($AF$2:$AF$33,MATCH($BE8,$AG$2:$AG$33,0))' -> 'BB BA' | BG8: '145 Avg w/500 Series #7' | BH8: '=IFERROR(LARGE($P$2:$P$600,ROW(BH7)),(""))' -> None | BD9: '=IF(BC9="","",SMALL(IF(INDEX($O$2:$O$526,,MATCH(LEFT(BB9,FIND("#",... -> None | BE9: '=IFERROR(CEILING(BD9/21,1)," ")' -> None | BF9: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BE9,$AG$2:$AG$33,0))," ")' -> None | BG9: '145 Avg w/500 Series #8' | BH9: '=IFERROR(LARGE($P$2:$P$600,ROW(BH8)),(""))' -> None | BD10: '=IF(BC10="","",SMALL(IF(INDEX($O$2:$O$526,,MATCH(LEFT(BB10,FIND("#... -> None | BE10: '=IFERROR(CEILING(BD10/21,1)," ")' -> None | BF10: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BE10,$AG$2:$AG$33,0))," ")' -> None | BG10: '145 Avg w/500 Series #9' | BH10: '=IFERROR(LARGE($P$2:$P$600,ROW(BH9)),(""))' -> None | BD11: '=IF(BC11="","",SMALL(IF(INDEX($O$2:$O$526,,MATCH(LEFT(BB11,FIND("#... -> None | BE11: '=IFERROR(CEILING(BD11/21,1)," ")' -> None | BF11: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BE11,$AG$2:$AG$33,0))," ")' -> None | BG11: '145 Avg w/500 Series #10' | BH11: '=IFERROR(LARGE($P$2:$P$600,ROW(BH10)),(""))' -> None

### `125be9ba2e04|IFERROR_MASK|RESULTS1!S29`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!S29`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")>=10,AVERAGEIFS(Table1[POINTS],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Wins'", "'1B <'"]; column header: ''; used range: A1:X80
- neighbourhood: Q27: '100-500M' | R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q28: '500M-1B' | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q29: '1B <' | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `552f4c55b2df|IFERROR_MASK|OrderSheetFinal!AP6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!AP6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,[1]T5!$B$54:$K$63,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AP7, Order Sheet Final!AP8, Order Sheet Final!AP9, Order Sheet Final!AP10, Order Sheet Final!AP11, Order Sheet Final!AP12, Order Sheet Final!AP13, Order Sheet Final!AP14, ....
- cached value: 1; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'T5'"; used range: A1:AS37
- neighbourhood: AN4: '=SUM(AN6:AN33)' -> 8 | AO4: '=SUM(AO6:AO33)' -> 8 | AP4: '=SUM(AP6:AP33)' -> 4 | AQ4: '=SUM(AQ6:AQ33)' -> 0 | AR4: '=SUM(AR6:AR33)' -> 0 | AN5: 'T2' | AO5: 'T3' | AP5: 'T5' | AQ5: 'SG1.1' | AR5: 'SG1.2' | AN6: '=IFERROR(VLOOKUP(B6,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO6: '=IFERROR(VLOOKUP(B6,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP6: '=IFERROR(VLOOKUP(B6,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 1 | AQ6: "=IFERROR(VLOOKUP(B6,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR6: "=IFERROR(VLOOKUP(B6,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0 | AN7: '=IFERROR(VLOOKUP(B7,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO7: '=IFERROR(VLOOKUP(B7,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP7: '=IFERROR(VLOOKUP(B7,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 0 | AQ7: "=IFERROR(VLOOKUP(B7,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR7: "=IFERROR(VLOOKUP(B7,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0 | AN8: '=IFERROR(VLOOKUP(B8,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO8: '=IFERROR(VLOOKUP(B8,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP8: '=IFERROR(VLOOKUP(B8,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 1 | AQ8: "=IFERROR(VLOOKUP(B8,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR8: "=IFERROR(VLOOKUP(B8,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0

### `86bd0c65882c|IFERROR_MASK|Sheet1!K5`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!K5`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($S$2:$S$124,MATCH($A5,$Q$2:$Q124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 78; row labels: []; column header: ''; used range: A1:BE279
- range $S$2:$S$124: values ['75', '76', '91', '78', '79', '87', '85', '82', '81', '88', '75', '76']; beyond: {'above': "S1: 'Age'", 'below': 'S125: None'}
- neighbourhood: J3: '=IFERROR(INDEX($R$2:$R$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 1944-04-11 00:00:00 | K3: '=IFERROR(INDEX($S$2:$S$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 76 | L3: '=IF(K3<85,"75-84",">85")' -> '75-84' | M3: '=IFERROR(INDEX($T$2:$T$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 'Male' | J4: '=IFERROR(INDEX($R$2:$R$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 1930-06-17 00:00:00 | K4: '=IFERROR(INDEX($S$2:$S$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 91 | L4: '=IF(K4<85,"75-84",">85")' -> '>85' | M4: '=IFERROR(INDEX($T$2:$T$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 'Female' | J5: '=IFERROR(INDEX($R$2:$R$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 1942-07-08 00:00:00 | K5: '=IFERROR(INDEX($S$2:$S$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 78 | L5: '=IF(K5<85,"75-84",">85")' -> '75-84' | M5: '=IFERROR(INDEX($T$2:$T$124,MATCH($A5,$Q$2:$Q124,0)),0)' -> 'Male' | J6: '=IFERROR(INDEX($R$2:$R$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 1941-10-15 00:00:00 | K6: '=IFERROR(INDEX($S$2:$S$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 79 | L6: '=IF(K6<85,"75-84",">85")' -> '75-84' | M6: '=IFERROR(INDEX($T$2:$T$124,MATCH($A6,$Q$2:$Q124,0)),0)' -> 'Female' | J7: '=IFERROR(INDEX($R$2:$R$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 1934-01-27 00:00:00 | K7: '=IFERROR(INDEX($S$2:$S$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 87 | L7: '=IF(K7<85,"75-84",">85")' -> '>85' | M7: '=IFERROR(INDEX($T$2:$T$124,MATCH($A7,$Q$2:$Q124,0)),0)' -> 'Male'

### `95fdf876027b|IFERROR_MASK|RESULTS1!T4`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!T4`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5x20",IF((Table1[WEEK]>=MAX(Table1[WEEK])-9),Table1[POINTS]))),10%),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Last 10 Wk '"]; column header: ''; used range: A1:X80
- neighbourhood: R2: '>= 4' | S2: '>= 5' | T2: '>= 6' | U2: '>= 7' | V2: '>= 8' | R3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None

### `f97f2feedd64|IFERROR_MASK|RESULTS1!V15`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!V15`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000"),0)`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: ["'ANNUALIZED GAIN CALCULATOR'", "'< 100M'"]; column header: "'50-100M'"; used range: A1:W67
- neighbourhood: T14: '10-20M' | U14: '20-50M' | V14: '50-100M' | W14: '100M <' | T15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 3 | U15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 1 | V15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | W15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 0 | T16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 5 | U16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 9 | V16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 3 | W16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 1 | T17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | U17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | V17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | W17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 1

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!W8`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!W8`  severity: Medium  confidence: Review
- formula: `=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=200%",Table1[SETUP],$P8),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are RESULTS 1!W9, RESULTS 1!W10, RESULTS 1!W11, RESULTS 1!W12.
- cached value: 0; row labels: ["'PMH'"]; column header: "'200% <'"; used range: A1:W67
- neighbourhood: U7: '100-150%' | V7: '150-200%' | W7: '200% <' | U8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0 | W8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=200%"... -> 0 | U9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0 | W9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=200%"... -> 0 | U10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | V10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=150%"... -> 0 | W10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=200%"... -> 0

### `afc2b280227b|IFERROR_MASK|Sheet1!B14`

- workbook: `all_data_912_v0.1/spreadsheet/42181/1_42181_input.xlsx`
- location: `Sheet1!B14`  severity: Medium  confidence: Review
- formula: `=SUM(IFERROR(IF(ISNUMBER(FIND(A13,$I$4:$I$10)),VALUE(LEFT($I$4:$I$10,FIND(A13,$I$4:$I$10)-1)),0),0))`
- evidence: Formula uses IFERROR.
- cached value: 3; row labels: ["'Partial Note'"]; column header: ''; used range: A1:I42
- range $I$4:$I$10: values ["'Note (blah blah ...", "'1 Note'", 'None', "'Note'", "'2 Notes'", 'None', 'None']; beyond: {'above': "I3: 'Notes'", 'below': 'I11: None'}
- neighbourhood: A13: 'Note' | B13: '=SUMIF($I$4:$I$10,"*"&A13&"*",$B$4:$B$10)' -> 10 | A14: 'Partial Note' | B14: '=SUM(IFERROR(IF(ISNUMBER(FIND(A13,$I$4:$I$10)),VALUE(LEFT($I$4:$I$... -> 3

### `86bd0c65882c|IFERROR_MASK|Sheet1!E8`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!E8`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($AG$2:$AG$124,MATCH($A8,$AA$2:$AA124,0)),0)`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:BE279
- range $AG$2:$AG$124: values ['13', '6', '1', '3', '2', '3', '2', '6', '8', '3', '2', '1']; beyond: {'above': "AG1: 'LoS'", 'below': 'AG125: None'}
- neighbourhood: D6: '=IF(COUNTIF(AF6,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E6: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A6,$AA$2:$AA124,0)),0)' -> 0 | F6: '=IF(E6>14,E6,"N/A")' -> 'N/A' | D7: '=IF(COUNTIF(AF7,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E7: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A7,$AA$2:$AA124,0)),0)' -> 0 | F7: '=IF(E7>14,E7,"N/A")' -> 'N/A' | D8: '=IF(COUNTIF(AF8,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E8: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A8,$AA$2:$AA124,0)),0)' -> 0 | F8: '=IF(E8>14,E8,"N/A")' -> 'N/A' | D9: '=IF(COUNTIF(AF9,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E9: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A9,$AA$2:$AA124,0)),0)' -> 0 | F9: '=IF(E9>14,E9,"N/A")' -> 'N/A' | D10: '=IF(COUNTIF(AF10,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E10: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A10,$AA$2:$AA124,0)),0)' -> 0 | F10: '=IF(E10>14,E10,"N/A")' -> 'N/A'

### `70420e2dcf7b|IFERROR_MASK|PAYMENT!B4`

- workbook: `all_data_912_v0.1/spreadsheet/49490/1_49490_input.xlsx`
- location: `PAYMENT!B4`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"60*90")`
- evidence: Formula uses IFERROR.
- cached value: '60*90'; row labels: []; column header: "'SIZE'"; used range: A1:L1001
- neighbourhood: B2: 'TOTAL PCS' | A3: 'TYPE' | B3: 'SIZE' | C3: 'STITCHING' | D3: 'PURPOSE' | A4: '=IFERROR(__xludf.DUMMYFUNCTION("sort(unique(Sheet1!F3:I1001))"),"B... -> 'BEDCOVER' | B4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"60*90")' -> '60*90' | C4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),FALSE)' -> False | D4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | A5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"BEDCOVER")' -> 'BEDCOVER' | B5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"90*100")' -> '90*100' | C5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NEW NAKSHI")' -> 'NEW NAKSHI' | D5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | A6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")' -> 'PILLOW' | C6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"SINGLE")' -> 'SINGLE' | D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING'

### `6741b8e20874|IFERROR_MASK|OrderSheetFinal!AQ6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!AQ6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AQ7, Order Sheet Final!AQ8, Order Sheet Final!AQ9, Order Sheet Final!AQ10, Order Sheet Final!AQ11, Order Sheet Final!AQ12, Order Sheet Final!AQ13, Order Sheet Final!AQ14, ....
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'SG1.1'"; used range: A1:AS37
- neighbourhood: AO4: '=SUM(AO6:AO33)' -> 8 | AP4: '=SUM(AP6:AP33)' -> 4 | AQ4: '=SUM(AQ6:AQ33)' -> 0 | AR4: '=SUM(AR6:AR33)' -> 0 | AS4: '=SUM(AS6:AS33)' -> 268 | AO5: 'T3' | AP5: 'T5' | AQ5: 'SG1.1' | AR5: 'SG1.2' | AS5: 'Total' | AO6: '=IFERROR(VLOOKUP(B6,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP6: '=IFERROR(VLOOKUP(B6,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 1 | AQ6: "=IFERROR(VLOOKUP(B6,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR6: "=IFERROR(VLOOKUP(B6,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0 | AS6: '=SUM(E6:AR6)' -> 3 | AO7: '=IFERROR(VLOOKUP(B7,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP7: '=IFERROR(VLOOKUP(B7,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 0 | AQ7: "=IFERROR(VLOOKUP(B7,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR7: "=IFERROR(VLOOKUP(B7,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0 | AS7: '=SUM(E7:AR7)' -> 17 | AO8: '=IFERROR(VLOOKUP(B8,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AP8: '=IFERROR(VLOOKUP(B8,[1]T5!$B$54:$K$63,10,FALSE),0)' -> 1 | AQ8: "=IFERROR(VLOOKUP(B8,'[1]SG1.1'!$B$51:$K$54,10,FALSE),0)" -> 0 | AR8: "=IFERROR(VLOOKUP(B8,'[1]SG1.2'!$B$51:$K$55,10,FALSE),0)" -> 0 | AS8: '=SUM(E8:AR8)' -> 2

### `552f4c55b2df|IFERROR_MASK|OrderSheetFinal!K6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!K6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,[1]S2!$B$58:$K$71,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!K7, Order Sheet Final!K8, Order Sheet Final!K9, Order Sheet Final!K10, Order Sheet Final!K11, Order Sheet Final!K12, Order Sheet Final!K13, Order Sheet Final!K14, ....
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'S2'"; used range: A1:AS37
- neighbourhood: I4: '=SUM(I6:I33)' -> 20 | J4: '=SUM(J6:J33)' -> 7 | K4: '=SUM(K6:K33)' -> 0 | L4: '=SUM(L6:L33)' -> 0 | M4: '=SUM(M6:M33)' -> 21 | I5: 'P4' | J5: 'S1' | K5: 'S2' | L5: 'S3' | M5: 'S4.1' | I6: '=IFERROR(VLOOKUP(B6,[1]P4!$B$58:$K$72,10,FALSE),0)' -> 0 | J6: '=IFERROR(VLOOKUP(B6,[1]S1!$B$55:$K$63,10,FALSE),0)' -> 0 | K6: '=IFERROR(VLOOKUP(B6,[1]S2!$B$58:$K$71,10,FALSE),0)' -> 0 | L6: '=IFERROR(VLOOKUP(B6,[1]S3!$B$58:$K$65,10,FALSE),0)' -> 0 | M6: "=IFERROR(VLOOKUP(B6,'[1]S4.1'!$B$58:$K$71,10,FALSE),0)" -> 0 | I7: '=IFERROR(VLOOKUP(B7,[1]P4!$B$58:$K$72,10,FALSE),0)' -> 3 | J7: '=IFERROR(VLOOKUP(B7,[1]S1!$B$55:$K$63,10,FALSE),0)' -> 0 | K7: '=IFERROR(VLOOKUP(B7,[1]S2!$B$58:$K$71,10,FALSE),0)' -> 0 | L7: '=IFERROR(VLOOKUP(B7,[1]S3!$B$58:$K$65,10,FALSE),0)' -> 0 | M7: "=IFERROR(VLOOKUP(B7,'[1]S4.1'!$B$58:$K$71,10,FALSE),0)" -> 4 | I8: '=IFERROR(VLOOKUP(B8,[1]P4!$B$58:$K$72,10,FALSE),0)' -> 0 | J8: '=IFERROR(VLOOKUP(B8,[1]S1!$B$55:$K$63,10,FALSE),0)' -> 0 | K8: '=IFERROR(VLOOKUP(B8,[1]S2!$B$58:$K$71,10,FALSE),0)' -> 0 | L8: '=IFERROR(VLOOKUP(B8,[1]S3!$B$58:$K$65,10,FALSE),0)' -> 0 | M8: "=IFERROR(VLOOKUP(B8,'[1]S4.1'!$B$58:$K$71,10,FALSE),0)" -> 0

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!Q36`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!Q36`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000")>=10,AVERAGEIFS(Table1[POINTS G/L],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'PM Trades %'", "'1B <'"]; column header: ''; used range: A1:W67
- neighbourhood: P34: '100-500M' | Q34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P35: '500M-1B' | Q35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P36: '1B <' | Q36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `783ba9a086e8|IFERROR_MASK|OrderSheetFinal!AF6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!AF6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]C9'!$B$54:$K$64,10,FALSE),0)`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AF7, Order Sheet Final!AF8, Order Sheet Final!AF9, Order Sheet Final!AF10, Order Sheet Final!AF11, Order Sheet Final!AF12, Order Sheet Final!AF13, Order Sheet Final!AF14, ....
- cached value: 1; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'C9'"; used range: A1:AS37
- neighbourhood: AD4: '=SUM(AD6:AD33)' -> 0 | AE4: '=SUM(AE6:AE33)' -> 10 | AF4: '=SUM(AF6:AF33)' -> 4 | AG4: '=SUM(AG6:AG33)' -> 9 | AH4: '=SUM(AH6:AH33)' -> 0 | AD5: 'C6.2' | AE5: 'C7' | AF5: 'C9' | AG5: 'C11' | AH5: 'C12' | AD6: "=IFERROR(VLOOKUP(B6,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE6: "=IFERROR(VLOOKUP(B6,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF6: "=IFERROR(VLOOKUP(B6,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 1 | AG6: "=IFERROR(VLOOKUP(B6,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AH6: "=IFERROR(VLOOKUP(B6,'[1]C12'!$B$55:$K$64,10,FALSE),0)" -> 0 | AD7: "=IFERROR(VLOOKUP(B7,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE7: "=IFERROR(VLOOKUP(B7,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 2 | AF7: "=IFERROR(VLOOKUP(B7,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 0 | AG7: "=IFERROR(VLOOKUP(B7,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AH7: "=IFERROR(VLOOKUP(B7,'[1]C12'!$B$55:$K$64,10,FALSE),0)" -> 0 | AD8: "=IFERROR(VLOOKUP(B8,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE8: "=IFERROR(VLOOKUP(B8,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF8: "=IFERROR(VLOOKUP(B8,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 1 | AG8: "=IFERROR(VLOOKUP(B8,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AH8: "=IFERROR(VLOOKUP(B8,'[1]C12'!$B$55:$K$64,10,FALSE),0)" -> 0

### `95fdf876027b|IFERROR_MASK|RESULTS1!X14`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!X14`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">100000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],"<100000000",Table1[FLOAT],">100000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Max stop loss for entry price < 20 is 30c, > 20 is 50c'", "'< 100M'"]; column header: "'100M <'"; used range: A1:X80
- neighbourhood: V13: '20-50M' | W13: '50-100M' | X13: '100M <' | V14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | X15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `40815e616aca|IFERROR_MASK|Sheet1!G4`

- workbook: `all_data_912_v0.1/spreadsheet/41410/2_41410_input.xlsx`
- location: `Sheet1!G4`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$22="Lighting"),ROWS(G$4:G4))),"")`
- evidence: Formula uses IFERROR.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are Sheet1!H4, Sheet1!G5, Sheet1!H5.
- cached value: 5; row labels: ["'Lighting'", "'Lighting'"]; column header: "'kW rating'"; used range: A1:H22
- range $B$4:$B$22: values ["'Lighting'", "'Cooling'", "'Cooling'", "'Lighting'", "'Heating'", "'Other'", "'Lighting'", "'Heating'", "'Lighting'", "'Other'", 'None', 'None']; beyond: {'above': "B3: 'Item'", 'below': 'B23: None'}
- neighbourhood: F2: 'Output:' | F3: 'Item' | G3: 'kW rating' | H3: 'Number' | F4: 'Lighting' | G4: '=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 5 | H4: '=IFERROR(INDEX(D:D,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 2 | F5: 'Lighting' | G5: '=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 0.05 | H5: '=IFERROR(INDEX(D:D,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 10

### `750361651608|IFERROR_MASK|PAYMENT!C4`

- workbook: `all_data_912_v0.1/spreadsheet/49490/3_49490_input.xlsx`
- location: `PAYMENT!C4`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),FALSE)`
- evidence: Formula uses IFERROR.
- cached value: False; row labels: []; column header: "'STITCHING'"; used range: A1:L1001
- neighbourhood: B2: 'TOTAL PCS' | E2: '=SUM(E4:E1001)' -> 315 | A3: 'TYPE' | B3: 'SIZE' | C3: 'STITCHING' | D3: 'PURPOSE' | E3: 'PCS' | A4: '=IFERROR(__xludf.DUMMYFUNCTION("sort(unique(Sheet1!F3:I1001))"),"B... -> 'BEDCOVER' | B4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"60*90")' -> '60*90' | C4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),FALSE)' -> False | D4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E4: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | A5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"BEDCOVER")' -> 'BEDCOVER' | B5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"90*100")' -> '90*100' | C5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NEW NAKSHI")' -> 'NEW NAKSHI' | D5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E5: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 105 | A6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")' -> 'PILLOW' | C6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"SINGLE")' -> 'SINGLE' | D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 210

## LITERAL_CONSTANT

### `ecefab75d6ce|LITERAL_CONSTANT|Calendar!B93`

- workbook: `all_data_912_v0.1/spreadsheet/57716/1_57716_input.xlsx`
- location: `Calendar!B93`  severity: Medium  confidence: Review
- formula: `=Days+22+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(Calendar7Year,Calendar7MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 22.
- cached value: 2020-10-19 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B91: '=Days+15+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(C... -> 2020-10-12 00:00:00 | C91: 2020-10-13 00:00:00 | D91: 2020-10-14 00:00:00 | B93: '=Days+22+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(C... -> 2020-10-19 00:00:00 | C93: 2020-10-20 00:00:00 | D93: 2020-10-21 00:00:00 | B95: '=Days+29+DATE(Calendar7Year,Calendar7MonthOption,1)-WEEKDAY(DATE(C... -> 2020-10-26 00:00:00 | C95: 2020-10-27 00:00:00 | D95: 2020-10-28 00:00:00

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B121`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B121`  severity: Medium  confidence: Review
- formula: `=Days+22+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(Calendar9Year,Calendar9MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 22.
- cached value: 2020-12-21 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B119: '=Days+15+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-14 00:00:00 | C119: 2020-12-15 00:00:00 | D119: 2020-12-16 00:00:00 | B121: '=Days+22+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-21 00:00:00 | C121: 2020-12-22 00:00:00 | D121: 2020-12-23 00:00:00 | B123: '=Days+29+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-28 00:00:00 | C123: 2020-12-29 00:00:00 | D123: 2020-12-30 00:00:00

### `c2c1c9ef2579|LITERAL_CONSTANT|formamspnc(7)!D5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!D5`  severity: Medium  confidence: Review
- formula: `=COUNTIF(F5:F11,3)`
- evidence: Non-trivial numeric literal(s) found: 3.
- cached value: 3; row labels: ["'1 ext,1st 1 ext'"]; column header: "'count of 3'"; used range: A1:ED48610
- range F5:F11: values ['None', '3', '5', 'None', '4', '3', '3']; beyond: {'above': "F4: 'vs prim than prim vs all'", 'below': 'F12: None'}
- neighbourhood: B3: 1 | C3: -1 | D3: 1 | F3: 0 | B4: 'count of 1' | C4: 'count of 2' | D4: 'count of 3' | F4: 'vs prim than prim vs all' | B5: '=COUNTIF(F5:F11,1)' -> 0 | C5: '=COUNTIF(F5:F11,2)' -> 0 | D5: '=COUNTIF(F5:F11,3)' -> 3 | C6: '=MID(A6,FIND("(",A6)+1,FIND(")",A6)-FIND("(",A6)-1)' -> '1 ext 1u/1d,1st of alm atcl7' | F6: '=IF(EB6=0,"",EB6)' -> 3 | C7: '=MID(A7,FIND("(",A7)+1,FIND(")",A7)-FIND("(",A7)-1)' -> '1pt 1u/2d,1st alm a3/a5' | F7: '=IF(EB7=0,"",EB7)' -> 5

### `47eb61dd533e|LITERAL_CONSTANT|TEST!I9`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!I9`  severity: Medium  confidence: Review
- formula: `=7350-4821.71`
- evidence: Non-trivial numeric literal(s) found: 7350, 4821.71.
- cached value: 2528.29; row labels: ["'Current Balance'"]; column header: ''; used range: A1:S1004
- neighbourhood: G7: '=B7' -> 1500.7 | H7: '=G7*0.1' -> 150.07 | I7: 1513.65 | J7: 'W' | K7: '=IF(J7=0,G7,IF(J7="W",G7+I7,G7-H7))' -> 3014.35 | G8: '=K7' -> 3014.35 | H8: '=IF(G8<30000,G8*0.1,3000)' -> 301.435 | I8: 1807.36 | J8: 'W' | K8: '=IF(J8=0,G8,IF(J8="W",G8+I8,G8-H8))' -> 4821.71 | G9: '=K8' -> 4821.71 | H9: 538.55 | I9: '=7350-4821.71' -> 2528.29 | J9: 'W' | K9: '=IF(J9=0,G9,IF(J9="W",G9+I9,G9-H9))' -> 7350 | G10: '=K9' -> 7350 | H10: '=350' -> 350 | I10: '=2721.97' -> 2721.97 | K10: '=IF(J10=0,G10,IF(J10="W",G10+I10,G10-H10))' -> 7350 | G11: '=K10' -> 7350 | H11: '=IF(G11<30000,G11*0.1,3000)' -> 735 | K11: '=IF(J11=0,G11,IF(J11="W",G11+I11,G11-H11))' -> 7350

### `e239b7cffe03|LITERAL_CONSTANT|Sheet2!B15`

- workbook: `all_data_912_v0.1/spreadsheet/32562/3_32562_input.xlsx`
- location: `Sheet2!B15`  severity: Medium  confidence: Review
- formula: `=COUNTIF(A15:A21,86)`
- evidence: Non-trivial numeric literal(s) found: 86.
- cached value: 0; row labels: []; column header: ''; used range: A1:B21
- range A15:A21: values ['374', '321', '321', '321', '9', '141', '109']; beyond: {'above': 'A14: 374', 'below': 'A22: None'}
- neighbourhood: A13: 374 | B13: '=COUNTIF(A13:A21,86)' -> 0 | A14: 374 | B14: '=COUNTIF(A14:A21,86)' -> 0 | A15: 374 | B15: '=COUNTIF(A15:A21,86)' -> 0 | A16: 321 | B16: '=COUNTIF(A16:A21,86)' -> 0 | A17: 321 | B17: '=COUNTIF(A17:A21,86)' -> 0

### `7bd972dd1e37|LITERAL_CONSTANT|July-KPIs!E6`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!E6`  severity: Medium  confidence: Review
- formula: `=IFERROR(((C6*1.3)+(D6*1))/((B6)),"0")`
- evidence: Non-trivial numeric literal(s) found: 1.3.
- evidence: The same relative formula appears in 31 cells on this sheet; the others are July-KPIs!E7, July-KPIs!E8, July-KPIs!E9, July-KPIs!E10, July-KPIs!E11, July-KPIs!E12, July-KPIs!E13, July-KPIs!E14, ....
- cached value: '0'; row labels: []; column header: "'Total Daily'"; used range: A1:T3212
- neighbourhood: C4: 'Calls Target' | F4: 'Summary' | C5: 'Inbound' | D5: 'Outbound' | E5: 'Total Daily' | E6: '=IFERROR(((C6*1.3)+(D6*1))/((B6)),"0")' -> '0' | F6: '=VLOOKUP(C1,#REF!,2,0)' -> '#REF!' | E7: '=IFERROR(((C7*1.3)+(D7*1))/((B7)),"0")' -> '0' | E8: '=IFERROR(((C8*1.3)+(D8*1))/((B8)),"0")' -> '0'

### `31acc3fe427b|LITERAL_CONSTANT|Holiday4FEB21-31MAR21!B6`

- workbook: `all_data_912_v0.1/spreadsheet/55883/2_55883_input.xlsx`
- location: `Holiday 4FEB21 - 31MAR21!B6`  severity: Medium  confidence: Review
- formula: `=SUM(3.5-C6)`
- evidence: Non-trivial numeric literal(s) found: 3.5.
- cached value: 0; row labels: ["'Natalie'"]; column header: ''; used range: A1:NU42
- neighbourhood: A4: 'Alex' | B4: '=SUM(2.5-C4)' -> 0 | C4: '=COUNTIF(E4:NE4,"H")+COUNTIF(E4:NE4,"HD")/2' -> 2.5 | D4: '=COUNTIF(E4:NE4,"S")' -> 0 | A5: 'Dale' | B5: '=SUM(3-C5)' -> 0 | C5: '=COUNTIF(E5:NE5,"H")+COUNTIF(E5:NE5,"HD")/2' -> 3 | D5: '=COUNTIF(E5:NE5,"S")' -> 0 | A6: 'Natalie' | B6: '=SUM(3.5-C6)' -> 0 | C6: '=COUNTIF(E6:NE6,"H")+COUNTIF(E6:NE6,"HD")/2' -> 3.5 | D6: '=COUNTIF(E6:NE6,"S")' -> 0 | A7: 'Dan' | B7: '=SUM(0-C7)' -> 0 | C7: '=COUNTIF(E7:NE7,"H")+COUNTIF(E7:NE7,"HD")/2' -> 0 | D7: '=COUNTIF(E7:NE7,"S")' -> 0

### `47eb61dd533e|LITERAL_CONSTANT|TEST!H10`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!H10`  severity: Medium  confidence: Review
- formula: `=350`
- evidence: Non-trivial numeric literal(s) found: 350.
- cached value: 350; row labels: ["'Goal'"]; column header: ''; used range: A1:S1004
- neighbourhood: F8: '=F7+1' -> 2021-04-06 00:00:00 | G8: '=K7' -> 3014.35 | H8: '=IF(G8<30000,G8*0.1,3000)' -> 301.435 | I8: 1807.36 | J8: 'W' | F9: '=F8+1' -> 2021-04-07 00:00:00 | G9: '=K8' -> 4821.71 | H9: 538.55 | I9: '=7350-4821.71' -> 2528.29 | J9: 'W' | F10: '=F9+1' -> 2021-04-08 00:00:00 | G10: '=K9' -> 7350 | H10: '=350' -> 350 | I10: '=2721.97' -> 2721.97 | F11: '=F10+1' -> 2021-04-09 00:00:00 | G11: '=K10' -> 7350 | H11: '=IF(G11<30000,G11*0.1,3000)' -> 735 | F12: '=F11+1' -> 2021-04-10 00:00:00 | G12: '=K11' -> 7350 | H12: '=IF(G12<30000,G12*0.1,3000)' -> 735

### `74d967658eee|LITERAL_CONSTANT|Sheet1!Y5`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!Y5`  severity: Medium  confidence: Review
- formula: `=IF(AND(I4>=12,G5>0),SUM(ROUNDDOWN(SUM(200-J4)*0.9,0)*3)+X5,"0")`
- evidence: Non-trivial numeric literal(s) found: 200, 3.
- evidence: The same relative formula appears in 346 cells on this sheet; the others are Sheet1!Y6, Sheet1!Y7, Sheet1!Y8, Sheet1!Y9, Sheet1!Y10, Sheet1!Y11, Sheet1!Y12, Sheet1!Y13, ....
- cached value: '0'; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: W3: '=IF(AND(I2>=12,G3>0),ROUNDDOWN(SUM(200-J2)*0.9,0)+V3," ")' -> None | X3: '=SUM(G3)' -> 291 | Y3: '=IF(AND(I2>=12,G3>0),SUM(ROUNDDOWN(SUM(200-J2)*0.9,0)*3)+X3," ")' -> None | AA3: 'High Scratch Game #2' | W4: '=IF(AND(I3>=12,G4>0),ROUNDDOWN(SUM(200-J3)*0.9,0)+V4," ")' -> None | X4: '=SUM(G4)' -> 372 | Y4: '=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")' -> None | AA4: 'High Scratch Game #3' | W5: '=IF(AND(I4>=12,G5>0),ROUNDDOWN(SUM(200-J4)*0.9,0)+V5," ")' -> None | X5: '=SUM(G5)' -> 0 | Y5: '=IF(AND(I4>=12,G5>0),SUM(ROUNDDOWN(SUM(200-J4)*0.9,0)*3)+X5,"0")' -> '0' | AA5: 'High Scratch Game #4' | W6: '=IF(AND(I5>=12,G6>0),ROUNDDOWN(SUM(200-J5)*0.9,0)+V6," ")' -> None | X6: '=SUM(G6)' -> 340 | Y6: '=IF(AND(I5>=12,G6>0),SUM(ROUNDDOWN(SUM(200-J5)*0.9,0)*3)+X6,"0")' -> '0' | AA6: 'High Scratch Game #5' | W7: '=IF(AND(I6>=12,G7>0),ROUNDDOWN(SUM(200-J6)*0.9,0)+V7,"0")' -> '0' | X7: '=SUM(G7)' -> 302 | Y7: '=IF(AND(I6>=12,G7>0),SUM(ROUNDDOWN(SUM(200-J6)*0.9,0)*3)+X7,"0")' -> '0' | AA7: 'High Scratch Game #6'

### `902b5e29897a|LITERAL_CONSTANT|LeadTimes!B6`

- workbook: `all_data_912_v0.1/spreadsheet/47741/1_47741_input.xlsx`
- location: `Lead Times!B6`  severity: Medium  confidence: Review
- formula: `=WORKDAY(B4,18,K14:K21)`
- evidence: Non-trivial numeric literal(s) found: 18.
- cached value: 2022-01-21 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range K14:K21: values ['2021-12-31 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None']; beyond: {'above': 'K13: None', 'below': 'K22: None'}
- neighbourhood: B4: '=INDEX(calendar,ndx+0) {array B4:H4}' -> 2021-12-27 00:00:00 | C4: 2021-12-28 00:00:00 | D4: 2021-12-29 00:00:00 | B5: '=_xlfn.TEXTJOIN("-",,WORKDAY(B4,10,K14:K20),WORKDAY(B4,12,K14:K20))' -> '44572-44574' | C5: '=WORKDAY(C4,10,L14:L20)' -> 2022-01-12 00:00:00 | D5: '=WORKDAY(D4,10,M14:M20)' -> 2022-01-13 00:00:00 | B6: '=WORKDAY(B4,18,K14:K21)' -> 2022-01-21 00:00:00 | C6: '=WORKDAY(C4,18,L15:L21)' -> 2022-01-21 00:00:00 | D6: '=WORKDAY(D4,18,M15:M21)' -> 2022-01-24 00:00:00 | B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22' | B8: '=INDEX(calendar,ndx+1) {array B8:H8}' -> 2022-01-03 00:00:00 | C8: 2022-01-04 00:00:00 | D8: 2022-01-05 00:00:00

### `125be9ba2e04|LITERAL_CONSTANT|RESULTS1!T4`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!T4`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5x20",IF((Table1[WEEK]>=MAX(Table1[WEEK])-9),Table1[POINTS]))),10%),"")`
- evidence: Non-trivial numeric literal(s) found: 6, 9.
- cached value: None; row labels: ["'Last 10 Wk '"]; column header: ''; used range: A1:X80
- neighbourhood: R2: '>= 4' | S2: '>= 5' | T2: '>= 6' | U2: '>= 7' | V2: '>= 8' | R3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF(Table1[EXIT REASON]="5... -> None

### `e239b7cffe03|LITERAL_CONSTANT|Sheet2!B20`

- workbook: `all_data_912_v0.1/spreadsheet/32562/3_32562_input.xlsx`
- location: `Sheet2!B20`  severity: Medium  confidence: Review
- formula: `=COUNTIF(A20:A21,86)`
- evidence: Non-trivial numeric literal(s) found: 86.
- cached value: 0; row labels: []; column header: ''; used range: A1:B21
- range A20:A21: values ['141', '109']; beyond: {'above': 'A19: 9', 'below': 'A22: None'}
- neighbourhood: A18: 321 | B18: '=COUNTIF(A18:A21,86)' -> 0 | A19: 9 | B19: '=COUNTIF(A19:A21,86)' -> 0 | A20: 141 | B20: '=COUNTIF(A20:A21,86)' -> 0 | A21: 109 | B21: '=COUNTIF(A21:A21,86)' -> 0

### `125be9ba2e04|LITERAL_CONSTANT|RESULTS1!S4`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!S4`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5x20",IF((Table1[WEEK]>=MAX(Table1[WEEK])-9),Table1[POINTS]))),10%),"")`
- evidence: Non-trivial numeric literal(s) found: 5, 9.
- cached value: None; row labels: ["'Last 10 Wk '"]; column header: ''; used range: A1:X80
- neighbourhood: Q2: 'MEAN G/L' | R2: '>= 4' | S2: '>= 5' | T2: '>= 6' | U2: '>= 7' | Q3: 'All-TIME (5)' | R3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U3: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | Q4: 'Last 10 Wk ' | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None | Q5: 'Last 5 Wk' | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF(Table1[EXIT REASON]="5... -> None | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF(Table1[EXIT REASON]="5... -> None | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF(Table1[EXIT REASON]="5... -> None | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF(Table1[EXIT REASON]="5... -> None

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!R30`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!R30`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")/COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Points % /s (Net)'", "'1B <'"]; column header: ''; used range: A1:W67
- neighbourhood: P28: '100-500M' | Q28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P29: '500M-1B' | Q29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P30: '1B <' | Q30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | P32: 'POINTS' | Q32: '1-3M' | R32: '3-5M' | S32: '5-10M' | T32: '10-20M'

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B39`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B39`  severity: Medium  confidence: Review
- formula: `=Days+29+DATE(Calendar3Year,Calendar3MonthOption,1)-WEEKDAY(DATE(Calendar3Year,Calendar3MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 29.
- cached value: 2020-06-29 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B37: '=Days+22+DATE(Calendar3Year,Calendar3MonthOption,1)-WEEKDAY(DATE(C... -> 2020-06-22 00:00:00 | C37: 2020-06-23 00:00:00 | D37: 2020-06-24 00:00:00 | B39: '=Days+29+DATE(Calendar3Year,Calendar3MonthOption,1)-WEEKDAY(DATE(C... -> 2020-06-29 00:00:00 | C39: 2020-06-30 00:00:00 | D39: 2020-07-01 00:00:00 | B41: '=Days+36+DATE(Calendar3Year,Calendar3MonthOption,1)-WEEKDAY(DATE(C... -> 2020-07-06 00:00:00 | C41: 2020-07-07 00:00:00 | D41: 'Notes:'

### `5cd8c4fe9805|LITERAL_CONSTANT|RESULTS1!R17`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!R17`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=30000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'1B <'"]; column header: ''; used range: A1:X80
- neighbourhood: Q15: '100-500M' | R15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q16: '500M-1B' | R16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q17: '1B <' | R17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | Q19: 'WIN % (10)' | R19: '1-3M' | S19: '3-5M' | T19: '5-10M'

### `c9ce3280a26d|LITERAL_CONSTANT|Sheet1!A7`

- workbook: `all_data_912_v0.1/spreadsheet/43406/1_43406_input.xlsx`
- location: `Sheet1!A7`  severity: Medium  confidence: Review
- formula: `=ROW(A7)-6`
- evidence: Non-trivial numeric literal(s) found: 6.
- evidence: The same relative formula appears in 14 cells on this sheet; the others are Sheet1!A8, Sheet1!A9, Sheet1!A10, Sheet1!A11, Sheet1!A12, Sheet1!A13, Sheet1!A14, Sheet1!A15, ....
- cached value: 1; row labels: []; column header: "'ROW'"; used range: A1:F20
- neighbourhood: A6: 'ROW' | B6: 'HELPER' | C6: "What I'd like to see" | A7: '=ROW(A7)-6' -> 1 | C7: 1 | A8: '=ROW(A8)-6' -> 2 | C8: 1.1 | A9: '=ROW(A9)-6' -> 3 | C9: 1.2

### `c2c1c9ef2579|LITERAL_CONSTANT|formamspnc(7)!DD6`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!DD6`  severity: Medium  confidence: Review
- formula: `=IF(AND(DO6=1,DP6=1,DQ6=1),3,"")`
- evidence: Non-trivial numeric literal(s) found: 3.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are formamspnc (7)!DD7, formamspnc (7)!DD8, formamspnc (7)!DD9, formamspnc (7)!DD10, formamspnc (7)!DD11.
- cached value: 3; row labels: ["'13c/15c/18c/21c/23c/25c/33c/35c/39c/44c/49c/51c/55c/59c/...", "'e'"]; column header: ''; used range: A1:ED48610
- neighbourhood: DD6: '=IF(AND(DO6=1,DP6=1,DQ6=1),3,"")' -> 3 | DE6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1),4,"")' -> None | DF6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1,DS6=1),5,"")' -> None | DD7: '=IF(AND(DO7=1,DP7=1,DQ7=1),3,"")' -> 3 | DE7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1),4,"")' -> None | DF7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1,DS7=1),5,"")' -> None | DD8: '=IF(AND(DO8=1,DP8=1,DQ8=1),3,"")' -> None | DE8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1),4,"")' -> None | DF8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1,DS8=1),5,"")' -> None

### `36080f34a91e|LITERAL_CONSTANT|Calendar!B145`

- workbook: `all_data_912_v0.1/spreadsheet/57716/2_57716_input.xlsx`
- location: `Calendar!B145`  severity: Medium  confidence: Review
- formula: `=Days+8+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(Calendar11Year,Calendar11MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 8.
- cached value: 2021-02-08 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B143: '=Days+1+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(... -> 2021-02-01 00:00:00 | C143: 2021-02-02 00:00:00 | D143: 2021-02-03 00:00:00 | B145: '=Days+8+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE(... -> 2021-02-08 00:00:00 | C145: 2021-02-09 00:00:00 | D145: 2021-02-10 00:00:00 | B147: '=Days+15+DATE(Calendar11Year,Calendar11MonthOption,1)-WEEKDAY(DATE... -> 2021-02-15 00:00:00 | C147: 2021-02-16 00:00:00 | D147: 2021-02-17 00:00:00

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!Q23`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!Q23`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">1000000",Table1[FLOAT],"<=3000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">1000000",Table1[FLOAT],"<=3000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'GAIN/LOSS'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: P21: '< 100M' | Q21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | P22: '100-500M' | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P23: '500M-1B' | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P24: '1B <' | Q24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `4ea284d68c01|LITERAL_CONSTANT|Sheet1!R3`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!R3`  severity: Medium  confidence: Review
- formula: `=IF(AND(I3>12,MAX(D3:F3)>=($J3+45)),MAX(D3:F3),"")`
- evidence: Non-trivial numeric literal(s) found: 45.
- evidence: The same relative formula appears in 233 cells on this sheet; the others are Sheet1!R4, Sheet1!R5, Sheet1!R6, Sheet1!R7, Sheet1!R8, Sheet1!R9, Sheet1!R10, Sheet1!R11, ....
- cached value: None; row labels: []; column header: "'Game 45 Pins Over Avg'"; used range: A1:CJ782
- range D3:F3: values ['97', '97', '97']; beyond: {'left': 'C3: 2020-11-02 00:00:00', 'right': "G3: '=SUM(D3:F3)'"}
- neighbourhood: P1: '145 Avg w/500 Series' | Q1: '175 Avg w/600 Series' | R1: 'Game 45 Pins Over Avg' | S1: 'Series 140 Pins Over Avg' | T1: 'Triple Score' | P3: '=IF(I2>=12,IF(AND(J2<=145,G3>=500),G3,""),"")' -> None | Q3: '=IF(I2>=12,IF(AND(J2>=175,G3>=600),G3,""),"")' -> None | R3: '=IF(AND(I3>12,MAX(D3:F3)>=($J3+45)),MAX(D3:F3),"")' -> None | S3: '=IF(I2>12,IF((G3>=J2*3+140),G3,""),"")' -> None | T3: '=IF(AND(D3=E3,E3=F3),D3," ")' -> 97 | P4: '=IF(I3>=12,IF(AND(J3<=145,G4>=500),G4,""),"")' -> None | Q4: '=IF(I3>=12,IF(AND(J3<=175,G4>=600),G4,""),"")' -> None | R4: '=IF(AND(I4>12,MAX(D4:F4)>=($J4+45)),MAX(D4:F4),"")' -> None | S4: '=IF(I3>12,IF((G4>=J3*3+140),G4,""),"")' -> None | T4: '=IF(AND(D4=E4,E4=F4),D4," ")' -> ' ' | P5: '=IF(I4>=12,IF(AND(J4<=145,G5>=500),G5,""),"")' -> None | Q5: '=IF(I4>=12,IF(AND(J4<=175,G5>=600),G5,""),"")' -> None | R5: '=IF(AND(I5>12,MAX(D5:F5)>=($J5+45)),MAX(D5:F5),"")' -> None | S5: '=IF(I4>12,IF((G5>=J4*3+140),G5,""),"")' -> None | T5: '=IF(AND(D5=E5,E5=F5),D5," ")' -> 0

### `63f333a488c9|LITERAL_CONSTANT|Sheet1!Q3`

- workbook: `all_data_912_v0.1/spreadsheet/31746/2_31746_input.xlsx`
- location: `Sheet1!Q3`  severity: Medium  confidence: Review
- formula: `=(+D3*70)+(E3*69)+(F3*64)+(G3*61)+(H3*58)+(I3*57)+(J3*52)+(K3*46)+(L3*45)+(M3*34)+(N3*22)+(O3*10)+(P3*4)`
- evidence: Non-trivial numeric literal(s) found: 70, 69, 64, 61, 58, 57, 46, 45, 34, 22, 10.
- evidence: The same relative formula appears in 13 cells on this sheet; the others are Sheet1!Q4, Sheet1!Q5, Sheet1!Q6, Sheet1!Q7, Sheet1!Q8, Sheet1!Q9, Sheet1!Q10, Sheet1!Q11, ....
- cached value: 113322; row labels: ["'TI-1'"]; column header: "'Priced in productivity'"; used range: A1:Q38
- neighbourhood: Q1: 'note contract has 81 months to run' | O2: 'Month 72' | P2: 'Month 78' | Q2: 'Priced in productivity' | O3: 0 | P3: 0 | Q3: '=(+D3*70)+(E3*69)+(F3*64)+(G3*61)+(H3*58)+(I3*57)+(J3*52)+(K3*46)+... -> 113322 | O4: 0 | P4: 0 | Q4: '=(+D4*70)+(E4*69)+(F4*64)+(G4*61)+(H4*58)+(I4*57)+(J4*52)+(K4*46)+... -> 0 | O5: 0 | P5: 0 | Q5: '=(+D5*70)+(E5*69)+(F5*64)+(G5*61)+(H5*58)+(I5*57)+(J5*52)+(K5*46)+... -> 179953.65120465573

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!R29`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!R29`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")/COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Points /s (Net)'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: P27: '< 100M' | Q27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | P28: '100-500M' | Q28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P29: '500M-1B' | Q29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P30: '1B <' | Q30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `7f9746d5c513|LITERAL_CONSTANT|DATA!K17`

- workbook: `all_data_912_v0.1/spreadsheet/58656/3_58656_input.xlsx`
- location: `DATA!K17`  severity: Medium  confidence: Review
- formula: `=IF(AND(G17="n",DATE(A17,4,21)>D17>=H17),"1",IF(AND(G17="n",J16>21),K16+1,K16))`
- evidence: Non-trivial numeric literal(s) found: 21.
- evidence: The same relative formula appears in 116 cells on this sheet; the others are DATA!K18, DATA!K19, DATA!K20, DATA!K21, DATA!K22, DATA!K23, DATA!K24, DATA!K25, ....
- cached value: 0; row labels: ["'4'", "'T'"]; column header: ''; used range: A1:K132
- neighbourhood: I15: '=D15-D14' -> 7 | J15: '=IF(G15="n","1",J14+I15)' -> 16 | I16: '=D16-D15' -> 7 | J16: '=IF(G16="n","1",J15+I16)' -> 23 | I17: '=D17-D16' -> 8 | J17: '=IF(G17="n","1",J16+I17)' -> 31 | K17: '=IF(AND(G17="n",DATE(A17,4,21)>D17>=H17),"1",IF(AND(G17="n",J16>21... -> 0 | I18: '=D18-D17' -> 8 | J18: '=IF(G18="n","1",J17+I18)' -> 39 | K18: '=IF(AND(G18="n",DATE(A18,4,21)>D18>=H18),"1",IF(AND(G18="n",J17>21... -> 0 | I19: '=D19-D18' -> 7 | J19: '=IF(G19="n","1",J18+I19)' -> 46 | K19: '=IF(AND(G19="n",DATE(A19,4,21)>D19>=H19),"1",IF(AND(G19="n",J18>21... -> 0

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!S23`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!S23`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'GAIN/LOSS'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: Q21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

## LIVE_ERROR

### `484f4df3fe7b|LIVE_ERROR|Statistics!G28`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G28`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E26: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G26: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E27: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G27: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G28: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E29: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G29: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E30: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G30: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `87c4744e15aa|LIVE_ERROR|book1!B5`

- workbook: `all_data_912_v0.1/spreadsheet/55049/1_55049_input.xlsx`
- location: `book1!B5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'F100065'"]; column header: ''; used range: A1:B23
- neighbourhood: A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!' | A6: 'F100066' | B6: '=SUMPRODUCT(book2!A:A=book1!A6)*book2!H:J {array B6}' -> '#VALUE!' | A7: 'F100067' | B7: '=SUMPRODUCT(book2!A:A=book1!A7)*book2!H:J {array B7}' -> '#VALUE!'

### `724cc496b076|LIVE_ERROR|Sheet1!BK5`

- workbook: `all_data_912_v0.1/spreadsheet/52450/3_52450_input.xlsx`
- location: `Sheet1!BK5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 8 dependent cell(s): Sheet1!BK4, Sheet1!P4, Sheet1!P5, Sheet1!S4, Sheet1!S5, Sheet1!T4, Sheet1!T5, Sheet1!V4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Wind'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: BI4: '=IF($H5="",0,IF($H5<"",SUM(BI5:BI104)))' -> '#VALUE!' | BJ4: '=IF($H5="",0,IF($H5<"",SUM(BJ5:BJ104)))' -> '#VALUE!' | BK4: '=IF($H5="",0,IF($H5<"",SUM(BK5:BK104)))' -> '#VALUE!' | BL4: '=IF($H5="",0,IF($H5<"",SUM(BL5:BL104)))' -> '#VALUE!' | BM4: '=IF($H5="",0,IF($H5<"",SUM(BM5:BM104)))' -> '#VALUE!' | BI5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BI6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!' | BI7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BI$1,\'[1]X... -> '#VALUE!' | BJ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BJ$1,\'[1]X... -> '#VALUE!' | BK7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BK$1,\'[1]X... -> '#VALUE!' | BL7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BL$1,\'[1]X... -> '#VALUE!' | BM7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BM$1,\'[1]X... -> '#VALUE!'

### `ed000e28cd42|LIVE_ERROR|Sheet1!G4`

- workbook: `all_data_912_v0.1/spreadsheet/49333/1_49333_input.xlsx`
- location: `Sheet1!G4`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'Dubbo'", "'Arrogant Benji'"]; column header: ''; used range: A1:L7
- neighbourhood: E2: 1 | F2: 'Bow Thai' | G2: '=VLOOKUP(F2,Sheet3!$A$2:$D$300,2,FALSE)' -> '#N/A' | H2: '=VLOOKUP(F2,Sheet3!$A$2:$D$300,3,FALSE)' -> '#N/A' | I2: '=VLOOKUP(F2,Sheet3!$A$2:$D$300,4,FALSE)' -> '#N/A' | E3: 8 | F3: 'Subzero Trans Am' | G3: '=VLOOKUP(F3,Sheet3!$A$2:$D$300,2,FALSE)' -> '#N/A' | H3: '=VLOOKUP(F3,Sheet3!$A$2:$D$300,3,FALSE)' -> '#N/A' | I3: '=VLOOKUP(F3,Sheet3!$A$2:$D$300,4,FALSE)' -> '#N/A' | E4: 6 | F4: 'Arrogant Benji' | G4: '=VLOOKUP(F4,Sheet3!$A$2:$D$300,2,FALSE)' -> '#N/A' | H4: '=VLOOKUP(F4,Sheet3!$A$2:$D$300,3,FALSE)' -> '#N/A' | I4: '=VLOOKUP(F4,Sheet3!$A$2:$D$300,4,FALSE)' -> '#N/A' | E5: 8 | F5: 'Subzero Sutton' | G5: '=VLOOKUP(F5,Sheet3!$A$2:$D$300,2,FALSE)' -> '#N/A' | H5: '=VLOOKUP(F5,Sheet3!$A$2:$D$300,3,FALSE)' -> '#N/A' | I5: '=VLOOKUP(F5,Sheet3!$A$2:$D$300,4,FALSE)' -> '#N/A' | E6: 2 | F6: 'Im No Slouch' | G6: '=VLOOKUP(F6,Sheet3!$A$2:$D$300,2,FALSE)' -> '#N/A' | H6: '=VLOOKUP(F6,Sheet3!$A$2:$D$300,3,FALSE)' -> '#N/A' | I6: '=VLOOKUP(F6,Sheet3!$A$2:$D$300,4,FALSE)' -> '#N/A'

### `79139a88c691|LIVE_ERROR|Sheet1!AI5`

- workbook: `all_data_912_v0.1/spreadsheet/52450/1_52450_input.xlsx`
- location: `Sheet1!AI5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 9 dependent cell(s): Sheet1!AI4, Sheet1!P4, Sheet1!P5, Sheet1!S4, Sheet1!S5, Sheet1!T4, Sheet1!T5, Sheet1!V4, .... Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Wind'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: AG4: '=IF($H5="",0,IF($H5<"",SUM(AG5:AG104)))' -> '#VALUE!' | AH4: '=IF($H5="",0,IF($H5<"",SUM(AH5:AH104)))' -> '#VALUE!' | AI4: '=IF($H5="",0,IF($H5<"",SUM(AI5:AI104)))' -> '#VALUE!' | AJ4: '=IF($H5="",0,IF($H5<"",SUM(AJ5:AJ104)))' -> '#VALUE!' | AK4: '=IF($H5="",0,IF($H5<"",SUM(AK5:AK104)))' -> '#VALUE!' | AG5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AG$1,\'[1]X... -> '#VALUE!' | AH5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AH$1,\'[1]X... -> '#VALUE!' | AI5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AI$1,\'[1]X... -> '#VALUE!' | AJ5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AJ$1,\'[1]X... -> '#VALUE!' | AK5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!' | AG6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AG$1,\'[1]X... -> '#VALUE!' | AH6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AH$1,\'[1]X... -> '#VALUE!' | AI6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AI$1,\'[1]X... -> '#VALUE!' | AJ6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AJ$1,\'[1]X... -> '#VALUE!' | AK6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!' | AG7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AG$1,\'[1]X... -> '#VALUE!' | AH7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AH$1,\'[1]X... -> '#VALUE!' | AI7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AI$1,\'[1]X... -> '#VALUE!' | AJ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AJ$1,\'[1]X... -> '#VALUE!' | AK7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AK$1,\'[1]X... -> '#VALUE!'

### `40c60acd7755|LIVE_ERROR|Sort!L33`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!L33`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2002_Q2'"]; column header: ''; used range: A1:T147
- neighbourhood: J31: "=VLOOKUP($B31,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> -0.09999999999999992 | K31: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A31,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L31: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A31,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M31: '=D31*P31' -> '#VALUE!' | N31: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A31,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J32: "=VLOOKUP($B32,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.59 | K32: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A32,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L32: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A32,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M32: '=D32*P32' -> '#VALUE!' | N32: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A32,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J33: "=VLOOKUP($B33,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.5800000000000001 | K33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M33: '=D33*P33' -> '#VALUE!' | N33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J34: "=VLOOKUP($B34,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.5 | K34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M34: '=D34*P34' -> '#VALUE!' | N34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J35: "=VLOOKUP($B35,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.18 | K35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M35: '=D35*P35' -> '#VALUE!' | N35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!'

### `be2f958d4b41|LIVE_ERROR|Sort!L25`

- workbook: `all_data_912_v0.1/spreadsheet/59932/2_59932_input.xlsx`
- location: `Sort!L25`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2000_Q2'"]; column header: ''; used range: A1:T147
- neighbourhood: J23: "=VLOOKUP($B23,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.7999999999999998 | K23: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A23,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L23: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A23,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M23: '=D23*P23' -> '#VALUE!' | N23: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A23,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J24: "=VLOOKUP($B24,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 1.8399999999999999 | K24: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A24,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L24: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A24,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M24: '=D24*P24' -> '#VALUE!' | N24: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A24,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J25: "=VLOOKUP($B25,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 2.06 | K25: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A25,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L25: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A25,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M25: '=D25*P25' -> '#VALUE!' | N25: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A25,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J26: "=VLOOKUP($B26,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 2.01 | K26: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A26,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L26: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A26,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M26: '=D26*P26' -> '#VALUE!' | N26: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A26,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J27: "=VLOOKUP($B27,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 2.17 | K27: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A27,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L27: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A27,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M27: '=D27*P27' -> '#VALUE!' | N27: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A27,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!'

### `1f2994e91d0b|LIVE_ERROR|Sheet1!D130`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/1_189-9_input.xlsx`
- location: `Sheet1!D130`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'LB094D'"]; column header: ''; used range: A1:E613
- neighbourhood: B128: 2010-05-30 00:00:00 | C128: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D128: '=INT(C128)-INT(B128)' -> '#VALUE!' | B129: 2015-04-30 00:00:00 | C129: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D129: '=INT(C129)-INT(B129)' -> '#VALUE!' | B130: 2015-04-30 00:00:00 | C130: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D130: '=INT(C130)-INT(B130)' -> '#VALUE!' | B131: 2015-04-30 00:00:00 | C131: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D131: '=INT(C131)-INT(B131)' -> '#VALUE!' | B132: 2013-06-30 00:00:00 | C132: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D132: '=INT(C132)-INT(B132)' -> '#VALUE!'

### `7cc6b0fe1206|LIVE_ERROR|Sort!L59`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!L59`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2008_Q4'"]; column header: ''; used range: A1:T147
- neighbourhood: J57: "=VLOOKUP($B57,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 4.85 | K57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M57: '=D57*P57' -> '#VALUE!' | N57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J58: "=VLOOKUP($B58,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 5.119999999999999 | K58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M58: '=D58*P58' -> '#VALUE!' | N58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J59: "=VLOOKUP($B59,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 5.369999999999999 | K59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M59: '=D59*P59' -> '#VALUE!' | N59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J60: "=VLOOKUP($B60,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 6.109999999999999 | K60: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A60,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L60: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A60,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M60: '=D60*P60' -> '#VALUE!' | N60: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A60,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J61: "=VLOOKUP($B61,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 6.74 | K61: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A61,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L61: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A61,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M61: '=D61*P61' -> '#VALUE!' | N61: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A61,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!'

### `79139a88c691|LIVE_ERROR|Sheet1!AZ9`

- workbook: `all_data_912_v0.1/spreadsheet/52450/1_52450_input.xlsx`
- location: `Sheet1!AZ9`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 1 dependent cell(s): Sheet1!AZ4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Trainer'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: AX7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AX$1,\'[1]X... -> '#VALUE!' | AY7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AY$1,\'[1]X... -> '#VALUE!' | AZ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AZ$1,\'[1]X... -> '#VALUE!' | BA7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BA$1,\'[1]X... -> '#VALUE!' | BB7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BB$1,\'[1]X... -> '#VALUE!' | AX8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AX$1,\'[1]X... -> '#VALUE!' | AY8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AY$1,\'[1]X... -> '#VALUE!' | AZ8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AZ$1,\'[1]X... -> '#VALUE!' | BA8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BA$1,\'[1]X... -> '#VALUE!' | BB8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BB$1,\'[1]X... -> '#VALUE!' | AX9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AX$1,\'[1]X... -> '#VALUE!' | AY9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AY$1,\'[1]X... -> '#VALUE!' | AZ9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AZ$1,\'[1]X... -> '#VALUE!' | BA9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BA$1,\'[1]X... -> '#VALUE!' | BB9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BB$1,\'[1]X... -> '#VALUE!' | AX10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AX$1,\'[1]... -> None | AY10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AY$1,\'[1]... -> None | AZ10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AZ$1,\'[1]... -> None | BA10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BA$1,\'[1]... -> None | BB10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BB$1,\'[1]... -> None | AX11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AX$1,\'[1]... -> None | AY11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AY$1,\'[1]... -> None | AZ11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AZ$1,\'[1]... -> None | BA11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BA$1,\'[1]... -> None | BB11: '=IF($E11<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&BB$1,\'[1]... -> None

### `385e5089842a|LIVE_ERROR|Type2!D17`

- workbook: `all_data_912_v0.1/spreadsheet/53068/1_53068_input.xlsx`
- location: `Type 2!D17`  severity: Critical  confidence: Defect
- evidence: Cell contains #DIV/0!.
- cached value: '#DIV/0!'; row labels: ["'Base Salary for PS'"]; column header: ''; used range: A1:S27
- neighbourhood: C15: '=$F$4/$M$4' -> 119.277108433735 | D15: '=$F$4/$M$4' -> 119.277108433735 | E15: '=$F$4/$M$4' -> 119.277108433735 | F15: '=$F$4/$M$4' -> 119.277108433735 | C16: '=C15*C13' -> 2624.09638554217 | D16: '=D15*D13' -> 2624.09638554217 | E16: '=E15*E13' -> 2624.09638554217 | F16: '=F15*F13' -> 2624.09638554217 | C17: '=C16/$I$4' -> '#DIV/0!' | D17: '=D16/$I$4' -> '#DIV/0!' | E17: '=E16/$I$4' -> '#DIV/0!' | F17: '=F16/$I$4' -> '#DIV/0!' | C19: '=SUM(C11:N11)' -> 9900 | F19: 'Time Base Calculator'

### `7cc6b0fe1206|LIVE_ERROR|Sort!K97`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!K97`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2018_Q2'"]; column header: ''; used range: A1:T147
- neighbourhood: I95: "=VLOOKUP($B95,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 48351 | J95: "=VLOOKUP($B95,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 9.2 | K95: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A95,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L95: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A95,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M95: '=D95*P95' -> '#VALUE!' | I96: "=VLOOKUP($B96,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 50525 | J96: "=VLOOKUP($B96,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 9.73 | K96: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A96,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L96: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A96,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M96: '=D96*P96' -> '#VALUE!' | I97: "=VLOOKUP($B97,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 53318 | J97: "=VLOOKUP($B97,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 10.36 | K97: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A97,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L97: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A97,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M97: '=D97*P97' -> '#VALUE!' | I98: "=VLOOKUP($B98,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 56120 | J98: "=VLOOKUP($B98,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 11.030000000000001 | K98: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A98,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L98: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A98,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M98: '=D98*P98' -> '#VALUE!' | I99: "=VLOOKUP($B99,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 59531 | J99: "=VLOOKUP($B99,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 11.870000000000001 | K99: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A99,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L99: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A99,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M99: '=D99*P99' -> '#VALUE!'

### `40c60acd7755|LIVE_ERROR|Sort!L35`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!L35`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2002_Q4'"]; column header: ''; used range: A1:T147
- neighbourhood: J33: "=VLOOKUP($B33,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.5800000000000001 | K33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M33: '=D33*P33' -> '#VALUE!' | N33: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A33,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J34: "=VLOOKUP($B34,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.5 | K34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M34: '=D34*P34' -> '#VALUE!' | N34: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A34,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J35: "=VLOOKUP($B35,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.18 | K35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M35: '=D35*P35' -> '#VALUE!' | N35: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A35,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J36: "=VLOOKUP($B36,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.05 | K36: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A36,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L36: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A36,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M36: '=D36*P36' -> '#VALUE!' | N36: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A36,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J37: "=VLOOKUP($B37,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> -0.020000000000000004 | K37: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A37,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L37: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A37,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M37: '=D37*P37' -> '#VALUE!' | N37: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A37,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!'

### `f4cc22517a5b|LIVE_ERROR|master!E66`

- workbook: `all_data_912_v0.1/spreadsheet/47933/1_47933_input.xlsx`
- location: `master!E66`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C64: '=INDEX(amount!A:A,MATCH(A64,amount!B:B,0))' -> 4162.79137682743 | D64: '=ROUND(C64/52/B64,2)' -> 2.67 | E64: '=IF(B64<37.5,"2",)*IF(B64>37.5,"D2,1.5,")' -> 0 | C65: '=INDEX(amount!A:A,MATCH(A65,amount!B:B,0))' -> 40159.0777607332 | D65: '=ROUND(C65/52/B65,2)' -> 18.17 | E65: '=IF(B65<37.5,"2",)*IF(B65>37.5,"D2,1.5,")' -> '#VALUE!' | C66: '=INDEX(amount!A:A,MATCH(A66,amount!B:B,0))' -> 67444.8621512994 | D66: '=ROUND(C66/52/B66,2)' -> 30.52 | E66: '=IF(B66<37.5,"2",)*IF(B66>37.5,"D2,1.5,")' -> '#VALUE!' | C67: '=INDEX(amount!A:A,MATCH(A67,amount!B:B,0))' -> 69974.0332118742 | D67: '=ROUND(C67/52/B67,2)' -> 31.66 | E67: '=IF(B67<37.5,"2",)*IF(B67>37.5,"D2,1.5,")' -> '#VALUE!' | C68: '=INDEX(amount!A:A,MATCH(A68,amount!B:B,0))' -> 70667.4529872098 | D68: '=ROUND(C68/52/B68,2)' -> 31.98 | E68: '=IF(B68<37.5,"2",)*IF(B68>37.5,"D2,1.5,")' -> '#VALUE!'

### `b3080eb0650b|LIVE_ERROR|Sheet1!F5`

- workbook: `all_data_912_v0.1/spreadsheet/48608/1_48608_input.xlsx`
- location: `Sheet1!F5`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'Sandy'", "'Pass'"]; column header: ''; used range: A1:K17
- neighbourhood: E3: '=IF(C3="pass",B3,"")' -> 45678 | F3: '=VLOOKUP(G3,A3:B9,1,0)' -> '#N/A' | G3: 45678 | E4: '=IF(C4="pass",B4,"")' -> None | F4: '=VLOOKUP(G4,A4:B10,1,0)' -> '#N/A' | G4: 15667 | E5: '=IF(C5="pass",B5,"")' -> 15667 | F5: '=VLOOKUP(G5,A5:B11,1,0)' -> '#N/A' | G5: 11111 | E6: '=IF(C6="pass",B6,"")' -> None | E7: '=IF(C7="pass",B7,"")' -> 11111

### `1f2994e91d0b|LIVE_ERROR|Sheet1!D109`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/1_189-9_input.xlsx`
- location: `Sheet1!D109`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'LB0YQ9'"]; column header: ''; used range: A1:E613
- neighbourhood: B107: 2015-04-30 00:00:00 | C107: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D107: '=INT(C107)-INT(B107)' -> '#VALUE!' | B108: 2015-02-28 00:00:00 | C108: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D108: '=INT(C108)-INT(B108)' -> '#VALUE!' | B109: 2015-04-30 00:00:00 | C109: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D109: '=INT(C109)-INT(B109)' -> '#VALUE!' | B110: 2015-06-30 00:00:00 | C110: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D110: '=INT(C110)-INT(B110)' -> '#VALUE!' | B111: 2015-04-30 00:00:00 | C111: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D111: '=INT(C111)-INT(B111)' -> '#VALUE!'

### `9ffa652c7e85|LIVE_ERROR|VolymP5_P6_2023!I5`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!I5`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'ABC3'"]; column header: ''; used range: A1:K10
- neighbourhood: G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007' | G5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I5: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C... -> '#VALUE!' | J5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I6: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!D:D,""))... -> '200000008' | K6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!E:E,""))... -> '460000008' | G7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I7: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!D:D,""))... -> '200000009' | K7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!E:E,""))... -> '460000009'

### `a94eb6a7585f|LIVE_ERROR|HR!AD12`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !AD12`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 3 dependent cell(s): HR !AD24, HR !AF12, HR !AP12. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'N/A'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: AB10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | AC10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | AD10: "=INDEX(#REF!,MATCH('HR '!$A10,#REF!,0))" -> '#REF!' | AE10: '=X10' -> '#REF!' | AF10: '=IF(AD10>99.99,"Yes","No")' -> '#REF!' | AB11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | AC11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | AD11: "=INDEX(#REF!,MATCH('HR '!$A11,#REF!,0))" -> '#REF!' | AE11: '=X11' -> '#REF!' | AF11: '=IF(AD11>99.99,"Yes","No")' -> '#REF!' | AB12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AC12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AD12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AE12: '=X12' -> '#REF!' | AF12: '=IF(AD12>99.99,"Yes","No")' -> '#REF!' | AB14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AC14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AD14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AE14: '=X14' -> '#REF!' | AF14: '=IF(AD14>99.99,"Yes","No")' -> '#REF!'

### `192a19040f63|LIVE_ERROR|Sheettwo!E257`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E257`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0084577333'"]; column header: ''; used range: A1:G6234
- neighbourhood: C255: '0D' | D255: '0000000834' | E255: '=VLOOKUP(G255,Suppliers2[],2,FALSE)' -> '#N/A' | F255: '017338' | G255: '88713000' | C256: '1D' | D256: '0084447560' | E256: '=VLOOKUP(G256,Suppliers2[],2,FALSE)' -> '#N/A' | F256: '017393' | G256: '70263016' | C257: '1D' | D257: '0084577333' | E257: '=VLOOKUP(G257,Suppliers2[],2,FALSE)' -> '#N/A' | F257: '017538' | G257: '70263016' | C258: '1D' | D258: '0085029184' | E258: '=VLOOKUP(G258,Suppliers2[],2,FALSE)' -> '#N/A' | F258: '017700' | G258: '88888837' | C259: '3D' | D259: '0085066631' | E259: '=VLOOKUP(G259,Suppliers2[],2,FALSE)' -> '#N/A' | F259: '017701' | G259: '88713000'

### `9792181a96d9|LIVE_ERROR|Exp-DB!G34`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/1_524-31_input.xlsx`
- location: `Exp-DB!G34`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'pets'", "'PAYPAL INST XFER'"]; column header: ''; used range: A1:G53
- neighbourhood: E32: '=VLOOKUP(D32 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G32: '=INDEX(cats,MATCH("*"&D32&"*",exDB,0))' -> '#N/A' | E33: '=VLOOKUP(D33 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G33: '=INDEX(cats,MATCH("*"&D33&"*",exDB,0))' -> '#N/A' | E34: '=VLOOKUP(D34 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G34: '=INDEX(cats,MATCH("*"&D34&"*",exDB,0))' -> '#N/A' | E35: '=VLOOKUP(D35 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G35: '=INDEX(cats,MATCH("*"&D35&"*",exDB,0))' -> '#N/A' | E36: '=VLOOKUP(D36 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G36: '=INDEX(cats,MATCH("*"&D36&"*",exDB,0))' -> '#N/A'

### `9792181a96d9|LIVE_ERROR|Exp-DB!G40`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/1_524-31_input.xlsx`
- location: `Exp-DB!G40`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'PRIME VIDEO*261IS0 888-802-3080 WA'"]; column header: ''; used range: A1:G53
- neighbourhood: E38: '=VLOOKUP(D38 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G38: '=INDEX(cats,MATCH("*"&D38&"*",exDB,0))' -> '#N/A' | E39: '=VLOOKUP(D39 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G39: '=INDEX(cats,MATCH("*"&D39&"*",exDB,0))' -> '#N/A' | E40: '=VLOOKUP(D40 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G40: '=INDEX(cats,MATCH("*"&D40&"*",exDB,0))' -> '#N/A' | E41: '=VLOOKUP(D41 & "*",$A$1:$B$37,2,0)' -> 'mortgage' | G41: '=INDEX(cats,MATCH("*"&D41&"*",exDB,0))' -> 'mortgage' | E42: '=VLOOKUP(D42 & "*",$A$1:$B$37,2,0)' -> 'mortgage' | G42: '=INDEX(cats,MATCH("*"&D42&"*",exDB,0))' -> 'mortgage'

### `48efbd20cf68|LIVE_ERROR|Sheet1!H9`

- workbook: `all_data_912_v0.1/spreadsheet/50631/3_50631_input.xlsx`
- location: `Sheet1!H9`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: F7: '=IF($B$3+ROWS($D$7:$F38)-1<=$F$3,$B$3+ROWS($D$7:$F38)-1,"")' -> 2021-10-02 00:00:00 | H7: '=IF($B$3+ROWS($B$7:$B7)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B7)-1,""))' -> '#VALUE!' | J7: 2021-10-01 00:00:00 | F8: '=IF($B$3+ROWS($B$7:$F39)-1<=$F$3,$B$3+ROWS($B$7:$F39)-1,"")' -> 2021-10-03 00:00:00 | H8: '=IF($B$3+ROWS($B$7:$B8)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B8)-1,""))' -> '#VALUE!' | F9: '=IF($B$3+ROWS($B$7:$F40)-1<=$F$3,$B$3+ROWS($B$7:$F40)-1,"")' -> 2021-10-04 00:00:00 | H9: '=IF($B$3+ROWS($B$7:$B9)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B9)-1,""))' -> '#VALUE!' | F10: '=IF($B$3+ROWS($B$7:$F41)-1<=$F$3,$B$3+ROWS($B$7:$F41)-1,"")' -> 2021-10-05 00:00:00 | H10: '=IF($B$3+ROWS($B$7:$B10)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B10)-1,""))' -> '#VALUE!' | F11: '=IF($B$3+ROWS($B$7:$F42)-1<=$F$3,$B$3+ROWS($B$7:$F42)-1,"")' -> 2021-10-06 00:00:00 | H11: '=IF($B$3+ROWS($B$7:$B11)-1<=$F$3,WORKDAY($B$3+ROWS($B$7:$B11)-1,""))' -> '#VALUE!'

### `e0964cd37ef3|LIVE_ERROR|Data!H26`

- workbook: `all_data_912_v0.1/spreadsheet/510-3/1_510-3_input.xlsx`
- location: `Data!H26`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'\\u202d02'", "'19\\u202c'"]; column header: "'#VALUE!'"; used range: A1:H78
- neighbourhood: F24: 9 | G24: '19\u202c' | H24: '#VALUE!' | F25: 9 | G25: '19\u202c' | H25: '#VALUE!' | F26: 9 | G26: '19\u202c' | H26: '#VALUE!' | F27: 9 | G27: '19\u202c' | H27: '#VALUE!' | F28: 9 | G28: '19\u202c' | H28: '#VALUE!'

### `6fd6aa9b279e|LIVE_ERROR|Sheet1!H21`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `Sheet1!H21`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'STORE'"]; column header: ''; used range: A1:Y1001
- neighbourhood: H19: "=VLOOKUP(E19&F19,'PRICE LIST'!$I$2:$L1017,4,0)" -> '#N/A' | I19: 'STITCHING' | H20: "=VLOOKUP(E20&F20,'PRICE LIST'!$I$2:$L1018,4,0)" -> '#N/A' | I20: 'STITCHING' | H21: "=VLOOKUP(E21&F21,'PRICE LIST'!$I$2:$L1019,4,0)" -> '#N/A' | I21: 'STITCHING' | H22: "=VLOOKUP(E22&F22,'PRICE LIST'!$I$2:$L1020,4,0)" -> '#N/A' | I22: 'STITCHING' | H23: "=VLOOKUP(E23&F23,'PRICE LIST'!$I$2:$L1021,4,0)" -> '#N/A' | I23: 'STITCHING'

### `1005e3afe84b|LIVE_ERROR|Query!C2`

- workbook: `all_data_912_v0.1/spreadsheet/42354/1_42354_input.xlsx`
- location: `Query!C2`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'Completed'", "'#N/A'"]; column header: "'C'"; used range: A1:D8
- neighbourhood: A1: 'A' | B1: 'B' | C1: 'C' | D1: 'Result' | A2: 'Completed' | B2: '#N/A' | C2: '#N/A' | D2: 'Completed' | A3: '#N/A' | B3: 2022-03-15 00:00:00 | C3: '#N/A' | D3: 2022-03-15 00:00:00 | A4: '#N/A' | B4: '#N/A' | C4: 'ENR' | D4: 'ENR'

## MERGED_CELL_IN_DATA_RANGE

### `47eb61dd533e|MERGED_CELL_IN_DATA_RANGE|TEST!S70:S76`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!S70:S76`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 50000; row labels: []; column header: ''; used range: A1:S1004
- neighbourhood: Q68: '=IF((M68+O68)>$P$6,$P$1,0)' -> 0 | R68: '=O68+M68-Q68' -> 16098.2045109518 | Q69: '=IF((M69+O69)>$P$6,$P$1,0)' -> 0 | R69: '=O69+M69-Q69' -> 21732.576089785 | Q70: '=IF((M70+O70)>$P$6,$P$1,0)' -> 0 | R70: '=O70+M70-Q70' -> 29338.9777212097 | S70: '=SUM(Q70:Q76)' -> 50000 | Q71: '=IF((M71+O71)>$P$6,$P$1,0)' -> 25000 | R71: '=O71+M71-Q71' -> 14607.6199236331 | Q72: '=IF((M72+O72)>$P$6,$P$1,0)' -> 0 | R72: '=O72+M72-Q72' -> 19720.2868969047

### `6fd6aa9b279e|MERGED_CELL_IN_DATA_RANGE|Sheet1!C1:H1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `Sheet1!C1:H1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 MOHAK STITCHING BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: C1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" MOHAK STITCHING BILL")' -> 'OCTOBER-2021 MOHAK STITCHI... | A2: 'DATE' | B2: 'PARTY NAME' | C2: 'STORE CH. NO.' | D2: 'AGST CH. NO.' | E2: 'QUALITY' | A3: 2021-10-02 00:00:00 | B3: 'STORE' | C3: 1055 | D3: 4845

### `be6378a48fb9|MERGED_CELL_IN_DATA_RANGE|TEST!S147:S153`

- workbook: `all_data_912_v0.1/spreadsheet/55039/2_55039_input.xlsx`
- location: `TEST!S147:S153`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 50000; row labels: []; column header: ''; used range: A1:S1004
- neighbourhood: Q145: '=IF((M145+O145)>$P$6,$P$1,0)' -> 0 | R145: '=O145+M145-Q145' -> 11806.817691272434 | Q146: '=IF((M146+O146)>$P$6,$P$1,0)' -> 0 | R146: '=O146+M146-Q146' -> 15939.203883217786 | Q147: '=IF((M147+O147)>$P$6,$P$1,0)' -> 0 | R147: '=O147+M147-Q147' -> 21517.925242344012 | S147: '=SUM(Q147:Q153)' -> 50000 | Q148: '=IF((M148+O148)>$P$6,$P$1,0)' -> 0 | R148: '=O148+M148-Q148' -> 29049.199077164416 | Q149: '=IF((M149+O149)>$P$6,$P$1,0)' -> 25000 | R149: '=O149+M149-Q149' -> 14216.418754171958

### `b31624554d1c|MERGED_CELL_IN_DATA_RANGE|TEST!S112:S118`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!S112:S118`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 25000; row labels: []; column header: ''; used range: A1:S1004
- neighbourhood: Q110: '=IF((M110+O110)>$P$6,$P$1,0)' -> 0 | R110: '=O110+M110-Q110' -> 12530.539363444383 | Q111: '=IF((M111+O111)>$P$6,$P$1,0)' -> 0 | R111: '=O111+M111-Q111' -> 16916.228140649917 | Q112: '=IF((M112+O112)>$P$6,$P$1,0)' -> 0 | R112: '=O112+M112-Q112' -> 22836.90798987739 | S112: '=SUM(Q112:Q118)' -> 25000 | Q113: '=IF((M113+O113)>$P$6,$P$1,0)' -> 25000 | R113: '=O113+M113-Q113' -> 5829.825786334477 | Q114: '=IF((M114+O114)>$P$6,$P$1,0)' -> 0 | R114: '=O114+M114-Q114' -> 7870.264811551544

### `47eb61dd533e|MERGED_CELL_IN_DATA_RANGE|TEST!S7:S13`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!S7:S13`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0; row labels: ["'Starting Balance'", "'W'"]; column header: ''; used range: A1:S1004
- neighbourhood: Q6: 'Withdrawal' | R6: 'Balance' | Q7: '=IF((M7+O7)>$P$6,$P$1,0)' -> 0 | R7: '=P7-Q7' -> 3014.35 | S7: '=SUM(Q7:Q13)' -> 0 | Q8: '=IF((M8+O8)>$P$6,$P$1,0)' -> 0 | R8: '=O8+M8-Q8' -> 4821.71 | Q9: '=IF((M9+O9)>$P$6,$P$1,0)' -> 0 | R9: '=O9+M9-Q9' -> 7350

### `b31624554d1c|MERGED_CELL_IN_DATA_RANGE|TEST!S56:S62`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!S56:S62`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 50000; row labels: []; column header: ''; used range: A1:S1004
- neighbourhood: Q54: '=IF((M54+O54)>$P$6,$P$1,0)' -> 0 | R54: '=O54+M54-Q54' -> 16011.64712721948 | Q55: '=IF((M55+O55)>$P$6,$P$1,0)' -> 0 | R55: '=O55+M55-Q55' -> 21615.7236217463 | Q56: '=IF((M56+O56)>$P$6,$P$1,0)' -> 0 | R56: '=O56+M56-Q56' -> 29181.226889357506 | S56: '=SUM(Q56:Q62)' -> 50000 | Q57: '=IF((M57+O57)>$P$6,$P$1,0)' -> 25000 | R57: '=O57+M57-Q57' -> 14394.656300632632 | Q58: '=IF((M58+O58)>$P$6,$P$1,0)' -> 0 | R58: '=O58+M58-Q58' -> 19432.786005854054

### `5ec32da9071e|MERGED_CELL_IN_DATA_RANGE|Total(2)!G75:H75`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!G75:H75`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.2; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E73: '=IFERROR(VLOOKUP($H73,$J$27:$L$35,3,0)*$C73,0)' -> 0 | I73: '=D73/C73' -> '#DIV/0!' | E74: '=IFERROR(VLOOKUP($H74,$J$27:$L$35,3,0)*$C74,0)' -> 0 | I74: '=D74/C74' -> '#DIV/0!' | E75: '=SUM(E62:E74)' -> 9868 | G75: '=D75/C75' -> 0.2

### `70420e2dcf7b|MERGED_CELL_IN_DATA_RANGE|Sheet1!C1:H1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/1_49490_input.xlsx`
- location: `Sheet1!C1:H1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 MOHAK STITCHING BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: C1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" MOHAK STITCHING BILL")' -> 'OCTOBER-2021 MOHAK STITCHI... | A2: 'DATE' | B2: 'PARTY NAME' | C2: 'STORE CH. NO.' | D2: 'AGST CH. NO.' | E2: 'QUALITY' | A3: 2021-10-02 00:00:00 | B3: 'STORE' | C3: 1055 | D3: 4845 | E3: 'NEW NAKSHI'

### `be6378a48fb9|MERGED_CELL_IN_DATA_RANGE|TEST!S70:S76`

- workbook: `all_data_912_v0.1/spreadsheet/55039/2_55039_input.xlsx`
- location: `TEST!S70:S76`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 50000; row labels: []; column header: ''; used range: A1:S1004
- neighbourhood: Q68: '=IF((M68+O68)>$P$6,$P$1,0)' -> 25000 | R68: '=O68+M68-Q68' -> 11924.596117025954 | Q69: '=IF((M69+O69)>$P$6,$P$1,0)' -> 0 | R69: '=O69+M69-Q69' -> 16098.204757985039 | Q70: '=IF((M70+O70)>$P$6,$P$1,0)' -> 0 | R70: '=O70+M70-Q70' -> 21732.576423279803 | S70: '=SUM(Q70:Q76)' -> 50000 | Q71: '=IF((M71+O71)>$P$6,$P$1,0)' -> 0 | R71: '=O71+M71-Q71' -> 29338.978171427734 | Q72: '=IF((M72+O72)>$P$6,$P$1,0)' -> 25000 | R72: '=O72+M72-Q72' -> 14607.620531427441

### `dd8e0d8d4758|MERGED_CELL_IN_DATA_RANGE|2023!D142:E142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/3_68-47_input.xlsx`
- location: `2023!D142:E142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: -40411153.260000005; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | D141: '=SUM(D6:D140)' -> 2008969.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | D142: '=D141-E141' -> -40411153.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 24.99999999254942

### `fdad7150c0c3|MERGED_CELL_IN_DATA_RANGE|2023!D142:E142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/2_68-47_input.xlsx`
- location: `2023!D142:E142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: -40411168.260000005; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | D141: '=SUM(D6:D140)' -> 2008954.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | D142: '=D141-E141' -> -40411168.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 9.99999999254942

### `fdad7150c0c3|MERGED_CELL_IN_DATA_RANGE|2023!F142:G142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/2_68-47_input.xlsx`
- location: `2023!F142:G142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 40411178.26; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | H140: '=D140-E140+F140-G140' -> 0 | D141: '=SUM(D6:D140)' -> 2008954.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | G141: '=SUM(G6:G140)' -> -39759264.059999995 | H141: '=SUM(H7:H140)' -> 66577.49999999997 | D142: '=D141-E141' -> -40411168.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 9.99999999254942

### `3a2b74c70f66|MERGED_CELL_IN_DATA_RANGE|Total(2)!G38:H38`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!G38:H38`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.375272538821744; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E36: '=IFERROR(VLOOKUP($H36,$J$27:$L$35,3,0)*$C36,0)' -> 0 | I36: '=D36/C36' -> '#DIV/0!' | E37: '=IFERROR(VLOOKUP($H37,$J$27:$L$35,3,0)*$C37,0)' -> 0 | I37: '=D37/C37' -> '#DIV/0!' | E38: '=SUM(E8:E37)' -> 33753.4 | G38: '=D38/C38' -> 0.375272538821744 | E40: 'Agent' | F40: 'Date' | G40: 'Paid' | H40: 'Agent'

### `5ec32da9071e|MERGED_CELL_IN_DATA_RANGE|Total(2)!G38:H38`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!G38:H38`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.375272538821744; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E36: '=IFERROR(VLOOKUP($H36,$J$27:$L$35,3,0)*$C36,0)' -> 0 | I36: '=D36/C36' -> '#DIV/0!' | E37: '=IFERROR(VLOOKUP($H37,$J$27:$L$35,3,0)*$C37,0)' -> 0 | I37: '=D37/C37' -> '#DIV/0!' | E38: '=SUM(E8:E37)' -> 33753.4 | G38: '=D38/C38' -> 0.375272538821744 | E40: 'Agent' | F40: 'Date' | G40: 'Paid' | H40: 'Agent'

### `3a2b74c70f66|MERGED_CELL_IN_DATA_RANGE|Total(2)!G75:H75`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!G75:H75`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.2; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E73: '=IFERROR(VLOOKUP($H73,$J$27:$L$35,3,0)*$C73,0)' -> 0 | I73: '=D73/C73' -> '#DIV/0!' | E74: '=IFERROR(VLOOKUP($H74,$J$27:$L$35,3,0)*$C74,0)' -> 0 | I74: '=D74/C74' -> '#DIV/0!' | E75: '=SUM(E62:E74)' -> 9868 | G75: '=D75/C75' -> 0.2

### `dd8e0d8d4758|MERGED_CELL_IN_DATA_RANGE|2023!F142:G142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/3_68-47_input.xlsx`
- location: `2023!F142:G142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 40411178.26; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | H140: '=D140-E140+F140-G140' -> 0 | D141: '=SUM(D6:D140)' -> 2008969.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | G141: '=SUM(G6:G140)' -> -39759264.059999995 | H141: '=SUM(H7:H140)' -> 66592.49999999997 | D142: '=D141-E141' -> -40411153.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 24.99999999254942

### `bc56a9f2824a|MERGED_CELL_IN_DATA_RANGE|Total(2)!G75:H75`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!G75:H75`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.2; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E73: '=IFERROR(VLOOKUP($H73,$J$27:$L$35,3,0)*$C73,0)' -> 0 | I73: '=D73/C73' -> '#DIV/0!' | E74: '=IFERROR(VLOOKUP($H74,$J$27:$L$35,3,0)*$C74,0)' -> 0 | I74: '=D74/C74' -> '#DIV/0!' | E75: '=SUM(E62:E74)' -> 9868 | G75: '=D75/C75' -> 0.2

### `750361651608|MERGED_CELL_IN_DATA_RANGE|Sheet1!P1:S1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/3_49490_input.xlsx`
- location: `Sheet1!P1:S1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 PRESS BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: P1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" PRESS BILL")' -> 'OCTOBER-2021 PRESS BILL' | N2: 'WITHOUT PRESS' | O2: 'DATE' | P2: 'PARTY NAME' | Q2: 'BY WHOM' | R2: 'CH. NO.' | O3: '=A3' -> 2021-10-02 00:00:00 | P3: '=B3' -> 'STORE' | Q3: '=M3' -> 'MOHAK' | R3: '=C3' -> 1055

### `750361651608|MERGED_CELL_IN_DATA_RANGE|Sheet1!C1:H1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/3_49490_input.xlsx`
- location: `Sheet1!C1:H1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 MOHAK STITCHING BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: C1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" MOHAK STITCHING BILL")' -> 'OCTOBER-2021 MOHAK STITCHI... | A2: 'DATE' | B2: 'PARTY NAME' | C2: 'STORE CH. NO.' | D2: 'AGST CH. NO.' | E2: 'QUALITY' | A3: 2021-10-02 00:00:00 | B3: 'STORE' | C3: 1055 | D3: 4845 | E3: 'NEW NAKSHI'

### `3f7694b32e64|MERGED_CELL_IN_DATA_RANGE|2023!F142:G142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/1_68-47_input.xlsx`
- location: `2023!F142:G142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 40411178.26; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | H140: '=D140-E140+F140-G140' -> 0 | D141: '=SUM(D6:D140)' -> 2008944.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | G141: '=SUM(G6:G140)' -> -39759264.059999995 | H141: '=SUM(H7:H140)' -> 66567.49999999997 | D142: '=D141-E141' -> -40411178.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 0

### `bc56a9f2824a|MERGED_CELL_IN_DATA_RANGE|Total(2)!G38:H38`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!G38:H38`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.375272538821744; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E36: '=IFERROR(VLOOKUP($H36,$J$27:$L$35,3,0)*$C36,0)' -> 0 | I36: '=D36/C36' -> '#DIV/0!' | E37: '=IFERROR(VLOOKUP($H37,$J$27:$L$35,3,0)*$C37,0)' -> 0 | I37: '=D37/C37' -> '#DIV/0!' | E38: '=SUM(E8:E37)' -> 33753.4 | G38: '=D38/C38' -> 0.375272538821744 | E40: 'Agent' | F40: 'Date' | G40: 'Paid' | H40: 'Agent'

### `3f7694b32e64|MERGED_CELL_IN_DATA_RANGE|2023!D142:E142`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/1_68-47_input.xlsx`
- location: `2023!D142:E142`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: -40411178.260000005; row labels: []; column header: ''; used range: A1:N144
- neighbourhood: D140: 0 | E140: 0 | D141: '=SUM(D6:D140)' -> 2008944.4400000004 | E141: '=SUM(E6:E140)' -> 42420122.7 | F141: '=SUM(F6:F140)' -> 651914.2000000001 | D142: '=D141-E141' -> -40411178.260000005 | F142: '=F141-G141' -> 40411178.26 | F143: '=SUM(D142:G142)' -> 0

### `6fd6aa9b279e|MERGED_CELL_IN_DATA_RANGE|Sheet1!P1:S1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `Sheet1!P1:S1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 PRESS BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: P1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" PRESS BILL")' -> 'OCTOBER-2021 PRESS BILL' | N2: 'WITHOUT PRESS' | O2: 'DATE' | P2: 'PARTY NAME' | Q2: 'BY WHOM' | R2: 'CH. NO.' | O3: '=A3' -> 2021-10-02 00:00:00 | P3: '=B3' -> 'STORE' | Q3: '=M3' -> 'MOHAK' | R3: '=C3' -> 1055

### `70420e2dcf7b|MERGED_CELL_IN_DATA_RANGE|Sheet1!P1:S1`

- workbook: `all_data_912_v0.1/spreadsheet/49490/1_49490_input.xlsx`
- location: `Sheet1!P1:S1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'OCTOBER-2021 PRESS BILL'; row labels: []; column header: ''; used range: A1:Y1001
- neighbourhood: P1: '=UPPER(TEXT($A$3,"MMMM-YYYY")&" PRESS BILL")' -> 'OCTOBER-2021 PRESS BILL' | N2: 'WITHOUT PRESS' | O2: 'DATE' | P2: 'PARTY NAME' | Q2: 'BY WHOM' | R2: 'CH. NO.' | O3: '=A3' -> 2021-10-02 00:00:00 | P3: '=B3' -> 'STORE' | Q3: '=M3' -> 'MOHAK' | R3: '=C3' -> 1055

## NUMBERS_STORED_AS_TEXT

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A116`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A116`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1040' in a column that otherwise holds 1547 numbers.
- cached value: '1040'; row labels: []; column header: "'1256'"; used range: A1:K2802
- neighbourhood: A114: '1255' | B114: 4500041932 | C114: 2018-03-08 00:00:00 | A115: '1256' | B115: 4500041932 | C115: 2018-03-08 00:00:00 | A116: '1040' | B116: 2500072620 | C116: 2018-03-12 00:00:00 | A117: '1252' | B117: 4500041932 | C117: 2018-03-12 00:00:00 | A118: '1253' | B118: 4500041932 | C118: 2018-03-12 00:00:00

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A1052`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A1052`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2761' in a column that otherwise holds 1547 numbers.
- cached value: '2761'; row labels: []; column header: "'2760'"; used range: A1:K2802
- neighbourhood: A1050: '2759' | B1050: '2500074720' | C1050: 2018-09-19 00:00:00 | A1051: '2760' | B1051: '2500074720' | C1051: 2018-09-19 00:00:00 | A1052: '2761' | B1052: '2500074720' | C1052: 2018-09-19 00:00:00 | A1053: '2729' | B1053: '3500030040' | C1053: 2018-09-20 00:00:00 | A1054: '2730' | B1054: '3500030040' | C1054: 2018-09-20 00:00:00

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet2!F36`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet2!F36`  severity: Medium  confidence: Review
- evidence: Cell contains text value '23342' in a column that otherwise holds 47 numbers.
- cached value: '23342'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D34: '3G' | E34: 13230 | F34: '21252' | G34: 22402 | D35: '4G' | E35: 135242504 | F35: 135242502 | G35: 135242501 | H35: 135242344 | D36: '2G' | E36: 1341 | F36: '23342' | G36: 52553 | H36: 51212 | D37: '3G' | E37: 44331 | F37: 55342 | G37: 53042 | H37: 41334 | D38: '4G' | E38: '10534001\n 13022020' | F38: '12344005\n 25103001' | G38: 12344002 | H38: 12450014

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A1050`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A1050`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2759' in a column that otherwise holds 1547 numbers.
- cached value: '2759'; row labels: []; column header: "'2858'"; used range: A1:K2802
- neighbourhood: A1048: '2857' | B1048: '8600000260' | C1048: 2018-09-13 00:00:00 | A1049: '2858' | B1049: '8600000260' | C1049: 2018-09-13 00:00:00 | A1050: '2759' | B1050: '2500074720' | C1050: 2018-09-19 00:00:00 | A1051: '2760' | B1051: '2500074720' | C1051: 2018-09-19 00:00:00 | A1052: '2761' | B1052: '2500074720' | C1052: 2018-09-19 00:00:00

### `9ea22c621bf1|NUMBERS_STORED_AS_TEXT|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/15671/3_15671_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313331477314' in a column that otherwise holds 250 numbers.
- cached value: '913313331477314'; row labels: []; column header: "'913313331154234'"; used range: A1:A269
- neighbourhood: A1: '911313316543722' | A2: '913313331154234' | A3: '913313331477314' | A4: '913313323763534' | A5: '913313323763473'

### `8a63f3e46c57|NUMBERS_STORED_AS_TEXT|RawData!E14`

- workbook: `all_data_912_v0.1/spreadsheet/6435/3_6435_input.xlsx`
- location: `Raw Data!E14`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '9940' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '9940'; row labels: ["'0013'"]; column header: "'9940'"; used range: A1:P110
- neighbourhood: C12: 2017-05-31 00:00:00 | D12: '0013' | E12: '9940' | F12: '=IF(D12="","",IF(E12="","",IF(ISODD(COUNTIFS(D$4:D12,D12,E$4:E12,E... -> 'In' | G12: '=IF(D12="","",IF(E12="","",IF((COUNTIFS(D$4:D12,D12,E$4:E12,E12)=C... -> 'In-Progress' | C13: 2017-05-31 00:00:00 | D13: '0013' | E13: '9940' | F13: '=IF(D13="","",IF(E13="","",IF(ISODD(COUNTIFS(D$4:D13,D13,E$4:E13,E... -> 'Out' | G13: '=IF(D13="","",IF(E13="","",IF((COUNTIFS(D$4:D13,D13,E$4:E13,E13)=C... -> 'In-Progress' | C14: 2017-07-20 00:00:00 | D14: '0013' | E14: '9940' | F14: '=IF(D14="","",IF(E14="","",IF(ISODD(COUNTIFS(D$4:D14,D14,E$4:E14,E... -> 'In' | G14: '=IF(D14="","",IF(E14="","",IF((COUNTIFS(D$4:D14,D14,E$4:E14,E14)=C... -> 'In-Progress' | C15: 2017-08-24 00:00:00 | D15: '0013' | E15: '9940' | F15: '=IF(D15="","",IF(E15="","",IF(ISODD(COUNTIFS(D$4:D15,D15,E$4:E15,E... -> 'Out' | G15: '=IF(D15="","",IF(E15="","",IF((COUNTIFS(D$4:D15,D15,E$4:E15,E15)=C... -> 'In-Progress' | C16: 2017-09-06 00:00:00 | D16: '0013' | E16: '0142' | F16: '=IF(D16="","",IF(E16="","",IF(ISODD(COUNTIFS(D$4:D16,D16,E$4:E16,E... -> 'Out' | G16: '=IF(D16="","",IF(E16="","",IF((COUNTIFS(D$4:D16,D16,E$4:E16,E16)=C... -> 'Open'

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet2!F36`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet2!F36`  severity: Medium  confidence: Review
- evidence: Cell contains text value '23342' in a column that otherwise holds 47 numbers.
- cached value: '23342'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D34: '3G' | E34: 13230 | F34: '21252' | G34: 22402 | D35: '4G' | E35: 135242504 | F35: 135242502 | G35: 135242501 | H35: 135242344 | D36: '2G' | E36: 1341 | F36: '23342' | G36: 52553 | H36: 51212 | D37: '3G' | E37: 44331 | F37: 55342 | G37: 53042 | H37: 41334 | D38: '4G' | E38: '10534001\n 13022020' | F38: '12344005\n 25103001' | G38: 12344002 | H38: 12450014

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet2!E47`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet2!E47`  severity: Medium  confidence: Review
- evidence: Cell contains text value '12402000' in a column that otherwise holds 55 numbers.
- cached value: '12402000'; row labels: ["'4G'"]; column header: ''; used range: A1:Z168
- neighbourhood: C45: 'EE' | D45: '2G' | E45: 33245 | F45: 33244 | D46: '3G' | E46: 40131 | D47: '4G' | E47: '12402000' | F47: '12402003' | G47: '12402004' | C48: 'H3' | D48: '3G' | E48: 4443 | D49: '4G' | E49: 253542

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet2!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet2!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 41 numbers.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: E3: 10433 | F3: 11114 | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A1145`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A1145`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1573' in a column that otherwise holds 1547 numbers.
- cached value: '1573'; row labels: []; column header: "'1568'"; used range: A1:K2802
- neighbourhood: A1143: '1567' | B1143: 1500006150 | C1143: 2018-10-05 00:00:00 | A1144: '1568' | B1144: 1500006150 | C1144: 2018-10-05 00:00:00 | A1145: '1573' | B1145: 1500006150 | C1145: 2018-10-05 00:00:00 | A1146: '2763' | B1146: '7600032590' | C1146: 2018-10-05 00:00:00 | A1147: '2765' | B1147: '7600032590' | C1147: 2018-10-05 00:00:00

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1144`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1144`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1568' in a column that otherwise holds 1547 numbers.
- cached value: '1568'; row labels: []; column header: "'1567'"; used range: A1:K2802
- neighbourhood: A1142: '1560' | B1142: 1500006150 | C1142: 2018-10-05 00:00:00 | A1143: '1567' | B1143: 1500006150 | C1143: 2018-10-05 00:00:00 | A1144: '1568' | B1144: 1500006150 | C1144: 2018-10-05 00:00:00 | A1145: '1573' | B1145: 1500006150 | C1145: 2018-10-05 00:00:00 | A1146: '2763' | B1146: '7600032590' | C1146: 2018-10-05 00:00:00

### `9ea22c621bf1|NUMBERS_STORED_AS_TEXT|Sheet1!A5`

- workbook: `all_data_912_v0.1/spreadsheet/15671/3_15671_input.xlsx`
- location: `Sheet1!A5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313323763473' in a column that otherwise holds 250 numbers.
- cached value: '913313323763473'; row labels: []; column header: "'913313323763534'"; used range: A1:A269
- neighbourhood: A3: '913313331477314' | A4: '913313323763534' | A5: '913313323763473' | A6: '913313329226819' | A7: '913313343567715'

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1065`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1065`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2707' in a column that otherwise holds 1547 numbers.
- cached value: '2707'; row labels: []; column header: "'2706'"; used range: A1:K2802
- neighbourhood: A1063: '2769' | B1063: '7600032590' | C1063: 2018-09-25 00:00:00 | A1064: '2706' | B1064: '8700000120' | C1064: 2018-09-26 00:00:00 | A1065: '2707' | B1065: '8700000120' | C1065: 2018-09-26 00:00:00 | A1066: '2708' | B1066: '8700000120' | C1066: 2018-09-26 00:00:00 | A1067: '2709' | B1067: '8700000120' | C1067: 2018-09-26 00:00:00

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!F60`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!F60`  severity: Medium  confidence: Review
- evidence: Cell contains text value '13421' in a column that otherwise holds 47 numbers.
- cached value: '13421'; row labels: ["'O2'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D58: '4G' | E58: 1035203 | D59: 'Generation' | E59: 'Serving Cells' | D60: '2G' | E60: 13411 | F60: '13421' | G60: 11153 | H60: 21430 | D61: '3G' | E61: '14532' | F61: '33332' | G61: 51242 | H61: 55233 | D62: '4G' | E62: 135134244

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!E63`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!E63`  severity: Medium  confidence: Review
- evidence: Cell contains text value '33223' in a column that otherwise holds 55 numbers.
- cached value: '33223'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D61: '3G' | E61: '14532' | F61: '33332' | G61: 51242 | D62: '4G' | E62: 135134244 | C63: 'EE' | D63: '2G' | E63: '33223' | F63: 33221 | G63: 523 | D64: '3G' | E64: 51201 | F64: 40500 | G64: 40154 | D65: '4G' | E65: '10311014\n 15053012' | F65: 10341002 | G65: 10341005

### `8a63f3e46c57|NUMBERS_STORED_AS_TEXT|RawData!E10`

- workbook: `all_data_912_v0.1/spreadsheet/6435/3_6435_input.xlsx`
- location: `Raw Data!E10`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '9940' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '9940'; row labels: ["'0012'"]; column header: "'9940'"; used range: A1:P110
- neighbourhood: C8: 2017-10-05 00:00:00 | D8: '0010' | E8: '9940' | F8: '=IF(D8="","",IF(E8="","",IF(ISODD(COUNTIFS(D$4:D8,D8,E$4:E8,E8)),"... -> 'Out' | G8: '=IF(D8="","",IF(E8="","",IF((COUNTIFS(D$4:D8,D8,E$4:E8,E8)=COUNTIF... -> 'In-Progress' | C9: 2017-10-23 00:00:00 | D9: '0010' | E9: '9940' | F9: '=IF(D9="","",IF(E9="","",IF(ISODD(COUNTIFS(D$4:D9,D9,E$4:E9,E9)),"... -> 'In' | G9: '=IF(D9="","",IF(E9="","",IF((COUNTIFS(D$4:D9,D9,E$4:E9,E9)=COUNTIF... -> 'Closed' | C10: 2017-11-07 00:00:00 | D10: '0012' | E10: '9940' | F10: '=IF(D10="","",IF(E10="","",IF(ISODD(COUNTIFS(D$4:D10,D10,E$4:E10,E... -> 'Out' | G10: '=IF(D10="","",IF(E10="","",IF((COUNTIFS(D$4:D10,D10,E$4:E10,E10)=C... -> 'Open' | C11: 2017-02-03 00:00:00 | D11: '0013' | E11: '9940' | F11: '=IF(D11="","",IF(E11="","",IF(ISODD(COUNTIFS(D$4:D11,D11,E$4:E11,E... -> 'Out' | G11: '=IF(D11="","",IF(E11="","",IF((COUNTIFS(D$4:D11,D11,E$4:E11,E11)=C... -> 'In-Progress' | C12: 2017-05-31 00:00:00 | D12: '0013' | E12: '9940' | F12: '=IF(D12="","",IF(E12="","",IF(ISODD(COUNTIFS(D$4:D12,D12,E$4:E12,E... -> 'In' | G12: '=IF(D12="","",IF(E12="","",IF((COUNTIFS(D$4:D12,D12,E$4:E12,E12)=C... -> 'In-Progress'

### `fbcb24cf156d|NUMBERS_STORED_AS_TEXT|RawData!E18`

- workbook: `all_data_912_v0.1/spreadsheet/6435/2_6435_input.xlsx`
- location: `Raw Data!E18`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '9940' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '9940'; row labels: ["'0013'"]; column header: "'9940'"; used range: A1:P110
- neighbourhood: C16: 2017-09-06 00:00:00 | D16: '0013' | E16: '9940' | F16: '=IF(D16="","",IF(E16="","",IF(ISODD(COUNTIFS(D$4:D16,D16,E$4:E16,E... -> 'In' | G16: '=IF(D16="","",IF(E16="","",IF((COUNTIFS(D$4:D16,D16,E$4:E16,E16)=C... -> 'In-Progress' | C17: 2017-09-06 00:00:00 | D17: '0013' | E17: '9940' | F17: '=IF(D17="","",IF(E17="","",IF(ISODD(COUNTIFS(D$4:D17,D17,E$4:E17,E... -> 'Out' | G17: '=IF(D17="","",IF(E17="","",IF((COUNTIFS(D$4:D17,D17,E$4:E17,E17)=C... -> 'In-Progress' | C18: 2017-09-13 00:00:00 | D18: '0013' | E18: '9940' | F18: '=IF(D18="","",IF(E18="","",IF(ISODD(COUNTIFS(D$4:D18,D18,E$4:E18,E... -> 'In' | G18: '=IF(D18="","",IF(E18="","",IF((COUNTIFS(D$4:D18,D18,E$4:E18,E18)=C... -> 'In-Progress' | C19: 2017-10-11 00:00:00 | D19: '0013' | E19: '9940' | F19: '=IF(D19="","",IF(E19="","",IF(ISODD(COUNTIFS(D$4:D19,D19,E$4:E19,E... -> 'Out' | G19: '=IF(D19="","",IF(E19="","",IF((COUNTIFS(D$4:D19,D19,E$4:E19,E19)=C... -> 'Open' | C20: 2017-10-05 00:00:00 | D20: '0033' | E20: '0007' | F20: '=IF(D20="","",IF(E20="","",IF(ISODD(COUNTIFS(D$4:D20,D20,E$4:E20,E... -> 'Out' | G20: '=IF(D20="","",IF(E20="","",IF((COUNTIFS(D$4:D20,D20,E$4:E20,E20)=C... -> 'In-Progress'

### `74d1b4bee11f|NUMBERS_STORED_AS_TEXT|Sheet1!A6`

- workbook: `all_data_912_v0.1/spreadsheet/53117/1_53117_input.xlsx`
- location: `Sheet1!A6`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1065414' in a column that otherwise holds 22 numbers.
- cached value: '1065414'; row labels: []; column header: "'1065414'"; used range: A1:G27
- neighbourhood: A4: '1065414' | B4: 4160 | C4: 'US' | A5: '1065414' | B5: 432.84 | C5: 'Canada' | A6: '1065414' | B6: 4995 | C6: 'Canada' | A7: 1001130 | B7: 141500 | C7: 'Japan' | A8: 1001130 | B8: 1122 | C8: 'Canada'

### `7e6034cae12d|NUMBERS_STORED_AS_TEXT|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/15671/2_15671_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313331477316' in a column that otherwise holds 250 numbers.
- cached value: '913313331477316'; row labels: []; column header: "'913313331154233'"; used range: A1:A269
- neighbourhood: A1: '911313316543723' | A2: '913313331154233' | A3: '913313331477316' | A4: '913313323763536' | A5: '913313323763473'

### `7e6034cae12d|NUMBERS_STORED_AS_TEXT|Sheet1!A14`

- workbook: `all_data_912_v0.1/spreadsheet/15671/2_15671_input.xlsx`
- location: `Sheet1!A14`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313335263142' in a column that otherwise holds 250 numbers.
- cached value: '911313335263142'; row labels: []; column header: "'911313335259935'"; used range: A1:A269
- neighbourhood: A12: '913313327497499' | A13: '911313335259935' | A14: '911313335263142' | A15: '911313335259896' | A16: '911313317514666'

### `fbcb24cf156d|NUMBERS_STORED_AS_TEXT|RawData!E16`

- workbook: `all_data_912_v0.1/spreadsheet/6435/2_6435_input.xlsx`
- location: `Raw Data!E16`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '9940' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '9940'; row labels: ["'0013'"]; column header: "'9940'"; used range: A1:P110
- neighbourhood: C14: 2017-07-20 00:00:00 | D14: '0013' | E14: '9940' | F14: '=IF(D14="","",IF(E14="","",IF(ISODD(COUNTIFS(D$4:D14,D14,E$4:E14,E... -> 'In' | G14: '=IF(D14="","",IF(E14="","",IF((COUNTIFS(D$4:D14,D14,E$4:E14,E14)=C... -> 'In-Progress' | C15: 2017-08-24 00:00:00 | D15: '0013' | E15: '9940' | F15: '=IF(D15="","",IF(E15="","",IF(ISODD(COUNTIFS(D$4:D15,D15,E$4:E15,E... -> 'Out' | G15: '=IF(D15="","",IF(E15="","",IF((COUNTIFS(D$4:D15,D15,E$4:E15,E15)=C... -> 'In-Progress' | C16: 2017-09-06 00:00:00 | D16: '0013' | E16: '9940' | F16: '=IF(D16="","",IF(E16="","",IF(ISODD(COUNTIFS(D$4:D16,D16,E$4:E16,E... -> 'In' | G16: '=IF(D16="","",IF(E16="","",IF((COUNTIFS(D$4:D16,D16,E$4:E16,E16)=C... -> 'In-Progress' | C17: 2017-09-06 00:00:00 | D17: '0013' | E17: '9940' | F17: '=IF(D17="","",IF(E17="","",IF(ISODD(COUNTIFS(D$4:D17,D17,E$4:E17,E... -> 'Out' | G17: '=IF(D17="","",IF(E17="","",IF((COUNTIFS(D$4:D17,D17,E$4:E17,E17)=C... -> 'In-Progress' | C18: 2017-09-13 00:00:00 | D18: '0013' | E18: '9940' | F18: '=IF(D18="","",IF(E18="","",IF(ISODD(COUNTIFS(D$4:D18,D18,E$4:E18,E... -> 'In' | G18: '=IF(D18="","",IF(E18="","",IF((COUNTIFS(D$4:D18,D18,E$4:E18,E18)=C... -> 'In-Progress'

### `746dbe220c3b|NUMBERS_STORED_AS_TEXT|RawData!E33`

- workbook: `all_data_912_v0.1/spreadsheet/6435/1_6435_input.xlsx`
- location: `Raw Data!E33`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '1321' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '1321'; row labels: ["'00297'"]; column header: "'0142'"; used range: A1:P110
- neighbourhood: C31: 2017-09-14 00:00:00 | D31: '00216' | E31: '0142' | F31: '=IF(D31="","",IF(E31="","",IF(ISODD(COUNTIFS(D$4:D31,D31,E$4:E31,E... -> 'In' | G31: '=IF(D31="","",IF(E31="","",IF((COUNTIFS(D$4:D31,D31,E$4:E31,E31)=C... -> 'In-Progress' | C32: 2017-09-14 00:00:00 | D32: '00216' | E32: '0142' | F32: '=IF(D32="","",IF(E32="","",IF(ISODD(COUNTIFS(D$4:D32,D32,E$4:E32,E... -> 'Out' | G32: '=IF(D32="","",IF(E32="","",IF((COUNTIFS(D$4:D32,D32,E$4:E32,E32)=C... -> 'Open' | C33: 2017-10-30 00:00:00 | D33: '00297' | E33: '1321' | F33: '=IF(D33="","",IF(E33="","",IF(ISODD(COUNTIFS(D$4:D33,D33,E$4:E33,E... -> 'Out' | G33: '=IF(D33="","",IF(E33="","",IF((COUNTIFS(D$4:D33,D33,E$4:E33,E33)=C... -> 'Open' | C34: 2017-07-20 00:00:00 | D34: '00300' | E34: '1323' | F34: '=IF(D34="","",IF(E34="","",IF(ISODD(COUNTIFS(D$4:D34,D34,E$4:E34,E... -> 'Out' | G34: '=IF(D34="","",IF(E34="","",IF((COUNTIFS(D$4:D34,D34,E$4:E34,E34)=C... -> 'In-Progress' | C35: 2017-08-11 00:00:00 | D35: '00300' | E35: '1323' | F35: '=IF(D35="","",IF(E35="","",IF(ISODD(COUNTIFS(D$4:D35,D35,E$4:E35,E... -> 'In' | G35: '=IF(D35="","",IF(E35="","",IF((COUNTIFS(D$4:D35,D35,E$4:E35,E35)=C... -> 'Closed'

### `1a12611d45b2|NUMBERS_STORED_AS_TEXT|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/15671/1_15671_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '913313331154233' in a column that otherwise holds 250 numbers.
- cached value: '913313331154233'; row labels: []; column header: "'911313316543722'"; used range: A1:A269
- neighbourhood: A1: '911313316543722' | A2: '913313331154233' | A3: '913313331477316' | A4: '913313323763536'

### `746dbe220c3b|NUMBERS_STORED_AS_TEXT|RawData!E12`

- workbook: `all_data_912_v0.1/spreadsheet/6435/1_6435_input.xlsx`
- location: `Raw Data!E12`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '9940' and a formula consumes it as a number; SUM-style functions skip text and arithmetic on it fails.
- cached value: '9940'; row labels: ["'0013'"]; column header: "'9940'"; used range: A1:P110
- neighbourhood: C10: 2017-11-07 00:00:00 | D10: '0012' | E10: '9940' | F10: '=IF(D10="","",IF(E10="","",IF(ISODD(COUNTIFS(D$4:D10,D10,E$4:E10,E... -> 'Out' | G10: '=IF(D10="","",IF(E10="","",IF((COUNTIFS(D$4:D10,D10,E$4:E10,E10)=C... -> 'Open' | C11: 2017-02-03 00:00:00 | D11: '0013' | E11: '9940' | F11: '=IF(D11="","",IF(E11="","",IF(ISODD(COUNTIFS(D$4:D11,D11,E$4:E11,E... -> 'Out' | G11: '=IF(D11="","",IF(E11="","",IF((COUNTIFS(D$4:D11,D11,E$4:E11,E11)=C... -> 'In-Progress' | C12: 2017-05-31 00:00:00 | D12: '0013' | E12: '9940' | F12: '=IF(D12="","",IF(E12="","",IF(ISODD(COUNTIFS(D$4:D12,D12,E$4:E12,E... -> 'In' | G12: '=IF(D12="","",IF(E12="","",IF((COUNTIFS(D$4:D12,D12,E$4:E12,E12)=C... -> 'In-Progress' | C13: 2017-05-31 00:00:00 | D13: '0013' | E13: '9940' | F13: '=IF(D13="","",IF(E13="","",IF(ISODD(COUNTIFS(D$4:D13,D13,E$4:E13,E... -> 'Out' | G13: '=IF(D13="","",IF(E13="","",IF((COUNTIFS(D$4:D13,D13,E$4:E13,E13)=C... -> 'In-Progress' | C14: 2017-07-20 00:00:00 | D14: '0013' | E14: '9940' | F14: '=IF(D14="","",IF(E14="","",IF(ISODD(COUNTIFS(D$4:D14,D14,E$4:E14,E... -> 'In' | G14: '=IF(D14="","",IF(E14="","",IF((COUNTIFS(D$4:D14,D14,E$4:E14,E14)=C... -> 'In-Progress'

### `1a12611d45b2|NUMBERS_STORED_AS_TEXT|Sheet1!A18`

- workbook: `all_data_912_v0.1/spreadsheet/15671/1_15671_input.xlsx`
- location: `Sheet1!A18`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313335263168' in a column that otherwise holds 250 numbers.
- cached value: '911313335263168'; row labels: []; column header: "'911313335263334'"; used range: A1:A269
- neighbourhood: A16: '911313317514666' | A17: '911313335263334' | A18: '911313335263168' | A19: '911313335263133' | A20: 911313335263126

## RANGE_EXCLUSION

### `070be904b648|RANGE_EXCLUSION|Vat!F24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/2_49859_input.xlsx`
- location: `Vat!F24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(F12:F19)`
- evidence: Vat!F12:F19 stops short of Vat!F20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range F12:F19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'F11: 3', 'below': 'F20: 0'}
- neighbourhood: D22: 0 | E22: 0 | F22: 0 | G22: 1 | H22: 0 | D23: 0 | E23: 0 | F23: 0 | G23: 1 | H23: 0 | D24: '=SUM(D12:D23)' -> 4 | E24: '=SUM(E12:E23)' -> 4 | F24: '=SUM(F12:F19)' -> 4 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4

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

### `070be904b648|RANGE_EXCLUSION|Vat!I24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/2_49859_input.xlsx`
- location: `Vat!I24`  severity: Critical  confidence: Likely defect
- formula: `=SUM(I12:I19)`
- evidence: Vat!I12:I19 stops short of Vat!I20 (value 0), which sits below the range, between it and the total.
- cached value: 4; row labels: []; column header: ''; used range: A1:Q26
- range I12:I19: values ['0', '0', '0', '0', '1', '1', '1', '1']; beyond: {'above': 'I11: 6', 'below': 'I20: 0'}
- neighbourhood: G22: 1 | H22: 0 | I22: 0 | J22: 1 | G23: 1 | H23: 0 | I23: 0 | J23: 1 | G24: '=SUM(G16:G23)' -> 4 | H24: '=SUM(H12:H23)' -> 4 | I24: '=SUM(I12:I19)' -> 4 | J24: '=SUM(J16:J23)' -> 4 | K24: '=SUM(K12:K23)' -> 0

## RANGE_LENGTH_MISMATCH

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!I26`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!I26`  severity: High  confidence: Likely defect
- formula: `=COUNT(D24:F26)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D24:F26: values ['149', '105', '123', '100', '131', '122', '130', '130', '130']; beyond: {}
- neighbourhood: G24: '=SUM(D24:F24)' -> 377 | H24: '=SUM(G24:G24)' -> 377 | I24: '=COUNT(D24:F24)' -> 3 | J24: '=IF(I24=0,0,(ROUNDDOWN(H24/I24,0)))' -> 125 | K24: '=IFERROR(IF(I23>=12,IF($J23<=100,0+SUBSTITUTE(IF($D24>=125,","&$D2... -> None | G25: '=SUM(D25:F25)' -> 353 | H25: '=SUM(G24:G25)' -> 730 | I25: '=COUNT(D24:F25)' -> 6 | J25: '=IF(I25=0,0,(ROUNDDOWN(H25/I25,0)))' -> 121 | K25: '=IFERROR(IF(I24>=12,IF($J24<=100,0+SUBSTITUTE(IF($D25>=125,","&$D2... -> None | G26: '=SUM(D26:F26)' -> 390 | H26: '=SUM(G24:G26)' -> 1120 | I26: '=COUNT(D24:F26)' -> 9 | J26: '=IF(I26=0,0,(ROUNDDOWN(H26/I26,0)))' -> 124 | K26: '=IFERROR(IF(I25>=12,IF($J25<=100,0+SUBSTITUTE(IF($D26>=125,","&$D2... -> None | G27: '=SUM(D27:F27)' -> 322 | H27: '=SUM(G24:G27)' -> 1442 | I27: '=COUNT(D24:F27)' -> 12 | J27: '=IF(I27=0,0,(ROUNDDOWN(H27/I27,0)))' -> 120 | K27: '=IFERROR(IF(I26>=12,IF($J26<=100,0+SUBSTITUTE(IF($D27>=125,","&$D2... -> None | G28: '=SUM(D28:F28)' -> 337 | H28: '=SUM(G24:G28)' -> 1779 | I28: '=COUNT(D24:F28)' -> 15 | J28: '=IF(I28=0,0,(ROUNDDOWN(H28/I28,0)))' -> 118 | K28: '=IFERROR(IF(I27>=12,IF($J27<=100,0+SUBSTITUTE(IF($D28>=125,","&$D2... -> None

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!I110`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!I110`  severity: High  confidence: Likely defect
- formula: `=COUNT(D108:F110)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D108:F110: values ['97', '80', '111', '138', '97', '112', '101', '167', '110']; beyond: {}
- neighbourhood: G108: '=SUM(D108:F108)' -> 288 | H108: '=SUM(G108:G108)' -> 288 | I108: '=COUNT(D108:F108)' -> 3 | J108: '=IF(I108=0,0,(ROUNDDOWN(H108/I108,0)))' -> 96 | K108: '=IFERROR(IF(I107>=12,IF($J107<=100,0+SUBSTITUTE(IF($D108>=125,","&... -> None | G109: '=SUM(D109:F109)' -> 347 | H109: '=SUM(G108:G109)' -> 635 | I109: '=COUNT(D108:F109)' -> 6 | J109: '=IF(I109=0,0,(ROUNDDOWN(H109/I109,0)))' -> 105 | K109: '=IFERROR(IF(I108>=12,IF($J108<=100,0+SUBSTITUTE(IF($D109>=125,","&... -> None | G110: '=SUM(D110:F110)' -> 378 | H110: '=SUM(G108:G110)' -> 1013 | I110: '=COUNT(D108:F110)' -> 9 | J110: '=IF(I110=0,0,(ROUNDDOWN(H110/I110,0)))' -> 112 | K110: '=IFERROR(IF(I109>=12,IF($J109<=100,0+SUBSTITUTE(IF($D110>=125,","&... -> None | G111: '=SUM(D111:F111)' -> 366 | H111: '=SUM(G108:G111)' -> 1379 | I111: '=COUNT(D108:F111)' -> 12 | J111: '=IF(I111=0,0,(ROUNDDOWN(H111/I111,0)))' -> 114 | K111: '=IFERROR(IF(I110>=12,IF($J110<=100,0+SUBSTITUTE(IF($D111>=125,","&... -> None | G112: '=SUM(D112:F112)' -> 324 | H112: '=SUM(G108:G112)' -> 1703 | I112: '=COUNT(D108:F112)' -> 15 | J112: '=IF(I112=0,0,(ROUNDDOWN(H112/I112,0)))' -> 113 | K112: '=IFERROR(IF(I111>=12,IF($J111<=100,0+SUBSTITUTE(IF($D112>=125,","&... -> None

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I89`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I89`  severity: High  confidence: Likely defect
- formula: `=COUNT(D87:F89)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 6; row labels: []; column header: ''; used range: A1:CJ782
- range D87:F89: values ['103', '129', '110', 'None', 'None', 'None', '97', '96', '105']; beyond: {}
- neighbourhood: G87: '=SUM(D87:F87)' -> 342 | H87: '=SUM(G87:G87)' -> 342 | I87: '=COUNT(D87:F87)' -> 3 | J87: '=IF(I87=0,0,(ROUNDDOWN(H87/I87,0)))' -> 114 | K87: '=IFERROR(IF(I86>=12,IF($J86<=100,0+SUBSTITUTE(IF($D87>=125,","&$D8... -> None | G88: '=SUM(D88:F88)' -> 0 | H88: '=SUM(G87:G88)' -> 342 | I88: '=COUNT(D87:F88)' -> 3 | J88: '=IF(I88=0,0,(ROUNDDOWN(H88/I88,0)))' -> 114 | K88: '=IFERROR(IF(I87>=12,IF($J87<=100,0+SUBSTITUTE(IF($D88>=125,","&$D8... -> None | G89: '=SUM(D89:F89)' -> 298 | H89: '=SUM(G87:G89)' -> 640 | I89: '=COUNT(D87:F89)' -> 6 | J89: '=IF(I89=0,0,(ROUNDDOWN(H89/I89,0)))' -> 106 | K89: '=IFERROR(IF(I88>=12,IF($J88<=100,0+SUBSTITUTE(IF($D89>=125,","&$D8... -> None | G90: '=SUM(D90:F90)' -> 287 | H90: '=SUM(G87:G90)' -> 927 | I90: '=COUNT(D87:F90)' -> 9 | J90: '=IF(I90=0,0,(ROUNDDOWN(H90/I90,0)))' -> 103 | K90: '=IFERROR(IF(I89>=12,IF($J89<=100,0+SUBSTITUTE(IF($D90>=125,","&$D9... -> None | G91: '=SUM(D91:F91)' -> 319 | H91: '=SUM(G87:G91)' -> 1246 | I91: '=COUNT(D87:F91)' -> 12 | J91: '=IF(I91=0,0,(ROUNDDOWN(H91/I91,0)))' -> 103 | K91: '=IFERROR(IF(I90>=12,IF($J90<=100,0+SUBSTITUTE(IF($D91>=125,","&$D9... -> None

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I215`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I215`  severity: High  confidence: Likely defect
- formula: `=COUNT(D213:F215)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D213:F215: values ['114', '97', '124', '113', '128', '98', '127', '114', '116']; beyond: {}
- neighbourhood: G213: '=SUM(D213:F213)' -> 335 | H213: '=SUM(G213:G213)' -> 335 | I213: '=COUNT(D213:F213)' -> 3 | J213: '=IF(I213=0,0,(ROUNDDOWN(H213/I213,0)))' -> 111 | K213: '=IFERROR(IF(I212>=12,IF($J212<=100,0+SUBSTITUTE(IF($D213>=125,","&... -> None | G214: '=SUM(D214:F214)' -> 339 | H214: '=SUM(G213:G214)' -> 674 | I214: '=COUNT(D213:F214)' -> 6 | J214: '=IF(I214=0,0,(ROUNDDOWN(H214/I214,0)))' -> 112 | K214: '=IFERROR(IF(I213>=12,IF($J213<=100,0+SUBSTITUTE(IF($D214>=125,","&... -> None | G215: '=SUM(D215:F215)' -> 357 | H215: '=SUM(G213:G215)' -> 1031 | I215: '=COUNT(D213:F215)' -> 9 | J215: '=IF(I215=0,0,(ROUNDDOWN(H215/I215,0)))' -> 114 | K215: '=IFERROR(IF(I214>=12,IF($J214<=100,0+SUBSTITUTE(IF($D215>=125,","&... -> None | G216: '=SUM(D216:F216)' -> 309 | H216: '=SUM(G213:G216)' -> 1340 | I216: '=COUNT(D213:F216)' -> 12 | J216: '=IF(I216=0,0,(ROUNDDOWN(H216/I216,0)))' -> 111 | K216: '=IFERROR(IF(I215>=12,IF($J215<=100,0+SUBSTITUTE(IF($D216>=125,","&... -> None | G217: '=SUM(D217:F217)' -> 329 | H217: '=SUM(G213:G217)' -> 1669 | I217: '=COUNT(D213:F217)' -> 15 | J217: '=IF(I217=0,0,(ROUNDDOWN(H217/I217,0)))' -> 111 | K217: '=IFERROR(IF(I216>=12,IF($J216<=100,0+SUBSTITUTE(IF($D217>=125,","&... -> None

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!I89`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!I89`  severity: High  confidence: Likely defect
- formula: `=COUNT(D87:F89)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 6; row labels: []; column header: ''; used range: A1:CJ782
- range D87:F89: values ['103', '129', '110', 'None', 'None', 'None', '97', '96', '105']; beyond: {}
- neighbourhood: G87: '=SUM(D87:F87)' -> 342 | H87: '=SUM(G87:G87)' -> 342 | I87: '=COUNT(D87:F87)' -> 3 | J87: '=IF(I87=0,0,(ROUNDDOWN(H87/I87,0)))' -> 114 | K87: '=IFERROR(IF(I86>=12,IF($J86<=100,0+SUBSTITUTE(IF($D87>=125,","&$D8... -> None | G88: '=SUM(D88:F88)' -> 0 | H88: '=SUM(G87:G88)' -> 342 | I88: '=COUNT(D87:F88)' -> 3 | J88: '=IF(I88=0,0,(ROUNDDOWN(H88/I88,0)))' -> 114 | K88: '=IFERROR(IF(I87>=12,IF($J87<=100,0+SUBSTITUTE(IF($D88>=125,","&$D8... -> None | G89: '=SUM(D89:F89)' -> 298 | H89: '=SUM(G87:G89)' -> 640 | I89: '=COUNT(D87:F89)' -> 6 | J89: '=IF(I89=0,0,(ROUNDDOWN(H89/I89,0)))' -> 106 | K89: '=IFERROR(IF(I88>=12,IF($J88<=100,0+SUBSTITUTE(IF($D89>=125,","&$D8... -> None | G90: '=SUM(D90:F90)' -> 287 | H90: '=SUM(G87:G90)' -> 927 | I90: '=COUNT(D87:F90)' -> 9 | J90: '=IF(I90=0,0,(ROUNDDOWN(H90/I90,0)))' -> 103 | K90: '=IFERROR(IF(I89>=12,IF($J89<=100,0+SUBSTITUTE(IF($D90>=125,","&$D9... -> None | G91: '=SUM(D91:F91)' -> 319 | H91: '=SUM(G87:G91)' -> 1246 | I91: '=COUNT(D87:F91)' -> 12 | J91: '=IF(I91=0,0,(ROUNDDOWN(H91/I91,0)))' -> 103 | K91: '=IFERROR(IF(I90>=12,IF($J90<=100,0+SUBSTITUTE(IF($D91>=125,","&$D9... -> None

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!I299`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!I299`  severity: High  confidence: Likely defect
- formula: `=COUNT(D297:F299)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D297:F299: values ['103', '83', '87', '142', '120', '121', '121', '124', '121']; beyond: {}
- neighbourhood: G297: '=SUM(D297:F297)' -> 273 | H297: '=SUM(G297:G297)' -> 273 | I297: '=COUNT(D297:F297)' -> 3 | J297: '=IF(I297=0,0,(ROUNDDOWN(H297/I297,0)))' -> 91 | K297: '=IFERROR(IF(I296>=12,IF($J296<=100,0+SUBSTITUTE(IF($D297>=125,","&... -> None | G298: '=SUM(D298:F298)' -> 383 | H298: '=SUM(G297:G298)' -> 656 | I298: '=COUNT(D297:F298)' -> 6 | J298: '=IF(I298=0,0,(ROUNDDOWN(H298/I298,0)))' -> 109 | K298: '=IFERROR(IF(I297>=12,IF($J297<=100,0+SUBSTITUTE(IF($D298>=125,","&... -> None | G299: '=SUM(D299:F299)' -> 366 | H299: '=SUM(G297:G299)' -> 1022 | I299: '=COUNT(D297:F299)' -> 9 | J299: '=IF(I299=0,0,(ROUNDDOWN(H299/I299,0)))' -> 113 | K299: '=IFERROR(IF(I298>=12,IF($J298<=100,0+SUBSTITUTE(IF($D299>=125,","&... -> None | G300: '=SUM(D300:F300)' -> 356 | H300: '=SUM(G297:G300)' -> 1378 | I300: '=COUNT(D297:F300)' -> 12 | J300: '=IF(I300=0,0,(ROUNDDOWN(H300/I300,0)))' -> 114 | K300: '=IFERROR(IF(I299>=12,IF($J299<=100,0+SUBSTITUTE(IF($D300>=125,","&... -> None | G301: '=SUM(D301:F301)' -> 347 | H301: '=SUM(G297:G301)' -> 1725 | I301: '=COUNT(D297:F301)' -> 15 | J301: '=IF(I301=0,0,(ROUNDDOWN(H301/I301,0)))' -> 115 | K301: '=IFERROR(IF(I300>=12,IF($J300<=100,0+SUBSTITUTE(IF($D301>=125,","&... -> None

## VOLATILE_FUNCTION

### `63492daacabf|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/48930/3_48930_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")`
- evidence: 16 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!E2, Sheet1!D3, Sheet1!E3, Sheet1!D4, Sheet1!E4, Sheet1!D5, Sheet1!E5, ....
- cached value: 8; row labels: ["'Matthew'", "'PK'"]; column header: "'Age'"; used range: A1:E9
- neighbourhood: B1: 'Grade' | C1: 'Birth Date' | D1: 'Age' | E1: 'KDG Year' | B2: 'PK' | C2: 2016-02-11 00:00:00 | D2: '=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")' -> 8 | E2: '=YEAR(TODAY())+(5-D2)' -> 2021 | B3: 'PK' | C3: 2017-12-22 00:00:00 | D3: '=IF(C3,DATEDIF(C3,TODAY(),"Y"),"")' -> 6 | E3: '=YEAR(TODAY())+(5-D3)' -> 2023 | B4: 'PK' | C4: 2016-12-13 00:00:00 | D4: '=IF(C4,DATEDIF(C4,TODAY(),"Y"),"")' -> 7 | E4: '=YEAR(TODAY())+(5-D4)' -> 2022

### `09478d797a42|VOLATILE_FUNCTION|YTDBudget&Summary!G2`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `YTD Budget & Summary!G2`  severity: Low  confidence: Info
- formula: `=YEAR(TODAY())`
- evidence: 1 formula(s) on YTD Budget & Summary use TODAY or NOW, so their results change with the clock: YTD Budget & Summary!G2.
- cached value: 2024; row labels: ["'ACTUAL vs. BUDGET YTD'", "'YEAR'"]; column header: ''; used range: A1:G22
- neighbourhood: F2: 'YEAR' | G2: '=YEAR(TODAY())' -> 2024 | E3: 'Budget' | F3: 'Remaining Rs.' | G3: 'Remaining %' | E4: 100000 | F4: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> 100000 | G4: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> 1

### `bc617c24080f|VOLATILE_FUNCTION|Sheet1!E4`

- workbook: `all_data_912_v0.1/spreadsheet/37900/2_37900_input.xlsx`
- location: `Sheet1!E4`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!E4.
- cached value: 2024-05-17 00:00:00; row labels: ["'Value'", "'Current Date'"]; column header: ''; used range: A1:G16
- neighbourhood: D4: 'Current Date' | E4: '=TODAY()' -> 2024-05-17 00:00:00 | D5: 'Current Value'

### `9950acdeddc6|VOLATILE_FUNCTION|Extract!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/1_444-27_input.xlsx`
- location: `Extract!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 5 formula(s) on Extract use TODAY or NOW, so their results change with the clock: Extract!H2, Extract!H3, Extract!H4, Extract!H5, Extract!H6.
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:U13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 13859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `cf1c0902ee66|VOLATILE_FUNCTION|GDPRTrg!S6`

- workbook: `all_data_912_v0.1/spreadsheet/237-21/2_237-21_input.xlsx`
- location: `GDPR Trg!S6`  severity: Low  confidence: Info
- formula: `=IF(A6="","",IF(U6="LTA","LTA",IF(AND(G6="",J6<>"",J6<TODAY()),"Overdue",IF(OR(F6="not_started",F6="Not Attempted"),"Not Attempted",IF(OR(F6="incomplete",F6="in_progress"),"incomplete",IF(COUNTIFS(C$6:C6,C6,F$6:F6,"Complete",E$6:E6,"GDPR*")>1,"Upgraded","Complete"))))))`
- evidence: 25 formula(s) on GDPR Trg use TODAY or NOW, so their results change with the clock: GDPR Trg!S6, GDPR Trg!S7, GDPR Trg!S8, GDPR Trg!S9, GDPR Trg!S10, GDPR Trg!S11, GDPR Trg!S12, GDPR Trg!S13, ....
- cached value: None; row labels: ["'Data Protection V9'", "'Not Attempted'"]; column header: "'Status'"; used range: A1:AL65
- range C$6:C6: values ['38001962']; beyond: {'above': "C5: 'EmployeeNumber'", 'below': 'C7: 38005850', 'left': 'B6: 1', 'right': 'D6: None'}
- neighbourhood: T4: 'MI Support Columns' | Q5: 'SF Location' | R5: 'SF Line Manager' | S5: 'Status' | T5: 'Score' | U5: 'LTA Status' | S6: '=IF(A6="","",IF(U6="LTA","LTA",IF(AND(G6="",J6<>"",J6<TODAY()),"Ov... -> None | T6: 1001 | S7: '=IF(A7="","",IF(U7="LTA","LTA",IF(AND(G7="",J7<>"",J7<TODAY()),"Ov... -> None | T7: 1002 | S8: '=IF(A8="","",IF(U8="LTA","LTA",IF(AND(G8="",J8<>"",J8<TODAY()),"Ov... -> None | T8: 1003

### `5124d0617e42|VOLATILE_FUNCTION|example!G8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!G8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(20,25)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!G9, example!G10, example!G11, example!G12.
- cached value: 25; row labels: ["'Egg'"]; column header: "'SHAMS'"; used range: A1:O18
- neighbourhood: E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 15 | G8: '=RANDBETWEEN(20,25)' -> 25 | H8: '=RANDBETWEEN(25,30)' -> 26 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 16 | G9: '=RANDBETWEEN(20,25)' -> 21 | H9: '=RANDBETWEEN(25,30)' -> 26 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 15 | G10: '=RANDBETWEEN(20,25)' -> 21 | H10: '=RANDBETWEEN(25,30)' -> 28

### `40397a4736e1|VOLATILE_FUNCTION|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F3`  severity: Low  confidence: Info
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: 56 formula(s) on Test use TODAY or NOW, so their results change with the clock: Test!F3, Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, ....
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:15:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `c4229dd05b85|VOLATILE_FUNCTION|example!E8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!E8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(10,15)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!E9, example!E10, example!E11, example!E12.
- cached value: 13; row labels: ["'Egg'"]; column header: "'AMIN'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 20 | C9: '=RANDBETWEEN(1,5)' -> 1 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 15 | G9: '=RANDBETWEEN(20,25)' -> 20 | C10: '=RANDBETWEEN(1,5)' -> 3 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 19 | G10: '=RANDBETWEEN(20,25)' -> 25

### `766ae98f7318|VOLATILE_FUNCTION|Sheet1!F10`

- workbook: `all_data_912_v0.1/spreadsheet/34435/3_34435_input.xlsx`
- location: `Sheet1!F10`  severity: Low  confidence: Info
- formula: `=TODAY()-E10`
- evidence: 14 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!F10, Sheet1!F11, Sheet1!F12, Sheet1!F13, Sheet1!F14, Sheet1!F15, Sheet1!F16, Sheet1!F17, ....
- cached value: 5001; row labels: []; column header: "'Amount of Days After Hire'"; used range: A1:L23
- neighbourhood: E9: 'Employee Start Date' | F9: 'Amount of Days After Hire' | G9: 'Accumulated PTO (Hours)' | E10: 2010-09-06 00:00:00 | F10: '=TODAY()-E10' -> 5001 | E11: 2011-09-06 00:00:00 | F11: '=TODAY()-E11' -> 4636 | E12: 2012-09-06 00:00:00 | F12: '=TODAY()-E12' -> 4270

### `a05e86bd9436|VOLATILE_FUNCTION|Open!P4`

- workbook: `all_data_912_v0.1/spreadsheet/105-24/1_105-24_input.xlsx`
- location: `Open!P4`  severity: Low  confidence: Info
- formula: `=INT(TODAY()-D4+(1))`
- evidence: 20 formula(s) on Open use TODAY or NOW, so their results change with the clock: Open!P4, Open!P5, Open!P6, Open!P7, Open!P8, Open!P9, Open!P10, Open!P11, ....
- cached value: None; row labels: ["'Perform Peer Review'", "'gsj65824'"]; column header: "'DM Age'"; used range: A1:S23
- neighbourhood: N3: 'Changed On' | O3: 'Time of change' | P3: 'DM Age' | N4: 2023-05-03 00:00:00 | O4: 16:48:09 | P4: '=INT(TODAY()-D4+(1))' -> None | N5: 2023-04-27 00:00:00 | O5: 18:53:30 | P5: '=INT(TODAY()-D5+(1))' -> None | N6: 2023-04-28 00:00:00 | O6: 18:10:33 | P6: '=INT(TODAY()-D6+(1))' -> None

### `6b43fa913e4f|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/45181/2_45181_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=C2-TODAY()`
- evidence: 19 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: -398; row labels: []; column header: "'Days left to return books'"; used range: A1:I20
- neighbourhood: B1: 'Date Picked UP' | C1: 'Date Drop Off' | D1: 'Days left to return books' | B2: 2022-04-29 00:00:00 | C2: '=B2+365' -> 2023-04-29 00:00:00 | D2: '=C2-TODAY()' -> -398 | B3: 2022-04-30 00:00:00 | C3: '=B3+365' -> 2023-04-30 00:00:00 | D3: '=C3-TODAY()' -> -397 | B4: 2022-05-01 00:00:00 | C4: '=B4+365' -> 2023-05-01 00:00:00 | D4: '=C4-TODAY()' -> -396

### `026595829753|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/54640/1_54640_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=DATEDIF(C2,TODAY(),"D")`
- evidence: 17 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: 1900-02-13 00:00:00; row labels: []; column header: ''; used range: A1:D18
- neighbourhood: C1: 'Start Date' | C2: 2024-04-16 00:00:00 | D2: '=DATEDIF(C2,TODAY(),"D")' -> 1900-02-13 00:00:00 | C3: 2024-04-16 00:00:00 | D3: '=DATEDIF(C3,TODAY(),"D")' -> 1900-02-13 00:00:00 | C4: 2024-04-16 00:00:00 | D4: '=DATEDIF(C4,TODAY(),"D")' -> 1900-02-13 00:00:00

### `c9425772da07|VOLATILE_FUNCTION|Purchases!M2`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/2_CF_3712_input.xlsx`
- location: `Purchases!M2`  severity: Low  confidence: Info
- formula: `=IF(K2="Yes", "DONE", IF(ISBLANK(G2), "", H2-TODAY() & " day(s) remaining"))`
- evidence: 402 formula(s) on Purchases use TODAY or NOW, so their results change with the clock: Purchases!M2, Purchases!M3, Purchases!M4, Purchases!M5, Purchases!M6, Purchases!M7, Purchases!M8, Purchases!M9, ....
- cached value: '6 day(s) remaining'; row labels: ["'No'", "'Yes'"]; column header: "'Days to pay'"; used range: A1:M441
- neighbourhood: K1: 'Invoice paid' | L1: 'Received' | M1: 'Days to pay' | K2: 'No' | L2: 'Yes' | M2: '=IF(K2="Yes", "DONE", IF(ISBLANK(G2), "", H2-TODAY() & " day(s) re... -> '6 day(s) remaining' | K3: 'No' | L3: 'No' | M3: '=IF(K3="Yes", "DONE", IF(ISBLANK(G3), "", H3-TODAY() & " day(s) re... -> '-34 day(s) remaining' | K4: 'No' | L4: 'No' | M4: '=IF(K4="Yes", "DONE", IF(ISBLANK(G4), "", H4-TODAY() & " day(s) re... -> '153 day(s) remaining'

### `5124d0617e42|VOLATILE_FUNCTION|example!E8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!E8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(10,15)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!E9, example!E10, example!E11, example!E12.
- cached value: 13; row labels: ["'Egg'"]; column header: "'AMIN'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 10 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 15 | G8: '=RANDBETWEEN(20,25)' -> 25 | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 6 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 16 | G9: '=RANDBETWEEN(20,25)' -> 21 | C10: '=RANDBETWEEN(1,5)' -> 4 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 15 | G10: '=RANDBETWEEN(20,25)' -> 21

### `a5e1567c7a75|VOLATILE_FUNCTION|DATABANK!B4`

- workbook: `all_data_912_v0.1/spreadsheet/54238/3_54238_input.xlsx`
- location: `DATABANK!B4`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on DATABANK use TODAY or NOW, so their results change with the clock: DATABANK!B4.
- cached value: 2024-05-20 00:00:00; row labels: []; column header: ''; used range: A1:I13
- neighbourhood: B4: '=TODAY()' -> 2024-05-20 00:00:00 | B6: 'Fiscal Month'

### `2b144ac2a52b|VOLATILE_FUNCTION|Result!J10`

- workbook: `all_data_912_v0.1/spreadsheet/118-10/1_118-10_input.xlsx`
- location: `Result!J10`  severity: Low  confidence: Info
- formula: `=IF(I10>0,TODAY()-(A10),"")`
- evidence: 14 formula(s) on Result use TODAY or NOW, so their results change with the clock: Result!J10, Result!J11, Result!J18, Result!J19, Result!J27, Result!J28, Result!J29, Result!J30, ....
- cached value: None; row labels: ["'xxxxx'", "'CustomerX,Polmia'"]; column header: ''; used range: A1:J46
- neighbourhood: H10: 'CustomerX,Polmia' | J10: '=IF(I10>0,TODAY()-(A10),"")' -> None | H11: 'CustomerX,Polmia' | J11: '=IF(I11>0,TODAY()-(A11),"")' -> None

### `3a4af9c80244|VOLATILE_FUNCTION|Sheet1!F3`

- workbook: `all_data_912_v0.1/spreadsheet/57376/3_57376_input.xlsx`
- location: `Sheet1!F3`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(E3+14,E3+RAND()*100)`
- evidence: Function(s) found: RAND, RANDBETWEEN.
- evidence: The same relative formula appears in 50 cells on this sheet; the others are Sheet1!F4, Sheet1!F5, Sheet1!F6, Sheet1!F7, Sheet1!F8, Sheet1!F9, Sheet1!F10, Sheet1!F11, ....
- cached value: 2021-01-21 00:00:00; row labels: []; column header: "'end date'"; used range: A1:G30002
- neighbourhood: D2: 'rang_val' | E2: 'start date' | F2: 'end date' | G2: 'duration_amount_available' | D3: '=RANDBETWEEN(50,750)' -> 608 | E3: 2021-01-03 00:00:00 | F3: '=RANDBETWEEN(E3+14,E3+RAND()*100)' -> 2021-01-21 00:00:00 | G3: '=DATEDIF(E3,F3,"D")+1' -> 19 | D4: '=RANDBETWEEN(50,750)' -> 323 | E4: 2021-01-02 00:00:00 | F4: '=RANDBETWEEN(E4+14,E4+RAND()*100)' -> 2021-01-29 00:00:00 | G4: '=DATEDIF(E4,F4,"D")+1' -> 28 | D5: '=RANDBETWEEN(50,750)' -> 516 | E5: 2021-01-02 00:00:00 | F5: '=RANDBETWEEN(E5+14,E5+RAND()*100)' -> 2021-03-11 00:00:00 | G5: '=DATEDIF(E5,F5,"D")+1' -> 69

### `0b213825e4f4|VOLATILE_FUNCTION|Result!J10`

- workbook: `all_data_912_v0.1/spreadsheet/118-10/2_118-10_input.xlsx`
- location: `Result!J10`  severity: Low  confidence: Info
- formula: `=IF(I10>0,TODAY()-(A10),"")`
- evidence: 14 formula(s) on Result use TODAY or NOW, so their results change with the clock: Result!J10, Result!J11, Result!J18, Result!J19, Result!J27, Result!J28, Result!J29, Result!J30, ....
- cached value: None; row labels: ["'xxxxx'", "'CustomerX,Polmia'"]; column header: ''; used range: A1:J46
- neighbourhood: H10: 'CustomerX,Polmia' | J10: '=IF(I10>0,TODAY()-(A10),"")' -> None | H11: 'CustomerX,Polmia' | J11: '=IF(I11>0,TODAY()-(A11),"")' -> None

### `c05e60f72c61|VOLATILE_FUNCTION|Dati!CF12`

- workbook: `all_data_912_v0.1/spreadsheet/55912/2_55912_input.xlsx`
- location: `Dati!CF12`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1))*(#REF!="SI"))`
- evidence: Function(s) found: OFFSET.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are Dati!CG12, Dati!CF17, Dati!CG17.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:CJ40
- neighbourhood: CF12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CG12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CF13: '=1-(CF12/AG2)' -> '#REF!' | CG13: '=1-(CG12/AG2)' -> '#REF!' | CF14: '=1/CF13' -> '#REF!' | CG14: '=1/CG13' -> '#REF!'

### `e61cd08d6d5f|VOLATILE_FUNCTION|SubCO's!B6`

- workbook: `all_data_912_v0.1/spreadsheet/49782/3_49782_input.xlsx`
- location: `Sub CO's!B6`  severity: Medium  confidence: Review
- formula: `=IF(A6=""," ",INDIRECT("'"&$A6&"'!C6")&"-"&COUNTIF($A$4:$A6,$A6))`
- evidence: Function(s) found: INDIRECT.
- cached value: '666-1'; row labels: ["'Smith'"]; column header: "'456-2'"; used range: A1:L50
- range $A$4:$A6: values ["'Huff'", "'Huff'", "'Smith'"]; beyond: {'above': "A3: 'Sub'", 'below': "A7: 'Granite'"}
- neighbourhood: A4: 'Huff' | B4: '456-1' | C4: '03 05 00' | D4: 2021-08-01 00:00:00 | A5: 'Huff' | B5: '456-2' | C5: '04 21 13' | D5: 2021-08-20 00:00:00 | A6: 'Smith' | B6: '=IF(A6=""," ",INDIRECT("\'"&$A6&"\'!C6")&"-"&COUNTIF($A$4:$A6,$A6))' -> '666-1' | C6: '05 51 33' | D6: 2021-08-28 00:00:00 | A7: 'Granite' | B7: '444-1' | C7: '22 01 00' | D7: 2021-09-15 00:00:00 | A8: 'Leo' | C8: '04 21 13' | D8: 2021-09-15 00:00:00

### `9bb02d9c0dd0|VOLATILE_FUNCTION|CALCULATEAGE!D2`

- workbook: `all_data_912_v0.1/spreadsheet/58613/1_58613_input.xlsx`
- location: `CALCULATE AGE!D2`  severity: Low  confidence: Info
- formula: `=DATEDIF(C2,TODAY(),"y")`
- evidence: 10 formula(s) on CALCULATE AGE use TODAY or NOW, so their results change with the clock: CALCULATE AGE!D2, CALCULATE AGE!D3, CALCULATE AGE!D4, CALCULATE AGE!D5, CALCULATE AGE!D6, CALCULATE AGE!D7, CALCULATE AGE!D8, CALCULATE AGE!D9, ....
- cached value: 28; row labels: ["'Paul'"]; column header: "'Age'"; used range: A1:D11
- neighbourhood: B1: 'Name' | C1: 'Date of birth' | D1: 'Age' | B2: 'Paul' | C2: 1995-06-06 00:00:00 | D2: '=DATEDIF(C2,TODAY(),"y")' -> 28 | B3: 'Cecilia' | C3: 1983-03-20 00:00:00 | D3: '=DATEDIF(C3,TODAY(),"y")' -> 41 | B4: 'David' | C4: 2000-11-16 00:00:00 | D4: '=DATEDIF(C4,TODAY(),"y")' -> 23

### `c4229dd05b85|VOLATILE_FUNCTION|example!D8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!D8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(5,10)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!D9, example!D10, example!D11, example!D12.
- cached value: 6; row labels: ["'Egg'"]; column header: "'INAM'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | B8: 'Egg' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 18 | B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 1 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 15 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 3 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 19

### `9d7ac18c8fd7|VOLATILE_FUNCTION|Extract!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/3_444-27_input.xlsx`
- location: `Extract!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 5 formula(s) on Extract use TODAY or NOW, so their results change with the clock: Extract!H2, Extract!H3, Extract!H4, Extract!H5, Extract!H6.
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:U13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 13859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `cb86e8d7c651|VOLATILE_FUNCTION|Sheet1!K1`

- workbook: `all_data_912_v0.1/spreadsheet/51894/3_51894_input.xlsx`
- location: `Sheet1!K1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!K1.
- cached value: 2024-05-29 00:00:00; row labels: ["'CM Target'", '"Today\'s Date"']; column header: ''; used range: A1:K11
- neighbourhood: J1: "Today's Date" | K1: '=TODAY()' -> 2024-05-29 00:00:00

### `f97521719691|VOLATILE_FUNCTION|Open!P4`

- workbook: `all_data_912_v0.1/spreadsheet/105-24/2_105-24_input.xlsx`
- location: `Open!P4`  severity: Low  confidence: Info
- formula: `=INT(TODAY()-D4+(1))`
- evidence: 20 formula(s) on Open use TODAY or NOW, so their results change with the clock: Open!P4, Open!P5, Open!P6, Open!P7, Open!P8, Open!P9, Open!P10, Open!P11, ....
- cached value: None; row labels: ["'Perform Peer Review'", "'gsj65824'"]; column header: "'DM Age'"; used range: A1:S23
- neighbourhood: N3: 'Changed On' | O3: 'Time of change' | P3: 'DM Age' | N4: 2023-05-03 00:00:00 | O4: 16:48:09 | P4: '=INT(TODAY()-D4+(1))' -> None | N5: 2023-04-27 00:00:00 | O5: 18:53:30 | P5: '=INT(TODAY()-D5+(1))' -> None | N6: 2023-04-28 00:00:00 | O6: 18:10:33 | P6: '=INT(TODAY()-D6+(1))' -> None

## WHITESPACE_KEY

### `ac9c457a4aed|WHITESPACE_KEY|Compiledandlocatedschoolsda!L2`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!L2`  severity: Medium  confidence: Review
- evidence: Raw value is ' CA13 9BH'; the other text values in this column are not padded.
- cached value: ' CA13 9BH'; row labels: ["' Cambridge Street'", "' Barrow-In-Furness'"]; column header: "'Postcode'"; used range: A1:AJ1419
- neighbourhood: J1: 'Address4' | K1: 'Address5' | L1: 'Postcode' | M1: 'Title' | N1: 'Initial' | L2: ' CA13 9BH' | M2: 'Mrs' | N2: 'S' | J3: ' Grange-Over-Sands' | L3: ' LA11 6SN' | M3: 'C' | N3: 'Mason' | L4: ' CA1 1JB' | M4: 'Mr' | N4: 'K'

### `411e282dd1c8|WHITESPACE_KEY|COVER!A23`

- workbook: `all_data_912_v0.1/spreadsheet/56915/3_56915_input.xlsx`
- location: `COVER!A23`  severity: Medium  confidence: Review
- evidence: Raw value is '        STUFF 3'; the other text values in this column are not padded.
- cached value: '        STUFF 3'; row labels: []; column header: "'        STUFF 2'"; used range: A1:E23
- neighbourhood: A21: '        STUFF 1' | B21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> 1227.87225264468 | C21: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A21,IF(DATA!... -> '#N/A' | A22: '        STUFF 2' | B22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> -66.5945609096971 | C22: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A22,IF(DATA!... -> '#N/A' | A23: '        STUFF 3' | B23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> 2482.02750258874 | C23: '=INDEX(DATA!$B$18:$AC$24,MATCH(1,IF(DATA!$A$18:$A$24=$A23,IF(DATA!... -> '#N/A'

### `c561c810150e|WHITESPACE_KEY|Sheet1!B40`

- workbook: `all_data_912_v0.1/spreadsheet/54675/2_54675_input.xlsx`
- location: `Sheet1!B40`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Marjory Mackie'"; used range: A1:F2452
- neighbourhood: A38: 4 | B38: 'Building Services' | A39: 4 | B39: 'Marjory Mackie' | A40: 4 | B40: 'Angela McConnell ' | A41: 4 | B41: 'Sandy Ross, Building Services' | A42: 4 | B42: 'Ralph Bell'

### `736a1dfb4636|WHITESPACE_KEY|Sheet1!M12`

- workbook: `all_data_912_v0.1/spreadsheet/CF_24784/3_CF_24784_input.xlsx`
- location: `Sheet1!M12`  severity: Medium  confidence: Review
- evidence: Raw value is 'HOME '; the other text values in this column are not padded.
- cached value: 'HOME '; row labels: ["'HOME'", "'AWAY'"]; column header: "'AWAY'"; used range: A1:U29
- neighbourhood: K10: 'HOME' | L10: 'DRAW' | M10: 'AWAY' | N10: 'HOME' | K11: 'HOME' | L11: 'AWAY' | M11: 'AWAY' | N11: 'DRAW' | K12: 'HOME' | L12: 'AWAY' | M12: 'HOME ' | N12: 'HOME' | K13: 'AWAY' | L13: 'AWAY' | M13: 'AWAY' | N13: 'HOME' | K14: 'HOME' | L14: 'AWAY' | M14: 'HOME ' | N14: 'HOME'

### `2f8c049b867d|WHITESPACE_KEY|Inventory!A10`

- workbook: `all_data_912_v0.1/spreadsheet/32895/1_32895_input.xlsx`
- location: `Inventory!A10`  severity: Medium  confidence: Review
- evidence: Raw value is 'WHIPPET 5KG '; the other text values in this column are not padded.
- cached value: 'WHIPPET 5KG '; row labels: []; column header: "'FINOWHIP250G'"; used range: A1:C16
- neighbourhood: A8: 'FINOWHIP 500G' | B8: 'B005' | C8: 0 | A9: 'FINOWHIP250G' | B9: 'B006' | A10: 'WHIPPET 5KG ' | B10: 'B007' | A11: 'WHIPPET 1KG' | B11: 'B008' | A12: 'WHIPPET 500G' | B12: 'B009'

### `7b8131bea152|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/312-46/2_312-46_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Raw value is 'ID '; the other text values in this column are not padded.
- cached value: 'ID '; row labels: []; column header: "'Table 1'"; used range: A1:F24
- neighbourhood: A1: 'Table 1' | A2: 'ID ' | B2: 'Test' | A3: 'a' | B3: 1 | A4: 'b' | B4: 1

### `adfb0542e52f|WHITESPACE_KEY|After!A9`

- workbook: `all_data_912_v0.1/spreadsheet/230-16/1_230-16_input.xlsx`
- location: `After!A9`  severity: Medium  confidence: Review
- evidence: Raw value is '2020-02-23 14:40:10.997 '; the other text values in this column are not padded.
- cached value: '2020-02-23 14:40:10.997 '; row labels: []; column header: "'2020-02-23 14:40:11.141 '"; used range: A1:B10
- neighbourhood: A7: '2020-02-23 14:40:11.184 ' | B7: 'event_type="BUSINESS"' | A8: '2020-02-23 14:40:11.141 ' | B8: 'event_type="BUSINESS"' | A9: '2020-02-23 14:40:10.997 ' | B9: 'event_type="BUSINESS"' | A10: '2020-02-23 14:40:10.431 ' | B10: 'event_type="BUSINESS"'

### `b3b8477b9402|WHITESPACE_KEY|Sheet1!A130`

- workbook: `all_data_912_v0.1/spreadsheet/290-27/1_290-27_input.xlsx`
- location: `Sheet1!A130`  severity: Medium  confidence: Review
- evidence: Raw value is 'GG '; the other text values in this column are not padded.
- cached value: 'GG '; row labels: []; column header: "'NAME'"; used range: A1:I139
- neighbourhood: A128: 'NAME' | B128: 'GG 6' | C128: 'Clm 16000' | A130: 'GG ' | B130: 2020-08-29 00:00:00 | C130: 'GG 6' | A132: 'CATS BLAME'

### `9ba8f22c1ad0|WHITESPACE_KEY|Sheet1!M6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_24784/1_CF_24784_input.xlsx`
- location: `Sheet1!M6`  severity: Medium  confidence: Review
- evidence: Raw value is 'HOME '; the other text values in this column are not padded.
- cached value: 'HOME '; row labels: ["'HOME'", "'AWAY'"]; column header: "'Villa  Baggies'"; used range: A1:U29
- neighbourhood: K4: 'Wolves  Burnley' | L4: 'Leeds  Man  Unt' | M4: 'Villa  Baggies' | N4: 'Leicester  Crystal  Pal' | K6: 'HOME' | L6: 'AWAY' | M6: 'HOME ' | N6: 'HOME' | K7: 'HOME' | L7: 'AWAY' | M7: 'HOME ' | N7: 'HOME' | K8: 'HOME' | L8: 'AWAY' | M8: 'DRAW' | N8: 'HOME'

### `37d41403fe20|WHITESPACE_KEY|WK1!C2`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `WK1!C2`  severity: Low  confidence: Info
- evidence: 22 of 23 text values in column C carry leading or trailing whitespace, for example ' Diced Bramley Apple - 10Kg - '; this looks like fixed-width padding from an export.
- cached value: ' Diced Bramley Apple - 10Kg - '; row labels: ["'APPLE001'"]; column header: "'Item Description'"; used range: A1:S3567
- neighbourhood: A1: '#' | B1: 'Item No.' | C1: 'Item Description' | D1: 'Quantity' | E1: 'Status' | A2: 1 | B2: 'APPLE001' | C2: ' Diced Bramley Apple - 10Kg - ' | D2: 700 | E2: '0' | A3: 2 | B3: 'APPLE001' | C3: ' Diced Bramley Apple - 10Kg - ' | D3: 700 | E3: '0' | A4: 3 | B4: 'APPLE001' | C4: ' Diced Bramley Apple - 10Kg - ' | D4: 700 | E4: '0'

### `53fb4bf35e11|WHITESPACE_KEY|Sheet1!A55`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/3_CF_6540_input.xlsx`
- location: `Sheet1!A55`  severity: Medium  confidence: Review
- evidence: Raw value is 'Approved Electrician '; the other text values in this column are not padded.
- cached value: 'Approved Electrician '; row labels: []; column header: "'Approved Electrician C&G 2391 Tester'"; used range: A1:CL123
- neighbourhood: A53: 'Electrical Supervisor' | A54: 'Approved Electrician C&G 2391 Tester' | A55: 'Approved Electrician ' | A56: 'Assistant Electrician' | A57: 'OLEC 1 '

### `950cdc594b54|WHITESPACE_KEY|After!A6`

- workbook: `all_data_912_v0.1/spreadsheet/230-16/3_230-16_input.xlsx`
- location: `After!A6`  severity: Medium  confidence: Review
- evidence: Raw value is '2020-02-23 14:40:11.618 '; the other text values in this column are not padded.
- cached value: '2020-02-23 14:40:11.618 '; row labels: []; column header: "'2020-02-23 14:41:01.412'"; used range: A1:B10
- neighbourhood: A4: '2020-02-22 14:35:59.356666' | B4: 'event_type="BUSINESS"' | A5: '2020-02-23 14:41:01.412' | B5: 'event_type="BUSINESS"' | A6: '2020-02-23 14:40:11.618 ' | B6: 'event_type="BUSINESS"' | A7: '2020-02-23 14:40:11.184 ' | B7: 'event_type="BUSINESS"' | A8: '2020-02-23 14:40:11.141 ' | B8: 'event_type="BUSINESS"'

### `b2d0d6365d71|WHITESPACE_KEY|Sheet1!B40`

- workbook: `all_data_912_v0.1/spreadsheet/54675/1_54675_input.xlsx`
- location: `Sheet1!B40`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Marjory Mackie'"; used range: A1:F2452
- neighbourhood: A38: 4 | B38: 'Building Services' | A39: 4 | B39: 'Marjory Mackie' | A40: 4 | B40: 'Angela McConnell ' | A41: 4 | B41: 'Sandy Ross, Building Services' | A42: 4 | B42: 'Ralph Bell'

### `4cfd58a6f68f|WHITESPACE_KEY|DATA!A24`

- workbook: `all_data_912_v0.1/spreadsheet/56915/1_56915_input.xlsx`
- location: `DATA!A24`  severity: Medium  confidence: Review
- evidence: Raw value is '        STUFF 3'; the other text values in this column are not padded.
- cached value: '        STUFF 3'; row labels: []; column header: "'        STUFF 2'"; used range: A1:AC24
- neighbourhood: A22: '        STUFF 1' | B22: 49887.7048682951 | C22: 0.0263935626775246 | A23: '        STUFF 2' | B23: -3390.80544821547 | C23: -0.00179393773197299 | A24: '        STUFF 3' | B24: 128564.289829883 | C24: 0.0680181549877828

### `16655eaea0b3|WHITESPACE_KEY|Sheet1!A73`

- workbook: `all_data_912_v0.1/spreadsheet/368-44/1_368-44_input.xlsx`
- location: `Sheet1!A73`  severity: Medium  confidence: Review
- evidence: Raw value is 'Financial               '; the other text values in this column are not padded.
- cached value: 'Financial               '; row labels: []; column header: "'REPORT END'"; used range: A1:J87
- neighbourhood: A71: 'REPORT END' | A73: 'Financial               ' | B73: 'Count' | C73: 'Total' | A74: 'Z1/Sales by TP       /10-08-2021/09:29' | A75: 'REPORT END'

### `da1e266217a2|WHITESPACE_KEY|Sheet1!A85`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/1_CF_6540_input.xlsx`
- location: `Sheet1!A85`  severity: Medium  confidence: Review
- evidence: Raw value is 'Steel Fixer '; the other text values in this column are not padded.
- cached value: 'Steel Fixer '; row labels: []; column header: "'Cable Puller'"; used range: A1:CL123
- neighbourhood: A83: 'Skilled Operative' | A84: 'Cable Puller' | A85: 'Steel Fixer ' | A86: 'Concreter ' | A87: 'Concrete Finisher '

### `b4bb29667c08|WHITESPACE_KEY|Sheet1!A9`

- workbook: `all_data_912_v0.1/spreadsheet/48930/1_48930_input.xlsx`
- location: `Sheet1!A9`  severity: Medium  confidence: Review
- evidence: Raw value is 'Tony '; the other text values in this column are not padded.
- cached value: 'Tony '; row labels: []; column header: "'Philip'"; used range: A1:E9
- neighbourhood: A7: 'Sandy' | B7: 'PK' | C7: 2017-10-10 00:00:00 | A8: 'Philip' | B8: 'PK' | C8: 2017-11-02 00:00:00 | A9: 'Tony ' | B9: 'PK' | C9: 2018-03-13 00:00:00

### `b2d0d6365d71|WHITESPACE_KEY|Sheet1!B23`

- workbook: `all_data_912_v0.1/spreadsheet/54675/1_54675_input.xlsx`
- location: `Sheet1!B23`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '; the other text values in this column are not padded.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Building Services'"; used range: A1:F2452
- neighbourhood: A21: 4 | B21: 'Angela McConnell ' | A22: 4 | B22: 'Building Services' | A23: 4 | B23: 'Angela McConnell ' | A24: 4 | B24: 'Angela McConnell ' | A25: 4 | B25: 'Phyllis McFadyen'

### `cc14175a29f0|WHITESPACE_KEY|Sheet1!A73`

- workbook: `all_data_912_v0.1/spreadsheet/368-44/2_368-44_input.xlsx`
- location: `Sheet1!A73`  severity: Medium  confidence: Review
- evidence: Raw value is 'Financial               '; the other text values in this column are not padded.
- cached value: 'Financial               '; row labels: []; column header: "'REPORT END'"; used range: A1:J87
- neighbourhood: A71: 'REPORT END' | A73: 'Financial               ' | B73: 'Count' | C73: 'Total' | A74: 'Z1/Sales by TP       /10-08-2021/09:29' | A75: 'REPORT END'

### `d724d7c85d8e|WHITESPACE_KEY|NOV23!A14`

- workbook: `all_data_912_v0.1/spreadsheet/50534/3_50534_input.xlsx`
- location: `NOV 23!A14`  severity: Medium  confidence: Review
- evidence: Raw value is 'COURTNEY '; the other text values in this column are not padded.
- cached value: 'COURTNEY '; row labels: []; column header: "'DONITA'"; used range: A1:I27
- neighbourhood: A12: 'ANDREW' | B12: '(206)571-7535' | C12: '7A-3P' | A13: 'DONITA' | B13: '(253)431-9941' | C13: '11P-7A' | A14: 'COURTNEY ' | B14: '(602)918-4633' | A15: 'TOM' | B15: '206-852-5614' | C15: '3-11' | A16: 'EDITH' | B16: '509-778-2033'

### `0e8785562296|WHITESPACE_KEY|DATA!A21`

- workbook: `all_data_912_v0.1/spreadsheet/56915/2_56915_input.xlsx`
- location: `DATA!A21`  severity: Medium  confidence: Review
- evidence: Raw value is '      STUFF'; the other text values in this column are not padded.
- cached value: '      STUFF'; row labels: []; column header: "'    COST OF GOODS SOLD'"; used range: A1:AC24
- neighbourhood: A20: '    COST OF GOODS SOLD' | A21: '      STUFF' | A22: '        STUFF 1' | B22: 49887.7048682951 | C22: 0.0263935626775246 | A23: '        STUFF 2' | B23: -3390.80544821547 | C23: -0.00179393773197299

### `d7ca7b8ac452|WHITESPACE_KEY|Inflexion!A13`

- workbook: `all_data_912_v0.1/spreadsheet/18645/1_18645_input.xlsx`
- location: `Inflexion!A13`  severity: Medium  confidence: Review
- evidence: Raw value is 'SMD '; the other text values in this column are not padded.
- cached value: 'SMD '; row labels: []; column header: "'CCG'"; used range: A1:C56
- neighbourhood: A11: 'Griffin Global Group' | B11: 2009 | C11: 'Travel/Logistics' | A12: 'CCG' | B12: 2009 | C12: 'Legal Disputes' | A13: 'SMD ' | B13: 2008 | C13: 'Submersibles' | A14: 'Jack Wills' | B14: 2007 | C14: 'Retail' | A15: 'Aspen Pumps' | B15: 2007 | C15: 'Air Conditioning'

### `34ca77355303|WHITESPACE_KEY|Inventory!A6`

- workbook: `all_data_912_v0.1/spreadsheet/32895/3_32895_input.xlsx`
- location: `Inventory!A6`  severity: Medium  confidence: Review
- evidence: Raw value is 'FINO WHIP 5KG '; the other text values in this column are not padded.
- cached value: 'FINO WHIP 5KG '; row labels: []; column header: "'PLASTIC ICING 500G'"; used range: A1:C16
- neighbourhood: A4: 'PLASTIC ICING 1KG ' | B4: 'B001' | C4: 100 | A5: 'PLASTIC ICING 500G' | B5: 'B003' | C5: 90 | A6: 'FINO WHIP 5KG ' | B6: 'B004' | C6: 247 | A7: 'FINO WHIP 1KG' | B7: 'B005' | C7: 0 | A8: 'FINOWHIP 500G' | B8: 'B005' | C8: 0

### `adfb0542e52f|WHITESPACE_KEY|After!A6`

- workbook: `all_data_912_v0.1/spreadsheet/230-16/1_230-16_input.xlsx`
- location: `After!A6`  severity: Medium  confidence: Review
- evidence: Raw value is '2020-02-23 14:40:11.618 '; the other text values in this column are not padded.
- cached value: '2020-02-23 14:40:11.618 '; row labels: []; column header: "'2020-02-23 14:41:01.412'"; used range: A1:B10
- neighbourhood: A4: '2020-02-22 14:35:59.356666' | B4: 'event_type="BUSINESS"' | A5: '2020-02-23 14:41:01.412' | B5: 'event_type="BUSINESS"' | A6: '2020-02-23 14:40:11.618 ' | B6: 'event_type="BUSINESS"' | A7: '2020-02-23 14:40:11.184 ' | B7: 'event_type="BUSINESS"' | A8: '2020-02-23 14:40:11.141 ' | B8: 'event_type="BUSINESS"'

### `c72923c9ab96|WHITESPACE_KEY|Sheet1!A17`

- workbook: `all_data_912_v0.1/spreadsheet/40892/1_40892_input.xlsx`
- location: `Sheet1!A17`  severity: Medium  confidence: Review
- evidence: Raw value is 'Trousers Black '; the other text values in this column are not padded.
- cached value: 'Trousers Black '; row labels: []; column header: "'Top Red'"; used range: A1:D17
- neighbourhood: A15: 'Purple Scarf' | A16: 'Top Red' | A17: 'Trousers Black '

## WHOLE_COLUMN_REFERENCE

### `37d41403fe20|WHOLE_COLUMN_REFERENCE|Statistics!B5`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!B5`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX('WK1'!$A:$R,_xlfn.AGGREGATE(15,6,ROW('WK1'!$B$2:$B$40)/('WK1'!$B$2:$B$40=$A$3),ROWS(B$5:B5)),MATCH(B$4,'WK1'!$1:$1,0)),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 212 cells on this sheet; the others are Statistics!C5, Statistics!D5, Statistics!E5, Statistics!B6, Statistics!C6, Statistics!D6, Statistics!E6, Statistics!B7, ....
- cached value: 700; row labels: ["'WK1'"]; column header: "'Quantity'"; used range: A1:AF100
- range 'WK1'!$B$2:$B$40: values ["'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE025'", "'APPLE025'", "'APPLE025'", "'APPLE033'", "'APPLE033'"]; beyond: {'above': "B1: 'Item No.'", 'below': 'B41: None'}
- neighbourhood: A3: 'APPLE025' | B3: '=VLOOKUP(A3,Data!A2:B248,2,FALSE)' -> ' 10mm Diced Bramley Apple,... | A4: 'Batch' | B4: 'Quantity' | C4: 'Weeks in Storage' | D4: 'Storage Cost' | A5: 'WK1' | B5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 700 | C5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 3.4285714285714284 | D5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.542857142857143 | B6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 700 | C6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 3.4285714285714284 | D6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.542857142857143 | B7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 240 | C7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 3.4285714285714284 | D7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.542857142857143

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!J2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!J3, Volym P5_P6_2023!J4, Volym P5_P6_2023!J5, Volym P5_P6_2023!J6, Volym P5_P6_2023!J7, Volym P5_P6_2023!J8, Volym P5_P6_2023!J9, Volym P5_P6_2023!J10.
- cached value: '200000001,200000002,200000000'; row labels: ["'ABC1'"]; column header: "'Source list Agreement (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000000 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '46022,45657,45291' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000001,200000002,200000... | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000001,460000002,460000... | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `b5cf69fbd13d|WHOLE_COLUMN_REFERENCE|Sheet1!P8`

- workbook: `all_data_912_v0.1/spreadsheet/530-28/3_530-28_input.xlsx`
- location: `Sheet1!P8`  severity: Medium  confidence: Review
- formula: `=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2:$A$176&"",$A$2:$A$176&"",)=ROW($1:$175),ROW($2:$176),4^8),COLUMN(J$1)))&""`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 2 cells on this sheet; the others are Sheet1!Q8.
- cached value: 'XD19020016'; row labels: ["'SCD181202515'", "'XO18120141'"]; column header: "'Order number'"; used range: A1:T100
- range $B$2:$B$176: values ["'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'"]; beyond: {'above': "B1: 'Construction order No'", 'below': 'B177: None'}
- neighbourhood: N6: '' | O6: '' | P8: '=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2... -> 'XD19020016' | Q8: '=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2... -> 'XD19010581'

### `64aece717e7d|WHOLE_COLUMN_REFERENCE|Sheet2!A8`

- workbook: `all_data_912_v0.1/spreadsheet/52640/2_52640_input.xlsx`
- location: `Sheet2!A8`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/(RAW!$G$2:$G$50>0),ROWS(A$8:A8)),MATCH(A$6,RAW!$A$1:$U$1,0)),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 272 cells on this sheet; the others are Sheet2!B8, Sheet2!C8, Sheet2!D8, Sheet2!E8, Sheet2!F8, Sheet2!G8, Sheet2!H8, Sheet2!A9, ....
- cached value: 201525; row labels: []; column header: "'Advert Id'"; used range: A1:H50
- range RAW!$G$2:$G$50: values ['0', '0', '0', '0', '0', '0', '3', '3', '1', '2', '3', '1']; beyond: {'above': "G1: 'Unfilled Ending within 7 Days'", 'below': 'G51: None'}
- neighbourhood: A6: 'Advert Id' | B6: 'Site' | C6: 'Unfilled Ending within 7 Days' | B7: '(Assending order A-z)' | A8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201525 | B8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | A9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201530 | B9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | A10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201549 | B10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1

### `acb548947286|WHOLE_COLUMN_REFERENCE|Statistics!B5`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!B5`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX('WK1'!$A:$R,_xlfn.AGGREGATE(15,6,ROW('WK1'!$B$2:$B$40)/('WK1'!$B$2:$B$40=$A$3),ROWS(B$5:B5)),MATCH(B$4,'WK1'!$1:$1,0)),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 212 cells on this sheet; the others are Statistics!C5, Statistics!D5, Statistics!E5, Statistics!B6, Statistics!C6, Statistics!D6, Statistics!E6, Statistics!B7, ....
- cached value: 700; row labels: ["'WK1'"]; column header: "'Quantity'"; used range: A1:AF100
- range 'WK1'!$B$2:$B$40: values ["'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE001'", "'APPLE025'", "'APPLE025'", "'APPLE025'", "'APPLE033'", "'APPLE033'"]; beyond: {'above': "B1: 'Item No.'", 'below': 'B41: None'}
- neighbourhood: A3: 'APPLE033' | B3: '=VLOOKUP(A3,Data!A2:B248,2,FALSE)' -> ' 20mm Diced Bramley Apple ... | A4: 'Batch' | B4: 'Quantity' | C4: 'Weeks in Storage' | D4: 'Storage Cost' | A5: 'WK1' | B5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 700 | C5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 25.428571428571427 | D5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 55.94285714285714 | B6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 700 | C6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 25.428571428571427 | D6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 55.94285714285714 | B7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 620 | C7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 25.428571428571427 | D7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 55.94285714285714

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!K2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!K2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!K3, Volym P5_P6_2023!K4, Volym P5_P6_2023!K5, Volym P5_P6_2023!K6, Volym P5_P6_2023!K7, Volym P5_P6_2023!K8, Volym P5_P6_2023!K9, Volym P5_P6_2023!K10.
- cached value: '460000003,460000005'; row labels: ["'ABC2'"]; column header: "'Source list Vendor (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007'

### `eb31bc468d52|WHOLE_COLUMN_REFERENCE|Form!D6`

- workbook: `all_data_912_v0.1/spreadsheet/59969/2_59969_input.xlsx`
- location: `Form!D6`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3)*(Report!$B$2:$B$70000=Form!$B$5),ROW(Report!$A$2:$A$70000)),ROWS($A$1:A1))),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 146 cells on this sheet; the others are Form!E6, Form!F6, Form!G6, Form!H6, Form!I6, Form!J6, Form!K6, Form!L6, ....
- cached value: 250; row labels: []; column header: "'NA Balance'"; used range: A1:M26
- range Report!$A$2:$A$70000: values ['None', '2073000108', '2073000108', '2073000108', '2073000108', '2073000108', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116']; beyond: {'above': 'A1: None', 'below': 'A70001: None'}
- neighbourhood: B5: 110018401 | D5: 'NA Balance' | E5: 'PA Balance' | F5: 'TA Balance' | D6: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 250 | E6: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F6: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D7: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 73.97 | E7: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F7: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D8: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | E8: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F8: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0

### `5358e587d475|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/1_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, ....
- cached value: 2014-04-08 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-08 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-03-24 00:00:00

### `8a16f4351e90|WHOLE_COLUMN_REFERENCE|Sheet1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/57743/1_57743_input.xlsx`
- location: `Sheet1!B3`  severity: Medium  confidence: Review
- formula: `=INDEX(D:D,MATCH(A3,C:C,0))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 15 cells on this sheet; the others are Sheet1!B4, Sheet1!B5, Sheet1!B8, Sheet1!B9, Sheet1!B10, Sheet1!B11, Sheet1!B12, Sheet1!B13, ....
- cached value: 312.625; row labels: ["'4GXCA003AC6HUA'"]; column header: ''; used range: A1:D19
- neighbourhood: A1: 'Model' | C1: 'Model Number' | D1: 'Cost' | A2: '4GXCA001AC6HUA' | B2: '=INDEX(D:D,MATCH(A2,C:C,0))' -> '#N/A' | C2: 'A4MXB1832AC6HA' | D2: 328 | A3: '4GXCA003AC6HUA' | B3: '=INDEX(D:D,MATCH(A3,C:C,0)) {array B3}' -> 312.625 | C3: 'A4MXA3036AC6HA' | D3: 338 | A4: '4GXCB002AC6HUA' | B4: '=INDEX(D:D,MATCH(A4,C:C,0)) {array B4}' -> '#N/A' | C4: 'A4MXB3642AC6HA' | D4: 338 | A5: '4GXCB004AC6HUA' | B5: '=INDEX(D:D,MATCH(A5,C:C,0)) {array B5}' -> '#N/A' | C5: 'A4MXC3642AC6HA' | D5: 360

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!K2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!K2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!K3, Volym P5_P6_2023!K4, Volym P5_P6_2023!K5, Volym P5_P6_2023!K6, Volym P5_P6_2023!K7, Volym P5_P6_2023!K8, Volym P5_P6_2023!K9, Volym P5_P6_2023!K10.
- cached value: '460000003,460000005'; row labels: ["'ABC2'"]; column header: "'Source list Vendor (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '46022,45657,45291'; row labels: ["'ABC1'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000000 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000000 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '46022,45657,45291' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000001,200000002,200000... | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000001,460000002,460000... | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '44926,45657'; row labels: ["'ABC2'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!J2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!J3, Volym P5_P6_2023!J4, Volym P5_P6_2023!J5, Volym P5_P6_2023!J6, Volym P5_P6_2023!J7, Volym P5_P6_2023!J8, Volym P5_P6_2023!J9, Volym P5_P6_2023!J10.
- cached value: '200000003,200000005'; row labels: ["'ABC2'"]; column header: "'Source list Agreement (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007'

### `df2b81a5f43c|WHOLE_COLUMN_REFERENCE|Sheet1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/57743/3_57743_input.xlsx`
- location: `Sheet1!B3`  severity: Medium  confidence: Review
- formula: `=INDEX(D:D,MATCH(A3,C:C,0))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 15 cells on this sheet; the others are Sheet1!B4, Sheet1!B5, Sheet1!B8, Sheet1!B9, Sheet1!B10, Sheet1!B11, Sheet1!B12, Sheet1!B13, ....
- cached value: 386; row labels: ["'A4MXC4248AC6HA'"]; column header: ''; used range: A1:D19
- neighbourhood: A1: 'Model' | C1: 'Model Number' | D1: 'Cost' | A2: 'A4MXB1832AC6HA' | B2: '=INDEX(D:D,MATCH(A2,C:C,0))' -> 328 | C2: 'A4MXB1832AC6HA' | D2: 328 | A3: 'A4MXC4248AC6HA' | B3: '=INDEX(D:D,MATCH(A3,C:C,0)) {array B3}' -> 386 | C3: 'A4MXA3036AC6HA' | D3: 338 | A4: 'A4MXD4248AC6HA' | B4: '=INDEX(D:D,MATCH(A4,C:C,0)) {array B4}' -> 418 | C4: 'A4MXB3642AC6HA' | D4: 338 | A5: 'A4MXC4260AC3HA' | B5: '=INDEX(D:D,MATCH(A5,C:C,0)) {array B5}' -> 468 | C5: 'A4MXC3642AC6HA' | D5: 360

### `593afcf306d6|WHOLE_COLUMN_REFERENCE|Sheet1!P8`

- workbook: `all_data_912_v0.1/spreadsheet/530-28/2_530-28_input.xlsx`
- location: `Sheet1!P8`  severity: Medium  confidence: Review
- formula: `=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2:$A$176&"",$A$2:$A$176&"",)=ROW($1:$175),ROW($2:$176),4^8),COLUMN(J$1)))&""`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 2 cells on this sheet; the others are Sheet1!Q8.
- cached value: 'XD19010576'; row labels: ["'SCD181202515'", "'XO18120141'"]; column header: "'Order number'"; used range: A1:T100
- range $B$2:$B$176: values ["'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'", "'SCD181202515'"]; beyond: {'above': "B1: 'Construction order No'", 'below': 'B177: None'}
- neighbourhood: N6: '' | O6: '' | P8: '=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2... -> 'XD19010576' | Q8: '=INDEX($A:$A,SMALL(IF(($B$2:$B$176&$C$2:$C$176=$E2&$F2)*MATCH($A$2... -> None

### `b31624554d1c|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7000 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `97d36b88791d|WHOLE_COLUMN_REFERENCE|Sheet1!G4`

- workbook: `all_data_912_v0.1/spreadsheet/41410/3_41410_input.xlsx`
- location: `Sheet1!G4`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$22="Lighting"),ROWS(G$4:G4))),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are Sheet1!H4, Sheet1!G5, Sheet1!H5.
- cached value: 5; row labels: ["'Lighting'", "'Lighting'"]; column header: "'kW rating'"; used range: A1:H22
- range $B$4:$B$22: values ["'Lighting'", "'Lighting'", "'Cooling'", "'Lighting'", "'Heating'", "'Other'", "'Lighting'", "'Heating'", "'Lighting'", "'Other'", 'None', 'None']; beyond: {'above': "B3: 'Item'", 'below': 'B23: None'}
- neighbourhood: F2: 'Output:' | F3: 'Item' | G3: 'kW rating' | H3: 'Number' | F4: 'Lighting' | G4: '=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 5 | H4: '=IFERROR(INDEX(D:D,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 2 | F5: 'Lighting' | G5: '=IFERROR(INDEX(C:C,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 50 | H5: '=IFERROR(INDEX(D:D,_xlfn.AGGREGATE(15,6,ROW($B$4:$B$22)/($B$4:$B$2... -> 1

### `61bf2143f38b|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/2_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, ....
- cached value: '#VALUE!'; row labels: ["'F100066'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100066' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `47eb61dd533e|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `be6378a48fb9|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/2_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `b569de1c5256|WHOLE_COLUMN_REFERENCE|Sheet2!A8`

- workbook: `all_data_912_v0.1/spreadsheet/52640/1_52640_input.xlsx`
- location: `Sheet2!A8`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/(RAW!$G$2:$G$50>0),ROWS(A$8:A8)),MATCH(A$6,RAW!$A$1:$U$1,0)),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 272 cells on this sheet; the others are Sheet2!B8, Sheet2!C8, Sheet2!D8, Sheet2!E8, Sheet2!F8, Sheet2!G8, Sheet2!H8, Sheet2!A9, ....
- cached value: 201525; row labels: []; column header: "'Advert Id'"; used range: A1:H50
- range RAW!$G$2:$G$50: values ['0', '0', '0', '0', '0', '0', '3', '3', '1', '2', '3', '1']; beyond: {'above': "G1: 'Unfilled Ending within 7 Days'", 'below': 'G51: None'}
- neighbourhood: A6: 'Advert Id' | B6: 'Site' | C6: 'Unfilled Ending within 7 Days' | B7: '(Assending order A-z)' | A8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201525 | B8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | A9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201530 | B9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | A10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201549 | B10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1

### `5d1887987f48|WHOLE_COLUMN_REFERENCE|Sheet2!A8`

- workbook: `all_data_912_v0.1/spreadsheet/52640/3_52640_input.xlsx`
- location: `Sheet2!A8`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/(RAW!$G$2:$G$50>0),ROWS(A$8:A8)),MATCH(A$6,RAW!$A$1:$U$1,0)),"")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 272 cells on this sheet; the others are Sheet2!B8, Sheet2!C8, Sheet2!D8, Sheet2!E8, Sheet2!F8, Sheet2!G8, Sheet2!H8, Sheet2!A9, ....
- cached value: 201525; row labels: []; column header: "'Advert Id'"; used range: A1:H50
- range RAW!$G$2:$G$50: values ['0', '0', '0', '0', '0', '0', '3', '66', '1', '2', '3', '1']; beyond: {'above': "G1: 'Unfilled Ending within 7 Days'", 'below': 'G51: None'}
- neighbourhood: A6: 'Advert Id' | B6: 'Site' | C6: 'Unfilled Ending within 7 Days' | B7: '(Assending order A-z)' | A8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201525 | B8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C8: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | A9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201530 | B9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 66 | A10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201549 | B10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1

### `0e309a2a0da6|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/2_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, ....
- cached value: 'PEPEPEPEPE'; row labels: ["'no'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE'

### `286f4ae7ac70|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/3_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, ....
- cached value: '#VALUE!'; row labels: ["'F100063'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `740614797bbb|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/1_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, ....
- cached value: 'PEPEPEPEPE'; row labels: ["'YES'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N2}' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N3}' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N4}' -> 'PEPEPEPEPE'
