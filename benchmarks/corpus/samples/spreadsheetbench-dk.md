# Finding cards: spreadsheetbench

Generated 2026-10-05T01:48:44+00:00 from benchmarks/corpus/results/spreadsheetbench-dk with seed 7, up to 25 per rule and 2 per workbook.

Label each card in `labels/<source>.json` as `TP` (the auditor is right), `FP` (it is wrong), or `unsure`, with a one-line reason.

## BROKEN_REFERENCE

### `5d8557dfb652|BROKEN_REFERENCE|July-KPIs!B6`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!B6`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A6),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 31 cells on this sheet; the others are July-KPIs!B7, July-KPIs!B8, July-KPIs!B9, July-KPIs!B10, July-KPIs!B11, July-KPIs!B12, July-KPIs!B13, July-KPIs!B14, and 22 more.
- cached value: None; row labels: []; column header: "'Paid Worked Hours'"; used range: A1:T3212
- neighbourhood: A4: 'Date' | B4: 'Paid Worked Hours' | C4: 'Calls Target' | C5: 'Inbound' | D5: 'Outbound' | A6: '=IF(ROWS(A$6:A6)>DAY(J$13),"",J$12+ROWS(A$6:A6)-1)' -> 2021-07-04 00:00:00 | B6: '=IFERROR(VLOOKUP(($C$1&"|"&A6),#REF!,2,0),"")' -> None | A7: '=IF(ROWS(A$6:A7)>DAY(J$13),"",J$12+ROWS(A$6:A7)-1)' -> 2021-07-05 00:00:00 | B7: '=IFERROR(VLOOKUP(($C$1&"|"&A7),#REF!,2,0),"")' -> None | A8: '=IF(ROWS(A$6:A8)>DAY(J$13),"",J$12+ROWS(A$6:A8)-1)' -> 2021-07-06 00:00:00 | B8: '=IFERROR(VLOOKUP(($C$1&"|"&A8),#REF!,2,0),"")' -> None

### `3ccd5643c7a2|BROKEN_REFERENCE|Sheet1!B1`

- workbook: `all_data_912_v0.1/spreadsheet/56637/3_56637_input.xlsx`
- location: `Sheet1!B1`  severity: Low  confidence: Info
- formula: `=VLOOKUP(D1,'[1]Order Data'!$A:$B,2,FALSE)`
- evidence: 7 cell(s) on Sheet1 link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Sheet1!B1, Sheet1!C3, Sheet1!D3, Sheet1!E3, Sheet1!F3, Sheet1!G3, Sheet1!H3.
- cached value: 'Period 3/ Wk3'; row labels: ["'Period/Week'"]; column header: ''; used range: A1:Q110
- neighbourhood: A1: 'Period/Week' | B1: "=VLOOKUP(D1,'[1]Order Data'!$A:$B,2,FALSE)" -> 'Period 3/ Wk3' | C1: 'Week' | D1: 2021-04-11 00:00:00 | A2: 'DOW' | B2: 'Mon' | C2: 'Tue' | D2: 'Wed' | A3: 'Orders' | B3: 300.5398 | C3: "=VLOOKUP($B$1,'[1]Order Data'!$B:$J,4,FALSE)" -> 261.7022 | D3: "=VLOOKUP($B$1,'[1]Order Data'!$B:$J,5,FALSE)" -> 261.7022

### `6d5548493a93|BROKEN_REFERENCE|July-KPIs!F6`

- workbook: `all_data_912_v0.1/spreadsheet/1726/1_1726_input.xlsx`
- location: `July-KPIs!F6`  severity: High  confidence: Defect
- formula: `=VLOOKUP(C1,#REF!,2,0)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: "'Summary'"; used range: A1:T3212
- neighbourhood: F4: 'Summary' | D5: 'Outbound' | E5: 'Total Daily' | E6: '=IFERROR(((C6*1.3)+(D6*1))/((B6)),"0")' -> '0' | F6: '=VLOOKUP(C1,#REF!,2,0)' -> '#REF!' | E7: '=IFERROR(((C7*1.3)+(D7*1))/((B7)),"0")' -> '0' | E8: '=IFERROR(((C8*1.3)+(D8*1))/((B8)),"0")' -> '0'

### `a556b2a52595|BROKEN_REFERENCE|Sheet1!C6`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!C6`  severity: High  confidence: Defect
- formula: `=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY8,0),""),"")`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 7 cells on this sheet; the others are Sheet1!C7, Sheet1!C8, Sheet1!C9, Sheet1!C10, Sheet1!C11, Sheet1!C12.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A4: 2023-10-16 00:00:00 | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | A5: 2023-10-23 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None

### `acb548947286|BROKEN_REFERENCE|Statistics!G6`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G6`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 51 cells on this sheet; the others are Statistics!G7, Statistics!G8, Statistics!G9, Statistics!G10, Statistics!G11, Statistics!G12, Statistics!G13, Statistics!G14, and 42 more.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E4: 'Value' | F4: 'Avg Total Cost per Kg' | E5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.5 | F5: '=SUM(D58:E58)/B58' -> 0.028449711723254324 | G5: "=COUNTIF('WK1'!B2:B1968,Statistics!$A$3)" -> 4 | E6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.5 | G6: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.5 | G7: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E8: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 7.5 | G8: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `95bb09d93e8b|BROKEN_REFERENCE|Foglio1!G2`

- workbook: `all_data_912_v0.1/spreadsheet/55965/2_55965_input.xlsx`
- location: `Foglio1!G2`  severity: Low  confidence: Info
- formula: `=INDEX([1]DATI!$J$1:$J$999,LARGE(INDEX(ROW([1]DATI!$K$2:$K$999)*([1]DATI!$K$2:$K$999=$E2),),G$1))`
- evidence: 2 cell(s) on Foglio1 link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Foglio1!G2, Foglio1!G3.
- cached value: '3-2'; row labels: []; column header: ''; used range: A1:P18
- range DATI!$J$1:$J$999: values ["'TOT'", "'1-1'", "'2-0'", "'1-0'", "'0-0'", "'2-0'", "'2-1'", "'3-2'", "'1-1'", "'2-1'", "'2-0'", "'0-0'"]; beyond: {'below': 'J1000: None'}
- neighbourhood: E1: 'IG' | G1: 9 | H1: 9 | I1: 8 | E2: 330 | G2: '=INDEX([1]DATI!$J$1:$J$999,LARGE(INDEX(ROW([1]DATI!$K$2:$K$999)*([... -> '3-2' | H2: '3-2' | I2: '0-0' | E3: 320 | G3: '=INDEX([1]DATI!$J$1:$J$999,LARGE(INDEX(ROW([1]DATI!$K$2:$K$999)*([... -> '3-1' | H3: '3-1' | I3: '2-0' | E4: 330

### `7dfe4964af12|BROKEN_REFERENCE|Sheet1!B14|0dcee9`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!B14`  severity: High  confidence: Defect
- formula: `=IF(IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),"")=0,"",IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),""))`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: A12: 2023-12-11 00:00:00 | C12: '=IF(AND(B12>0,$AW14>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D12: '=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A13: 2023-12-18 00:00:00 | C13: '=IF(AND(B13>0,$AW15>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A15,$BD$4:$B... -> None | D13: '=IF(AND(B13>0,$AW15>0),IFERROR(_xlfn.XLOOKUP($A15,$BD$4:$BD$82,$BF... -> None | A14: 2023-12-25 00:00:00 | B14: '=IF(IFERROR(INDEX(\'[1]UPS & Billing Data\'!$B$3:$BL$81,MATCH($A16... -> None | C14: '=IF(AND(B14>0,$AW16>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A16,$BD$4:$B... -> None | D14: '=IF(AND(B14>0,$AW16>0),IFERROR(_xlfn.XLOOKUP($A16,$BD$4:$BD$82,$BF... -> None

### `7bd972dd1e37|BROKEN_REFERENCE|July-KPIs!B6`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!B6`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A6),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 31 cells on this sheet; the others are July-KPIs!B7, July-KPIs!B8, July-KPIs!B9, July-KPIs!B10, July-KPIs!B11, July-KPIs!B12, July-KPIs!B13, July-KPIs!B14, and 22 more.
- cached value: None; row labels: []; column header: "'Paid Worked Hours'"; used range: A1:T3212
- neighbourhood: A4: 'Date' | B4: 'Paid Worked Hours' | C4: 'Calls Target' | C5: 'Inbound' | D5: 'Outbound' | A6: '=IF(ROWS(A$6:A6)>DAY(J$13),"",J$12+ROWS(A$6:A6)-1)' -> 2021-07-02 00:00:00 | B6: '=IFERROR(VLOOKUP(($C$1&"|"&A6),#REF!,2,0),"")' -> None | A7: '=IF(ROWS(A$6:A7)>DAY(J$13),"",J$12+ROWS(A$6:A7)-1)' -> 2021-07-03 00:00:00 | B7: '=IFERROR(VLOOKUP(($C$1&"|"&A7),#REF!,2,0),"")' -> None | A8: '=IF(ROWS(A$6:A8)>DAY(J$13),"",J$12+ROWS(A$6:A8)-1)' -> 2021-07-04 00:00:00 | B8: '=IFERROR(VLOOKUP(($C$1&"|"&A8),#REF!,2,0),"")' -> None

### `43493e031c73|BROKEN_REFERENCE|Dati!CF12`

- workbook: `all_data_912_v0.1/spreadsheet/55912/1_55912_input.xlsx`
- location: `Dati!CF12`  severity: High  confidence: Defect
- formula: `=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1))*(#REF!="SI"))`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 4 cells on this sheet; the others are Dati!CG12, Dati!CF17, Dati!CG17.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:CJ40
- neighbourhood: CF12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CG12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CF13: '=1-(CF12/AG2)' -> '#REF!' | CG13: '=1-(CG12/AG2)' -> '#REF!' | CF14: '=1/CF13' -> '#REF!' | CG14: '=1/CG13' -> '#REF!'

### `c2c1c9ef2579|BROKEN_REFERENCE|formamspnc(7)!I10`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!I10`  severity: High  confidence: Defect
- formula: `=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10=""),NOT(BH11="")),6,IF(AND(AR10=0,BH10="b"),"X",IF(AR10=0,"Y",""))))`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: ["'14c/19c/21c/24c/28c/36c/39c/50c/55c/58c/66c/70c(1 ext 1u..."]; column header: ''; used range: A1:ED48610
- neighbourhood: G8: '=IF(AND(OR(F8=1,F8=2),OR(BH8="b",BH8="c",BH8=1)),1,IF(AND(OR(AD8=$... -> None | H8: '=IF(OR(AND(K8="D",L8="E",M8="F"),AND(ISNUMBER(BI8),G8=2)),"H",IF(O... -> None | I8: '=IF(AND(NOT(BH8=""),NOT(BH9=""),NOT(BH10="")),7,IF(AND(NOT(BH8="")... -> None | J8: '=IF(AND(OR(H8="h",AND(K8="d",L8="e"),AND(L8="e",M8="f"),AND(K8="d"... -> None | K8: '=IF(AND(AE8=0,AF8=0,ISNUMBER(BI8)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> None | G9: '=IF(AND(OR(F9=1,F9=2),OR(BH9="b",BH9="c",BH9=1)),1,IF(AND(OR(AD9=$... -> None | H9: '=IF(OR(AND(K9="D",L9="E",M9="F"),AND(ISNUMBER(BI9),G9=2)),"H",IF(O... -> None | I9: '=IF(AND(NOT(BH9=""),NOT(BH10=""),NOT(BH11="")),7,IF(AND(NOT(BH9=""... -> None | J9: '=IF(AND(OR(H9="h",AND(K9="d",L9="e"),AND(L9="e",M9="f"),AND(K9="d"... -> None | K9: '=IF(AND(AE9=0,AF9=0,ISNUMBER(BI9)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> 'D' | G10: '=IF(AND(OR(F10=1,F10=2),OR(BH10="b",BH10="c",BH10=1)),1,IF(AND(OR(... -> None | H10: '=IF(OR(AND(K10="D",L10="E",M10="F"),AND(ISNUMBER(BI10),G10=2)),"H"... -> None | I10: '=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10... -> '#REF!' | J10: '=IF(AND(OR(H10="h",AND(K10="d",L10="e"),AND(L10="e",M10="f"),AND(K... -> None | K10: '=IF(AND(AE10=0,AF10=0,ISNUMBER(BI10)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None | G11: '=IF(AND(OR(F11=1,F11=2),OR(BH11="b",BH11="c",BH11=1)),1,IF(AND(OR(... -> None | H11: '=IF(OR(AND(K11="D",L11="E",M11="F"),AND(ISNUMBER(BI11),G11=2)),"H"... -> None | I11: '=IF(AND(NOT(BH11=""),NOT(#REF!=""),NOT(#REF!="")),7,IF(AND(NOT(BH1... -> '#REF!' | J11: '=IF(AND(OR(H11="h",AND(K11="d",L11="e"),AND(L11="e",M11="f"),AND(K... -> None | K11: '=IF(AND(AE11=0,AF11=0,ISNUMBER(BI11)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None

### `30c6f4937476|BROKEN_REFERENCE|HR!GC3`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !GC3`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 29 cells on this sheet; the others are HR !GC4, HR !GC5, HR !FC7, HR !FN7, HR !GC7, HR !GC9, HR !FC10, HR !FN10, and 20 more.
- cached value: '#REF!'; row labels: ["'Month 3'", "'Month 1'"]; column header: "'Paid last month?'"; used range: A1:GT37
- neighbourhood: GA2: 'Total' | GB2: 'Holiday + Total' | GC2: 'Paid last month?' | GD2: 'HR to pay?' | GE2: 'What to do?' | GA3: 95.6934 | GB3: 107.24359338 | GC3: '=#REF!' -> '#REF!' | GD3: '=IF(GB3>99.99,"Yes","No")' -> 'Yes' | GE3: 'Month 2' | GA4: 578.1699 | GB4: 647.95500693 | GC4: '=#REF!' -> '#REF!' | GD4: '=IF(GB4>99.99,"Yes","No")' -> 'Yes' | GE4: '=IF(ISNUMBER(SEARCH("Yes",GD4)),GB4,"")' -> 647.95500693 | GA5: 396.694 | GB5: 443.3679658 | GC5: '=#REF!' -> '#REF!' | GD5: 'Yes' | GE5: 'Month 6'

### `c05e60f72c61|BROKEN_REFERENCE|Dati!CF12`

- workbook: `all_data_912_v0.1/spreadsheet/55912/2_55912_input.xlsx`
- location: `Dati!CF12`  severity: High  confidence: Defect
- formula: `=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1))*(#REF!="SI"))`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 4 cells on this sheet; the others are Dati!CG12, Dati!CF17, Dati!CG17.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:CJ40
- neighbourhood: CF12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CG12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CF13: '=1-(CF12/AG2)' -> '#REF!' | CG13: '=1-(CG12/AG2)' -> '#REF!' | CF14: '=1/CF13' -> '#REF!' | CG14: '=1/CG13' -> '#REF!'

### `29e8f5fbc26c|BROKEN_REFERENCE|Result!J1`

- workbook: `all_data_912_v0.1/spreadsheet/55085/2_55085_input.xlsx`
- location: `Result!J1`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 2 cells on this sheet; the others are Result!L1.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:L13
- neighbourhood: J1: '=#REF!' -> '#REF!' | K1: '=J1' -> '#REF!' | L1: '=#REF!' -> '#REF!' | H2: 'Mango' | I2: 'Banana' | J2: 'Apple' | K2: 'Mango' | L2: 'Banana' | H3: '=G3' -> 'Shrawan' | I3: '=H3' -> 'Shrawan' | J3: 'Bhadra' | K3: '=J3' -> 'Bhadra' | L3: '=K3' -> 'Bhadra'

### `2069bdc39cd5|BROKEN_REFERENCE|Result!J1`

- workbook: `all_data_912_v0.1/spreadsheet/55085/1_55085_input.xlsx`
- location: `Result!J1`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 2 cells on this sheet; the others are Result!L1.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:L13
- neighbourhood: J1: '=#REF!' -> '#REF!' | K1: '=J1' -> '#REF!' | L1: '=#REF!' -> '#REF!' | H2: 'Mango' | I2: 'Banana' | J2: 'Apple' | K2: 'Mango' | L2: 'Banana' | H3: '=G3' -> 'Shrawan' | I3: '=H3' -> 'Shrawan' | J3: 'Bhadra' | K3: '=J3' -> 'Bhadra' | L3: '=K3' -> 'Bhadra'

### `a4ee03c3468a|BROKEN_REFERENCE|HR!D3`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !D3`  severity: High  confidence: Defect
- formula: `=INDEX(#REF!,MATCH('HR '!A3,#REF!,0))`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 13 cells on this sheet; the others are HR !D4, HR !D5, HR !D7, HR !D8, HR !D10, HR !D11, HR !D12, HR !D14, and 4 more.
- cached value: '#REF!'; row labels: ["'Test'"]; column header: "'Holiday Payment'"; used range: A1:GT37
- neighbourhood: B2: 'Vetter Name' | C2: 'Month' | D2: 'Holiday Payment' | E2: 'Total' | F2: 'Holiday + Total' | B3: 'Test' | C3: 2019-05-01 00:00:00 | D3: "=INDEX(#REF!,MATCH('HR '!A3,#REF!,0))" -> '#REF!' | E3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | F3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | B4: 'Tst' | C4: 2019-05-01 00:00:00 | D4: "=INDEX(#REF!,MATCH('HR '!A4,#REF!,0))" -> '#REF!' | E4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | F4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | B5: 'Atsuko Kodera' | C5: 2019-05-01 00:00:00 | D5: "=INDEX(#REF!,MATCH('HR '!A5,#REF!,0))" -> '#REF!' | E5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | F5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!'

### `a94eb6a7585f|BROKEN_REFERENCE|HR!GR13`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !GR13`  severity: High  confidence: Defect
- formula: `=SUM(#REF!,FZ13,GK13)`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 3 cells on this sheet; the others are HR !GS13, HR !GT13.
- cached value: '#REF!'; row labels: ["'Month 3'", "'Month 3'"]; column header: ''; used range: A1:GT37
- neighbourhood: GP11: '=IF(ISNUMBER(SEARCH("Yes",GO11)),GM11,"")' -> 146.58621516 | GP12: '=IF(ISNUMBER(SEARCH("Yes",GO12)),GM12,"")' -> 422.18427636 | GP13: 'Month 3' | GQ13: 'Month 3' | GR13: '=SUM(#REF!,FZ13,GK13)' -> '#REF!' | GS13: '=SUM(#REF!,GA13,GL13)' -> '#REF!' | GT13: '=SUM(#REF!,GB13,GM13)' -> '#REF!' | GP14: 'Month 1' | GQ14: 'Month 1' | GP15: '=IF(ISNUMBER(SEARCH("Yes",GO15)),GM15,"")' -> 138.57713719

### `0c0e0e5f0156|BROKEN_REFERENCE|Sheet1!B13`

- workbook: `all_data_912_v0.1/spreadsheet/49237/2_49237_input.xlsx`
- location: `Sheet1!B13`  severity: High  confidence: Defect
- formula: `=#REF!`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: ["'Letter Dates'"]; column header: "'Joe George Veteran\\n8675309 Lane NE\\nJenny, MN 12345'"; used range: A1:L27
- neighbourhood: A11: 'Letter Name' | A12: 'VBMS-A Remarks' | A13: 'Letter Dates' | B13: '=#REF!' -> '#REF!' | A14: 'Letter Dates' | A15: 'Calculator Name'

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!B14|0dcee9`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!B14`  severity: High  confidence: Defect
- formula: `=IF(IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),"")=0,"",IFERROR(INDEX('[1]UPS & Billing Data'!$B$3:$BL$81,MATCH($A16,'[1]UPS & Billing Data'!$A$3:$A$70,0),MATCH(_xlfn.CONCAT("Total ",#REF!),'[1]UPS & Billing Data'!$B$2:$BL$2,0)),""))`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: A12: 2023-12-11 00:00:00 | C12: '=IF(AND(B12>0,$AW14>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D12: '=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A13: 2023-12-18 00:00:00 | C13: '=IF(AND(B13>0,$AW15>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A15,$BD$4:$B... -> None | D13: '=IF(AND(B13>0,$AW15>0),IFERROR(_xlfn.XLOOKUP($A15,$BD$4:$BD$82,$BF... -> None | A14: 2023-12-25 00:00:00 | B14: '=IF(IFERROR(INDEX(\'[1]UPS & Billing Data\'!$B$3:$BL$81,MATCH($A16... -> None | C14: '=IF(AND(B14>0,$AW16>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP($A16,$BD$4:$B... -> None | D14: '=IF(AND(B14>0,$AW16>0),IFERROR(_xlfn.XLOOKUP($A16,$BD$4:$BD$82,$BF... -> None

### `506d9df5a3af|BROKEN_REFERENCE|TaskAssesment!A4`

- workbook: `all_data_912_v0.1/spreadsheet/46444/1_46444_input.xlsx`
- location: `Task Assesment!A4`  severity: Low  confidence: Info
- formula: `=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkDays!$A$2:$A$100000=$B4),ROW([2]tblWorkDays!$D$2:$D$100000)-1,""),ROWS($A$1:$A$1))),"")`
- evidence: 6 cell(s) on Task Assesment link to [2]; external links are inventoried but not followed, so their cached values are taken as given: Task Assesment!A4, Task Assesment!E4, Task Assesment!A5, Task Assesment!E5, Task Assesment!A6, Task Assesment!E6.
- cached value: 2018-11-09 00:00:00; row labels: []; column header: "'Dates'"; used range: A1:L6
- neighbourhood: A3: 'Dates' | B3: 'Date code' | C3: 'Activity ID' | A4: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B4: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 24 | C4: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 68 | A5: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B5: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 25 | C5: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 69 | A6: '=IFERROR(INDEX([2]tblWorkDays!$D$2:$D$100000,SMALL(IF(([2]tblWorkD... -> 2018-11-09 00:00:00 | B6: '=IFERROR(INDEX(tblTaskActivities!$B$2:$B$14705,SMALL(IF((tblTaskAc... -> 25 | C6: '=IFERROR(INDEX(tblTaskActivities!$A$2:$A$14705,SMALL(IF((tblTaskAc... -> 69

### `611a47e3b917|BROKEN_REFERENCE|Sheet1!A19`

- workbook: `all_data_912_v0.1/spreadsheet/382-10/3_382-10_input.xlsx`
- location: `Sheet1!A19`  severity: High  confidence: Defect
- formula: `=IFERROR(#REF!/#REF!,0)`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:A19
- neighbourhood: A17: 4.4 | A18: 4.5 | A19: '=IFERROR(#REF!/#REF!,0)' -> None

### `596a7d18841b|BROKEN_REFERENCE|Streets!G3`

- workbook: `all_data_912_v0.1/spreadsheet/13284/1_13284_input.xlsx`
- location: `Streets!G3`  severity: Low  confidence: Info
- formula: `=IFERROR(VLOOKUP(E3,[1]Assistente!R6:S23,2,0)," ")`
- evidence: 2 cell(s) on Streets link to [1]; external links are inventoried but not followed, so their cached values are taken as given: Streets!G3, Streets!G4.
- cached value: ' '; row labels: ["'Avenida Braz De Pina'", "'Mario'"]; column header: "'Observação'"; used range: A1:G26
- neighbourhood: E1: 'Área' | F1: 'Assistente' | G1: 'Observação' | F2: 'Paulo Mauricio' | F3: 'Mario' | G3: '=IFERROR(VLOOKUP(E3,[1]Assistente!R6:S23,2,0)," ")' -> ' ' | F4: 'Celia' | G4: '=IFERROR(VLOOKUP(E4,[1]Assistente!R7:S24,2,0)," ")' -> ' ' | F5: 'Sonia'

### `a4ee03c3468a|BROKEN_REFERENCE|HR!GG3`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !GG3`  severity: High  confidence: Defect
- formula: `=SUM(#REF!,FZ3)`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 6 cells on this sheet; the others are HR !GH3, HR !GI3, HR !GG16, HR !GH16, HR !GI16.
- cached value: '#REF!'; row labels: ["'Month 2'", "'March + April'"]; column header: "'Holiday Payment'"; used range: A1:GT37
- neighbourhood: GG1: 'Accruals only' | GE2: 'What to do?' | GF2: 'Notes' | GG2: 'Holiday Payment' | GH2: 'Total' | GI2: 'Holiday + Total' | GE3: 'Month 2' | GF3: 'March + April' | GG3: '=SUM(#REF!,FZ3)' -> '#REF!' | GH3: '=SUM(#REF!,GA3)' -> '#REF!' | GI3: '=SUM(#REF!,GB3)' -> '#REF!' | GE4: '=IF(ISNUMBER(SEARCH("Yes",GD4)),GB4,"")' -> 647.95500693 | GE5: 'Month 6' | GF5: 'Nov to April' | GG5: '=SUM(#REF!+#REF!+#REF!+#REF!+#REF!+FZ5)' -> '#REF!' | GH5: '=SUM(#REF!+#REF!+#REF!+#REF!+#REF!+GA5)' -> '#REF!' | GI5: '=SUM(#REF!+#REF!+#REF!+#REF!+#REF!+GB5)' -> '#REF!'

### `a696b4bd2604|BROKEN_REFERENCE|Sheet1!A18`

- workbook: `all_data_912_v0.1/spreadsheet/382-10/2_382-10_input.xlsx`
- location: `Sheet1!A18`  severity: High  confidence: Defect
- formula: `=IFERROR(#REF!/#REF!,0)`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:A18
- neighbourhood: A16: 'Comments' | A17: 4.5 | A18: '=IFERROR(#REF!/#REF!,0)' -> None

### `a94eb6a7585f|BROKEN_REFERENCE|HR!D3`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !D3`  severity: High  confidence: Defect
- formula: `=INDEX(#REF!,MATCH('HR '!A3,#REF!,0))`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 13 cells on this sheet; the others are HR !D4, HR !D5, HR !D7, HR !D8, HR !D10, HR !D11, HR !D12, HR !D14, and 4 more.
- cached value: '#REF!'; row labels: ["'Test'"]; column header: "'Holiday Payment'"; used range: A1:GT37
- neighbourhood: B2: 'Vetter Name' | C2: 'Month' | D2: 'Holiday Payment' | E2: 'Total' | F2: 'Holiday + Total' | B3: 'Test' | C3: 2019-05-01 00:00:00 | D3: "=INDEX(#REF!,MATCH('HR '!A3,#REF!,0))" -> '#REF!' | E3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | F3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | B4: 'Tst' | C4: 2019-05-01 00:00:00 | D4: "=INDEX(#REF!,MATCH('HR '!A4,#REF!,0))" -> '#REF!' | E4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | F4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | B5: 'Atsuko Kodera' | C5: 2019-05-01 00:00:00 | D5: "=INDEX(#REF!,MATCH('HR '!A5,#REF!,0))" -> '#REF!' | E5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | F5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!'

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G6`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G6`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- evidence: The same relative formula contains #REF! in 51 cells on this sheet; the others are Statistics!G7, Statistics!G8, Statistics!G9, Statistics!G10, Statistics!G11, Statistics!G12, Statistics!G13, Statistics!G14, and 42 more.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E4: 'Value' | F4: 'Avg Total Cost per Kg' | E5: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 5 | F5: '=SUM(D58:E58)/B58' -> 0.007648083623693379 | G5: "=COUNTIF('WK1'!B2:B1968,Statistics!$A$3)" -> 3 | E6: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 5 | G6: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E7: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> 5 | G7: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E8: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G8: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

## CIRCULAR_REFERENCE

### `b6d10437377d|CIRCULAR_REFERENCE|Sheettwo!E10`

- workbook: `all_data_912_v0.1/spreadsheet/54196/1_54196_input.xlsx`
- location: `Sheet two!E10`  severity: High  confidence: Likely defect
- evidence: 278 cells depend on each other in a cycle: Sheet two!E10 -> Sheet two!E100 -> Sheet two!E101 -> Sheet two!E102 -> Sheet two!E103 -> Sheet two!E104 -> Sheet two!E105 -> Sheet two!E106 -> ...
- cached value: '#N/A'; row labels: ["'2D'", "'0000000098'"]; column header: ''; used range: A1:G6234
- neighbourhood: C8: '2D' | D8: '0000000071' | E8: '=VLOOKUP(G8,Suppliers2[],2,FALSE)' -> '#N/A' | F8: '000225' | G8: '44533388' | C9: '6D' | D9: '0000000075' | E9: '=VLOOKUP(G9,Suppliers2[],2,FALSE)' -> '#N/A' | F9: '000237' | G9: '88713000' | C10: '2D' | D10: '0000000098' | E10: '=VLOOKUP(G10,Suppliers2[],2,FALSE)' -> '#N/A' | F10: '000475' | G10: '70263016' | C11: '3D' | D11: '0000000101' | E11: '=VLOOKUP(G11,Suppliers2[],2,FALSE)' -> '#N/A' | F11: '000552' | G11: '44533388' | C12: '1D' | D12: '0010330231' | E12: '=VLOOKUP(G12,Suppliers2[],2,FALSE)' -> '#N/A' | F12: '000555' | G12: '70263016'

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F3`  severity: High  confidence: Likely defect
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: Test!F3 depends on itself, for example a total whose range includes the total cell.
- evidence: The same relative formula references its own cell in 56 cells on this sheet; the others are Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, Test!F11, and 47 more.
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'OOO' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:25:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `63a66071d918|CIRCULAR_REFERENCE|Sheettwo!E10`

- workbook: `all_data_912_v0.1/spreadsheet/54196/2_54196_input.xlsx`
- location: `Sheet two!E10`  severity: High  confidence: Likely defect
- evidence: 278 cells depend on each other in a cycle: Sheet two!E10 -> Sheet two!E100 -> Sheet two!E101 -> Sheet two!E102 -> Sheet two!E103 -> Sheet two!E104 -> Sheet two!E105 -> Sheet two!E106 -> ...
- cached value: '#N/A'; row labels: ["'2D'", "'0000000098'"]; column header: ''; used range: A1:G6234
- neighbourhood: C8: '2D' | D8: '0000000071' | E8: '=VLOOKUP(G8,Suppliers2[],2,FALSE)' -> '#N/A' | F8: '000225' | G8: '44533388' | C9: '6D' | D9: '0000000075' | E9: '=VLOOKUP(G9,Suppliers2[],2,FALSE)' -> '#N/A' | F9: '000237' | G9: '88713000' | C10: '2D' | D10: '0000000098' | E10: '=VLOOKUP(G10,Suppliers2[],2,FALSE)' -> '#N/A' | F10: '000475' | G10: '70263016' | C11: '3D' | D11: '0000000101' | E11: '=VLOOKUP(G11,Suppliers2[],2,FALSE)' -> '#N/A' | F11: '000552' | G11: '44533388' | C12: '1D' | D12: '0010330231' | E12: '=VLOOKUP(G12,Suppliers2[],2,FALSE)' -> '#N/A' | F12: '000555' | G12: '70263016'

### `70a7680e9819|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/3_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- formula: `=IF(A323="E","",MAX(B$7:B377)+1)`
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- range B$7:B377: values ['417', '418', "''", '419', '420', 'None', '421', '422', '423', '424', 'None', '425']; beyond: {'above': 'B6: None', 'below': 'B378: None'}
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `0a3eeb22d16c|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/2_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- formula: `=IF(A323="E","",MAX(B$7:B377)+1)`
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- range B$7:B377: values ['417', '418', "''", '419', '420', 'None', '421', '422', '423', '424', 'None', '425']; beyond: {'above': 'B6: None', 'below': 'B378: None'}
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F3`  severity: High  confidence: Likely defect
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: Test!F3 depends on itself, for example a total whose range includes the total cell.
- evidence: The same relative formula references its own cell in 56 cells on this sheet; the others are Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, Test!F11, and 47 more.
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:15:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `192a19040f63|CIRCULAR_REFERENCE|Sheettwo!E10`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E10`  severity: High  confidence: Likely defect
- evidence: 278 cells depend on each other in a cycle: Sheet two!E10 -> Sheet two!E100 -> Sheet two!E101 -> Sheet two!E102 -> Sheet two!E103 -> Sheet two!E104 -> Sheet two!E105 -> Sheet two!E106 -> ...
- cached value: '#N/A'; row labels: ["'2D'", "'0000000098'"]; column header: ''; used range: A1:G6234
- neighbourhood: C8: '2D' | D8: '0000000071' | E8: '=VLOOKUP(G8,Suppliers2[],2,FALSE)' -> '#N/A' | F8: '000225' | G8: '44533388' | C9: '6D' | D9: '0000000075' | E9: '=VLOOKUP(G9,Suppliers2[],2,FALSE)' -> '#N/A' | F9: '000237' | G9: '88713000' | C10: '2D' | D10: '0000000098' | E10: '=VLOOKUP(G10,Suppliers2[],2,FALSE)' -> '#N/A' | F10: '000475' | G10: '70263016' | C11: '3D' | D11: '0000000101' | E11: '=VLOOKUP(G11,Suppliers2[],2,FALSE)' -> '#N/A' | F11: '000552' | G11: '44533388' | C12: '1D' | D12: '0010330231' | E12: '=VLOOKUP(G12,Suppliers2[],2,FALSE)' -> '#N/A' | F12: '000555' | G12: '70263016'

### `21bdc0943b23|CIRCULAR_REFERENCE|Sheet1!B323`

- workbook: `all_data_912_v0.1/spreadsheet/48982/1_48982_input.xlsx`
- location: `Sheet1!B323`  severity: High  confidence: Likely defect
- formula: `=IF(A323="E","",MAX(B$7:B377)+1)`
- evidence: Sheet1!B323 depends on itself, for example a total whose range includes the total cell.
- cached value: 0; row labels: []; column header: "''"; used range: A1:B326
- range B$7:B377: values ['417', '418', "''", '419', '420', 'None', '421', '422', '423', '424', 'None', '425']; beyond: {'above': 'B6: None', 'below': 'B378: None'}
- neighbourhood: B322: '' | B323: '=IF(A323="E","",MAX(B$7:B377)+1)' -> 0

### `92f8bf691072|CIRCULAR_REFERENCE|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F3`  severity: High  confidence: Likely defect
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: Test!F3 depends on itself, for example a total whose range includes the total cell.
- evidence: The same relative formula references its own cell in 56 cells on this sheet; the others are Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, Test!F11, and 47 more.
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:15:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

## DUPLICATE_KEY

### `f367b87c90dd|DUPLICATE_KEY|Sheet1!A10,Sheet1!B10`

- workbook: `all_data_912_v0.1/spreadsheet/59185/3_59185_input.xlsx`
- location: `Sheet1!A10, Sheet1!B10`  severity: Medium  confidence: Review
- evidence: Normalized key 'wbnb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'WBNB Splits'; row labels: []; column header: ''; used range: A1:P22
- neighbourhood: B8: 'CBV Splits' | B9: 2124 | A10: 'WBNB Splits' | B10: 'WBNB Splits' | C10: 'Pb Splits' | A11: 2206 | B11: 1820 | C11: 680 | B12: 'WBNB Splits'

### `37d41403fe20|DUPLICATE_KEY|WK1!F1,WK1!P1`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `WK1!F1, WK1!P1`  severity: Medium  confidence: Review
- evidence: Normalized key 'expiry date' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Expiry Date'; row labels: ["'Quantity'", "'Status'"]; column header: ''; used range: A1:S3567
- neighbourhood: D1: 'Quantity' | E1: 'Status' | F1: 'Expiry Date' | G1: 'Value' | H1: 'BatchNum' | D2: 700 | E2: '0' | F2: 1999-12-31 00:00:00 | G2: 10 | H2: 'APPLE00101070' | D3: 700 | E3: '0' | F3: 1999-12-31 00:00:00 | G3: 10 | H3: 'APPLE00101071'

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A14,RS.Food!A409`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A14, RS.Food!A409`  severity: Medium  confidence: Review
- evidence: Normalized key 'omelette' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 49 keys repeat in column A; the others are 'avocado sourdough' 2 times (A15, A301); 'smoked salmon scrambled eggs bri' 2 times (A20, A443); 'fruit salad' 2 times (A30, A349); 'porridge' 2 times (A32, A429); 'egg white omelette' 2 times (A39, A342); 'homemade granola' 2 times (A46, A365); 'protein shake' 2 times (A85, A430); 'fries' 2 times (A184, A346); and 40 more.
- cached value: 'Omelette'; row labels: []; column header: "'Sliced Fruit Plate'"; used range: A1:W607
- neighbourhood: A12: 'Seasonal Berries' | B12: 1512 | C12: 0.00969477488822476 | A13: 'Sliced Fruit Plate' | B13: 1482 | C13: 0.00950241824361713 | A14: 'Omelette' | B14: 1278 | C14: 0.00819439306028521 | A15: 'Avocado Sourdough' | B15: 1248 | C15: 0.00800203641567758 | A16: 'Continental Brf' | B16: 1216 | C16: 0.00779685599476277

### `b7d670f8a092|DUPLICATE_KEY|Sheet1!A8,Sheet1!A20`

- workbook: `all_data_912_v0.1/spreadsheet/48799/1_48799_input.xlsx`
- location: `Sheet1!A8, Sheet1!A20`  severity: Medium  confidence: Review
- evidence: Normalized key 'g' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 6 keys repeat in column A; the others are 'h' 2 times (A9, A21); 'i' 2 times (A10, A22); 'j' 2 times (A11, A23); 'k' 2 times (A12, A24); 'l' 2 times (A13, A25).
- cached value: 'G'; row labels: []; column header: "'F '"; used range: A1:D25
- neighbourhood: A6: 'E' | B6: 7.8 | C6: 6.282 | A7: 'F ' | B7: 6.2 | C7: 7.458 | A8: 'G' | B8: 4.62 | C8: 4.461 | A9: 'H' | B9: 3.47 | C9: 4.7766 | A10: 'I' | B10: 6.72 | C10: 2.94

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K3,URNlookup!K214`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K3, URN lookup!K214`  severity: Medium  confidence: Review
- evidence: Normalized key 'ca9 3qu' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 72 keys repeat in column K; the others are 'ca15 6jn' 2 times (K29, K130); 'ca15 8hn' 2 times (K30, K182); 'la12 9ju' 2 times (K70, K71); 'la14 1ny' 2 times (K72, K203); 'ca2 7lw' 2 times (K83, K1448); 'ca2 6dx' 2 times (K86, K87); 'la10 5al' 2 times (K93, K1213); 'ca2 7be' 2 times (K97, K1400); and 63 more.
- cached value: 'CA9 3QU'; row labels: ["'Church Road'", "'Alston'"]; column header: "'CA15 6QG'"; used range: A1:X1461
- neighbourhood: I1: 'ADDRESS3' | J1: 'TOWN' | K1: 'POSTCODE' | L1: 'SCHSTATUS' | M1: 'OPENDATE' | J2: 'Maryport' | K2: 'CA15 6QG' | L2: 'Open' | J3: 'Alston' | K3: 'CA9 3QU' | L3: 'Open' | J4: 'Carlisle' | K4: 'CA4 9PW' | L4: 'Open' | J5: 'Carlisle' | K5: 'CA6 6PF' | L5: 'Open'

### `b55280430702|DUPLICATE_KEY|Sheet1!B1,Sheet1!I1,Sheet1!P1`

- workbook: `all_data_912_v0.1/spreadsheet/57989/3_57989_input.xlsx`
- location: `Sheet1!B1, Sheet1!I1, Sheet1!P1`  severity: Medium  confidence: Review
- evidence: Normalized key 'friday' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 7 keys repeat in row 1; the others are 'saturday' 3 times (C1, J1, Q1); 'sunday' 3 times (D1, K1, R1); 'monday' 3 times (E1, L1, S1); 'tuesday' 3 times (F1, M1, T1); 'wednesday' 3 times (G1, N1, U1); 'thursday' 2 times (H1, O1).
- cached value: 'Friday'; row labels: []; column header: ''; used range: A1:Y118
- neighbourhood: B1: 'Friday' | C1: 'Saturday' | D1: 'Sunday' | A3: 'Driver 1' | D3: 'hk'

### `bd12e76534e8|DUPLICATE_KEY|Sheet1!A2,Sheet1!A6`

- workbook: `all_data_912_v0.1/spreadsheet/48620/2_48620_input.xlsx`
- location: `Sheet1!A2, Sheet1!A6`  severity: Medium  confidence: Review
- evidence: Normalized key 'pencil' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 2 keys repeat in column A; the others are 'paper' 2 times (A5, A7).
- cached value: 'Pencil'; row labels: []; column header: "'Products'"; used range: A1:F7
- neighbourhood: A1: 'Products' | B1: 'Type' | A2: 'Pencil' | B2: 'Black' | A3: 'Stapler' | B3: 'Black' | A4: 'Ruler' | B4: 'Yellow1'

### `d7bb3bd8958a|DUPLICATE_KEY|Sheet1!B1,Sheet1!I1,Sheet1!P1`

- workbook: `all_data_912_v0.1/spreadsheet/57989/1_57989_input.xlsx`
- location: `Sheet1!B1, Sheet1!I1, Sheet1!P1`  severity: Medium  confidence: Review
- evidence: Normalized key 'friday' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 7 keys repeat in row 1; the others are 'saturday' 3 times (C1, J1, Q1); 'sunday' 3 times (D1, K1, R1); 'monday' 3 times (E1, L1, S1); 'tuesday' 3 times (F1, M1, T1); 'wednesday' 3 times (G1, N1, U1); 'thursday' 2 times (H1, O1).
- cached value: 'Friday'; row labels: []; column header: ''; used range: A1:Y118
- neighbourhood: B1: 'Friday' | C1: 'Saturday' | D1: 'Sunday' | A3: 'Driver 1' | D3: 'hk'

### `484f4df3fe7b|DUPLICATE_KEY|WK1!F1,WK1!P1`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `WK1!F1, WK1!P1`  severity: Medium  confidence: Review
- evidence: Normalized key 'expiry date' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Expiry Date'; row labels: ["'Quantity'", "'Status'"]; column header: ''; used range: A1:S3567
- neighbourhood: D1: 'Quantity' | E1: 'Status' | F1: 'Expiry Date' | G1: 'Value' | H1: 'BatchNum' | D2: 1.5 | E2: '0' | F2: 1999-12-31 00:00:00 | G2: 10 | H2: 'APPLE00101070' | D3: 700 | E3: '0' | F3: 1999-12-31 00:00:00 | G3: 10 | H3: 'APPLE00101071'

### `852b58472b57|DUPLICATE_KEY|Sheet1!A10,Sheet1!B10`

- workbook: `all_data_912_v0.1/spreadsheet/59185/1_59185_input.xlsx`
- location: `Sheet1!A10, Sheet1!B10`  severity: Medium  confidence: Review
- evidence: Normalized key 'wbnb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'WBNB Splits'; row labels: []; column header: ''; used range: A1:P24
- neighbourhood: B8: 'CBV Splits' | B9: 2124 | A10: 'WBNB Splits' | B10: 'WBNB Splits' | C10: 'Pb Splits' | A11: 2206 | B11: 1820 | C11: 680 | B12: 'WBNB Splits'

### `f367b87c90dd|DUPLICATE_KEY|Sheet1!C14,Sheet1!I14`

- workbook: `all_data_912_v0.1/spreadsheet/59185/3_59185_input.xlsx`
- location: `Sheet1!C14, Sheet1!I14`  severity: Medium  confidence: Review
- evidence: Normalized key 'pb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Pb Splits'; row labels: ["'WBNB Splits'", "'KBD Splits'"]; column header: ''; used range: A1:P22
- neighbourhood: B12: 'WBNB Splits' | B13: 2195 | A14: 'WBNB Splits' | B14: 'KBD Splits' | C14: 'Pb Splits' | D14: 'CBV/WBNB sp mix' | A15: 2368 | B15: 1560 | C15: 768 | D15: 252

### `3211215352e9|DUPLICATE_KEY|Grouping!A3,Grouping!A5`

- workbook: `all_data_912_v0.1/spreadsheet/7902/2_7902_input.xlsx`
- location: `Grouping!A3, Grouping!A5`  severity: Medium  confidence: Review
- evidence: Normalized key 'group b' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 2 keys repeat in column A; the others are 'group c' 2 times (A4, A6).
- cached value: 'Group B'; row labels: []; column header: "'Group A'"; used range: A1:I7
- neighbourhood: A1: 'Main Group' | B1: 'Material' | C1: '0 to 6 Month' | A2: 'Group A' | C2: 0.1 | A3: 'Group B' | C3: 0.1 | A4: 'Group C' | C4: 0.05 | A5: 'Group B' | B5: 'Material X' | C5: 0.12

### `acb548947286|DUPLICATE_KEY|WK1!F1,WK1!P1`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `WK1!F1, WK1!P1`  severity: Medium  confidence: Review
- evidence: Normalized key 'expiry date' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Expiry Date'; row labels: ["'Quantity'", "'Status'"]; column header: ''; used range: A1:S3567
- neighbourhood: D1: 'Quantity' | E1: 'Status' | F1: 'Expiry Date' | G1: 'Value' | H1: 'BatchNum' | D2: 700 | E2: '0' | F2: 1999-12-31 00:00:00 | G2: 10 | H2: 'APPLE00101070' | D3: 700 | E3: '0' | F3: 1999-12-31 00:00:00 | G3: 10 | H3: 'APPLE00101071'

### `38117ed54ea2|DUPLICATE_KEY|Grouping!A3,Grouping!A5`

- workbook: `all_data_912_v0.1/spreadsheet/7902/3_7902_input.xlsx`
- location: `Grouping!A3, Grouping!A5`  severity: Medium  confidence: Review
- evidence: Normalized key 'group b' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 2 keys repeat in column A; the others are 'group c' 2 times (A4, A6).
- cached value: 'Group B'; row labels: []; column header: "'Group A'"; used range: A1:I7
- neighbourhood: A1: 'Main Group' | B1: 'Material' | C1: '0 to 6 Month' | A2: 'Group A' | C2: 0 | A3: 'Group B' | C3: 0.1 | A4: 'Group C' | C4: 0.05 | A5: 'Group B' | B5: 'Material X' | C5: 0.12

### `843712f5ec1b|DUPLICATE_KEY|Sheet1!A2,Sheet1!A6`

- workbook: `all_data_912_v0.1/spreadsheet/48620/3_48620_input.xlsx`
- location: `Sheet1!A2, Sheet1!A6`  severity: Medium  confidence: Review
- evidence: Normalized key 'pencil' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Pencil'; row labels: []; column header: "'Products'"; used range: A1:F7
- neighbourhood: A1: 'Products' | B1: 'Type' | A2: 'Pencil' | B2: 'Yellow' | A3: 'Stapler' | B3: 'Yellow1' | A4: 'Ruler' | B4: 'Yellow1'

### `f0d026f067a4|DUPLICATE_KEY|Sheet1!C14,Sheet1!I14`

- workbook: `all_data_912_v0.1/spreadsheet/59185/2_59185_input.xlsx`
- location: `Sheet1!C14, Sheet1!I14`  severity: Medium  confidence: Review
- evidence: Normalized key 'pb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Pb Splits'; row labels: ["'WBNB Splits'", "'KBD Splits'"]; column header: ''; used range: A1:P22
- neighbourhood: B12: 'WBNB Splits' | B13: 2195 | A14: 'WBNB Splits' | B14: 'KBD Splits' | C14: 'Pb Splits' | D14: 'CBV/WBNB sp mix' | A15: 2368 | B15: 1560 | C15: 768 | D15: 252

### `1c06477fced9|DUPLICATE_KEY|URNlookup!K3,URNlookup!K214`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `URN lookup!K3, URN lookup!K214`  severity: Medium  confidence: Review
- evidence: Normalized key 'ca9 3qu' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 72 keys repeat in column K; the others are 'ca15 6jn' 2 times (K29, K130); 'ca15 8hn' 2 times (K30, K182); 'la12 9ju' 2 times (K70, K71); 'la14 1ny' 2 times (K72, K203); 'ca2 7lw' 2 times (K83, K1448); 'ca2 6dx' 2 times (K86, K87); 'la10 5al' 2 times (K93, K1213); 'ca2 7be' 2 times (K97, K1400); and 63 more.
- cached value: 'CA9 3QU'; row labels: ["'Church Road'", "'Alston'"]; column header: "'CA15 6QG'"; used range: A1:X1461
- neighbourhood: I1: 'ADDRESS3' | J1: 'TOWN' | K1: 'POSTCODE' | L1: 'SCHSTATUS' | M1: 'OPENDATE' | J2: 'Maryport' | K2: 'CA15 6QG' | L2: 'Open' | J3: 'Alston' | K3: 'CA9 3QU' | L3: 'Open' | J4: 'Carlisle' | K4: 'CA4 9PW' | L4: 'Open' | J5: 'Carlisle' | K5: 'CA6 6PF' | L5: 'Open'

### `f0d026f067a4|DUPLICATE_KEY|Sheet1!B2,Sheet1!G2`

- workbook: `all_data_912_v0.1/spreadsheet/59185/2_59185_input.xlsx`
- location: `Sheet1!B2, Sheet1!G2`  severity: Medium  confidence: Review
- evidence: Normalized key 'gnb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 2 keys repeat in row 2; the others are 'wbnb' 2 times (J2, K2).
- cached value: 'GNB Splits'; row labels: ["'WBNB Splits'"]; column header: ''; used range: A1:P22
- neighbourhood: A1: 'Top is South' | D1: 'Mill Inventory' | A2: 'WBNB Splits' | B2: 'GNB Splits' | D2: 'CBV/WBNB mix' | A3: 2178 | B3: 1000 | C3: 1192 | D3: 4116 | D4: 'QC HOLD'

### `852b58472b57|DUPLICATE_KEY|Sheet1!B2,Sheet1!G2`

- workbook: `all_data_912_v0.1/spreadsheet/59185/1_59185_input.xlsx`
- location: `Sheet1!B2, Sheet1!G2`  severity: Medium  confidence: Review
- evidence: Normalized key 'gnb splits' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 2 keys repeat in row 2; the others are 'wbnb' 2 times (J2, K2).
- cached value: 'GNB Splits'; row labels: ["'WBNB Splits'"]; column header: ''; used range: A1:P24
- neighbourhood: A1: 'Top is South' | D1: 'Mill Inventory' | A2: 'WBNB Splits' | B2: 'GNB Splits' | D2: 'CBV/WBNB mix' | A3: 2178 | B3: 1026 | C3: 1192 | D3: 4116 | D4: 'QC HOLD'

### `10ace2be6dbc|DUPLICATE_KEY|Sheet1!B5,Sheet1!B7,Sheet1!B10,Sheet1!B14,Sheet1!B20`

- workbook: `all_data_912_v0.1/spreadsheet/59902/1_59902_input.xlsx`
- location: `Sheet1!B5, Sheet1!B7, Sheet1!B10, Sheet1!B14, Sheet1!B20`  severity: Medium  confidence: Review
- evidence: Normalized key 'bob' appears 7 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 3 keys repeat in column B; the others are 'jane' 6 times (B6, B8, B12, B13, ...); 'donald' 10 times (B9, B11, B15, B16, ...).
- cached value: 'Bob'; row labels: []; column header: "'Name'"; used range: A1:H28
- neighbourhood: A3: 'ASCENDING (NOT WORKING)' | A4: 'Date' | B4: 'Name' | C4: 'Days Since Sale' | A5: 2008-08-29 00:00:00 | B5: 'Bob' | C5: '=A5-INDEX($A$4:$A4,MATCH(B5,$B$4:$B4,0),1)' -> '#N/A' | A6: 2008-08-29 00:00:00 | B6: 'Jane' | C6: '=A6-INDEX($A$4:$A5,MATCH(B6,$B$4:$B5,0),1)' -> '#N/A' | A7: 2008-08-30 00:00:00 | B7: 'Bob' | C7: '=A7-INDEX($A$4:$A6,MATCH(B7,$B$4:$B6,0),1)' -> 1

### `7dfe4964af12|DUPLICATE_KEY|Sheet1!BG2,Sheet1!BH2`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!BG2, Sheet1!BH2`  severity: Medium  confidence: Review
- evidence: Normalized key 'case replies' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Case Replies'; row labels: ["'CASE REPLIES'", "'Inbound Calls'"]; column header: ''; used range: A1:BR82
- neighbourhood: BE2: 'Inbound Calls' | BG2: 'Case Replies' | BH2: 'Case Replies' | BI2: 'Customers Helped / Cases Solved' | BE3: 'Goal #' | BF3: 'Goal %' | BG3: 'Goal #' | BH3: 'Goal %' | BI3: 'Goal #' | BE4: 5 | BF4: 7 | BG4: 6 | BH4: 8 | BI4: 7

### `3db55cfd98cc|DUPLICATE_KEY|Sheet2!B3,Sheet2!B12`

- workbook: `all_data_912_v0.1/spreadsheet/52216/3_52216_input.xlsx`
- location: `Sheet2!B3, Sheet2!B12`  severity: Medium  confidence: Review
- evidence: Normalized key 'advertising & marketing' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 3 keys repeat in column B; the others are 'electricity' 2 times (B4, B13); 'insurance' 2 times (B5, B14).
- cached value: 'Advertising & Marketing'; row labels: ["'Regional'"]; column header: ''; used range: A1:G20
- neighbourhood: C1: 1 | D1: 2 | A3: 'Regional' | B3: 'Advertising & Marketing' | C3: 3.44 | D3: 3.17 | A4: 'Regional' | B4: 'Electricity' | C4: 1.24 | D4: 1.8 | A5: 'Regional' | B5: 'Insurance' | C5: 2.56 | D5: 2.53

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A14,RS.Food!A409`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A14, RS.Food!A409`  severity: Medium  confidence: Review
- evidence: Normalized key 'omelette' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 49 keys repeat in column A; the others are 'avocado sourdough' 2 times (A15, A301); 'smoked salmon scrambled eggs bri' 2 times (A20, A443); 'fruit salad' 2 times (A30, A349); 'porridge' 2 times (A32, A429); 'egg white omelette' 2 times (A39, A342); 'homemade granola' 2 times (A46, A365); 'protein shake' 2 times (A85, A430); 'fries' 2 times (A184, A346); and 40 more.
- cached value: 'Omelette'; row labels: []; column header: "'Sliced Fruit Plate'"; used range: A1:W607
- neighbourhood: A12: 'Seasonal Berries' | B12: 1512 | C12: 0.00969477488822476 | A13: 'Sliced Fruit Plate' | B13: 1482 | C13: 0.00950241824361713 | A14: 'Omelette' | B14: 1278 | C14: 0.00819439306028521 | A15: 'Avocado Sourdough' | B15: 1248 | C15: 0.00800203641567758 | A16: 'Continental Brf' | B16: 1216 | C16: 0.00779685599476277

### `ff0beb280ebe|DUPLICATE_KEY|Sheet1!B5,Sheet1!B7,Sheet1!B10,Sheet1!B14,Sheet1!B20`

- workbook: `all_data_912_v0.1/spreadsheet/59902/3_59902_input.xlsx`
- location: `Sheet1!B5, Sheet1!B7, Sheet1!B10, Sheet1!B14, Sheet1!B20`  severity: Medium  confidence: Review
- evidence: Normalized key 'bob' appears 7 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 3 keys repeat in column B; the others are 'jane' 6 times (B6, B8, B12, B13, ...); 'donald' 10 times (B9, B11, B15, B16, ...).
- cached value: 'Bob'; row labels: []; column header: "'Name'"; used range: A1:H28
- neighbourhood: A3: 'ASCENDING (NOT WORKING)' | A4: 'Date' | B4: 'Name' | C4: 'Days Since Sale' | A5: 2008-08-29 00:00:00 | B5: 'Bob' | C5: '=A5-INDEX($A$4:$A4,MATCH(B5,$B$4:$B4,0),1)' -> '#N/A' | A6: 2008-08-29 00:00:00 | B6: 'Jane' | C6: '=A6-INDEX($A$4:$A5,MATCH(B6,$B$4:$B5,0),1)' -> '#N/A' | A7: 2008-08-30 00:00:00 | B7: 'Bob' | C7: '=A7-INDEX($A$4:$A6,MATCH(B7,$B$4:$B6,0),1)' -> 1

### `a4becd1e83e9|DUPLICATE_KEY|Sheet1!A8,Sheet1!A20`

- workbook: `all_data_912_v0.1/spreadsheet/48799/3_48799_input.xlsx`
- location: `Sheet1!A8, Sheet1!A20`  severity: Medium  confidence: Review
- evidence: Normalized key 'g' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- evidence: 6 keys repeat in column A; the others are 'h' 2 times (A9, A21); 'i' 2 times (A10, A22); 'j' 2 times (A11, A23); 'k' 2 times (A12, A24); 'l' 2 times (A13, A25).
- cached value: 'G'; row labels: []; column header: "'F '"; used range: A1:D25
- neighbourhood: A6: 'E' | B6: 7.8 | C6: 6.282 | A7: 'F ' | B7: 6.2 | C7: 7.458 | A8: 'G' | B8: 4.62 | C8: 4.461 | A9: 'H' | B9: 3.47 | C9: 4.7766 | A10: 'I' | B10: 6.72 | C10: 2.94

## FORMULA_DRIFT

### `050df5c328bc|FORMULA_DRIFT|Sheet1!U4`

- workbook: `all_data_912_v0.1/spreadsheet/14240/3_14240_input.xlsx`
- location: `Sheet1!U4`  severity: High  confidence: Likely defect
- formula: `=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=71): =SUMPRODUCT((R4C1:R75C1=RC19)*(R4C2:R75C2=R3C)*(R3C3:R3C16=RC20),R4C3:R75C16)
- evidence: This cell: =SUMPRODUCT((RC[-20]:R[71]C[-20]=RC[-3])*(RC[-19]:R[71]C[-19]=RC[-2])*R[-1]C[-18]:R[-1]C[-8],RC[-18]:R[71]C[-8]=RC[-1])
- cached value: '#VALUE!'; row labels: ["'Individual'", "'3M-25yrs'"]; column header: ''; used range: A1:U75
- range A4:A75: values ["'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'"]; beyond: {'above': "A3: '00 To 35'", 'below': 'A76: None'}
- neighbourhood: S3: 'Members' | T3: 'Sum Insured' | S4: 150000 | T4: '3M-25yrs' | U4: '=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)' -> '#VALUE!' | S5: 150000 | T5: '3M-25yrs' | U5: '=SUMPRODUCT(($A$4:$A$75=$S5)*($B$4:$B$75=U$3)*($C$3:$P$3=$T5),$C$4... -> 0 | S6: 150000 | T6: '3M-25yrs' | U6: '=SUMPRODUCT(($A$4:$A$75=$S6)*($B$4:$B$75=U$3)*($C$3:$P$3=$T6),$C$4... -> 0

### `74d967658eee|FORMULA_DRIFT|Sheet1!Y4`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!Y4`  severity: High  confidence: Likely defect
- formula: `=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=16): =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1],"0")
- evidence: This cell: =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1]," ")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: Z2: '=CONCATENATE(A2," ",B2," ")' -> 'AA AB' | AA2: 'High Scratch Game #1' | W3: '=IF(AND(I2>=12,G3>0),ROUNDDOWN(SUM(200-J2)*0.9,0)+V3," ")' -> None | X3: '=SUM(G3)' -> 291 | Y3: '=IF(AND(I2>=12,G3>0),SUM(ROUNDDOWN(SUM(200-J2)*0.9,0)*3)+X3," ")' -> None | AA3: 'High Scratch Game #2' | W4: '=IF(AND(I3>=12,G4>0),ROUNDDOWN(SUM(200-J3)*0.9,0)+V4," ")' -> None | X4: '=SUM(G4)' -> 372 | Y4: '=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")' -> None | AA4: 'High Scratch Game #3' | W5: '=IF(AND(I4>=12,G5>0),ROUNDDOWN(SUM(200-J4)*0.9,0)+V5," ")' -> None | X5: '=SUM(G5)' -> 0 | Y5: '=IF(AND(I4>=12,G5>0),SUM(ROUNDDOWN(SUM(200-J4)*0.9,0)*3)+X5,"0")' -> '0' | AA5: 'High Scratch Game #4' | W6: '=IF(AND(I5>=12,G6>0),ROUNDDOWN(SUM(200-J5)*0.9,0)+V6," ")' -> None | X6: '=SUM(G6)' -> 340 | Y6: '=IF(AND(I5>=12,G6>0),SUM(ROUNDDOWN(SUM(200-J5)*0.9,0)*3)+X6,"0")' -> '0' | AA6: 'High Scratch Game #5'

### `902b5e29897a|FORMULA_DRIFT|LeadTimes!B5`

- workbook: `all_data_912_v0.1/spreadsheet/47741/1_47741_input.xlsx`
- location: `Lead Times!B5`  severity: High  confidence: Likely defect
- formula: `=_xlfn.TEXTJOIN("-",,WORKDAY(B4,10,K14:K20),WORKDAY(B4,12,K14:K20))`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =WORKDAY(R[-1]C,10,R[9]C[9]:R[15]C[9])
- evidence: This cell: =_XLFN.TEXTJOIN("-",,WORKDAY(R[-1]C,10,R[9]C[9]:R[15]C[9]),WORKDAY(R[-1]C,12,R[9]C[9]:R[15]C[9]))
- cached value: '44572-44574'; row labels: []; column header: ''; used range: A1:O31
- range K14:K20: values ['2021-12-31 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00']; beyond: {'above': 'K13: None', 'below': 'K21: None'}
- neighbourhood: B3: '=calendar {array B3:H3}' -> 44550 | C3: 44551 | D3: 44552 | B4: '=INDEX(calendar,ndx+0) {array B4:H4}' -> 2021-12-27 00:00:00 | C4: 2021-12-28 00:00:00 | D4: 2021-12-29 00:00:00 | B5: '=_xlfn.TEXTJOIN("-",,WORKDAY(B4,10,K14:K20),WORKDAY(B4,12,K14:K20))' -> '44572-44574' | C5: '=WORKDAY(C4,10,L14:L20)' -> 2022-01-12 00:00:00 | D5: '=WORKDAY(D4,10,M14:M20)' -> 2022-01-13 00:00:00 | B6: '=WORKDAY(B4,18,K14:K21)' -> 2022-01-21 00:00:00 | C6: '=WORKDAY(C4,18,L15:L21)' -> 2022-01-21 00:00:00 | D6: '=WORKDAY(D4,18,M15:M21)' -> 2022-01-24 00:00:00 | B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22'

### `9cc23579ce3a|FORMULA_DRIFT|DATACARS!B24`

- workbook: `all_data_912_v0.1/spreadsheet/58829/3_58829_input.xlsx`
- location: `DATA CARS!B24`  severity: High  confidence: Likely defect
- formula: `=Afschrijving!B4`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=3): =AFSCHRIJVING!R[-20]C[10]
- evidence: This cell: =AFSCHRIJVING!R[-20]C
- cached value: 0.73496; row labels: ["'DISCOUNT'"]; column header: ''; used range: A1:F32
- neighbourhood: A22: 'FIRST REGISTARTION' | B22: 2017-05-01 00:00:00 | C22: 2018-05-01 00:00:00 | D22: 2019-05-01 00:00:00 | A23: 'DATE TO BUY' | B23: 2022-05-01 00:00:00 | C23: 2022-05-01 00:00:00 | D23: 2022-05-01 00:00:00 | A24: 'DISCOUNT' | B24: '=Afschrijving!B4' -> 0.73496 | C24: '=Afschrijving!M4' -> 0.665 | D24: '=Afschrijving!N4' -> 0.56998

### `3a2b74c70f66|FORMULA_DRIFT|Total(2)!E31`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!E31`  severity: High  confidence: Likely defect
- formula: `=SUM(B31*0.5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =IFERROR(VLOOKUP(RC8,R27C10:R35C12,3,0)*RC3,0)
- evidence: This cell: =SUM(RC[-3]*0.5)
- cached value: 900; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C' | C32: '=(B32*12)/12' -> 3000 | D32: '=SUM(C32-E32)' -> 1050 | E32: '=IFERROR(VLOOKUP($H32,$J$27:$L$35,3,0)*$C32,0)' -> 1950 | F32: 44589 | G32: 'C' | C33: '=(B33*12)/12' -> 2400 | D33: '=SUM(C33-E33)' -> 480 | E33: '=IFERROR(VLOOKUP($H33,$J$27:$L$35,3,0)*$C33,0)' -> 1920

### `bc56a9f2824a|FORMULA_DRIFT|Total(2)!E31`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!E31`  severity: High  confidence: Likely defect
- formula: `=SUM(B31*0.5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =IFERROR(VLOOKUP(RC8,R27C10:R35C12,3,0)*RC3,0)
- evidence: This cell: =SUM(RC[-3]*0.5)
- cached value: 900; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C' | C32: '=(B32*12)/12' -> 3000 | D32: '=SUM(C32-E32)' -> 1050 | E32: '=IFERROR(VLOOKUP($H32,$J$27:$L$35,3,0)*$C32,0)' -> 1950 | F32: 44589 | G32: 'C' | C33: '=(B33*12)/12' -> 2400 | D33: '=SUM(C33-E33)' -> 480 | E33: '=IFERROR(VLOOKUP($H33,$J$27:$L$35,3,0)*$C33,0)' -> 1920

### `a4ee03c3468a|FORMULA_DRIFT|HR!EU24`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !EU24`  severity: High  confidence: Likely defect
- formula: `=SUMIF(EU2:EU20,"<>#N/A")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =SUMIF(R[-21]C:R[-4]C,"<>#N/A")
- evidence: This cell: =SUMIF(R[-22]C:R[-4]C,"<>#N/A")
- cached value: '#REF!'; row labels: []; column header: "'Holiday + Total'"; used range: A1:GT37
- range EU2:EU20: values ["'Holiday + Total'", "'#REF!'", "'#REF!'", "'#REF!'", 'None', "'#REF!'", "'#REF!'", 'None', "'#REF!'", "'#REF!'", "'#REF!'", 'None']; beyond: {'above': 'EU1: None', 'below': 'EU21: None'}
- neighbourhood: ES23: 'Holiday Payment' | ET23: 'Total' | EU23: 'Holiday + Total' | ES24: '=SUMIF(ES3:ES20,"<>#N/A")' -> '#REF!' | ET24: '=SUMIF(ET3:ET20,"<>#N/A")' -> '#REF!' | EU24: '=SUMIF(EU2:EU20,"<>#N/A")' -> '#REF!'

### `902b5e29897a|FORMULA_DRIFT|LeadTimes!B9`

- workbook: `all_data_912_v0.1/spreadsheet/47741/1_47741_input.xlsx`
- location: `Lead Times!B9`  severity: High  confidence: Likely defect
- formula: `=WORKDAY(B8,10,K14:K24)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =WORKDAY(R[-1]C,10,R[9]C[9]:R[15]C[9])
- evidence: This cell: =WORKDAY(R[-1]C,10,R[5]C[9]:R[15]C[9])
- cached value: 2022-01-17 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range K14:K24: values ['2021-12-31 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None', 'None', 'None', 'None']; beyond: {'above': 'K13: None', 'below': 'K25: None'}
- neighbourhood: B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22' | B8: '=INDEX(calendar,ndx+1) {array B8:H8}' -> 2022-01-03 00:00:00 | C8: 2022-01-04 00:00:00 | D8: 2022-01-05 00:00:00 | B9: '=WORKDAY(B8,10,K14:K24)' -> 2022-01-17 00:00:00 | C9: '=WORKDAY(C8,10,L18:L24)' -> 2022-01-18 00:00:00 | D9: '=WORKDAY(D8,10,M18:M24)' -> 2022-01-19 00:00:00 | B10: '=WORKDAY(B8,18,K19:K25)' -> 2022-01-27 00:00:00 | C10: '=WORKDAY(C8,18,L19:L25)' -> 2022-01-28 00:00:00 | D10: '=WORKDAY(D8,18,M19:M25)' -> 2022-01-31 00:00:00 | B11: '1/6/22-1/10/22' | C11: '1/7/22-1/11/22' | D11: '1/10/22-1/12/22'

### `d3575a4dff7b|FORMULA_DRIFT|HouseBudget!F123`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/2_CF_22493_input.xlsx`
- location: `House Budget!F123`  severity: High  confidence: Likely defect
- formula: `=SUM(G65:G122)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=58): =SUM(RC[1]:RC[25])
- evidence: This cell: =SUM(R[-58]C[1]:R[-1]C[1])
- cached value: 0; row labels: []; column header: ''; used range: A1:AG123
- range G65:G122: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'G64: None', 'below': 'G123: None'}
- neighbourhood: D121: '=F59' -> 0 | E121: "='Money In Checking Next Month'!A58" -> 0 | F121: '=SUM(G121:AE121)' -> 0 | D122: '=F60' -> 0 | E122: "='Money In Checking Next Month'!A59" -> 370 | F122: '=SUM(G122:AE122)' -> 0 | E123: '=SUM(E65:E122)' -> 7237.48 | F123: '=SUM(G65:G122)' -> 0

### `24f6192d8cf3|FORMULA_DRIFT|data!G32`

- workbook: `all_data_912_v0.1/spreadsheet/56225/2_56225_input.xlsx`
- location: `data!G32`  severity: High  confidence: Likely defect
- formula: `=TEXT(F32-E32,"h:mm:ss")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =HOUR(RC[-3])+MINUTE(RC[-3])/60+SECOND(RC[-3])/3600
- evidence: This cell: =TEXT(RC[-1]-RC[-2],"h:mm:ss")
- cached value: '0:00:29'; row labels: ["'gage yount'", "'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: E30: 13:35:01 | F30: 14:21:31 | G30: '=TEXT(F30-E30,"h:mm:ss")' -> '0:46:30' | H30: '=HOUR(E30)+MINUTE(E30)/60+SECOND(E30)/3600' -> 13.5836111111111 | I30: '=HOUR(F30)+MINUTE(F30)/60+SECOND(F30)/3600' -> 14.3586111111111 | E31: 16:06:47 | F31: 17:03:11 | E32: 12:59:13 | F32: 12:59:42 | G32: '=TEXT(F32-E32,"h:mm:ss")' -> '0:00:29' | H32: '=HOUR(E32)+MINUTE(E32)/60+SECOND(E32)/3600' -> 12.9869444444444 | I32: '=HOUR(F32)+MINUTE(F32)/60+SECOND(F32)/3600' -> 12.995 | E33: 14:57:41 | F33: 16:04:19 | E34: 07:58:07 | F34: 08:50:30

### `a94eb6a7585f|FORMULA_DRIFT|HR!FF24`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !FF24`  severity: High  confidence: Likely defect
- formula: `=SUMIF(FF2:FF20,"<>#N/A")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =SUMIF(R[-21]C:R[-4]C,"<>#N/A")
- evidence: This cell: =SUMIF(R[-22]C:R[-4]C,"<>#N/A")
- cached value: '#REF!'; row labels: []; column header: "'Holiday + Total'"; used range: A1:GT37
- range FF2:FF20: values ["'Holiday + Total'", "'#REF!'", "'#REF!'", "'#REF!'", 'None', "'#REF!'", "'#REF!'", 'None', "'#REF!'", "'#REF!'", "'#REF!'", 'None']; beyond: {'above': 'FF1: None', 'below': 'FF21: None'}
- neighbourhood: FD23: 'Holiday Payment' | FE23: 'Total' | FF23: 'Holiday + Total' | FD24: '=SUMIF(FD3:FD20,"<>#N/A")' -> '#REF!' | FE24: '=SUMIF(FE3:FE20,"<>#N/A")' -> '#REF!' | FF24: '=SUMIF(FF2:FF20,"<>#N/A")' -> '#REF!'

### `a94eb6a7585f|FORMULA_DRIFT|HR!BN3`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !BN3`  severity: High  confidence: Likely defect
- formula: `=BR3`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =IF(ISNUMBER(SEARCH("Yes",RC[-1])),RC[-3],"")
- evidence: This cell: =RC[4]
- cached value: '#REF!'; row labels: ["'Month 2'", "'Yes'"]; column header: "'Total to pay'"; used range: A1:GT37
- neighbourhood: BP1: 'Accruals only' | BL2: 'Paid last month?' | BM2: 'HR to pay?' | BN2: 'Total to pay' | BO2: 'Notes' | BP2: 'Holiday Payment' | BL3: '=BB3' -> '#REF!' | BM3: 'Yes' | BN3: '=BR3' -> '#REF!' | BO3: 'Sep-Nov' | BP3: '=AM3+AX3+BI3' -> '#REF!' | BL4: '=BB4' -> '#REF!' | BM4: '=IF(BK4>99.99,"Yes","No")' -> '#REF!' | BN4: '=IF(ISNUMBER(SEARCH("Yes",BM4)),BK4,"")' -> None | BO4: 'N/A' | BL5: '=BB5' -> 'Yes' | BM5: '=IF(BK5>99.99,"Yes","No")' -> '#REF!' | BN5: '=IF(ISNUMBER(SEARCH("Yes",BM5)),BK5,"")' -> None | BO5: 'Month 1'

### `4ea284d68c01|FORMULA_DRIFT|Sheet1!Y4`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!Y4`  severity: High  confidence: Likely defect
- formula: `=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=16): =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1],"0")
- evidence: This cell: =IF(AND(R[-1]C[-16]>=12,RC[-18]>0),SUM(ROUNDDOWN(SUM(200-R[-1]C[-15])*0.9,0)*3)+RC[-1]," ")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: Z2: '=CONCATENATE(A2," ",B2," ")' -> 'AA AB' | AA2: 'High Scratch Game #1' | W3: '=IF(AND(I2>=12,G3>0),ROUNDDOWN(SUM(200-J2)*0.9,0)+V3," ")' -> None | X3: '=SUM(G3)' -> 291 | Y3: '=IF(AND(I2>=12,G3>0),SUM(ROUNDDOWN(SUM(200-J2)*0.9,0)*3)+X3," ")' -> None | AA3: 'High Scratch Game #2' | W4: '=IF(AND(I3>=12,G4>0),ROUNDDOWN(SUM(200-J3)*0.9,0)+V4," ")' -> ' ' | X4: '=SUM(G4)' -> 372 | Y4: '=IF(AND(I3>=12,G4>0),SUM(ROUNDDOWN(SUM(200-J3)*0.9,0)*3)+X4," ")' -> None | AA4: 'High Scratch Game #3' | W5: '=IF(AND(I4>=12,G5>0),ROUNDDOWN(SUM(200-J4)*0.9,0)+V5," ")' -> ' ' | X5: '=SUM(G5)' -> 0 | Y5: '=IF(AND(I4>=12,G5>0),SUM(ROUNDDOWN(SUM(200-J4)*0.9,0)*3)+X5,"0")' -> '0' | AA5: 'High Scratch Game #4' | W6: '=IF(AND(I5>=12,G6>0),ROUNDDOWN(SUM(200-J5)*0.9,0)+V6," ")' -> ' ' | X6: '=SUM(G6)' -> 340 | Y6: '=IF(AND(I5>=12,G6>0),SUM(ROUNDDOWN(SUM(200-J5)*0.9,0)*3)+X6,"0")' -> '0' | AA6: 'High Scratch Game #5'

### `30c6f4937476|FORMULA_DRIFT|HR!Y5`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !Y5`  severity: High  confidence: Likely defect
- formula: `=SUM(F5+N5+V5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =IF(ISNUMBER(SEARCH("Yes",RC[-1])),RC[-3],"")
- evidence: This cell: =SUM(RC[-19]+RC[-11]+RC[-3])
- cached value: '#REF!'; row labels: ["'Month 2'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: W3: '=P3' -> '#REF!' | X3: 'No' | Y3: '=IF(ISNUMBER(SEARCH("Yes",X3)),V3,"")' -> None | Z3: 'June + July ' | AA3: 2019-08-01 00:00:00 | W4: '=P4' -> '#REF!' | X4: '=IF(V4>99.99,"Yes","No")' -> '#REF!' | Y4: '=IF(ISNUMBER(SEARCH("Yes",X4)),V4,"")' -> None | AA4: 2019-08-01 00:00:00 | W5: '=P5' -> '#REF!' | X5: 'Yes' | Y5: '=SUM(F5+N5+V5)' -> '#REF!' | Z5: 'May-July' | AA5: 2019-08-01 00:00:00 | W7: '=P7' -> '#REF!' | X7: '=IF(V7>99.99,"Yes","No")' -> '#REF!' | Y7: '=IF(ISNUMBER(SEARCH("Yes",X7)),V7,"")' -> None | AA7: 2019-08-01 00:00:00

### `1632b774f5f0|FORMULA_DRIFT|Summary!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17111/2_17111_input.xlsx`
- location: `Summary!B2`  severity: High  confidence: Likely defect
- formula: `=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary!$B$1)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=4): =SUMIFS(SHEET1!C[2]:C[2],SHEET1!C:C,SUMMARY!RC[-1],SHEET1!C[1]:C[1],SUMMARY!R1C2)
- evidence: This cell: =SUMIFS(SHEET1!C4:C4,SHEET1!C2:C2,SUMMARY!RC1,SHEET1!C3:C3,SUMMARY!R1C2)
- cached value: 1126; row labels: ["'rahul'"]; column header: "'HD'"; used range: A1:F9
- neighbourhood: A1: 'Name' | B1: 'HD' | C1: 'SD' | A2: 'rahul' | B2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 1126 | C2: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A2,Sheet1!$C:$C,Summary... -> 131 | A3: 'rahul' | B3: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A3,Sheet1!C:C,Summary!$B$1)' -> 1126 | C3: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A3,Sheet1!$C:$C,Summary... -> 131 | A4: 'mohit' | B4: '=SUMIFS(Sheet1!D:D,Sheet1!B:B,Summary!A4,Sheet1!C:C,Summary!$B$1)' -> 954 | C4: '=SUMIFS(Sheet1!$D:$D,Sheet1!$B:$B,Summary!$A4,Sheet1!$C:$C,Summary... -> 586

### `d41f7f014578|FORMULA_DRIFT|Sheet1!F7`

- workbook: `all_data_912_v0.1/spreadsheet/49237/1_49237_input.xlsx`
- location: `Sheet1!F7`  severity: High  confidence: Likely defect
- formula: `=LEFT(F10)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=2): =PROPER(R[-1]C[-1])
- evidence: This cell: =LEFT(R[3]C)
- cached value: 'G'; row labels: ["'AEW Date (Use DOC)'"]; column header: ''; used range: A1:L27
- neighbourhood: E5: '=LEFT(E19,FIND(" ",E19)-1)' -> 'Joe' | E6: '=LEFT(MID(E9,1,1)&MID(E9,2,1)&MID(E9,3,1)&MID(E9,4,1),2*LEN(E9))' -> 'Geor' | F6: '=PROPER(E5)' -> 'Joe' | G6: 'Reopen AEW' | E7: '=RIGHT(E19,LEN(E19)-FIND("*",SUBSTITUTE(E19," ","*",LEN(E19)-LEN(S... -> 'Veteran' | F7: '=LEFT(F10)' -> 'G' | F8: '=PROPER(E7)' -> 'Veteran' | G8: '21-22, 214' | E9: '=TRIM(MID(E19,LEN(E5)+1,LEN(E19)-LEN(E5&E7)))' -> 'George'

### `c212843d66a8|FORMULA_DRIFT|LeadTimes!B6`

- workbook: `all_data_912_v0.1/spreadsheet/47741/2_47741_input.xlsx`
- location: `Lead Times!B6`  severity: High  confidence: Likely defect
- formula: `=WORKDAY(B4,18,K14:K21)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =WORKDAY(R[-2]C,18,R[9]C[9]:R[15]C[9])
- evidence: This cell: =WORKDAY(R[-2]C,18,R[8]C[9]:R[15]C[9])
- cached value: 2022-01-20 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range K14:K21: values ['2021-12-04 00:00:00', '2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None']; beyond: {'above': 'K13: None', 'below': 'K22: None'}
- neighbourhood: B4: '=INDEX(calendar,ndx+0) {array B4:H4}' -> 2021-12-27 00:00:00 | C4: 2021-12-28 00:00:00 | D4: 2021-12-29 00:00:00 | B5: '=_xlfn.TEXTJOIN("-",,WORKDAY(B4,10,K14:K20),WORKDAY(B4,12,K14:K20))' -> '44571-44573' | C5: '=WORKDAY(C4,10,L14:L20)' -> 2022-01-12 00:00:00 | D5: '=WORKDAY(D4,10,M14:M20)' -> 2022-01-13 00:00:00 | B6: '=WORKDAY(B4,18,K14:K21)' -> 2022-01-20 00:00:00 | C6: '=WORKDAY(C4,18,L15:L21)' -> 2022-01-21 00:00:00 | D6: '=WORKDAY(D4,18,M15:M21)' -> 2022-01-24 00:00:00 | B7: '12/30/22-1/4/22' | C7: '1/3/22-1/5/22' | D7: '1/4/22-1/6/22' | B8: '=INDEX(calendar,ndx+1) {array B8:H8}' -> 2022-01-03 00:00:00 | C8: 2022-01-04 00:00:00 | D8: 2022-01-05 00:00:00

### `fbb712543e38|FORMULA_DRIFT|Sheet1!E9`

- workbook: `all_data_912_v0.1/spreadsheet/38655/3_38655_input.xlsx`
- location: `Sheet1!E9`  severity: High  confidence: Likely defect
- formula: `=+DB($C$4,$C$5,$C$6,E8)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =+DB(R4C3,R5C3,R6C3,R[-1]C,1)
- evidence: This cell: =+DB(R4C3,R5C3,R6C3,R[-1]C)
- cached value: 0; row labels: []; column header: ''; used range: A1:Q12
- neighbourhood: C8: 1 | D8: 2 | E8: 3 | F8: 4 | C9: '=+DB($C$4,$C$5,$C$6,C8,1)' -> 460071.236361904 | D9: '=+DB($C$4,$C$5,$C$6,D8,1)' -> 5060783.59998094 | E9: '=+DB($C$4,$C$5,$C$6,E8)' -> 0

### `4ea284d68c01|FORMULA_DRIFT|Sheet1!N294`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!N294`  severity: High  confidence: Likely defect
- formula: `=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=18): =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90,RC[-7]>=300),RC[-7],""),"")
- evidence: This cell: =IF(R[-1]C[-5]>=12,IF(AND(R[-1]C[-4]<=90120,RC[-7]>=300),RC[-7],""),"")
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: L292: '=IFERROR(IF(I291>=12,IF($J291<=120,0+SUBSTITUTE(IF($D292>=150,","&... -> None | M292: '=IFERROR(IF(I291>=12,IF($J291<=140,0+SUBSTITUTE(IF($D292>=175,","&... -> None | N292: '=IF(I291>=12,IF(AND(J291<=90,G292>=300),G292,""),"")' -> None | O292: '=IF(I291>=12,IF(AND(J291<=120,G292>=400),G292,""),"")' -> None | P292: '=IF(I291>=12,IF(AND(J291<=145,G292>=500),G292,""),"")' -> None | L293: '=IFERROR(IF(I292>=12,IF($J292<=120,0+SUBSTITUTE(IF($D293>=150,","&... -> None | M293: '=IFERROR(IF(I292>=12,IF($J292<=140,0+SUBSTITUTE(IF($D293>=175,","&... -> None | N293: '=IF(I292>=12,IF(AND(J292<=90,G293>=300),G293,""),"")' -> None | O293: '=IF(I292>=12,IF(AND(J292<=120,G293>=400),G293,""),"")' -> None | P293: '=IF(I292>=12,IF(AND(J292<=145,G293>=500),G293,""),"")' -> None | L294: '=IFERROR(IF(I293>=12,IF($J293<=120,0+SUBSTITUTE(IF($D294>=150,","&... -> None | M294: '=IFERROR(IF(I293>=12,IF($J293<=140,0+SUBSTITUTE(IF($D294>=175,","&... -> None | N294: '=IF(I293>=12,IF(AND(J293<=90120,G294>=300),G294,""),"")' -> None | O294: '=IF(I293>=12,IF(AND(J293<=120,G294>=400),G294,""),"")' -> None | P294: '=IF(I293>=12,IF(AND(J293<=145,G294>=500),G294,""),"")' -> None | L295: '=IFERROR(IF(I294>=12,IF($J294<=120,0+SUBSTITUTE(IF($D295>=150,","&... -> None | M295: '=IFERROR(IF(I294>=12,IF($J294<=140,0+SUBSTITUTE(IF($D295>=175,","&... -> None | L296: '=IFERROR(IF(I295>=12,IF($J295<=120,0+SUBSTITUTE(IF($D296>=150,","&... -> None | M296: '=IFERROR(IF(I295>=12,IF($J295<=140,0+SUBSTITUTE(IF($D296>=175,","&... -> None | N296: '=IF(I295>=12,IF(AND(J295<=120,G296>=300),G296,""),"")' -> None

### `1ee00a60f590|FORMULA_DRIFT|Sheet1!BS2`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!BS2`  severity: High  confidence: Likely defect
- formula: `=IF(BR2="","",SMALL(IF(INDEX($R$2:$R$600,,MATCH(LEFT(BQ2,FIND("#",BQ2)-2),$R$1:$R$1,0))=BR2,ROW($R$2:$R$600)),COUNTIF(BR$2:BR2,BR2)))`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=31): =IF(RC[-1]="","",SMALL(IF(INDEX(R2C18:R526C18,,MATCH(LEFT(RC[-2],FIND("#",RC[-2])-2),R1C18:R1C18,0))=RC[-1],ROW(R2C18:R526C18)),COUNTIF(R2C[-1]:RC[-1],RC[-1])))
- evidence: This cell: =IF(RC[-1]="","",SMALL(IF(INDEX(R2C18:R600C18,,MATCH(LEFT(RC[-2],FIND("#",RC[-2])-2),R1C18:R1C18,0))=RC[-1],ROW(R2C18:R600C18)),COUNTIF(R2C[-1]:RC[-1],RC[-1])))
- cached value: 141; row labels: ["'175 Avg w/600 Series #1'", "'Game 45 Pins Over Avg #1'"]; column header: "'ID#'"; used range: A1:CJ782
- range $R$2:$R$600: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '177', 'None', 'None', 'None']; beyond: {'above': "R1: 'Game 45 Pins Over Avg'", 'below': 'R601: None'}
- neighbourhood: BQ1: 'Game 45 Pins Over Avg' | BR1: 'Score' | BS1: 'ID#' | BT1: 'Position of Name in List' | BU1: 'Full Name' | BQ2: 'Game 45 Pins Over Avg #1' | BR2: '=IFERROR(LARGE($R$2:$R$600,ROW(BR1)),(""))' -> 194 | BS2: '=IF(BR2="","",SMALL(IF(INDEX($R$2:$R$600,,MATCH(LEFT(BQ2,FIND("#",... -> 141 | BT2: '=IFERROR(CEILING(BS2/21,1)," ")' -> 7 | BU2: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BT2,$AG$2:$AG$33,))," ")' -> 'GG AG' | BQ3: 'Game 45 Pins Over Avg #2' | BR3: '=IFERROR(LARGE($R$2:$R$600,ROW(BR2)),(""))' -> 193 | BS3: '=IF(BR3="","",SMALL(IF(INDEX($R$2:$R$526,,MATCH(LEFT(BQ3,FIND("#",... -> 80 | BT3: '=IFERROR(CEILING(BS3/21,1)," ")' -> 4 | BU3: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BT3,$AG$2:$AG$33,))," ")' -> 'DD AD' | BQ4: 'Game 45 Pins Over Avg #3' | BR4: '=IFERROR(LARGE($R$2:$R$600,ROW(BR3)),(""))' -> 188 | BS4: '=IF(BR4="","",SMALL(IF(INDEX($R$2:$R$526,,MATCH(LEFT(BQ4,FIND("#",... -> 71 | BT4: '=IFERROR(CEILING(BS4/21,1)," ")' -> 4 | BU4: '=IFERROR(INDEX($AF$2:$AF$33,MATCH($BT4,$AG$2:$AG$33,))," ")' -> 'DD AD'

### `7c3edf13b7c6|FORMULA_DRIFT|Malaga!O11`

- workbook: `all_data_912_v0.1/spreadsheet/40809/2_40809_input.xlsx`
- location: `Malaga!O11`  severity: High  confidence: Likely defect
- formula: `=C8`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =R[-3]C[-11]
- evidence: This cell: =R[-3]C[-12]
- cached value: 'NAME'; row labels: ["'MUNTING (Tony)'", "'G'"]; column header: ''; used range: A1:AJ57
- neighbourhood: M9: '=IF(J9="","",IF(K9="G",$G$4-L9,IF(K9="N/G",$L$4-L9,IF(K9="S/S",$L$... -> 799 | O9: '=A7' -> 'Golf at La Cala America, L... | M10: '=IF(J10="","",IF(K10="G",$G$4-L10,IF(K10="N/G",$L$4-L10,IF(K10="S/... -> 799 | O10: '=H7' -> 'La Cala Europa & Santa Mon... | M11: '=IF(J11="","",IF(K11="G",$G$4-L11,IF(K11="N/G",$L$4-L11,IF(K11="S/... -> 799 | O11: '=C8' -> 'NAME' | P11: '=E8' -> 'PAID' | Q11: '=F8' -> 'BALANCE' | M12: '=IF(J12="","",IF(K12="G",$G$4-L12,IF(K12="N/G",$L$4-L12,IF(K12="S/... -> None | O12: '=IF(C9="","",C9)' -> 'CURT (Kellie)' | P12: '=IF(E9="","",E9)' -> 0 | Q12: '=IF(F9="","",F9)' -> 449 | M13: '=IF(J13="","",IF(K13="G",$G$4-L13,IF(K13="N/G",$L$4-L13,IF(K13="S/... -> 449 | O13: '=IF(C10="","",C10)' -> 'CURT (Sean)' | P13: '=IF(E10="","",E10)' -> 0 | Q13: '=IF(F10="","",F10)' -> 799

### `d01aaa205624|FORMULA_DRIFT|HouseBudget!F123`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/1_CF_22493_input.xlsx`
- location: `House Budget!F123`  severity: High  confidence: Likely defect
- formula: `=SUM(G65:G122)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=58): =SUM(RC[1]:RC[25])
- evidence: This cell: =SUM(R[-58]C[1]:R[-1]C[1])
- cached value: 0; row labels: []; column header: ''; used range: A1:AG123
- range G65:G122: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'G64: None', 'below': 'G123: None'}
- neighbourhood: D121: '=F59' -> 0 | E121: "='Money In Checking Next Month'!A58" -> 0 | F121: '=SUM(G121:AE121)' -> 0 | D122: '=F60' -> 0 | E122: "='Money In Checking Next Month'!A59" -> 370 | F122: '=SUM(G122:AE122)' -> 0 | E123: '=SUM(E65:E122)' -> 7237.48 | F123: '=SUM(G65:G122)' -> 0

### `53fb4bf35e11|FORMULA_DRIFT|Sheet1!BI93`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/3_CF_6540_input.xlsx`
- location: `Sheet1!BI93`  severity: High  confidence: Likely defect
- formula: `=SUM(BF93*1.5)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=14): =RC[-3]*1.5
- evidence: This cell: =SUM(RC[-3]*1.5)
- cached value: 34.5; row labels: ["'Banksman'"]; column header: ''; used range: A1:CL123
- neighbourhood: BG91: 21.25 | BH91: 22.25 | BI91: '=BF91*1.5' -> 31.875 | BJ91: '£16.00' | BK91: '£18.00' | BG92: 22.25 | BH92: 23.25 | BI92: '=BF92*1.5' -> 33.375 | BJ92: '£16.00' | BK92: '£18.00' | BG93: 23 | BH93: 24 | BI93: '=SUM(BF93*1.5)' -> 34.5 | BJ93: '£21.10' | BK93: '£23.10' | BG94: 20.25 | BH94: 21.75 | BI94: '=BF94*1.5' -> 30.375 | BJ94: '£16.00' | BK94: '£18.00' | BG95: 18.5 | BH95: 19.5 | BI95: '=BF95*1.5' -> 27.75 | BJ95: '£16.00' | BK95: '£18.00'

### `fe65a777a463|FORMULA_DRIFT|DATABASECountries!F4`

- workbook: `all_data_912_v0.1/spreadsheet/37462/3_37462_input.xlsx`
- location: `DATABASE Countries!F4`  severity: High  confidence: Likely defect
- formula: `=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36)`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=240): =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C2:R36C2)
- evidence: This cell: =SUMPRODUCT(ISNUMBER(SEARCH(RC[-1],R4C1:R36C1))*R4C3:R36C3)
- cached value: '#VALUE!'; row labels: ["'India'", "'Afghanistan'"]; column header: "'Revenue'"; used range: A1:J244
- range $A$4:$A$36: values ["'India'", "'United Kingdom'", "'Afghanistan'", "'Albania'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "A3: 'Country'", 'below': 'A37: None'}
- neighbourhood: E2: 'TOTAL' | F2: '=SUM(F4:F83)' -> '#VALUE!' | E3: 'Countries' | F3: 'Revenue' | D4: 1 | E4: 'Afghanistan' | F4: '=SUMPRODUCT(ISNUMBER(SEARCH(E4,$A$4:$A$36))*$C$4:$C$36) {array F4}' -> '#VALUE!' | H4: 'TOP 1' | D5: '=D4+1' -> 2 | E5: 'Albania' | F5: '=SUMPRODUCT(ISNUMBER(SEARCH(E5,$A$4:$A$36))*$B$4:$B$36) {array F5}' -> 88 | H5: 'TOP 2' | D6: '=D5+1' -> 3 | E6: 'Algeria' | F6: '=SUMPRODUCT(ISNUMBER(SEARCH(E6,$A$4:$A$36))*$B$4:$B$36) {array F6}' -> 0 | H6: 'TOP 3'

### `bc56a9f2824a|FORMULA_DRIFT|Total(2)!O13`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!O13`  severity: High  confidence: Likely defect
- formula: `=SUMIFS($C$1:$C$37,$F$1:$F$37,">"&O16,$F$1:$F$37,"<"&P10)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=4): =SUMIFS(R1C3:R37C3,R1C6:R37C6,">"&R[3]C,R1C6:R37C6,"<"&R[3]C[1])
- evidence: This cell: =SUMIFS(R1C3:R37C3,R1C6:R37C6,">"&R[3]C,R1C6:R37C6,"<"&R[-3]C[1])
- cached value: 0; row labels: ["'PE'", "'Rentals'"]; column header: ''; used range: A1:Z1026
- range $C$1:$C$37: values ['None', 'None', 'None', 'None', 'None', 'None', "'Commission'", '1950', '2000', '2500', '2150', '1800']; beyond: {'below': "C38: '=SUM(C8:C37)'"}
- neighbourhood: M12: '=SUMIFS($C$41:$C$58,$F$41:$F$58,">"&M16,$F$41:$F$58,"<"&N16)' -> 0 | N12: '=SUMIFS($C$41:$C$58,$F$41:$F$58,">"&N16,$F$41:$F$58,"<"&O16)' -> 0 | O12: '=SUMIFS($C$41:$C$58,$F$41:$F$58,">"&O16,$F$41:$F$58,"<"&P10)' -> 0 | M13: '=SUMIFS($C$1:$C$37,$F$1:$F$37,">"&M16,$F$1:$F$37,"<"&N16)' -> 0 | N13: '=SUMIFS($C$1:$C$37,$F$1:$F$37,">"&N16,$F$1:$F$37,"<"&O16)' -> 0 | O13: '=SUMIFS($C$1:$C$37,$F$1:$F$37,">"&O16,$F$1:$F$37,"<"&P10)' -> 0 | M14: '=SUMIFS($C$62:$C$74,$F$62:$F$74,">"&M16,$F$62:$F$74,"<"&N16)' -> 0 | N14: '=SUMIFS($C$62:$C$74,$F$62:$F$74,">"&N16,$F$62:$F$74,"<"&O16)' -> 0 | O14: '=SUMIFS($C$62:$C$74,$F$62:$F$74,">"&O16,$F$62:$F$74,"<"&P16)' -> 0 | M15: '=SUMIFS(D8:D77,F8:F77,">"&M16,F8:F77,"<"&N16)' -> 0 | N15: '=SUMIFS(D8:D77,F8:F77,">"&N16,F8:F77,"<"&O16)' -> 0 | O15: '=SUMIFS(D8:D77,F8:F77,">"&O16,F8:F77,"<"&P10)' -> 0

## HARDCODE_IN_FORMULA_BLOCK

### `643562b8c3e5|HARDCODE_IN_FORMULA_BLOCK|Sheet1!H9`

- workbook: `all_data_912_v0.1/spreadsheet/33094/1_33094_input.xlsx`
- location: `Sheet1!H9`  severity: High  confidence: Likely defect
- evidence: Value 6 sits between Sheet1!H8 and Sheet1!H10, which share the pattern =R[-1]C/R7C2.
- cached value: 6; row labels: ["'Employee3'"]; column header: ''; used range: A1:Z10
- neighbourhood: F7: 25 | G7: 25 | H7: 25 | I7: 17 | J7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!O$4:O$1000)' -> 0 | F8: '=F7/$B$7' -> 0.625 | G8: '=G7/$B$7' -> 0.625 | H8: '=H7/$B$7' -> 0.625 | I8: '=I7/$B$7' -> 0.425 | J8: '=J7/$B$7' -> 0 | F9: 8 | G9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)' -> 0 | H9: 6 | I9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!N$4:N$1000)' -> 0 | J9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!O$4:O$1000)' -> 0 | F10: '=F9/$B$7' -> 0.2 | G10: '=G9/$B$7' -> 0 | H10: '=H9/$B$7' -> 0.15 | I10: '=I9/$B$7' -> 0 | J10: '=J9/$B$7' -> 0

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!Q6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!Q6`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!O6 and Sheet1!R6, which share the pattern =RC[-2]-RC[-1].
- cached value: 1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0 | O7: '=M7-N7' -> -1 | P7: 2 | Q7: 3 | R7: '=P7-Q7' -> -1 | O8: '=M8-N8' -> -2 | P8: 0 | Q8: 2 | R8: '=P8-Q8' -> -2

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!J6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!J6`  severity: High  confidence: Likely defect
- evidence: Value 5 sits between Sheet1!I6 and Sheet1!L6, which share the pattern =RC[-2]-RC[-1].
- cached value: 5; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: H4: 2 | I4: '=G4-H4' -> 0 | J4: 3 | K4: 5 | L4: '=J4-K4' -> -2 | H5: 2 | I5: -1 | J5: 1 | K5: 7 | L5: -1 | H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4 | H7: 3 | I7: '=G7-H7' -> -1 | J7: 2 | K7: 3 | L7: '=J7-K7' -> -1 | H8: 2 | I8: '=G8-H8' -> -2 | J8: 0 | K8: 2 | L8: '=J8-K8' -> -2

### `e5094a660f5e|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D83`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/2_395-48_input.xlsx`
- location: `Sheet1!D83`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D82 and Sheet1!D84, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'RIVERA SANTOS'", "'OROZCO IRVING'"]; column header: ''; used range: A1:D302
- neighbourhood: B81: 'ALVARADO F T' | C81: 'ALVARADO F T' | D81: '=IF(AND(A81=1,B81=C81),1,"")' -> None | B82: 'TERRERO PEDRO M' | C82: 'AYUSO ARMANDO' | D82: '=IF(AND(A82=1,B82=C82),1,"")' -> None | B83: 'RIVERA SANTOS' | C83: 'OROZCO IRVING' | D83: 1 | B84: 'AYUSO ARMANDO' | C84: 'PEREIRA TIAGO' | D84: '=IF(AND(A84=1,B84=C84),1,"")' -> None | B85: 'ESPINOZA ASSAEL' | C85: 'MONROY FRANCISCO' | D85: '=IF(AND(A85=1,B85=C85),1,"")' -> None

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!M6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!M6`  severity: High  confidence: Likely defect
- evidence: Value 5 sits between Sheet1!L6 and Sheet1!O6, which share the pattern =RC[-2]-RC[-1].
- cached value: 5; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | O4: '=M4-N4' -> 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | O5: -1 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | O6: '=M6-N6' -> 5 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3 | O7: '=M7-N7' -> -1 | K8: 2 | L8: '=J8-K8' -> -2 | M8: 0 | N8: 2 | O8: '=M8-N8' -> -2

### `a4ee03c3468a|HARDCODE_IN_FORMULA_BLOCK|HR!GC8`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !GC8`  severity: High  confidence: Likely defect
- evidence: Value 10.11 sits between HR !GC7 and HR !GC9, which share the pattern =#REF!.
- cached value: 10.11; row labels: ["'N/A'", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: GA6: 496.287 | GB6: 556.1888409 | GA7: 165.5478 | GB7: 185.52941946 | GC7: '=#REF!' -> '#REF!' | GD7: '=IF(GB7>99.99,"Yes","No")' -> 'Yes' | GE7: '=IF(ISNUMBER(SEARCH("Yes",GD7)),GB7,"")' -> 185.52941946 | GA8: 240.9 | GB8: 269.97663 | GC8: 10.11 | GD8: '=IF(GB8>99.99,"Yes","No")' -> 'Yes' | GE8: 'Month 1' | GA9: 130.7988 | GB9: 146.58621516 | GC9: '=#REF!' -> '#REF!' | GD9: '=IF(GB9>99.99,"Yes","No")' -> 'Yes' | GE9: '=IF(ISNUMBER(SEARCH("Yes",GD9)),GB9,"")' -> 146.58621516 | GA10: 376.7148 | GB10: 422.18427636 | GC10: '=#REF!' -> '#REF!' | GD10: '=IF(GB10>99.99,"Yes","No")' -> 'Yes' | GE10: '=IF(ISNUMBER(SEARCH("Yes",GD10)),GB10,"")' -> 422.18427636

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!L5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!L5`  severity: High  confidence: Likely defect
- evidence: Value -1 sits between Sheet1!L4 and Sheet1!L6, which share the pattern =RC[-2]-RC[-1].
- cached value: -1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: J3: 2 | K3: 2 | L3: '=J3-K3' -> 0 | M3: 2 | N3: 2 | J4: 3 | K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | J5: 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | J7: 2 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!P4`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!O4 and Sheet1!R4, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: N2: 'MBQ' | O2: 'Diff' | P2: 'Actual' | Q2: 'MBQ' | R2: 'Diff' | N3: 2 | O3: '=M3-N3' -> 0 | P3: 2 | Q3: 2 | R3: '=P3-Q3' -> 0 | N4: 2 | O4: '=M4-N4' -> 1 | P4: 2 | Q4: 2 | R4: '=P4-Q4' -> 0 | N5: 6 | O5: -1 | P5: 1 | Q5: 2 | R5: -1 | N6: 0 | O6: '=M6-N6' -> 5 | P6: 1 | Q6: 1 | R6: '=P6-Q6' -> 0

### `3a2b74c70f66|HARDCODE_IN_FORMULA_BLOCK|Total(2)!E30`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!E30`  severity: High  confidence: Likely defect
- evidence: Value 925 sits between Total (2)!E27 and Total (2)!E31, which share the pattern =SUM(RC[-3]*0.5).
- cached value: 925; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | F28: 44576 | G28: 'N' | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C' | C32: '=(B32*12)/12' -> 3000 | D32: '=SUM(C32-E32)' -> 1050 | E32: '=IFERROR(VLOOKUP($H32,$J$27:$L$35,3,0)*$C32,0)' -> 1950 | F32: 44589 | G32: 'C'

### `e5094a660f5e|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D72`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/2_395-48_input.xlsx`
- location: `Sheet1!D72`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D71 and Sheet1!D74, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'ESPINOZA ASSAEL'", "'ANTONGEORGI WILLIAM JR'"]; column header: ''; used range: A1:D302
- neighbourhood: B70: 'AYUSO ARMANDO' | C70: 'AYUSO ARMANDO' | D70: '=IF(AND(A70=1,B70=C70),1,"")' -> None | B71: 'AMADOR SILVIO RUIZ' | C71: 'OROZCO KEVIN E' | D71: '=IF(AND(A71=1,B71=C71),1,"")' -> None | B72: 'ESPINOZA ASSAEL' | C72: 'ANTONGEORGI WILLIAM JR' | D72: 1 | B73: 'PENA BRYAN' | C73: 'GONZALEZ RICARDO' | D73: 1 | B74: 'ANTONGEORGI WILLIAM JR' | C74: 'ANTONGEORGI WILLIAM JR' | D74: '=IF(AND(A74=1,B74=C74),1,"")' -> None

### `2ed80e0ee4cd|HARDCODE_IN_FORMULA_BLOCK|DRP!N20`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!N20`  severity: High  confidence: Likely defect
- evidence: Value 12 sits between DRP!L20 and DRP!O20, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 12; row labels: ["'RRM1'", "'CV1'"]; column header: ''; used range: A1:O23
- neighbourhood: L18: '=I18+J18-K18' -> None | O18: '=L18+M18-N18' -> None | L19: '=I19+J19-K19' -> None | M19: 10 | O19: '=L19+M19-N19' -> None | L20: '=I20+J20-K20' -> None | N20: 12 | O20: '=L20+M20-N20' -> None | L21: '=I21+J21-K21' -> None | O21: '=L21+M21-N21' -> None | L22: '=I22+J22-K22' -> None | O22: '=L22+M22-N22' -> None

### `a4ee03c3468a|HARDCODE_IN_FORMULA_BLOCK|HR!BC5`

- workbook: `all_data_912_v0.1/spreadsheet/54590/3_54590_input.xlsx`
- location: `HR !BC5`  severity: High  confidence: Likely defect
- evidence: Value 46.09674447 sits between HR !BC4 and HR !BC7, which share the pattern =IF(ISNUMBER(SEARCH("Yes",RC[-1])),RC[-3],"").
- cached value: 46.09674447; row labels: ["'Month 2'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: BA3: '=AQ3' -> '#REF!' | BB3: '=IF(AZ3>99.99,"Yes","No")' -> '#REF!' | BC3: '=IF(ISNUMBER(SEARCH("Yes",BB3)),AZ3,"")' -> None | BD3: 'Month 2' | BA4: '=AQ4' -> '#REF!' | BB4: '=IF(AZ4>99.99,"Yes","No")' -> '#REF!' | BC4: '=IF(ISNUMBER(SEARCH("Yes",BB4)),AZ4,"")' -> None | BD4: 'N/A' | BA5: '=AQ5' -> '#REF!' | BB5: 'Yes' | BC5: 46.09674447 | BD5: 'Aug - Oct' | BE5: '=AB5+AM5+AX5' -> '#REF!' | BA7: '=AQ7' -> '#REF!' | BB7: '=IF(AZ7>99.99,"Yes","No")' -> '#REF!' | BC7: '=IF(ISNUMBER(SEARCH("Yes",BB7)),AZ7,"")' -> None | BD7: 'N/A'

### `f5521bffa45f|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D93`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D93`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D92 and Sheet1!D94, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'PENA BRYAN'", "'HERRERA CRISTOBAL'"]; column header: ''; used range: A1:D302
- neighbourhood: B91: 'RIVERA SANTOS' | C91: 'PAYERAS EDGAR' | D91: '=IF(AND(A91=1,B91=C91),1,"")' -> None | B92: 'LOPEZ DAVID CARLOS' | C92: 'ANTONGEORGI WILLIAM JR' | D92: '=IF(AND(A92=1,B92=C92),1,"")' -> None | B93: 'PENA BRYAN' | C93: 'HERRERA CRISTOBAL' | D93: 1 | D94: '=IF(AND(A94=1,B94=C94),1,"")' -> None | D95: '=IF(AND(A95=1,B95=C95),1,"")' -> None

### `f5521bffa45f|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D48`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D48`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D47 and Sheet1!D49, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'MARTINEZ CATALINO'", "'BRAVO J'"]; column header: ''; used range: A1:D302
- neighbourhood: B46: 'TERRERO PEDRO M' | C46: 'TERRERO PEDRO M' | D46: '=IF(AND(A46=1,B46=C46),1,"")' -> None | B47: 'PENA BRYAN' | C47: 'PENA BRYAN' | D47: '=IF(AND(A47=1,B47=C47),1,"")' -> None | B48: 'MARTINEZ CATALINO' | C48: 'BRAVO J' | D48: 1 | B49: 'MONROY FRANCISCO' | C49: 'FREY KYLE' | D49: '=IF(AND(A49=1,B49=C49),1,"")' -> None | B50: 'MONROY FRANCISCO' | C50: 'MONROY FRANCISCO' | D50: '=IF(AND(A50=1,B50=C50),1,"")' -> None

### `a94eb6a7585f|HARDCODE_IN_FORMULA_BLOCK|HR!BC5`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !BC5`  severity: High  confidence: Likely defect
- evidence: Value 46.09674447 sits between HR !BC4 and HR !BC7, which share the pattern =IF(ISNUMBER(SEARCH("Yes",RC[-1])),RC[-3],"").
- cached value: 46.09674447; row labels: ["'Month 2'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: BA3: '=AQ3' -> '#REF!' | BB3: '=IF(AZ3>99.99,"Yes","No")' -> '#REF!' | BC3: '=IF(ISNUMBER(SEARCH("Yes",BB3)),AZ3,"")' -> None | BD3: 'Month 2' | BA4: '=AQ4' -> '#REF!' | BB4: '=IF(AZ4>99.99,"Yes","No")' -> '#REF!' | BC4: '=IF(ISNUMBER(SEARCH("Yes",BB4)),AZ4,"")' -> None | BD4: 'N/A' | BA5: '=AQ5' -> '#REF!' | BB5: 'Yes' | BC5: 46.09674447 | BD5: 'Aug - Oct' | BE5: '=AB5+AM5+AX5' -> '#REF!' | BA7: '=AQ7' -> '#REF!' | BB7: '=IF(AZ7>99.99,"Yes","No")' -> '#REF!' | BC7: '=IF(ISNUMBER(SEARCH("Yes",BB7)),AZ7,"")' -> None | BD7: 'N/A'

### `bc56a9f2824a|HARDCODE_IN_FORMULA_BLOCK|Total(2)!C27`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!C27`  severity: High  confidence: Likely defect
- evidence: Value 2300 sits between Total (2)!C25 and Total (2)!C28, which share the pattern =(RC[-1]*12)/12.
- cached value: 2300; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: A25: 18 | B25: 2800 | C25: '=(B25*12)/12' -> 2800 | D25: '=SUM(C25-E25)' -> 1120 | E25: 1680 | A26: 19 | B26: 2400 | C26: 2300 | D26: '=SUM(C26-E26)' -> 1100 | E26: '=SUM(B26*0.5)' -> 1200 | A27: 20 | B27: 2400 | C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | A28: 21 | B28: 2055 | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | A29: 22 | B29: 2300 | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840

### `30c6f4937476|HARDCODE_IN_FORMULA_BLOCK|HR!BC11`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !BC11`  severity: High  confidence: Likely defect
- evidence: Value 141.97061221 sits between HR !BC10 and HR !BC12, which share the pattern =IF(ISNUMBER(SEARCH("Yes",RC[-1])),RC[-3],"").
- cached value: 141.97061221; row labels: ["'Month 2'", "'Yes'"]; column header: ''; used range: A1:GT37
- neighbourhood: BA10: '=AQ10' -> '#REF!' | BB10: '=IF(AZ10>99.99,"Yes","No")' -> '#REF!' | BC10: '=IF(ISNUMBER(SEARCH("Yes",BB10)),AZ10,"")' -> None | BD10: 'N/A' | BA11: '=AQ11' -> '#REF!' | BB11: 'Yes' | BC11: 141.97061221 | BD11: 'Aug - Oct' | BE11: '=AB11+AM11+AX11' -> '#REF!' | BA12: '=AQ12' -> '#REF!' | BB12: '=IF(AZ12>99.99,"Yes","No")' -> '#REF!' | BC12: '=IF(ISNUMBER(SEARCH("Yes",BB12)),AZ12,"")' -> None | BD12: 'N/A'

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!M4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!M4`  severity: High  confidence: Likely defect
- evidence: Value 3 sits between Sheet1!L4 and Sheet1!O4, which share the pattern =RC[-2]-RC[-1].
- cached value: 3; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: K2: 'MBQ' | L2: 'Diff' | M2: 'Actual' | N2: 'MBQ' | O2: 'Diff' | K3: 2 | L3: '=J3-K3' -> 0 | M3: 2 | N3: 2 | O3: '=M3-N3' -> 0 | K4: 5 | L4: '=J4-K4' -> -2 | M4: 3 | N4: 2 | O4: '=M4-N4' -> 1 | K5: 7 | L5: -1 | M5: 1 | N5: 6 | O5: -1 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | O6: '=M6-N6' -> 5

### `6116800fac3b|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D4`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/1_395-48_input.xlsx`
- location: `Sheet1!D4`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D3 and Sheet1!D5, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'PENA BRYAN'", "'ALVARADO F T'"]; column header: ''; used range: A1:D302
- neighbourhood: B3: 'OROZCO IRVING' | C3: 'ROMAN EVIN A' | D3: '=IF(AND(A3=1,B3=C3),1,"")' -> None | B4: 'PENA BRYAN' | C4: 'ALVARADO F T' | D4: 1 | B5: 'AMADOR SILVIO RUIZ' | C5: 'AYUSO ARMANDO' | D5: '=IF(AND(A5=1,B5=C5),1,"")' -> None | B6: 'ESPINOZA ASSAEL' | C6: 'ROMAN EVIN A' | D6: '=IF(AND(A6=1,B6=C6),1,"")' -> None

### `bc56a9f2824a|HARDCODE_IN_FORMULA_BLOCK|Total(2)!E29`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!E29`  severity: High  confidence: Likely defect
- evidence: Value 1840 sits between Total (2)!E27 and Total (2)!E31, which share the pattern =SUM(RC[-3]*0.5).
- cached value: 1840; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: C27: 2300 | D27: '=SUM(C27-E27)' -> 1100 | E27: '=SUM(B27*0.5)' -> 1200 | F27: 44589 | G27: 'C' | C28: '=(B28*12)/12' -> 2055 | D28: '=SUM(C28-E28)' -> 411 | E28: 1644 | F28: 44576 | G28: 'N' | C29: '=(B29*12)/12' -> 2300 | D29: '=SUM(C29-E29)' -> 460 | E29: 1840 | F29: 44576 | G29: 'N' | C30: '=(B30*12)/12' -> 1500 | D30: '=SUM(C30-E30)' -> 575 | E30: 925 | F30: 44571 | G30: 'Y' | C31: '=(B31*12)/12' -> 1800 | D31: '=SUM(C31-E31)' -> 900 | E31: '=SUM(B31*0.5)' -> 900 | F31: 44585 | G31: 'C'

### `8b7bb50b3697|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C31`

- workbook: `all_data_912_v0.1/spreadsheet/35207/2_35207_input.xlsx`
- location: `Sheet1!C31`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/30/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899 | A33: '2/1/1890' | B33: 0.0001807 | C33: 0

### `8b7bb50b3697|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C30`

- workbook: `all_data_912_v0.1/spreadsheet/35207/2_35207_input.xlsx`
- location: `Sheet1!C30`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/29/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A28: '1/27/1890' | B28: 0.0141 | A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899

### `70f5a8fe58e1|HARDCODE_IN_FORMULA_BLOCK|Sheet1!C31`

- workbook: `all_data_912_v0.1/spreadsheet/35207/1_35207_input.xlsx`
- location: `Sheet1!C31`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!C29 and Sheet1!C32, which share the pattern =SUM(RC[-1]:R[2]C[-1]).
- cached value: 0; row labels: ["'1/30/1890'"]; column header: ''; used range: A1:C650
- neighbourhood: A29: '1/28/1890' | B29: 0.03142 | C29: '=SUM(B29:B31)' -> 0.0356753 | A30: '1/29/1890' | B30: 0.003586 | C30: 0 | A31: '1/30/1890' | B31: 0.0006693 | C31: 0 | A32: '1/31/1890' | B32: 0.0002845 | C32: '=SUM(B32:B34)' -> 0.0005899 | A33: '2/1/1890' | B33: 0.0001807 | C33: 0

### `3bdd8dbbaf67|HARDCODE_IN_FORMULA_BLOCK|Dati!AB27`

- workbook: `all_data_912_v0.1/spreadsheet/55912/3_55912_input.xlsx`
- location: `Dati!AB27`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Dati!AB24 and Dati!AB28, which share the pattern =IF(OR(RC18="-",RC18="\"),RC19+RC20," ").
- cached value: 1; row labels: ["'MULTIGOL 3-6'", "'\\\\'"]; column header: ''; used range: A1:CJ40
- neighbourhood: AB25: 1 | AC25: '=IF(OR($R25="-",$R25="\\"),IF($AB25>0,"YES","NO")," ")' -> 'YES' | AA26: '=IF(OR($R26="-",$R26="\\"),$U26+$V26," ")' -> 1 | AB26: 1 | AC26: '=IF(OR($R26="-",$R26="\\"),IF($AB26>0,"YES","NO")," ")' -> 'YES' | AA27: '=IF(OR($R27="-",$R27="\\"),$U27+$V27," ")' -> 1 | AB27: 1 | AC27: '=IF(OR($R27="-",$R27="\\"),IF($AB27>0,"YES","NO")," ")' -> 'YES' | AA28: '=IF(OR($R28="-",$R28="\\"),$U28+$V28," ")' -> 3 | AB28: '=IF(OR($R28="-",$R28="\\"),$S28+$T28," ")' -> 2 | AC28: '=IF(OR($R28="-",$R28="\\"),IF($AB28>0,"YES","NO")," ")' -> 'YES' | AB29: '=IF(OR($R29="-",$R29="\\"),$S29+$T29," ")' -> 0 | AC29: '=IF(OR($R29="-",$R29="\\"),IF($AB29>0,"YES","NO")," ")' -> 'NO'

### `7b15ef0c0d8c|HARDCODE_IN_FORMULA_BLOCK|data!K25`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!K25`  severity: High  confidence: Likely defect
- evidence: Value 1.5 sits between data!K24 and data!K28, which share the pattern =SUM(RC[-2]-RC[-3]).
- cached value: 1.5; row labels: ["'TREvor bock'", "'unit has a miss'"]; column header: ''; used range: A1:O48
- neighbourhood: I23: '=HOUR(F23)+MINUTE(F23)/60+SECOND(F23)/3600' -> 16.5180555555556 | K23: '=SUM(I23-H23)' -> 1.51222222222222 | I24: '=HOUR(F24)+MINUTE(F24)/60+SECOND(F24)/3600' -> 9.875 | K24: '=SUM(I24-H24)' -> 1.48638888888889 | K25: 1.5

## HIDDEN_STRUCTURE_IN_TOTAL

### `09478d797a42|HIDDEN_STRUCTURE_IN_TOTAL|MonthlyExpensesSummary!E6`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Monthly Expenses Summary!E6`  severity: Medium  confidence: Review
- formula: `=IFERROR(SUMPRODUCT(('Journal Entries'!$C$6:$C$3000='Monthly Expenses Summary'!$B6)*('Journal Entries'!$B$6:$B$3000<>"")*(MONTH('Journal Entries'!$B$6:$B$3000)=MONTH(E$4&0))*(YEAR('Journal Entries'!$B$6:$B$3000)='Monthly Expenses Summary'!$R$2)*('Journal Entries'!$F$6:$F$3000)),"")`
- evidence: Hidden row 2 on Monthly Expenses Summary feeds 480 visible formula(s): Monthly Expenses Summary!E6, Monthly Expenses Summary!F6, Monthly Expenses Summary!G6, Monthly Expenses Summary!H6, Monthly Expenses Summary!I6, Monthly Expenses Summary!J6, Monthly Expenses Summary!K6, Monthly Expenses Summary!L6, and 472 more.
- cached value: 0; row labels: ["'Building Rent'"]; column header: "'January'"; used range: A1:R65
- range 'Journal Entries'!$C$6:$C$3000: values ["'WG/CR/027'", "'WG/CR/001'", "'WG/CR/006'", "'WG/CR/006'", "'WG/CR/008'", "'WG/CR/006'", "'WG/CR/007'", "'WG/CR/003'", "'WG/CR/001'", "'WG/CR/027'", "'WG/CR/028'", "'WG/CR/029'"]; beyond: {'above': "C5: 'Item Code'", 'below': 'C3001: None'}
- neighbourhood: C4: 'Final Acc. Entry' | D4: 'Account Title' | E4: 'January' | F4: 'February' | G4: 'March' | D5: 'Expenses' | C6: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D6: 'Building Rent' | E6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 35000 | C7: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D7: 'Electricity' | E7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | C8: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D8: 'Fuel' | E8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 2000

### `fd82a768c064|HIDDEN_STRUCTURE_IN_TOTAL|Employee1!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/3_382-29_input.xlsx`
- location: `Employee 1!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden rows 23 to 24 on Employee 1 feed 22 visible formula(s): Employee 1!U3, Employee 1!V3, Employee 1!AB8, Employee 1!AB9, Employee 1!AB10, Employee 1!AB11, Employee 1!AB12, Employee 1!AB13, and 14 more.
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `9b7879bd3308|HIDDEN_STRUCTURE_IN_TOTAL|Here!I2`

- workbook: `all_data_912_v0.1/spreadsheet/58147/1_58147_input.xlsx`
- location: `Here!I2`  severity: Medium  confidence: Review
- formula: `=1&" - "&F2`
- evidence: Hidden column F on Here feeds 2 visible formula(s): Here!I2, Here!I6.
- cached value: '1 - Tbnor, Cadigan - TA32785655'; row labels: []; column header: "'Extract'"; used range: A1:J140
- neighbourhood: G1: 'Letter' | H1: 'First Name' | I1: 'Extract' | J1: 'Outcome' | G2: '=LEFT(F2,1)' -> 'T' | H2: '=1&" - "&C2' -> '1 - Tbnor' | I2: '=1&" - "&F2' -> '1 - Tbnor, Cadigan - TA327... | J2: 'Tbnor, Cadigan' | G3: '=LEFT(F3,1)' -> 'A' | H3: '=C4' -> 'Tbra' | I3: 'Tbra, Cadle - AA21259159' | J3: 'Tbra, Cadle' | G4: '=LEFT(F4,1)' -> 'T' | H4: '=C7' -> 'Tbrahame' | I4: 'Tbrahame, Cadogan - LB71531251' | J4: 'Tbrahame, Cadogan'

### `fa8217b2c986|HIDDEN_STRUCTURE_IN_TOTAL|Here!A2`

- workbook: `all_data_912_v0.1/spreadsheet/58114/1_58114_input.xlsx`
- location: `Here!A2`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!A2="","",Sheet1!A2)`
- evidence: Hidden sheet 'Sheet1' feeds 834 visible formula(s): Here!A2, Here!B2, Here!C2, Here!D2, Here!E2, Here!F2, Here!A3, Here!B3, and 826 more.
- cached value: 1; row labels: []; column header: "'#'"; used range: A1:J140
- neighbourhood: A1: '#' | B1: 'ID' | C1: 'First Name' | A2: '=IF(Sheet1!A2="","",Sheet1!A2)' -> 1 | B2: '=IF(Sheet1!B2="","",Sheet1!B2)' -> 'TA32785655' | C2: '=IF(Sheet1!C2="","",Sheet1!C2)' -> 'Tbnor' | A3: '=IF(Sheet1!A3="","",Sheet1!A3)' -> 2 | B3: '=IF(Sheet1!B3="","",Sheet1!B3)' -> 'SA12442673' | C3: '=IF(Sheet1!C3="","",Sheet1!C3)' -> 'Abo' | A4: '=IF(Sheet1!A4="","",Sheet1!A4)' -> 3 | B4: '=IF(Sheet1!B4="","",Sheet1!B4)' -> 'AA21259159' | C4: '=IF(Sheet1!C4="","",Sheet1!C4)' -> 'Tbra'

### `69355e1eb76d|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22 to 498 on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, and 14 more.
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `a556b2a52595|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden columns N, AW, AY on Sheet1 feed 42 visible formula(s): Sheet1!D4, Sheet1!C5, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, and 34 more.
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `ea1e0839ce78|HIDDEN_STRUCTURE_IN_TOTAL|Here!A2`

- workbook: `all_data_912_v0.1/spreadsheet/58114/2_58114_input.xlsx`
- location: `Here!A2`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!A2="","",Sheet1!A2)`
- evidence: Hidden sheet 'Sheet1' feeds 834 visible formula(s): Here!A2, Here!B2, Here!C2, Here!D2, Here!E2, Here!F2, Here!A3, Here!B3, and 826 more.
- cached value: 1; row labels: []; column header: "'#'"; used range: A1:J140
- neighbourhood: A1: '#' | B1: 'ID' | C1: 'First Name' | A2: '=IF(Sheet1!A2="","",Sheet1!A2)' -> 1 | B2: '=IF(Sheet1!B2="","",Sheet1!B2)' -> 'TA32785655' | C2: '=IF(Sheet1!C2="","",Sheet1!C2)' -> 'Tbnor' | A3: '=IF(Sheet1!A3="","",Sheet1!A3)' -> 2 | B3: '=IF(Sheet1!B3="","",Sheet1!B3)' -> 'SA12442673' | C3: '=IF(Sheet1!C3="","",Sheet1!C3)' -> 'Abo' | A4: '=IF(Sheet1!A4="","",Sheet1!A4)' -> 3 | B4: '=IF(Sheet1!B4="","",Sheet1!B4)' -> 'AA21259159' | C4: '=IF(Sheet1!C4="","",Sheet1!C4)' -> 'Tbra'

### `158be0e0e878|HIDDEN_STRUCTURE_IN_TOTAL|Employee1!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/1_382-29_input.xlsx`
- location: `Employee 1!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden rows 23 to 24 on Employee 1 feed 25 visible formula(s): Employee 1!U3, Employee 1!V3, Employee 1!AB5, Employee 1!AB6, Employee 1!AB7, Employee 1!AB8, Employee 1!AB9, Employee 1!AB10, and 17 more.
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `3ee4d6f069b6|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22 to 498 on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, and 14 more.
- cached value: 28599; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 28599 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `470be426ac84|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25`

- workbook: `all_data_912_v0.1/spreadsheet/57989/2_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden rows 12, 17 on Sheet1 feed 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, and 125 more.
- cached value: 0; row labels: ["'Driver 19'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 19' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 2' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 1 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 3' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 1 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `d207fd1fc90f|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/54638/2_54638_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- formula: `=IF(Sheet2!A2="","",Sheet2!A2)`
- evidence: Hidden sheet 'Sheet2' feeds 149 visible formula(s): Sheet1!A2, Sheet1!A3, Sheet1!A4, Sheet1!A5, Sheet1!A6, Sheet1!A7, Sheet1!A8, Sheet1!A9, and 141 more.
- cached value: 'Paid Time Off'; row labels: []; column header: "'Time off '"; used range: A1:B150
- neighbourhood: A1: 'Time off ' | B1: 'Time off ' | A2: '=IF(Sheet2!A2="","",Sheet2!A2)' -> 'Paid Time Off' | B2: 'Paid Time Off' | A3: '=IF(Sheet2!A3="","",Sheet2!A3)' -> 'Paid Time Off' | B3: 'FMLA' | A4: '=IF(Sheet2!A4="","",Sheet2!A4)' -> 'Paid Time Off' | B4: 'Bereavement Leave'

### `fd82a768c064|HIDDEN_STRUCTURE_IN_TOTAL|Employee2!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/3_382-29_input.xlsx`
- location: `Employee 2!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden rows 23 to 24 on Employee 2 feed 25 visible formula(s): Employee 2!U3, Employee 2!V3, Employee 2!AB5, Employee 2!AB6, Employee 2!AB7, Employee 2!AB8, Employee 2!AB9, Employee 2!AB10, and 17 more.
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `ac9c457a4aed|HIDDEN_STRUCTURE_IN_TOTAL|Compiledandlocatedschoolsda!B2`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!B2`  severity: Medium  confidence: Review
- formula: `=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$1461,0))`
- evidence: Hidden rows 2 to 127, 129 to 1461 on URN lookup feed 12 visible formula(s): Compiled and located schools da!B2, Compiled and located schools da!B3, Compiled and located schools da!B4, Compiled and located schools da!B5, Compiled and located schools da!B6, Compiled and located schools da!B7, Compiled and located schools da!B8, Compiled and located schools da!B9, and 4 more.
- cached value: '#N/A'; row labels: []; column header: "'DFES check'"; used range: A1:AJ1419
- range 'URN lookup'!$D$2:$D$1461: values ['2001', '2004', '2005', '2008', '2010', '2014', '2019', '2020', '2027', '2028', '2032', '2033']; beyond: {'above': "D1: 'ESTAB'", 'below': 'D1462: None'}
- neighbourhood: A1: 'URN' | B1: 'DFES check' | C1: 'DfE Number' | D1: 'County' | B2: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$146... -> '#N/A' | D2: 'Cumbria' | B3: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L3,'URN lookup'!$K$2:$K$146... -> '#N/A' | D3: 'Cumbria' | B4: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L4,'URN lookup'!$K$2:$K$146... -> '#N/A' | D4: 'Cumbria'

### `60062672a233|HIDDEN_STRUCTURE_IN_TOTAL|Admin&Settings!U5`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/2_118-8_input.xlsx`
- location: `Admin & Settings!U5`  severity: Medium  confidence: Review
- formula: `=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*7)+T5-WEEKDAY(DATE(Schedule!$B$6,Q5,1))+IF(T5<WEEKDAY(DATE(Schedule!$B$6,Q5,1)),7,0))`
- evidence: Hidden column B on Schedule feeds 70 visible formula(s): Admin & Settings!U5, Admin & Settings!U6, Admin & Settings!U7, Admin & Settings!U8, Admin & Settings!U9, Admin & Settings!U10, Admin & Settings!U11, Admin & Settings!U12, and 62 more.
- cached value: 2023-01-16 00:00:00; row labels: ["'Duration'", "'ML King Day'"]; column header: "'Date'"; used range: A1:X80
- neighbourhood: S4: 'Week' | T4: 'Weekday' | U4: 'Date' | V4: 'When / Notes' | S5: 3 | T5: 2 | U5: '=IF(OR(OR(Q5="",S5=""),T5=""),"",(DATE(Schedule!$B$6,Q5,1)+(S5-1)*... -> 2023-01-16 00:00:00 | V5: 'January 1' | S6: 3 | T6: 2 | U6: '=IF(OR(OR(Q6="",S6=""),T6=""),"",(DATE(Schedule!$B$6,Q6,1)+(S6-1)*... -> 2023-02-20 00:00:00 | V6: 'The 3rd Monday in January' | S7: 2 | T7: 1 | U7: '=IF(OR(OR(Q7="",S7=""),T7=""),"",(DATE(Schedule!$B$6,Q7,1)+(S7-1)*... -> 2023-05-14 00:00:00 | V7: '2nd Sunday in May'

### `447f9eaa5b6c|HIDDEN_STRUCTURE_IN_TOTAL|Employee1!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/2_382-29_input.xlsx`
- location: `Employee 1!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden rows 23 to 24 on Employee 1 feed 24 visible formula(s): Employee 1!U3, Employee 1!V3, Employee 1!AB6, Employee 1!AB7, Employee 1!AB8, Employee 1!AB9, Employee 1!AB10, Employee 1!AB11, and 16 more.
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `3876d02857ce|HIDDEN_STRUCTURE_IN_TOTAL|DATACARS!B24`

- workbook: `all_data_912_v0.1/spreadsheet/58829/2_58829_input.xlsx`
- location: `DATA CARS!B24`  severity: Medium  confidence: Review
- formula: `=Afschrijving!B4`
- evidence: Hidden sheet 'Afschrijving' feeds 4 visible formula(s): DATA CARS!B24, DATA CARS!C24, DATA CARS!D24, DATA CARS!E24.
- cached value: 0.73496; row labels: ["'DISCOUNT'"]; column header: ''; used range: A1:F32
- neighbourhood: A22: 'FIRST REGISTARTION' | B22: 2017-05-01 00:00:00 | C22: 2018-05-01 00:00:00 | D22: 2019-05-01 00:00:00 | A23: 'DATE TO BUY' | B23: 2022-05-01 00:00:00 | C23: 2022-05-01 00:00:00 | D23: 2022-05-01 00:00:00 | A24: 'DISCOUNT' | B24: '=Afschrijving!B4' -> 0.73496 | C24: '=Afschrijving!M4' -> 0.665 | D24: '=Afschrijving!N4' -> 0.56998

### `d7bb3bd8958a|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25`

- workbook: `all_data_912_v0.1/spreadsheet/57989/1_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden rows 12, 17 on Sheet1 feed 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, and 125 more.
- cached value: 0; row labels: ["'Driver 1'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 1' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 2' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 1 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 3' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 1 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden rows 22 to 498 on Inbound Receipts feed 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, and 14 more.
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!N3`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!N3`  severity: Medium  confidence: Review
- formula: `=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Errors!$B:$B,"="&$B3,Errors!$AB:$AB,"="&$G3,Errors!$AB:$AB,"="&$H3,Errors!$AB:$AB,"="&$I3,Errors!$AB:$AB,"="&$J3)`
- evidence: Hidden rows 2 to 11, 16 to 506 on Errors feed 110 visible formula(s): Daily Numbers!N3, Daily Numbers!O3, Daily Numbers!P3, Daily Numbers!Q3, Daily Numbers!R3, Daily Numbers!N4, Daily Numbers!O4, Daily Numbers!P4, and 102 more.
- cached value: 0; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'II'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | P2: 'IT' | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | P3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | P4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | P5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `b55280430702|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25`

- workbook: `all_data_912_v0.1/spreadsheet/57989/3_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden rows 12, 17 on Sheet1 feed 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, and 125 more.
- cached value: 0; row labels: ["'Driver 19'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 19' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 15' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 16' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `5a98e72c8ee6|HIDDEN_STRUCTURE_IN_TOTAL|MonthlyExpensesSummary!E6`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Monthly Expenses Summary!E6`  severity: Medium  confidence: Review
- formula: `=IFERROR(SUMPRODUCT(('Journal Entries'!$C$6:$C$3000='Monthly Expenses Summary'!$B6)*('Journal Entries'!$B$6:$B$3000<>"")*(MONTH('Journal Entries'!$B$6:$B$3000)=MONTH(E$4&0))*(YEAR('Journal Entries'!$B$6:$B$3000)='Monthly Expenses Summary'!$R$2)*('Journal Entries'!$F$6:$F$3000)),"")`
- evidence: Hidden row 2 on Monthly Expenses Summary feeds 480 visible formula(s): Monthly Expenses Summary!E6, Monthly Expenses Summary!F6, Monthly Expenses Summary!G6, Monthly Expenses Summary!H6, Monthly Expenses Summary!I6, Monthly Expenses Summary!J6, Monthly Expenses Summary!K6, Monthly Expenses Summary!L6, and 472 more.
- cached value: 0; row labels: ["'Building Rent'"]; column header: "'January'"; used range: A1:R65
- range 'Journal Entries'!$C$6:$C$3000: values ["'WG/CR/027'", "'WG/CR/001'", "'WG/CR/006'", "'WG/CR/006'", "'WG/CR/008'", "'WG/CR/006'", "'WG/CR/007'", "'WG/CR/003'", "'WG/CR/001'", "'WG/CR/027'", "'WG/CR/028'", "'WG/CR/029'"]; beyond: {'above': "C5: 'Item Code'", 'below': 'C3001: None'}
- neighbourhood: C4: 'Final Acc. Entry' | D4: 'Account Title' | E4: 'January' | F4: 'February' | G4: 'March' | D5: 'Expenses' | C6: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D6: 'Building Rent' | E6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G6: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 35000 | C7: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D7: 'Electricity' | E7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G7: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | C8: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D8: 'Fuel' | E8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | G8: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 2000

### `447f9eaa5b6c|HIDDEN_STRUCTURE_IN_TOTAL|Employee3!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/2_382-29_input.xlsx`
- location: `Employee 3!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden rows 23 to 24 on Employee 3 feed 25 visible formula(s): Employee 3!U3, Employee 3!V3, Employee 3!AB5, Employee 3!AB6, Employee 3!AB7, Employee 3!AB8, Employee 3!AB9, Employee 3!AB10, and 17 more.
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

### `7f9746d5c513|HIDDEN_STRUCTURE_IN_TOTAL|EXAMPLE!I13`

- workbook: `all_data_912_v0.1/spreadsheet/58656/3_58656_input.xlsx`
- location: `EXAMPLE!I13`  severity: Medium  confidence: Review
- formula: `=D13-D12`
- evidence: Hidden row 12 on EXAMPLE feeds 2 visible formula(s): EXAMPLE!I13, EXAMPLE!J13.
- cached value: 7; row labels: ["'3'", "'n'"]; column header: ''; used range: A1:K36
- neighbourhood: G11: 'M' | H11: 2021-03-20 11:37:00 | I11: '=D11-D10' -> 8 | J11: '=IF(G11="n","1",J10+I11)' -> 17 | G12: 'G' | H12: 2021-03-20 11:37:00 | I12: '=D12-D11' -> 7 | J12: '=IF(G12="n","1",J11+I12)' -> 24 | G13: 'n' | H13: 2021-03-20 11:37:00 | I13: '=D13-D12' -> 7 | J13: '=IF(G13="n","1",J12+I13)' -> '1' | G14: 'T' | H14: 2021-03-20 11:37:00 | I14: '=D14-D13' -> 8 | J14: '=IF(G14="n","1",J13+I14)' -> 9 | G15: 'M' | H15: 2021-03-20 11:37:00 | I15: '=D15-D14' -> 7 | J15: '=IF(G15="n","1",J14+I15)' -> 16

### `ca735d6e64af|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H4`

- workbook: `all_data_912_v0.1/spreadsheet/50154/1_50154_input.xlsx`
- location: `Sheet1!H4`  severity: Medium  confidence: Review
- formula: `=SUM(G4,F4)`
- evidence: Hidden columns F to G on Sheet1 feed 11 visible formula(s): Sheet1!H4, Sheet1!H5, Sheet1!H6, Sheet1!H7, Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, and 3 more.
- cached value: 7.66666666666667; row labels: ["'Winter Guard #1'", "'Y'"]; column header: "'Final Score'"; used range: A1:O15
- neighbourhood: F3: 'Splash page points' | G3: 'AVG' | H3: 'Final Score' | F4: '=IF(D4="Y",1,0)' -> 1 | G4: '=AVERAGE(B4:C4,E4)' -> 6.66666666666667 | H4: '=SUM(G4,F4)' -> 7.66666666666667 | F5: '=IF(D5="Y",1,0)' -> 0 | G5: '=AVERAGE(B5:C5,E5)' -> 6.33333333333333 | H5: '=SUM(G5,F5)' -> 6.33333333333333 | F6: '=IF(D6="Y",1,0)' -> 1 | G6: '=AVERAGE(B6:C6,E6)' -> 6.66666666666667 | H6: '=SUM(G6,F6)' -> 7.66666666666667

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!BG3`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!BG3`  severity: Medium  confidence: Review
- formula: `=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")`
- evidence: Hidden columns P, R to BE on formamspnc (7) feed 274 visible formula(s): formamspnc (7)!BG3, formamspnc (7)!BH3, formamspnc (7)!BI3, formamspnc (7)!I5, formamspnc (7)!O5, formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, and 266 more.
- cached value: 0; row labels: ["'m2'", "'m3'"]; column header: ''; used range: A1:ED48610
- range BI5:BI11: values ['None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'BI4: None', 'below': 'BI12: None'}
- neighbourhood: BE2: 12 | BF2: 13 | BE3: 'm2' | BF3: 'm3' | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BH3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),2) {array BH3}' -> '#NUM!' | BI3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),3) {array BI3}' -> '#NUM!' | BE5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")... -> None | BF5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")... -> None

## IFERROR_MASK

### `f97f2feedd64|IFERROR_MASK|RESULTS1!R8`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!R8`  severity: Medium  confidence: Review
- formula: `=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",Table1[PM MAX GAP],"<50%",Table1[SETUP],$P8),0)`
- evidence: IFERROR replaces any error from AVERAGEIFS with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are RESULTS 1!R9, RESULTS 1!R10, RESULTS 1!R11, RESULTS 1!R12.
- cached value: 0; row labels: ["'PMH'"]; column header: "'20-50%'"; used range: A1:W67
- neighbourhood: P7: 'AVE G/L' | Q7: '< 20%' | R7: '20-50%' | S7: '50-75%' | T7: '75-100%' | P8: 'PMH' | Q8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | P9: 'Pivot' | Q9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | P10: 'HOD' | Q10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0

### `70420e2dcf7b|IFERROR_MASK|PAYMENT!F8`

- workbook: `all_data_912_v0.1/spreadsheet/49490/1_49490_input.xlsx`
- location: `PAYMENT!F8`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter('PRICE LIST'!$E$2:$E1001,'PRICE LIST'!$A$2:$A1001=$D8,'PRICE LIST'!$B$2:$B1001=A8,'PRICE LIST'!$C$2:$C1001=B8,'PRICE LIST'!$D$2:$D1001=C8),1,1))"),"")`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, "": the cell holds a frozen value, not a live calculation.
- cached value: None; row labels: []; column header: ''; used range: A1:L1001
- range 'PRICE LIST'!$E$2:$E1001: values ['7', '7', '7', '9', '9', '10', '9.5', '9.5', '10.5', '12.25', '12.25', '12.7']; beyond: {'above': "E1: 'PRICE'", 'below': 'E1002: None'}
- neighbourhood: D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 210 | F6: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> 7 | G6: 1470 | D7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E7: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F7: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | D8: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E8: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F8: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | D9: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E9: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F9: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | E10: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F10: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None

### `6fd6aa9b279e|IFERROR_MASK|PAYMENT!C7`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `PAYMENT!C7`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NAKSHI")`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, "NAKSHI": the cell holds a frozen value, not a live calculation.
- cached value: 'NAKSHI'; row labels: []; column header: ''; used range: A1:L1001
- neighbourhood: A5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"BEDCOVER")' -> 'BEDCOVER' | B5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"90*100")' -> '90*100' | C5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NEW NAKSHI")' -> 'NEW NAKSHI' | D5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E5: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 105 | A6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")' -> 'PILLOW' | C6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"SINGLE")' -> 'SINGLE' | D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 210 | C7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NAKSHI")' -> 'NAKSHI' | D7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E7: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | C8: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NEW NAKSHI")' -> 'NEW NAKSHI' | D8: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E8: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | C9: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"SINGLE")' -> 'SINGLE' | D9: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E9: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None

### `6fd6aa9b279e|IFERROR_MASK|BIRJUPAYMENT!A6`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `BIRJU PAYMENT!A6`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, "PILLOW": the cell holds a frozen value, not a live calculation.
- cached value: 'PILLOW'; row labels: []; column header: ''; used range: A1:E13
- neighbourhood: A4: 'TYPE' | C4: 'PCS' | A5: '=IFERROR(__xludf.DUMMYFUNCTION("SORT(UNIQUE(Sheet1!T3:T12524))"),"... -> 'BEDCOVER' | C5: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> 105 | A6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")' -> 'PILLOW' | C6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> 0 | C7: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> None | C8: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> None

### `57d001666bfd|IFERROR_MASK|Sheet1!E3`

- workbook: `all_data_912_v0.1/spreadsheet/52964/1_52964_input.xlsx`
- location: `Sheet1!E3`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($AG$2:$AG$124,MATCH($A3,$AA$2:$AA124,0)),0)`
- evidence: IFERROR replaces any error from INDEX, MATCH with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 0; row labels: []; column header: ''; used range: A1:BE279
- range $AG$2:$AG$124: values ['13', '6', '1', '3', '2', '3', '2', '6', '8', '3', '2', '1']; beyond: {'above': "AG1: 'LoS'", 'below': 'AG125: None'}
- neighbourhood: C1: 'Mortality < 30 Days  ( GERIATRIC SUR... | D1: 'Postoperative Delirium ( ADMITTED PT... | E1: 'LOS  ( ADMITTED PTS DX AL) COMPLETE' | F1: 'LOS > 14 Days (FORMULA) COMPLETE' | G1: 'Readmission < 30 days ( GERIATRIC DI... | D2: '=IF(COUNTIF(AF2,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E2: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A2,$AA$2:$AA124,0)),0)' -> 6 | F2: '=IF(E2>14,E2,"N/A")' -> 'N/A' | D3: '=IF(COUNTIF(AF3,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E3: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A3,$AA$2:$AA124,0)),0)' -> 0 | F3: '=IF(E3>14,E3,"N/A")' -> 'N/A' | D4: '=IF(COUNTIF(AF4,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E4: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A4,$AA$2:$AA124,0)),0)' -> 0 | F4: '=IF(E4>14,E4,"N/A")' -> 'N/A' | D5: '=IF(COUNTIF(AF5,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E5: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A5,$AA$2:$AA124,0)),0)' -> 0 | F5: '=IF(E5>14,E5,"N/A")' -> 'N/A'

### `125be9ba2e04|IFERROR_MASK|RESULTS1!O14`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!O14`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[WEEK],$J14)/COUNTIFS(Table1[ENTRY ATTEMPT],"<>",Table1[WEEK],$J14),0)`
- evidence: IFERROR replaces any error from a division with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 10 cells on this sheet; the others are RESULTS 1!O15, RESULTS 1!O16, RESULTS 1!O17, RESULTS 1!O18, RESULTS 1!O19, RESULTS 1!O20, RESULTS 1!O21, RESULTS 1!O22, and 1 more.
- cached value: 0; row labels: ["'Max stop loss for entry price < 20 is 30c, > 20 is 50c'"]; column header: "'ENTRY %'"; used range: A1:X80
- neighbourhood: M12: '=AVERAGE(Table2[POINTS])' -> -2.9 | N12: '=AVERAGE(Table2[ENTRY %])' -> 0 | M13: 'POINTS' | N13: 'G/L $' | O13: 'ENTRY %' | Q13: 'ENTRY (10)' | M14: '=SUMIFS(Table1[POINTS],Table1[WEEK],$J14)' -> -29 | N14: '=SUMIFS(Table1[G/L $],Table1[WEEK],$J14)' -> 0 | O14: '=IFERROR(COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[WEEK],$J14)/CO... -> 0 | Q14: '< 100M' | M15: '=SUMIFS(Table1[POINTS],Table1[WEEK],$J15)' -> 0 | N15: '=SUMIFS(Table1[G/L $],Table1[WEEK],$J15)' -> 0 | O15: '=IFERROR(COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[WEEK],$J15)/CO... -> 0 | Q15: '100-500M' | M16: '=SUMIFS(Table1[POINTS],Table1[WEEK],$J16)' -> 0 | N16: '=SUMIFS(Table1[G/L $],Table1[WEEK],$J16)' -> 0 | O16: '=IFERROR(COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[WEEK],$J16)/CO... -> 0 | Q16: '500M-1B'

### `750361651608|IFERROR_MASK|PAYMENT!B5`

- workbook: `all_data_912_v0.1/spreadsheet/49490/3_49490_input.xlsx`
- location: `PAYMENT!B5`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"90*100")`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, "90*100": the cell holds a frozen value, not a live calculation.
- cached value: '90*100'; row labels: []; column header: ''; used range: A1:L1001
- neighbourhood: A3: 'TYPE' | B3: 'SIZE' | C3: 'STITCHING' | D3: 'PURPOSE' | A4: '=IFERROR(__xludf.DUMMYFUNCTION("sort(unique(Sheet1!F3:I1001))"),"B... -> 'BEDCOVER' | B4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"60*90")' -> '60*90' | C4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),FALSE)' -> False | D4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | A5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"BEDCOVER")' -> 'BEDCOVER' | B5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"90*100")' -> '90*100' | C5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NEW NAKSHI")' -> 'NEW NAKSHI' | D5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | A6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"PILLOW")' -> 'PILLOW' | C6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"SINGLE")' -> 'SINGLE' | D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | C7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"NAKSHI")' -> 'NAKSHI' | D7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING'

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!T5`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!T5`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Table1[WEEK])-4),Table1[POINTS G/L])),10%),0)`
- evidence: IFERROR replaces any error from TRIMMEAN with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 8.31333333333333; row labels: ["'This includes time off and days no trades available'", "'Last 5 Wk'"]; column header: ''; used range: A1:W67
- neighbourhood: R3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=5,Table1[POINTS G/L]),10%) {array R3}' -> 5.20833333333333 | S3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=6,Table1[POINTS G/L]),10%) {array S3}' -> 5.89777777777778 | T3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=7,Table1[POINTS G/L]),10%) {array T3}' -> 7.165 | U3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=8,Table1[POINTS G/L]),10%) {array U3}' -> 9.11 | V3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=9,Table1[POINTS G/L]),10%) {array V3}' -> 9.74666666666667 | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.20833333333333 | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.89777777777778 | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 7.165 | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 9.11 | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF((Table1[WEEK]>=MAX(Tab... -> 9.74666666666667 | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.22571428571429 | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.83833333333333 | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF((Table1[WEEK]>=MAX(Tab... -> 8.87 | R7: '20-50%' | S7: '50-75%' | T7: '75-100%' | U7: '100-150%' | V7: '150-200%'

### `86bd0c65882c|IFERROR_MASK|Sheet1!M2`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!M2`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($T$2:$T$124,MATCH($A2,$Q$2:$Q124,0)),0)`
- evidence: IFERROR replaces any error from INDEX, MATCH with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 'Female'; row labels: []; column header: "'Gender  ( GERIATRIC SURG LOG X)  '"; used range: A1:BE279
- range $T$2:$T$124: values ["'Female'", "'Male'", "'Female'", "'Male'", "'Female'", "'Male'", "'Male'", "'Female'", "'Female'", "'Male'", "'Female'", "'Male'"]; beyond: {'above': "T1: 'Gender'", 'below': 'T125: None'}
- neighbourhood: K1: 'Age  ( GERIATRIC SURG LOG W)  ' | L1: 'Age range ( CALCULATION)' | M1: 'Gender  ( GERIATRIC SURG LOG X)  ' | N1: 'Date of Surgery  ( GERIATRIC SURG LO... | O1: 'Procedure Month and year ( FORMAT CE... | K2: '=IFERROR(INDEX($S$2:$S$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 75 | L2: '=IF(K2<85,"75-84",">85")' -> '75-84' | M2: '=IFERROR(INDEX($T$2:$T$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 'Female' | N2: '=IFERROR(INDEX($U$2:$U$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 2021-04-01 00:00:00 | O2: '=N2' -> 2021-04-01 00:00:00 | K3: '=IFERROR(INDEX($S$2:$S$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 76 | L3: '=IF(K3<85,"75-84",">85")' -> '75-84' | M3: '=IFERROR(INDEX($T$2:$T$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 'Male' | N3: '=IFERROR(INDEX($U$2:$U$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 2021-04-01 00:00:00 | O3: '=N3' -> 2021-04-01 00:00:00 | K4: '=IFERROR(INDEX($S$2:$S$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 91 | L4: '=IF(K4<85,"75-84",">85")' -> '>85' | M4: '=IFERROR(INDEX($T$2:$T$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 'Female' | N4: '=IFERROR(INDEX($U$2:$U$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 2021-06-24 00:00:00 | O4: '=N4' -> 2021-06-24 00:00:00

### `552f4c55b2df|IFERROR_MASK|OrderSheetFinal!AK6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!AK6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,[1]D1!$B$55:$K$65,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AK7, Order Sheet Final!AK8, Order Sheet Final!AK9, Order Sheet Final!AK10, Order Sheet Final!AK11, Order Sheet Final!AK12, Order Sheet Final!AK13, Order Sheet Final!AK14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'D1'"; used range: A1:AS37
- neighbourhood: AI4: '=SUM(AI6:AI33)' -> 0 | AJ4: '=SUM(AJ6:AJ33)' -> 0 | AK4: '=SUM(AK6:AK33)' -> 0 | AL4: '=SUM(AL6:AL33)' -> 10 | AM4: '=SUM(AM6:AM33)' -> 0 | AI5: 'C14.1' | AJ5: 'C14.2' | AK5: 'D1' | AL5: 'D2' | AM5: 'D3' | AI6: "=IFERROR(VLOOKUP(B6,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ6: "=IFERROR(VLOOKUP(B6,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK6: '=IFERROR(VLOOKUP(B6,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL6: '=IFERROR(VLOOKUP(B6,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0 | AM6: '=IFERROR(VLOOKUP(B6,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0 | AI7: "=IFERROR(VLOOKUP(B7,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ7: "=IFERROR(VLOOKUP(B7,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK7: '=IFERROR(VLOOKUP(B7,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL7: '=IFERROR(VLOOKUP(B7,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 2 | AM7: '=IFERROR(VLOOKUP(B7,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0 | AI8: "=IFERROR(VLOOKUP(B8,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AJ8: "=IFERROR(VLOOKUP(B8,'[1]C14.2'!$B$55:$K$59,10,FALSE),0)" -> 0 | AK8: '=IFERROR(VLOOKUP(B8,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL8: '=IFERROR(VLOOKUP(B8,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0 | AM8: '=IFERROR(VLOOKUP(B8,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0

### `1a947d3f59c7|IFERROR_MASK|Sheet1!E27`

- workbook: `all_data_912_v0.1/spreadsheet/45738/3_45738_input.xlsx`
- location: `Sheet1!E27`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D6,0)+1,"m"),12/$C6)=0)*$B6,0)+(EOMONTH($D6,0)=E$4)*$A6`
- evidence: IFERROR replaces any error from MOD, DATEDIF, arithmetic on a cell, EOMONTH, a division with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 480 cells on this sheet; the others are Sheet1!F27, Sheet1!G27, Sheet1!H27, Sheet1!I27, Sheet1!J27, Sheet1!K27, Sheet1!L27, Sheet1!M27, and 471 more.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: C25: 1 | D25: 2023-11-22 00:00:00 | E27: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D6,0)+1,"m"),12/$C6)=0)*$B6,0... -> 0 | F27: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D6,0)+1,"m"),12/$C6)=0)*$B6,0... -> 0 | G27: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D6,0)+1,"m"),12/$C6)=0)*$B6,0... -> 0 | E28: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D7,0)+1,"m"),12/$C7)=0)*$B7,0... -> 0 | F28: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D7,0)+1,"m"),12/$C7)=0)*$B7,0... -> 0 | G28: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D7,0)+1,"m"),12/$C7)=0)*$B7,0... -> 0 | E29: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | F29: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | G29: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0

### `750361651608|IFERROR_MASK|BIRJUPAYMENT!D8`

- workbook: `all_data_912_v0.1/spreadsheet/49490/3_49490_input.xlsx`
- location: `BIRJU PAYMENT!D8`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(Sheet1!$W$3:$W12524,Sheet1!$T$3:$T12524=$A8),1,1))"),"")`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, "": the cell holds a frozen value, not a live calculation.
- cached value: None; row labels: []; column header: ''; used range: A1:E13
- range Sheet1!$W$3:$W12524: values ['1.5', '1.5', '1.5', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "W2: 'PRICE'", 'below': 'W12525: None'}
- neighbourhood: C6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> 0 | D6: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(Sheet1!$W$3:$... -> 0.9 | E6: '=IF(D6<>"",C6*D6,"")' -> 0 | C7: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> None | D7: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(Sheet1!$W$3:$... -> None | E7: '=IF(D7<>"",C7*D7,"")' -> None | C8: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> None | D8: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(Sheet1!$W$3:$... -> None | E8: '=IF(D8<>"",C8*D8,"")' -> None | C9: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!O:X,""SELECT ... -> None | D9: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(Sheet1!$W$3:$... -> None | E9: '=IF(D9<>"",C9*D9,"")' -> None

### `57d001666bfd|IFERROR_MASK|Sheet1!J2`

- workbook: `all_data_912_v0.1/spreadsheet/52964/1_52964_input.xlsx`
- location: `Sheet1!J2`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($R$2:$R$124,MATCH($A2,$Q$2:$Q124,0)),0)`
- evidence: IFERROR replaces any error from INDEX, MATCH with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 1946-03-11 00:00:00; row labels: []; column header: "'Date of Birth  ( GERIATRIC SURG LOG V)  '"; used range: A1:BE279
- range $R$2:$R$124: values ['1946-03-11 00:00:00', '1944-04-11 00:00:00', '1930-06-17 00:00:00', '1942-07-08 00:00:00', '1941-10-15 00:00:00', '1934-01-27 00:00:00', '1935-05-08 00:00:00', '1938-08-05 00:00:00', '1940-01-05 00:00:00', '1932-08-05 00:00:00', '1945-04-08 00:00:00', '1944-06-26 00:00:00']; beyond: {'above': "R1: 'Date of Birth'", 'below': 'R125: None'}
- neighbourhood: H1: 'ICU > 3 Days ( GERI ICU TRANSFER)' | I1: 'High Risk ( MANUAL INPUT )' | J1: 'Date of Birth  ( GERIATRIC SURG LOG ... | K1: 'Age  ( GERIATRIC SURG LOG W)  ' | L1: 'Age range ( CALCULATION)' | J2: '=IFERROR(INDEX($R$2:$R$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 1946-03-11 00:00:00 | K2: '=IFERROR(INDEX($S$2:$S$124,MATCH($A2,$Q$2:$Q124,0)),0)' -> 75 | L2: '=IF(K2<85,"75-84",">85")' -> '75-84' | J3: '=IFERROR(INDEX($R$2:$R$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 1944-04-11 00:00:00 | K3: '=IFERROR(INDEX($S$2:$S$124,MATCH($A3,$Q$2:$Q124,0)),0)' -> 76 | L3: '=IF(K3<85,"75-84",">85")' -> '75-84' | J4: '=IFERROR(INDEX($R$2:$R$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 1930-06-17 00:00:00 | K4: '=IFERROR(INDEX($S$2:$S$124,MATCH($A4,$Q$2:$Q124,0)),0)' -> 91 | L4: '=IF(K4<85,"75-84",">85")' -> '>85'

### `552f4c55b2df|IFERROR_MASK|OrderSheetFinal!T6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!T6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]S14.2'!$B$58:$K$63,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!T7, Order Sheet Final!T8, Order Sheet Final!T9, Order Sheet Final!T10, Order Sheet Final!T11, Order Sheet Final!T12, Order Sheet Final!T13, Order Sheet Final!T14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'S14.2'"; used range: A1:AS37
- neighbourhood: R4: '=SUM(R6:R33)' -> 19 | S4: '=SUM(S6:S33)' -> 13 | T4: '=SUM(T6:T33)' -> 13 | U4: '=SUM(U6:U33)' -> 13 | V4: '=SUM(V6:V33)' -> 7 | R5: 'S13.3' | S5: 'S14.1' | T5: 'S14.2' | U5: 'S14.3' | V5: 'S15' | R6: "=IFERROR(VLOOKUP(B6,'[1]S13.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | S6: "=IFERROR(VLOOKUP(B6,'[1]S14.1'!$B$58:$K$69,10,FALSE),0)" -> 0 | T6: "=IFERROR(VLOOKUP(B6,'[1]S14.2'!$B$58:$K$63,10,FALSE),0)" -> 0 | U6: "=IFERROR(VLOOKUP(B6,'[1]S14.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | V6: '=IFERROR(VLOOKUP(B6,[1]S15!$B$55:$K$63,10,FALSE),0)' -> 0 | R7: "=IFERROR(VLOOKUP(B7,'[1]S13.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | S7: "=IFERROR(VLOOKUP(B7,'[1]S14.1'!$B$58:$K$69,10,FALSE),0)" -> 0 | T7: "=IFERROR(VLOOKUP(B7,'[1]S14.2'!$B$58:$K$63,10,FALSE),0)" -> 0 | U7: "=IFERROR(VLOOKUP(B7,'[1]S14.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | V7: '=IFERROR(VLOOKUP(B7,[1]S15!$B$55:$K$63,10,FALSE),0)' -> 0 | R8: "=IFERROR(VLOOKUP(B8,'[1]S13.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | S8: "=IFERROR(VLOOKUP(B8,'[1]S14.1'!$B$58:$K$69,10,FALSE),0)" -> 0 | T8: "=IFERROR(VLOOKUP(B8,'[1]S14.2'!$B$58:$K$63,10,FALSE),0)" -> 0 | U8: "=IFERROR(VLOOKUP(B8,'[1]S14.3'!$B$58:$K$63,10,FALSE),0)" -> 0 | V8: '=IFERROR(VLOOKUP(B8,[1]S15!$B$55:$K$63,10,FALSE),0)' -> 0

### `86bd0c65882c|IFERROR_MASK|Sheet1!N12`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!N12`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($U$2:$U$124,MATCH($A12,$Q$2:$Q124,0)),0)`
- evidence: IFERROR replaces any error from INDEX, MATCH with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 2021-04-13 00:00:00; row labels: []; column header: ''; used range: A1:BE279
- range $U$2:$U$124: values ['2021-04-01 00:00:00', '2021-04-01 00:00:00', '2021-06-24 00:00:00', '2021-05-07 00:00:00', '2021-05-12 00:00:00', '2021-06-21 00:00:00', '2021-04-07 00:00:00', '2021-06-30 00:00:00', '2021-06-29 00:00:00', '2021-06-22 00:00:00', '2021-04-13 00:00:00', '2021-04-13 00:00:00']; beyond: {'above': "U1: 'Date'", 'below': 'U125: None'}
- neighbourhood: L10: '=IF(K10<85,"75-84",">85")' -> '75-84' | M10: '=IFERROR(INDEX($T$2:$T$124,MATCH($A10,$Q$2:$Q124,0)),0)' -> 'Female' | N10: '=IFERROR(INDEX($U$2:$U$124,MATCH($A10,$Q$2:$Q124,0)),0)' -> 2021-06-29 00:00:00 | O10: '=N10' -> 2021-06-29 00:00:00 | L11: '=IF(K11<85,"75-84",">85")' -> '>85' | M11: '=IFERROR(INDEX($T$2:$T$124,MATCH($A11,$Q$2:$Q124,0)),0)' -> 'Male' | N11: '=IFERROR(INDEX($U$2:$U$124,MATCH($A11,$Q$2:$Q124,0)),0)' -> 2021-06-22 00:00:00 | O11: '=N11' -> 2021-06-22 00:00:00 | L12: '=IF(K12<85,"75-84",">85")' -> '75-84' | M12: '=IFERROR(INDEX($T$2:$T$124,MATCH($A12,$Q$2:$Q124,0)),0)' -> 'Female' | N12: '=IFERROR(INDEX($U$2:$U$124,MATCH($A12,$Q$2:$Q124,0)),0)' -> 2021-04-13 00:00:00 | O12: '=N12' -> 2021-04-13 00:00:00 | L13: '=IF(K13<85,"75-84",">85")' -> '75-84' | M13: '=IFERROR(INDEX($T$2:$T$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 'Male' | N13: '=IFERROR(INDEX($U$2:$U$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 2021-04-13 00:00:00 | O13: '=N13' -> 2021-04-13 00:00:00 | L14: '=IF(K14<85,"75-84",">85")' -> '75-84' | M14: '=IFERROR(INDEX($T$2:$T$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 'Male' | N14: '=IFERROR(INDEX($U$2:$U$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 2021-05-19 00:00:00 | O14: '=N14' -> 2021-05-19 00:00:00

### `70420e2dcf7b|IFERROR_MASK|Sheet7!F5`

- workbook: `all_data_912_v0.1/spreadsheet/49490/1_49490_input.xlsx`
- location: `Sheet7!F5`  severity: Medium  confidence: Review
- formula: `=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter('PRICE LIST'!$E$2:$E1000,'PRICE LIST'!$A$2:$A1000=$D5,'PRICE LIST'!$B$2:$B1000=A5,'PRICE LIST'!$C$2:$C1000=B5,'PRICE LIST'!$D$2:$D1000=C5),1,1))"),4)`
- evidence: IFERROR wraps a Google Sheets placeholder and returns its cached value, 4: the cell holds a frozen value, not a live calculation.
- cached value: 4; row labels: []; column header: ''; used range: A1:G1000
- range 'PRICE LIST'!$E$2:$E1000: values ['7', '7', '7', '9', '9', '10', '9.5', '9.5', '10.5', '12.25', '12.25', '12.7']; beyond: {'above': "E1: 'PRICE'", 'below': 'E1001: None'}
- neighbourhood: D3: 'PURPOSE' | E3: 'PCS' | F3: 'PRICE' | G3: 'AMOUNT' | D4: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E4: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F4: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None | G4: '=IF(ISNUMBER(E4:E1000)*(E4:E1000>0)*(F4:F1000>0),E4:E1000*F4:F1000... -> None | D5: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E5: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 105 | F5: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> 4 | G5: 420 | D6: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E6: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> 210 | F6: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> 7 | G6: 1470 | D7: '=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"STITCHING")' -> 'STITCHING' | E7: '=IFERROR(__xludf.DUMMYFUNCTION("IFERROR(QUERY(Sheet1!A:L,""SELECT ... -> None | F7: '=IFERROR(__xludf.DUMMYFUNCTION("iferror(index(filter(\'PRICE LIST\... -> None

### `6741b8e20874|IFERROR_MASK|OrderSheetFinal!Z6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!Z6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!Z7, Order Sheet Final!Z8, Order Sheet Final!Z9, Order Sheet Final!Z10, Order Sheet Final!Z11, Order Sheet Final!Z12, Order Sheet Final!Z13, Order Sheet Final!Z14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'C4.1'"; used range: A1:AS37
- neighbourhood: X4: '=SUM(X6:X33)' -> 3 | Y4: '=SUM(Y6:Y33)' -> 0 | Z4: '=SUM(Z6:Z33)' -> 0 | AA4: '=SUM(AA6:AA33)' -> 0 | AB4: '=SUM(AB6:AB33)' -> 10 | X5: 'C2' | Y5: 'C3' | Z5: 'C4.1' | AA5: 'C4.2' | AB5: 'C5' | X6: '=IFERROR(VLOOKUP(B6,[1]C2!$B$51:$K$60,10,FALSE),0)' -> 0 | Y6: '=IFERROR(VLOOKUP(B6,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z6: "=IFERROR(VLOOKUP(B6,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA6: "=IFERROR(VLOOKUP(B6,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB6: '=IFERROR(VLOOKUP(B6,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 1 | X7: '=IFERROR(VLOOKUP(B7,[1]C2!$B$51:$K$60,10,FALSE),0)' -> 1 | Y7: '=IFERROR(VLOOKUP(B7,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z7: "=IFERROR(VLOOKUP(B7,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA7: "=IFERROR(VLOOKUP(B7,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB7: '=IFERROR(VLOOKUP(B7,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 1 | X8: '=IFERROR(VLOOKUP(B8,[1]C2!$B$51:$K$60,10,FALSE),0)' -> 0 | Y8: '=IFERROR(VLOOKUP(B8,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z8: "=IFERROR(VLOOKUP(B8,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA8: "=IFERROR(VLOOKUP(B8,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB8: '=IFERROR(VLOOKUP(B8,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0

### `4ea284d68c01|IFERROR_MASK|Sheet1!AI2`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!AI2`  severity: Medium  confidence: Review
- formula: `=IFERROR(LARGE($K$2:$K$600,ROW(AI1)),(""))`
- evidence: IFERROR replaces any error from LARGE with (""), which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 32 cells on this sheet; the others are Sheet1!AI3, Sheet1!AI4, Sheet1!AI5, Sheet1!AI6, Sheet1!AI7, Sheet1!AI8, Sheet1!AI9, Sheet1!AI10, and 23 more.
- cached value: 127; row labels: ["'High Scratch Game #1'", "'100 Avg w/125 Gm #1'"]; column header: "'Score'"; used range: A1:CJ782
- range $K$2:$K$600: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "K1: '100 Avg w/125 Gm'", 'below': 'K601: None'}
- neighbourhood: AH1: '100 Avg w/125 Gm' | AI1: 'Score' | AJ1: 'ID#' | AK1: 'Position of Name in List' | AG2: 1 | AH2: '100 Avg w/125 Gm #1' | AI2: '=IFERROR(LARGE($K$2:$K$600,ROW(AI1)),(""))' -> 127 | AJ2: '=IF(AI2="","",SMALL(IF(INDEX($K$2:$K$600,,MATCH(LEFT(AH2,FIND("#",... -> 345 | AK2: '=IFERROR(CEILING(AJ2/21,1)," ")' -> 17 | AG3: 2 | AH3: '100 Avg w/125 Gm #2' | AI3: '=IFERROR(LARGE($K$2:$K$600,ROW(AI2)),(""))' -> 125 | AJ3: '=IF(AI3="","",SMALL(IF(INDEX($K$2:$K$600,,MATCH(LEFT(AH3,FIND("#",... -> 177 | AK3: '=IFERROR(CEILING(AJ3/21,1)," ")' -> 9 | AG4: 3 | AH4: '100 Avg w/125 Gm #3' | AI4: '=IFERROR(LARGE($K$2:$K$600,ROW(AI3)),(""))' -> 125 | AJ4: '=IF(AI4="","",SMALL(IF(INDEX($K$2:$K$600,,MATCH(LEFT(AH4,FIND("#",... -> 353 | AK4: '=IFERROR(CEILING(AJ4/21,1)," ")' -> 17

### `783ba9a086e8|IFERROR_MASK|OrderSheetFinal!U6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!U6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,[1]S14.3!$B$58:$K$63,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!U7, Order Sheet Final!U8, Order Sheet Final!U9, Order Sheet Final!U10, Order Sheet Final!U11, Order Sheet Final!U12, Order Sheet Final!U13, Order Sheet Final!U14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'S14.3'"; used range: A1:AS37
- neighbourhood: S4: '=SUM(S6:S33)' -> 13 | T4: '=SUM(T6:T33)' -> 13 | U4: '=SUM(U6:U33)' -> 13 | V4: '=SUM(V6:V33)' -> 7 | W4: '=SUM(W6:W33)' -> 0 | S5: 'S14.1' | T5: 'S14.2' | U5: 'S14.3' | V5: 'S15' | W5: 'C1' | S6: '=IFERROR(VLOOKUP(B6,[1]S14.1!$B$58:$K$69,10,FALSE),0)' -> 0 | T6: '=IFERROR(VLOOKUP(B6,[1]S14.2!$B$58:$K$63,10,FALSE),0)' -> 0 | U6: '=IFERROR(VLOOKUP(B6,[1]S14.3!$B$58:$K$63,10,FALSE),0)' -> 0 | V6: "=IFERROR(VLOOKUP(B6,'[1]S15'!$B$55:$K$63,10,FALSE),0)" -> 0 | W6: "=IFERROR(VLOOKUP(B6,'[1]C1'!$B$55:$K$65,10,FALSE),0)" -> 0 | S7: '=IFERROR(VLOOKUP(B7,[1]S14.1!$B$58:$K$69,10,FALSE),0)' -> 0 | T7: '=IFERROR(VLOOKUP(B7,[1]S14.2!$B$58:$K$63,10,FALSE),0)' -> 0 | U7: '=IFERROR(VLOOKUP(B7,[1]S14.3!$B$58:$K$63,10,FALSE),0)' -> 0 | V7: "=IFERROR(VLOOKUP(B7,'[1]S15'!$B$55:$K$63,10,FALSE),0)" -> 0 | W7: "=IFERROR(VLOOKUP(B7,'[1]C1'!$B$55:$K$65,10,FALSE),0)" -> 0 | S8: '=IFERROR(VLOOKUP(B8,[1]S14.1!$B$58:$K$69,10,FALSE),0)' -> 0 | T8: '=IFERROR(VLOOKUP(B8,[1]S14.2!$B$58:$K$63,10,FALSE),0)' -> 0 | U8: '=IFERROR(VLOOKUP(B8,[1]S14.3!$B$58:$K$63,10,FALSE),0)' -> 0 | V8: "=IFERROR(VLOOKUP(B8,'[1]S15'!$B$55:$K$63,10,FALSE),0)" -> 0 | W8: "=IFERROR(VLOOKUP(B8,'[1]C1'!$B$55:$K$65,10,FALSE),0)" -> 0

### `f97f2feedd64|IFERROR_MASK|RESULTS1!V5`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!V5`  severity: Medium  confidence: Review
- formula: `=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF((Table1[WEEK]>=MAX(Table1[WEEK])-4),Table1[POINTS G/L])),10%),0)`
- evidence: IFERROR replaces any error from TRIMMEAN with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- cached value: 8.87; row labels: ["'This includes time off and days no trades available'", "'Last 5 Wk'"]; column header: ''; used range: A1:W67
- neighbourhood: T3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=7,Table1[POINTS G/L]),10%) {array T3}' -> 7.165 | U3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=8,Table1[POINTS G/L]),10%) {array U3}' -> 9.11 | V3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=9,Table1[POINTS G/L]),10%) {array V3}' -> 9.74666666666667 | W3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=10,Table1[POINTS G/L]),10%) {array ... -> 9.74666666666667 | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 7.165 | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 9.11 | V4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF((Table1[WEEK]>=MAX(Tab... -> 9.74666666666667 | W4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=10,IF((Table1[WEEK]>=MAX(Ta... -> 9.74666666666667 | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | V5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=9,IF((Table1[WEEK]>=MAX(Tab... -> 8.87 | W5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=10,IF((Table1[WEEK]>=MAX(Ta... -> 8.87 | T7: '75-100%' | U7: '100-150%' | V7: '150-200%' | W7: '200% <'

### `6741b8e20874|IFERROR_MASK|OrderSheetFinal!AM6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!AM6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,[1]D3!$B$61:$K$70,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AM7, Order Sheet Final!AM8, Order Sheet Final!AM9, Order Sheet Final!AM10, Order Sheet Final!AM11, Order Sheet Final!AM12, Order Sheet Final!AM13, Order Sheet Final!AM14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'D3'"; used range: A1:AS37
- neighbourhood: AK4: '=SUM(AK6:AK33)' -> 0 | AL4: '=SUM(AL6:AL33)' -> 10 | AM4: '=SUM(AM6:AM33)' -> 0 | AN4: '=SUM(AN6:AN33)' -> 8 | AO4: '=SUM(AO6:AO33)' -> 8 | AK5: 'D1' | AL5: 'D2' | AM5: 'D3' | AN5: 'T2' | AO5: 'T3' | AK6: '=IFERROR(VLOOKUP(B6,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL6: '=IFERROR(VLOOKUP(B6,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0 | AM6: '=IFERROR(VLOOKUP(B6,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0 | AN6: '=IFERROR(VLOOKUP(B6,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO6: '=IFERROR(VLOOKUP(B6,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AK7: '=IFERROR(VLOOKUP(B7,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL7: '=IFERROR(VLOOKUP(B7,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 2 | AM7: '=IFERROR(VLOOKUP(B7,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0 | AN7: '=IFERROR(VLOOKUP(B7,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO7: '=IFERROR(VLOOKUP(B7,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0 | AK8: '=IFERROR(VLOOKUP(B8,[1]D1!$B$55:$K$65,10,FALSE),0)' -> 0 | AL8: '=IFERROR(VLOOKUP(B8,[1]D2!$B$61:$K$74,10,FALSE),0)' -> 0 | AM8: '=IFERROR(VLOOKUP(B8,[1]D3!$B$61:$K$70,10,FALSE),0)' -> 0 | AN8: '=IFERROR(VLOOKUP(B8,[1]T2!$B$55:$K$65,10,FALSE),0)' -> 0 | AO8: '=IFERROR(VLOOKUP(B8,[1]T3!$B$55:$K$65,10,FALSE),0)' -> 0

### `1ee00a60f590|IFERROR_MASK|Sheet1!CG2`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!CG2`  severity: Medium  confidence: Review
- formula: `=IFERROR(LARGE($U$2:$U$600,ROW(CG1)),(""))`
- evidence: IFERROR replaces any error from LARGE with (""), which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 32 cells on this sheet; the others are Sheet1!CG3, Sheet1!CG4, Sheet1!CG5, Sheet1!CG6, Sheet1!CG7, Sheet1!CG8, Sheet1!CG9, Sheet1!CG10, and 23 more.
- cached value: 125; row labels: ["'Triple Score #1'", "'Consecutive Score #1'"]; column header: "'Score'"; used range: A1:CJ782
- range $U$2:$U$600: values ['None', 'None', '125', 'None', "' '", "' '", '109', "' '", "' '", "' '", "' '", "' '"]; beyond: {'above': "U1: 'Consecutive Score'", 'below': 'U601: None'}
- neighbourhood: CE1: 'Full Name' | CF1: 'Consecutive Score' | CG1: 'Score' | CH1: 'ID#' | CI1: 'Position of Name in List' | CE2: '=IFERROR(INDEX($AF$2:$AF$32,MATCH($CD2,$AG$2:$AG$33,))," ")' -> 'BB BA' | CF2: 'Consecutive Score #1' | CG2: '=IFERROR(LARGE($U$2:$U$600,ROW(CG1)),(""))' -> 125 | CH2: '=IF(CG2="","",SMALL(IF(INDEX($U$2:$U$600,,MATCH(LEFT(CF2,FIND("#",... -> 4 | CI2: '=IFERROR(CEILING(CH2/21,1)," ")' -> 1 | CE3: '=IFERROR(INDEX($AF$2:$AF$32,MATCH($CD3,$AG$2:$AG$33,))," ")' -> 'AA AB' | CF3: 'Consecutive Score #2' | CG3: '=IFERROR(LARGE($U$2:$U$600,ROW(CG2)),(""))' -> 110 | CH3: '=IF(CG3="","",SMALL(IF(INDEX($U$2:$U$600,,MATCH(LEFT(CF3,FIND("#",... -> 35 | CI3: '=IFERROR(CEILING(CH3/21,1)," ")' -> 2 | CE4: '=IFERROR(INDEX($AF$2:$AF$32,MATCH($CD4,$AG$2:$AG$33,))," ")' -> 'AA AB' | CF4: 'Consecutive Score #3' | CG4: '=IFERROR(LARGE($U$2:$U$600,ROW(CG3)),(""))' -> 109 | CH4: '=IF(CG4="","",SMALL(IF(INDEX($U$2:$U$600,,MATCH(LEFT(CF4,FIND("#",... -> 8 | CI4: '=IFERROR(CEILING(CH4/21,1)," ")' -> 1

### `4ea284d68c01|IFERROR_MASK|Sheet1!AS2`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!AS2`  severity: Medium  confidence: Review
- formula: `=IFERROR(LARGE($M$2:$M$600,ROW(AR1)),(""))`
- evidence: IFERROR replaces any error from LARGE with (""), which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 32 cells on this sheet; the others are Sheet1!AS3, Sheet1!AS4, Sheet1!AS5, Sheet1!AS6, Sheet1!AS7, Sheet1!AS8, Sheet1!AS9, Sheet1!AS10, and 23 more.
- cached value: 194; row labels: ["'120 Avg w/150 Gm #1'", "'140 Avg w/175 Gm #1'"]; column header: "'Score'"; used range: A1:CJ782
- range $M$2:$M$600: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '177', 'None', 'None', 'None']; beyond: {'above': "M1: '140 Avg w/175 Gm'", 'below': 'M601: None'}
- neighbourhood: AQ1: 'Full Name' | AR1: '140 Avg w/175 Gm' | AS1: 'Score' | AT1: 'ID#' | AU1: 'Position of Name in List' | AQ2: '=IFERROR(INDEX($AF$2:$AF$32,MATCH(AP2,AG$2:AG$32,0)),"")' -> 'GG AG' | AR2: '140 Avg w/175 Gm #1' | AS2: '=IFERROR(LARGE($M$2:$M$600,ROW(AR1)),(""))' -> 194 | AT2: '=IF(AS2="","",SMALL(IF(INDEX($M$2:$M$600,,MATCH(LEFT(AR2,FIND("#",... -> 141 | AU2: '=IFERROR(CEILING(AT2/21,1)," ")' -> 7 | AQ3: '=IFERROR(INDEX($AF$2:$AF$32,MATCH(AP3,AG$2:AG$32,0)),"")' -> 'BB BA' | AR3: '140 Avg w/175 Gm #2' | AS3: '=IFERROR(LARGE($M$2:$M$600,ROW(AR2)),(""))' -> 178 | AT3: '=IF(AS3="","",SMALL(IF(INDEX($M$2:$M$600,,MATCH(LEFT(AR3,FIND("#",... -> 33 | AU3: '=IFERROR(CEILING(AT3/21,1)," ")' -> 2 | AQ4: '=IFERROR(INDEX($AF$2:$AF$32,MATCH(AP4,AG$2:AG$32,0)),"")' -> 'BB BA' | AR4: '140 Avg w/175 Gm #3' | AS4: '=IFERROR(LARGE($M$2:$M$600,ROW(AR3)),(""))' -> 178 | AT4: '=IF(AS4="","",SMALL(IF(INDEX($M$2:$M$600,,MATCH(LEFT(AR4,FIND("#",... -> 36 | AU4: '=IFERROR(CEILING(AT4/21,1)," ")' -> 2

### `30faaaeef9ee|IFERROR_MASK|RESULTS1!S8`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!S8`  severity: Medium  confidence: Review
- formula: `=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",Table1[PM MAX GAP],"<75%",Table1[SETUP],$P8),0)`
- evidence: IFERROR replaces any error from AVERAGEIFS with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are RESULTS 1!S9, RESULTS 1!S10, RESULTS 1!S11, RESULTS 1!S12.
- cached value: 0; row labels: ["'PMH'"]; column header: "'50-75%'"; used range: A1:W67
- neighbourhood: Q7: '< 20%' | R7: '20-50%' | S7: '50-75%' | T7: '75-100%' | U7: '100-150%' | Q8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U8: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | Q9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U9: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0 | Q10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],"<20%",T... -> 0 | R10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=20%",... -> 0 | S10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=50%",... -> 0 | T10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=75%",... -> 0 | U10: '=IFERROR(AVERAGEIFS(Table1[POINTS G/L],Table1[PM MAX GAP],">=100%"... -> 0

### `783ba9a086e8|IFERROR_MASK|OrderSheetFinal!AO6`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!AO6`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(B6,'[1]T3'!$B$55:$K$65,10,FALSE),0)`
- evidence: IFERROR replaces any error from VLOOKUP with 0, which reads as a real value to anyone looking at the cell and to every formula that uses it.
- evidence: The same relative formula appears in 28 cells on this sheet; the others are Order Sheet Final!AO7, Order Sheet Final!AO8, Order Sheet Final!AO9, Order Sheet Final!AO10, Order Sheet Final!AO11, Order Sheet Final!AO12, Order Sheet Final!AO13, Order Sheet Final!AO14, and 19 more.
- cached value: 0; row labels: ["'600mm Cantilever Arm Slotted'", "'N2'"]; column header: "'T3'"; used range: A1:AS37
- neighbourhood: AM4: '=SUM(AM6:AM33)' -> 0 | AN4: '=SUM(AN6:AN33)' -> 8 | AO4: '=SUM(AO6:AO33)' -> 8 | AP4: '=SUM(AP6:AP33)' -> 4 | AQ4: '=SUM(AQ6:AQ33)' -> 0 | AM5: 'D3' | AN5: 'T2' | AO5: 'T3' | AP5: 'T5' | AQ5: 'SG1.1' | AM6: "=IFERROR(VLOOKUP(B6,'[1]D3'!$B$61:$K$70,10,FALSE),0)" -> 0 | AN6: "=IFERROR(VLOOKUP(B6,'[1]T2'!$B$55:$K$65,10,FALSE),0)" -> 0 | AO6: "=IFERROR(VLOOKUP(B6,'[1]T3'!$B$55:$K$65,10,FALSE),0)" -> 0 | AP6: "=IFERROR(VLOOKUP(B6,'[1]T5'!$B$54:$K$63,10,FALSE),0)" -> 1 | AQ6: '=IFERROR(VLOOKUP(B6,[1]SG1.1!$B$51:$K$54,10,FALSE),0)' -> 0 | AM7: "=IFERROR(VLOOKUP(B7,'[1]D3'!$B$61:$K$70,10,FALSE),0)" -> 0 | AN7: "=IFERROR(VLOOKUP(B7,'[1]T2'!$B$55:$K$65,10,FALSE),0)" -> 0 | AO7: "=IFERROR(VLOOKUP(B7,'[1]T3'!$B$55:$K$65,10,FALSE),0)" -> 0 | AP7: "=IFERROR(VLOOKUP(B7,'[1]T5'!$B$54:$K$63,10,FALSE),0)" -> 0 | AQ7: '=IFERROR(VLOOKUP(B7,[1]SG1.1!$B$51:$K$54,10,FALSE),0)' -> 0 | AM8: "=IFERROR(VLOOKUP(B8,'[1]D3'!$B$61:$K$70,10,FALSE),0)" -> 0 | AN8: "=IFERROR(VLOOKUP(B8,'[1]T2'!$B$55:$K$65,10,FALSE),0)" -> 0 | AO8: "=IFERROR(VLOOKUP(B8,'[1]T3'!$B$55:$K$65,10,FALSE),0)" -> 0 | AP8: "=IFERROR(VLOOKUP(B8,'[1]T5'!$B$54:$K$63,10,FALSE),0)" -> 1 | AQ8: '=IFERROR(VLOOKUP(B8,[1]SG1.1!$B$51:$K$54,10,FALSE),0)' -> 0

## LITERAL_CONSTANT

### `67efc211ab2e|LITERAL_CONSTANT|PalletLog!L10`

- workbook: `all_data_912_v0.1/spreadsheet/34493/1_34493_input.xlsx`
- location: `Pallet Log!L10`  severity: Medium  confidence: Review
- formula: `=COUNTIF($I10:$J10,">0")+IF($K10>225,1,0)+IF($K10>382,1,0)+IF($K10>611,1,0)+IF($K10>845,1,0)+1`
- evidence: Non-trivial numeric literal(s) found: 225, 382, 611, 845.
- evidence: The same relative formula appears in 10 cells on this sheet; the others are Pallet Log!L11, Pallet Log!L12, Pallet Log!L13, Pallet Log!L14, Pallet Log!L16, Pallet Log!L17, Pallet Log!L18, Pallet Log!L19, and 1 more.
- cached value: 2; row labels: ["'#'", "'P'"]; column header: "'White Sheets'"; used range: A1:EWJ1135
- range $I10:$J10: values ['1', '0']; beyond: {'left': 'H10: None', 'right': "K10: '=SUM(J10*2)'"}
- neighbourhood: J10: 0 | K10: '=SUM(J10*2)' -> 0 | L10: '=COUNTIF($I10:$J10,">0")+IF($K10>225,1,0)+IF($K10>382,1,0)+IF($K10... -> 2 | M10: '=SUM(L10-1)' -> 1 | N10: '=SUM(I10+M10)' -> 2 | J11: 0 | K11: '=SUM(J11*2)' -> 0 | L11: '=COUNTIF($I11:$J11,">0")+IF($K11>225,1,0)+IF($K11>382,1,0)+IF($K11... -> 2 | M11: '=SUM(L11-1)' -> 1 | N11: '=SUM(I11+M11)' -> 4 | J12: 0 | K12: '=SUM(J12*2)' -> 0 | L12: '=COUNTIF($I12:$J12,">0")+IF($K12>225,1,0)+IF($K12>382,1,0)+IF($K12... -> 2 | M12: '=SUM(L12-1)' -> 1 | N12: '=SUM(I12+M12)' -> 7

### `970db979d624|LITERAL_CONSTANT|formamspnc(7)!DG6`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!DG6`  severity: Medium  confidence: Review
- formula: `=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1,DS6=1,DT6=1),6,"")`
- evidence: Non-trivial numeric literal(s) found: 6.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are formamspnc (7)!DG7, formamspnc (7)!DG8, formamspnc (7)!DG9, formamspnc (7)!DG10, formamspnc (7)!DG11.
- cached value: None; row labels: ["'13c/15c/18c/21c/23c/25c/33c/35c/39c/44c/49c/51c/55c/59c/..."]; column header: ''; used range: A1:ED48610
- neighbourhood: DH5: '=IF(AND(DO5=1,DP5=1,DQ5=1,DR5=1,DS5=1,DT5=1,DU5=1),7,"")' -> None | DE6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1),4,"")' -> None | DF6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1,DS6=1),5,"")' -> None | DG6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1,DS6=1,DT6=1),6,"")' -> None | DH6: '=IF(AND(DO6=1,DP6=1,DQ6=1,DR6=1,DS6=1,DT6=1,DU6=1),7,"")' -> None | DE7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1),4,"")' -> None | DF7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1,DS7=1),5,"")' -> None | DG7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1,DS7=1,DT7=1),6,"")' -> None | DH7: '=IF(AND(DO7=1,DP7=1,DQ7=1,DR7=1,DS7=1,DT7=1,DU7=1),7,"")' -> None | DE8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1),4,"")' -> None | DF8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1,DS8=1),5,"")' -> None | DG8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1,DS8=1,DT8=1),6,"")' -> None | DH8: '=IF(AND(DO8=1,DP8=1,DQ8=1,DR8=1,DS8=1,DT8=1,DU8=1),7,"")' -> None

### `c212843d66a8|LITERAL_CONSTANT|LeadTimes!K9`

- workbook: `all_data_912_v0.1/spreadsheet/47741/2_47741_input.xlsx`
- location: `Lead Times!K9`  severity: Medium  confidence: Review
- formula: `=WORKDAY(K5,3,K15:K20)`
- evidence: Non-trivial numeric literal(s) found: 3.
- cached value: 2022-11-08 00:00:00; row labels: ["'ELECTRONICS'"]; column header: ''; used range: A1:O31
- range K15:K20: values ['2022-05-30 00:00:00', '2022-07-04 00:00:00', '2022-09-05 00:00:00', '2022-11-24 00:00:00', '2022-11-25 00:00:00', '2022-12-26 00:00:00']; beyond: {'above': 'K14: 2021-12-04 00:00:00', 'below': 'K21: None'}
- neighbourhood: J7: 'STANDARD' | K7: '=WORKDAY(K5,10,K15:K20)' -> 2022-11-17 00:00:00 | L7: '-' | M7: '=WORKDAY(K5,10,K15:K20)' -> 2022-11-17 00:00:00 | J8: 'FULL CUSTOM' | K8: '=WORKDAY(K5,18,K15:K20)' -> 2022-12-01 00:00:00 | L8: '-' | M8: '=WORKDAY(K5,18,K15:K20)' -> 2022-12-01 00:00:00 | J9: 'ELECTRONICS' | K9: '=WORKDAY(K5,3,K15:K20)' -> 2022-11-08 00:00:00 | L9: '-' | M9: '=WORKDAY(K5,5,K15:K20)' -> 2022-11-10 00:00:00

### `ec5304138d83|LITERAL_CONSTANT|Current!D7`

- workbook: `all_data_912_v0.1/spreadsheet/45937/1_45937_input.xlsx`
- location: `Current!D7`  severity: Medium  confidence: Review
- formula: `=IF(B7<=59,"A",IF(AND(B7>59,B7<=99),"B",IF(AND(B7>99,B7<=139),"C",IF(AND(B7>139,B7<=179),"D","E"))))`
- evidence: Non-trivial numeric literal(s) found: 59, 59, 99, 99, 139, 139, 179.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Current!D8, Current!D9.
- cached value: 'A'; row labels: []; column header: "'Category'"; used range: A1:N22
- neighbourhood: B6: 'Number' | C6: 'kms' | D6: 'Category' | E6: '%' | B7: 59 | C7: 25000 | D7: '=IF(B7<=59,"A",IF(AND(B7>59,B7<=99),"B",IF(AND(B7>99,B7<=139),"C",... -> 'A' | E7: 22.5 | B8: 60 | C8: 25000 | D8: '=IF(B8<=59,"A",IF(AND(B8>59,B8<=99),"B",IF(AND(B8>99,B8<=139),"C",... -> 'B' | B9: 100 | C9: 26002 | D9: '=IF(B9<=59,"A",IF(AND(B9>59,B9<=99),"B",IF(AND(B9>99,B9<=139),"C",... -> 'C'

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!S35`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!S35`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[POINTS G/L],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'PM Trades'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: Q33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `c4229dd05b85|LITERAL_CONSTANT|example!D8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!D8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(5,10)`
- evidence: Non-trivial numeric literal(s) found: 5, 10.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!D9, example!D10, example!D11, example!D12.
- cached value: 6; row labels: ["'Egg'"]; column header: "'INAM'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | B8: 'Egg' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 18 | B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 1 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 15 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 3 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 19

### `30faaaeef9ee|LITERAL_CONSTANT|RESULTS1!S3`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!S3`  severity: Medium  confidence: Review
- formula: `=TRIMMEAN(IF(Table1[MAX GAIN]>=6,Table1[POINTS G/L]),10%)`
- evidence: Non-trivial numeric literal(s) found: 6.
- cached value: 5.89777777777778; row labels: ["'All-TIME'"]; column header: "'>= 6'"; used range: A1:W67
- neighbourhood: Q2: '>= 4' | R2: '>= 5' | S2: '>= 6' | T2: '>= 7' | U2: '>= 8' | Q3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=4,Table1[POINTS G/L]),10%) {array Q3}' -> 4.779375 | R3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=5,Table1[POINTS G/L]),10%) {array R3}' -> 5.20833333333333 | S3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=6,Table1[POINTS G/L]),10%) {array S3}' -> 5.89777777777778 | T3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=7,Table1[POINTS G/L]),10%) {array T3}' -> 7.165 | U3: '=TRIMMEAN(IF(Table1[MAX GAIN]>=8,Table1[POINTS G/L]),10%) {array U3}' -> 9.11 | Q4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF((Table1[WEEK]>=MAX(Tab... -> 4.779375 | R4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.20833333333333 | S4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.89777777777778 | T4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 7.165 | U4: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 9.11 | Q5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=4,IF((Table1[WEEK]>=MAX(Tab... -> 4.646 | R5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=5,IF((Table1[WEEK]>=MAX(Tab... -> 5.22571428571429 | S5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=6,IF((Table1[WEEK]>=MAX(Tab... -> 5.83833333333333 | T5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=7,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333 | U5: '=IFERROR(TRIMMEAN(IF(Table1[MAX GAIN]>=8,IF((Table1[WEEK]>=MAX(Tab... -> 8.31333333333333

### `1ee00a60f590|LITERAL_CONSTANT|Sheet1!Y22`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!Y22`  severity: Medium  confidence: Review
- formula: `=IF(AND(I20>=12,G22>0),SUM(ROUNDDOWN(SUM(200-J20)*0.9,0)*3)+X22,"0")`
- evidence: Non-trivial numeric literal(s) found: 200, 0.9, 3.
- evidence: The same relative formula appears in 2 cells on this sheet; the others are Sheet1!Y317.
- cached value: '0'; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: W20: '=IF(AND(I19>=12,G20>0),ROUNDDOWN(SUM(200-J19)*0.9,0)+V20,"0")' -> '0' | X20: '=SUM(G20)' -> 0 | Y20: '=IF(AND(I19>=12,G20>0),SUM(ROUNDDOWN(SUM(200-J19)*0.9,0)*3)+X20,"0")' -> '0' | AA20: 'High Scratch Series #3' | W21: '=IF(AND(I20>=12,G21>0),ROUNDDOWN(SUM(200-J20)*0.9,0)+V21,"0")' -> '0' | X21: '=SUM(G21)' -> 0 | AA21: 'High Scratch Series #4' | W22: '=IF(AND(I21>=12,G22>0),ROUNDDOWN(SUM(200-J21)*0.9,0)+V22,"0")' -> '0' | X22: '=SUM(G22)' -> 0 | Y22: '=IF(AND(I20>=12,G22>0),SUM(ROUNDDOWN(SUM(200-J20)*0.9,0)*3)+X22,"0")' -> '0' | AA22: 'High Scratch Series #6' | X23: '=SUM(G23)' -> 0 | Z23: '=CONCATENATE(A23," ",B23," ")' -> 'BB BA' | AA23: 'High Scratch Series #7' | W24: '=IF(AND(I23>=12,G24>0),ROUNDDOWN(SUM(200-J23)*0.9,0)+V24,"0")' -> '0' | X24: '=SUM(G24)' -> 377 | Y24: '=IF(AND(I23>=12,G24>0),SUM(ROUNDDOWN(SUM(200-J23)*0.9,0)*3)+X24,"0")' -> '0' | AA24: 'High Scratch Series #8'

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!V30`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!V30`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000")/COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Points % /s (Net)'", "'1B <'"]; column header: ''; used range: A1:W67
- neighbourhood: T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> 0.8125 | T32: '10-20M' | U32: '20-50M' | V32: '50-100M' | W32: '100M <'

### `30faaaeef9ee|LITERAL_CONSTANT|RESULTS1!W22`

- workbook: `all_data_912_v0.1/spreadsheet/50442/3_50442_input.xlsx`
- location: `RESULTS 1!W22`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">100000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">100000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: U20: '20-50M' | V20: '50-100M' | W20: '100M <' | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> 13.189375

### `7149679332c0|LITERAL_CONSTANT|RESULTS1!S29`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!S29`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,COUNTIFS(Table1[POINTS G/L],">0",Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")/COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Points /s (Net)'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: Q27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U30: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `125be9ba2e04|LITERAL_CONSTANT|RESULTS1!T20`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!T20`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,COUNTIFS(Table1[POINTS],">0",Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")/COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'ATI'", "'< 100M'"]; column header: "'5-10M'"; used range: A1:X80
- neighbourhood: R19: '1-3M' | S19: '3-5M' | T19: '5-10M' | U19: '10-20M' | V19: '20-50M' | R20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V20: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B27`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B27`  severity: Medium  confidence: Review
- formula: `=Days+36+DATE(Calendar2Year,Calendar2MonthOption,1)-WEEKDAY(DATE(Calendar2Year,Calendar2MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 36.
- cached value: 2020-06-01 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B25: '=Days+29+DATE(Calendar2Year,Calendar2MonthOption,1)-WEEKDAY(DATE(C... -> 2020-05-25 00:00:00 | C25: 2020-05-26 00:00:00 | D25: 2020-05-27 00:00:00 | B27: '=Days+36+DATE(Calendar2Year,Calendar2MonthOption,1)-WEEKDAY(DATE(C... -> 2020-06-01 00:00:00 | C27: 2020-06-02 00:00:00 | D27: 'Notes:' | B29: '=YEAR(DATE(Calendar2Year,Calendar2MonthOption+1,1))' -> 2020 | C29: '=TEXT(DATE(Calendar2Year,Calendar2MonthOption+1,1),"mmmm")' -> 'June'

### `125be9ba2e04|LITERAL_CONSTANT|RESULTS1!T29`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!T29`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[POINTS],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Wins'", "'1B <'"]; column header: ''; used range: A1:X80
- neighbourhood: R27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `95fdf876027b|LITERAL_CONSTANT|RESULTS1!V28`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!V28`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")>=10,AVERAGEIFS(Table1[POINTS],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'Trades'", "'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: T26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | X27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `d2a515f35dce|LITERAL_CONSTANT|Schedule!B11`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Schedule!B11`  severity: Medium  confidence: Review
- formula: `=IFERROR(MATCH(E3,Cont_Name,0)+3,"")`
- evidence: Non-trivial numeric literal(s) found: 3.
- cached value: 4; row labels: ["'Cont. Name Row'"]; column header: ''; used range: A1:V78
- neighbourhood: A9: 'Appt. ID Row' | B9: '=IFERROR(MATCH(B8,Appt_ID,0)+3,"")' -> 4 | D9: 'Status' | A10: 'Next Appt. ID' | B10: '=IFERROR(MAX(Appt_ID)+1,1)' -> 13 | D10: 'Job #' | A11: 'Cont. Name Row' | B11: '=IFERROR(MATCH(E3,Cont_Name,0)+3,"")' -> 4 | A12: 'Sel. Cont ID' | B12: 1 | A13: 'Sel. Cont Row' | B13: '=IFERROR(MATCH(B12,Cont_ID,0)+3,"")' -> 4 | D13: 'Name'

### `ecefab75d6ce|LITERAL_CONSTANT|Calendar!B123`

- workbook: `all_data_912_v0.1/spreadsheet/57716/1_57716_input.xlsx`
- location: `Calendar!B123`  severity: Medium  confidence: Review
- formula: `=Days+29+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(Calendar9Year,Calendar9MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 29.
- cached value: 2020-12-28 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B121: '=Days+22+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-21 00:00:00 | C121: 2020-12-22 00:00:00 | D121: 2020-12-23 00:00:00 | B123: '=Days+29+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2020-12-28 00:00:00 | C123: 2020-12-29 00:00:00 | D123: 2020-12-30 00:00:00 | B125: '=Days+36+DATE(Calendar9Year,Calendar9MonthOption,1)-WEEKDAY(DATE(C... -> 2021-01-04 00:00:00 | C125: 2021-01-05 00:00:00 | D125: 'Notes:'

### `36080f34a91e|LITERAL_CONSTANT|Calendar!B165`

- workbook: `all_data_912_v0.1/spreadsheet/57716/2_57716_input.xlsx`
- location: `Calendar!B165`  severity: Medium  confidence: Review
- formula: `=Days+29+DATE(Calendar12Year,Calendar12MonthOption,1)-WEEKDAY(DATE(Calendar12Year,Calendar12MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 29.
- cached value: 2021-03-29 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B163: '=Days+22+DATE(Calendar12Year,Calendar12MonthOption,1)-WEEKDAY(DATE... -> 2021-03-22 00:00:00 | C163: 2021-03-23 00:00:00 | D163: 2021-03-24 00:00:00 | B165: '=Days+29+DATE(Calendar12Year,Calendar12MonthOption,1)-WEEKDAY(DATE... -> 2021-03-29 00:00:00 | C165: 2021-03-30 00:00:00 | D165: 2021-03-31 00:00:00 | B167: '=Days+36+DATE(Calendar12Year,Calendar12MonthOption,1)-WEEKDAY(DATE... -> 2021-04-05 00:00:00 | C167: 2021-04-06 00:00:00 | D167: 'Notes:'

### `a3ba2c45816f|LITERAL_CONSTANT|Calendar!B133`

- workbook: `all_data_912_v0.1/spreadsheet/57716/3_57716_input.xlsx`
- location: `Calendar!B133`  severity: Medium  confidence: Review
- formula: `=Days+15+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE(Calendar10Year,Calendar10MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 15.
- cached value: 2021-01-11 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B131: '=Days+8+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE(... -> 2021-01-04 00:00:00 | C131: 2021-01-05 00:00:00 | D131: 2021-01-06 00:00:00 | B133: '=Days+15+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE... -> 2021-01-11 00:00:00 | C133: 2021-01-12 00:00:00 | D133: 2021-01-13 00:00:00 | B135: '=Days+22+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE... -> 2021-01-18 00:00:00 | C135: 2021-01-19 00:00:00 | D135: 2021-01-20 00:00:00

### `95fdf876027b|LITERAL_CONSTANT|RESULTS1!W23`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!W23`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000")>=10,COUNTIFS(Table1[POINTS],">0",Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000")/COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">50000000",Table1[FLOAT],"<=100000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'GAIN/LOSS'", "'1B <'"]; column header: ''; used range: A1:X80
- neighbourhood: U21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | X21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U25: '10-20M' | V25: '20-50M' | W25: '50-100M' | X25: '100M <'

### `f97f2feedd64|LITERAL_CONSTANT|RESULTS1!R22`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!R22`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: P20: 'ENTRY' | Q20: '1-3M' | R20: '3-5M' | S20: '5-10M' | T20: '10-20M' | P21: '< 100M' | Q21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T21: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | P22: '100-500M' | Q22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T22: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P23: '500M-1B' | Q23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T23: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P24: '1B <' | Q24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T24: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `da1e266217a2|LITERAL_CONSTANT|Sheet1!Y7`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/1_CF_6540_input.xlsx`
- location: `Sheet1!Y7`  severity: Medium  confidence: Review
- formula: `=V7*1.5`
- evidence: Non-trivial numeric literal(s) found: 1.5.
- evidence: The same relative formula appears in 191 cells on this sheet; the others are Sheet1!BI7, Sheet1!CC7, Sheet1!Y8, Sheet1!BI8, Sheet1!CC8, Sheet1!Y9, Sheet1!BI9, Sheet1!CC9, and 182 more.
- cached value: 52.5; row labels: ["'Site Manager '"]; column header: "'Bank Holiday'"; used range: A1:CL123
- neighbourhood: W5: 'Midweek Nights                      ... | X5: 'Weekend' | Y5: 'Bank Holiday' | Z5: 'Midweek Days 0600 - 1800' | AA5: 'Midweek Nights                      ... | Z6: ' ' | W7: '=V7*1.1' -> 38.5 | X7: '=V7*1.2' -> 42 | Y7: '=V7*1.5' -> 52.5 | Z7: 37.708499999999994 | AA7: 42.354499999999994 | W8: '=V8*1.1' -> 30.800000000000004 | X8: '=V8*1.2' -> 33.6 | Y8: '=V8*1.5' -> 42 | Z8: 26.45 | AA8: 29.9 | W9: '=V9*1.1' -> 27.500000000000004 | X9: '=V9*1.2' -> 30 | Y9: '=V9*1.5' -> 37.5 | Z9: 22.424999999999997 | AA9: 22.424999999999997

### `b298ecd55a03|LITERAL_CONSTANT|Purchases!H5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/3_CF_3712_input.xlsx`
- location: `Purchases!H5`  severity: Medium  confidence: Review
- formula: `=IF(ISBLANK(G5), "", G5 + 14)`
- evidence: Non-trivial numeric literal(s) found: 14.
- cached value: 2024-09-09 00:00:00; row labels: ["'Pasjeshouder'", "'Overig'"]; column header: ''; used range: A1:M441
- neighbourhood: F3: '=(C3*E3)+D3' -> 127 | G3: 2024-05-24 00:00:00 | H3: '=IF(ISBLANK(G3), "", G3 + 30)' -> 2024-06-23 00:00:00 | I3: 'BIOP003' | J3: 'Microbes' | F4: '=(C4*E4)+D4' -> 127 | G4: 2024-02-27 00:00:00 | H4: '=IF(ISBLANK(G4), "", G4 + 30)' -> 2024-03-28 00:00:00 | I4: 'BIOP002' | J4: 'Plasmids' | F5: '=(C5*E5)+D5' -> 29.6 | G5: 2024-08-26 00:00:00 | H5: '=IF(ISBLANK(G5), "", G5 + 14)' -> 2024-09-09 00:00:00 | I5: 'BIOP001' | J5: 'Office' | F6: '=(C6*E6)+D6' -> 0 | H6: '=IF(ISBLANK(G6), "", G6 + 30)' -> None | F7: '=(C7*E7)+D7' -> 0 | H7: '=IF(ISBLANK(G7), "", G7 + 30)' -> None

### `5cd8c4fe9805|LITERAL_CONSTANT|RESULTS1!X16`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!X16`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">100000000")>=10,AVERAGEIFS(Table1[ENTRY],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">100000000"),""),0)`
- evidence: Non-trivial numeric literal(s) found: 10.
- cached value: None; row labels: ["'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: V14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X14: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | X15: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X16: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X17: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `19dfd5dbcec5|LITERAL_CONSTANT|formamspnc(7)!EC6`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!EC6`  severity: Medium  confidence: Review
- formula: `=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($BJ6:$BU6<>"")*($BK6:$BV6<>"")*($BK6:$BV6=$BJ6:$BU6),COLUMN($BJ6:$BU6)),IF(($BJ6:$BU6="")+($BK6:$BV6="")+($BK6:$BV6<>$BJ6:$BU6),COLUMN($BJ6:$BU6))),"[=0]-1;#"),{1,2})*{10,1}),{0,20,22,30,32,40},{0,5,3,4,2,1})`
- evidence: Non-trivial numeric literal(s) found: 10, 20, 22, 32, 40, 5, 3.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are formamspnc (7)!EC7, formamspnc (7)!EC8, formamspnc (7)!EC9, formamspnc (7)!EC10, formamspnc (7)!EC11.
- cached value: 3; row labels: ["'13c/15c/18c/21c/23c/25c/33c/35c/39c/44c/49c/51c/55c/59c/..."]; column header: "'pairs'"; used range: A1:ED48610
- range $BJ6:$BU6: values ['0', '0', '-1', '0', '2', '-3', '0', '1', '-2', '0', '0', '-1']; beyond: {'left': "BI6: '=IF(COUNTIF(AT6:BF6,0)>3,COUNTIF(AT6...", 'right': 'BV6: \'=IF(IF(ISBLANK(AD$1),"",-1*(LOOKUP(1...'}
- neighbourhood: EA6: '=IF(OR(AQ6=1,AQ6=0,AQ6=-1),1,"")' -> 1 | EB6: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($AE6:$AP6<>"... -> 3 | EC6: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($BJ6:$BU6<>"... -> 3 | EA7: '=IF(OR(AQ7=1,AQ7=0,AQ7=-1),1,"")' -> 1 | EB7: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($AE7:$AP7<>"... -> 5 | EC7: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($BJ7:$BU7<>"... -> 3 | EA8: '=IF(OR(AQ8=1,AQ8=0,AQ8=-1),1,"")' -> None | EB8: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($AE8:$AP8<>"... -> 0 | EC8: '=LOOKUP(SUM(_xlfn.AGGREGATE(14,6,1+TEXT(FREQUENCY(IF(($BJ8:$BU8<>"... -> 3

## LIVE_ERROR

### `be2f958d4b41|LIVE_ERROR|Sort!K68`

- workbook: `all_data_912_v0.1/spreadsheet/59932/2_59932_input.xlsx`
- location: `Sort!K68`  severity: Critical  confidence: Defect
- formula: `=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$S$12:$S$112)`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 36 cells on this sheet; the others are Sort!K69, Sort!K70, Sort!K71, Sort!K72, Sort!K73, Sort!K74, Sort!K75, Sort!K76, and 27 more.
- cached value: '#VALUE!'; row labels: ["'2011_Q1'"]; column header: ''; used range: A1:T147
- neighbourhood: I66: "=VLOOKUP($B66,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 12237 | J66: "=VLOOKUP($B66,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 13.28 | K66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M66: '=D66*P66' -> '#VALUE!' | I67: "=VLOOKUP($B67,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 14013 | J67: "=VLOOKUP($B67,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 15.149999999999999 | K67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M67: '=D67*P67' -> '#VALUE!' | I68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 16639 | J68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 17.91 | K68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M68: '=D68*P68' -> '#VALUE!' | I69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 19552 | J69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 20.979999999999997 | K69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M69: '=D69*P69' -> '#VALUE!' | I70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 23607 | J70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 25.26 | K70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M70: '=D70*P70' -> '#VALUE!'

### `40c60acd7755|LIVE_ERROR|Sort!T12`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!T12`  severity: Critical  confidence: Defect
- formula: `=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$D$12:$D$112)`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 56 cells on this sheet; the others are Sort!T13, Sort!T14, Sort!T15, Sort!T16, Sort!T17, Sort!T18, Sort!T19, Sort!T20, and 47 more.
- cached value: '#VALUE!'; row labels: ["'1996_Q1'"]; column header: "'Equity'"; used range: A1:T147
- neighbourhood: R10: 18 | S10: 19 | T10: 20 | R11: ' Equity / Assets                    ... | S11: 'Operation Income / Interest Exp.    ... | T11: 'Equity' | R12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | T12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$D$12:$D$... -> '#VALUE!' | R13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | T13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$D$12:$D$... -> '#VALUE!' | R14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | T14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$D$12:$D$... -> '#VALUE!'

### `050df5c328bc|LIVE_ERROR|Sheet1!U4`

- workbook: `all_data_912_v0.1/spreadsheet/14240/3_14240_input.xlsx`
- location: `Sheet1!U4`  severity: Critical  confidence: Defect
- formula: `=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)`
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'Individual'", "'3M-25yrs'"]; column header: ''; used range: A1:U75
- range A4:A75: values ["'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'Individual'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'", "'2Adults'"]; beyond: {'above': "A3: '00 To 35'", 'below': 'A76: None'}
- neighbourhood: S3: 'Members' | T3: 'Sum Insured' | S4: 150000 | T4: '3M-25yrs' | U4: '=SUMPRODUCT((A4:A75=R4)*(B4:B75=S4)*C3:M3,C4:M75=T4)' -> '#VALUE!' | S5: 150000 | T5: '3M-25yrs' | U5: '=SUMPRODUCT(($A$4:$A$75=$S5)*($B$4:$B$75=U$3)*($C$3:$P$3=$T5),$C$4... -> 0 | S6: 150000 | T6: '3M-25yrs' | U6: '=SUMPRODUCT(($A$4:$A$75=$S6)*($B$4:$B$75=U$3)*($C$3:$P$3=$T6),$C$4... -> 0

### `21865bab73e8|LIVE_ERROR|Sheet1!B8`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `Sheet1!B8`  severity: Critical  confidence: Defect
- formula: `=RANK(A8,$A$1:$A$2998,0)+COUNTIF($A$1:A8,A8)-1`
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'-'"]; column header: ''; used range: A1:D8
- range $A$1:$A$2998: values ['10', '10', '10', '20', '30', '40', '50', "'-'", 'None', 'None', 'None', 'None']; beyond: {'below': 'A2999: None'}
- neighbourhood: A6: 40 | B6: '=RANK(A6,$A$1:$A$2998,0)+COUNTIF($A$1:A6,A6)-1' -> 2 | A7: 50 | B7: '=RANK(A7,$A$1:$A$2998,0)+COUNTIF($A$1:A7,A7)-1' -> 1 | A8: '-' | B8: '=RANK(A8,$A$1:$A$2998,0)+COUNTIF($A$1:A8,A8)-1' -> '#VALUE!'

### `d207f4db35f5|LIVE_ERROR|Sheet1!K5`

- workbook: `all_data_912_v0.1/spreadsheet/48685/3_48685_input.xlsx`
- location: `Sheet1!K5`  severity: Critical  confidence: Defect
- formula: `=IF(E5="","",E5+K3)`
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'A1'", "'PartA1'"]; column header: ''; used range: A1:K12
- neighbourhood: I3: 'Bom QtyReq' | J3: 'InStock' | K3: 'SubTotal' | K4: '=IF(E4="","",E4+K1)' -> 5:22:46 | I5: 426 | J5: 0 | K5: '=IF(E5="","",E5+K3)' -> '#VALUE!' | K6: '=IF(E6="","",E6+#REF!)' -> None | K7: '=IF(E7="","",E7+K4)' -> None

### `5d8557dfb652|LIVE_ERROR|July-KPIs!F6`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!F6`  severity: Critical  confidence: Defect
- formula: `=VLOOKUP(C1,#REF!,2,0)`
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- cached value: '#REF!'; row labels: []; column header: "'Summary'"; used range: A1:T3212
- neighbourhood: F4: 'Summary' | D5: 'Outbound' | E5: 'Total Daily' | E6: '=IFERROR(((C6*1.3)+(D6*1))/((B6)),"0")' -> '0' | F6: '=VLOOKUP(C1,#REF!,2,0)' -> '#REF!' | E7: '=IFERROR(((C7*1.3)+(D7*1))/((B7)),"0")' -> '0' | E8: '=IFERROR(((C8*1.3)+(D8*1))/((B8)),"0")' -> '0'

### `b328dd851137|LIVE_ERROR|Sheet2!A124`

- workbook: `all_data_912_v0.1/spreadsheet/36764/3_36764_input.xlsx`
- location: `Sheet2!A124`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- evidence: #N/A is typed as a value in 3 cells on this sheet; the others are Sheet2!R124, Sheet2!S124.
- cached value: '#N/A'; row labels: []; column header: "'To be actioned                                    '"; used range: A1:S362
- neighbourhood: A122: 'Fully linked                        ... | A123: 'To be actioned                      ... | A124: '#N/A' | A125: 'Fully linked                        ... | A126: 'To be actioned                      ...

### `40c60acd7755|LIVE_ERROR|Sort!K68`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!K68`  severity: Critical  confidence: Defect
- formula: `=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$S$12:$S$112)`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 36 cells on this sheet; the others are Sort!K69, Sort!K70, Sort!K71, Sort!K72, Sort!K73, Sort!K74, Sort!K75, Sort!K76, and 27 more.
- cached value: '#VALUE!'; row labels: ["'2011_Q1'"]; column header: ''; used range: A1:T147
- neighbourhood: I66: "=VLOOKUP($B66,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 12237 | J66: "=VLOOKUP($B66,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 13.28 | K66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M66: '=D66*P66' -> '#VALUE!' | I67: "=VLOOKUP($B67,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 14013 | J67: "=VLOOKUP($B67,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 15.149999999999999 | K67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M67: '=D67*P67' -> '#VALUE!' | I68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 16639 | J68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 17.91 | K68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M68: '=D68*P68' -> '#VALUE!' | I69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 19552 | J69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 20.979999999999997 | K69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M69: '=D69*P69' -> '#VALUE!' | I70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 23607 | J70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 25.26 | K70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M70: '=D70*P70' -> '#VALUE!'

### `21865bab73e8|LIVE_ERROR|RS.Food!S26`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!S26`  severity: Critical  confidence: Defect
- formula: `=INDEX($A$6:$K$600,SMALL(IF(COUNTIF($S$7,$I$6:$I$600)*COUNTIF(R26,$K$6:$K$600),MATCH(ROW($A$6:$H$600),ROW($A$6:$H$600))),ROWS($A$1:A1)),COLUMNS($A$1:$A$1))`
- evidence: Cell contains #NUM!.
- evidence: The error propagates to 44 dependent cell(s): RS.Food!V8, RS.Food!W8, RS.Food!V9, RS.Food!W9, RS.Food!V10, RS.Food!W10, RS.Food!V11, RS.Food!W11, and 36 more. Fixing the source clears them.
- cached value: '#NUM!'; row labels: ["'Main'", "'Grill Salmon'"]; column header: ''; used range: A1:W607
- range $A$6:$K$600: values ["'Food'", '113209.8', '0.725888575490045', "''", "''", '-292.2', '19702', '5.74610699421379', 'None', 'None', 'None', "'Breakfasts'"]; beyond: {}
- neighbourhood: R24: 17 | S24: '=INDEX($A$6:$K$600,SMALL(IF(COUNTIF($S$7,$I$6:$I$600)*COUNTIF(R24,... -> '#NUM!' | T24: '=VLOOKUP(S24,$A$6:$H$600,7,0)' -> '#NUM!' | U24: '=VLOOKUP(S24,$A$6:$H$600,2,0)' -> '#NUM!' | R25: 18 | S25: '=INDEX($A$6:$K$600,SMALL(IF(COUNTIF($S$7,$I$6:$I$600)*COUNTIF(R25,... -> '#NUM!' | T25: '=VLOOKUP(S25,$A$6:$H$600,7,0)' -> '#NUM!' | U25: '=VLOOKUP(S25,$A$6:$H$600,2,0)' -> '#NUM!' | R26: 19 | S26: '=INDEX($A$6:$K$600,SMALL(IF(COUNTIF($S$7,$I$6:$I$600)*COUNTIF(R26,... -> '#NUM!' | T26: '=VLOOKUP(S26,$A$6:$H$600,7,0)' -> '#NUM!' | U26: '=VLOOKUP(S26,$A$6:$H$600,2,0)' -> '#NUM!' | R27: 20 | S27: '=INDEX($A$6:$K$600,SMALL(IF(COUNTIF($S$7,$I$6:$I$600)*COUNTIF(R27,... -> '#NUM!' | T27: '=VLOOKUP(S27,$A$6:$H$600,7,0)' -> '#NUM!' | U27: '=VLOOKUP(S27,$A$6:$H$600,2,0)' -> '#NUM!'

### `95fdf876027b|LIVE_ERROR|RESULTS1!C34`

- workbook: `all_data_912_v0.1/spreadsheet/49613/3_49613_input.xlsx`
- location: `RESULTS 1!C34`  severity: Critical  confidence: Defect
- formula: `=COUNTIF(Table1[ENTRY ATTEMPT],"=1")/COUNT(Table1[ENTRY ATTEMPT])`
- evidence: Cell contains #DIV/0!.
- cached value: '#DIV/0!'; row labels: ["'Entry Success %'"]; column header: ''; used range: A1:X80
- neighbourhood: B32: 'Points (Wk Ave)' | C32: '=C30/($C$27/5)' -> -47.5 | B33: 'Points (Annualized)' | C33: '=(C30/C27)*(C6*C9)' -> -2251.499999999999 | B34: 'Entry Success %' | C34: '=COUNTIF(Table1[ENTRY ATTEMPT],"=1")/COUNT(Table1[ENTRY ATTEMPT])' -> '#DIV/0!' | B35: 'Negative trades' | C35: '=MAX(FREQUENCY(IF(Table1[POINTS]<0,ROW(Table1[POINTS])),IF(Table1[... -> 1 | E35: 'Greatest sequence of negative trades' | B36: 'Ave neg trades' | C36: '=AVERAGE(IFERROR(1/(1/FREQUENCY(IF(Table1[POINTS]<0,ROW(Table1[POI... -> 1 | E36: 'Average sequence of negative trades'

### `970db979d624|LIVE_ERROR|Sheet1!Q6`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `Sheet1!Q6`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: #VALUE! is typed as a value in 3 cells on this sheet; the others are Sheet1!Q7, Sheet1!Q8.
- cached value: '#VALUE!'; row labels: ["''", "''"]; column header: "''"; used range: A1:BI8
- neighbourhood: O4: 'A' | P4: '' | Q4: '' | R4: 12 | S4: 14 | O5: '' | P5: '' | Q5: '' | R5: 12 | S5: 16 | O6: '' | P6: '' | Q6: '#VALUE!' | R6: 14 | S6: 21 | O7: 'A' | P7: '' | Q7: '#VALUE!' | R7: 14 | S7: 19 | O8: 'A' | P8: '' | Q8: '#VALUE!' | R8: 13 | S8: 18

### `f98021ebb2e8|LIVE_ERROR|master!E2`

- workbook: `all_data_912_v0.1/spreadsheet/47933/2_47933_input.xlsx`
- location: `master!E2`  severity: Critical  confidence: Defect
- formula: `=IF(B2<37.5,"2",)*IF(B2>37.5,"D2,1.5,")`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 99 cells on this sheet; the others are master!E5, master!E8, master!E9, master!E10, master!E11, master!E12, master!E13, master!E16, and 90 more.
- cached value: '#VALUE!'; row labels: []; column header: "'Sum'"; used range: A1:E154
- neighbourhood: C1: 'Amount' | D1: 'Rate' | E1: 'Sum' | C2: '=INDEX(amount!A:A,MATCH(A2,amount!B:B,0))' -> 25881.1959248275 | D2: '=ROUND(C2/52/B2,2)' -> 11.71 | E2: '=IF(B2<37.5,"2",)*IF(B2>37.5,"D2,1.5,")' -> '#VALUE!' | C3: '=INDEX(amount!A:A,MATCH(A3,amount!B:B,0))' -> 60411.6208405792 | D3: '=ROUND(C3/52/B3,2)' -> 30.98 | E3: '=IF(B3<37.5,"2",)*IF(B3>37.5,"D2,1.5,")' -> 0 | C4: '=INDEX(amount!A:A,MATCH(A4,amount!B:B,0))' -> 57005.1701444134 | D4: '=ROUND(C4/52/B4,2)' -> 31.32 | E4: '=IF(B4<37.5,"2",)*IF(B4>37.5,"D2,1.5,")' -> 0

### `e3281236e4b3|LIVE_ERROR|results!U95`

- workbook: `all_data_912_v0.1/spreadsheet/54490/2_54490_input.xlsx`
- location: `results!U95`  severity: Critical  confidence: Defect
- formula: `=AVERAGEIFS(U$3:U$92,$B$3:$B$92,$B95,U$3:U$92,"<>0")`
- evidence: Cell contains #DIV/0!.
- evidence: The same relative formula evaluates to #DIV/0! in 7 cells on this sheet; the others are results!V95, results!T96, results!U96, results!X96, results!U97, results!V97.
- evidence: The error propagates to 4 dependent cell(s): results!T98, results!U98, results!V98, results!X98. Fixing the source clears them.
- cached value: '#DIV/0!'; row labels: ["'Night'"]; column header: ''; used range: A1:Z98
- range U$3:U$92: values ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']; beyond: {'above': "U2: 'RM48 WOB - Manual Machine 2 (SM)'", 'below': 'U93: None'}
- neighbourhood: S95: '=AVERAGEIFS(S$3:S$92,$B$3:$B$92,$B95,S$3:S$92,"<>0")' -> 241.937765937766 | T95: '=AVERAGEIFS(T$3:T$92,$B$3:$B$92,$B95,T$3:T$92,"<>0")' -> 148.8 | U95: '=AVERAGEIFS(U$3:U$92,$B$3:$B$92,$B95,U$3:U$92,"<>0")' -> '#DIV/0!' | V95: '=AVERAGEIFS(V$3:V$92,$B$3:$B$92,$B95,V$3:V$92,"<>0")' -> '#DIV/0!' | W95: '=AVERAGEIFS(W$3:W$92,$B$3:$B$92,$B95,W$3:W$92,"<>0")' -> 216.782852564102 | S96: '=AVERAGEIFS(S$3:S$92,$B$3:$B$92,$B96,S$3:S$92,"<>0")' -> 157.916666666667 | T96: '=AVERAGEIFS(T$3:T$92,$B$3:$B$92,$B96,T$3:T$92,"<>0")' -> '#DIV/0!' | U96: '=AVERAGEIFS(U$3:U$92,$B$3:$B$92,$B96,U$3:U$92,"<>0")' -> '#DIV/0!' | V96: '=AVERAGEIFS(V$3:V$92,$B$3:$B$92,$B96,V$3:V$92,"<>0")' -> 317.511105915361 | W96: '=AVERAGEIFS(W$3:W$92,$B$3:$B$92,$B96,W$3:W$92,"<>0")' -> 241.950161778164 | S97: '=AVERAGEIFS(S$3:S$92,$B$3:$B$92,$B97,S$3:S$92,"<>0")' -> 241.937765937766 | T97: '=AVERAGEIFS(T$3:T$92,$B$3:$B$92,$B97,T$3:T$92,"<>0")' -> 148.8 | U97: '=AVERAGEIFS(U$3:U$92,$B$3:$B$92,$B97,U$3:U$92,"<>0")' -> '#DIV/0!' | V97: '=AVERAGEIFS(V$3:V$92,$B$3:$B$92,$B97,V$3:V$92,"<>0")' -> '#DIV/0!' | W97: '=AVERAGEIFS(W$3:W$92,$B$3:$B$92,$B97,W$3:W$92,"<>0")' -> 216.782852564102

### `1e354abd5c10|LIVE_ERROR|Sheet1!C10`

- workbook: `all_data_912_v0.1/spreadsheet/165-23/1_165-23_input.xlsx`
- location: `Sheet1!C10`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- evidence: #N/A is typed as a value in 8 cells on this sheet; the others are Sheet1!D10, Sheet1!C11, Sheet1!D11, Sheet1!C19, Sheet1!D19, Sheet1!C20, Sheet1!D20.
- cached value: '#N/A'; row labels: ["'Singapore Cup'"]; column header: "'UEFA'"; used range: A1:N73
- neighbourhood: A8: 7 | B8: 'UEFA Conference League' | C8: 'UEFA' | D8: 'Conference League' | E8: 2022-10-27 00:00:00 | A9: 8 | B9: 'UEFA Conference League' | C9: 'UEFA' | D9: 'Conference League' | E9: 2022-10-27 00:00:00 | A10: 9 | B10: 'Singapore Cup' | C10: '#N/A' | D10: '#N/A' | E10: 2022-10-27 00:00:00 | A11: 10 | B11: 'Singapore Cup' | C11: '#N/A' | D11: '#N/A' | E11: 2022-10-27 00:00:00 | A12: 11 | B12: 'Germany. Bundesliga' | C12: 'Germany' | D12: 'Bundesliga' | E12: 2022-10-28 00:00:00

### `b0189d43ef5f|LIVE_ERROR|DATABASECountries!J4`

- workbook: `all_data_912_v0.1/spreadsheet/37462/2_37462_input.xlsx`
- location: `DATABASE Countries!J4`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'Afghanistan'", "'TOP 1'"]; column header: ''; used range: A1:J244
- neighbourhood: H4: 'TOP 1' | I4: '=_xlfn.SORTBY(E4:F244,F4:F244,-1) {array I4:J244}' -> 'Afghanistan' | J4: '#VALUE!' | H5: 'TOP 2' | I5: 'India' | J5: 236681.49 | H6: 'TOP 3' | I6: 'United Kingdom' | J6: 5489.16

### `7cc6b0fe1206|LIVE_ERROR|Sort!Q68`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!Q68`  severity: Critical  confidence: Defect
- formula: `=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$BB$12:$BB$112)`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 36 cells on this sheet; the others are Sort!Q69, Sort!Q70, Sort!Q71, Sort!Q72, Sort!Q73, Sort!Q74, Sort!Q75, Sort!Q76, and 27 more.
- cached value: '#VALUE!'; row labels: ["'2011_Q1'"]; column header: ''; used range: A1:T147
- neighbourhood: O66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$K$12:$K$... -> '#VALUE!' | P66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$F$12:$F$... -> '#VALUE!' | Q66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$BB$12:$B... -> '#VALUE!' | R66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S66: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A66,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | O67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$K$12:$K$... -> '#VALUE!' | P67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$F$12:$F$... -> '#VALUE!' | Q67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$BB$12:$B... -> '#VALUE!' | R67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S67: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A67,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | O68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$K$12:$K$... -> '#VALUE!' | P68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$F$12:$F$... -> '#VALUE!' | Q68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$BB$12:$B... -> '#VALUE!' | R68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$BC$12:$B... -> '#VALUE!' | S68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$BD$12:$B... -> '#VALUE!' | O69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$K$12:$K$... -> '#VALUE!' | P69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$F$12:$F$... -> '#VALUE!' | Q69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$BB$12:$B... -> '#VALUE!' | R69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$BC$12:$B... -> '#VALUE!' | S69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$BD$12:$B... -> '#VALUE!' | O70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$K$12:$K$... -> '#VALUE!' | P70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$F$12:$F$... -> '#VALUE!' | Q70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$BB$12:$B... -> '#VALUE!' | R70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$BC$12:$B... -> '#VALUE!' | S70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$BD$12:$B... -> '#VALUE!'

### `29e8f5fbc26c|LIVE_ERROR|Result!J1`

- workbook: `all_data_912_v0.1/spreadsheet/55085/2_55085_input.xlsx`
- location: `Result!J1`  severity: Critical  confidence: Defect
- formula: `=#REF!`
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The same relative formula evaluates to #REF! in 2 cells on this sheet; the others are Result!L1.
- evidence: The error propagates to 1 dependent cell(s): Result!K1. Fixing the source clears them.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:L13
- neighbourhood: J1: '=#REF!' -> '#REF!' | K1: '=J1' -> '#REF!' | L1: '=#REF!' -> '#REF!' | H2: 'Mango' | I2: 'Banana' | J2: 'Apple' | K2: 'Mango' | L2: 'Banana' | H3: '=G3' -> 'Shrawan' | I3: '=H3' -> 'Shrawan' | J3: 'Bhadra' | K3: '=J3' -> 'Bhadra' | L3: '=K3' -> 'Bhadra'

### `970db979d624|LIVE_ERROR|formamspnc(7)!BI3`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!BI3`  severity: Critical  confidence: Defect
- formula: `=LARGE(IF(AD5:AD11>0,BI5:BI11),3)`
- evidence: Cell contains #NUM!.
- cached value: '#NUM!'; row labels: ["'m2'", "'m3'"]; column header: ''; used range: A1:ED48610
- range AD5:AD11: values ['None', '55', '59', '60', '68', '70', '69']; beyond: {'above': 'AD4: None', 'below': 'AD12: None'}
- neighbourhood: BJ1: 'patt analysis prime patt versus all' | BJ2: 1 | BK2: 2 | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BH3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),2) {array BH3}' -> '#NUM!' | BI3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),3) {array BI3}' -> '#NUM!' | BJ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(R5:AD5,R$1+{1,0,-1}),{1,0,-1}),"")... -> None | BK5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:AE5,S$1+{1,0,-1}),{1,0,-1}),"")... -> None

### `7cc6b0fe1206|LIVE_ERROR|Sort!Q12`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!Q12`  severity: Critical  confidence: Defect
- formula: `=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BB$12:$BB$112)`
- evidence: Cell contains #VALUE!.
- evidence: The same relative formula evaluates to #VALUE! in 56 cells on this sheet; the others are Sort!Q13, Sort!Q14, Sort!Q15, Sort!Q16, Sort!Q17, Sort!Q18, Sort!Q19, Sort!Q20, and 47 more.
- cached value: '#VALUE!'; row labels: ["'1997_Q1'"]; column header: "' Equity / Assets                                        ..."; used range: A1:T147
- neighbourhood: O10: 15 | P10: 16 | Q10: 17 | R10: 18 | S10: 19 | O11: 'Current Ratio "CA/CL"' | P11: 'Share Out. ' | Q11: ' Equity / Assets                    ... | R11: ' Equity / Assets                    ... | S11: 'Operation Income / Interest Exp.    ... | O12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$K$12:$K$... -> '#VALUE!' | P12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$F$12:$F$... -> '#VALUE!' | Q12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BB$12:$B... -> '#VALUE!' | R12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S12: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A12,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | O13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$K$12:$K$... -> '#VALUE!' | P13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$F$12:$F$... -> '#VALUE!' | Q13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$BB$12:$B... -> '#VALUE!' | R13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S13: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A13,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!' | O14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$K$12:$K$... -> '#VALUE!' | P14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$F$12:$F$... -> '#VALUE!' | Q14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$BB$12:$B... -> '#VALUE!' | R14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$BC$12:$B... -> '#VALUE!' | S14: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A14,'[1]<2010Cal'!$BD$12:$B... -> '#VALUE!'

### `c903fcb4672b|LIVE_ERROR|Sheet1!B8`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `Sheet1!B8`  severity: Critical  confidence: Defect
- formula: `=RANK(A8,$A$1:$A$2998,0)+COUNTIF($A$1:A8,A8)-1`
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'-'"]; column header: ''; used range: A1:D8
- range $A$1:$A$2998: values ['10', '10', '10', '20', '30', '40', '50', "'-'", 'None', 'None', 'None', 'None']; beyond: {'below': 'A2999: None'}
- neighbourhood: A6: 40 | B6: '=RANK(A6,$A$1:$A$2998,0)+COUNTIF($A$1:A6,A6)-1' -> 2 | A7: 50 | B7: '=RANK(A7,$A$1:$A$2998,0)+COUNTIF($A$1:A7,A7)-1' -> 1 | A8: '-' | B8: '=RANK(A8,$A$1:$A$2998,0)+COUNTIF($A$1:A8,A8)-1' -> '#VALUE!'

### `0c87c637e542|LIVE_ERROR|Data!AH9`

- workbook: `all_data_912_v0.1/spreadsheet/545-35/1_545-35_input.xlsx`
- location: `Data!AH9`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: #VALUE! is typed as a value in 4 cells on this sheet; the others are Data!U15, Data!AE15, Data!AE19.
- cached value: '#VALUE!'; row labels: ["'Á™‘'", "'t:í'"]; column header: "' NW'"; used range: A1:AK23
- neighbourhood: AF7: 'GaY' | AG7: '?_x0007_è' | AH7: '0\tï' | AI7: '°\\O' | AF8: '_x001C_\x7fÄ' | AG8: '_x000E_|©' | AH8: ' NW' | AI8: "'_x0004_ð" | AF9: 'Á™‘' | AG9: 't:í' | AH9: '#VALUE!' | AI9: '©0g' | AF10: 'J\xad|' | AG10: 'P©ë' | AH10: 'ÀÅu' | AI10: 'É)_x0004_' | AF11: 'ÆâV' | AG11: 'y¦×' | AH11: 'å_x0018_¼' | AI11: '”‘†'

### `f49918401273|LIVE_ERROR|Sheet1!B7`

- workbook: `all_data_912_v0.1/spreadsheet/41691/2_41691_input.xlsx`
- location: `Sheet1!B7`  severity: Critical  confidence: Defect
- formula: `=VLOOKUP(A7,A1:A5,6,FALSE)`
- evidence: Cell contains #REF!.
- cached value: '#REF!'; row labels: []; column header: "'five'"; used range: A1:B7
- range A1:A5: values ['1', '2', '3', '4', '5']; beyond: {'below': 'A6: None'}
- neighbourhood: A5: 5 | B5: 'five' | A7: 3 | B7: '=VLOOKUP(A7,A1:A5,6,FALSE)' -> '#REF!'

### `5cd8c4fe9805|LIVE_ERROR|RESULTS1!C26`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!C26`  severity: Critical  confidence: Defect
- formula: `=C30/SUMIF(Table1[POINTS],">=0",Table1[POINTS])`
- evidence: Cell contains #DIV/0!.
- cached value: '#DIV/0!'; row labels: ["'Profit %'"]; column header: ''; used range: A1:X80
- neighbourhood: C24: 'All-time' | D24: 'Last 3 Wk' | E24: '> 1 pt' | B25: 'Win %' | C25: '=C29/C28' -> 0 | D25: '=AVERAGEIFS(Table2[WIN %],Table2[WEEK],">="&MAX(Table2[WEEK])-2)' -> 0 | B26: 'Profit %' | C26: '=C30/SUMIF(Table1[POINTS],">=0",Table1[POINTS])' -> '#DIV/0!' | B27: 'Days (Traded)' | C27: '=SUMPRODUCT((Table1[DATE]<>"")/COUNTIF(Table1[DATE],Table1[DATE]&"... -> 3 | B28: 'Trades' | C28: '=COUNTIF(Table1[POINTS],"<>0")' -> 3

### `4d98025351b4|LIVE_ERROR|DesiredSheet1afterdelrow2!C2`

- workbook: `all_data_912_v0.1/spreadsheet/165-23/3_165-23_input.xlsx`
- location: `Desired Sheet1 after delrow2!C2`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- evidence: #N/A is typed as a value in 8 cells on this sheet; the others are Desired Sheet1 after delrow2!D2, Desired Sheet1 after delrow2!C3, Desired Sheet1 after delrow2!D3, Desired Sheet1 after delrow2!C4, Desired Sheet1 after delrow2!D4, Desired Sheet1 after delrow2!C5, Desired Sheet1 after delrow2!D5.
- cached value: '#N/A'; row labels: ["'Singapore Cup'"]; column header: ''; used range: A1:N5
- neighbourhood: A2: 9 | B2: 'Singapore Cup' | C2: '#N/A' | D2: '#N/A' | E2: 2022-10-27 00:00:00 | A3: 10 | B3: 'Singapore Cup' | C3: '#N/A' | D3: '#N/A' | E3: 2022-10-27 00:00:00 | A4: 18 | B4: 'Singapore Cup' | C4: '#N/A' | D4: '#N/A' | E4: 2022-10-28 00:00:00

### `9792181a96d9|LIVE_ERROR|Exp-DB!G2`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/1_524-31_input.xlsx`
- location: `Exp-DB!G2`  severity: Critical  confidence: Defect
- formula: `=INDEX(cats,MATCH("*"&D2&"*",exDB,0))`
- evidence: Cell contains #N/A.
- evidence: The same relative formula evaluates to #N/A in 37 cells on this sheet; the others are Exp-DB!G4, Exp-DB!G5, Exp-DB!G6, Exp-DB!G7, Exp-DB!G8, Exp-DB!G9, Exp-DB!G10, Exp-DB!G11, and 28 more.
- cached value: '#N/A'; row labels: ["'amazon'", "'AMAZON.COM*1T9SS2M AMZN.COM/BILLWA'"]; column header: ''; used range: A1:G53
- neighbourhood: E1: '=VLOOKUP(D1 & "*",$A$1:$B$37,2,0)' -> 'life insurance' | G1: '=INDEX(cats,MATCH("*"&D1&"*",exDB,0))' -> 'life insurance' | E2: '=VLOOKUP(D2 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G2: '=INDEX(cats,MATCH("*"&D2&"*",exDB,0))' -> '#N/A' | E3: '=VLOOKUP(D3 & "*",$A$1:$B$37,2,0)' -> 'life insurance' | G3: '=INDEX(cats,MATCH("*"&D3&"*",exDB,0))' -> 'life insurance' | E4: '=VLOOKUP(D4 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G4: '=INDEX(cats,MATCH("*"&D4&"*",exDB,0))' -> '#N/A'

## NUMBERS_STORED_AS_TEXT

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet2!F26`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet2!F26`  severity: Medium  confidence: Review
- evidence: Cell contains text value '32131' in a column that otherwise holds 47 numbers.
- evidence: 9 numeric-looking text values sit in number column F; the others are F30 '50045', F34 '21252', F36 '23342', F42 '25334', F47 '12402003', F60 '13421', F61 '33332', F69 '35443'.
- cached value: '32131'; row labels: ["'H3'", "'3G'"]; column header: ''; used range: A1:Z168
- neighbourhood: D24: '3G' | E24: 32334 | F24: 32333 | G24: 32332 | H24: 44321 | D25: '4G' | E25: '10415013\n 15124012' | F25: 10450000 | G25: 10450002 | H25: 10450003 | D26: '3G' | E26: 21450 | F26: '32131' | G26: '32134' | H26: 34115 | D27: '4G' | E27: 102403 | F27: 122134 | G27: 113432 | H27: 113303 | D28: 'Generation' | E28: 'Serving Cells'

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet1!J11`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet1!J11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '25234' in a column that otherwise holds 10 numbers.
- evidence: 3 numeric-looking text values sit in number column J; the others are J25 '11032014', J38 '13022005'.
- cached value: '25234'; row labels: ["'11540\\n 30113'", "'12111\\n 32443'"]; column header: ''; used range: A1:J168
- neighbourhood: H11: 13424 | I11: 20352 | J11: '25234' | H13: '10311014\n 15053012'

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet1!H52`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet1!H52`  severity: Medium  confidence: Review
- evidence: Cell contains text value '34113' in a column that otherwise holds 31 numbers.
- cached value: '34113'; row labels: ["'3G'"]; column header: ''; used range: A1:J168
- neighbourhood: F51: 20214 | G51: 21111 | H51: 25443 | I51: 34301 | J51: 33005 | F52: 22323 | G52: 33025 | H52: '34113' | F53: 122314104 | G53: '134045314' | F54: 24102 | G54: 24101 | H54: 43531

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '8600000040' in a column that otherwise holds 2329 numbers.
- evidence: 458 numeric-looking text values sit in number column B; the others are B4 '8600000040', B163 '4500035436', B164 '4500035436', B165 '4500035436', B226 '4500041933', B347 '4500042190', B413 '8600000020', B414 '8600000020', and 449 more.
- cached value: '8600000040'; row labels: ["'8993'"]; column header: "'Project ID'"; used range: A1:K2802
- neighbourhood: A1: 'Serial ID' | B1: 'Project ID' | C1: 'Shipped' | A2: '8993' | B2: '8600000040' | C2: 2017-04-21 00:00:00 | A3: '8994' | B3: 8600000040 | C3: 2017-04-21 00:00:00 | A4: '8991' | B4: '8600000040' | C4: 2017-04-24 00:00:00

### `a3b766273873|NUMBERS_STORED_AS_TEXT|GLDetails!A11`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/3_601-4_input.xlsx`
- location: `GL Details!A11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '322115' in a column that otherwise holds 9 numbers.
- cached value: '322115'; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: A9: 102985 | C9: 299030 | A10: 102985 | C10: 122200 | A11: '322115' | C11: 108250

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 41 numbers.
- evidence: 5 numeric-looking text values sit in number column G; the others are G26 '32134', G43 '35325', G47 '12402004', G53 '134045314'.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: E3: 10433 | F3: 11114 | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!B163`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!B163`  severity: Medium  confidence: Review
- evidence: Cell contains text value '4500035436' in a column that otherwise holds 2331 numbers.
- evidence: 456 numeric-looking text values sit in number column B; the others are B164 '4500035436', B165 '4500035436', B226 '4500041933', B347 '4500042190', B413 '8600000020', B414 '8600000020', B415 '8600000020', B416 '8600000020', and 447 more.
- cached value: '4500035436'; row labels: ["'1236'"]; column header: ''; used range: A1:K2802
- neighbourhood: A161: 1418 | B161: 4500042460 | C161: 2018-04-04 00:00:00 | A162: '1235' | B162: 4500042230 | C162: 2018-04-04 00:00:00 | A163: '1236' | B163: '4500035436' | C163: 2018-04-04 00:00:00 | A164: '1237' | B164: '4500035436' | C164: 2018-04-04 00:00:00 | A165: '1238' | B165: '4500035436' | C165: 2018-04-04 00:00:00

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet1!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet1!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 40 numbers.
- evidence: 5 numeric-looking text values sit in number column G; the others are G26 '32134', G43 '35325', G47 '12402004', G53 '134045314'.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:J168
- neighbourhood: E3: '10433\n 52413' | F3: '11114\n 3042' | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '8993' in a column that otherwise holds 1547 numbers.
- evidence: 1240 numeric-looking text values sit in number column A; the others are A3 '8994', A4 '8991', A5 '8992', A6 '9973', A21 '2047', A22 '2048', A23 '2049', A24 '2050', and 1231 more.
- cached value: '8993'; row labels: []; column header: "'Serial ID'"; used range: A1:K2802
- neighbourhood: A1: 'Serial ID' | B1: 'Project ID' | C1: 'Shipped' | A2: '8993' | B2: '8600000040' | C2: 2017-04-21 00:00:00 | A3: '8994' | B3: 8600000040 | C3: 2017-04-21 00:00:00 | A4: '8991' | B4: '8600000040' | C4: 2017-04-24 00:00:00

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet1!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet1!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 40 numbers.
- evidence: 5 numeric-looking text values sit in number column G; the others are G26 '32134', G43 '35325', G47 '12402004', G53 '134045314'.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:J168
- neighbourhood: E3: '10433\n 52413' | F3: '11114\n 3042' | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `355d8bd13c80|NUMBERS_STORED_AS_TEXT|Sheet1!I8`

- workbook: `all_data_912_v0.1/spreadsheet/418-25/1_418-25_input.xlsx`
- location: `Sheet1!I8`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1771 ' in a column that otherwise holds 7 numbers.
- cached value: '1771 '; row labels: ["'MQ-818YEJ'", "'Purchase Ordering'"]; column header: "'2391  Sammy'"; used range: A1:I27
- neighbourhood: I6: '1791 REFUND ' | I7: '2391  Sammy' | I8: '1771 ' | I9: '1611  Sammy jonker' | I10: '2002 jW 78 WF GP'

### `c5f93923f23e|NUMBERS_STORED_AS_TEXT|GLDetails!A11`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/1_601-4_input.xlsx`
- location: `GL Details!A11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '322115' in a column that otherwise holds 9 numbers.
- cached value: '322115'; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: A9: 102985 | C9: 299030 | A10: 102985 | C10: 122200 | A11: '322115' | C11: 108250

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '8993' in a column that otherwise holds 1547 numbers.
- evidence: 1240 numeric-looking text values sit in number column A; the others are A3 '8994', A4 '8991', A5 '8992', A6 '9973', A21 '2047', A22 '2048', A23 '2049', A24 '2050', and 1231 more.
- cached value: '8993'; row labels: []; column header: "'Serial ID'"; used range: A1:K2802
- neighbourhood: A1: 'Serial ID' | B1: 'Project ID' | C1: 'Shipped' | A2: '8993' | B2: 8600000041 | C2: 2017-04-21 00:00:00 | A3: '8994' | B3: 8600000042 | C3: 2017-04-21 00:00:00 | A4: '8991' | B4: 8600000040 | C4: 2017-04-24 00:00:00

### `7e6034cae12d|NUMBERS_STORED_AS_TEXT|Sheet1!A1`

- workbook: `all_data_912_v0.1/spreadsheet/15671/2_15671_input.xlsx`
- location: `Sheet1!A1`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313316543723' in a column that otherwise holds 250 numbers.
- evidence: 19 numeric-looking text values sit in number column A; the others are A2 '913313331154233', A3 '913313331477316', A4 '913313323763536', A5 '913313323763473', A6 '913313329226819', A7 '913313343567715', A8 '913313329228226', A9 '911313318355914', and 10 more.
- cached value: '911313316543723'; row labels: []; column header: ''; used range: A1:A269
- neighbourhood: A1: '911313316543723' | A2: '913313331154233' | A3: '913313331477316'

### `ab03f9015e49|NUMBERS_STORED_AS_TEXT|GLDetails!A11`

- workbook: `all_data_912_v0.1/spreadsheet/601-4/2_601-4_input.xlsx`
- location: `GL Details!A11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '322115' in a column that otherwise holds 9 numbers.
- cached value: '322115'; row labels: []; column header: ''; used range: A1:G11
- neighbourhood: A9: 102985 | C9: 299030 | A10: 102985 | C10: 122200 | A11: '322115' | C11: 108250

### `74d1b4bee11f|NUMBERS_STORED_AS_TEXT|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/53117/1_53117_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1065414' in a column that otherwise holds 22 numbers.
- evidence: 4 numeric-looking text values sit in number column A; the others are A4 '1065414', A5 '1065414', A6 '1065414'.
- cached value: '1065414'; row labels: []; column header: ''; used range: A1:G27
- neighbourhood: A1: 'Customer' | B1: 'Total' | C1: 'Country' | A2: 1065414 | B2: 333.33 | C2: 'Japan' | A3: '1065414' | B3: -4160 | C3: 'Canada' | A4: '1065414' | B4: 4160 | C4: 'US' | A5: '1065414' | B5: 432.84 | C5: 'Canada'

### `1a12611d45b2|NUMBERS_STORED_AS_TEXT|Sheet1!A1`

- workbook: `all_data_912_v0.1/spreadsheet/15671/1_15671_input.xlsx`
- location: `Sheet1!A1`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313316543722' in a column that otherwise holds 250 numbers.
- evidence: 19 numeric-looking text values sit in number column A; the others are A2 '913313331154233', A3 '913313331477316', A4 '913313323763536', A5 '913313323763473', A6 '913313329226819', A7 '913313343567715', A8 '913313329228226', A9 '911313318355914', and 10 more.
- cached value: '911313316543722'; row labels: []; column header: ''; used range: A1:A269
- neighbourhood: A1: '911313316543722' | A2: '913313331154233' | A3: '913313331477316'

### `35eccaaedf70|NUMBERS_STORED_AS_TEXT|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/53117/2_53117_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1065414' in a column that otherwise holds 22 numbers.
- evidence: 4 numeric-looking text values sit in number column A; the others are A4 '1065414', A5 '1065414', A6 '1065414'.
- cached value: '1065414'; row labels: []; column header: ''; used range: A1:G27
- neighbourhood: A1: 'Customer' | B1: 'Total' | C1: 'Country' | A2: 1065414 | B2: 333.33 | C2: 'US' | A3: '1065414' | B3: -4160 | C3: 'Canada' | A4: '1065414' | B4: 4160 | C4: 'US' | A5: '1065414' | B5: 432.84 | C5: 'Canada'

### `f8daf4406797|NUMBERS_STORED_AS_TEXT|Sheet2!E2`

- workbook: `all_data_912_v0.1/spreadsheet/453-49/1_453-49_input.xlsx`
- location: `Sheet2!E2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '7460118' in a column that otherwise holds 5 numbers.
- cached value: '7460118'; row labels: ["'PPL2122075'"]; column header: "'Batch'"; used range: A1:M7
- neighbourhood: C1: 'SLoc' | D1: 'S' | E1: 'Batch' | F1: 'S' | G1: 'Special Stock Number' | E2: '7460118' | E3: 7460987 | E4: 1234567

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '8993' in a column that otherwise holds 1547 numbers.
- evidence: 1240 numeric-looking text values sit in number column A; the others are A3 '8994', A4 '8991', A5 '8992', A6 '9973', A21 '2047', A22 '2048', A23 '2049', A24 '2050', and 1231 more.
- cached value: '8993'; row labels: []; column header: "'Serial ID'"; used range: A1:K2802
- neighbourhood: A1: 'Serial ID' | B1: 'Project ID' | C1: 'Shipped' | A2: '8993' | B2: 8600000041 | C2: 2017-04-21 00:00:00 | A3: '8994' | B3: 8600000040 | C3: 2017-04-21 00:00:00 | A4: '8991' | B4: '8600000040' | C4: 2017-04-24 00:00:00

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!B4`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!B4`  severity: Medium  confidence: Review
- evidence: Cell contains text value '8600000040' in a column that otherwise holds 2330 numbers.
- evidence: 457 numeric-looking text values sit in number column B; the others are B163 '4500035436', B164 '4500035436', B165 '4500035436', B226 '4500041933', B347 '4500042190', B413 '8600000020', B414 '8600000020', B415 '8600000020', and 448 more.
- cached value: '8600000040'; row labels: ["'8991'"]; column header: ''; used range: A1:K2802
- neighbourhood: A2: '8993' | B2: 8600000041 | C2: 2017-04-21 00:00:00 | A3: '8994' | B3: 8600000040 | C3: 2017-04-21 00:00:00 | A4: '8991' | B4: '8600000040' | C4: 2017-04-24 00:00:00 | A5: '8992' | B5: 8600000040 | C5: 2017-04-24 00:00:00 | A6: '9973' | B6: 1500006150 | C6: 2017-06-24 00:00:00

### `9ea22c621bf1|NUMBERS_STORED_AS_TEXT|Sheet1!A1`

- workbook: `all_data_912_v0.1/spreadsheet/15671/3_15671_input.xlsx`
- location: `Sheet1!A1`  severity: Medium  confidence: Review
- evidence: Cell contains text value '911313316543722' in a column that otherwise holds 250 numbers.
- evidence: 19 numeric-looking text values sit in number column A; the others are A2 '913313331154234', A3 '913313331477314', A4 '913313323763534', A5 '913313323763473', A6 '913313329226819', A7 '913313343567715', A8 '913313329228226', A9 '911313318355914', and 10 more.
- cached value: '911313316543722'; row labels: []; column header: ''; used range: A1:A269
- neighbourhood: A1: '911313316543722' | A2: '913313331154234' | A3: '913313331477314'

### `8985b82c7663|NUMBERS_STORED_AS_TEXT|Sheet1!C1`

- workbook: `all_data_912_v0.1/spreadsheet/94-28/3_94-28_input.xlsx`
- location: `Sheet1!C1`  severity: Medium  confidence: Review
- evidence: Cell contains text value '\xa087682.95' in a column that otherwise holds 3 numbers.
- cached value: '\xa087682.95'; row labels: []; column header: ''; used range: A1:C4
- neighbourhood: C1: '\xa087682.95' | C2: 3.6 | C3: 314257.6

### `7094b0a39fbe|NUMBERS_STORED_AS_TEXT|Sheet2!E2`

- workbook: `all_data_912_v0.1/spreadsheet/453-49/3_453-49_input.xlsx`
- location: `Sheet2!E2`  severity: Medium  confidence: Review
- evidence: Cell contains text value '7460118' in a column that otherwise holds 5 numbers.
- cached value: '7460118'; row labels: ["'PPL2122075'"]; column header: "'Batch'"; used range: A1:M7
- neighbourhood: C1: 'SLoc' | D1: 'S' | E1: 'Batch' | F1: 'S' | G1: 'Special Stock Number' | E2: '7460118' | E3: 7460987 | E4: 1234567

### `4cb669285990|NUMBERS_STORED_AS_TEXT|Sheet1!I8`

- workbook: `all_data_912_v0.1/spreadsheet/418-25/2_418-25_input.xlsx`
- location: `Sheet1!I8`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1771 ' in a column that otherwise holds 7 numbers.
- cached value: '1771 '; row labels: ["'MQ-818YEJ'", "'Purchase Ordering'"]; column header: "'2391  Sammy'"; used range: A1:I27
- neighbourhood: I6: '1791 REFUND ' | I7: '2391  Sammy' | I8: '1771 ' | I9: '1611  Sammy jonker' | I10: '2002 jW 78 WF GP'

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

### `92f8bf691072|VOLATILE_FUNCTION|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!F3`  severity: Low  confidence: Info
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: 56 formula(s) on Test use TODAY or NOW, so their results change with the clock: Test!F3, Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, ....
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:15:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `40397a4736e1|VOLATILE_FUNCTION|Test!F3`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F3`  severity: Low  confidence: Info
- formula: `=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-CO",B3="PRG/TVL-CO",B3="FLY1-CO",B3="TVL1-CO"),IF(IFERROR(1/(1/F3),"")="",TODAY()+VLOOKUP(C3,DATA!$A:$E,4,0),F3),"")`
- evidence: 56 formula(s) on Test use TODAY or NOW, so their results change with the clock: Test!F3, Test!F4, Test!F5, Test!F6, Test!F7, Test!F8, Test!F9, Test!F10, ....
- cached value: 2021-04-30 08:45:00; row labels: ["'PRG/FLY'"]; column header: ''; used range: A1:M79
- neighbourhood: D3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")' -> 'AAA' | E3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,3,0),"")' -> 'LLL' | F3: '=IF(OR(B3="PRG/FLY",B3="PRG/TVL",B3="FLY1",B3="TVL1",B3="PRG/FLY-C... -> 2021-04-30 08:45:00 | G3: '=IFERROR(VLOOKUP(C3,DATA!$A:$E,5,0),"")' -> 1:15:00 | D4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,2,0),"")' -> 'AAA' | E4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,3,0),"")' -> 'QQQ' | F4: '=IF(OR(B4="PRG/FLY",B4="PRG/TVL",B4="FLY1",B4="TVL1",B4="PRG/FLY-C... -> None | G4: '=IFERROR(VLOOKUP(C4,DATA!$A:$E,5,0),"")' -> 0:55:00 | D5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,2,0),"")' -> 'AAA' | E5: 'AAA' | F5: '=IF(OR(B5="PRG/FLY",B5="PRG/TVL",B5="FLY1",B5="TVL1",B5="PRG/FLY-C... -> None | G5: '=IFERROR(VLOOKUP(C5,DATA!$A:$E,5,0),"")' -> 1:25:00

### `c5ab9001d952|VOLATILE_FUNCTION|YTDBudget&Summary!G2`

- workbook: `all_data_912_v0.1/spreadsheet/55392/1_55392_input.xlsx`
- location: `YTD Budget & Summary!G2`  severity: Low  confidence: Info
- formula: `=YEAR(TODAY())`
- evidence: 1 formula(s) on YTD Budget & Summary use TODAY or NOW, so their results change with the clock: YTD Budget & Summary!G2.
- cached value: 2021; row labels: ["'ACTUAL vs. BUDGET YTD'", "'YEAR'"]; column header: ''; used range: A1:G22
- neighbourhood: F2: 'YEAR' | G2: '=YEAR(TODAY())' -> 2021 | E3: 'Budget' | F3: 'Remaining Rs.' | G3: 'Remaining %' | E4: 100000 | F4: '=IF(YearToDateTable[[#This Row],[Budget]]="","",YearToDateTable[[#... -> 100000 | G4: '=IFERROR(YearToDateTable[[#This Row],[Remaining Rs.]]/YearToDateTa... -> 1

### `c4229dd05b85|VOLATILE_FUNCTION|example!F8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!F8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(15,20)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!F9, example!F10, example!F11, example!F12.
- cached value: 18; row labels: ["'Egg'"]; column header: "'NOOR'"; used range: A1:O18
- neighbourhood: D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 20 | H8: '=RANDBETWEEN(25,30)' -> 28 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | F9: '=RANDBETWEEN(15,20)' -> 15 | G9: '=RANDBETWEEN(20,25)' -> 20 | H9: '=RANDBETWEEN(25,30)' -> 30 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | F10: '=RANDBETWEEN(15,20)' -> 19 | G10: '=RANDBETWEEN(20,25)' -> 25 | H10: '=RANDBETWEEN(25,30)' -> 30

### `b7e17665b0cc|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/54640/2_54640_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=DATEDIF(C2,TODAY(),"D")`
- evidence: 17 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: 1903-02-09 00:00:00; row labels: []; column header: ''; used range: A1:D18
- neighbourhood: C1: 'Start Date' | C2: 2021-04-10 00:00:00 | D2: '=DATEDIF(C2,TODAY(),"D")' -> 1903-02-09 00:00:00 | C3: 2021-04-16 00:00:00 | D3: '=DATEDIF(C3,TODAY(),"D")' -> 1903-02-03 00:00:00 | C4: 2021-04-16 00:00:00 | D4: '=DATEDIF(C4,TODAY(),"D")' -> 1903-02-03 00:00:00

### `61961992fd15|VOLATILE_FUNCTION|DATABANK!B4`

- workbook: `all_data_912_v0.1/spreadsheet/54238/1_54238_input.xlsx`
- location: `DATABANK!B4`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on DATABANK use TODAY or NOW, so their results change with the clock: DATABANK!B4.
- cached value: 2024-05-30 00:00:00; row labels: []; column header: ''; used range: A1:I13
- neighbourhood: B4: '=TODAY()' -> 2024-05-30 00:00:00 | B6: 'Fiscal Month'

### `201fbe2f5c4e|VOLATILE_FUNCTION|Sheet1!F14`

- workbook: `all_data_912_v0.1/spreadsheet/13894/3_13894_input.xlsx`
- location: `Sheet1!F14`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(ucode,SMALL(IF(MATCH(ucode,ucode,0)=ROW(INDIRECT("1:"&ROWS(ucode))),MATCH(ucode,ucode,0),""),ROW(INDIRECT("1:"&ROWS(ucode))))),"")`
- evidence: Function(s) found: INDIRECT.
- cached value: '8424.20.00ACMECHINA'; row labels: []; column header: "'IFERROR(INDEX(ucode;SMALL(IF(MATCH(ucode;ucode;0)=ROW(IN..."; used range: A1:K25
- neighbourhood: F12: 'IFERROR(INDEX(ucode;SMALL(IF(MATCH(u... | F14: '=IFERROR(INDEX(ucode,SMALL(IF(MATCH(ucode,ucode,0)=ROW(INDIRECT("1... -> '8424.20.00ACMECHINA' | G14: 1 | F15: '5620.30.00YYYYFRANCE' | G15: 2 | F16: '3424.20.00ACMECHINA' | G16: 3

### `9e84580cc354|VOLATILE_FUNCTION|Sheet1!C2`

- workbook: `all_data_912_v0.1/spreadsheet/49196/3_49196_input.xlsx`
- location: `Sheet1!C2`  severity: Low  confidence: Info
- formula: `=LEFT(K2,2)&"/"&MID(K2,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K2,FIND(" ",K2,1),6)`
- evidence: 46 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!C2, Sheet1!C3, Sheet1!C4, Sheet1!C5, Sheet1!C6, Sheet1!C7, Sheet1!C8, Sheet1!C9, ....
- cached value: '21/11/24 14:28'; row labels: []; column header: "'Start Time'"; used range: A1:L47
- neighbourhood: C1: 'Start Time' | D1: 'Month' | E1: 'Week' | C2: '=LEFT(K2,2)&"/"&MID(K2,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K2,FIND(" "... -> '21/11/24 14:28' | D2: '=TEXT(C2,"mmm")' -> 'Nov' | E2: '=WEEKNUM(C2,21)' -> '#NUM!' | C3: '=LEFT(K3,2)&"/"&MID(K3,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K3,FIND(" "... -> '22/11/24 05:00' | D3: '=TEXT(C3,"mmm")' -> 'Nov' | E3: '=WEEKNUM(C3,21)' -> '#NUM!' | C4: '=LEFT(K4,2)&"/"&MID(K4,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K4,FIND(" "... -> '23/11/24 06:00' | D4: '=TEXT(C4,"mmm")' -> 'Nov' | E4: '=WEEKNUM(C4,21)' -> '#NUM!'

### `63492daacabf|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/48930/3_48930_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")`
- evidence: 16 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!E2, Sheet1!D3, Sheet1!E3, Sheet1!D4, Sheet1!E4, Sheet1!D5, Sheet1!E5, ....
- cached value: 8; row labels: ["'Matthew'", "'PK'"]; column header: "'Age'"; used range: A1:E9
- neighbourhood: B1: 'Grade' | C1: 'Birth Date' | D1: 'Age' | E1: 'KDG Year' | B2: 'PK' | C2: 2016-02-11 00:00:00 | D2: '=IF(C2,DATEDIF(C2,TODAY(),"Y"),"")' -> 8 | E2: '=YEAR(TODAY())+(5-D2)' -> 2021 | B3: 'PK' | C3: 2017-12-22 00:00:00 | D3: '=IF(C3,DATEDIF(C3,TODAY(),"Y"),"")' -> 6 | E3: '=YEAR(TODAY())+(5-D3)' -> 2023 | B4: 'PK' | C4: 2016-12-13 00:00:00 | D4: '=IF(C4,DATEDIF(C4,TODAY(),"Y"),"")' -> 7 | E4: '=YEAR(TODAY())+(5-D4)' -> 2022

### `3a4af9c80244|VOLATILE_FUNCTION|Sheet1!F3`

- workbook: `all_data_912_v0.1/spreadsheet/57376/3_57376_input.xlsx`
- location: `Sheet1!F3`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(E3+14,E3+RAND()*100)`
- evidence: Function(s) found: RAND, RANDBETWEEN.
- evidence: The same relative formula appears in 50 cells on this sheet; the others are Sheet1!F4, Sheet1!F5, Sheet1!F6, Sheet1!F7, Sheet1!F8, Sheet1!F9, Sheet1!F10, Sheet1!F11, and 41 more.
- cached value: 2021-01-21 00:00:00; row labels: []; column header: "'end date'"; used range: A1:G30002
- neighbourhood: D2: 'rang_val' | E2: 'start date' | F2: 'end date' | G2: 'duration_amount_available' | D3: '=RANDBETWEEN(50,750)' -> 608 | E3: 2021-01-03 00:00:00 | F3: '=RANDBETWEEN(E3+14,E3+RAND()*100)' -> 2021-01-21 00:00:00 | G3: '=DATEDIF(E3,F3,"D")+1' -> 19 | D4: '=RANDBETWEEN(50,750)' -> 323 | E4: 2021-01-02 00:00:00 | F4: '=RANDBETWEEN(E4+14,E4+RAND()*100)' -> 2021-01-29 00:00:00 | G4: '=DATEDIF(E4,F4,"D")+1' -> 28 | D5: '=RANDBETWEEN(50,750)' -> 516 | E5: 2021-01-02 00:00:00 | F5: '=RANDBETWEEN(E5+14,E5+RAND()*100)' -> 2021-03-11 00:00:00 | G5: '=DATEDIF(E5,F5,"D")+1' -> 69

### `901359d33672|VOLATILE_FUNCTION|Sheet1!D2`

- workbook: `all_data_912_v0.1/spreadsheet/45181/3_45181_input.xlsx`
- location: `Sheet1!D2`  severity: Low  confidence: Info
- formula: `=C2-TODAY()`
- evidence: 19 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!D2, Sheet1!D3, Sheet1!D4, Sheet1!D5, Sheet1!D6, Sheet1!D7, Sheet1!D8, Sheet1!D9, ....
- cached value: -398; row labels: []; column header: "'Days left to return books'"; used range: A1:I20
- neighbourhood: B1: 'Date Picked UP' | C1: 'Date Drop Off' | D1: 'Days left to return books' | B2: 2022-04-29 00:00:00 | C2: '=B2+365' -> 2023-04-29 00:00:00 | D2: '=C2-TODAY()' -> -398 | B3: 2022-04-30 00:00:00 | C3: '=B3+365' -> 2023-04-30 00:00:00 | D3: '=C3-TODAY()' -> -397 | B4: 2022-05-02 00:00:00 | C4: '=B4+365' -> 2023-05-02 00:00:00 | D4: '=C4-TODAY()' -> -395

### `b7e4ec773e1c|VOLATILE_FUNCTION|Sheet1!L3`

- workbook: `all_data_912_v0.1/spreadsheet/44296/1_44296_input.xlsx`
- location: `Sheet1!L3`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- evidence: The same relative formula appears in 357 cells on this sheet; the others are Sheet1!M3, Sheet1!N3, Sheet1!O3, Sheet1!P3, Sheet1!Q3, Sheet1!R3, Sheet1!L4, Sheet1!M4, and 348 more.
- cached value: 0.95712595163862; row labels: ["'AK'"]; column header: ''; used range: A1:R53
- neighbourhood: K1: 'Year' | L1: 2015 | M1: 2016 | N1: 2017 | L3: '=RAND()' -> 0.95712595163862 | M3: '=RAND()' -> 0.226131197765814 | N3: '=RAND()' -> 0.109928922291012 | L4: '=RAND()' -> 0.801817882567899 | M4: '=RAND()' -> 0.655036053648042 | N4: '=RAND()' -> 0.760715331614859 | L5: '=RAND()' -> 0.0933720053682066 | M5: '=RAND()' -> 0.549548348313342 | N5: '=RAND()' -> 0.116555380285132

### `9d7ac18c8fd7|VOLATILE_FUNCTION|ImportData!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/3_444-27_input.xlsx`
- location: `Import Data!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 12 formula(s) on Import Data use TODAY or NOW, so their results change with the clock: Import Data!H2, Import Data!H3, Import Data!H4, Import Data!H5, Import Data!H6, Import Data!H7, Import Data!H8, Import Data!H9, ....
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:J13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 13859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `9950acdeddc6|VOLATILE_FUNCTION|ImportData!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/1_444-27_input.xlsx`
- location: `Import Data!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 12 formula(s) on Import Data use TODAY or NOW, so their results change with the clock: Import Data!H2, Import Data!H3, Import Data!H4, Import Data!H5, Import Data!H6, Import Data!H7, Import Data!H8, Import Data!H9, ....
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:J13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 13859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `a5e1567c7a75|VOLATILE_FUNCTION|DATABANK!B4`

- workbook: `all_data_912_v0.1/spreadsheet/54238/3_54238_input.xlsx`
- location: `DATABANK!B4`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on DATABANK use TODAY or NOW, so their results change with the clock: DATABANK!B4.
- cached value: 2024-05-20 00:00:00; row labels: []; column header: ''; used range: A1:I13
- neighbourhood: B4: '=TODAY()' -> 2024-05-20 00:00:00 | B6: 'Fiscal Month'

### `c05e60f72c61|VOLATILE_FUNCTION|Dati!CF12`

- workbook: `all_data_912_v0.1/spreadsheet/55912/2_55912_input.xlsx`
- location: `Dati!CF12`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1))*(#REF!="SI"))`
- evidence: Function(s) found: OFFSET.
- evidence: The same relative formula appears in 4 cells on this sheet; the others are Dati!CG12, Dati!CF17, Dati!CG17.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:CJ40
- neighbourhood: CF12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CG12: '=SUMPRODUCT(SUBTOTAL(3,OFFSET(#REF!,ROW(#REF!)-MIN(ROW(#REF!)),,1)... -> '#REF!' | CF13: '=1-(CF12/AG2)' -> '#REF!' | CG13: '=1-(CG12/AG2)' -> '#REF!' | CF14: '=1/CF13' -> '#REF!' | CG14: '=1/CG13' -> '#REF!'

### `2f9a764eab30|VOLATILE_FUNCTION|Sheet1!I6`

- workbook: `all_data_912_v0.1/spreadsheet/52541/1_52541_input.xlsx`
- location: `Sheet1!I6`  severity: Low  confidence: Info
- formula: `=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[#This Row],[Due Date]])`
- evidence: 5 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!I6, Sheet1!I7, Sheet1!I8, Sheet1!I9, Sheet1!I10.
- cached value: 1171; row labels: ["'ARON'"]; column header: "'Over Due Days'"; used range: A1:J13
- neighbourhood: G5: 'Due Date' | H5: 'Amount Outstanding' | I5: 'Over Due Days' | J5: 'Remarks' | G6: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-03-16 00:00:00 | H6: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 25000 | I6: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1171 | J6: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | G7: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-04-13 00:00:00 | H7: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 22000 | I7: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1143 | J7: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | G8: '=IF(Table2[[#This Row],[Invoice Date]]="","",Table2[[#This Row],[I... -> 2021-04-18 00:00:00 | H8: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> -3000 | I8: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1138 | J8: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts'

### `e3e5ae270e30|VOLATILE_FUNCTION|Sheet1!L5`

- workbook: `all_data_912_v0.1/spreadsheet/52450/2_52450_input.xlsx`
- location: `Sheet1!L5`  severity: Low  confidence: Info
- formula: `=IF(H5="","",IF(TODAY()>=I5,I5-H5,IF(TODAY()<H5,0,IF(H5<"",TODAY()-H5-J5,))))`
- evidence: 400 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!L5, Sheet1!P5, Sheet1!T5, Sheet1!V5, Sheet1!L6, Sheet1!P6, Sheet1!T6, Sheet1!V6, ....
- cached value: 0; row labels: ["'Wind'", "'Scott '"]; column header: "'Days Onsite to Date'"; used range: A1:NX104
- neighbourhood: J4: '=IF(H5="",0,IF(H5<"",SUM(J5:J104)))' -> 5 | K4: '=IF(G5="",0,IF(G5<"",SUM(K5:K104)))' -> 47 | M4: '=IF(H5="",0,IF(H5<"",SUM(M5:M104)))' -> 0 | J5: 5 | K5: '=IF(H5="","",IF(D5="Trainer","",IF(D5="Supps","",IF(H5<"""",I5-H5-... -> 12 | L5: '=IF(H5="","",IF(TODAY()>=I5,I5-H5,IF(TODAY()<H5,0,IF(H5<"",TODAY()... -> 0 | N5: 3 | K6: '=IF(H6="","",IF(D6="Trainer","",IF(D6="Supps","",IF(H6<"""",I6-H6-... -> 18 | L6: '=IF(H6="","",IF(TODAY()>=I6,I6-H6,IF(TODAY()<H6,0,IF(H6<"",TODAY()... -> 0 | N6: 3 | K7: '=IF(H7="","",IF(D7="Trainer","",IF(D7="Supps","",IF(H7<"""",I7-H7-... -> 17 | L7: '=IF(H7="","",IF(TODAY()>=I7,I7-H7,IF(TODAY()<H7,0,IF(H7<"",TODAY()... -> 0 | N7: 2

### `6b591cf8ff22|VOLATILE_FUNCTION|Open!O4`

- workbook: `all_data_912_v0.1/spreadsheet/124-9/3_124-9_input.xlsx`
- location: `Open!O4`  severity: Low  confidence: Info
- formula: `=INT(TODAY()-D4+(1))`
- evidence: 4997 formula(s) on Open use TODAY or NOW, so their results change with the clock: Open!O4, Open!O5, Open!O6, Open!O7, Open!O8, Open!O9, Open!O10, Open!O11, ....
- cached value: None; row labels: ["'Closed Complete'", "'Bekkam Rajashekar'"]; column header: "'Age'"; used range: A1:Q5000
- neighbourhood: M3: 'Closed' | N3: 'Updated' | O3: 'Age' | P3: 'Age Slab' | Q3: 'First Closed' | M4: 2023-03-17 22:36:21 | N4: 2023-03-17 22:36:21 | O4: '=INT(TODAY()-D4+(1))' -> None | P4: '=IF(O4<=2,"(0-2)",IF(O4<=5,"(3-5)",">5"))' -> None | Q4: '=IF(M4>0,IF(G4="Closed",M4-7,IF(LEFT(G4,6)="Closed",M4,0)),IF(AND(... -> None | M5: 2023-03-17 22:35:05 | N5: 2023-03-17 22:35:05 | O5: '=INT(TODAY()-D5+(1))' -> None | P5: '=IF(O5<=2,"(0-2)",IF(O5<=5,"(3-5)",">5"))' -> None | Q5: '=IF(M5>0,IF(G5="Closed",M5-7,IF(LEFT(G5,6)="Closed",M5,0)),IF(AND(... -> None | M6: 2023-03-17 22:47:22 | N6: 2023-03-17 22:47:21 | O6: '=INT(TODAY()-D6+(1))' -> None | P6: '=IF(O6<=2,"(0-2)",IF(O6<=5,"(3-5)",">5"))' -> None | Q6: '=IF(M6>0,IF(G6="Closed",M6-7,IF(LEFT(G6,6)="Closed",M6,0)),IF(AND(... -> None

### `565bd65adf32|VOLATILE_FUNCTION|Example!C1`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3575/2_CF_3575_input.xlsx`
- location: `Example!C1`  severity: Low  confidence: Info
- formula: `=TODAY()`
- evidence: 1 formula(s) on Example use TODAY or NOW, so their results change with the clock: Example!C1.
- cached value: 2024-05-27 00:00:00; row labels: []; column header: ''; used range: A1:BA85
- neighbourhood: C1: '=TODAY()' -> 2024-05-27 00:00:00 | B2: 'Example'

### `1699999ded57|VOLATILE_FUNCTION|ImportData!H2`

- workbook: `all_data_912_v0.1/spreadsheet/444-27/2_444-27_input.xlsx`
- location: `Import Data!H2`  severity: Low  confidence: Info
- formula: `=NOW()-E2`
- evidence: 12 formula(s) on Import Data use TODAY or NOW, so their results change with the clock: Import Data!H2, Import Data!H3, Import Data!H4, Import Data!H5, Import Data!H6, Import Data!H7, Import Data!H8, Import Data!H9, ....
- cached value: None; row labels: ["'62MTKGLA64'", "'JYT1987-2196'"]; column header: "'Ageing'"; used range: A1:J13
- neighbourhood: F1: 'Balance' | G1: 'Supplier Reference' | H1: 'Ageing' | F2: 14859.48 | G2: 'JYT1987-2196' | H2: '=NOW()-E2' -> None | F3: 18445.8753333333 | G3: 2208 | H3: '=NOW()-E3' -> None | F4: 19089.2833333333 | G4: 2208 | H4: '=NOW()-E4' -> None

### `c4229dd05b85|VOLATILE_FUNCTION|example!H8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!H8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(25,30)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!H9, example!H10, example!H11, example!H12.
- cached value: 28; row labels: ["'Egg'"]; column header: "'AHSAN'"; used range: A1:O18
- neighbourhood: F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | J7: 'Product' | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 20 | H8: '=RANDBETWEEN(25,30)' -> 28 | J8: 'Egg' | F9: '=RANDBETWEEN(15,20)' -> 15 | G9: '=RANDBETWEEN(20,25)' -> 20 | H9: '=RANDBETWEEN(25,30)' -> 30 | J9: 'Milk' | F10: '=RANDBETWEEN(15,20)' -> 19 | G10: '=RANDBETWEEN(20,25)' -> 25 | H10: '=RANDBETWEEN(25,30)' -> 30 | J10: 'Masala'

### `766ae98f7318|VOLATILE_FUNCTION|Sheet1!F10`

- workbook: `all_data_912_v0.1/spreadsheet/34435/3_34435_input.xlsx`
- location: `Sheet1!F10`  severity: Low  confidence: Info
- formula: `=TODAY()-E10`
- evidence: 14 formula(s) on Sheet1 use TODAY or NOW, so their results change with the clock: Sheet1!F10, Sheet1!F11, Sheet1!F12, Sheet1!F13, Sheet1!F14, Sheet1!F15, Sheet1!F16, Sheet1!F17, ....
- cached value: 5001; row labels: []; column header: "'Amount of Days After Hire'"; used range: A1:L23
- neighbourhood: E9: 'Employee Start Date' | F9: 'Amount of Days After Hire' | G9: 'Accumulated PTO (Hours)' | E10: 2010-09-06 00:00:00 | F10: '=TODAY()-E10' -> 5001 | E11: 2011-09-06 00:00:00 | F11: '=TODAY()-E11' -> 4636 | E12: 2012-09-06 00:00:00 | F12: '=TODAY()-E12' -> 4270

### `2b144ac2a52b|VOLATILE_FUNCTION|Data!I10`

- workbook: `all_data_912_v0.1/spreadsheet/118-10/1_118-10_input.xlsx`
- location: `Data!I10`  severity: Low  confidence: Info
- formula: `=IF(H10>0,TODAY()-(A10),"")`
- evidence: 14 formula(s) on Data use TODAY or NOW, so their results change with the clock: Data!I10, Data!I11, Data!I18, Data!I19, Data!I27, Data!I28, Data!I29, Data!I30, ....
- cached value: None; row labels: []; column header: ''; used range: A1:I46
- neighbourhood: I10: '=IF(H10>0,TODAY()-(A10),"")' -> None | I11: '=IF(H11>0,TODAY()-(A11),"")' -> None

### `5635b3c618d2|VOLATILE_FUNCTION|example!E8`

- workbook: `all_data_912_v0.1/spreadsheet/56996/3_56996_input.xlsx`
- location: `example!E8`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(10,15)`
- evidence: Function(s) found: RANDBETWEEN.
- evidence: The same relative formula appears in 5 cells on this sheet; the others are example!E9, example!E10, example!E11, example!E12.
- cached value: 11; row labels: ["'Egg'"]; column header: "'AMIN'"; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | F7: 'NOOR' | G7: 'SHAMS' | C8: '=RANDBETWEEN(1,5)' -> 2 | D8: '=RANDBETWEEN(5,10)' -> 7 | E8: '=RANDBETWEEN(10,15)' -> 11 | F8: '=RANDBETWEEN(15,20)' -> 18 | G8: '=RANDBETWEEN(20,25)' -> 25 | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 5 | E9: '=RANDBETWEEN(10,15)' -> 10 | F9: '=RANDBETWEEN(15,20)' -> 19 | G9: '=RANDBETWEEN(20,25)' -> 22 | C10: '=RANDBETWEEN(1,5)' -> 5 | D10: '=RANDBETWEEN(5,10)' -> 7 | E10: '=RANDBETWEEN(10,15)' -> 11 | F10: '=RANDBETWEEN(15,20)' -> 17 | G10: '=RANDBETWEEN(20,25)' -> 23

## WHITESPACE_KEY

### `5a98e72c8ee6|WHITESPACE_KEY|JournalEntries!E20`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Journal Entries!E20`  severity: Medium  confidence: Review
- evidence: Raw value is 'Third Party Loans '; the other text values in this column are not padded.
- cached value: 'Third Party Loans '; row labels: []; column header: "'Loans Disburesed'"; used range: A1:R3000
- neighbourhood: C18: '=IFERROR(VLOOKUP($E18,Sheet1!$B$2:$C$96,2,0),"")' -> 'WG/CR/030' | D18: '=IFERROR(VLOOKUP($E18,Sheet1!$B$2:$D$96,3,0),"")' -> 'Capital Acc' | E18: 'Donations' | F18: 100000 | G18: 'Bank' | C19: '=IFERROR(VLOOKUP($E19,Sheet1!$B$2:$C$96,2,0),"")' -> 'WG/CR/021' | D19: '=IFERROR(VLOOKUP($E19,Sheet1!$B$2:$D$96,3,0),"")' -> 'Debtors' | E19: 'Loans Disburesed' | F19: 200000 | G19: 'Bank' | C20: '=IFERROR(VLOOKUP($E20,Sheet1!$B$2:$C$96,2,0),"")' -> 'WG/CR/033' | D20: '=IFERROR(VLOOKUP($E20,Sheet1!$B$2:$D$96,3,0),"")' -> 'Debt Capital' | E20: 'Third Party Loans ' | F20: 3000000 | G20: 'Bank' | C21: '=IFERROR(VLOOKUP($E21,Sheet1!$B$2:$C$96,2,0),"")' -> 'WG/CR/032' | D21: '=IFERROR(VLOOKUP($E21,Sheet1!$B$2:$D$96,3,0),"")' -> 'Equity Capital' | E21: 'Owners Capital' | F21: 2500000 | G21: 'Bank' | C22: '=IFERROR(VLOOKUP($E22,Sheet1!$B$2:$C$96,2,0),"")' -> 'WG/CR/021' | D22: '=IFERROR(VLOOKUP($E22,Sheet1!$B$2:$D$96,3,0),"")' -> 'Debtors' | E22: 'Loans Disburesed' | F22: 1500000 | G22: 'Bank'

### `55d45b916f0d|WHITESPACE_KEY|Sheet1!A5`

- workbook: `all_data_912_v0.1/spreadsheet/48799/2_48799_input.xlsx`
- location: `Sheet1!A5`  severity: Medium  confidence: Review
- evidence: Raw value is 'D '.
- evidence: 3 of 25 text values in column A carry leading or trailing whitespace; the others are A7 'F ', A17 'P '.
- cached value: 'D '; row labels: []; column header: "'C'"; used range: A1:D25
- neighbourhood: A3: 'B' | B3: 3.13 | C3: 3.8682 | A4: 'C' | B4: 3.84 | C4: 4.2396 | A5: 'D ' | B5: 5.27 | C5: 3.6702 | A6: 'E' | B6: 7.8 | C6: 6.282 | A7: 'F ' | B7: 6.2 | C7: 7.458

### `3a2b74c70f66|WHITESPACE_KEY|Total(2)!E106`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!E106`  severity: Medium  confidence: Review
- evidence: Raw value is ' xcb.'; the other text values in this column are not padded.
- cached value: ' xcb.'; row labels: ["'b'"]; column header: ''; used range: A1:Z1026
- neighbourhood: E106: ' xcb.'

### `e32dc7118a33|WHITESPACE_KEY|Sheet1!A4`

- workbook: `all_data_912_v0.1/spreadsheet/55468/3_55468_input.xlsx`
- location: `Sheet1!A4`  severity: Medium  confidence: Review
- evidence: Raw value is 'Grade '; the other text values in this column are not padded.
- cached value: 'Grade '; row labels: []; column header: ''; used range: A1:AG31
- neighbourhood: C2: '200-499' | B3: 'qty code' | C3: 1 | A4: 'Grade ' | B4: 'Flute ' | C4: 1 | A5: '125C125C' | B5: 'B' | C5: 302 | A6: '125T125T' | B6: 'B' | C6: 305

### `d3575a4dff7b|WHITESPACE_KEY|HouseBudget!T61`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/2_CF_22493_input.xlsx`
- location: `House Budget!T61`  severity: Medium  confidence: Review
- evidence: Raw value is 'Total  '; the other text values in this column are not padded.
- cached value: 'Total  '; row labels: ["'Total Budgeted Expenses  '", "'Total For Month'"]; column header: ''; used range: A1:AG123
- neighbourhood: T59: '=E59' -> 0 | U59: '=SUM(H59:S59)' -> 0 | V59: '=U59/12' -> 0 | T60: '=E60' -> 0 | U60: '=SUM(H60:S60)' -> 0 | V60: '=U60/12' -> 0 | R61: '=SUM(R3:R60)' -> 0 | S61: '=SUM(S3:S60)' -> 0 | T61: 'Total  ' | U61: '=SUM(U3:U60)' -> 0 | V61: '=U61/12' -> 0 | R62: '=IF(R61>F61,(R61-F61),"")' -> None | S62: '=IF(S61>F61,(S61-F61),"")' -> None | R63: '=IF(R61<F61,(F61-R61),"")' -> 7411 | S63: '=IF(S61<F61,(F61-S61),"")' -> 7411

### `5a98e72c8ee6|WHITESPACE_KEY|MonthlyExpensesSummary!D43`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Monthly Expenses Summary!D43`  severity: Medium  confidence: Review
- evidence: Raw value is 'Third Party Loans '; the other text values in this column are not padded.
- cached value: 'Third Party Loans '; row labels: []; column header: "'Owners Capital'"; used range: A1:R65
- neighbourhood: B41: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'WG/CR/031' | C41: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'P & L' | D41: 'Other Incomes' | E41: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F41: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | B42: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'WG/CR/032' | C42: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'Equity Capital' | D42: 'Owners Capital' | E42: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F42: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | B43: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'WG/CR/033' | C43: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> 'Debt Capital' | D43: 'Third Party Loans ' | E43: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F43: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | B44: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> None | C44: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> None | E44: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F44: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | B45: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> None | C45: '=IFERROR(VLOOKUP(MonthlyExpensesSummary[[#This Row],[Account Title... -> None | E45: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0 | F45: '=IFERROR(SUMPRODUCT((\'Journal Entries\'!$C$6:$C$3000=\'Monthly Ex... -> 0

### `ef479c030de6|WHITESPACE_KEY|Sheet1!A3`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!A3`  severity: Medium  confidence: Review
- evidence: Raw value is 'Week '; the other text values in this column are not padded.
- cached value: 'Week '; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: B2: 'CASE REPLIES' | A3: 'Week ' | B3: 'Team Total' | C3: 'Goal #' | A4: 2023-10-16 00:00:00 | B4: 167 | A5: 2023-10-23 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None

### `1c06477fced9|WHITESPACE_KEY|Compiledandlocatedschoolsda!L2`

- workbook: `all_data_912_v0.1/spreadsheet/55427/1_55427_input.xlsx`
- location: `Compiled and located schools da!L2`  severity: Medium  confidence: Review
- evidence: Raw value is ' LA13 9RP'; 757 other text value(s) in column L are padded too, but only these 12 are read by a formula or in the first column, where keys usually sit.
- evidence: 12 of 1418 text values in column L carry leading or trailing whitespace; the others are L3 ' LA11 6SN', L4 ' CA1 1JB', L5 ' CA13 9BH', L6 ' CA13 9BH', L7 ' LA11 7RD', L8 ' CA15 6QG', L9 ' CA9 3UF', L10 ' LA22 0BZ', and 3 more.
- cached value: ' LA13 9RP'; row labels: ["' Cambridge Street'", "' Barrow-In-Furness'"]; column header: "'Postcode'"; used range: A1:AJ1419
- neighbourhood: J1: 'Address4' | K1: 'Address5' | L1: 'Postcode' | M1: 'Title' | N1: 'Initial' | L2: ' LA13 9RP' | M2: 'Mrs' | N2: 'S' | J3: ' Grange-Over-Sands' | L3: ' LA11 6SN' | M3: 'C' | N3: 'Mason' | L4: ' CA1 1JB' | M4: 'Mr' | N4: 'K'

### `a86f94be97b9|WHITESPACE_KEY|Sheet1!A4`

- workbook: `all_data_912_v0.1/spreadsheet/55468/2_55468_input.xlsx`
- location: `Sheet1!A4`  severity: Medium  confidence: Review
- evidence: Raw value is 'Grade '; the other text values in this column are not padded.
- cached value: 'Grade '; row labels: []; column header: ''; used range: A1:AG31
- neighbourhood: C2: '200-499' | B3: 'qty code' | C3: 1 | A4: 'Grade ' | B4: 'Flute ' | C4: 1 | A5: '125C125C' | B5: 'B' | C5: 302 | A6: '125T125T' | B6: 'B' | C6: 305

### `d7704e65e140|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/48968/3_48968_input.xlsx`
- location: `Sheet1!A2`  severity: Low  confidence: Info
- evidence: 11 of 12 text values in column A carry leading or trailing whitespace, for example 'Garments manufactured For Winnerforce \nMEN-MATRIXT-JACKET(COYOTE)\nWOMEN-WREN-JACKET(COYOTE)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'; this looks like fixed-width padding from an export.
- cached value: 'Garments manufactured For Winnerforce \nMEN-MATRIXT-JACK...; row labels: []; column header: "'Original list'"; used range: A1:B12
- neighbourhood: A1: 'Original list' | B1: 'preferred display' | A2: 'Garments manufactured For Winnerforc... | B2: 'Garments manufactured For Winnerforc... | A3: 'Garments manufactured For Winnerforc... | B3: 'Garments manufactured For Winnerforc... | A4: 'Garments manufactured For Winnerforc... | B4: 'Garments manufactured For Winnerforc...

### `cae03100ef09|WHITESPACE_KEY|Sheet1!I4`

- workbook: `all_data_912_v0.1/spreadsheet/40510/3_40510_input.xlsx`
- location: `Sheet1!I4`  severity: Medium  confidence: Review
- evidence: Raw value is 'JUNE 2022GENERAL BORROWER '; 2 other text value(s) in column I are padded too, but only this one is read by a formula or in the first column, where keys usually sit.
- cached value: 'JUNE 2022GENERAL BORROWER '; row labels: ["''", "''"]; column header: "'Scheme Name'"; used range: A1:N31
- neighbourhood: J2: 'I want this RESULT ' | G3: 'SCheme6' | I3: 'Scheme Name' | J3: 'Interest' | G4: '' | H4: '' | I4: 'JUNE 2022GENERAL BORROWER ' | J4: '=SUMPRODUCT(([1]!Table1[Interest])*([1]!Table1[[SCheme1]:[SCheme6]... -> 0 | K4: '' | G5: '' | H5: '' | I5: ' GHARKUL YOJANA  ABN ' | K5: '' | I6: 'CLEAN   '

### `50e95eddd565|WHITESPACE_KEY|Sheet1!A10`

- workbook: `all_data_912_v0.1/spreadsheet/50472/2_50472_input.xlsx`
- location: `Sheet1!A10`  severity: Medium  confidence: Review
- evidence: Raw value is '606270 Acc. Social Charges - Expense '.
- evidence: 6 of 12 text values in column A carry leading or trailing whitespace; the others are A11 '205035 Accrued Social Charges ', A13 '606270 Acc. Social Charges - Expense ', A14 '205035 Accrued Social Charges ', A16 '606270 Acc. Social Charges - Expense ', A17 '205035 Accrued Social Charges '.
- cached value: '606270 Acc. Social Charges - Expense '; row labels: []; column header: "'205020 - Accrued Commissions'"; used range: A1:A17
- neighbourhood: A8: '205020 - Accrued Commissions' | A10: '606270 Acc. Social Charges - Expense ' | A11: '205035 Accrued Social Charges '

### `b4bb29667c08|WHITESPACE_KEY|Sheet1!A9`

- workbook: `all_data_912_v0.1/spreadsheet/48930/1_48930_input.xlsx`
- location: `Sheet1!A9`  severity: Medium  confidence: Review
- evidence: Raw value is 'Tony '; the other text values in this column are not padded.
- cached value: 'Tony '; row labels: []; column header: "'Philip'"; used range: A1:E9
- neighbourhood: A7: 'Sandy' | B7: 'PK' | C7: 2017-10-10 00:00:00 | A8: 'Philip' | B8: 'PK' | C8: 2017-11-02 00:00:00 | A9: 'Tony ' | B9: 'PK' | C9: 2018-03-13 00:00:00

### `2f8c049b867d|WHITESPACE_KEY|ProductList!A4`

- workbook: `all_data_912_v0.1/spreadsheet/32895/1_32895_input.xlsx`
- location: `Product List!A4`  severity: Medium  confidence: Review
- evidence: Raw value is 'PLASTIC ICING 1KG '.
- evidence: 3 of 13 text values in column A carry leading or trailing whitespace; the others are A6 'FINO WHIP 5KG ', A10 'WHIPPET 5KG '.
- cached value: 'PLASTIC ICING 1KG '; row labels: []; column header: "'Product'"; used range: A1:C14
- neighbourhood: A3: 'Product' | B3: 'Code' | C3: 'Opening Balance' | A4: 'PLASTIC ICING 1KG ' | B4: 'B001' | C4: 100 | A5: 'PLASTIC ICING 500G' | B5: 'B002' | C5: 40 | A6: 'FINO WHIP 5KG ' | B6: 'B003' | C6: 90

### `e4dd1fc8c138|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/57225/1_57225_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Raw value is 'pick 2 '; the other text values in this column are not padded.
- cached value: 'pick 2 '; row labels: []; column header: "'pick 1'"; used range: A1:J7
- neighbourhood: A1: 'pick 1' | B1: 'david' | A2: 'pick 2 '

### `d7e27f29097e|WHITESPACE_KEY|Malaga!A7`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!A7`  severity: Medium  confidence: Review
- evidence: Raw value is 'Golf at La Cala America, La Cala Asia, '; the other text values in this column are not padded.
- cached value: 'Golf at La Cala America, La Cala Asia, '; row labels: []; column header: "'Golf'"; used range: A1:AJ57
- neighbourhood: A5: 'Not Inc: Flights available from Birm... | A6: 'Golf' | A7: 'Golf at La Cala America, La Cala Asi... | A8: 'No' | B8: 'Room' | C8: 'NAME' | A9: 1 | B9: 1 | C9: 'CURT (Kellie)'

### `c561c810150e|WHITESPACE_KEY|Sheet1!B12`

- workbook: `all_data_912_v0.1/spreadsheet/54675/2_54675_input.xlsx`
- location: `Sheet1!B12`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '.
- evidence: 21 of 146 text values in column B carry leading or trailing whitespace; the others are B13 'Angela McConnell ', B16 'Angela McConnell ', B20 'Building Services, Angela McConnell ', B21 'Angela McConnell ', B23 'Angela McConnell ', B24 'Angela McConnell ', B34 'Gary Stoddard, Angela McConnell ', B35 'Angela McConnell ', and 12 more.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Building Services'"; used range: A1:F2452
- neighbourhood: A10: 4 | B10: 'Lynn Meek, Sandy Ross, Kirsty Mcdonald' | A11: 4 | B11: 'Building Services' | A12: 4 | B12: 'Angela McConnell ' | A13: 4 | B13: 'Angela McConnell ' | A14: 4 | B14: 'Phyllis McFadyen'

### `f7c5dc14603a|WHITESPACE_KEY|Inflexion!A9`

- workbook: `all_data_912_v0.1/spreadsheet/18645/3_18645_input.xlsx`
- location: `Inflexion!A9`  severity: Medium  confidence: Review
- evidence: Raw value is 'Asperity '.
- evidence: 2 of 16 text values in column A carry leading or trailing whitespace; the others are A13 'SMD '.
- cached value: 'Asperity '; row labels: []; column header: "'Phlexglobal'"; used range: A1:C56
- neighbourhood: A7: 'Ideal Shopping Direct' | B7: 2011 | C7: 'Online/TV Retail' | A8: 'Phlexglobal' | B8: 2011 | C8: 'Pharmaceutical' | A9: 'Asperity ' | B9: 2010 | C9: 'Employee Benefits' | A10: 'FDM Group' | B10: 2010 | C10: 'IT Temp & Services' | A11: 'Griffin Global Group' | B11: 2009 | C11: 'Travel/Logistics'

### `b577453716f5|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/56451/2_56451_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Raw value is 'John '; the other text values in this column are not padded.
- cached value: 'John '; row labels: []; column header: "'NAME'"; used range: A1:U11
- neighbourhood: A1: 'NAME' | B1: 'transport' | C1: 'weight' | A2: 'John ' | B2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'Plane' | C2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'Plane' | A3: 'Mary' | B3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | C3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | A4: 'Todd' | B4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | C4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk'

### `decb1aae7638|WHITESPACE_KEY|Sheet1!A2`

- workbook: `all_data_912_v0.1/spreadsheet/31184/1_31184_input.xlsx`
- location: `Sheet1!A2`  severity: Medium  confidence: Review
- evidence: Raw value is 'Mike '; 1 other text value(s) in column A are padded too, but only these 2 are read by a formula or in the first column, where keys usually sit.
- evidence: 2 of 7 text values in column A carry leading or trailing whitespace; the others are A3 'Mike '.
- cached value: 'Mike '; row labels: []; column header: "'Name '"; used range: A1:R15
- neighbourhood: A1: 'Name ' | A2: 'Mike ' | B2: 'yes' | A3: 'Mike ' | B3: 'yes'

### `1354a93ef2de|WHITESPACE_KEY|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/48354/1_48354_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- evidence: Raw value is 'operating an international flight '; the other text values in this column are not padded.
- cached value: 'operating an international flight '; row labels: ["'N/A'"]; column header: "'ContactType'"; used range: A1:D6
- neighbourhood: A1: 'D or I' | B1: 'ContactType' | A2: 'N/A' | B2: 'operating an international flight ' | D2: '=IF(B2="domestic",“D”,IF(B2="international",“I”,“N/A”)) {array D2}' -> '#NAME?' | A3: 'N/A' | B3: 'operating a domestic flight' | D3: '=IF(B3="domestic",“D”,IF(B3="international",“I”,“N/A”)) {array D3}' -> '#NAME?' | A4: 'N/A' | B4: 'jumpseating (domestic)' | D4: '=IF(B4="domestic",“D”,IF(B4="international",“I”,“N/A”)) {array D4}' -> '#NAME?'

### `6354e61254b2|WHITESPACE_KEY|Sheet1!A82`

- workbook: `all_data_912_v0.1/spreadsheet/290-27/2_290-27_input.xlsx`
- location: `Sheet1!A82`  severity: Medium  confidence: Review
- evidence: Raw value is 'GG '.
- evidence: 5 of 95 text values in column A carry leading or trailing whitespace; the others are A93 'GG ', A105 'GG ', A116 'GG ', A130 'GG '.
- cached value: 'GG '; row labels: []; column header: "'NAME'"; used range: A1:I139
- neighbourhood: A80: 'NAME' | B80: 'GG 1' | C80: 'Clm 4000b' | A82: 'GG ' | B82: 2020-08-29 00:00:00 | C82: 'GG 1' | A84: "LACEY'S RAINBOW"

### `1d7b84636c8e|WHITESPACE_KEY|Sheet1!A12`

- workbook: `all_data_912_v0.1/spreadsheet/40892/2_40892_input.xlsx`
- location: `Sheet1!A12`  severity: Medium  confidence: Review
- evidence: Raw value is 'Trousers Black '.
- evidence: 2 of 17 text values in column A carry leading or trailing whitespace; the others are A17 'Trousers Black '.
- cached value: 'Trousers Black '; row labels: []; column header: "'Top Red'"; used range: A1:D17
- neighbourhood: A10: 'Purple Scarf' | A11: 'Top Red' | A12: 'Trousers Black ' | A13: 'Orange Jumpsuits' | A14: 'Yellow Jumpsuit'

### `72574e72007c|WHITESPACE_KEY|Sheet1!A10`

- workbook: `all_data_912_v0.1/spreadsheet/50472/1_50472_input.xlsx`
- location: `Sheet1!A10`  severity: Medium  confidence: Review
- evidence: Raw value is '606270 Acc. Social Charges - Expense '.
- evidence: 6 of 12 text values in column A carry leading or trailing whitespace; the others are A11 '205035 Accrued Social Charges ', A13 '606270 Acc. Social Charges - Expense ', A14 '205035 Accrued Social Charges ', A16 '606270 Acc. Social Charges - Expense ', A17 '205035 Accrued Social Charges '.
- cached value: '606270 Acc. Social Charges - Expense '; row labels: []; column header: "'205020 - Accrued Commissions'"; used range: A1:A17
- neighbourhood: A8: '205020 - Accrued Commissions' | A10: '606270 Acc. Social Charges - Expense ' | A11: '205035 Accrued Social Charges '

### `3517fbb37fa4|WHITESPACE_KEY|Dec14!A14`

- workbook: `all_data_912_v0.1/spreadsheet/50534/2_50534_input.xlsx`
- location: `Dec 14!A14`  severity: Medium  confidence: Review
- evidence: Raw value is 'COURTNEY '; the other text values in this column are not padded.
- cached value: 'COURTNEY '; row labels: []; column header: "'DONITA'"; used range: A1:I27
- neighbourhood: A12: 'ANDREW' | B12: '(206)571-7535' | C12: 'admin' | A13: 'DONITA' | B13: '(253)431-9941' | C13: '11P-7A' | A14: 'COURTNEY ' | B14: '(602)918-4633' | C14: '3-11' | A15: 'TOM' | B15: '206-852-5614' | C15: '7-3' | A16: 'EDITH' | B16: '509-778-2033'

## WHOLE_COLUMN_REFERENCE

### `7cc6b0fe1206|WHOLE_COLUMN_REFERENCE|All!AE2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `All!AE2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(D:D=K2,$I:$I))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AE3, All!AE4, All!AE5, All!AE6, All!AE7, All!AE8, All!AE9, All!AE10, and 16 more.
- cached value: -6.659999999999999; row labels: []; column header: "'Hi P/B                                         (NTA)'"; used range: A1:AL5968
- neighbourhood: AC1: 'Hi P/E' | AD1: 'Hi P/S' | AE1: 'Hi P/B                              ... | AG1: 'Year' | AC2: '=MAX(IF(D:D=K2,$G:$G)) {array AC2}' -> 0 | AD2: '=MAX(IF(D:D=K2,$H:$H)) {array AD2}' -> 0.31728659476117105 | AE2: '=MAX(IF(D:D=K2,$I:$I)) {array AE2}' -> -6.659999999999999 | AG2: '=K2' -> 1997 | AC3: '=MAX(IF(D:D=K3,$G:$G)) {array AC3}' -> 347.1999999999997 | AD3: '=MAX(IF(D:D=K3,$H:$H)) {array AD3}' -> 0.8538468271334791 | AE3: '=MAX(IF(D:D=K3,$I:$I)) {array AE3}' -> 2.04 | AG3: '=K3' -> 1998 | AC4: '=MAX(IF(D:D=K4,$G:$G)) {array AC4}' -> 21.544444444444448 | AD4: '=MAX(IF(D:D=K4,$H:$H)) {array AD4}' -> 2.0331998695793936 | AE4: '=MAX(IF(D:D=K4,$I:$I)) {array AE4}' -> 2.2199999999999998 | AG4: '=K4' -> 1999

### `b31624554d1c|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7000 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `0e309a2a0da6|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/2_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, and 20 more.
- cached value: 'PEPEPEPEPE'; row labels: ["'no'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J))' -> 'PEPEPEPEPE'

### `7cc6b0fe1206|WHOLE_COLUMN_REFERENCE|All!AH2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `All!AH2`  severity: Medium  confidence: Review
- formula: `=MIN(IF(D:D=K2,B:B))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AH3, All!AH4, All!AH5, All!AH6, All!AH7, All!AH8, All!AH9, All!AH10, and 16 more.
- cached value: 0; row labels: []; column header: "'Low Price'"; used range: A1:AL5968
- neighbourhood: AG1: 'Year' | AH1: 'Low Price' | AI1: 'Low Market Cap' | AJ1: 'Low P/E' | AG2: '=K2' -> 1997 | AH2: '=MIN(IF(D:D=K2,B:B)) {array AH2}' -> 0 | AI2: '=MIN(IF($D:$D=K2,$F:$F)) {array AI2}' -> 0 | AJ2: '=MIN(IF($D:$D=K2,$G:$G)) {array AJ2}' -> 0 | AG3: '=K3' -> 1998 | AH3: '=MIN(IF(D:D=K3,B:B)) {array AH3}' -> 4.26 | AI3: '=MIN(IF($D:$D=K3,$F:$F)) {array AI3}' -> 6845.819574 | AJ3: '=MIN(IF($D:$D=K3,$G:$G)) {array AJ3}' -> 0 | AG4: '=K4' -> 1999 | AH4: '=MIN(IF(D:D=K4,B:B)) {array AH4}' -> 42.75 | AI4: '=MIN(IF($D:$D=K4,$F:$F)) {array AI4}' -> 132695.99144999997 | AJ4: '=MIN(IF($D:$D=K4,$G:$G)) {array AJ4}' -> 8.990825688073395

### `be2f958d4b41|WHOLE_COLUMN_REFERENCE|All!AD2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/2_59932_input.xlsx`
- location: `All!AD2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(D:D=K2,$H:$H))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AD3, All!AD4, All!AD5, All!AD6, All!AD7, All!AD8, All!AD9, All!AD10, and 16 more.
- cached value: 0.31728659476117105; row labels: []; column header: "'Hi P/S'"; used range: A1:AL5968
- neighbourhood: AB1: 'Hi Market Cap' | AC1: 'Hi P/E' | AD1: 'Hi P/S' | AE1: 'Hi P/B                              ... | AB2: '=MAX(IF(D:D=K2,$F:$F)) {array AB2}' -> 6187.719461 | AC2: '=MAX(IF(D:D=K2,$G:$G)) {array AC2}' -> 0 | AD2: '=MAX(IF(D:D=K2,$H:$H)) {array AD2}' -> 0.31728659476117105 | AE2: '=MAX(IF(D:D=K2,$I:$I)) {array AE2}' -> -6.659999999999999 | AB3: '=MAX(IF(D:D=K3,$F:$F)) {array AB3}' -> 94266.614134 | AC3: '=MAX(IF(D:D=K3,$G:$G)) {array AC3}' -> 347.1999999999997 | AD3: '=MAX(IF(D:D=K3,$H:$H)) {array AD3}' -> 0.8538468271334791 | AE3: '=MAX(IF(D:D=K3,$I:$I)) {array AE3}' -> 2.04 | AB4: '=MAX(IF(D:D=K4,$F:$F)) {array AB4}' -> 331165.73866199993 | AC4: '=MAX(IF(D:D=K4,$G:$G)) {array AC4}' -> 21.544444444444448 | AD4: '=MAX(IF(D:D=K4,$H:$H)) {array AD4}' -> 2.0331998695793936 | AE4: '=MAX(IF(D:D=K4,$I:$I)) {array AE4}' -> 2.2199999999999998

### `be2f958d4b41|WHOLE_COLUMN_REFERENCE|All!AJ2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/2_59932_input.xlsx`
- location: `All!AJ2`  severity: Medium  confidence: Review
- formula: `=MIN(IF($D:$D=K2,$G:$G))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AJ3, All!AJ4, All!AJ5, All!AJ6, All!AJ7, All!AJ8, All!AJ9, All!AJ10, and 16 more.
- cached value: 0; row labels: []; column header: "'Low P/E'"; used range: A1:AL5968
- neighbourhood: AH1: 'Low Price' | AI1: 'Low Market Cap' | AJ1: 'Low P/E' | AK1: 'Low P/S' | AL1: 'Low P/B                             ... | AH2: '=MIN(IF(D:D=K2,B:B)) {array AH2}' -> 0 | AI2: '=MIN(IF($D:$D=K2,$F:$F)) {array AI2}' -> 0 | AJ2: '=MIN(IF($D:$D=K2,$G:$G)) {array AJ2}' -> 0 | AK2: '=MIN(IF($D:$D=K2,$H:$H)) {array AK2}' -> 0.26543523693803156 | AL2: '=MIN(IF($D:$D=K2,$I:$I)) {array AL2}' -> -8.3 | AH3: '=MIN(IF(D:D=K3,B:B)) {array AH3}' -> 4.26 | AI3: '=MIN(IF($D:$D=K3,$F:$F)) {array AI3}' -> 6845.819574 | AJ3: '=MIN(IF($D:$D=K3,$G:$G)) {array AJ3}' -> 0 | AK3: '=MIN(IF($D:$D=K3,$H:$H)) {array AK3}' -> 0.3652263399693721 | AL3: '=MIN(IF($D:$D=K3,$I:$I)) {array AL3}' -> -7.01 | AH4: '=MIN(IF(D:D=K4,B:B)) {array AH4}' -> 42.75 | AI4: '=MIN(IF($D:$D=K4,$F:$F)) {array AI4}' -> 132695.99144999997 | AJ4: '=MIN(IF($D:$D=K4,$G:$G)) {array AJ4}' -> 8.990825688073395 | AK4: '=MIN(IF($D:$D=K4,$H:$H)) {array AK4}' -> 1.0379318294088589 | AL4: '=MIN(IF($D:$D=K4,$I:$I)) {array AL4}' -> 1.7999999999999998

### `40c60acd7755|WHOLE_COLUMN_REFERENCE|All!AE2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `All!AE2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(D:D=K2,$I:$I))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AE3, All!AE4, All!AE5, All!AE6, All!AE7, All!AE8, All!AE9, All!AE10, and 16 more.
- cached value: -6.659999999999999; row labels: []; column header: "'Hi P/B                                         (NTA)'"; used range: A1:AL5968
- neighbourhood: AC1: 'Hi P/E' | AD1: 'Hi P/S' | AE1: 'Hi P/B                              ... | AG1: 'Year' | AC2: '=MAX(IF(D:D=K2,$G:$G)) {array AC2}' -> 0 | AD2: '=MAX(IF(D:D=K2,$H:$H)) {array AD2}' -> 0.31728659476117105 | AE2: '=MAX(IF(D:D=K2,$I:$I)) {array AE2}' -> -6.659999999999999 | AG2: '=K2' -> 1997 | AC3: '=MAX(IF(D:D=K3,$G:$G)) {array AC3}' -> 347.1999999999997 | AD3: '=MAX(IF(D:D=K3,$H:$H)) {array AD3}' -> 0.8538468271334791 | AE3: '=MAX(IF(D:D=K3,$I:$I)) {array AE3}' -> 2.04 | AG3: '=K3' -> 1998 | AC4: '=MAX(IF(D:D=K4,$G:$G)) {array AC4}' -> 21.544444444444448 | AD4: '=MAX(IF(D:D=K4,$H:$H)) {array AD4}' -> 2.0331998695793936 | AE4: '=MAX(IF(D:D=K4,$I:$I)) {array AE4}' -> 2.2199999999999998 | AG4: '=K4' -> 1999

### `40c60acd7755|WHOLE_COLUMN_REFERENCE|All!AH2`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `All!AH2`  severity: Medium  confidence: Review
- formula: `=MIN(IF(D:D=K2,B:B))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 25 cells on this sheet; the others are All!AH3, All!AH4, All!AH5, All!AH6, All!AH7, All!AH8, All!AH9, All!AH10, and 16 more.
- cached value: 0; row labels: []; column header: "'Low Price'"; used range: A1:AL5968
- neighbourhood: AG1: 'Year' | AH1: 'Low Price' | AI1: 'Low Market Cap' | AJ1: 'Low P/E' | AG2: '=K2' -> 1997 | AH2: '=MIN(IF(D:D=K2,B:B)) {array AH2}' -> 0 | AI2: '=MIN(IF($D:$D=K2,$F:$F)) {array AI2}' -> 0 | AJ2: '=MIN(IF($D:$D=K2,$G:$G)) {array AJ2}' -> 0 | AG3: '=K3' -> 1998 | AH3: '=MIN(IF(D:D=K3,B:B)) {array AH3}' -> 4.26 | AI3: '=MIN(IF($D:$D=K3,$F:$F)) {array AI3}' -> 6845.819574 | AJ3: '=MIN(IF($D:$D=K3,$G:$G)) {array AJ3}' -> 0 | AG4: '=K4' -> 1999 | AH4: '=MIN(IF(D:D=K4,B:B)) {array AH4}' -> 42.75 | AI4: '=MIN(IF($D:$D=K4,$F:$F)) {array AI4}' -> 132695.99144999997 | AJ4: '=MIN(IF($D:$D=K4,$G:$G)) {array AJ4}' -> 8.990825688073395

### `be6378a48fb9|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/2_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I5`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!I5`  severity: Medium  confidence: Review
- formula: `=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C,""))),"ÅÅÅÅ-MM-DD")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are Volym P5_P6_2023!I6, Volym P5_P6_2023!I7, Volym P5_P6_2023!I8, Volym P5_P6_2023!I9, Volym P5_P6_2023!I10.
- cached value: '#VALUE!'; row labels: ["'ABC3'"]; column header: ''; used range: A1:K10
- neighbourhood: G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007' | G5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I5: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C... -> '#VALUE!' | J5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I6: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!D:D,""))... -> '200000008' | K6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!E:E,""))... -> '460000008' | G7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I7: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!D:D,""))... -> '200000009' | K7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!E:E,""))... -> '460000009'

### `286f4ae7ac70|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/3_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, and 12 more.
- cached value: '#VALUE!'; row labels: ["'F100063'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `740614797bbb|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/1_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, and 20 more.
- cached value: 'PEPEPEPEPE'; row labels: ["'YES'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N2}' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N3}' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N4}' -> 'PEPEPEPEPE'

### `8738ef8d70bc|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/2_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, and 396 more.
- cached value: 2014-04-28 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-28 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-03-24 00:00:00

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!J2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!J3, Volym P5_P6_2023!J4, Volym P5_P6_2023!J5, Volym P5_P6_2023!J6, Volym P5_P6_2023!J7, Volym P5_P6_2023!J8, Volym P5_P6_2023!J9, Volym P5_P6_2023!J10.
- cached value: '200000003,200000005'; row labels: ["'ABC2'"]; column header: "'Source list Agreement (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '44926' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000007'

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I5`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!I5`  severity: Medium  confidence: Review
- formula: `=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C,""))),"ÅÅÅÅ-MM-DD")`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 6 cells on this sheet; the others are Volym P5_P6_2023!I6, Volym P5_P6_2023!I7, Volym P5_P6_2023!I8, Volym P5_P6_2023!I9, Volym P5_P6_2023!I10.
- cached value: '2022-12-31'; row labels: ["'ABC4'"]; column header: ''; used range: A1:K10
- neighbourhood: G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006' | G5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H5: '=IF(B5="Yes",_xlfn.XLOOKUP(A5,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I5: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!D:D,""))... -> '200000007' | K5: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A5=ZORD!A:A,ZORD!E:E,""))... -> '460000007' | G6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H6: '=IF(B6="Yes",_xlfn.XLOOKUP(A6,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I6: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!D:D,""))... -> '200000008' | K6: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A6=ZORD!A:A,ZORD!E:E,""))... -> '460000008' | G7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I7: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!D:D,""))... -> '200000009' | K7: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!E:E,""))... -> '460000009'

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '44926,45657'; row labels: ["'ABC2'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `9dd7a633cf36|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!J2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/2_45896_input.xlsx`
- location: `Volym P5_P6_2023!J2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 9 cells on this sheet; the others are Volym P5_P6_2023!J3, Volym P5_P6_2023!J4, Volym P5_P6_2023!J5, Volym P5_P6_2023!J6, Volym P5_P6_2023!J7, Volym P5_P6_2023!J8, Volym P5_P6_2023!J9, Volym P5_P6_2023!J10.
- cached value: '200000003,200000005'; row labels: ["'ABC2'"]; column header: "'Source list Agreement (If Quota)\\n2nd option'"; used range: A1:K10
- neighbourhood: H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `eba9bd965a28|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!I2`

- workbook: `all_data_912_v0.1/spreadsheet/45896/1_45896_input.xlsx`
- location: `Volym P5_P6_2023!I2`  severity: Medium  confidence: Review
- formula: `=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,"")))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 3 cells on this sheet; the others are Volym P5_P6_2023!I3, Volym P5_P6_2023!I4.
- cached value: '46022,45657,45291'; row labels: ["'ABC1'"]; column header: "'Source list (If Quota) \\n2nd option'"; used range: A1:K10
- neighbourhood: G1: 'Source list Agreement\n(If Quota)' | H1: 'Source list Vendor\n(If Quota)' | I1: 'Source list (If Quota) \n2nd option' | J1: 'Source list Agreement (If Quota)\n2n... | K1: 'Source list Vendor (If Quota)\n2nd o... | G2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000000 | H2: '=IF(B2="Yes",_xlfn.XLOOKUP(A2,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000000 | I2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!C:C,""))... -> '46022,45657,45291' | J2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!D:D,""))... -> '200000001,200000002,200000... | K2: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A2=ZORD!A:A,ZORD!E:E,""))... -> '460000001,460000002,460000... | G3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000005 | H3: '=IF(B3="Yes",_xlfn.XLOOKUP(A3,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000005 | I3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!C:C,""))... -> '44926,45657' | J3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!D:D,""))... -> '200000003,200000005' | K3: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A3=ZORD!A:A,ZORD!E:E,""))... -> '460000003,460000005' | G4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!E:E,,,-1),"")' -> 460000006 | H4: '=IF(B4="Yes",_xlfn.XLOOKUP(A4,ZORD!A:A,ZORD!D:D,,,-1),"")' -> 200000006 | I4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!C:C,""))... -> '45627,45657' | J4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!D:D,""))... -> '200000004,200000006' | K4: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A4=ZORD!A:A,ZORD!E:E,""))... -> '460000004,460000006'

### `d7cd8ee7e5c8|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/3_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, and 396 more.
- cached value: 2014-04-08 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-08 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-12-24 00:00:00

### `321c9048065c|WHOLE_COLUMN_REFERENCE|Sheet1!N2`

- workbook: `all_data_912_v0.1/spreadsheet/33935/3_33935_input.xlsx`
- location: `Sheet1!N2`  severity: Medium  confidence: Review
- formula: `=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 29 cells on this sheet; the others are Sheet1!N3, Sheet1!N4, Sheet1!N5, Sheet1!N6, Sheet1!N7, Sheet1!N8, Sheet1!N9, Sheet1!N10, and 20 more.
- cached value: 'PEPEPEPEPE'; row labels: ["'YES'", "'02:59 Sat'"]; column header: "'Start'"; used range: A1:S30
- neighbourhood: L1: 'Pos' | N1: 'Start' | L2: '=IF(AND(G2<1,L1<>""),1,L1+1)' -> 1 | N2: '=IF(L3>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N2}' -> 'PEPEPEPEPE' | L3: '=IF(AND(G3<1,L2<>""),1,L2+1)' -> 2 | N3: '=IF(L4>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N3}' -> 'PEPEPEPEPE' | L4: '=IF(AND(G4<1,L3<>""),1,L3+1)' -> 3 | N4: '=IF(L5>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N4}' -> 'PEPEPEPEPE'

### `87c4744e15aa|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/1_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, and 12 more.
- cached value: '#VALUE!'; row labels: ["'F100063'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100063' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'

### `47eb61dd533e|WHOLE_COLUMN_REFERENCE|TEST!B11`

- workbook: `all_data_912_v0.1/spreadsheet/55039/1_55039_input.xlsx`
- location: `TEST!B11`  severity: Medium  confidence: Review
- formula: `=LOOKUP(2,1/(F:F<>""),F:F)`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- cached value: 2021-08-29 00:00:00; row labels: ["'Goal Date'"]; column header: ''; used range: A1:S1004
- neighbourhood: A9: 'Current Balance' | B9: '=K63' -> 7350 | A10: 'Goal' | B10: '=B47' -> 1000000 | C10: '=_xlfn.DAYS(B11,B8)' -> 146 | A11: 'Goal Date' | B11: '=LOOKUP(2,1/(F:F<>""),F:F) {array B11}' -> 2021-08-29 00:00:00 | A13: 'Level 1' | B13: 1000 | C13: '=IF(B13<=$B$9,"ONE STEP CLOSER","FOCUS")' -> 'ONE STEP CLOSER'

### `5358e587d475|WHOLE_COLUMN_REFERENCE|Sheet1!B2`

- workbook: `all_data_912_v0.1/spreadsheet/17049/1_17049_input.xlsx`
- location: `Sheet1!B2`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A2,G:G,""))`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 405 cells on this sheet; the others are Sheet1!B3, Sheet1!B4, Sheet1!B5, Sheet1!B6, Sheet1!B7, Sheet1!B8, Sheet1!B9, Sheet1!B10, and 396 more.
- cached value: 2014-04-08 00:00:00; row labels: []; column header: "'Recent Date'"; used range: A1:G1998
- neighbourhood: A1: 'Row Labels' | B1: 'Recent Date' | A2: 1 | B2: '=MAX(IF(F:F=A2,G:G,"")) {array B2}' -> 2014-04-08 00:00:00 | A3: 2 | B3: '=MAX(IF(F:F=A3,G:G,"")) {array B3}' -> 00:00:00 | A4: 3 | B4: '=MAX(IF(F:F=A4,G:G,"")) {array B4}' -> 2014-03-24 00:00:00

### `61bf2143f38b|WHOLE_COLUMN_REFERENCE|book1!B3`

- workbook: `all_data_912_v0.1/spreadsheet/55049/2_55049_input.xlsx`
- location: `book1!B3`  severity: Medium  confidence: Review
- formula: `=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J`
- evidence: A whole-column reference is evaluated as an array here, so every recalculation scans the full column height.
- evidence: The same relative formula appears in 21 cells on this sheet; the others are book1!B4, book1!B5, book1!B6, book1!B7, book1!B8, book1!B9, book1!B10, book1!B11, and 12 more.
- cached value: '#VALUE!'; row labels: ["'F100066'"]; column header: ''; used range: A1:B23
- neighbourhood: A2: 'Place' | A3: 'F100066' | B3: '=SUMPRODUCT(book2!A:A=book1!A3)*book2!H:J {array B3}' -> '#VALUE!' | A4: 'F100064' | B4: '=SUMPRODUCT(book2!A:A=book1!A4)*book2!H:J {array B4}' -> '#VALUE!' | A5: 'F100065' | B5: '=SUMPRODUCT(book2!A:A=book1!A5)*book2!H:J {array B5}' -> '#VALUE!'
