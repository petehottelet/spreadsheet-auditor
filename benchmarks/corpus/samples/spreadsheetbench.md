# Finding cards: spreadsheetbench

Generated 2026-09-14T06:34:07+00:00 from C:\Users\PeteHottelet\Projects\skills\spreadsheet-auditor\benchmarks\corpus\results\spreadsheetbench with seed 7, up to 25 per rule and 2 per workbook.

Label each card in `labels/<source>.json` as `TP` (the auditor is right), `FP` (it is wrong), or `unsure`, with a one-line reason.

## BLANK_PRECEDENT

### `f065dc30ad2b|BLANK_PRECEDENT|Sheet1!CH13|8db8bc`

- workbook: `all_data_912_v0.1/spreadsheet/CF_6540/2_CF_6540_input.xlsx`
- location: `Sheet1!CH13`  severity: Medium  confidence: Review
- formula: `=MIN(F13,J13,N13,R13,V13,Z13,AD13,AH13,AL13,AP13,AT13,AX13,BB13,BF13,BN13,BR13,BV13,BZ13,CD13)`
- evidence: Referenced cell Sheet1!BN13 is blank.
- cached value: 20; row labels: ["'Hand Signaller '"]; column header: ''; used range: A1:CL123
- neighbourhood: CH11: '=MIN(F11,J11,N11,R11,V11,Z11,AD11,AH11,AL11,AP11,AT11,AX11,BB11,BF... -> 20.2 | CI11: '=MIN(G11,K11,O11,S11,W11,AA11,AE11,AI11,AM11,AQ11,AU11,AY11,BC11,B... -> 20.2 | CJ11: '=MIN(H11,L11,P11,T11,X11,AB11,AF11,AJ11,AN11,AR11,AV11,AZ11,BD11,B... -> 23.5 | CH12: '=MIN(F12,J12,N12,R12,V12,Z12,AD12,AH12,AL12,AP12,AT12,AX12,BB12,BF... -> 0 | CI12: '=MIN(G12,K12,O12,S12,W12,AA12,AE12,AI12,AM12,AQ12,AU12,AY12,BC12,B... -> 0 | CJ12: '=MIN(H12,L12,P12,T12,X12,AB12,AF12,AJ12,AN12,AR12,AV12,AZ12,BD12,B... -> 0 | CH13: '=MIN(F13,J13,N13,R13,V13,Z13,AD13,AH13,AL13,AP13,AT13,AX13,BB13,BF... -> 20 | CI13: '=MIN(G13,K13,O13,S13,W13,AA13,AE13,AI13,AM13,AQ13,AU13,AY13,BC13,B... -> 21 | CJ13: '=MIN(H13,L13,P13,T13,X13,AB13,AF13,AJ13,AN13,AR13,AV13,AZ13,BD13,B... -> 23 | CF14: 24.3 | CG14: 31.59 | CH14: '=MIN(F14,J14,N14,R14,V14,Z14,AD14,AH14,AL14,AP14,AT14,AX14,BB14,BF... -> 18.63 | CI14: '=MIN(G14,K14,O14,S14,W14,AA14,AE14,AI14,AM14,AQ14,AU14,AY14,BC14,B... -> 19.5275 | CJ14: '=MIN(H14,L14,P14,T14,X14,AB14,AF14,AJ14,AN14,AR14,AV14,AZ14,BD14,B... -> 20.865000000000002 | CH15: '=MIN(F15,J15,N15,R15,V15,Z15,AD15,AH15,AL15,AP15,AT15,AX15,BB15,BF... -> 0 | CI15: '=MIN(G15,K15,O15,S15,W15,AA15,AE15,AI15,AM15,AQ15,AU15,AY15,BC15,B... -> 0 | CJ15: '=MIN(H15,L15,P15,T15,X15,AB15,AF15,AJ15,AN15,AR15,AV15,AZ15,BD15,B... -> 0

### `2ed80e0ee4cd|BLANK_PRECEDENT|DRP!O5|4e80a2`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!O5`  severity: Medium  confidence: Review
- formula: `=L5+M5-N5`
- evidence: Referenced cell DRP!N5 is blank.
- cached value: None; row labels: ["'RE1'", "'RS1'"]; column header: ''; used range: A1:O23
- neighbourhood: M3: 400 | N3: 20 | O3: '=L3+M3-N3' -> None | N4: 20 | O4: '=L4+M4-N4' -> None | O5: '=L5+M5-N5' -> None | M6: '=SUM(M2:M5)' -> None | N6: '=SUM(N2:N5)' -> None | O6: '=SUM(O2:O5)' -> None | M7: 100 | N7: 10 | O7: '=L7+M7-N7' -> None

### `e1683f0529fe|BLANK_PRECEDENT|MoneyInChecking!E10`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/3_CF_22493_input.xlsx`
- location: `Money In Checking!E10`  severity: Medium  confidence: Review
- formula: `=IF(C10="","",B10)`
- evidence: Referenced cell Money In Checking!C10 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:R65
- neighbourhood: E8: '=IF(C8="","",B8)' -> None | F8: "='Money In Checking Next Month'!G8" -> '21st' | G8: 0 | E9: '=IF(C9="","",B9)' -> None | F9: "='Money In Checking Next Month'!G9" -> '12th' | E10: '=IF(C10="","",B10)' -> None | F10: "='Money In Checking Next Month'!G10" -> '21st' | G10: 'Money In Checking' | E11: '=IF(C11="","",B11)' -> None | F11: "='Money In Checking Next Month'!G11" -> '4th' | G11: 0 | E12: '=IF(C12="","",B12)' -> None | F12: "='Money In Checking Next Month'!G12" -> '1st'

### `92f8bf691072|BLANK_PRECEDENT|Test!E34`

- workbook: `all_data_912_v0.1/spreadsheet/54667/1_54667_input.xlsx`
- location: `Test!E34`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(C34,DATA!$A:$E,3,0),"")`
- evidence: Referenced cell Test!C34 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,2,0),"")' -> None | E32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,3,0),"")' -> None | F32: '=IF(OR(B32="PRG/FLY",B32="PRG/TVL",B32="FLY1",B32="TVL1",B32="PRG/... -> None | G32: '=IFERROR(VLOOKUP(C32,DATA!$A:$E,5,0),"")' -> None | D33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,2,0),"")' -> None | E33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,3,0),"")' -> None | F33: '=IF(OR(B33="PRG/FLY",B33="PRG/TVL",B33="FLY1",B33="TVL1",B33="PRG/... -> None | G33: '=IFERROR(VLOOKUP(C33,DATA!$A:$E,5,0),"")' -> None | D34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,2,0),"")' -> None | E34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,3,0),"")' -> None | F34: '=IF(OR(B34="PRG/FLY",B34="PRG/TVL",B34="FLY1",B34="TVL1",B34="PRG/... -> None | G34: '=IFERROR(VLOOKUP(C34,DATA!$A:$E,5,0),"")' -> None | D35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,2,0),"")' -> None | E35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,3,0),"")' -> None | F35: '=IF(OR(B35="PRG/FLY",B35="PRG/TVL",B35="FLY1",B35="TVL1",B35="PRG/... -> None | G35: '=IFERROR(VLOOKUP(C35,DATA!$A:$E,5,0),"")' -> None | D36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,2,0),"")' -> None | E36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,3,0),"")' -> None | F36: '=IF(OR(B36="PRG/FLY",B36="PRG/TVL",B36="FLY1",B36="TVL1",B36="PRG/... -> None | G36: '=IFERROR(VLOOKUP(C36,DATA!$A:$E,5,0),"")' -> None

### `09478d797a42|BLANK_PRECEDENT|BankBalance!N24|e0b8fe`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Bank Balance!N24`  severity: Medium  confidence: Review
- formula: `=IF(AND('Journal Entries'!$H27="credit",'Journal Entries'!$E27='Bank Balance'!N$2),'Journal Entries'!$F27,"")`
- evidence: Referenced cell Journal Entries!F27 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:AL3000
- neighbourhood: L22: '=IF(AND(\'Journal Entries\'!$H25="credit",\'Journal Entries\'!$E25... -> None | M22: '=IF(AND(\'Journal Entries\'!$H25="credit",\'Journal Entries\'!$E25... -> None | N22: '=IF(AND(\'Journal Entries\'!$H25="credit",\'Journal Entries\'!$E25... -> None | O22: '=IF(AND(\'Journal Entries\'!$H25="credit",\'Journal Entries\'!$E25... -> None | P22: '=IF(AND(\'Journal Entries\'!$H25="credit",\'Journal Entries\'!$E25... -> None | L23: '=IF(AND(\'Journal Entries\'!$H26="credit",\'Journal Entries\'!$E26... -> None | M23: '=IF(AND(\'Journal Entries\'!$H26="credit",\'Journal Entries\'!$E26... -> None | N23: '=IF(AND(\'Journal Entries\'!$H26="credit",\'Journal Entries\'!$E26... -> None | O23: '=IF(AND(\'Journal Entries\'!$H26="credit",\'Journal Entries\'!$E26... -> None | P23: '=IF(AND(\'Journal Entries\'!$H26="credit",\'Journal Entries\'!$E26... -> None | L24: '=IF(AND(\'Journal Entries\'!$H27="credit",\'Journal Entries\'!$E27... -> None | M24: '=IF(AND(\'Journal Entries\'!$H27="credit",\'Journal Entries\'!$E27... -> None | N24: '=IF(AND(\'Journal Entries\'!$H27="credit",\'Journal Entries\'!$E27... -> None | O24: '=IF(AND(\'Journal Entries\'!$H27="credit",\'Journal Entries\'!$E27... -> None | P24: '=IF(AND(\'Journal Entries\'!$H27="credit",\'Journal Entries\'!$E27... -> None

### `589c38846e3c|BLANK_PRECEDENT|Oct!A48`

- workbook: `all_data_912_v0.1/spreadsheet/11842/3_11842_input.xlsx`
- location: `Oct!A48`  severity: Medium  confidence: Review
- formula: `=Jan!A48`
- evidence: Referenced cell Jan!A48 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:AO49
- neighbourhood: A46: '=Jan!A46' -> 0 | A48: '=Jan!A48' -> 0

### `d3575a4dff7b|BLANK_PRECEDENT|MoneyInChecking!N51`

- workbook: `all_data_912_v0.1/spreadsheet/CF_22493/2_CF_22493_input.xlsx`
- location: `Money In Checking!N51`  severity: Medium  confidence: Review
- formula: `='Money In Checking Next Month'!C51`
- evidence: Referenced cell Money In Checking Next Month!C51 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:R65
- neighbourhood: L49: '=J49-K49' -> 0 | N49: "='Money In Checking Next Month'!C49" -> 0 | P49: "='Money In Checking Next Month'!A49" -> 0 | L50: '=J50-K50' -> 0 | N50: "='Money In Checking Next Month'!C50" -> 0 | P50: "='Money In Checking Next Month'!A50" -> 0 | L51: '=J51-K51' -> 0 | N51: "='Money In Checking Next Month'!C51" -> 0 | P51: "='Money In Checking Next Month'!A51" -> 0 | L52: '=J52-K52' -> 0 | N52: "='Money In Checking Next Month'!C52" -> 0 | P52: "='Money In Checking Next Month'!A52" -> 0 | L53: '=J53-K53' -> 0 | N53: "='Money In Checking Next Month'!C53" -> 0 | P53: "='Money In Checking Next Month'!A53" -> 0

### `b8b03c02336b|BLANK_PRECEDENT|Test!E41`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!E41`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(C41,DATA!$A:$E,3,0),"")`
- evidence: Referenced cell Test!C41 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,2,0),"")' -> None | E39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,3,0),"")' -> None | F39: '=IF(OR(B39="PRG/FLY",B39="PRG/TVL",B39="FLY1",B39="TVL1",B39="PRG/... -> None | G39: '=IFERROR(VLOOKUP(C39,DATA!$A:$E,5,0),"")' -> None | D40: '=IFERROR(VLOOKUP(C40,DATA!$A:$E,2,0),"")' -> None | E40: '=IFERROR(VLOOKUP(C40,DATA!$A:$E,3,0),"")' -> None | F40: '=IF(OR(B40="PRG/FLY",B40="PRG/TVL",B40="FLY1",B40="TVL1",B40="PRG/... -> None | G40: '=IFERROR(VLOOKUP(C40,DATA!$A:$E,5,0),"")' -> None | D41: '=IFERROR(VLOOKUP(C41,DATA!$A:$E,2,0),"")' -> None | E41: '=IFERROR(VLOOKUP(C41,DATA!$A:$E,3,0),"")' -> None | F41: '=IF(OR(B41="PRG/FLY",B41="PRG/TVL",B41="FLY1",B41="TVL1",B41="PRG/... -> None | G41: '=IFERROR(VLOOKUP(C41,DATA!$A:$E,5,0),"")' -> None | D42: '=IFERROR(VLOOKUP(C42,DATA!$A:$E,2,0),"")' -> None | E42: '=IFERROR(VLOOKUP(C42,DATA!$A:$E,3,0),"")' -> None | F42: '=IF(OR(B42="PRG/FLY",B42="PRG/TVL",B42="FLY1",B42="TVL1",B42="PRG/... -> None | G42: '=IFERROR(VLOOKUP(C42,DATA!$A:$E,5,0),"")' -> None | D43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,2,0),"")' -> None | E43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,3,0),"")' -> None | F43: '=IF(OR(B43="PRG/FLY",B43="PRG/TVL",B43="FLY1",B43="TVL1",B43="PRG/... -> None | G43: '=IFERROR(VLOOKUP(C43,DATA!$A:$E,5,0),"")' -> None

### `0bffec63dc84|BLANK_PRECEDENT|Purchases!F159|908af3`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/1_CF_3712_input.xlsx`
- location: `Purchases!F159`  severity: Medium  confidence: Review
- formula: `=(C159*E159)+D159`
- evidence: Referenced cell Purchases!D159 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:M441
- neighbourhood: F157: '=(C157*E157)+D157' -> 0 | H157: '=IF(ISBLANK(G157), "", G157 + 30)' -> None | F158: '=(C158*E158)+D158' -> 0 | H158: '=IF(ISBLANK(G158), "", G158 + 30)' -> None | F159: '=(C159*E159)+D159' -> 0 | H159: '=IF(ISBLANK(G159), "", G159 + 30)' -> None | F160: '=(C160*E160)+D160' -> 0 | H160: '=IF(ISBLANK(G160), "", G160 + 30)' -> None | F161: '=(C161*E161)+D161' -> 0 | H161: '=IF(ISBLANK(G161), "", G161 + 30)' -> None

### `2b89f3e053b3|BLANK_PRECEDENT|Here!C25|f05495`

- workbook: `all_data_912_v0.1/spreadsheet/58147/2_58147_input.xlsx`
- location: `Here!C25`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!C25="","",Sheet1!C25)`
- evidence: Referenced cell Sheet1!C25 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: A23: '=IF(Sheet1!A23="","",Sheet1!A23)' -> 22 | B23: '=IF(Sheet1!B23="","",Sheet1!B23)' -> 'HO10339330' | C23: '=IF(Sheet1!C23="","",Sheet1!C23)' -> None | D23: '=IF(Sheet1!D23="","",Sheet1!D23)' -> None | E23: '=IF(Sheet1!E23="","",Sheet1!E23)' -> None | A24: '=IF(Sheet1!A24="","",Sheet1!A24)' -> 23 | B24: '=IF(Sheet1!B24="","",Sheet1!B24)' -> 'RS31728184' | C24: '=IF(Sheet1!C24="","",Sheet1!C24)' -> None | D24: '=IF(Sheet1!D24="","",Sheet1!D24)' -> None | E24: '=IF(Sheet1!E24="","",Sheet1!E24)' -> None | A25: '=IF(Sheet1!A25="","",Sheet1!A25)' -> 24 | B25: '=IF(Sheet1!B25="","",Sheet1!B25)' -> 'SS43010028' | C25: '=IF(Sheet1!C25="","",Sheet1!C25)' -> None | D25: '=IF(Sheet1!D25="","",Sheet1!D25)' -> None | E25: '=IF(Sheet1!E25="","",Sheet1!E25)' -> None | A26: '=IF(Sheet1!A26="","",Sheet1!A26)' -> 25 | B26: '=IF(Sheet1!B26="","",Sheet1!B26)' -> 'TT33991592' | C26: '=IF(Sheet1!C26="","",Sheet1!C26)' -> None | D26: '=IF(Sheet1!D26="","",Sheet1!D26)' -> None | E26: '=IF(Sheet1!E26="","",Sheet1!E26)' -> None | A27: '=IF(Sheet1!A27="","",Sheet1!A27)' -> 26 | B27: '=IF(Sheet1!B27="","",Sheet1!B27)' -> 'CV22833553' | C27: '=IF(Sheet1!C27="","",Sheet1!C27)' -> None | D27: '=IF(Sheet1!D27="","",Sheet1!D27)' -> None | E27: '=IF(Sheet1!E27="","",Sheet1!E27)' -> None

### `5d9172f87a18|BLANK_PRECEDENT|AFTER!S21|0bdb2c`

- workbook: `all_data_912_v0.1/spreadsheet/47360/2_47360_input.xlsx`
- location: `AFTER!S21`  severity: Medium  confidence: Review
- formula: `=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A21)*(BEFORE!$B$2:$B$977=B21)),BEFORE!$A$2:$A$977)),"N","Y")`
- evidence: Referenced cell AFTER!A21 is blank.
- cached value: 'Y'; row labels: []; column header: ''; used range: A1:W258
- range BEFORE!$A$2:$A$977: values ["'NAMETEST1'", "'NAMETEST2'", "'NAMETEST3'", "'NAMETEST4'", "'NAMETEST5'", 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "A1: 'Name'", 'below': 'A978: None'}
- neighbourhood: S19: '=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A19)*(BEFORE!$B$2:$B$977=... -> 'Y' | S20: '=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A20)*(BEFORE!$B$2:$B$977=... -> 'Y' | S21: '=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A21)*(BEFORE!$B$2:$B$977=... -> 'Y' | S22: '=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A22)*(BEFORE!$B$2:$B$977=... -> 'Y' | S23: '=IF(ISNA(LOOKUP(2,1/((BEFORE!$A$2:$A$977=A23)*(BEFORE!$B$2:$B$977=... -> 'Y'

### `fc600bf64e36|BLANK_PRECEDENT|Sheet1!F11|2deeef`

- workbook: `all_data_912_v0.1/spreadsheet/48643/1_48643_input.xlsx`
- location: `Sheet1!F11`  severity: Medium  confidence: Review
- formula: `=(1+C11)*B11`
- evidence: Referenced cell Sheet1!B11 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:H40
- neighbourhood: E9: '=B9*C9' -> 0 | F9: '=(1+C9)*B9' -> 0 | E10: '=B10*C10' -> 0 | F10: '=(1+C10)*B10' -> 0 | E11: '=B11*C11' -> 0 | F11: '=(1+C11)*B11' -> 0 | E12: '=B12*C12' -> 0 | F12: '=(1+C12)*B12' -> 0 | E13: '=B13*C13' -> 0 | F13: '=(1+C13)*B13' -> 0

### `a94399daa94c|BLANK_PRECEDENT|Here!C25|f05495`

- workbook: `all_data_912_v0.1/spreadsheet/58114/3_58114_input.xlsx`
- location: `Here!C25`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!C25="","",Sheet1!C25)`
- evidence: Referenced cell Sheet1!C25 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: A23: '=IF(Sheet1!A23="","",Sheet1!A23)' -> 22 | B23: '=IF(Sheet1!B23="","",Sheet1!B23)' -> 'HO10339330' | C23: '=IF(Sheet1!C23="","",Sheet1!C23)' -> None | D23: '=IF(Sheet1!D23="","",Sheet1!D23)' -> None | E23: '=IF(Sheet1!E23="","",Sheet1!E23)' -> None | A24: '=IF(Sheet1!A24="","",Sheet1!A24)' -> 23 | B24: '=IF(Sheet1!B24="","",Sheet1!B24)' -> 'RS31728184' | C24: '=IF(Sheet1!C24="","",Sheet1!C24)' -> None | D24: '=IF(Sheet1!D24="","",Sheet1!D24)' -> None | E24: '=IF(Sheet1!E24="","",Sheet1!E24)' -> None | A25: '=IF(Sheet1!A25="","",Sheet1!A25)' -> 24 | B25: '=IF(Sheet1!B25="","",Sheet1!B25)' -> 'SS43010028' | C25: '=IF(Sheet1!C25="","",Sheet1!C25)' -> None | D25: '=IF(Sheet1!D25="","",Sheet1!D25)' -> None | E25: '=IF(Sheet1!E25="","",Sheet1!E25)' -> None | A26: '=IF(Sheet1!A26="","",Sheet1!A26)' -> 25 | B26: '=IF(Sheet1!B26="","",Sheet1!B26)' -> 'TT33991592' | C26: '=IF(Sheet1!C26="","",Sheet1!C26)' -> None | D26: '=IF(Sheet1!D26="","",Sheet1!D26)' -> None | E26: '=IF(Sheet1!E26="","",Sheet1!E26)' -> None | A27: '=IF(Sheet1!A27="","",Sheet1!A27)' -> 26 | B27: '=IF(Sheet1!B27="","",Sheet1!B27)' -> 'CV22833553' | C27: '=IF(Sheet1!C27="","",Sheet1!C27)' -> None | D27: '=IF(Sheet1!D27="","",Sheet1!D27)' -> None | E27: '=IF(Sheet1!E27="","",Sheet1!E27)' -> None

### `e61cd08d6d5f|BLANK_PRECEDENT|Huff!H30|5c60d0`

- workbook: `all_data_912_v0.1/spreadsheet/49782/3_49782_input.xlsx`
- location: `Huff!H30`  severity: Medium  confidence: Review
- formula: `=(F30+G30)*(1-$C$8)`
- evidence: Referenced cell Huff!F30 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:M326
- neighbourhood: H28: '=(F28+G28)*(1-$C$8)' -> 0 | J28: '=SUM(F28:G28)-H28' -> 0 | H29: '=(F29+G29)*(1-$C$8)' -> 0 | J29: '=SUM(F29:G29)-H29' -> 0 | H30: '=(F30+G30)*(1-$C$8)' -> 0 | J30: '=SUM(F30:G30)-H30' -> 0 | H31: '=(F31+G31)*(1-$C$8)' -> 0 | J31: '=SUM(F31:G31)-H31' -> 0 | H32: '=(F32+G32)*(1-$C$8)' -> 0 | J32: '=SUM(F32:G32)-H32' -> 0

### `7dfe4964af12|BLANK_PRECEDENT|Sheet1!C9`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!C9`  severity: Medium  confidence: Review
- formula: `=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY11,0),""),"")`
- evidence: Referenced cell Sheet1!B9 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A9: 2023-11-20 00:00:00 | C9: '=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D9: '=IF(AND(B9>0,$AW11>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A10: 2023-11-27 00:00:00 | C10: '=IF(AND(B10>0,$AW12>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D10: '=IF(AND(B10>0,$AW12>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A11: 2023-12-04 00:00:00 | C11: '=IF(AND(B11>0,$AW13>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D11: '=IF(AND(B11>0,$AW13>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None

### `f5521bffa45f|BLANK_PRECEDENT|Sheet1!D160|94c23c`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D160`  severity: Medium  confidence: Review
- formula: `=IF(AND(A160=1,B160=C160),1,"")`
- evidence: Referenced cell Sheet1!C160 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:D302
- neighbourhood: D158: '=IF(AND(A158=1,B158=C158),1,"")' -> None | D159: '=IF(AND(A159=1,B159=C159),1,"")' -> None | D160: '=IF(AND(A160=1,B160=C160),1,"")' -> None | D161: '=IF(AND(A161=1,B161=C161),1,"")' -> None | D162: '=IF(AND(A162=1,B162=C162),1,"")' -> None

### `7dfe4964af12|BLANK_PRECEDENT|Sheet1!G14`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!G14`  severity: Medium  confidence: Review
- formula: `=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(E14/B14,""),"")`
- evidence: Referenced cell Sheet1!E14 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: F12: '=IF(AND(NOT(ISBLANK(E12)),B12>0,$AW14>0),IFERROR(E12/B12,""),"")' -> None | G12: '=IF(AND(NOT(ISBLANK(E12)),B12>0,$AW14>0),IFERROR(E12/B12,""),"")' -> None | H12: '=IF(AND(NOT(ISBLANK($N14)),$K14>0,$AW14>0),IFERROR(F12/D12,""),"")' -> None | I12: '=IF(MAX(G12,H12)=0,"",MAX(G12,H12))' -> None | F13: '=IF(AND(NOT(ISBLANK(E13)),B13>0,$AW15>0),IFERROR(E13/B13,""),"")' -> None | G13: '=IF(AND(NOT(ISBLANK(E13)),B13>0,$AW15>0),IFERROR(E13/B13,""),"")' -> None | H13: '=IF(AND(NOT(ISBLANK($N15)),$K15>0,$AW15>0),IFERROR(F13/D13,""),"")' -> None | I13: '=IF(MAX(G13,H13)=0,"",MAX(G13,H13))' -> None | F14: '=IF(AND(NOT(ISBLANK(E14)),B14>0,$AW16>0),IFERROR(E14/B14,""),"")' -> None | G14: '=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(E14/B14,""),"")' -> None | H14: '=IF(AND(NOT(ISBLANK($N16)),$K16>0,$AW16>0),IFERROR(F14/D14,""),"")' -> None | I14: '=IF(MAX(G14,H14)=0,"",MAX(G14,H14))' -> None

### `2b89f3e053b3|BLANK_PRECEDENT|Here!C24|3be594`

- workbook: `all_data_912_v0.1/spreadsheet/58147/2_58147_input.xlsx`
- location: `Here!C24`  severity: Medium  confidence: Review
- formula: `=IF(Sheet1!C24="","",Sheet1!C24)`
- evidence: Referenced cell Sheet1!C24 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: A22: '=IF(Sheet1!A22="","",Sheet1!A22)' -> 21 | B22: '=IF(Sheet1!B22="","",Sheet1!B22)' -> 'MM12168514' | C22: '=IF(Sheet1!C22="","",Sheet1!C22)' -> 'Tbnor' | D22: '=IF(Sheet1!D22="","",Sheet1!D22)' -> 'Cadigan' | E22: '=IF(Sheet1!E22="","",Sheet1!E22)' -> 'Tbnor, Cadigan' | A23: '=IF(Sheet1!A23="","",Sheet1!A23)' -> 22 | B23: '=IF(Sheet1!B23="","",Sheet1!B23)' -> 'HO10339330' | C23: '=IF(Sheet1!C23="","",Sheet1!C23)' -> None | D23: '=IF(Sheet1!D23="","",Sheet1!D23)' -> None | E23: '=IF(Sheet1!E23="","",Sheet1!E23)' -> None | A24: '=IF(Sheet1!A24="","",Sheet1!A24)' -> 23 | B24: '=IF(Sheet1!B24="","",Sheet1!B24)' -> 'RS31728184' | C24: '=IF(Sheet1!C24="","",Sheet1!C24)' -> None | D24: '=IF(Sheet1!D24="","",Sheet1!D24)' -> None | E24: '=IF(Sheet1!E24="","",Sheet1!E24)' -> None | A25: '=IF(Sheet1!A25="","",Sheet1!A25)' -> 24 | B25: '=IF(Sheet1!B25="","",Sheet1!B25)' -> 'SS43010028' | C25: '=IF(Sheet1!C25="","",Sheet1!C25)' -> None | D25: '=IF(Sheet1!D25="","",Sheet1!D25)' -> None | E25: '=IF(Sheet1!E25="","",Sheet1!E25)' -> None | A26: '=IF(Sheet1!A26="","",Sheet1!A26)' -> 25 | B26: '=IF(Sheet1!B26="","",Sheet1!B26)' -> 'TT33991592' | C26: '=IF(Sheet1!C26="","",Sheet1!C26)' -> None | D26: '=IF(Sheet1!D26="","",Sheet1!D26)' -> None | E26: '=IF(Sheet1!E26="","",Sheet1!E26)' -> None

### `4ea284d68c01|BLANK_PRECEDENT|Sheet1!K131|dd7850`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!K131`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(I130>=12,IF($J130<=100,0+SUBSTITUTE(IF($D131>=125,","&$D131,"")&IF($E131>=125,","&$E131,"")&IF($F131>=125,","&$F131,""),",","",1),""),""),"")`
- evidence: Referenced cell Sheet1!D131 is blank.
- cached value: None; row labels: []; column header: ''; used range: A1:CJ782
- neighbourhood: I129: '=COUNT(D129:F129)' -> 3 | J129: '=IF(I129=0,0,(ROUNDDOWN(H129/I129,0)))' -> 107 | K129: '=IFERROR(IF(I128>=12,IF($J128<=100,0+SUBSTITUTE(IF($D129>=125,","&... -> None | L129: '=IFERROR(IF(I128>=12,IF($J128<=120,0+SUBSTITUTE(IF($D129>=150,","&... -> None | M129: '=IFERROR(IF(I128>=12,IF($J128<=140,0+SUBSTITUTE(IF($D129>=175,","&... -> None | I130: '=COUNT(D129:F130)' -> 6 | J130: '=IF(I130=0,0,(ROUNDDOWN(H130/I130,0)))' -> 93 | K130: '=IFERROR(IF(I129>=12,IF($J129<=100,0+SUBSTITUTE(IF($D130>=125,","&... -> None | L130: '=IFERROR(IF(I129>=12,IF($J129<=120,0+SUBSTITUTE(IF($D130>=150,","&... -> None | M130: '=IFERROR(IF(I129>=12,IF($J129<=140,0+SUBSTITUTE(IF($D130>=175,","&... -> None | I131: '=COUNT(D129:F131)' -> 6 | J131: '=IF(I131=0,0,(ROUNDDOWN(H131/I131,0)))' -> 93 | K131: '=IFERROR(IF(I130>=12,IF($J130<=100,0+SUBSTITUTE(IF($D131>=125,","&... -> None | L131: '=IFERROR(IF(I130>=12,IF($J130<=120,0+SUBSTITUTE(IF($D131>=150,","&... -> None | M131: '=IFERROR(IF(I130>=12,IF($J130<=140,0+SUBSTITUTE(IF($D131>=175,","&... -> None | I132: '=COUNT(D129:F132)' -> 9 | J132: '=IF(I132=0,0,(ROUNDDOWN(H132/I132,0)))' -> 103 | K132: '=IFERROR(IF(I131>=12,IF($J131<=100,0+SUBSTITUTE(IF($D132>=125,","&... -> None | L132: '=IFERROR(IF(I131>=12,IF($J131<=120,0+SUBSTITUTE(IF($D132>=150,","&... -> None | M132: '=IFERROR(IF(I131>=12,IF($J131<=140,0+SUBSTITUTE(IF($D132>=175,","&... -> None | I133: '=COUNT(D129:F133)' -> 12 | J133: '=IF(I133=0,0,(ROUNDDOWN(H133/I133,0)))' -> 105 | K133: '=IFERROR(IF(I132>=12,IF($J132<=100,0+SUBSTITUTE(IF($D133>=125,","&... -> None | L133: '=IFERROR(IF(I132>=12,IF($J132<=120,0+SUBSTITUTE(IF($D133>=150,","&... -> None | M133: '=IFERROR(IF(I132>=12,IF($J132<=140,0+SUBSTITUTE(IF($D133>=175,","&... -> None

### `0bffec63dc84|BLANK_PRECEDENT|Purchases!F114|775426`

- workbook: `all_data_912_v0.1/spreadsheet/CF_3712/1_CF_3712_input.xlsx`
- location: `Purchases!F114`  severity: Medium  confidence: Review
- formula: `=(C114*E114)+D114`
- evidence: Referenced cell Purchases!C114 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:M441
- neighbourhood: F112: '=(C112*E112)+D112' -> 0 | H112: '=IF(ISBLANK(G112), "", G112 + 30)' -> None | F113: '=(C113*E113)+D113' -> 0 | H113: '=IF(ISBLANK(G113), "", G113 + 30)' -> None | F114: '=(C114*E114)+D114' -> 0 | H114: '=IF(ISBLANK(G114), "", G114 + 30)' -> None | F115: '=(C115*E115)+D115' -> 0 | H115: '=IF(ISBLANK(G115), "", G115 + 30)' -> None | F116: '=(C116*E116)+D116' -> 0 | H116: '=IF(ISBLANK(G116), "", G116 + 30)' -> None

### `4ce48011e366|BLANK_PRECEDENT|Sheet1!F8|09cfd9`

- workbook: `all_data_912_v0.1/spreadsheet/48643/2_48643_input.xlsx`
- location: `Sheet1!F8`  severity: Medium  confidence: Review
- formula: `=(1+C8)*B8`
- evidence: Referenced cell Sheet1!C8 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:H40
- neighbourhood: E6: '=B6*C6' -> 0 | F6: '=(1+C6)*B6' -> 0 | E7: '=B7*C7' -> 0 | F7: '=(1+C7)*B7' -> 0 | E8: '=B8*C8' -> 0 | F8: '=(1+C8)*B8' -> 0 | E9: '=B9*C9' -> 0 | F9: '=(1+C9)*B9' -> 0 | E10: '=B10*C10' -> 0 | F10: '=(1+C10)*B10' -> 0

### `f42d1d87f115|BLANK_PRECEDENT|Sheet1!U20|95dce9`

- workbook: `all_data_912_v0.1/spreadsheet/57262/1_57262_input.xlsx`
- location: `Sheet1!U20`  severity: Medium  confidence: Review
- formula: `=T20-S20-R20`
- evidence: Referenced cell Sheet1!S20 is blank.
- cached value: 0; row labels: []; column header: ''; used range: A1:Y25
- neighbourhood: U18: '=T18-S18-R18' -> 0 | U19: '=T19-S19-R19' -> 0 | U20: '=T20-S20-R20' -> 0 | U21: '=T21-S21-R21' -> 0 | U22: '=T22-S22-R22' -> 0

### `fdad7150c0c3|BLANK_PRECEDENT|2023!H53|1a7f35`

- workbook: `all_data_912_v0.1/spreadsheet/68-47/2_68-47_input.xlsx`
- location: `2023!H53`  severity: Medium  confidence: Review
- formula: `=D53-E53+F53-G53`
- evidence: Referenced cell 2023!F53 is blank.
- cached value: -149.5; row labels: ["'NAG/BR/23-49/3'", "'XXXXX'"]; column header: ''; used range: A1:N144
- neighbourhood: H51: '=D51-E51+F51-G51' -> 149.5 | I51: '=IF(C51="","",IF(COUNTIF(C51, "*AFS/FSTC"),"Corresponding Entry", ... -> None | J51: '=((COUNTIF(H:H,H51)-COUNTIF(H:H,-H51))>=COUNTIF($H$7:H51,H51))*ISN... -> 0 | H52: '=D52-E52+F52-G52' -> -6000 | I52: '=IF(C52="","",IF(COUNTIF(C52, "*AFS/FSTC"),"Corresponding Entry", ... -> None | J52: '=((COUNTIF(H:H,H52)-COUNTIF(H:H,-H52))>=COUNTIF($H$7:H52,H52))*ISN... -> 0 | H53: '=D53-E53+F53-G53' -> -149.5 | I53: '=IF(C53="","",IF(COUNTIF(C53, "*AFS/FSTC"),"Corresponding Entry", ... -> None | J53: '=((COUNTIF(H:H,H53)-COUNTIF(H:H,-H53))>=COUNTIF($H$7:H53,H53))*ISN... -> 0 | H54: '=D54-E54+F54-G54' -> -69971 | I54: '=IF(C54="","",IF(COUNTIF(C54, "*AFS/FSTC"),"Corresponding Entry", ... -> None | J54: '=((COUNTIF(H:H,H54)-COUNTIF(H:H,-H54))>=COUNTIF($H$7:H54,H54))*ISN... -> 0 | F55: 350 | H55: '=D55-E55+F55-G55' -> 0 | I55: '=IF(C55="","",IF(COUNTIF(C55, "*AFS/FSTC"),"Corresponding Entry", ... -> None | J55: '=((COUNTIF(H:H,H55)-COUNTIF(H:H,-H55))>=COUNTIF($H$7:H55,H55))*ISN... -> 0

### `8409a6c4a25c|BLANK_PRECEDENT|Sheet2!AD12|712597`

- workbook: `all_data_912_v0.1/spreadsheet/575-25/2_575-25_input.xlsx`
- location: `Sheet2!AD12`  severity: Medium  confidence: Review
- formula: `=MAX(D12,K12,S12,Y12)`
- evidence: Referenced cell Sheet2!K12 is blank.
- cached value: 2016-12-16 00:00:00; row labels: []; column header: ''; used range: A1:AH37
- neighbourhood: AD10: '=MAX(D10,K10,S10,Y10)' -> 2016-12-16 00:00:00 | AD11: '=MAX(D11,K11,S11,Y11)' -> 2016-12-16 00:00:00 | AD12: '=MAX(D12,K12,S12,Y12)' -> 2016-12-16 00:00:00 | AD13: '=MAX(D13,K13,S13,Y13)' -> 2016-12-16 00:00:00 | AD14: '=MAX(D14,K14,S14,Y14)' -> 2016-12-16 00:00:00

### `970db979d624|BLANK_PRECEDENT|formamspnc(7)!K11|396805`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!K11`  severity: Medium  confidence: Review
- formula: `=IF(AND(AE11=0,AF11=0,ISNUMBER(BI11)),2,IF(AND(ISNUMBER(SEARCH($F$3&$G$3&$H$3&$I$3&$J$3,AE11&AF11&AG11&AH11&AI11&AJ11&AK11&AL11&AM11&AN11)),OR(BH11="b",BH11="c",BH11="d",BH11=1)),1,IF(ISNUMBER(SEARCH($F$3&$G$3&$H$3&$I$3&$J$3,AE11&AF11&AG11&AH11&AI11&AJ11&AK11&AL11&AM11&AN11)),"D","")))`
- evidence: Referenced cell formamspnc (7)!I3 is blank.
- cached value: None; row labels: ["'13c/18c/20c/25c/28c/32c/34c/37c/41c/49c/58c/63c/69c(1 ex..."]; column header: ''; used range: A1:ED48610
- neighbourhood: I9: '=IF(AND(NOT(BH9=""),NOT(BH10=""),NOT(BH11="")),7,IF(AND(NOT(BH9=""... -> None | J9: '=IF(AND(OR(H9="h",AND(K9="d",L9="e"),AND(L9="e",M9="f"),AND(K9="d"... -> None | K9: '=IF(AND(AE9=0,AF9=0,ISNUMBER(BI9)),2,IF(AND(ISNUMBER(SEARCH($F$3&$... -> 'D' | L9: '=IF(ISNUMBER(SEARCH($AE$3&$AF$3&$AG$3&$AH$3&$AI$3,AE9&AF9&AG9&AH9&... -> None | M9: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE9&AF9&AG9&AH9&... -> None | I10: '=IF(AND(NOT(BH10=""),NOT(BH11=""),NOT(#REF!="")),7,IF(AND(NOT(BH10... -> '#REF!' | J10: '=IF(AND(OR(H10="h",AND(K10="d",L10="e"),AND(L10="e",M10="f"),AND(K... -> None | K10: '=IF(AND(AE10=0,AF10=0,ISNUMBER(BI10)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None | L10: '=IF(ISNUMBER(SEARCH($AE$3&$AF$3&$AG$3&$AH$3&$AI$3,AE10&AF10&AG10&A... -> 'E' | M10: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE10&AF10&AG10&A... -> None | I11: '=IF(AND(NOT(BH11=""),NOT(#REF!=""),NOT(#REF!="")),7,IF(AND(NOT(BH1... -> '#REF!' | J11: '=IF(AND(OR(H11="h",AND(K11="d",L11="e"),AND(L11="e",M11="f"),AND(K... -> None | K11: '=IF(AND(AE11=0,AF11=0,ISNUMBER(BI11)),2,IF(AND(ISNUMBER(SEARCH($F$... -> None | L11: '=IF(ISNUMBER(SEARCH($AE$3&$AF$3&$AG$3&$AH$3&$AI$3,AE11&AF11&AG11&A... -> 'E' | M11: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE11&AF11&AG11&A... -> None

## BROKEN_REFERENCE

### `32b3a786ec79|BROKEN_REFERENCE|Sheet1!V5`

- workbook: `all_data_912_v0.1/spreadsheet/33094/2_33094_input.xlsx`
- location: `Sheet1!V5`  severity: High  confidence: Review
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AA$4:AA$1000)`
- evidence: External workbook links are inventoried but not followed by default: [1]Sheet2!$A$4:$A$1000, [1]Sheet2!AA$4:AA$1000.
- cached value: 0; row labels: ["'Employee1'"]; column header: "'Wk10'"; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: T3: 2024-02-25 00:00:00 | U3: 2024-03-03 00:00:00 | V3: 2024-03-10 00:00:00 | W3: 2024-03-17 00:00:00 | X3: 2024-03-24 00:00:00 | T4: 'Wk8' | U4: 'Wk9' | V4: 'Wk10' | W4: 'Wk11' | X4: 'Wk12' | T5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!Y$4:Y$1000)' -> 0 | U5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!Z$4:Z$1000)' -> 0 | V5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AA$4:AA$1000)' -> 0 | W5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AB$4:AB$1000)' -> 0 | X5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AC$4:AC$1000)' -> 0 | T6: '=T5/$B$5' -> 0 | U6: '=U5/$B$5' -> 0 | V6: '=V5/$B$5' -> 0 | W6: '=W5/$B$5' -> 0 | X6: '=X5/$B$5' -> 0 | T7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Y$4:Y$1000)' -> 0 | U7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Z$4:Z$1000)' -> 0 | V7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AA$4:AA$1000)' -> 0 | W7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AB$4:AB$1000)' -> 0 | X7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AC$4:AC$1000)' -> 0

### `552f4c55b2df|BROKEN_REFERENCE|OrderSheetFinal!AD14`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!AD14`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B14,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: '[1]C6.2'!$B$57:$K$64.
- cached value: 0; row labels: ["'41 x 41 Slotted Back To Back Channel 1 Metres'", "'W3'"]; column header: ''; used range: A1:AS37
- neighbourhood: AB12: '=IFERROR(VLOOKUP(B12,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC12: "=IFERROR(VLOOKUP(B12,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD12: "=IFERROR(VLOOKUP(B12,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE12: '=IFERROR(VLOOKUP(B12,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF12: '=IFERROR(VLOOKUP(B12,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AB13: '=IFERROR(VLOOKUP(B13,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC13: "=IFERROR(VLOOKUP(B13,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD13: "=IFERROR(VLOOKUP(B13,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE13: '=IFERROR(VLOOKUP(B13,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF13: '=IFERROR(VLOOKUP(B13,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AB14: '=IFERROR(VLOOKUP(B14,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC14: "=IFERROR(VLOOKUP(B14,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD14: "=IFERROR(VLOOKUP(B14,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE14: '=IFERROR(VLOOKUP(B14,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF14: '=IFERROR(VLOOKUP(B14,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AB15: '=IFERROR(VLOOKUP(B15,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC15: "=IFERROR(VLOOKUP(B15,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD15: "=IFERROR(VLOOKUP(B15,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE15: '=IFERROR(VLOOKUP(B15,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF15: '=IFERROR(VLOOKUP(B15,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AB16: '=IFERROR(VLOOKUP(B16,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC16: "=IFERROR(VLOOKUP(B16,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD16: "=IFERROR(VLOOKUP(B16,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE16: '=IFERROR(VLOOKUP(B16,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF16: '=IFERROR(VLOOKUP(B16,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0

### `783ba9a086e8|BROKEN_REFERENCE|OrderSheetFinal!AE28`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!AE28`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B28,'[1]C7'!$B$55:$K$63,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: '[1]C7'!$B$55:$K$63.
- cached value: 0; row labels: ["'M10 x 40mm Set Bolts'", "'J2'"]; column header: ''; used range: A1:AS37
- neighbourhood: AC26: "=IFERROR(VLOOKUP(B26,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD26: "=IFERROR(VLOOKUP(B26,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE26: "=IFERROR(VLOOKUP(B26,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF26: "=IFERROR(VLOOKUP(B26,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 0 | AG26: "=IFERROR(VLOOKUP(B26,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AC27: "=IFERROR(VLOOKUP(B27,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD27: "=IFERROR(VLOOKUP(B27,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE27: "=IFERROR(VLOOKUP(B27,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF27: "=IFERROR(VLOOKUP(B27,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 2 | AG27: "=IFERROR(VLOOKUP(B27,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 2 | AC28: "=IFERROR(VLOOKUP(B28,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD28: "=IFERROR(VLOOKUP(B28,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE28: "=IFERROR(VLOOKUP(B28,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF28: "=IFERROR(VLOOKUP(B28,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 0 | AG28: "=IFERROR(VLOOKUP(B28,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AC29: "=IFERROR(VLOOKUP(B29,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD29: "=IFERROR(VLOOKUP(B29,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE29: "=IFERROR(VLOOKUP(B29,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 0 | AF29: "=IFERROR(VLOOKUP(B29,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 0 | AG29: "=IFERROR(VLOOKUP(B29,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0 | AC30: "=IFERROR(VLOOKUP(B30,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD30: "=IFERROR(VLOOKUP(B30,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE30: "=IFERROR(VLOOKUP(B30,'[1]C7'!$B$55:$K$63,10,FALSE),0)" -> 1 | AF30: "=IFERROR(VLOOKUP(B30,'[1]C9'!$B$54:$K$64,10,FALSE),0)" -> 0 | AG30: "=IFERROR(VLOOKUP(B30,'[1]C11'!$B$55:$K$67,10,FALSE),0)" -> 0

### `84b858fcb37f|BROKEN_REFERENCE|Sheet1!I20`

- workbook: `all_data_912_v0.1/spreadsheet/14240/1_14240_input.xlsx`
- location: `Sheet1!I20`  severity: High  confidence: Review
- formula: `=+[1]BA!$AF$43`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AF$43.
- cached value: 39783; row labels: ["'2Adults+1Child'"]; column header: ''; used range: A1:U75
- neighbourhood: G18: '=+[1]BA!$AF$23' -> 22446 | H18: '=+[1]BA!$AF$24' -> 25811 | I18: '=+[1]BA!$AF$25' -> 28392 | J18: '=+[1]BA!$AF$26' -> 34071 | K18: '=+[1]BA!$AF$27' -> 40885 | G19: '=+[1]BA!$AF$32' -> 26248 | H19: '=+[1]BA!$AF$33' -> 30186 | I19: '=+[1]BA!$AF$34' -> 34713 | J19: '=+[1]BA!$AF$35' -> 41655 | K19: '=+[1]BA!$AF$36' -> 49987 | G20: '=+[1]BA!$AF$41' -> 31288 | H20: '=+[1]BA!$AF$42' -> 35982 | I20: '=+[1]BA!$AF$43' -> 39783 | J20: '=+[1]BA!$AF$44' -> 47740 | K20: '=+[1]BA!$AF$45' -> 57288 | G21: '=+[1]BA!$AF$50' -> 38171 | H21: '=+[1]BA!$AF$51' -> 43897 | I21: '=+[1]BA!$AF$52' -> 48288 | J21: '=+[1]BA!$AF$53' -> 57946 | K21: '=+[1]BA!$AF$54' -> 69535 | G22: '=+[1]BA!$AF$59' -> 48685 | H22: '=+[1]BA!$AF$60' -> 55988 | I22: '=+[1]BA!$AF$61' -> 61588 | J22: '=+[1]BA!$AF$62' -> 73906 | K22: '=+[1]BA!$AF$63' -> 88687

### `552f4c55b2df|BROKEN_REFERENCE|OrderSheetFinal!AG10`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/2_566-40_input.xlsx`
- location: `Order Sheet Final!AG10`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B10,[1]C11!$B$55:$K$67,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: [1]C11!$B$55:$K$67.
- cached value: 0; row labels: ["'M10 Spring Nuts'", "'K4'"]; column header: ''; used range: A1:AS37
- neighbourhood: AE8: '=IFERROR(VLOOKUP(B8,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF8: '=IFERROR(VLOOKUP(B8,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 1 | AG8: '=IFERROR(VLOOKUP(B8,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH8: '=IFERROR(VLOOKUP(B8,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI8: "=IFERROR(VLOOKUP(B8,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AE9: '=IFERROR(VLOOKUP(B9,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF9: '=IFERROR(VLOOKUP(B9,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG9: '=IFERROR(VLOOKUP(B9,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH9: '=IFERROR(VLOOKUP(B9,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI9: "=IFERROR(VLOOKUP(B9,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AE10: '=IFERROR(VLOOKUP(B10,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF10: '=IFERROR(VLOOKUP(B10,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG10: '=IFERROR(VLOOKUP(B10,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH10: '=IFERROR(VLOOKUP(B10,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI10: "=IFERROR(VLOOKUP(B10,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AE11: '=IFERROR(VLOOKUP(B11,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF11: '=IFERROR(VLOOKUP(B11,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG11: '=IFERROR(VLOOKUP(B11,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH11: '=IFERROR(VLOOKUP(B11,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI11: "=IFERROR(VLOOKUP(B11,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0 | AE12: '=IFERROR(VLOOKUP(B12,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF12: '=IFERROR(VLOOKUP(B12,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG12: '=IFERROR(VLOOKUP(B12,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AH12: '=IFERROR(VLOOKUP(B12,[1]C12!$B$55:$K$64,10,FALSE),0)' -> 0 | AI12: "=IFERROR(VLOOKUP(B12,'[1]C14.1'!$B$55:$K$59,10,FALSE),0)" -> 0

### `7dfe4964af12|BROKEN_REFERENCE|Sheet1!C10`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!C10`  severity: High  confidence: Defect
- formula: `=IF(AND(B10>0,$AW12>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY12,0),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A9: 2023-11-20 00:00:00 | C9: '=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D9: '=IF(AND(B9>0,$AW11>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A10: 2023-11-27 00:00:00 | C10: '=IF(AND(B10>0,$AW12>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D10: '=IF(AND(B10>0,$AW12>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A11: 2023-12-04 00:00:00 | C11: '=IF(AND(B11>0,$AW13>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D11: '=IF(AND(B11>0,$AW13>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None | A12: 2023-12-11 00:00:00 | C12: '=IF(AND(B12>0,$AW14>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D12: '=IF(AND(B12>0,$AW14>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None

### `6741b8e20874|BROKEN_REFERENCE|OrderSheetFinal!AA10`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!AA10`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B10,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: '[1]C4.2'!$B$62:$K$75.
- cached value: 0; row labels: ["'M10 Spring Nuts'", "'K4'"]; column header: ''; used range: A1:AS37
- neighbourhood: Y8: '=IFERROR(VLOOKUP(B8,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z8: "=IFERROR(VLOOKUP(B8,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA8: "=IFERROR(VLOOKUP(B8,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB8: '=IFERROR(VLOOKUP(B8,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC8: "=IFERROR(VLOOKUP(B8,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | Y9: '=IFERROR(VLOOKUP(B9,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z9: "=IFERROR(VLOOKUP(B9,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA9: "=IFERROR(VLOOKUP(B9,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB9: '=IFERROR(VLOOKUP(B9,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC9: "=IFERROR(VLOOKUP(B9,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | Y10: '=IFERROR(VLOOKUP(B10,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z10: "=IFERROR(VLOOKUP(B10,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA10: "=IFERROR(VLOOKUP(B10,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB10: '=IFERROR(VLOOKUP(B10,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 1 | AC10: "=IFERROR(VLOOKUP(B10,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | Y11: '=IFERROR(VLOOKUP(B11,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z11: "=IFERROR(VLOOKUP(B11,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA11: "=IFERROR(VLOOKUP(B11,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB11: '=IFERROR(VLOOKUP(B11,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC11: "=IFERROR(VLOOKUP(B11,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | Y12: '=IFERROR(VLOOKUP(B12,[1]C3!$B$55:$K$61,10,FALSE),0)' -> 0 | Z12: "=IFERROR(VLOOKUP(B12,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA12: "=IFERROR(VLOOKUP(B12,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB12: '=IFERROR(VLOOKUP(B12,[1]C5!$B$57:$K$71,10,FALSE),0)' -> 0 | AC12: "=IFERROR(VLOOKUP(B12,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G17`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G17`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E15: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G15: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E16: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G16: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E17: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G17: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E18: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G18: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E19: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G19: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `050df5c328bc|BROKEN_REFERENCE|Sheet1!H35`

- workbook: `all_data_912_v0.1/spreadsheet/14240/3_14240_input.xlsx`
- location: `Sheet1!H35`  severity: High  confidence: Review
- formula: `=+[1]BA!$AI$15`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AI$15.
- cached value: 29500; row labels: ["'2Adults+4Children'"]; column header: ''; used range: A1:U75
- neighbourhood: F33: '=+[1]BA!$AH$49' -> 41823 | G33: '=+[1]BA!$AH$50' -> 49077 | H33: '=+[1]BA!$AH$51' -> 56439 | I33: '=+[1]BA!$AH$52' -> 62084 | J33: '=+[1]BA!$AH$53' -> 74502 | F34: '=+[1]BA!$AH$58' -> 53343 | G34: '=+[1]BA!$AH$59' -> 62595 | H34: '=+[1]BA!$AH$60' -> 71984 | I34: '=+[1]BA!$AH$61' -> 79184 | J34: '=+[1]BA!$AH$62' -> 95022 | F35: '=+[1]BA!$AI$13' -> 16758 | G35: '=+[1]BA!$AI$14' -> 25650 | H35: '=+[1]BA!$AI$15' -> 29500 | I35: '=+[1]BA!$AI$16' -> 32450 | J35: '=+[1]BA!$AI$17' -> 38940 | F36: '=+[1]BA!$AI$22' -> 20950 | G36: '=+[1]BA!$AI$23' -> 32065 | H36: '=+[1]BA!$AI$24' -> 36873 | I36: '=+[1]BA!$AI$25' -> 40560 | J36: '=+[1]BA!$AI$26' -> 48673 | F37: '=+[1]BA!$AI$31' -> 31248 | G37: '=+[1]BA!$AI$32' -> 37498 | H37: '=+[1]BA!$AI$33' -> 43123 | I37: '=+[1]BA!$AI$34' -> 49590 | J37: '=+[1]BA!$AI$35' -> 59508

### `84b858fcb37f|BROKEN_REFERENCE|Sheet1!F24`

- workbook: `all_data_912_v0.1/spreadsheet/14240/1_14240_input.xlsx`
- location: `Sheet1!F24`  severity: High  confidence: Review
- formula: `=+[1]BA!$AG$22`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AG$22.
- cached value: 16760; row labels: ["'2Adults+2Children'"]; column header: ''; used range: A1:U75
- neighbourhood: D22: '=+[1]BA!$AF$56' -> 19098 | E22: '=+[1]BA!$AF$57' -> 24941 | F22: '=+[1]BA!$AF$58' -> 41489 | G22: '=+[1]BA!$AF$59' -> 48685 | H22: '=+[1]BA!$AF$60' -> 55988 | D23: '=+[1]BA!$AG$11' -> 6566 | E23: '=+[1]BA!$AG$12' -> 8618 | F23: '=+[1]BA!$AG$13' -> 13406 | G23: '=+[1]BA!$AG$14' -> 20520 | H23: '=+[1]BA!$AG$15' -> 23600 | D24: '=+[1]BA!$AG$20' -> 8860 | E24: '=+[1]BA!$AG$21' -> 12130 | F24: '=+[1]BA!$AG$22' -> 16760 | G24: '=+[1]BA!$AG$23' -> 25652 | H24: '=+[1]BA!$AG$24' -> 29498 | D25: '=+[1]BA!$AG$29' -> 10260 | E25: '=+[1]BA!$AG$30' -> 15640 | F25: '=+[1]BA!$AG$31' -> 24998 | G25: '=+[1]BA!$AG$32' -> 29998 | H25: '=+[1]BA!$AG$33' -> 34498 | D26: '=+[1]BA!$AG$38' -> 12312 | E26: '=+[1]BA!$AG$39' -> 19152 | F26: '=+[1]BA!$AG$40' -> 30472 | G26: '=+[1]BA!$AG$41' -> 35758 | H26: '=+[1]BA!$AG$42' -> 41122

### `643562b8c3e5|BROKEN_REFERENCE|Sheet1!X7`

- workbook: `all_data_912_v0.1/spreadsheet/33094/1_33094_input.xlsx`
- location: `Sheet1!X7`  severity: High  confidence: Review
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AC$4:AC$1000)`
- evidence: External workbook links are inventoried but not followed by default: [1]Sheet2!$A$4:$A$1000, [1]Sheet2!AC$4:AC$1000.
- cached value: 0; row labels: ["'Employee2'"]; column header: ''; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: V5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AA$4:AA$1000)' -> 0 | W5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AB$4:AB$1000)' -> 0 | X5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AC$4:AC$1000)' -> 0 | Y5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AD$4:AD$1000)' -> 0 | Z5: '=SUM(C5:Y5)' -> 3.9 | V6: '=V5/$B$5' -> 0 | W6: '=W5/$B$5' -> 0 | X6: '=X5/$B$5' -> 0 | Y6: '=Y5/$B$5' -> 0 | V7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AA$4:AA$1000)' -> 0 | W7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AB$4:AB$1000)' -> 0 | X7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AC$4:AC$1000)' -> 0 | Y7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AD$4:AD$1000)' -> 0 | Z7: '=SUM(C7:Y7)' -> 92 | V8: '=V7/$B$7' -> 0 | W8: '=W7/$B$7' -> 0 | X8: '=X7/$B$7' -> 0 | Y8: '=Y7/$B$7' -> 0 | Z8: '=SUM(C8:Y8)' -> 2.3 | V9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AA$4:AA$1000)' -> 0 | W9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AB$4:AB$1000)' -> 0 | X9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AC$4:AC$1000)' -> 0 | Y9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AD$4:AD$1000)' -> 0 | Z9: '=SUM(C9:Y9)' -> 24

### `b230bc5037bf|BROKEN_REFERENCE|PrevworkingdayQuote(2)!A27|0dcee9`

- workbook: `all_data_912_v0.1/spreadsheet/47699/3_47699_input.xlsx`
- location: `Prev working day Quote (2)!A27`  severity: High  confidence: Defect
- formula: `=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:F27
- neighbourhood: A25: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B25: 'Oscar' | C25: 7 | A26: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B26: 'Oscar' | C26: 7 | A27: '=VLOOKUP(#REF!,[1]VA25N_Quote!D:L,9,FALSE)' -> '#REF!' | B27: 'Oscar' | C27: 7

### `ef479c030de6|BROKEN_REFERENCE|Sheet1!C8`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!C8`  severity: High  confidence: Defect
- formula: `=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY10,0),""),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A9: 2023-11-20 00:00:00 | C9: '=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D9: '=IF(AND(B9>0,$AW11>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A10: 2023-11-27 00:00:00 | C10: '=IF(AND(B10>0,$AW12>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$... -> None | D10: '=IF(AND(B10>0,$AW12>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$B... -> None

### `7bd972dd1e37|BROKEN_REFERENCE|July-KPIs!B34`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!B34`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A34),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A32: '=IF(ROWS(A$6:A32)>DAY(J$13),"",J$12+ROWS(A$6:A32)-1)' -> 2021-07-28 00:00:00 | B32: '=IFERROR(VLOOKUP(($C$1&"|"&A32),#REF!,2,0),"")' -> None | A33: '=IF(ROWS(A$6:A33)>DAY(J$13),"",J$12+ROWS(A$6:A33)-1)' -> 2021-07-29 00:00:00 | B33: '=IFERROR(VLOOKUP(($C$1&"|"&A33),#REF!,2,0),"")' -> None | A34: '=IF(ROWS(A$6:A34)>DAY(J$13),"",J$12+ROWS(A$6:A34)-1)' -> 2021-07-30 00:00:00 | B34: '=IFERROR(VLOOKUP(($C$1&"|"&A34),#REF!,2,0),"")' -> None | A35: '=IF(ROWS(A$6:A35)>DAY(J$13),"",J$12+ROWS(A$6:A35)-1)' -> 2021-07-31 00:00:00 | B35: '=IFERROR(VLOOKUP(($C$1&"|"&A35),#REF!,2,0),"")' -> None | A36: '=IF(ROWS(A$6:A36)>DAY(J$13),"",J$12+ROWS(A$6:A36)-1)' -> 2021-08-01 00:00:00 | B36: '=IFERROR(VLOOKUP(($C$1&"|"&A36),#REF!,2,0),"")' -> None

### `6c3f8788f84d|BROKEN_REFERENCE|Sheet1!E20`

- workbook: `all_data_912_v0.1/spreadsheet/14240/2_14240_input.xlsx`
- location: `Sheet1!E20`  severity: High  confidence: Review
- formula: `=+[1]BA!$AF$39`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AF$39.
- cached value: 16758; row labels: ["'2Adults+1Child'"]; column header: ''; used range: A1:U75
- neighbourhood: C18: '=+[1]BA!$AF$19' -> 5786 | D18: '=+[1]BA!$AF$20' -> 7753 | E18: '=+[1]BA!$AF$21' -> 10614 | F18: '=+[1]BA!$AF$22' -> 14665 | G18: '=+[1]BA!$AF$23' -> 22446 | C19: '=+[1]BA!$AF$28' -> 7581 | D19: '=+[1]BA!$AF$29' -> 8978 | E19: '=+[1]BA!$AF$30' -> 13685 | F19: '=+[1]BA!$AF$31' -> 21873 | G19: '=+[1]BA!$AF$32' -> 26248 | C20: '=+[1]BA!$AF$37' -> 9177 | D20: '=+[1]BA!$AF$38' -> 10773 | E20: '=+[1]BA!$AF$39' -> 16758 | F20: '=+[1]BA!$AF$40' -> 26663 | G20: '=+[1]BA!$AF$41' -> 31288 | C21: '=+[1]BA!$AF$46' -> 11704 | D21: '=+[1]BA!$AF$47' -> 15654 | E21: '=+[1]BA!$AF$48' -> 20445 | F21: '=+[1]BA!$AF$49' -> 32529 | G21: '=+[1]BA!$AF$50' -> 38171 | C22: '=+[1]BA!$AF$55' -> 14280 | D22: '=+[1]BA!$AF$56' -> 19098 | E22: '=+[1]BA!$AF$57' -> 24941 | F22: '=+[1]BA!$AF$58' -> 41489 | G22: '=+[1]BA!$AF$59' -> 48685

### `484f4df3fe7b|BROKEN_REFERENCE|Statistics!G46`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!G46`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G44: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G45: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G46: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G47: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G48: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `19ea38afb413|BROKEN_REFERENCE|Sheet1!F5`

- workbook: `all_data_912_v0.1/spreadsheet/33094/3_33094_input.xlsx`
- location: `Sheet1!F5`  severity: High  confidence: Review
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!K$4:K$1000)`
- evidence: External workbook links are inventoried but not followed by default: [1]Sheet2!$A$4:$A$1000, [1]Sheet2!K$4:K$1000.
- cached value: 0; row labels: ["'Employee1'"]; column header: "'Wk46'"; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: D3: 2023-11-05 00:00:00 | E3: 2023-11-12 00:00:00 | F3: 2023-11-19 00:00:00 | G3: 2023-11-26 00:00:00 | H3: 2023-12-03 00:00:00 | D4: 'Wk44' | E4: 'Wk45' | F4: 'Wk46' | G4: 'Wk47' | H4: 'Wk48' | D5: 1.3 | E5: 1.3 | F5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!K$4:K$1000)' -> 0 | G5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!L$4:L$1000)' -> 0 | H5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!M$4:M$1000)' -> 0 | D6: '=D5/$B$5' -> 0.065 | E6: '=E5/$B$5' -> 0.065 | F6: '=F5/$B$5' -> 0 | G6: '=G5/$B$5' -> 0 | H6: '=H5/$B$5' -> 0 | D7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!I$4:I$1000)' -> 0 | E7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!J$4:J$1000)' -> 0 | F7: 25 | G7: 25 | H7: 25

### `6c3f8788f84d|BROKEN_REFERENCE|Sheet1!D12`

- workbook: `all_data_912_v0.1/spreadsheet/14240/2_14240_input.xlsx`
- location: `Sheet1!D12`  severity: High  confidence: Review
- formula: `=+[1]BA!$AE$20`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AE$20.
- cached value: 6645; row labels: ["'2Adults'"]; column header: ''; used range: A1:U75
- neighbourhood: B10: 1000000 | C10: 8160 | D10: 10913 | E10: 14252 | F10: 23708 | B11: 200000 | C11: '=+[1]BA!$AE$10' -> 3507 | D11: '=+[1]BA!$AE$11' -> 4925 | E11: '=+[1]BA!$AE$12' -> 6464 | F11: '=+[1]BA!$AE$13' -> 10055 | B12: 300000 | C12: '=+[1]BA!$AE$19' -> 4959 | D12: '=+[1]BA!$AE$20' -> 6645 | E12: '=+[1]BA!$AE$21' -> 9098 | F12: '=+[1]BA!$AE$22' -> 12570 | B13: 400000 | C13: '=+[1]BA!$AE$28' -> 6498 | D13: '=+[1]BA!$AE$29' -> 7695 | E13: '=+[1]BA!$AE$30' -> 11730 | F13: '=+[1]BA!$AE$31' -> 18749 | B14: 500000 | C14: '=+[1]BA!$AE$37' -> 7866 | D14: '=+[1]BA!$AE$38' -> 9234 | E14: '=+[1]BA!$AE$39' -> 14364 | F14: '=+[1]BA!$AE$40' -> 22854

### `32b3a786ec79|BROKEN_REFERENCE|Sheet1!U7`

- workbook: `all_data_912_v0.1/spreadsheet/33094/2_33094_input.xlsx`
- location: `Sheet1!U7`  severity: High  confidence: Review
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Z$4:Z$1000)`
- evidence: External workbook links are inventoried but not followed by default: [1]Sheet2!$A$4:$A$1000, [1]Sheet2!Z$4:Z$1000.
- cached value: 0; row labels: ["'Employee2'"]; column header: ''; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: S5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!X$4:X$1000)' -> 0 | T5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!Y$4:Y$1000)' -> 0 | U5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!Z$4:Z$1000)' -> 0 | V5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AA$4:AA$1000)' -> 0 | W5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!AB$4:AB$1000)' -> 0 | S6: '=S5/$B$5' -> 0 | T6: '=T5/$B$5' -> 0 | U6: '=U5/$B$5' -> 0 | V6: '=V5/$B$5' -> 0 | W6: '=W5/$B$5' -> 0 | S7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!X$4:X$1000)' -> 0 | T7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Y$4:Y$1000)' -> 0 | U7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Z$4:Z$1000)' -> 0 | V7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AA$4:AA$1000)' -> 0 | W7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!AB$4:AB$1000)' -> 0 | S8: '=S7/$B$7' -> 0 | T8: '=T7/$B$7' -> 0 | U8: '=U7/$B$7' -> 0 | V8: '=V7/$B$7' -> 0 | W8: '=W7/$B$7' -> 0 | S9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!X$4:X$1000)' -> 0 | T9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!Y$4:Y$1000)' -> 0 | U9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!Z$4:Z$1000)' -> 0 | V9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AA$4:AA$1000)' -> 0 | W9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!AB$4:AB$1000)' -> 0

### `6741b8e20874|BROKEN_REFERENCE|OrderSheetFinal!AE7`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/1_566-40_input.xlsx`
- location: `Order Sheet Final!AE7`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B7,[1]C7!$B$55:$K$63,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: [1]C7!$B$55:$K$63.
- cached value: 2; row labels: ["'M10 Square Washers'", "'P1'"]; column header: ''; used range: A1:AS37
- neighbourhood: AC5: 'C6.1' | AD5: 'C6.2' | AE5: 'C7' | AF5: 'C9' | AG5: 'C11' | AC6: "=IFERROR(VLOOKUP(B6,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD6: "=IFERROR(VLOOKUP(B6,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE6: '=IFERROR(VLOOKUP(B6,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF6: '=IFERROR(VLOOKUP(B6,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 1 | AG6: '=IFERROR(VLOOKUP(B6,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AC7: "=IFERROR(VLOOKUP(B7,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD7: "=IFERROR(VLOOKUP(B7,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE7: '=IFERROR(VLOOKUP(B7,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 2 | AF7: '=IFERROR(VLOOKUP(B7,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG7: '=IFERROR(VLOOKUP(B7,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AC8: "=IFERROR(VLOOKUP(B8,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD8: "=IFERROR(VLOOKUP(B8,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE8: '=IFERROR(VLOOKUP(B8,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF8: '=IFERROR(VLOOKUP(B8,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 1 | AG8: '=IFERROR(VLOOKUP(B8,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0 | AC9: "=IFERROR(VLOOKUP(B9,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD9: "=IFERROR(VLOOKUP(B9,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | AE9: '=IFERROR(VLOOKUP(B9,[1]C7!$B$55:$K$63,10,FALSE),0)' -> 0 | AF9: '=IFERROR(VLOOKUP(B9,[1]C9!$B$54:$K$64,10,FALSE),0)' -> 0 | AG9: '=IFERROR(VLOOKUP(B9,[1]C11!$B$55:$K$67,10,FALSE),0)' -> 0

### `050df5c328bc|BROKEN_REFERENCE|Sheet1!I12`

- workbook: `all_data_912_v0.1/spreadsheet/14240/3_14240_input.xlsx`
- location: `Sheet1!I12`  severity: High  confidence: Review
- formula: `=+[1]BA!$AE$25`
- evidence: External workbook links are inventoried but not followed by default: [1]BA!$AE$25.
- cached value: 24336; row labels: ["'2Adults'"]; column header: ''; used range: A1:U75
- neighbourhood: G10: 27820 | H10: 31993 | I10: 35193 | J10: 42232 | K10: 50678 | G11: '=+[1]BA!$AE$14' -> 15390 | H11: '=+[1]BA!$AE$15' -> 17700 | I11: '=+[1]BA!$AE$16' -> 19470 | J11: '=+[1]BA!$AE$17' -> 23364 | K11: '=+[1]BA!$AE$18' -> 28038 | G12: '=+[1]BA!$AE$23' -> 19239 | H12: '=+[1]BA!$AE$24' -> 22124 | I12: '=+[1]BA!$AE$25' -> 24336 | J12: '=+[1]BA!$AE$26' -> 29204 | K12: '=+[1]BA!$AE$27' -> 35045 | G13: '=+[1]BA!$AE$32' -> 22499 | H13: '=+[1]BA!$AE$33' -> 25874 | I13: '=+[1]BA!$AE$34' -> 29754 | J13: '=+[1]BA!$AE$35' -> 35705 | K13: '=+[1]BA!$AE$36' -> 42846 | G14: '=+[1]BA!$AE$41' -> 26819 | H14: '=+[1]BA!$AE$42' -> 30842 | I14: '=+[1]BA!$AE$43' -> 34100 | J14: '=+[1]BA!$AE$44' -> 40920 | K14: '=+[1]BA!$AE$45' -> 49104

### `7bd972dd1e37|BROKEN_REFERENCE|July-KPIs!B31`

- workbook: `all_data_912_v0.1/spreadsheet/1726/2_1726_input.xlsx`
- location: `July-KPIs!B31`  severity: High  confidence: Defect
- formula: `=IFERROR(VLOOKUP(($C$1&"|"&A31),#REF!,2,0),"")`
- evidence: Formula text contains #REF!.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A29: '=IF(ROWS(A$6:A29)>DAY(J$13),"",J$12+ROWS(A$6:A29)-1)' -> 2021-07-25 00:00:00 | B29: '=IFERROR(VLOOKUP(($C$1&"|"&A29),#REF!,2,0),"")' -> None | A30: '=IF(ROWS(A$6:A30)>DAY(J$13),"",J$12+ROWS(A$6:A30)-1)' -> 2021-07-26 00:00:00 | B30: '=IFERROR(VLOOKUP(($C$1&"|"&A30),#REF!,2,0),"")' -> None | A31: '=IF(ROWS(A$6:A31)>DAY(J$13),"",J$12+ROWS(A$6:A31)-1)' -> 2021-07-27 00:00:00 | B31: '=IFERROR(VLOOKUP(($C$1&"|"&A31),#REF!,2,0),"")' -> None | A32: '=IF(ROWS(A$6:A32)>DAY(J$13),"",J$12+ROWS(A$6:A32)-1)' -> 2021-07-28 00:00:00 | B32: '=IFERROR(VLOOKUP(($C$1&"|"&A32),#REF!,2,0),"")' -> None | A33: '=IF(ROWS(A$6:A33)>DAY(J$13),"",J$12+ROWS(A$6:A33)-1)' -> 2021-07-29 00:00:00 | B33: '=IFERROR(VLOOKUP(($C$1&"|"&A33),#REF!,2,0),"")' -> None

### `783ba9a086e8|BROKEN_REFERENCE|OrderSheetFinal!AB29`

- workbook: `all_data_912_v0.1/spreadsheet/566-40/3_566-40_input.xlsx`
- location: `Order Sheet Final!AB29`  severity: High  confidence: Review
- formula: `=IFERROR(VLOOKUP(B29,'[1]C5'!$B$57:$K$71,10,FALSE),0)`
- evidence: External workbook links are inventoried but not followed by default: '[1]C5'!$B$57:$K$71.
- cached value: 0; row labels: ["'M10 x 65mm Coach Screws'", "'J2'"]; column header: ''; used range: A1:AS37
- neighbourhood: Z27: "=IFERROR(VLOOKUP(B27,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA27: "=IFERROR(VLOOKUP(B27,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB27: "=IFERROR(VLOOKUP(B27,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 2 | AC27: "=IFERROR(VLOOKUP(B27,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD27: "=IFERROR(VLOOKUP(B27,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z28: "=IFERROR(VLOOKUP(B28,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA28: "=IFERROR(VLOOKUP(B28,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB28: "=IFERROR(VLOOKUP(B28,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 0 | AC28: "=IFERROR(VLOOKUP(B28,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD28: "=IFERROR(VLOOKUP(B28,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z29: "=IFERROR(VLOOKUP(B29,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA29: "=IFERROR(VLOOKUP(B29,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB29: "=IFERROR(VLOOKUP(B29,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 0 | AC29: "=IFERROR(VLOOKUP(B29,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD29: "=IFERROR(VLOOKUP(B29,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z30: "=IFERROR(VLOOKUP(B30,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA30: "=IFERROR(VLOOKUP(B30,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB30: "=IFERROR(VLOOKUP(B30,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 1 | AC30: "=IFERROR(VLOOKUP(B30,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD30: "=IFERROR(VLOOKUP(B30,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0 | Z31: "=IFERROR(VLOOKUP(B31,'[1]C4.1'!$B$59:$K$72,10,FALSE),0)" -> 0 | AA31: "=IFERROR(VLOOKUP(B31,'[1]C4.2'!$B$62:$K$75,10,FALSE),0)" -> 0 | AB31: "=IFERROR(VLOOKUP(B31,'[1]C5'!$B$57:$K$71,10,FALSE),0)" -> 0 | AC31: "=IFERROR(VLOOKUP(B31,'[1]C6.1'!$B$57:$K$70,10,FALSE),0)" -> 0 | AD31: "=IFERROR(VLOOKUP(B31,'[1]C6.2'!$B$57:$K$64,10,FALSE),0)" -> 0

### `19ea38afb413|BROKEN_REFERENCE|Sheet1!N7`

- workbook: `all_data_912_v0.1/spreadsheet/33094/3_33094_input.xlsx`
- location: `Sheet1!N7`  severity: High  confidence: Review
- formula: `=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!S$4:S$1000)`
- evidence: External workbook links are inventoried but not followed by default: [1]Sheet2!$A$4:$A$1000, [1]Sheet2!S$4:S$1000.
- cached value: 0; row labels: ["'Employee2'"]; column header: ''; used range: A1:Z10
- range Sheet2!$A$4:$A$1000: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'A3: None', 'below': 'A1001: None'}
- neighbourhood: L5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!Q$4:Q$1000)' -> 0 | M5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!R$4:R$1000)' -> 0 | N5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!S$4:S$1000)' -> 0 | O5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!T$4:T$1000)' -> 0 | P5: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A5,[1]Sheet2!U$4:U$1000)' -> 0 | L6: '=L5/$B$5' -> 0 | M6: '=M5/$B$5' -> 0 | N6: '=N5/$B$5' -> 0 | O6: '=O5/$B$5' -> 0 | P6: '=P5/$B$5' -> 0 | L7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!Q$4:Q$1000)' -> 0 | M7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!R$4:R$1000)' -> 0 | N7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!S$4:S$1000)' -> 0 | O7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!T$4:T$1000)' -> 0 | P7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!U$4:U$1000)' -> 0 | L8: '=L7/$B$7' -> 0 | M8: '=M7/$B$7' -> 0 | N8: '=N7/$B$7' -> 0 | O8: '=O7/$B$7' -> 0 | P8: '=P7/$B$7' -> 0 | L9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!Q$4:Q$1000)' -> 0 | M9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!R$4:R$1000)' -> 0 | N9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!S$4:S$1000)' -> 0 | O9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!T$4:T$1000)' -> 0 | P9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!U$4:U$1000)' -> 0

### `37d41403fe20|BROKEN_REFERENCE|Statistics!G15`

- workbook: `all_data_912_v0.1/spreadsheet/55572/1_55572_input.xlsx`
- location: `Statistics!G15`  severity: High  confidence: Defect
- formula: `=COUNTIF(#REF!,Statistics!$A$3)`
- evidence: Formula text contains #REF!.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E13: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G13: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E14: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G14: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E15: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G15: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E16: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G16: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E17: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G17: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

## CIRCULAR_REFERENCE

### `d4944e722073|CIRCULAR_REFERENCE|Sheet1!AA7`

- workbook: `all_data_912_v0.1/spreadsheet/45581/3_45581_input.xlsx`
- location: `Sheet1!AA7`  severity: High  confidence: Likely defect
- evidence: Sheet1!AA7 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF9
- neighbourhood: Y7: '=IFERROR(MID($B5,COLUMNS($D7:Y7),1),"")' -> None | Z7: '=IFERROR(MID($B5,COLUMNS($D7:Z7),1),"")' -> None | AA7: '=IFERROR(MID($B5,COLUMNS($D7:AA7),1),"")' -> None | AB7: '=IFERROR(MID($B5,COLUMNS($D7:AB7),1),"")' -> None | AC7: '=IFERROR(MID($B5,COLUMNS($D7:AC7),1),"")' -> None | Y9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Y)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | Z9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Z)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | AA9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AA)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AB9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AB)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AC9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AC)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None

### `5d8557dfb652|CIRCULAR_REFERENCE|July-KPIs!A8`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!A8`  severity: High  confidence: Likely defect
- evidence: July-KPIs!A8 depends on itself, for example a total whose range includes the total cell.
- cached value: 2021-07-06 00:00:00; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A6: '=IF(ROWS(A$6:A6)>DAY(J$13),"",J$12+ROWS(A$6:A6)-1)' -> 2021-07-04 00:00:00 | B6: '=IFERROR(VLOOKUP(($C$1&"|"&A6),#REF!,2,0),"")' -> None | A7: '=IF(ROWS(A$6:A7)>DAY(J$13),"",J$12+ROWS(A$6:A7)-1)' -> 2021-07-05 00:00:00 | B7: '=IFERROR(VLOOKUP(($C$1&"|"&A7),#REF!,2,0),"")' -> None | A8: '=IF(ROWS(A$6:A8)>DAY(J$13),"",J$12+ROWS(A$6:A8)-1)' -> 2021-07-06 00:00:00 | B8: '=IFERROR(VLOOKUP(($C$1&"|"&A8),#REF!,2,0),"")' -> None | A9: '=IF(ROWS(A$6:A9)>DAY(J$13),"",J$12+ROWS(A$6:A9)-1)' -> 2021-07-07 00:00:00 | B9: '=IFERROR(VLOOKUP(($C$1&"|"&A9),#REF!,2,0),"")' -> None | A10: '=IF(ROWS(A$6:A10)>DAY(J$13),"",J$12+ROWS(A$6:A10)-1)' -> 2021-07-08 00:00:00 | B10: '=IFERROR(VLOOKUP(($C$1&"|"&A10),#REF!,2,0),"")' -> None

### `64aece717e7d|CIRCULAR_REFERENCE|Sheet2!F37`

- workbook: `all_data_912_v0.1/spreadsheet/52640/2_52640_input.xlsx`
- location: `Sheet2!F37`  severity: High  confidence: Likely defect
- evidence: Sheet2!F37 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: D35: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E35: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F35: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G35: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H35: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D36: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E36: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F36: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G36: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H36: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None

### `d4944e722073|CIRCULAR_REFERENCE|Sheet1!AC7`

- workbook: `all_data_912_v0.1/spreadsheet/45581/3_45581_input.xlsx`
- location: `Sheet1!AC7`  severity: High  confidence: Likely defect
- evidence: Sheet1!AC7 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF9
- neighbourhood: AA7: '=IFERROR(MID($B5,COLUMNS($D7:AA7),1),"")' -> None | AB7: '=IFERROR(MID($B5,COLUMNS($D7:AB7),1),"")' -> None | AC7: '=IFERROR(MID($B5,COLUMNS($D7:AC7),1),"")' -> None | AD7: '=IFERROR(MID($B5,COLUMNS($D7:AD7),1),"")' -> None | AA9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AA)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AB9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AB)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AC9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AC)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AD9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AD)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AE9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AE)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> 'd'

### `484f4df3fe7b|CIRCULAR_REFERENCE|Statistics!C46`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!C46`  severity: High  confidence: Likely defect
- evidence: Statistics!C46 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: B44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E45: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E46: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E47: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E48: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None

### `ad194e63840c|CIRCULAR_REFERENCE|Edit!D16`

- workbook: `all_data_912_v0.1/spreadsheet/49667/2_49667_input.xlsx`
- location: `Edit!D16`  severity: High  confidence: Likely defect
- evidence: Edit!D16 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: ["'Name 15'"]; column header: ''; used range: A1:AT16
- neighbourhood: B14: 10:30:00 | C14: 10:30:00 | D14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:00:00 | E14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:15:00 | D15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | E15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | D16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | E16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | F16: 'x'

### `b569de1c5256|CIRCULAR_REFERENCE|Sheet2!C11`

- workbook: `all_data_912_v0.1/spreadsheet/52640/1_52640_input.xlsx`
- location: `Sheet2!C11`  severity: High  confidence: Likely defect
- evidence: Sheet2!C11 depends on itself, for example a total whose range includes the total cell.
- cached value: 2; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: A9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201530 | B9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | D9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 4 | E9: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 'First Years Childcare Ltd' | A10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201549 | B10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1 | D10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1 | E10: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 'Cherry Red Records LTD' | A11: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201965 | B11: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C11: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 2 | D11: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 2 | E11: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 'D&D London Ltd.' | A12: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201636 | B12: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C12: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 3 | D12: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 5 | E12: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 'STERLING WINSHAW SOLICITOR... | A13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201654 | B13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1 | D13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 5 | E13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 'STERLING WINSHAW SOLICITOR...

### `a7b0a8a7bf55|CIRCULAR_REFERENCE|Sheet1!A19`

- workbook: `all_data_912_v0.1/spreadsheet/43406/2_43406_input.xlsx`
- location: `Sheet1!A19`  severity: High  confidence: Likely defect
- evidence: Sheet1!A19 depends on itself, for example a total whose range includes the total cell.
- cached value: 13; row labels: []; column header: ''; used range: A1:F20
- neighbourhood: A17: '=ROW(A17)-6' -> 11 | A18: '=ROW(A18)-6' -> 12 | A19: '=ROW(A19)-6' -> 13 | A20: '=ROW(A20)-6' -> 14

### `484f4df3fe7b|CIRCULAR_REFERENCE|Statistics!C42`

- workbook: `all_data_912_v0.1/spreadsheet/55572/2_55572_input.xlsx`
- location: `Statistics!C42`  severity: High  confidence: Likely defect
- evidence: Statistics!C42 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: B40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E42: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E43: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E44: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None

### `5d8557dfb652|CIRCULAR_REFERENCE|July-KPIs!A32`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!A32`  severity: High  confidence: Likely defect
- evidence: July-KPIs!A32 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A30: '=IF(ROWS(A$6:A30)>DAY(J$13),"",J$12+ROWS(A$6:A30)-1)' -> None | B30: '=IFERROR(VLOOKUP(($C$1&"|"&A30),#REF!,2,0),"")' -> None | A31: '=IF(ROWS(A$6:A31)>DAY(J$13),"",J$12+ROWS(A$6:A31)-1)' -> None | B31: '=IFERROR(VLOOKUP(($C$1&"|"&A31),#REF!,2,0),"")' -> None | A32: '=IF(ROWS(A$6:A32)>DAY(J$13),"",J$12+ROWS(A$6:A32)-1)' -> None | B32: '=IFERROR(VLOOKUP(($C$1&"|"&A32),#REF!,2,0),"")' -> None | A33: '=IF(ROWS(A$6:A33)>DAY(J$13),"",J$12+ROWS(A$6:A33)-1)' -> None | B33: '=IFERROR(VLOOKUP(($C$1&"|"&A33),#REF!,2,0),"")' -> None | A34: '=IF(ROWS(A$6:A34)>DAY(J$13),"",J$12+ROWS(A$6:A34)-1)' -> None | B34: '=IFERROR(VLOOKUP(($C$1&"|"&A34),#REF!,2,0),"")' -> None

### `5d1887987f48|CIRCULAR_REFERENCE|Sheet2!A15`

- workbook: `all_data_912_v0.1/spreadsheet/52640/3_52640_input.xlsx`
- location: `Sheet2!A15`  severity: High  confidence: Likely defect
- evidence: Sheet2!A15 depends on itself, for example a total whose range includes the total cell.
- cached value: 201968; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: A13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201654 | B13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C13: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 1 | A14: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201958 | B14: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C14: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 2 | A15: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201968 | B15: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C15: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 6 | A16: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 201972 | B16: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C16: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> 9

### `acb548947286|CIRCULAR_REFERENCE|Statistics!C26`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!C26`  severity: High  confidence: Likely defect
- evidence: Statistics!C26 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: B24: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C24: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D24: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E24: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B25: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C25: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D25: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E25: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B26: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C26: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D26: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E26: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B27: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C27: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D27: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E27: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E28: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None

### `acb548947286|CIRCULAR_REFERENCE|Statistics!C36`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!C36`  severity: High  confidence: Likely defect
- evidence: Statistics!C36 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: B34: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C34: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D34: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E34: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B35: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C35: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D35: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E35: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B36: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C36: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D36: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E36: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | B38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | C38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | D38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | E38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None

### `69b62f583cbe|CIRCULAR_REFERENCE|Edit!D13`

- workbook: `all_data_912_v0.1/spreadsheet/49667/3_49667_input.xlsx`
- location: `Edit!D13`  severity: High  confidence: Likely defect
- evidence: Edit!D13 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: ["'Name 12'"]; column header: ''; used range: A1:AT16
- neighbourhood: D11: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F11:$AT11,_xlpm.z,FREQUENCY... -> None | E11: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F11:$AT11,_xlpm.z,FREQUENCY... -> None | D12: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F12:$AT12,_xlpm.z,FREQUENCY... -> None | E12: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F12:$AT12,_xlpm.z,FREQUENCY... -> None | D13: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F13:$AT13,_xlpm.z,FREQUENCY... -> None | E13: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F13:$AT13,_xlpm.z,FREQUENCY... -> None | B14: 10:30:00 | C14: 10:30:00 | D14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:00:00 | E14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:15:00 | D15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | E15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None

### `ca01aea20178|CIRCULAR_REFERENCE|PrintFile!B16`

- workbook: `all_data_912_v0.1/spreadsheet/444-14/3_444-14_input.xlsx`
- location: `Print File!B16`  severity: High  confidence: Likely defect
- evidence: Print File!B16 depends on itself, for example a total whose range includes the total cell.
- cached value: 'A-10'; row labels: []; column header: ''; used range: A1:G42
- neighbourhood: A14: '=IF(ROWS($A$6:A14)>$B$4,"",INDEX(Data!$C$2:$C$144,SMALL(IF(Data!$B... -> 134 | B14: '=IF(ROWS($B$6:B14)>$B$4,"",INDEX(Data!$A$2:$A$144,SMALL(IF(Data!$B... -> 'A-04' | D14: 'A-07' | A15: '=IF(ROWS($A$6:A15)>$B$4,"",INDEX(Data!$C$2:$C$144,SMALL(IF(Data!$B... -> 136 | B15: '=IF(ROWS($B$6:B15)>$B$4,"",INDEX(Data!$A$2:$A$144,SMALL(IF(Data!$B... -> 'A-07' | D15: 'A-07' | A16: '=IF(ROWS($A$6:A16)>$B$4,"",INDEX(Data!$C$2:$C$144,SMALL(IF(Data!$B... -> 137 | B16: '=IF(ROWS($B$6:B16)>$B$4,"",INDEX(Data!$A$2:$A$144,SMALL(IF(Data!$B... -> 'A-10' | D16: 'A-08' | A17: '=IF(ROWS($A$6:A17)>$B$4,"",INDEX(Data!$C$2:$C$144,SMALL(IF(Data!$B... -> 139 | B17: '=IF(ROWS($B$6:B17)>$B$4,"",INDEX(Data!$A$2:$A$144,SMALL(IF(Data!$B... -> 'A-13' | D17: 'A-09' | A18: '=IF(ROWS($A$6:A18)>$B$4,"",INDEX(Data!$C$2:$C$144,SMALL(IF(Data!$B... -> 140 | B18: '=IF(ROWS($B$6:B18)>$B$4,"",INDEX(Data!$A$2:$A$144,SMALL(IF(Data!$B... -> 'B-03' | D18: 'A-10'

### `8734ff2c3db4|CIRCULAR_REFERENCE|Sheet1!B29`

- workbook: `all_data_912_v0.1/spreadsheet/50631/1_50631_input.xlsx`
- location: `Sheet1!B29`  severity: High  confidence: Likely defect
- evidence: Sheet1!B29 depends on itself, for example a total whose range includes the total cell.
- cached value: 2021-09-23 00:00:00; row labels: []; column header: ''; used range: A1:J38
- neighbourhood: B27: '=IF($B$3+ROWS($B$7:$B27)-1<=$F$3,$B$3+ROWS($B$7:$B27)-1,"")' -> 2021-09-21 00:00:00 | D27: '=IF($B$3+ROWS($B$7:$D58)-1<=$F$3,$B$3+ROWS($B$7:$D58)-1,"")' -> 2021-10-22 00:00:00 | B28: '=IF($B$3+ROWS($B$7:$B28)-1<=$F$3,$B$3+ROWS($B$7:$B28)-1,"")' -> 2021-09-22 00:00:00 | D28: '=IF($B$3+ROWS($B$7:$D59)-1<=$F$3,$B$3+ROWS($B$7:$D59)-1,"")' -> 2021-10-23 00:00:00 | B29: '=IF($B$3+ROWS($B$7:$B29)-1<=$F$3,$B$3+ROWS($B$7:$B29)-1,"")' -> 2021-09-23 00:00:00 | D29: '=IF($B$3+ROWS($B$7:$D60)-1<=$F$3,$B$3+ROWS($B$7:$D60)-1,"")' -> 2021-10-24 00:00:00 | B30: '=IF($B$3+ROWS($B$7:$B30)-1<=$F$3,$B$3+ROWS($B$7:$B30)-1,"")' -> 2021-09-24 00:00:00 | D30: '=IF($B$3+ROWS($B$7:$D61)-1<=$F$3,$B$3+ROWS($B$7:$D61)-1,"")' -> 2021-10-25 00:00:00 | B31: '=IF($B$3+ROWS($B$7:$B31)-1<=$F$3,$B$3+ROWS($B$7:$B31)-1,"")' -> 2021-09-25 00:00:00 | D31: '=IF($B$3+ROWS($B$7:$D62)-1<=$F$3,$B$3+ROWS($B$7:$D62)-1,"")' -> 2021-10-26 00:00:00

### `34d406898185|CIRCULAR_REFERENCE|Sheet1!Y9`

- workbook: `all_data_912_v0.1/spreadsheet/45581/2_45581_input.xlsx`
- location: `Sheet1!Y9`  severity: High  confidence: Likely defect
- evidence: Sheet1!Y9 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:AF9
- neighbourhood: W7: '=IFERROR(MID($B5,COLUMNS($D7:W7),1),"")' -> None | X7: '=IFERROR(MID($B5,COLUMNS($D7:X7),1),"")' -> None | Y7: '=IFERROR(MID($B5,COLUMNS($D7:Y7),1),"")' -> None | Z7: '=IFERROR(MID($B5,COLUMNS($D7:Z7),1),"")' -> None | AA7: '=IFERROR(MID($B5,COLUMNS($D7:AA7),1),"")' -> None | W9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:W)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | X9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:X)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | Y9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Y)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | Z9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Z)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | AA9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AA)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None

### `5d1887987f48|CIRCULAR_REFERENCE|Sheet2!E43`

- workbook: `all_data_912_v0.1/spreadsheet/52640/3_52640_input.xlsx`
- location: `Sheet2!E43`  severity: High  confidence: Likely defect
- evidence: Sheet2!E43 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: C41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C42: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D42: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E42: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F42: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G42: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C43: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D43: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E43: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F43: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G43: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C44: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D44: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E44: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F44: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G44: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C45: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D45: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E45: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F45: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G45: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None

### `6d5548493a93|CIRCULAR_REFERENCE|July-KPIs!A30`

- workbook: `all_data_912_v0.1/spreadsheet/1726/1_1726_input.xlsx`
- location: `July-KPIs!A30`  severity: High  confidence: Likely defect
- evidence: July-KPIs!A30 depends on itself, for example a total whose range includes the total cell.
- cached value: 2024-08-03 00:00:00; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: A28: '=IF(ROWS(A$6:A28)>DAY(J$13),"",J$12+ROWS(A$6:A28)-1)' -> 2024-08-01 00:00:00 | B28: '=IFERROR(VLOOKUP(($C$1&"|"&A28),#REF!,2,0),"")' -> None | A29: '=IF(ROWS(A$6:A29)>DAY(J$13),"",J$12+ROWS(A$6:A29)-1)' -> 2024-08-02 00:00:00 | B29: '=IFERROR(VLOOKUP(($C$1&"|"&A29),#REF!,2,0),"")' -> None | A30: '=IF(ROWS(A$6:A30)>DAY(J$13),"",J$12+ROWS(A$6:A30)-1)' -> 2024-08-03 00:00:00 | B30: '=IFERROR(VLOOKUP(($C$1&"|"&A30),#REF!,2,0),"")' -> None | A31: '=IF(ROWS(A$6:A31)>DAY(J$13),"",J$12+ROWS(A$6:A31)-1)' -> 2024-08-04 00:00:00 | B31: '=IFERROR(VLOOKUP(($C$1&"|"&A31),#REF!,2,0),"")' -> None | A32: '=IF(ROWS(A$6:A32)>DAY(J$13),"",J$12+ROWS(A$6:A32)-1)' -> 2024-08-05 00:00:00 | B32: '=IFERROR(VLOOKUP(($C$1&"|"&A32),#REF!,2,0),"")' -> None

### `64aece717e7d|CIRCULAR_REFERENCE|Sheet2!F39`

- workbook: `all_data_912_v0.1/spreadsheet/52640/2_52640_input.xlsx`
- location: `Sheet2!F39`  severity: High  confidence: Likely defect
- evidence: Sheet2!F39 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: D37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H37: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H38: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H39: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D40: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E40: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F40: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G40: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H40: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | G41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | H41: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None

### `b569de1c5256|CIRCULAR_REFERENCE|Sheet2!D32`

- workbook: `all_data_912_v0.1/spreadsheet/52640/1_52640_input.xlsx`
- location: `Sheet2!D32`  severity: High  confidence: Likely defect
- evidence: Sheet2!D32 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:H50
- neighbourhood: B30: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C30: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D30: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E30: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F30: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | B31: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C31: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D31: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E31: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F31: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | B32: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C32: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D32: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E32: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F32: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | B33: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C33: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D33: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E33: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F33: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | B34: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | C34: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | D34: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | E34: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None | F34: '=IFERROR(INDEX(RAW!$A:$U,_xlfn.AGGREGATE(15,6,ROW(RAW!$G$2:$G$50)/... -> None

### `69b62f583cbe|CIRCULAR_REFERENCE|Edit!E16`

- workbook: `all_data_912_v0.1/spreadsheet/49667/3_49667_input.xlsx`
- location: `Edit!E16`  severity: High  confidence: Likely defect
- evidence: Edit!E16 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: ["'Name 15'"]; column header: ''; used range: A1:AT16
- neighbourhood: C14: 10:30:00 | D14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:00:00 | E14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:15:00 | D15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | E15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | D16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | E16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | F16: 'x' | G16: 'x'

### `b8b03c02336b|CIRCULAR_REFERENCE|Test!F53`

- workbook: `all_data_912_v0.1/spreadsheet/54667/2_54667_input.xlsx`
- location: `Test!F53`  severity: High  confidence: Likely defect
- evidence: Test!F53 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D51: '=IFERROR(VLOOKUP(C51,DATA!$A:$E,2,0),"")' -> None | E51: '=IFERROR(VLOOKUP(C51,DATA!$A:$E,3,0),"")' -> None | F51: '=IF(OR(B51="PRG/FLY",B51="PRG/TVL",B51="FLY1",B51="TVL1",B51="PRG/... -> None | G51: '=IFERROR(VLOOKUP(C51,DATA!$A:$E,5,0),"")' -> None | D52: '=IFERROR(VLOOKUP(C52,DATA!$A:$E,2,0),"")' -> None | E52: '=IFERROR(VLOOKUP(C52,DATA!$A:$E,3,0),"")' -> None | F52: '=IF(OR(B52="PRG/FLY",B52="PRG/TVL",B52="FLY1",B52="TVL1",B52="PRG/... -> None | G52: '=IFERROR(VLOOKUP(C52,DATA!$A:$E,5,0),"")' -> None | D53: '=IFERROR(VLOOKUP(C53,DATA!$A:$E,2,0),"")' -> None | E53: '=IFERROR(VLOOKUP(C53,DATA!$A:$E,3,0),"")' -> None | F53: '=IF(OR(B53="PRG/FLY",B53="PRG/TVL",B53="FLY1",B53="TVL1",B53="PRG/... -> None | G53: '=IFERROR(VLOOKUP(C53,DATA!$A:$E,5,0),"")' -> None | D54: '=IFERROR(VLOOKUP(C54,DATA!$A:$E,2,0),"")' -> None | E54: '=IFERROR(VLOOKUP(C54,DATA!$A:$E,3,0),"")' -> None | F54: '=IF(OR(B54="PRG/FLY",B54="PRG/TVL",B54="FLY1",B54="TVL1",B54="PRG/... -> None | G54: '=IFERROR(VLOOKUP(C54,DATA!$A:$E,5,0),"")' -> None | D55: '=IFERROR(VLOOKUP(C55,DATA!$A:$E,2,0),"")' -> None | E55: '=IFERROR(VLOOKUP(C55,DATA!$A:$E,3,0),"")' -> None | F55: '=IF(OR(B55="PRG/FLY",B55="PRG/TVL",B55="FLY1",B55="TVL1",B55="PRG/... -> None | G55: '=IFERROR(VLOOKUP(C55,DATA!$A:$E,5,0),"")' -> None

### `34d406898185|CIRCULAR_REFERENCE|Sheet1!Q9`

- workbook: `all_data_912_v0.1/spreadsheet/45581/2_45581_input.xlsx`
- location: `Sheet1!Q9`  severity: High  confidence: Likely defect
- evidence: Sheet1!Q9 depends on itself, for example a total whose range includes the total cell.
- cached value: 'i'; row labels: []; column header: ''; used range: A1:AF9
- neighbourhood: O7: '=IFERROR(MID($B5,COLUMNS($D7:O7),1),"")' -> 'i' | P7: '=IFERROR(MID($B5,COLUMNS($D7:P7),1),"")' -> 'u' | Q7: '=IFERROR(MID($B5,COLUMNS($D7:Q7),1),"")' -> 'i' | R7: '=IFERROR(MID($B5,COLUMNS($D7:R7),1),"")' -> None | S7: '=IFERROR(MID($B5,COLUMNS($D7:S7),1),"")' -> None | O9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:O)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'i' | P9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:P)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'u' | Q9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Q)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'i' | R9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:R)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | S9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:S)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None

### `40397a4736e1|CIRCULAR_REFERENCE|Test!F8`

- workbook: `all_data_912_v0.1/spreadsheet/54667/3_54667_input.xlsx`
- location: `Test!F8`  severity: High  confidence: Likely defect
- evidence: Test!F8 depends on itself, for example a total whose range includes the total cell.
- cached value: None; row labels: []; column header: ''; used range: A1:M79
- neighbourhood: D6: '=IFERROR(VLOOKUP(C6,DATA!$A:$E,2,0),"")' -> None | E6: '=IFERROR(VLOOKUP(C6,DATA!$A:$E,3,0),"")' -> None | F6: '=IF(OR(B6="PRG/FLY",B6="PRG/TVL",B6="FLY1",B6="TVL1",B6="PRG/FLY-C... -> None | G6: '=IFERROR(VLOOKUP(C6,DATA!$A:$E,5,0),"")' -> None | D7: '=IFERROR(VLOOKUP(C7,DATA!$A:$E,2,0),"")' -> None | E7: '=IFERROR(VLOOKUP(C7,DATA!$A:$E,3,0),"")' -> None | F7: '=IF(OR(B7="PRG/FLY",B7="PRG/TVL",B7="FLY1",B7="TVL1",B7="PRG/FLY-C... -> None | G7: '=IFERROR(VLOOKUP(C7,DATA!$A:$E,5,0),"")' -> None | D8: '=IFERROR(VLOOKUP(C8,DATA!$A:$E,2,0),"")' -> None | E8: '=IFERROR(VLOOKUP(C8,DATA!$A:$E,3,0),"")' -> None | F8: '=IF(OR(B8="PRG/FLY",B8="PRG/TVL",B8="FLY1",B8="TVL1",B8="PRG/FLY-C... -> None | G8: '=IFERROR(VLOOKUP(C8,DATA!$A:$E,5,0),"")' -> None | D9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,2,0),"")' -> None | E9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,3,0),"")' -> None | F9: '=IF(OR(B9="PRG/FLY",B9="PRG/TVL",B9="FLY1",B9="TVL1",B9="PRG/FLY-C... -> None | G9: '=IFERROR(VLOOKUP(C9,DATA!$A:$E,5,0),"")' -> None | D10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,2,0),"")' -> None | E10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,3,0),"")' -> None | F10: '=IF(OR(B10="PRG/FLY",B10="PRG/TVL",B10="FLY1",B10="TVL1",B10="PRG/... -> None | G10: '=IFERROR(VLOOKUP(C10,DATA!$A:$E,5,0),"")' -> None

## DUPLICATE_KEY

### `b55280430702|DUPLICATE_KEY|Sheet1!A8,Sheet1!A30`

- workbook: `all_data_912_v0.1/spreadsheet/57989/3_57989_input.xlsx`
- location: `Sheet1!A8, Sheet1!A30`  severity: Medium  confidence: Review
- evidence: Normalized key 'driver 6' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Driver 6'; row labels: []; column header: "'Driver 5'"; used range: A1:Y118
- neighbourhood: A6: 'Driver 4' | A7: 'Driver 5' | A8: 'Driver 6' | C8: 'hk' | A9: 'Driver 7' | A10: 'Driver 8' | C10: 'hk'

### `4dd4d6e28040|DUPLICATE_KEY|Sheet1!A40,Sheet1!A41,Sheet1!A42`

- workbook: `all_data_912_v0.1/spreadsheet/42378/2_42378_input.xlsx`
- location: `Sheet1!A40, Sheet1!A41, Sheet1!A42`  severity: Medium  confidence: Review
- evidence: Normalized key '#29179' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '#29179'; row labels: []; column header: "'#29180'"; used range: A1:D52
- neighbourhood: A38: '#29180' | A39: '#29180' | A40: '#29179' | B40: 'xxxxxxx@gmail.com' | A41: '#29179' | B41: 'xxxxxxx@gmail.com' | A42: '#29179' | B42: 'xxxxxxx@gmail.com'

### `59dd5b78ebc8|DUPLICATE_KEY|dataApril!B14,dataApril!B38,dataApril!B62,dataApril!B86,dataApril!B110`

- workbook: `all_data_912_v0.1/spreadsheet/54490/3_54490_input.xlsx`
- location: `data April!B14, data April!B38, data April!B62, data April!B86, data April!B110`  severity: Medium  confidence: Review
- evidence: Normalized key 't24 - diverter' appears 90 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'T24 - Diverter'; row labels: []; column header: "'T24 - Manual Machine Bay 1'"; used range: A1:D2161
- neighbourhood: A12: 2021-04-01 00:00:00 | B12: 'T24 - Machine 3 (104)' | C12: 'Early' | D12: '' | A13: 2021-04-01 00:00:00 | B13: 'T24 - Manual Machine Bay 1' | C13: 'Early' | D13: '' | A14: 2021-04-01 00:00:00 | B14: 'T24 - Diverter' | C14: 'Early' | D14: '' | A15: 2021-04-01 00:00:00 | B15: 'T24 - Machine 2 (Olivia)' | C15: 'Early' | D15: '' | A16: 2021-04-01 00:00:00 | B16: 'T24 Manual Machine 2 (SO Man)' | C16: 'Early' | D16: ''

### `623070110cdb|DUPLICATE_KEY|Leave_Record!G7,Leave_Record!G11`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13024/2_CF_13024_input.xlsx`
- location: `Leave_Record!G7, Leave_Record!G11`  severity: Medium  confidence: Review
- evidence: Normalized key 'al' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'AL'; row labels: ["'Tom'", "'A'"]; column header: ''; used range: A1:BI34
- neighbourhood: F5: 'Roster' | G5: '=G4' -> 2022-06-01 00:00:00 | H5: '=G5+1' -> 2022-06-02 00:00:00 | I5: '=H5+1' -> 2022-06-03 00:00:00 | E6: 'Shift Type' | F6: 'A/B' | G6: '=TEXT(G5,"ddd")' -> 'Wed' | H6: '=TEXT(H5,"ddd")' -> 'Thu' | I6: '=TEXT(I5,"ddd")' -> 'Fri' | E7: "=VLOOKUP(B7,'Staff Database'!B:D,3,FALSE)" -> 'D' | F7: 'A' | G7: 'AL' | H7: 'AL' | I7: 'AL' | E8: "=VLOOKUP(B8,'Staff Database'!B:D,3,FALSE)" -> 'D' | F8: "=VLOOKUP(B8,'Staff Database'!B:E,4,FALSE)" -> 'A' | H8: 'AL' | E9: "=VLOOKUP(B9,'Staff Database'!B:D,3,FALSE)" -> 'N' | F9: "=VLOOKUP(B9,'Staff Database'!B:E,4,FALSE)" -> 'A' | I9: 'SL'

### `69355e1eb76d|DUPLICATE_KEY|Errors!I100,Errors!I101,Errors!I102`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Errors!I100, Errors!I101, Errors!I102`  severity: Medium  confidence: Review
- evidence: Normalized key '3g' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '          3G'; row labels: ["'BE GC MW Crinkles 32x140g'", "'BE GC MW Crinkles 32x140g'"]; column header: ''; used range: A1:AZ506
- neighbourhood: G98: 'ED Beetroot Sliced 16x425g' | H98: 'BEETROOT SLICED' | I98: 35 | K98: "'13AUG21ECH" | G99: 'ED Beetroot Sliced 16x425g' | H99: 'BEETROOT SLICED' | I99: 35 | K99: "'13AUG21ECH" | G100: 'BE GC MW Crinkles 32x140g' | H100: 'BE GC MW Crinkles 32x140g' | I100: '          3G' | K100: "'1102201336" | G101: 'BE GC MW Crinkles 32x140g' | H101: 'BE GC MW Crinkles 32x140g' | I101: '          3G' | K101: "'1012311336" | G102: 'BE GC MW Crinkles 32x140g' | H102: 'BE GC MW Crinkles 32x140g' | I102: '          3G' | K102: "'1102201336"

### `e82a4e0e50b2|DUPLICATE_KEY|DATABASECountries!B45,DATABASECountries!B46,DATABASECountries!B47`

- workbook: `all_data_912_v0.1/spreadsheet/37462/1_37462_input.xlsx`
- location: `DATABASE Countries!B45, DATABASE Countries!B46, DATABASE Countries!B47`  severity: Medium  confidence: Review
- evidence: Normalized key 'usd' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'USD'; row labels: ["'Hong Kong'"]; column header: "'IDR'"; used range: A1:J244
- neighbourhood: A43: 'India' | B43: 'INR' | C43: 70 | D43: '=D42+1' -> 40 | A44: 'Indonesia' | B44: 'IDR' | C44: 13500 | D44: '=D43+1' -> 41 | A45: 'Hong Kong' | B45: 'USD' | C45: 1 | D45: '=D44+1' -> 42 | A46: 'Turkey' | B46: 'USD' | C46: 1 | D46: '=D45+1' -> 43 | A47: 'Russia' | B47: 'USD' | C47: 1 | D47: '=D46+1' -> 44

### `3ee4d6f069b6|DUPLICATE_KEY|Errors!I300,Errors!I301,Errors!I302,Errors!I303,Errors!I304`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Errors!I300, Errors!I301, Errors!I302, Errors!I303, Errors!I304`  severity: Medium  confidence: Review
- evidence: Normalized key '4k' appears 93 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '          4K'; row labels: ["'CK Pluto Pups 2.25kg'", "'PLUTO PUPS'"]; column header: ''; used range: A1:AZ506
- neighbourhood: G298: 'ED Chick Peas 10x400g' | H298: 'CHICK PEAS' | I298: 44 | K298: "'04AUG21BAT" | G299: 'ED Chick Peas 10x400g' | H299: 'CHICK PEAS' | I299: 44 | K299: "'04AUG21BAT" | G300: 'CK Pluto Pups 2.25kg' | H300: 'PLUTO PUPS' | I300: '          4K' | K300: "'091222" | G301: 'CK Pluto Pups 2.25kg' | H301: 'PLUTO PUPS' | I301: '          4K' | K301: "'091222" | G302: 'CK Pluto Pups 2.25kg' | H302: 'PLUTO PUPS' | I302: '          4K' | K302: "'221222"

### `26314df08aa9|DUPLICATE_KEY|Sheet1!A4,Sheet1!A10,Sheet1!A13`

- workbook: `all_data_912_v0.1/spreadsheet/39515/1_39515_input.xlsx`
- location: `Sheet1!A4, Sheet1!A10, Sheet1!A13`  severity: Medium  confidence: Review
- evidence: Normalized key 'apr' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Apr'; row labels: []; column header: "'Oct'"; used range: A1:O13
- neighbourhood: A2: 'Mar' | B2: 2023 | C2: 1235 | A3: 'Oct' | B3: 2022 | C3: 1350 | A4: 'Apr' | B4: 2023 | C4: 1235 | A5: 'Mar' | B5: 2023 | C5: 1235 | A6: 'Oct' | B6: 2022 | C6: 1455

### `440ba3af0eec|DUPLICATE_KEY|Data!I6,Data!I7,Data!I8,Data!I10,Data!I11`

- workbook: `all_data_912_v0.1/spreadsheet/7-5/1_7-5_input.xlsx`
- location: `Data!I6, Data!I7, Data!I8, Data!I10, Data!I11`  severity: Medium  confidence: Review
- evidence: Normalized key 'n.x' appears 6 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'N.X'; row labels: ["'N.X'", "'N.X'"]; column header: "'N.X'"; used range: A1:AP12
- neighbourhood: G4: '=F4+1' -> None | H4: '=G4+1' -> None | I4: '=H4+1' -> None | J4: '=I4+1' -> None | K4: '=J4+1' -> None | G5: 'N.X' | H5: 'N.X' | I5: 'N.X' | J5: 'N.X' | K5: 'N.X' | G6: 'N.X' | H6: 'N.X' | I6: 'N.X' | J6: 'N.X' | K6: 'N.X' | G7: '1-0' | H7: 'N.X' | I7: 'N.X' | J7: 'N.X' | K7: 'N.X' | G8: 'N.X' | H8: 'N.X' | I8: 'N.X' | J8: 'N.X' | K8: 'N.X'

### `dad7502c3898|DUPLICATE_KEY|Data!P7,Data!P8,Data!P9,Data!P10,Data!P12`

- workbook: `all_data_912_v0.1/spreadsheet/7-5/2_7-5_input.xlsx`
- location: `Data!P7, Data!P8, Data!P9, Data!P10, Data!P12`  severity: Medium  confidence: Review
- evidence: Normalized key 'n.x' appears 5 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'N.X'; row labels: ["'N.X'", "'1-0'"]; column header: ''; used range: A1:AP12
- neighbourhood: N5: 'N.X' | O5: 'N.X' | P5: 'N.X' | Q5: 'N.X' | R5: 'N.X' | N6: '1-1' | O6: 2 | P6: 3 | Q6: 4 | R6: 'N.X' | N7: 'N.X' | O7: '1-0' | P7: 'N.X' | Q7: 'N.X' | R7: 'N.X' | N8: 'N.X' | O8: 'N.X' | P8: 'N.X' | Q8: 'N.X' | R8: 'N.X' | N9: '1-0' | O9: 'N.X' | P9: 'N.X' | Q9: 'N.X' | R9: 'N.X'

### `59dd5b78ebc8|DUPLICATE_KEY|dataApril!C50,dataApril!C51,dataApril!C52,dataApril!C53,dataApril!C54`

- workbook: `all_data_912_v0.1/spreadsheet/54490/3_54490_input.xlsx`
- location: `data April!C50, data April!C51, data April!C52, data April!C53, data April!C54`  severity: Medium  confidence: Review
- evidence: Normalized key 'night' appears 720 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Night'; row labels: ["'T48 - Machine 1 (Oliver)'"]; column header: "'Late'"; used range: A1:D2161
- neighbourhood: A48: 2021-04-01 00:00:00 | B48: 'THV Returns - Bay 10' | C48: 'Late' | D48: 191.976811594203 | A49: 2021-04-01 00:00:00 | B49: 'THV Returns - Bay 9' | C49: 'Late' | D49: 192.173553719008 | A50: 2021-04-01 00:00:00 | B50: 'T48 - Machine 1 (Oliver)' | C50: 'Night' | D50: 185.922077922078 | A51: 2021-04-01 00:00:00 | B51: 'T48 - Machine 2 (Olivia)' | C51: 'Night' | D51: 270.078947368421 | A52: 2021-04-01 00:00:00 | B52: 'T48 - Machine 3 (104)' | C52: 'Night' | D52: 273.96

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K1154,URNlookup!K1429`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K1154, URN lookup!K1429`  severity: Medium  confidence: Review
- evidence: Normalized key 'bb10 3aa' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'BB10 3AA'; row labels: ["'Ormerod Road'", "'Burnley'"]; column header: "'BB10 2AT'"; used range: A1:X1461
- neighbourhood: J1152: 'Burnley' | K1152: 'BB11 5BT' | L1152: 'Closed' | J1153: 'Burnley' | K1153: 'BB10 2AT' | L1153: 'Open' | J1154: 'Burnley' | K1154: 'BB10 3AA' | L1154: 'Closed' | J1155: 'Burnley' | K1155: 'BB10 1JD' | L1155: 'Closed' | J1156: 'Burnley' | K1156: 'BB11 3DF' | L1156: 'Open'

### `3a2b74c70f66|DUPLICATE_KEY|Total(2)!F7,Total(2)!F40,Total(2)!F61`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!F7, Total (2)!F40, Total (2)!F61`  severity: Medium  confidence: Review
- evidence: Normalized key 'date' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Date'; row labels: ["'Office'", "'Agent'"]; column header: ''; used range: A1:Z1026
- neighbourhood: D7: 'Office' | E7: 'Agent' | F7: 'Date' | G7: 'Paid' | H7: 'Agent' | D8: '=SUM(C8-E8)' -> 975 | E8: 975 | F8: 44392 | G8: 'Y' | H8: 'GS' | D9: '=SUM(C9-E9)' -> 1000 | E9: 1000 | F9: 44392 | G9: 'Y' | H9: 'GS'

### `158be0e0e878|DUPLICATE_KEY|Employee3!C7,Employee3!C8,Employee3!C11,Employee3!C13,Employee3!C14`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/1_382-29_input.xlsx`
- location: `Employee 3!C7, Employee 3!C8, Employee 3!C11, Employee 3!C13, Employee 3!C14`  severity: Medium  confidence: Review
- evidence: Normalized key 'a' appears 14 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'A'; row labels: ["'C'", "'Test 3'"]; column header: "'B'"; used range: A1:AB30
- neighbourhood: A5: 'A' | B5: 'Test 1' | C5: 'X' | D5: 'X' | E5: 'X' | A6: 'B' | B6: 'Test 2' | C6: 'B' | D6: 'X' | E6: 'X' | A7: 'C' | B7: 'Test 3' | C7: 'A' | D7: 'B' | E7: 'X' | A8: 'D' | B8: 'Test 4' | C8: 'A' | D8: 'B' | E8: 'C' | A9: 'E' | B9: 'Test 5' | C9: 'E' | D9: 'E' | E9: 'E'

### `e3281236e4b3|DUPLICATE_KEY|results!B3,results!B6,results!B9,results!B12,results!B15`

- workbook: `all_data_912_v0.1/spreadsheet/54490/2_54490_input.xlsx`
- location: `results!B3, results!B6, results!B9, results!B12, results!B15`  severity: Medium  confidence: Review
- evidence: Normalized key 'early' appears 30 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Early'; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: C2: 'T48 - Machine 1 (Oliver)' | D2: 'T48 - Machine 2 (Olivia)' | A3: 2021-04-01 00:00:00 | B3: 'Early' | C3: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 132.218181818182 | D3: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 213.1 | B4: 'Late' | C4: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 185.929595827901 | D4: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 0 | B5: 'Night' | C5: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 185.922077922078 | D5: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 270.078947368421

### `7c8ce353b5ce|DUPLICATE_KEY|Data!A8,Data!A18,Data!A34,Data!A59,Data!A87`

- workbook: `all_data_912_v0.1/spreadsheet/444-14/1_444-14_input.xlsx`
- location: `Data!A8, Data!A18, Data!A34, Data!A59, Data!A87`  severity: Medium  confidence: Review
- evidence: Normalized key 'b-10' appears 7 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'B-10'; row labels: []; column header: "'B-04'"; used range: A1:C144
- neighbourhood: A6: 'B-01' | B6: 2020-04-21 00:00:00 | C6: 5 | A7: 'B-04' | B7: 2020-04-21 00:00:00 | C7: 6 | A8: 'B-10' | B8: 2020-04-21 00:00:00 | C8: 7 | A9: 'B-16' | B9: 2020-04-21 00:00:00 | C9: 8 | A10: 'A-02' | B10: 2020-05-18 00:00:00 | C10: 9

### `c903fcb4672b|DUPLICATE_KEY|RS.Food!A577,RS.Food!A598`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!A577, RS.Food!A598`  severity: Medium  confidence: Review
- evidence: Normalized key 'small mixed nuts amen' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Small Mixed Nuts AMEN'; row labels: []; column header: "'Small Gugelhupf AMEN'"; used range: A1:W607
- neighbourhood: A575: 'Small Fruit Skewers AMEN' | B575: 0 | C575: 0 | A576: 'Small Gugelhupf AMEN' | B576: 0 | C576: 0 | A577: 'Small Mixed Nuts AMEN' | B577: 0 | C577: 0 | A578: 'Small Sliced Fruit AMEN' | B578: 0 | C578: 0 | A579: 'Small Sliced Fruit AMEN' | B579: 0 | C579: 0

### `1e954dcecb7e|DUPLICATE_KEY|Sheet1!B5,Sheet1!B9,Sheet1!B14`

- workbook: `all_data_912_v0.1/spreadsheet/55794/3_55794_input.xlsx`
- location: `Sheet1!B5, Sheet1!B9, Sheet1!B14`  severity: Medium  confidence: Review
- evidence: Normalized key '2022 1st q' appears 3 times in a range searched by lookup formulas; only the first match is returned.
- cached value: '2022 1st Q'; row labels: ["'Project3'"]; column header: "'2021 2nd Q'"; used range: A1:E24
- neighbourhood: A3: 'Project1' | B3: '2020 1st Q' | C3: 'Completed' | A4: 'Project2' | B4: '2021 2nd Q' | C4: 'Completed' | A5: 'Project3' | B5: '2022 1st Q' | C5: 'Not Planned' | A6: 'Project4' | B6: '2020 1st Q' | C6: 'Completed' | A7: 'Project5' | B7: '2020 2nd Q' | C7: 'Testing'

### `d49eeac3b8af|DUPLICATE_KEY|Sheet1!B6,Sheet1!B9,Sheet1!B13,Sheet1!B17,Sheet1!B22`

- workbook: `all_data_912_v0.1/spreadsheet/59902/2_59902_input.xlsx`
- location: `Sheet1!B6, Sheet1!B9, Sheet1!B13, Sheet1!B17, Sheet1!B22`  severity: Medium  confidence: Review
- evidence: Normalized key 'jane' appears 6 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Jane'; row labels: []; column header: "'Bob'"; used range: A1:H28
- neighbourhood: A4: 'Date' | B4: 'Name' | C4: 'Days Since Sale' | A5: 2008-08-29 00:00:00 | B5: 'Bob' | C5: '=A5-INDEX($A$4:$A4,MATCH(B5,$B$4:$B4,0),1)' -> '#N/A' | A6: 2008-08-29 00:00:00 | B6: 'Jane' | C6: '=A6-INDEX($A$4:$A5,MATCH(B6,$B$4:$B5,0),1)' -> '#N/A' | A7: 2008-08-30 00:00:00 | B7: 'Bob' | C7: '=A7-INDEX($A$4:$A6,MATCH(B7,$B$4:$B6,0),1)' -> 1 | A8: 2008-08-30 00:00:00 | B8: 'Bob' | C8: '=A8-INDEX($A$4:$A7,MATCH(B8,$B$4:$B7,0),1)' -> 1

### `447f9eaa5b6c|DUPLICATE_KEY|Employee2!W5,Employee2!W6,Employee2!W7,Employee2!W8,Employee2!W9`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/2_382-29_input.xlsx`
- location: `Employee 2!W5, Employee 2!W6, Employee 2!W7, Employee 2!W8, Employee 2!W9`  severity: Medium  confidence: Review
- evidence: Normalized key 'x' appears 21 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'X'; row labels: ["'X'", "'X'"]; column header: "'U'"; used range: A1:AB30
- neighbourhood: U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | X3: '=$B26' -> 'Test 22' | Y3: '=$B27' -> 'Test 23' | U4: 'S' | V4: 'T' | W4: 'U' | X4: 'V' | Y4: 'W' | U5: 'X' | V5: 'X' | W5: 'X' | X5: 'X' | Y5: 'X' | U6: 'X' | V6: 'X' | W6: 'X' | X6: 'X' | Y6: 'X' | U7: 'X' | V7: 'X' | W7: 'X' | X7: 'X' | Y7: 'X'

### `3c0a56086b5d|DUPLICATE_KEY|URNlookup!K93,URNlookup!K1213`

- workbook: `all_data_912_v0.1/spreadsheet/55427/2_55427_input.xlsx`
- location: `URN lookup!K93, URN lookup!K1213`  severity: Medium  confidence: Review
- evidence: Normalized key 'la10 5al' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'LA10 5AL'; row labels: ["'Long Lane'", "'Sedbergh'"]; column header: "'LA12 0BD'"; used range: A1:X1461
- neighbourhood: J91: 'Carlisle' | K91: 'CA1 2JB' | L91: 'Open' | I92: 'Sir John Barrow School' | J92: 'Ulverston' | K92: 'LA12 0BD' | L92: 'Open' | J93: 'Sedbergh' | K93: 'LA10 5AL' | L93: 'Open' | J94: 'Dalton-in-Furness' | K94: 'LA15 8SE' | L94: 'Open' | J95: 'Wigton' | K95: 'CA7 4DR' | L95: 'Open'

### `a3ce241a69c4|DUPLICATE_KEY|Customers!H5,Customers!H6`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/3_118-8_input.xlsx`
- location: `Customers!H5, Customers!H6`  severity: Medium  confidence: Review
- evidence: Normalized key 'in' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'IN'; row labels: ["'2646 Eu Rd.'", "'Indianapolis'"]; column header: "'MI'"; used range: A1:J14
- neighbourhood: F3: 'Address' | G3: 'City' | H3: 'State' | I3: 'Zip' | J3: 'Property Notes' | F4: '1324 Iaculis Av.' | G4: 'Racine' | H4: 'MI' | I4: 43119 | J4: 'Test Notes 1' | F5: '2646 Eu Rd.' | G5: 'Indianapolis' | H5: 'IN' | I5: 59677 | J5: 'Nice Contact' | F6: '1114 Interdum. Road' | G6: 'South Bend' | H6: 'IN' | I6: 43779 | J6: 'Test Notes 4' | F7: '4582 Porttitor Rd.' | G7: 'Oklahoma City' | H7: 'OK' | I7: 53512 | J7: 'Test Notes Updated'

### `65228fa5c9a0|DUPLICATE_KEY|RS.Food!A381,RS.Food!A382`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!A381, RS.Food!A382`  severity: Medium  confidence: Review
- evidence: Normalized key 'mixed toast' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Mixed Toast'; row labels: []; column header: "'Mixed Pastries'"; used range: A1:W607
- neighbourhood: A379: 'Med Well' | B379: 0 | C379: 0 | A380: 'Mixed Pastries' | B380: 0 | C380: 0 | A381: 'Mixed Toast' | B381: 0 | C381: 0 | A382: 'Mixed Toast' | B382: 0 | C382: 0 | A383: 'Mushroom' | B383: 0 | C383: 0

### `21865bab73e8|DUPLICATE_KEY|RS.Food!A407,RS.Food!A408`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!A407, RS.Food!A408`  severity: Medium  confidence: Review
- evidence: Normalized key 'oat milk' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'Oat Milk'; row labels: []; column header: "'No Yoghurt'"; used range: A1:W607
- neighbourhood: A405: 'No Toast' | B405: 0 | C405: 0 | A406: 'No Yoghurt' | B406: 0 | C406: 0 | A407: 'Oat Milk' | B407: 0 | C407: 0 | A408: 'Oat Milk' | B408: 0 | C408: 0 | A409: 'Omelette' | B409: 0 | C409: 0

### `ac9c457a4aed|DUPLICATE_KEY|URNlookup!K972,URNlookup!K1010`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `URN lookup!K972, URN lookup!K1010`  severity: Medium  confidence: Review
- evidence: Normalized key 'hg4 2es' appears 2 times in a range searched by lookup formulas; only the first match is returned.
- cached value: 'HG4 2ES'; row labels: ["'Church Lane'", "'Ripon'"]; column header: "'HG4 1LT'"; used range: A1:X1461
- neighbourhood: J970: 'Harrogate' | K970: 'HG3 3AY' | L970: 'Open' | J971: 'Ripon' | K971: 'HG4 1LT' | L971: 'Open' | J972: 'Ripon' | K972: 'HG4 2ES' | L972: 'Open' | J973: 'York' | K973: 'YO51 9LY' | L973: 'Open' | J974: 'Ripon' | K974: 'HG4 3PJ' | L974: 'Open'

## FORMULA_DRIFT

### `d2a515f35dce|FORMULA_DRIFT|Schedule!G28`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/1_118-8_input.xlsx`
- location: `Schedule!G28`  severity: High  confidence: Likely defect
- formula: `=IF(MONTH(S22+1)<>MONTH(S22),"",S22+1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=7): =IFERROR(INDEX(ADMIN & SETTINGS!R5C16:R66C16,MATCH(SCHEDULE!RC[-1],ADMIN & SETTINGS!R5C21:R66C21,0)),"")
- evidence: This cell: =IF(MONTH(R[-6]C[12]+1)<>MONTH(R[-6]C[12]),"",R[-6]C[12]+1)
- cached value: 2023-05-28 00:00:00; row labels: []; column header: ''; used range: A1:V78
- neighbourhood: G28: '=IF(MONTH(S22+1)<>MONTH(S22),"",S22+1)' -> 2023-05-28 00:00:00 | H28: '=IFERROR(INDEX(\'Admin & Settings\'!$P$5:$P$66,MATCH(Schedule!G28,... -> None | I28: '=IF(G28="","",IF(MONTH(G28+1)<>MONTH(G28),"",G28+1))' -> 2023-05-29 00:00:00

### `d216c973ba67|FORMULA_DRIFT|Malaga!O14`

- workbook: `all_data_912_v0.1/spreadsheet/40809/1_40809_input.xlsx`
- location: `Malaga!O14`  severity: High  confidence: Likely defect
- formula: `=IF(C11="","",C11)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =IF(R[-3]C[-11]="","",R[-3]C[-11])
- evidence: This cell: =IF(R[-3]C[-12]="","",R[-3]C[-12])
- cached value: 'DONNELLY (Louise)'; row labels: ["'PYM (Keith)'", "'G'"]; column header: ''; used range: A1:AJ57
- neighbourhood: M12: '=IF(J12="","",IF(K12="G",$G$4-L12,IF(K12="N/G",$L$4-L12,IF(K12="S/... -> None | O12: '=IF(C9="","",C9)' -> 'CURT (Kellie)' | P12: '=IF(E9="","",E9)' -> 799 | Q12: '=IF(F9="","",F9)' -> 0 | M13: '=IF(J13="","",IF(K13="G",$G$4-L13,IF(K13="N/G",$L$4-L13,IF(K13="S/... -> 449 | O13: '=IF(C10="","",C10)' -> 'CURT (Sean)' | P13: '=IF(E10="","",E10)' -> 0 | Q13: '=IF(F10="","",F10)' -> 799 | M14: '=IF(J14="","",IF(K14="G",$G$4-L14,IF(K14="N/G",$L$4-L14,IF(K14="S/... -> 799 | O14: '=IF(C11="","",C11)' -> 'DONNELLY (Louise)' | P14: '=IF(E11="","",E11)' -> 0 | Q14: '=IF(F11="","",F11)' -> 449 | M15: '=IF(J15="","",IF(K15="G",$G$4-L15,IF(K15="N/G",$L$4-L15,IF(K15="S/... -> None | O15: '=IF(C12="","",C12)' -> 'DONNELLY (Rob)' | P15: '=IF(E12="","",E12)' -> 0 | Q15: '=IF(F12="","",F12)' -> 799 | M16: '=IF(J16="","",IF(K16="G",$G$4-L16,IF(K16="N/G",$L$4-L16,IF(K16="S/... -> None | O16: '=IF(C13="","",C13)' -> 'DOWNER (Nic)' | P16: '=IF(E13="","",E13)' -> 0 | Q16: '=IF(F13="","",F13)' -> 799

### `24f6192d8cf3|FORMULA_DRIFT|data!G15`

- workbook: `all_data_912_v0.1/spreadsheet/56225/2_56225_input.xlsx`
- location: `data!G15`  severity: High  confidence: Likely defect
- formula: `=TEXT(F15-E15,"h:mm:ss")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =HOUR(RC[-3])+MINUTE(RC[-3])/60+SECOND(RC[-3])/3600
- evidence: This cell: =TEXT(RC[-1]-RC[-2],"h:mm:ss")
- cached value: '0:00:00'; row labels: ["'andrew faulk'", "'warr grind'"]; column header: ''; used range: A1:O48
- neighbourhood: E13: 10:23:25 | F13: 12:00:04 | G13: '=TEXT(F13-E13,"h:mm:ss")' -> '1:36:39' | H13: '=HOUR(E13)+MINUTE(E13)/60+SECOND(E13)/3600' -> 10.3902777777778 | I13: '=HOUR(F13)+MINUTE(F13)/60+SECOND(F13)/3600' -> 12.0011111111111 | E14: 10:28:52 | F14: 11:59:05 | G14: '=TEXT(F14-E14,"h:mm:ss")' -> '1:30:13' | H14: '=HOUR(E14)+MINUTE(E14)/60+SECOND(E14)/3600' -> 10.4811111111111 | I14: '=HOUR(F14)+MINUTE(F14)/60+SECOND(F14)/3600' -> 11.9847222222222 | E15: 14:43:37 | F15: 14:43:37 | G15: '=TEXT(F15-E15,"h:mm:ss")' -> '0:00:00' | H15: '=HOUR(E15)+MINUTE(E15)/60+SECOND(E15)/3600' -> 14.7269444444444 | I15: '=HOUR(F15)+MINUTE(F15)/60+SECOND(F15)/3600' -> 14.7269444444444 | E16: 15:17:49 | F16: 15:53:00 | G16: '=TEXT(F16-E16,"h:mm:ss")' -> '0:35:11' | H16: '=HOUR(E16)+MINUTE(E16)/60+SECOND(E16)/3600' -> 15.2969444444444 | I16: '=HOUR(F16)+MINUTE(F16)/60+SECOND(F16)/3600' -> 15.8833333333333 | E17: 11:03:00 | F17: 11:06:03 | G17: '=TEXT(F17-E17,"h:mm:ss")' -> '0:03:03' | H17: '=HOUR(E17)+MINUTE(E17)/60+SECOND(E17)/3600' -> 11.05 | I17: '=HOUR(F17)+MINUTE(F17)/60+SECOND(F17)/3600' -> 11.1008333333333

### `a94399daa94c|FORMULA_DRIFT|Here!G28`

- workbook: `all_data_912_v0.1/spreadsheet/58114/3_58114_input.xlsx`
- location: `Here!G28`  severity: High  confidence: Likely defect
- formula: `=LEFT(F28,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E26: '=IF(Sheet1!E26="","",Sheet1!E26)' -> None | F26: '=IF(Sheet1!F26="","",Sheet1!F26)' -> None | G26: '=LEFT(F26,1)' -> None | I26: '' | E27: '=IF(Sheet1!E27="","",Sheet1!E27)' -> None | F27: '=IF(Sheet1!F27="","",Sheet1!F27)' -> None | G27: '=LEFT(F27,1)' -> None | I27: '' | E28: '=IF(Sheet1!E28="","",Sheet1!E28)' -> None | F28: '=IF(Sheet1!F28="","",Sheet1!F28)' -> None | G28: '=LEFT(F28,1)' -> None | I28: '' | E29: '=IF(Sheet1!E29="","",Sheet1!E29)' -> None | F29: '=IF(Sheet1!F29="","",Sheet1!F29)' -> None | G29: '=LEFT(F29,1)' -> None | I29: '' | E30: '=IF(Sheet1!E30="","",Sheet1!E30)' -> None | F30: '=IF(Sheet1!F30="","",Sheet1!F30)' -> None | G30: '=LEFT(F30,1)' -> None | I30: ''

### `470111f62d4c|FORMULA_DRIFT|Total!A7`

- workbook: `all_data_912_v0.1/spreadsheet/11842/1_11842_input.xlsx`
- location: `Total!A7`  severity: High  confidence: Likely defect
- formula: `=Jan!A10`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[3]C[31]+FEB!R[3]C[31]+MAR!R[3]C[31]+APR!R[3]C[31]+MAY!R[3]C[31]+JUN!R[3]C[31]+JUL!R[3]C[31]+AUG!R[3]C[31]+SEP!R[3]C[31]+OCT!R[3]C[31]+NOV!R[3]C[31]+DEC!R[3]C[31]+JAN!R[4]C[31]+FEB!R[4]C[31]+MAR!R[4]C[31]+APR!R[4]C[31]+MAY!R[4]C[31]+JUN!R[4]C[31]+JUL!R[4]C[31]+AUG!R[4]C[31]+SEP!R[4]C[31]+OCT!R[4]C[31]+NOV!R[4]C[31]+DEC!R[4]C[31])/2
- evidence: This cell: =JAN!R[3]C
- cached value: 'SHATRUDHAN MAHATO'; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A5: '=Jan!A6' -> 'PETER NORONHA' | B5: '=(Jan!AG6+Feb!AG6+Mar!AG6+Apr!AG6+May!AG6+Jun!AG6+Jul!AG6+Aug!AG6+... -> 2 | C5: '=(Jan!AH6+Feb!AH6+Mar!AH6+Apr!AH6+May!AH6+Jun!AH6+Jul!AH6+Aug!AH6+... -> 0 | A6: '=Jan!A8' -> 'SHYAMBALI PAL' | B6: '=(Jan!AG8+Feb!AG8+Mar!AG8+Apr!AG8+May!AG8+Jun!AG8+Jul!AG8+Aug!AG8+... -> 1 | C6: '=(Jan!AH8+Feb!AH8+Mar!AH8+Apr!AH8+May!AH8+Jun!AH8+Jul!AH8+Aug!AH8+... -> 0 | A7: '=Jan!A10' -> 'SHATRUDHAN MAHATO' | B7: '=(Jan!AG10+Feb!AG10+Mar!AG10+Apr!AG10+May!AG10+Jun!AG10+Jul!AG10+A... -> 0 | C7: '=(Jan!AH10+Feb!AH10+Mar!AH10+Apr!AH10+May!AH10+Jun!AH10+Jul!AH10+A... -> 0 | A8: '=Jan!A12' -> 'RAVINDRA V. GOVEKAR' | B8: '=(Jan!AG12+Feb!AG12+Mar!AG12+Apr!AG12+May!AG12+Jun!AG12+Jul!AG12+A... -> 0 | C8: '=(Jan!AH12+Feb!AH12+Mar!AH12+Apr!AH12+May!AH12+Jun!AH12+Jul!AH12+A... -> 0 | A9: '=Jan!A14' -> 'DEEPAK WARPE' | B9: '=(Jan!AG14+Feb!AG14+Mar!AG14+Apr!AG14+May!AG14+Jun!AG14+Jul!AG14+A... -> 0 | C9: '=(Jan!AH14+Feb!AH14+Mar!AH14+Apr!AH14+May!AH14+Jun!AH14+Jul!AH14+A... -> 0

### `ea1e0839ce78|FORMULA_DRIFT|Here!G107`

- workbook: `all_data_912_v0.1/spreadsheet/58114/2_58114_input.xlsx`
- location: `Here!G107`  severity: High  confidence: Likely defect
- formula: `=LEFT(F107,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E105: '=IF(Sheet1!E105="","",Sheet1!E105)' -> None | F105: '=IF(Sheet1!F105="","",Sheet1!F105)' -> None | G105: '=LEFT(F105,1)' -> None | I105: '' | E106: '=IF(Sheet1!E106="","",Sheet1!E106)' -> None | F106: '=IF(Sheet1!F106="","",Sheet1!F106)' -> None | G106: '=LEFT(F106,1)' -> None | I106: '' | E107: '=IF(Sheet1!E107="","",Sheet1!E107)' -> None | F107: '=IF(Sheet1!F107="","",Sheet1!F107)' -> None | G107: '=LEFT(F107,1)' -> None | I107: '' | E108: '=IF(Sheet1!E108="","",Sheet1!E108)' -> None | F108: '=IF(Sheet1!F108="","",Sheet1!F108)' -> None | G108: '=LEFT(F108,1)' -> None | I108: '' | E109: '=IF(Sheet1!E109="","",Sheet1!E109)' -> None | F109: '=IF(Sheet1!F109="","",Sheet1!F109)' -> None | G109: '=LEFT(F109,1)' -> None | I109: ''

### `fa8217b2c986|FORMULA_DRIFT|Here!G21`

- workbook: `all_data_912_v0.1/spreadsheet/58114/1_58114_input.xlsx`
- location: `Here!G21`  severity: High  confidence: Likely defect
- formula: `=LEFT(F21,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: 'A'; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E19: '=IF(Sheet1!E19="","",Sheet1!E19)' -> 'Abselon, Cafaro' | F19: '=IF(Sheet1!F19="","",Sheet1!F19)' -> 'Abselon, Cafaro - LL21590248' | G19: '=LEFT(F19,1)' -> 'A' | I19: '' | E20: '=IF(Sheet1!E20="","",Sheet1!E20)' -> 'Absolom, Cafasso' | F20: '=IF(Sheet1!F20="","",Sheet1!F20)' -> 'Absolom, Cafasso - RK32756... | G20: '=LEFT(F20,1)' -> 'A' | I20: '' | E21: '=IF(Sheet1!E21="","",Sheet1!E21)' -> 'Absolum, Caggiano' | F21: '=IF(Sheet1!F21="","",Sheet1!F21)' -> 'Absolum, Caggiano - EM2600... | G21: '=LEFT(F21,1)' -> 'A' | I21: '' | E22: '=IF(Sheet1!E22="","",Sheet1!E22)' -> 'Tbnor, Cadigan' | F22: '=IF(Sheet1!F22="","",Sheet1!F22)' -> 'Tbnor, Cadigan - MM12168514' | G22: '=LEFT(F22,1)' -> 'T' | I22: '' | E23: '=IF(Sheet1!E23="","",Sheet1!E23)' -> None | F23: '=IF(Sheet1!F23="","",Sheet1!F23)' -> None | G23: '=LEFT(F23,1)' -> None | I23: ''

### `a94399daa94c|FORMULA_DRIFT|Here!G72`

- workbook: `all_data_912_v0.1/spreadsheet/58114/3_58114_input.xlsx`
- location: `Here!G72`  severity: High  confidence: Likely defect
- formula: `=LEFT(F72,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E70: '=IF(Sheet1!E70="","",Sheet1!E70)' -> None | F70: '=IF(Sheet1!F70="","",Sheet1!F70)' -> None | G70: '=LEFT(F70,1)' -> None | I70: '' | E71: '=IF(Sheet1!E71="","",Sheet1!E71)' -> None | F71: '=IF(Sheet1!F71="","",Sheet1!F71)' -> None | G71: '=LEFT(F71,1)' -> None | I71: '' | E72: '=IF(Sheet1!E72="","",Sheet1!E72)' -> None | F72: '=IF(Sheet1!F72="","",Sheet1!F72)' -> None | G72: '=LEFT(F72,1)' -> None | I72: '' | E73: '=IF(Sheet1!E73="","",Sheet1!E73)' -> None | F73: '=IF(Sheet1!F73="","",Sheet1!F73)' -> None | G73: '=LEFT(F73,1)' -> None | I73: '' | E74: '=IF(Sheet1!E74="","",Sheet1!E74)' -> None | F74: '=IF(Sheet1!F74="","",Sheet1!F74)' -> None | G74: '=LEFT(F74,1)' -> None | I74: ''

### `589c38846e3c|FORMULA_DRIFT|Total!A14`

- workbook: `all_data_912_v0.1/spreadsheet/11842/3_11842_input.xlsx`
- location: `Total!A14`  severity: High  confidence: Likely defect
- formula: `=Jan!A24`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[10]C[31]+FEB!R[10]C[31]+MAR!R[10]C[31]+APR!R[10]C[31]+MAY!R[10]C[31]+JUN!R[10]C[31]+JUL!R[10]C[31]+AUG!R[10]C[31]+SEP!R[10]C[31]+OCT!R[10]C[31]+NOV!R[10]C[31]+DEC!R[10]C[31]+JAN!R[11]C[31]+FEB!R[11]C[31]+MAR!R[11]C[31]+APR!R[11]C[31]+MAY!R[11]C[31]+JUN!R[11]C[31]+JUL!R[11]C[31]+AUG!R[11]C[31]+SEP!R[11]C[31]+OCT!R[11]C[31]+NOV!R[11]C[31]+DEC!R[11]C[31])/2
- evidence: This cell: =JAN!R[10]C
- cached value: 'RESHMA KHOLKAR'; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A12: '=Jan!A20' -> 'RUZAR VAZ' | B12: '=(Jan!AG20+Feb!AG20+Mar!AG20+Apr!AG20+May!AG20+Jun!AG20+Jul!AG20+A... -> 0 | C12: '=(Jan!AH20+Feb!AH20+Mar!AH20+Apr!AH20+May!AH20+Jun!AH20+Jul!AH20+A... -> 0 | A13: '=Jan!A22' -> 'DHARMENDRA KUMAR' | B13: '=(Jan!AG22+Feb!AG22+Mar!AG22+Apr!AG22+May!AG22+Jun!AG22+Jul!AG22+A... -> 0 | C13: '=(Jan!AH22+Feb!AH22+Mar!AH22+Apr!AH22+May!AH22+Jun!AH22+Jul!AH22+A... -> 0 | A14: '=Jan!A24' -> 'RESHMA KHOLKAR' | B14: '=(Jan!AG24+Feb!AG24+Mar!AG24+Apr!AG24+May!AG24+Jun!AG24+Jul!AG24+A... -> 0 | C14: '=(Jan!AH24+Feb!AH24+Mar!AH24+Apr!AH24+May!AH24+Jun!AH24+Jul!AH24+A... -> 0 | A15: '=Jan!A26' -> 0 | B15: '=(Jan!AG26+Feb!AG26+Mar!AG26+Apr!AG26+May!AG26+Jun!AG26+Jul!AG26+A... -> 0 | C15: '=(Jan!AH26+Feb!AH26+Mar!AH26+Apr!AH26+May!AH26+Jun!AH26+Jul!AH26+A... -> 0 | A16: '=Jan!A28' -> 0 | B16: '=(Jan!AG28+Feb!AG28+Mar!AG28+Apr!AG28+May!AG28+Jun!AG28+Jul!AG28+A... -> 0 | C16: '=(Jan!AH28+Feb!AH28+Mar!AH28+Apr!AH28+May!AH28+Jun!AH28+Jul!AH28+A... -> 0

### `d7e27f29097e|FORMULA_DRIFT|Malaga!O27`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!O27`  severity: High  confidence: Likely defect
- formula: `=IF(J13="","",J13)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =IF(R[-14]C[-4]="","",R[-14]C[-4])
- evidence: This cell: =IF(R[-14]C[-5]="","",R[-14]C[-5])
- cached value: 'PYM (Carole)'; row labels: []; column header: ''; used range: A1:AJ57
- neighbourhood: O25: '=IF(J11="","",J11)' -> 'MUNTING (Tony)' | P25: '=IF(L11="","",L11)' -> 0 | Q25: '=IF(M11="","",M11)' -> 799 | O26: '=IF(J12="","",J12)' -> None | P26: '=IF(L12="","",L12)' -> None | Q26: '=IF(M12="","",M12)' -> None | O27: '=IF(J13="","",J13)' -> 'PYM (Carole)' | P27: '=IF(L13="","",L13)' -> 0 | Q27: '=IF(M13="","",M13)' -> 449 | M28: '=SUM(M24:M27)' -> 0 | O28: '=IF(J14="","",J14)' -> 'PYM (Keith)' | P28: '=IF(L14="","",L14)' -> 0 | Q28: '=IF(M14="","",M14)' -> 799 | O29: '=IF(J15="","",J15)' -> None | P29: '=IF(L15="","",L15)' -> None | Q29: '=IF(M15="","",M15)' -> None

### `2b89f3e053b3|FORMULA_DRIFT|Here!G120`

- workbook: `all_data_912_v0.1/spreadsheet/58147/2_58147_input.xlsx`
- location: `Here!G120`  severity: High  confidence: Likely defect
- formula: `=LEFT(F120,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E118: '=IF(Sheet1!E118="","",Sheet1!E118)' -> None | F118: '=IF(Sheet1!F118="","",Sheet1!F118)' -> None | G118: '=LEFT(F118,1)' -> None | I118: '' | E119: '=IF(Sheet1!E119="","",Sheet1!E119)' -> None | F119: '=IF(Sheet1!F119="","",Sheet1!F119)' -> None | G119: '=LEFT(F119,1)' -> None | I119: '' | E120: '=IF(Sheet1!E120="","",Sheet1!E120)' -> None | F120: '=IF(Sheet1!F120="","",Sheet1!F120)' -> None | G120: '=LEFT(F120,1)' -> None | I120: '' | E121: '=IF(Sheet1!E121="","",Sheet1!E121)' -> None | F121: '=IF(Sheet1!F121="","",Sheet1!F121)' -> None | G121: '=LEFT(F121,1)' -> None | I121: '' | E122: '=IF(Sheet1!E122="","",Sheet1!E122)' -> None | F122: '=IF(Sheet1!F122="","",Sheet1!F122)' -> None | G122: '=LEFT(F122,1)' -> None | I122: ''

### `2069bdc39cd5|FORMULA_DRIFT|Result!K1`

- workbook: `all_data_912_v0.1/spreadsheet/55085/1_55085_input.xlsx`
- location: `Result!K1`  severity: High  confidence: Likely defect
- formula: `=J1`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =#REF!
- evidence: This cell: =RC[-1]
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:L13
- neighbourhood: J1: '=#REF!' -> '#REF!' | K1: '=J1' -> '#REF!' | L1: '=#REF!' -> '#REF!' | I2: 'Banana' | J2: 'Apple' | K2: 'Mango' | L2: 'Banana' | I3: '=H3' -> 'Shrawan' | J3: 'Bhadra' | K3: '=J3' -> 'Bhadra' | L3: '=K3' -> 'Bhadra'

### `2b89f3e053b3|FORMULA_DRIFT|Here!G50`

- workbook: `all_data_912_v0.1/spreadsheet/58147/2_58147_input.xlsx`
- location: `Here!G50`  severity: High  confidence: Likely defect
- formula: `=LEFT(F50,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E48: '=IF(Sheet1!E48="","",Sheet1!E48)' -> None | F48: '=IF(Sheet1!F48="","",Sheet1!F48)' -> None | G48: '=LEFT(F48,1)' -> None | I48: '' | E49: '=IF(Sheet1!E49="","",Sheet1!E49)' -> None | F49: '=IF(Sheet1!F49="","",Sheet1!F49)' -> None | G49: '=LEFT(F49,1)' -> None | I49: '' | E50: '=IF(Sheet1!E50="","",Sheet1!E50)' -> None | F50: '=IF(Sheet1!F50="","",Sheet1!F50)' -> None | G50: '=LEFT(F50,1)' -> None | I50: '' | E51: '=IF(Sheet1!E51="","",Sheet1!E51)' -> None | F51: '=IF(Sheet1!F51="","",Sheet1!F51)' -> None | G51: '=LEFT(F51,1)' -> None | I51: '' | E52: '=IF(Sheet1!E52="","",Sheet1!E52)' -> None | F52: '=IF(Sheet1!F52="","",Sheet1!F52)' -> None | G52: '=LEFT(F52,1)' -> None | I52: ''

### `589c38846e3c|FORMULA_DRIFT|Total!A17`

- workbook: `all_data_912_v0.1/spreadsheet/11842/3_11842_input.xlsx`
- location: `Total!A17`  severity: High  confidence: Likely defect
- formula: `=Jan!A30`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=8): =(JAN!R[13]C[31]+FEB!R[13]C[31]+MAR!R[13]C[31]+APR!R[13]C[31]+MAY!R[13]C[31]+JUN!R[13]C[31]+JUL!R[13]C[31]+AUG!R[13]C[31]+SEP!R[13]C[31]+OCT!R[13]C[31]+NOV!R[13]C[31]+DEC!R[13]C[31]+JAN!R[14]C[31]+FEB!R[14]C[31]+MAR!R[14]C[31]+APR!R[14]C[31]+MAY!R[14]C[31]+JUN!R[14]C[31]+JUL!R[14]C[31]+AUG!R[14]C[31]+SEP!R[14]C[31]+OCT!R[14]C[31]+NOV!R[14]C[31]+DEC!R[14]C[31])/2
- evidence: This cell: =JAN!R[13]C
- cached value: 0; row labels: []; column header: ''; used range: A1:Z26
- neighbourhood: A15: '=Jan!A26' -> 0 | B15: '=(Jan!AG26+Feb!AG26+Mar!AG26+Apr!AG26+May!AG26+Jun!AG26+Jul!AG26+A... -> 0 | C15: '=(Jan!AH26+Feb!AH26+Mar!AH26+Apr!AH26+May!AH26+Jun!AH26+Jul!AH26+A... -> 0 | A16: '=Jan!A28' -> 0 | B16: '=(Jan!AG28+Feb!AG28+Mar!AG28+Apr!AG28+May!AG28+Jun!AG28+Jul!AG28+A... -> 0 | C16: '=(Jan!AH28+Feb!AH28+Mar!AH28+Apr!AH28+May!AH28+Jun!AH28+Jul!AH28+A... -> 0 | A17: '=Jan!A30' -> 0 | B17: '=(Jan!AG30+Feb!AG30+Mar!AG30+Apr!AG30+May!AG30+Jun!AG30+Jul!AG30+A... -> 0 | C17: '=(Jan!AH30+Feb!AH30+Mar!AH30+Apr!AH30+May!AH30+Jun!AH30+Jul!AH30+A... -> 0 | A18: '=Jan!A32' -> 0 | B18: '=(Jan!AG32+Feb!AG32+Mar!AG32+Apr!AG32+May!AG32+Jun!AG32+Jul!AG32+A... -> 0 | C18: '=(Jan!AH32+Feb!AH32+Mar!AH32+Apr!AH32+May!AH32+Jun!AH32+Jul!AH32+A... -> 0 | A19: '=Jan!A34' -> 0 | B19: '=(Jan!AG34+Feb!AG34+Mar!AG34+Apr!AG34+May!AG34+Jun!AG34+Jul!AG34+A... -> 0 | C19: '=(Jan!AH34+Feb!AH34+Mar!AH34+Apr!AH34+May!AH34+Jun!AH34+Jul!AH34+A... -> 0

### `24f6192d8cf3|FORMULA_DRIFT|data!G16`

- workbook: `all_data_912_v0.1/spreadsheet/56225/2_56225_input.xlsx`
- location: `data!G16`  severity: High  confidence: Likely defect
- formula: `=TEXT(F16-E16,"h:mm:ss")`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =HOUR(RC[-3])+MINUTE(RC[-3])/60+SECOND(RC[-3])/3600
- evidence: This cell: =TEXT(RC[-1]-RC[-2],"h:mm:ss")
- cached value: '0:35:11'; row labels: ["'tevor bock'", "'basic serv'"]; column header: ''; used range: A1:O48
- neighbourhood: E14: 10:28:52 | F14: 11:59:05 | G14: '=TEXT(F14-E14,"h:mm:ss")' -> '1:30:13' | H14: '=HOUR(E14)+MINUTE(E14)/60+SECOND(E14)/3600' -> 10.4811111111111 | I14: '=HOUR(F14)+MINUTE(F14)/60+SECOND(F14)/3600' -> 11.9847222222222 | E15: 14:43:37 | F15: 14:43:37 | G15: '=TEXT(F15-E15,"h:mm:ss")' -> '0:00:00' | H15: '=HOUR(E15)+MINUTE(E15)/60+SECOND(E15)/3600' -> 14.7269444444444 | I15: '=HOUR(F15)+MINUTE(F15)/60+SECOND(F15)/3600' -> 14.7269444444444 | E16: 15:17:49 | F16: 15:53:00 | G16: '=TEXT(F16-E16,"h:mm:ss")' -> '0:35:11' | H16: '=HOUR(E16)+MINUTE(E16)/60+SECOND(E16)/3600' -> 15.2969444444444 | I16: '=HOUR(F16)+MINUTE(F16)/60+SECOND(F16)/3600' -> 15.8833333333333 | E17: 11:03:00 | F17: 11:06:03 | G17: '=TEXT(F17-E17,"h:mm:ss")' -> '0:03:03' | H17: '=HOUR(E17)+MINUTE(E17)/60+SECOND(E17)/3600' -> 11.05 | I17: '=HOUR(F17)+MINUTE(F17)/60+SECOND(F17)/3600' -> 11.1008333333333 | E18: 11:20:04 | F18: 11:47:14 | G18: '=TEXT(F18-E18,"h:mm:ss")' -> '0:27:10' | H18: '=HOUR(E18)+MINUTE(E18)/60+SECOND(E18)/3600' -> 11.3344444444444 | I18: '=HOUR(F18)+MINUTE(F18)/60+SECOND(F18)/3600' -> 11.7872222222222

### `19dfd5dbcec5|FORMULA_DRIFT|formamspnc(7)!AT8`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!AT8`  severity: High  confidence: Likely defect
- formula: `=AE8`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=13): =IF(IF(ISBLANK(RC[-13]),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS(R1C18:R1C35-RC[-13])),R1C18:R1C35)-RC[-13]))<6,IF(ISBLANK(RC[-13]),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS(R1C18:R1C35-RC[-13])),R1C18:R1C35)-RC[-13])),"")
- evidence: This cell: =RC[-15]
- cached value: -1; row labels: ["'12c/16c/19c/24c/27c/29c/33c/40c/43c/47c/50c/55c/60c/63c(...", "'1pt 1u/2d,1st alm a5/a6'"]; column header: ''; used range: A1:ED48610
- neighbourhood: AR6: '=SUM(AE6:AN6)' -> 5 | AS6: '=CONCATENATE(AE6,",",AF6,",",AG6,",",AH6,",",AI6,",",AJ6,",",AK6,"... -> '0,0,1,4,-2,0,0,-1,3,0,-2,0,1' | AT6: '=AE6' -> 0 | AU6: '=AF6+AT6' -> 0 | AV6: '=SUM(AE6:AG6)' -> 1 | AR7: '=SUM(AE7:AN7)' -> 3 | AS7: '=CONCATENATE(AE7,",",AF7,",",AG7,",",AH7,",",AI7,",",AJ7,",",AK7,"... -> '-1,1,1,-2,1,0,1,2,-2,2,-1,... | AT7: '=AE7' -> -1 | AU7: '=AF7+AT7' -> 0 | AV7: '=SUM(AE7:AG7)' -> 1 | AR8: '=SUM(AE8:AN8)' -> 6 | AS8: '=CONCATENATE(AE8,",",AF8,",",AG8,",",AH8,",",AI8,",",AJ8,",",AK8,"... -> '-1,1,2,-1,0,3,0,-2,1,3,-1,... | AT8: '=AE8' -> -1 | AU8: '=AF8+AT8' -> 0 | AV8: '=SUM(AE8:AG8)' -> 2 | AR9: '=SUM(AE9:AN9)' -> 4 | AS9: '=CONCATENATE(AE9,",",AF9,",",AG9,",",AH9,",",AI9,",",AJ9,",",AK9,"... -> '1,4,-1,0,1,0,-1,0,0,0,2,1,0' | AT9: '=AE9' -> 1 | AU9: '=AF9+AT9' -> 5 | AV9: '=SUM(AE9:AG9)' -> 4 | AR10: '=SUM(AE10:AN10)' -> 10 | AS10: '=CONCATENATE(AE10,",",AF10,",",AG10,",",AH10,",",AI10,",",AJ10,","... -> '1,2,4,-1,1,0,3,-1,1,0,0,2,2' | AT10: '=AE10' -> 1 | AU10: '=AF10+AT10' -> 3 | AV10: '=SUM(AE10:AG10)' -> 7

### `ea1e0839ce78|FORMULA_DRIFT|Here!G76`

- workbook: `all_data_912_v0.1/spreadsheet/58114/2_58114_input.xlsx`
- location: `Here!G76`  severity: High  confidence: Likely defect
- formula: `=LEFT(F76,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E74: '=IF(Sheet1!E74="","",Sheet1!E74)' -> None | F74: '=IF(Sheet1!F74="","",Sheet1!F74)' -> None | G74: '=LEFT(F74,1)' -> None | I74: '' | E75: '=IF(Sheet1!E75="","",Sheet1!E75)' -> None | F75: '=IF(Sheet1!F75="","",Sheet1!F75)' -> None | G75: '=LEFT(F75,1)' -> None | I75: '' | E76: '=IF(Sheet1!E76="","",Sheet1!E76)' -> None | F76: '=IF(Sheet1!F76="","",Sheet1!F76)' -> None | G76: '=LEFT(F76,1)' -> None | I76: '' | E77: '=IF(Sheet1!E77="","",Sheet1!E77)' -> None | F77: '=IF(Sheet1!F77="","",Sheet1!F77)' -> None | G77: '=LEFT(F77,1)' -> None | I77: '' | E78: '=IF(Sheet1!E78="","",Sheet1!E78)' -> None | F78: '=IF(Sheet1!F78="","",Sheet1!F78)' -> None | G78: '=LEFT(F78,1)' -> None | I78: ''

### `fe65a777a463|FORMULA_DRIFT|DATABASECountries!D38`

- workbook: `all_data_912_v0.1/spreadsheet/37462/3_37462_input.xlsx`
- location: `DATABASE Countries!D38`  severity: High  confidence: Likely defect
- formula: `=D37+1`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=2): =R[-1]C-R[-14]C[4]
- evidence: This cell: =R[-1]C+1
- cached value: 35; row labels: []; column header: ''; used range: A1:J244
- neighbourhood: C36: '=IF(B36="","",IFERROR(B36/$B$2,0))' -> None | D36: '=D35+1' -> 33 | E36: 'Bulgaria' | F36: '=SUMPRODUCT(ISNUMBER(SEARCH(E36,$A$4:$A$36))*$B$4:$B$36) {array F36}' -> 0 | B37: '=SUM(B4:B36)' -> 37324.65 | C37: '=SUM(C4:C36)' -> 533.2092857142858 | D37: '=D36+1' -> 34 | E37: 'Burkina Faso' | F37: '=SUMPRODUCT(ISNUMBER(SEARCH(E37,$A$4:$A$36))*$B$4:$B$36) {array F37}' -> 0 | B38: '=B37-F24' -> 37324.65 | C38: '=C37-G24' -> 533.2092857142858 | D38: '=D37+1' -> 35 | E38: 'Burundi' | F38: '=SUMPRODUCT(ISNUMBER(SEARCH(E38,$A$4:$A$36))*$B$4:$B$36) {array F38}' -> 0 | D39: '=D38+1' -> 36 | E39: 'Cambodia' | F39: '=SUMPRODUCT(ISNUMBER(SEARCH(E39,$A$4:$A$36))*$B$4:$B$36) {array F39}' -> 0 | D40: '=D39+1' -> 37 | E40: 'Cameroon' | F40: '=SUMPRODUCT(ISNUMBER(SEARCH(E40,$A$4:$A$36))*$B$4:$B$36) {array F40}' -> 0

### `b31624554d1c|FORMULA_DRIFT|TEST!M7`

- workbook: `all_data_912_v0.1/spreadsheet/55039/3_55039_input.xlsx`
- location: `TEST!M7`  severity: High  confidence: Likely defect
- formula: `=B7`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=146): =R[-1]C[5]
- evidence: This cell: =RC[-11]
- cached value: 1500.7; row labels: ["'Starting Balance'", "'W'"]; column header: ''; used range: A1:S1004
- neighbourhood: K6: 'Balance' | N6: 'Bet' | O6: 'Win' | K7: '=IF(J7=0,G7,IF(J7="W",G7+I7,G7-H7))' -> 3014.35 | M7: '=B7' -> 1500.7 | N7: '=IF(AND(M7<500,M7>250),50,M7*0.1)' -> 150.07 | O7: '=IF(J7="L",-H7,IF(J7="w",I7,N7*3.5))' -> 1513.65 | K8: '=IF(J8=0,G8,IF(J8="W",G8+I8,G8-H8))' -> 4821.71 | M8: '=R7' -> 3014.35 | N8: '=IF(AND(M8<500,M8>250),50,M8*0.1)' -> 301.435 | O8: '=IF(J8="L",-H8,IF(J8="w",I8,N8*3.5))' -> 1807.36 | K9: '=IF(J9=0,G9,IF(J9="W",G9+I9,G9-H9))' -> 7350 | M9: '=R8' -> 4821.71 | N9: '=IF(AND(M9<500,M9>250),50,M9*0.1)' -> 482.171 | O9: '=IF(J9="L",-H9,IF(J9="w",I9,N9*3.5))' -> 2528.29

### `fe65a777a463|FORMULA_DRIFT|DATABASECountries!C38`

- workbook: `all_data_912_v0.1/spreadsheet/37462/3_37462_input.xlsx`
- location: `DATABASE Countries!C38`  severity: High  confidence: Likely defect
- formula: `=C37-G24`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=33): =IF(RC[-1]="","",IFERROR(RC[-1]/R2C2,0))
- evidence: This cell: =R[-1]C-R[-14]C[4]
- cached value: 533.2092857142858; row labels: []; column header: ''; used range: A1:J244
- neighbourhood: C36: '=IF(B36="","",IFERROR(B36/$B$2,0))' -> None | D36: '=D35+1' -> 33 | E36: 'Bulgaria' | B37: '=SUM(B4:B36)' -> 37324.65 | C37: '=SUM(C4:C36)' -> 533.2092857142858 | D37: '=D36+1' -> 34 | E37: 'Burkina Faso' | B38: '=B37-F24' -> 37324.65 | C38: '=C37-G24' -> 533.2092857142858 | D38: '=D37+1' -> 35 | E38: 'Burundi' | D39: '=D38+1' -> 36 | E39: 'Cambodia' | D40: '=D39+1' -> 37 | E40: 'Cameroon'

### `90411d62a6a8|FORMULA_DRIFT|Here!G130`

- workbook: `all_data_912_v0.1/spreadsheet/58147/3_58147_input.xlsx`
- location: `Here!G130`  severity: High  confidence: Likely defect
- formula: `=LEFT(F130,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E128: '=IF(Sheet1!E128="","",Sheet1!E128)' -> None | F128: '=IF(Sheet1!F128="","",Sheet1!F128)' -> None | G128: '=LEFT(F128,1)' -> None | I128: '' | E129: '=IF(Sheet1!E129="","",Sheet1!E129)' -> None | F129: '=IF(Sheet1!F129="","",Sheet1!F129)' -> None | G129: '=LEFT(F129,1)' -> None | I129: '' | E130: '=IF(Sheet1!E130="","",Sheet1!E130)' -> None | F130: '=IF(Sheet1!F130="","",Sheet1!F130)' -> None | G130: '=LEFT(F130,1)' -> None | I130: '' | E131: '=IF(Sheet1!E131="","",Sheet1!E131)' -> None | F131: '=IF(Sheet1!F131="","",Sheet1!F131)' -> None | G131: '=LEFT(F131,1)' -> None | I131: '' | E132: '=IF(Sheet1!E132="","",Sheet1!E132)' -> None | F132: '=IF(Sheet1!F132="","",Sheet1!F132)' -> None | G132: '=LEFT(F132,1)' -> None | I132: ''

### `9b7879bd3308|FORMULA_DRIFT|Here!G47`

- workbook: `all_data_912_v0.1/spreadsheet/58147/1_58147_input.xlsx`
- location: `Here!G47`  severity: High  confidence: Likely defect
- formula: `=LEFT(F47,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E45: '=IF(Sheet1!E45="","",Sheet1!E45)' -> None | F45: '=IF(Sheet1!F45="","",Sheet1!F45)' -> None | G45: '=LEFT(F45,1)' -> None | I45: '' | E46: '=IF(Sheet1!E46="","",Sheet1!E46)' -> None | F46: '=IF(Sheet1!F46="","",Sheet1!F46)' -> None | G46: '=LEFT(F46,1)' -> None | I46: '' | E47: '=IF(Sheet1!E47="","",Sheet1!E47)' -> None | F47: '=IF(Sheet1!F47="","",Sheet1!F47)' -> None | G47: '=LEFT(F47,1)' -> None | I47: '' | E48: '=IF(Sheet1!E48="","",Sheet1!E48)' -> None | F48: '=IF(Sheet1!F48="","",Sheet1!F48)' -> None | G48: '=LEFT(F48,1)' -> None | I48: '' | E49: '=IF(Sheet1!E49="","",Sheet1!E49)' -> None | F49: '=IF(Sheet1!F49="","",Sheet1!F49)' -> None | G49: '=LEFT(F49,1)' -> None | I49: ''

### `fa8217b2c986|FORMULA_DRIFT|Here!G67`

- workbook: `all_data_912_v0.1/spreadsheet/58114/1_58114_input.xlsx`
- location: `Here!G67`  severity: High  confidence: Likely defect
- formula: `=LEFT(F67,1)`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=6): =IF(SHEET1!RC="","",SHEET1!RC)
- evidence: This cell: =LEFT(RC[-1],1)
- cached value: None; row labels: []; column header: ''; used range: A1:J140
- neighbourhood: E65: '=IF(Sheet1!E65="","",Sheet1!E65)' -> None | F65: '=IF(Sheet1!F65="","",Sheet1!F65)' -> None | G65: '=LEFT(F65,1)' -> None | I65: '' | E66: '=IF(Sheet1!E66="","",Sheet1!E66)' -> None | F66: '=IF(Sheet1!F66="","",Sheet1!F66)' -> None | G66: '=LEFT(F66,1)' -> None | I66: '' | E67: '=IF(Sheet1!E67="","",Sheet1!E67)' -> None | F67: '=IF(Sheet1!F67="","",Sheet1!F67)' -> None | G67: '=LEFT(F67,1)' -> None | I67: '' | E68: '=IF(Sheet1!E68="","",Sheet1!E68)' -> None | F68: '=IF(Sheet1!F68="","",Sheet1!F68)' -> None | G68: '=LEFT(F68,1)' -> None | I68: '' | E69: '=IF(Sheet1!E69="","",Sheet1!E69)' -> None | F69: '=IF(Sheet1!F69="","",Sheet1!F69)' -> None | G69: '=LEFT(F69,1)' -> None | I69: ''

### `6bc9e1c652db|FORMULA_DRIFT|INPUTS!C4`

- workbook: `all_data_912_v0.1/spreadsheet/52216/1_52216_input.xlsx`
- location: `INPUTS!C4`  severity: High  confidence: Likely defect
- formula: `=DATA!B4*DATA!B7`
- evidence: Formula differs from the dominant relative pattern in this row.
- evidence: Dominant pattern (n=9): =RC[-1]*(1+R[1]C)
- evidence: This cell: =DATA!RC[-1]*DATA!R[3]C[-1]
- cached value: 1250000; row labels: ["'Gross Potential Rent (GPR)'"]; column header: ''; used range: A1:L23
- neighbourhood: B2: 'YEAR' | A3: 'REVENUE ' | B3: 0 | C3: 1 | D3: 2 | E3: 3 | A4: 'Gross Potential Rent (GPR)' | B4: 0 | C4: '=DATA!B4*DATA!B7' -> 1250000 | D4: '=C4*(1+D5)' -> 1300000 | E4: '=D4*(1+E5)' -> 1352000 | A5: 'GPR Growth (%)' | B5: 0 | C5: '=DATA!B5' -> 0.04 | D5: '=DATA!B5' -> 0.04 | E5: '=DATA!B5' -> 0.04 | A6: 'Vacancy Rate' | B6: 1 | C6: 1 | D6: 0.55 | E6: 0.1

### `c2c1c9ef2579|FORMULA_DRIFT|formamspnc(7)!BK5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!BK5`  severity: High  confidence: Likely defect
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:AE5,S$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Formula differs from the dominant relative pattern in this column.
- evidence: Dominant pattern (n=6): =IF(IF(ISBLANK(R1C[-44]),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS(RC18:RC30-R1C[-44])),RC18:RC30)-R1C[-44]))<6,IF(ISBLANK(R1C[-44]),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS(RC18:RC30-R1C[-44])),RC18:RC30)-R1C[-44])),"")
- evidence: This cell: =_XLFN.IFNA(LOOKUP(1,0/COUNTIFS(RC[-44]:RC[-32],R1C[-44]+{1,0,-1}),{1,0,-1}),"")
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range S5:AE5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': "R5: '1 ext,1st 1 ext'", 'right': 'AF5: None'}
- neighbourhood: BI3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),3) {array BI3}' -> '#NUM!' | BJ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(R5:AD5,R$1+{1,0,-1}),{1,0,-1}),"")... -> None | BK5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:AE5,S$1+{1,0,-1}),{1,0,-1}),"")... -> None | BL5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(T5:AF5,T$1+{1,0,-1}),{1,0,-1}),"")... -> None | BM5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(U5:AG5,U$1+{1,0,-1}),{1,0,-1}),"")... -> None | BI6: '=IF(COUNTIF(AT6:BF6,0)>3,COUNTIF(AT6:BF6,0),"")' -> None | BJ6: '=IF(IF(ISBLANK(R$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-R$1... -> 0 | BK6: '=IF(IF(ISBLANK(S$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-S$1... -> 0 | BL6: '=IF(IF(ISBLANK(T$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-T$1... -> -1 | BM6: '=IF(IF(ISBLANK(U$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R6:$AD6-U$1... -> 0 | BI7: '=IF(COUNTIF(AT7:BF7,0)>3,COUNTIF(AT7:BF7,0),"")' -> None | BJ7: '=IF(IF(ISBLANK(R$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-R$1... -> 1 | BK7: '=IF(IF(ISBLANK(S$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-S$1... -> 1 | BL7: '=IF(IF(ISBLANK(T$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-T$1... -> -1 | BM7: '=IF(IF(ISBLANK(U$1),"",-1*(LOOKUP(1,1/FREQUENCY(0,ABS($R7:$AD7-U$1... -> 2

## HARDCODE_IN_FORMULA_BLOCK

### `eaf10bcf4950|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E41`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/1_191-40_input.xlsx`
- location: `Sheet1!E41`  severity: High  confidence: Likely defect
- evidence: Value 113.7 sits between Sheet1!D41 and Sheet1!F41, which share the pattern =RC[-2]+RC[-1].
- cached value: 113.7; row labels: ["'RICH GOLD'"]; column header: ''; used range: A1:L250
- neighbourhood: C39: 0 | D39: '=B39+C39' -> 0 | E39: 108.1 | F39: '=D39+E39' -> 108.1 | G39: 6 | C40: -114.8 | D40: '=B40+C40' -> -114.8 | E40: 115.7 | F40: '=D40+E40' -> 0.9000000000000057 | G40: 6 | C41: 0 | D41: '=B41+C41' -> 111.8 | E41: 113.7 | F41: '=D41+E41' -> 225.5 | G41: 6 | C42: 0 | D42: '=B42+C42' -> 0 | E42: 116.3 | F42: '=D42+E42' -> 116.3 | G42: 6 | C43: 0 | D43: '=B43+C43' -> 0 | E43: 110.5 | F43: '=D43+E43' -> 110.5 | G43: 6

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!J8`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!J8`  severity: High  confidence: Likely defect
- evidence: Value 0 sits between Sheet1!I8 and Sheet1!L8, which share the pattern =RC[-2]-RC[-1].
- cached value: 0; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | K6: 1 | L6: '=J6-K6' -> 4 | H7: 3 | I7: '=G7-H7' -> -1 | J7: 2 | K7: 3 | L7: '=J7-K7' -> -1 | H8: 2 | I8: '=G8-H8' -> -2 | J8: 0 | K8: 2 | L8: '=J8-K8' -> -2

### `d0ff63b07a1a|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P9`

- workbook: `all_data_912_v0.1/spreadsheet/57262/2_57262_input.xlsx`
- location: `Sheet1!P9`  severity: High  confidence: Likely defect
- evidence: Value 12.75 sits between Sheet1!N9 and Sheet1!Q9, which share the pattern =RC[-2]*RC[-1].
- cached value: 12.75; row labels: ["'Order 3'"]; column header: ''; used range: A1:Y25
- neighbourhood: N7: '=L7*M7' -> 1.4984 | O7: 0.02 | P7: 8 | Q7: '=O7*P7' -> 0.16 | R7: '=Q7+N7' -> 1.6584 | N8: '=L8*M8' -> 0.5808 | O8: 0.02 | P8: 3.25 | Q8: '=O8*P8' -> 0.065 | R8: '=Q8+N8' -> 0.6458 | N9: '=L9*M9' -> 2.6104 | O9: 0.02 | P9: 12.75 | Q9: '=O9*P9' -> 0.255 | R9: '=Q9+N9' -> 2.8654 | N10: '=L10*M10' -> 0.1964 | O10: 0.02 | P10: 2.6 | Q10: '=O10*P10' -> 0.052 | R10: '=Q10+N10' -> 0.2484 | N11: '=L11*M11' -> 2.2576 | O11: 0.02 | P11: 15.75 | Q11: '=O11*P11' -> 0.315 | R11: '=Q11+N11' -> 2.5726

### `f6618f3a869c|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E38`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/3_191-40_input.xlsx`
- location: `Sheet1!E38`  severity: High  confidence: Likely defect
- evidence: Value 115.6 sits between Sheet1!D38 and Sheet1!F38, which share the pattern =RC[-2]+RC[-1].
- cached value: 115.6; row labels: ["'RIVERSIDE'"]; column header: ''; used range: A1:L250
- neighbourhood: C37: 0 | D37: '=B37+C37' -> 0 | E37: 115 | F37: '=D37+E37' -> 115 | G37: 6 | C38: 112.7 | D38: '=B38+C38' -> 224.5 | E38: 115.6 | F38: '=D38+E38' -> 340.1 | G38: 6 | C39: 0 | D39: '=B39+C39' -> 0 | E39: 108.1 | F39: '=D39+E39' -> 108.1 | G39: 6 | C40: -114.8 | D40: '=B40+C40' -> -114.8 | E40: 115.7 | F40: '=D40+E40' -> 0.900000000000006 | G40: 6

### `cae038ac83e8|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E77`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/2_191-40_input.xlsx`
- location: `Sheet1!E77`  severity: High  confidence: Likely defect
- evidence: Value 113.5 sits between Sheet1!D77 and Sheet1!F77, which share the pattern =RC[-2]+RC[-1].
- cached value: 113.5; row labels: ["'GAME TIME'"]; column header: ''; used range: A1:L250
- neighbourhood: C76: 0 | D76: '=B76+C76' -> 111.9 | E76: 108.4 | F76: '=D76+E76' -> 220.3 | G76: 10 | C77: 111.9 | D77: '=B77+C77' -> 223.9 | E77: 113.5 | F77: '=D77+E77' -> 337.4 | G77: 10 | C78: 0 | D78: '=B78+C78' -> 112.3 | E78: 110.4 | F78: '=D78+E78' -> 222.7 | G78: 10 | C79: 0 | D79: '=B79+C79' -> 112.6 | E79: 110.9 | F79: '=D79+E79' -> 223.5 | G79: 10

### `eaf10bcf4950|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E52`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/1_191-40_input.xlsx`
- location: `Sheet1!E52`  severity: High  confidence: Likely defect
- evidence: Value 116 sits between Sheet1!D52 and Sheet1!F52, which share the pattern =RC[-2]+RC[-1].
- cached value: 116; row labels: ["'MOOSE MITCHELL'"]; column header: ''; used range: A1:L250
- neighbourhood: C50: -109.5 | D50: '=B50+C50' -> 2.799999999999997 | E50: 109.3 | F50: '=D50+E50' -> 112.1 | G50: 7 | C51: 0 | D51: '=B51+C51' -> 113.3 | E51: 112.6 | F51: '=D51+E51' -> 225.89999999999998 | G51: 7 | C52: -113.4 | D52: '=B52+C52' -> -0.4000000000000057 | E52: 116 | F52: '=D52+E52' -> 115.6 | G52: 7 | C53: -112.2 | D53: '=B53+C53' -> 0.3999999999999915 | E53: 112.4 | F53: '=D53+E53' -> 112.8 | G53: 7

### `6116800fac3b|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D48`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/1_395-48_input.xlsx`
- location: `Sheet1!D48`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D47 and Sheet1!D49, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'MARTINEZ CATALINO'", "'BRAVO J'"]; column header: ''; used range: A1:D302
- neighbourhood: B46: 'TERRERO PEDRO M' | C46: 'TERRERO PEDRO M' | D46: '=IF(AND(A46=1,B46=C46),1,"")' -> None | B47: 'PENA BRYAN' | C47: 'PENA BRYAN' | D47: '=IF(AND(A47=1,B47=C47),1,"")' -> None | B48: 'MARTINEZ CATALINO' | C48: 'BRAVO J' | D48: 1 | B49: 'MONROY FRANCISCO' | C49: 'FREY KYLE' | D49: '=IF(AND(A49=1,B49=C49),1,"")' -> None | B50: 'MONROY FRANCISCO' | C50: 'MONROY FRANCISCO' | D50: '=IF(AND(A50=1,B50=C50),1,"")' -> None

### `cae038ac83e8|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E10`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/2_191-40_input.xlsx`
- location: `Sheet1!E10`  severity: High  confidence: Likely defect
- evidence: Value 113.4 sits between Sheet1!D10 and Sheet1!F10, which share the pattern =RC[-2]+RC[-1].
- cached value: 113.4; row labels: ["'LEISUREWEAR'"]; column header: ''; used range: A1:L250
- neighbourhood: C9: 110.6 | D9: '=B9+C9' -> 221.3 | E9: 112.1 | F9: '=D9+E9' -> 333.4 | G9: 3 | C10: 112.5 | D10: '=B10+C10' -> 224.9 | E10: 113.4 | F10: '=D10+E10' -> 338.3 | G10: 3 | C11: 112.5 | D11: '=B11+C11' -> 224.9 | E11: 113.2 | F11: '=D11+E11' -> 338.1 | G11: 3 | C12: -110.9 | D12: '=B12+C12' -> 1.59999999999999 | E12: 113.4 | F12: '=D12+E12' -> 115 | G12: 3

### `f5521bffa45f|HARDCODE_IN_FORMULA_BLOCK|Sheet1!D11`

- workbook: `all_data_912_v0.1/spreadsheet/395-48/3_395-48_input.xlsx`
- location: `Sheet1!D11`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!D10 and Sheet1!D12, which share the pattern =IF(AND(RC[-3]=1,RC[-2]=RC[-1]),1,"").
- cached value: 1; row labels: ["'MONROY FRANCISCO'", "'B'"]; column header: ''; used range: A1:D302
- neighbourhood: B9: 'ALVARADO F T' | C9: 'ALVARADO F T' | B10: 'MARTINEZ CATALINO' | C10: 'ROMAN EVIN A' | D10: '=IF(AND(A10=1,B10=C10),1,"")' -> None | B11: 'MONROY FRANCISCO' | C11: 'B' | D11: 1 | B12: 'ANTONGEORGI WILLIAM JR' | C12: 'HERRERA CRISTOBAL' | D12: '=IF(AND(A12=1,B12=C12),1,"")' -> None | B13: 'TERRERO PEDRO M' | C13: 'OROZCO IRVING' | D13: '=IF(AND(A13=1,B13=C13),1,"")' -> None

### `f42d1d87f115|HARDCODE_IN_FORMULA_BLOCK|Sheet1!O7`

- workbook: `all_data_912_v0.1/spreadsheet/57262/1_57262_input.xlsx`
- location: `Sheet1!O7`  severity: High  confidence: Likely defect
- evidence: Value 0.02 sits between Sheet1!N7 and Sheet1!Q7, which share the pattern =RC[-2]*RC[-1].
- cached value: 0.02; row labels: ["'Order 1'"]; column header: "'Energy cost per hour'"; used range: A1:Y25
- neighbourhood: M6: 'Material cost per 1ml' | N6: 'Material Cost Total' | O6: 'Energy cost per hour' | P6: 'Time Required\n(r-up to hour)' | Q6: 'Energy Cost \nTotal' | M7: 0.04 | N7: '=L7*M7' -> 1.4984 | O7: 0.02 | P7: 8 | Q7: '=O7*P7' -> 0.16 | M8: 0.04 | N8: '=L8*M8' -> 0.5808 | O8: 0.02 | P8: 3.25 | Q8: '=O8*P8' -> 0.065 | M9: 0.04 | N9: '=L9*M9' -> 2.6104 | O9: 0.02 | P9: 12.75 | Q9: '=O9*P9' -> 0.255

### `2ed80e0ee4cd|HARDCODE_IN_FORMULA_BLOCK|DRP!M10`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!M10`  severity: High  confidence: Likely defect
- evidence: Value 131 sits between DRP!L10 and DRP!O10, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 131; row labels: ["'RM1'", "'RC1'"]; column header: ''; used range: A1:O23
- neighbourhood: K8: 5 | L8: '=I8+J8-K8' -> None | M8: 600 | N8: 5 | O8: '=L8+M8-N8' -> None | L9: '=I9+J9-K9' -> None | M9: 125 | O9: '=L9+M9-N9' -> None | L10: '=I10+J10-K10' -> None | M10: 131 | O10: '=L10+M10-N10' -> None | K11: '=SUM(K7:K10)' -> None | L11: '=SUM(L7:L10)' -> None | M11: '=SUM(M7:M10)' -> None | N11: '=SUM(N7:N10)' -> None | O11: '=SUM(O7:O10)' -> None | L12: '=I12+J12-K12' -> None | O12: '=L12+M12-N12' -> None

### `d0ff63b07a1a|HARDCODE_IN_FORMULA_BLOCK|Sheet1!O15`

- workbook: `all_data_912_v0.1/spreadsheet/57262/2_57262_input.xlsx`
- location: `Sheet1!O15`  severity: High  confidence: Likely defect
- evidence: Value 0.02 sits between Sheet1!N15 and Sheet1!Q15, which share the pattern =RC[-2]*RC[-1].
- cached value: 0.02; row labels: ["'Order 9'"]; column header: ''; used range: A1:Y25
- neighbourhood: M13: 0.04 | N13: '=L13*M13' -> 0.3388 | O13: 0.02 | P13: 5 | Q13: '=O13*P13' -> 0.1 | M14: 0.04 | N14: '=L14*M14' -> 0.3464 | O14: 0.02 | P14: 5.3 | Q14: '=O14*P14' -> 0.106 | M15: 0.04 | N15: '=L15*M15' -> 1.2024 | O15: 0.02 | P15: 5.3 | Q15: '=O15*P15' -> 0.106 | M16: 0.04 | N16: '=L16*M16' -> 0 | O16: 0.02 | Q16: '=O16*P16' -> 0 | M17: 0.04 | N17: '=L17*M17' -> 0 | O17: 0.02 | Q17: '=O17*P17' -> 0

### `6d6fc1caeb06|HARDCODE_IN_FORMULA_BLOCK|DRP!N3`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/1_175-10_input.xlsx`
- location: `DRP!N3`  severity: High  confidence: Likely defect
- evidence: Value 20 sits between DRP!L3 and DRP!O3, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 20; row labels: ["'RE1'", "'RS1'"]; column header: ''; used range: A1:O23
- neighbourhood: L1: 'NET' | M1: 'BUYING' | N1: 'SELLING' | O1: 'NET' | L2: '=I2+J2-K2' -> None | M2: 0 | N2: 0 | O2: '=L2+M2-N2' -> None | L3: '=I3+J3-K3' -> None | M3: 400 | N3: 20 | O3: '=L3+M3-N3' -> None | L4: '=I4+J4-K4' -> None | N4: 20 | O4: '=L4+M4-N4' -> None | L5: '=I5+J5-K5' -> None | O5: '=L5+M5-N5' -> None

### `e2c7f2deac85|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P9`

- workbook: `all_data_912_v0.1/spreadsheet/57262/3_57262_input.xlsx`
- location: `Sheet1!P9`  severity: High  confidence: Likely defect
- evidence: Value 12.75 sits between Sheet1!N9 and Sheet1!Q9, which share the pattern =RC[-2]*RC[-1].
- cached value: 12.75; row labels: ["'Order 3'"]; column header: ''; used range: A1:Y25
- neighbourhood: N7: '=L7*M7' -> 1.4984 | O7: 0.02 | P7: 8 | Q7: '=O7*P7' -> 0.16 | R7: '=Q7+N7' -> 1.6584 | N8: '=L8*M8' -> 0.5808 | O8: 0.02 | P8: 3.25 | Q8: '=O8*P8' -> 0.065 | R8: '=Q8+N8' -> 0.6458 | N9: '=L9*M9' -> 2.6104 | O9: 0.02 | P9: 12.75 | Q9: '=O9*P9' -> 0.255 | R9: '=Q9+N9' -> 2.8654 | N10: '=L10*M10' -> 0.1964 | O10: 0.02 | P10: 2.6 | Q10: '=O10*P10' -> 0.052 | R10: '=Q10+N10' -> 0.2484 | N11: '=L11*M11' -> 2.2576 | O11: 0.02 | P11: 15.75 | Q11: '=O11*P11' -> 0.315 | R11: '=Q11+N11' -> 2.5726

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!H8`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!H8`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!F8 and Sheet1!I8, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: F6: '=D6-E6' -> 4 | G6: 5 | H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | F7: '=D7-E7' -> -1 | G7: 2 | H7: 3 | I7: '=G7-H7' -> -1 | J7: 2 | F8: '=D8-E8' -> -2 | G8: 0 | H8: 2 | I8: '=G8-H8' -> -2 | J8: 0

### `fe25bc710753|HARDCODE_IN_FORMULA_BLOCK|Sheet1!H6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/2_CF_13993_input.xlsx`
- location: `Sheet1!H6`  severity: High  confidence: Likely defect
- evidence: Value 1 sits between Sheet1!F6 and Sheet1!I6, which share the pattern =RC[-2]-RC[-1].
- cached value: 1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: F4: '=D4-E4' -> 1 | G4: 2 | H4: 2 | I4: '=G4-H4' -> 0 | J4: 3 | F5: -1 | G5: 3 | H5: 2 | I5: -1 | J5: 1 | F6: '=D6-E6' -> 4 | G6: 5 | H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | F7: '=D7-E7' -> -1 | G7: 2 | H7: 3 | I7: '=G7-H7' -> -1 | J7: 2 | F8: '=D8-E8' -> -2 | G8: 0 | H8: 2 | I8: '=G8-H8' -> -2 | J8: 0

### `f42d1d87f115|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P11`

- workbook: `all_data_912_v0.1/spreadsheet/57262/1_57262_input.xlsx`
- location: `Sheet1!P11`  severity: High  confidence: Likely defect
- evidence: Value 15.75 sits between Sheet1!N11 and Sheet1!Q11, which share the pattern =RC[-2]*RC[-1].
- cached value: 15.75; row labels: ["'Order 5'"]; column header: ''; used range: A1:Y25
- neighbourhood: N9: '=L9*M9' -> 2.6104 | O9: 0.02 | P9: 12.75 | Q9: '=O9*P9' -> 0.255 | R9: '=Q9+N9' -> 2.8654 | N10: '=L10*M10' -> 0.1964 | O10: 0.02 | P10: 2.6 | Q10: '=O10*P10' -> 0.052 | R10: '=Q10+N10' -> 0.2484 | N11: '=L11*M11' -> 2.2576 | O11: 0.02 | P11: 15.75 | Q11: '=O11*P11' -> 0.315 | R11: '=Q11+N11' -> 2.5726 | N12: '=L12*M12' -> 0.4532 | O12: 0.02 | P12: 6.5 | Q12: '=O12*P12' -> 0.13 | R12: '=Q12+N12' -> 0.5832 | N13: '=L13*M13' -> 0.3388 | O13: 0.02 | P13: 5 | Q13: '=O13*P13' -> 0.1 | R13: '=Q13+N13' -> 0.4388

### `f6618f3a869c|HARDCODE_IN_FORMULA_BLOCK|Sheet1!E53`

- workbook: `all_data_912_v0.1/spreadsheet/191-40/3_191-40_input.xlsx`
- location: `Sheet1!E53`  severity: High  confidence: Likely defect
- evidence: Value 112.4 sits between Sheet1!D53 and Sheet1!F53, which share the pattern =RC[-2]+RC[-1].
- cached value: 112.4; row labels: ["'SINGLE ME OUT'"]; column header: ''; used range: A1:L250
- neighbourhood: C51: 0 | D51: '=B51+C51' -> 113.3 | E51: 112.6 | F51: '=D51+E51' -> 225.9 | G51: 7 | C52: -113.4 | D52: '=B52+C52' -> -0.400000000000006 | E52: 116 | F52: '=D52+E52' -> 115.6 | G52: 7 | C53: -112.2 | D53: '=B53+C53' -> 0.399999999999991 | E53: 112.4 | F53: '=D53+E53' -> 112.8 | G53: 7 | C55: 107.7 | D55: '=B55+C55' -> 217.6 | E55: 109.8 | F55: '=D55+E55' -> 327.4 | G55: 8

### `495cb6cdb000|HARDCODE_IN_FORMULA_BLOCK|Sheet1!M7`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/1_CF_13993_input.xlsx`
- location: `Sheet1!M7`  severity: High  confidence: Likely defect
- evidence: Value 2 sits between Sheet1!L7 and Sheet1!O7, which share the pattern =RC[-2]-RC[-1].
- cached value: 2; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: K5: 7 | L5: -1 | M5: 1 | N5: 6 | O5: -1 | K6: 1 | L6: '=J6-K6' -> 4 | M6: 5 | N6: 0 | O6: '=M6-N6' -> 5 | K7: 3 | L7: '=J7-K7' -> -1 | M7: 2 | N7: 3 | O7: '=M7-N7' -> -1 | K8: 2 | L8: '=J8-K8' -> -2 | M8: 0 | N8: 2 | O8: '=M8-N8' -> -2

### `19ea38afb413|HARDCODE_IN_FORMULA_BLOCK|Sheet1!F9`

- workbook: `all_data_912_v0.1/spreadsheet/33094/3_33094_input.xlsx`
- location: `Sheet1!F9`  severity: High  confidence: Likely defect
- evidence: Value 8 sits between Sheet1!F8 and Sheet1!F10, which share the pattern =R[-1]C/R7C2.
- cached value: 8; row labels: ["'Employee3'"]; column header: ''; used range: A1:Z10
- neighbourhood: D7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!I$4:I$1000)' -> 0 | E7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!J$4:J$1000)' -> 0 | F7: 25 | G7: 25 | H7: 25 | D8: '=D7/$B$7' -> 0 | E8: '=E7/$B$7' -> 0 | F8: '=F7/$B$7' -> 0.625 | G8: '=G7/$B$7' -> 0.625 | H8: '=H7/$B$7' -> 0.625 | D9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!I$4:I$1000)' -> 0 | E9: 10 | F9: 8 | G9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)' -> 0 | H9: 6 | D10: '=D9/$B$7' -> 0 | E10: '=E9/$B$7' -> 0.25 | F10: '=F9/$B$7' -> 0.2 | G10: '=G9/$B$7' -> 0 | H10: '=H9/$B$7' -> 0.15

### `e2c7f2deac85|HARDCODE_IN_FORMULA_BLOCK|Sheet1!P11`

- workbook: `all_data_912_v0.1/spreadsheet/57262/3_57262_input.xlsx`
- location: `Sheet1!P11`  severity: High  confidence: Likely defect
- evidence: Value 15.75 sits between Sheet1!N11 and Sheet1!Q11, which share the pattern =RC[-2]*RC[-1].
- cached value: 15.75; row labels: ["'Order 5'"]; column header: ''; used range: A1:Y25
- neighbourhood: N9: '=L9*M9' -> 2.6104 | O9: 0.02 | P9: 12.75 | Q9: '=O9*P9' -> 0.255 | R9: '=Q9+N9' -> 2.8654 | N10: '=L10*M10' -> 0.1964 | O10: 0.02 | P10: 2.6 | Q10: '=O10*P10' -> 0.052 | R10: '=Q10+N10' -> 0.2484 | N11: '=L11*M11' -> 2.2576 | O11: 0.02 | P11: 15.75 | Q11: '=O11*P11' -> 0.315 | R11: '=Q11+N11' -> 2.5726 | N12: '=L12*M12' -> 0.4532 | O12: 0.02 | P12: 6.5 | Q12: '=O12*P12' -> 0.13 | R12: '=Q12+N12' -> 0.5832 | N13: '=L13*M13' -> 0.3388 | O13: 0.02 | P13: 5 | Q13: '=O13*P13' -> 0.1 | R13: '=Q13+N13' -> 0.4388

### `dfc7d039db26|HARDCODE_IN_FORMULA_BLOCK|Sheet2!B8`

- workbook: `all_data_912_v0.1/spreadsheet/56953/2_56953_input.xlsx`
- location: `Sheet2!B8`  severity: High  confidence: Likely defect
- evidence: Value 700 sits between Sheet2!B6 and Sheet2!B9, which share the pattern =R[-1]C+100.
- cached value: 700; row labels: []; column header: "'Engine HS'"; used range: A1:L15
- neighbourhood: A6: 70 | B6: '=B5+100' -> 1200 | C6: '=B6*1.65' -> 1980 | D6: '=A6*9550/C6' -> 337.626262626263 | A7: 'Power (kW)' | B7: 'Engine HS' | C7: 'Power take-off (rpm)' | D7: '(Nm)' | A8: 70 | B8: 700 | C8: '=B8*2.04' -> 1428 | D8: '=A8*9550/C8' -> 468.137254901961 | A9: 70 | B9: '=B8+100' -> 800 | C9: '=B9*2.04' -> 1632 | D9: '=A9*9550/C9' -> 409.620098039216 | A10: 'Power (kW)' | B10: 'Engine LS' | C10: 'Power take-off (rpm)' | D10: '(Nm)'

### `32b3a786ec79|HARDCODE_IN_FORMULA_BLOCK|Sheet1!H9`

- workbook: `all_data_912_v0.1/spreadsheet/33094/2_33094_input.xlsx`
- location: `Sheet1!H9`  severity: High  confidence: Likely defect
- evidence: Value 6 sits between Sheet1!H8 and Sheet1!H10, which share the pattern =R[-1]C/R7C2.
- cached value: 6; row labels: ["'Employee3'"]; column header: ''; used range: A1:Z10
- neighbourhood: F7: 25 | G7: 25 | H7: 25 | I7: 17 | J7: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A7,[1]Sheet2!O$4:O$1000)' -> 0 | F8: '=F7/$B$7' -> 0.625 | G8: '=G7/$B$7' -> 0.625 | H8: '=H7/$B$7' -> 0.625 | I8: '=I7/$B$7' -> 0.425 | J8: '=J7/$B$7' -> 0 | F9: 8 | G9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!L$4:L$1000)' -> 0 | H9: 6 | I9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!N$4:N$1000)' -> 0 | J9: '=SUMIF([1]Sheet2!$A$4:$A$1000,$A9,[1]Sheet2!O$4:O$1000)' -> 0 | F10: '=F9/$B$7' -> 0.2 | G10: '=G9/$B$7' -> 0 | H10: '=H9/$B$7' -> 0.15 | I10: '=I9/$B$7' -> 0 | J10: '=J9/$B$7' -> 0

### `2ed80e0ee4cd|HARDCODE_IN_FORMULA_BLOCK|DRP!M8`

- workbook: `all_data_912_v0.1/spreadsheet/175-10/3_175-10_input.xlsx`
- location: `DRP!M8`  severity: High  confidence: Likely defect
- evidence: Value 600 sits between DRP!L8 and DRP!O8, which share the pattern =RC[-3]+RC[-2]-RC[-1].
- cached value: 600; row labels: ["'RM1'", "'RC1'"]; column header: ''; used range: A1:O23
- neighbourhood: K6: '=SUM(K2:K5)' -> None | L6: '=SUM(L2:L5)' -> None | M6: '=SUM(M2:M5)' -> None | N6: '=SUM(N2:N5)' -> None | O6: '=SUM(O2:O5)' -> None | K7: 10 | L7: '=I7+J7-K7' -> None | M7: 100 | N7: 10 | O7: '=L7+M7-N7' -> None | K8: 5 | L8: '=I8+J8-K8' -> None | M8: 600 | N8: 5 | O8: '=L8+M8-N8' -> None | L9: '=I9+J9-K9' -> None | M9: 125 | O9: '=L9+M9-N9' -> None | L10: '=I10+J10-K10' -> None | M10: 131 | O10: '=L10+M10-N10' -> None

### `5fb44ac2af63|HARDCODE_IN_FORMULA_BLOCK|Sheet1!I5`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13993/3_CF_13993_input.xlsx`
- location: `Sheet1!I5`  severity: High  confidence: Likely defect
- evidence: Value -1 sits between Sheet1!I4 and Sheet1!I6, which share the pattern =RC[-2]-RC[-1].
- cached value: -1; row labels: ["'Arti-1'", "'Black'"]; column header: ''; used range: A1:R8
- neighbourhood: G3: 1 | H3: 2 | I3: '=G3-H3' -> -1 | J3: 2 | K3: 2 | G4: 2 | H4: 2 | I4: '=G4-H4' -> 0 | J4: 3 | K4: 5 | G5: 3 | H5: 2 | I5: -1 | J5: 1 | K5: 7 | G6: 5 | H6: 1 | I6: '=G6-H6' -> 4 | J6: 5 | K6: 1 | G7: 2 | H7: 3 | I7: '=G7-H7' -> -1 | J7: 2 | K7: 3

## HIDDEN_STRUCTURE_IN_TOTAL

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|b73d1c`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 46 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `3ee4d6f069b6|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|0971ac`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 78 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 28599; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 28599 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `ef479c030de6|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!D4|eaab5a`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!D4`  severity: Medium  confidence: Review
- formula: `=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$4:$BF$82)*($AY6/100),""),"")`
- evidence: Hidden column AW on Sheet1 feeds 42 visible formula(s): Sheet1!D4, Sheet1!C5, Sheet1!D5, Sheet1!C6, Sheet1!D6, Sheet1!C7, Sheet1!D7, Sheet1!C8, ....
- cached value: None; row labels: []; column header: "'Goal (%)'"; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: B2: 'CASE REPLIES' | B3: 'Team Total' | C3: 'Goal #' | D3: 'Goal (%)' | E3: 'Actual (#)' | F3: 'Goal (%) Actual' | B4: 167 | D4: '=IF(AND(B4>0,$AW6>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E4: 12 | F4: 0.0718562874251497 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | F5: 0.0769230769230769 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | F6: 0.0818713450292398

### `69355e1eb76d|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|b1475b`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 183 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CO5`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!CO5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AQ on formamspnc (7) feeds 31 visible formula(s): formamspnc (7)!CO5, formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AQ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AR5: None'}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CM6: '=IF(COUNTIF(BX6:CJ6,0)>3,COUNTIF(BX6:CJ6,0),"")' -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CM7: '=IF(COUNTIF(BX7:CJ7,0)>3,COUNTIF(BX7:CJ7,0),"")' -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `d3e7f4128e71|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|552821`

- workbook: `all_data_912_v0.1/spreadsheet/51090/3_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 48 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 2083 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 2083 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `3ee4d6f069b6|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|963084`

- workbook: `all_data_912_v0.1/spreadsheet/51090/1_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 152 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 28599; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 28599 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `c5dcce1aa966|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|bc4a58`

- workbook: `all_data_912_v0.1/spreadsheet/57728/2_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 46 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `69355e1eb76d|HIDDEN_STRUCTURE_IN_TOTAL|DailyNumbers!M3|2d06b6`

- workbook: `all_data_912_v0.1/spreadsheet/51090/2_51090_input.xlsx`
- location: `Daily Numbers!M3`  severity: Medium  confidence: Review
- formula: `=SUMIFS('Inbound Receipts'!M:M,'Inbound Receipts'!I:I,"="&A3,'Inbound Receipts'!Q:Q,"="&L3)`
- evidence: Hidden row 60 on Inbound Receipts feeds 22 visible formula(s): Daily Numbers!M3, Daily Numbers!M4, Daily Numbers!M5, Daily Numbers!M6, Daily Numbers!M7, Daily Numbers!M8, Daily Numbers!M9, Daily Numbers!M10, ....
- cached value: 46501; row labels: ["'CHSJEFFE'", "'CHBTHOMA'"]; column header: "'Inbound Receipts'"; used range: A1:BQ24
- neighbourhood: N1: 'Errors' | K2: 'Week' | L2: 'Date' | M2: 'Inbound Receipts' | N2: 'II' | O2: 'IR' | K3: 0 | L3: 2021-08-20 00:00:00 | M3: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A3,\... -> 46501 | N3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | O3: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A3,Errors!$Q:$Q,"="&$L3,Err... -> 0 | K4: 0 | L4: 2021-08-20 00:00:00 | M4: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A4,\... -> 46501 | N4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | O4: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A4,Errors!$Q:$Q,"="&$L4,Err... -> 0 | K5: 0 | L5: 2021-08-20 00:00:00 | M5: '=SUMIFS(\'Inbound Receipts\'!M:M,\'Inbound Receipts\'!I:I,"="&A5,\... -> 6732 | N5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0 | O5: '=SUMIFS(Errors!$M:$M,Errors!$I:$I,"="&$A5,Errors!$Q:$Q,"="&$L5,Err... -> 0

### `ab88bab5d14b|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H4|affac6`

- workbook: `all_data_912_v0.1/spreadsheet/50154/2_50154_input.xlsx`
- location: `Sheet1!H4`  severity: Medium  confidence: Review
- formula: `=SUM(G4,F4)`
- evidence: Hidden column G on Sheet1 feeds 11 visible formula(s): Sheet1!H4, Sheet1!H5, Sheet1!H6, Sheet1!H7, Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, ....
- cached value: 7.66666666666667; row labels: ["'Winter Guard #1'", "'Y'"]; column header: "'Final Score'"; used range: A1:O15
- neighbourhood: F3: 'Splash page points' | G3: 'AVG' | H3: 'Final Score' | F4: '=IF(D4="Y",1,0)' -> 1 | G4: '=AVERAGE(B4:C4,E4)' -> 6.66666666666667 | H4: '=SUM(G4,F4)' -> 7.66666666666667 | F5: '=IF(D5="Y",1,0)' -> 0 | G5: '=AVERAGE(B5:C5,E5)' -> 6.33333333333333 | H5: '=SUM(G5,F5)' -> 6.33333333333333 | F6: '=IF(D6="Y",1,0)' -> 1 | G6: '=AVERAGE(B6:C6,E6)' -> 6.66666666666667 | H6: '=SUM(G6,F6)' -> 7.66666666666667

### `ac9c457a4aed|HIDDEN_STRUCTURE_IN_TOTAL|Compiledandlocatedschoolsda!B2|796f70`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!B2`  severity: Medium  confidence: Review
- formula: `=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$1461,0))`
- evidence: Hidden row 78 on URN lookup feeds 12 visible formula(s): Compiled and located schools da!B2, Compiled and located schools da!B3, Compiled and located schools da!B4, Compiled and located schools da!B5, Compiled and located schools da!B6, Compiled and located schools da!B7, Compiled and located schools da!B8, Compiled and located schools da!B9, ....
- cached value: '#N/A'; row labels: []; column header: "'DFES check'"; used range: A1:AJ1419
- range 'URN lookup'!$D$2:$D$1461: values ['2001', '2004', '2005', '2008', '2010', '2014', '2019', '2020', '2027', '2028', '2032', '2033']; beyond: {'above': "D1: 'ESTAB'", 'below': 'D1462: None'}
- neighbourhood: A1: 'URN' | B1: 'DFES check' | C1: 'DfE Number' | D1: 'County' | B2: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$146... -> '#N/A' | D2: 'Cumbria' | B3: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L3,'URN lookup'!$K$2:$K$146... -> '#N/A' | D3: 'Cumbria' | B4: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L4,'URN lookup'!$K$2:$K$146... -> '#N/A' | D4: 'Cumbria'

### `c5dcce1aa966|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|7e9433`

- workbook: `all_data_912_v0.1/spreadsheet/57728/2_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 10 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `712151c9ae8c|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|f92920`

- workbook: `all_data_912_v0.1/spreadsheet/57728/1_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 65 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!CP5|c290ef`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!CP5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column AU on formamspnc (7) feeds 29 visible formula(s): formamspnc (7)!CP5, formamspnc (7)!CQ5, formamspnc (7)!CR5, formamspnc (7)!CS5, formamspnc (7)!CT5, formamspnc (7)!CU5, formamspnc (7)!CV5, formamspnc (7)!CW5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AF5:BJ5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AE5: None', 'right': "BK5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(S5:A..."}
- neighbourhood: CO5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AE5:AQ5,AE$1+{1,0,-1}),{1,0,-1}),"... -> None | CP5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AF5:BJ5,AF$1+{1,0,-1}),{1,0,-1}),"... -> None | CQ5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AG5:BK5,AG$1+{1,0,-1}),{1,0,-1}),"... -> None | CR5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(AH5:BL5,AH$1+{1,0,-1}),{1,0,-1}),"... -> None | CN6: '=CONCATENATE(BJ6,",",BK6,",",BL6,",",BM6,",",BN6,",",BO6,",",BP6,"... -> '0,0,-1,0,2,-3,0,1,-2,0,0,-... | CO6: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R6:$AD6,AE$1+{1,0,-1}),{1,0,-1}),... -> None | CN7: '=CONCATENATE(BJ7,",",BK7,",",BL7,",",BM7,",",BN7,",",BO7,",",BP7,"... -> '1,1,-1,2,-1,0,-1,2,2,-2,1,... | CO7: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS($R7:$AD7,AE$1+{1,0,-1}),{1,0,-1}),... -> None

### `cb6809749f05|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|04afab`

- workbook: `all_data_912_v0.1/spreadsheet/57728/3_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 77 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!BF5|ef284c`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!BF5`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")`
- evidence: Hidden column Y on formamspnc (7) feeds 99 visible formula(s): formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'", "'1 ext,1st 1 ext'"]; column header: "'m3'"; used range: A1:ED48610
- range P5:AB5: values ['None', 'None', "'1 ext,1st 1 ext'", 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'O5: \'=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A",...', 'right': 'AC5: None'}
- neighbourhood: BD3: 'm1' | BE3: 'm2' | BF3: 'm3' | BG3: '=_xlfn.MAXIFS(BI5:BI11,AD5:AD11,">1")' -> 0 | BH3: '=LARGE(IF(AD5:AD11>0,BI5:BI11),2) {array BH3}' -> '#NUM!' | BD5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(L5:Z5,L$1+{1,0,-1}),{1,0,-1}),"") ... -> None | BE5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1+{1,0,-1}),{1,0,-1}),"")... -> None | BF5: '=_xlfn.IFNA(LOOKUP(1,0/COUNTIFS(P5:AB5,P$1+{1,0,-1}),{1,0,-1}),"")... -> None | BD6: '=SUM(AE6:AO6)' -> 3 | BE6: '=SUM(AE6:AP6)' -> 3 | BF6: '=SUM(AE6:AQ6)' -> 4 | BG6: '=IF(COUNTIF(AT6:AY6,0)>2,"a","")' -> None | BD7: '=SUM(AE7:AO7)' -> 2 | BE7: '=SUM(AE7:AP7)' -> 2 | BF7: '=SUM(AE7:AQ7)' -> 3 | BG7: '=IF(COUNTIF(AT7:AY7,0)>2,"a","")' -> 'a' | BH7: 'e'

### `712151c9ae8c|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|c6719e`

- workbook: `all_data_912_v0.1/spreadsheet/57728/1_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 34 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `19dfd5dbcec5|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|413471`

- workbook: `all_data_912_v0.1/spreadsheet/53062/3_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AE on formamspnc (7) feeds 80 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, formamspnc (7)!BQ5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> None | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> '1'

### `ac9c457a4aed|HIDDEN_STRUCTURE_IN_TOTAL|Compiledandlocatedschoolsda!B2|672ed9`

- workbook: `all_data_912_v0.1/spreadsheet/55427/3_55427_input.xlsx`
- location: `Compiled and located schools da!B2`  severity: Medium  confidence: Review
- formula: `=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$1461,0))`
- evidence: Hidden row 74 on URN lookup feeds 12 visible formula(s): Compiled and located schools da!B2, Compiled and located schools da!B3, Compiled and located schools da!B4, Compiled and located schools da!B5, Compiled and located schools da!B6, Compiled and located schools da!B7, Compiled and located schools da!B8, Compiled and located schools da!B9, ....
- cached value: '#N/A'; row labels: []; column header: "'DFES check'"; used range: A1:AJ1419
- range 'URN lookup'!$D$2:$D$1461: values ['2001', '2004', '2005', '2008', '2010', '2014', '2019', '2020', '2027', '2028', '2032', '2033']; beyond: {'above': "D1: 'ESTAB'", 'below': 'D1462: None'}
- neighbourhood: A1: 'URN' | B1: 'DFES check' | C1: 'DfE Number' | D1: 'County' | B2: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L2,'URN lookup'!$K$2:$K$146... -> '#N/A' | D2: 'Cumbria' | B3: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L3,'URN lookup'!$K$2:$K$146... -> '#N/A' | D3: 'Cumbria' | B4: "=INDEX('URN lookup'!$D$2:$D$1461,MATCH(L4,'URN lookup'!$K$2:$K$146... -> '#N/A' | D4: 'Cumbria'

### `d7bb3bd8958a|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!B25|d7e1cd`

- workbook: `all_data_912_v0.1/spreadsheet/57989/1_57989_input.xlsx`
- location: `Sheet1!B25`  severity: Medium  confidence: Review
- formula: `=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:$U$1,0)))`
- evidence: Hidden row 12 on Sheet1 feeds 133 visible formula(s): Sheet1!B25, Sheet1!C25, Sheet1!D25, Sheet1!E25, Sheet1!F25, Sheet1!G25, Sheet1!H25, Sheet1!B26, ....
- cached value: 0; row labels: ["'Driver 1'"]; column header: "'Friday'"; used range: A1:Y118
- range $A$1:$U$21: values ['None', "'Friday'", "'Saturday'", "'Sunday'", "'Monday'", "'Tuesday'", "'Wednesday'", "'Thursday'", "'Friday'", "'Saturday'", "'Sunday'", "'Monday'"]; beyond: {}
- neighbourhood: A23: 'Synthese' | B24: 'Friday' | C24: 'Saturday' | D24: 'Sunday' | A25: 'Driver 1' | B25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D25: '=COUNTA(INDEX($A$1:$U$21,MATCH($A25,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 1 | A26: 'Driver 2' | B26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 1 | C26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 0 | D26: '=COUNTA(INDEX($A$1:$U$21,MATCH($A26,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0 | A27: 'Driver 3' | B27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(B$24,$A$1:... -> 0 | C27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(C$24,$A$1:... -> 1 | D27: '=COUNTA(INDEX($A$1:$U$21,MATCH($A27,$A$1:$A$21,0),MATCH(D$24,$A$1:... -> 0

### `970db979d624|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|c9282e`

- workbook: `all_data_912_v0.1/spreadsheet/53062/2_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column V on formamspnc (7) feeds 103 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BF5, formamspnc (7)!BJ5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!O6, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> None | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> None

### `cb6809749f05|HIDDEN_STRUCTURE_IN_TOTAL|Sheet2!B1|4727cf`

- workbook: `all_data_912_v0.1/spreadsheet/57728/3_57728_input.xlsx`
- location: `Sheet2!B1`  severity: Medium  confidence: Review
- formula: `=_xlfn.AGGREGATE(9,3,B3:B96)`
- evidence: Hidden row 53 on Sheet2 feeds 6 visible formula(s): Sheet2!B1, Sheet2!C1, Sheet2!D1, Sheet2!E1, Sheet2!F1, Sheet2!G1.
- cached value: 0; row labels: []; column header: ''; used range: A1:J96
- range B3:B96: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'B2: 1', 'below': 'B97: None'}
- neighbourhood: B1: '=_xlfn.AGGREGATE(9,3,B3:B96)' -> 0 | C1: '=_xlfn.AGGREGATE(2,3,C3:C96)' -> 0 | D1: '=_xlfn.AGGREGATE(3,3,D3:D96)' -> 0 | A2: 'Column' | B2: 1 | C2: 2 | D2: 3

### `c2c1c9ef2579|HIDDEN_STRUCTURE_IN_TOTAL|formamspnc(7)!O5|413471`

- workbook: `all_data_912_v0.1/spreadsheet/53062/1_53062_input.xlsx`
- location: `formamspnc (7)!O5`  severity: Medium  confidence: Review
- formula: `=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")`
- evidence: Hidden column AE on formamspnc (7) feeds 80 visible formula(s): formamspnc (7)!O5, formamspnc (7)!BK5, formamspnc (7)!BL5, formamspnc (7)!BM5, formamspnc (7)!BN5, formamspnc (7)!BO5, formamspnc (7)!BP5, formamspnc (7)!BQ5, ....
- cached value: None; row labels: ["'1 ext,1st 1 ext'"]; column header: ''; used range: A1:ED48610
- range AE5:AO5: values ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'AD5: None', 'right': 'AP5: None'}
- neighbourhood: O5: '=IF(COUNTIF(AE5:AO5,$V$3)>=$T$3,"A","")' -> None | P5: '=IF(COUNTIF(AE5:AN5,$W$3)>=$U$3,"B","")' -> None | M6: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE6&AF6&AG6&AH6&... -> None | N6: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE6&AF6&AG6&AH6&AI6&A... -> None | O6: '=IF(COUNTIF(AE6:AO6,$V$3)>=$T$3,"A","")' -> None | P6: '=IF(COUNTIF(AE6:AN6,$W$3)>=$U$3,"B","")' -> None | Q6: '=IF(AND(SEARCH("1st",C6)>0,BH6="e"),"1","")' -> '1' | M7: '=IF(ISNUMBER(SEARCH($AK$3&$AL$3&$AM$3&$AN$3&$AO$3,AE7&AF7&AG7&AH7&... -> None | N7: '=IF(ISNUMBER(SEARCH($A$3&$B$3&$C$3&$D$3&$E$3,AE7&AF7&AG7&AH7&AI7&A... -> None | O7: '=IF(COUNTIF(AE7:AO7,$V$3)>=$T$3,"A","")' -> 'A' | P7: '=IF(COUNTIF(AE7:AN7,$W$3)>=$U$3,"B","")' -> None | Q7: '=IF(AND(SEARCH("1st",C7)>0,BH7="e"),"1","")' -> None

### `a556b2a52595|HIDDEN_STRUCTURE_IN_TOTAL|Sheet1!H8`

- workbook: `all_data_912_v0.1/spreadsheet/32789/2_32789_input.xlsx`
- location: `Sheet1!H8`  severity: Medium  confidence: Review
- formula: `=IF(AND(NOT(ISBLANK($N10)),$K10>0,$AW10>0),IFERROR(F8/D8,""),"")`
- evidence: Hidden column N on Sheet1 feeds 8 visible formula(s): Sheet1!H8, Sheet1!H9, Sheet1!H10, Sheet1!H11, Sheet1!H12, Sheet1!H13, Sheet1!G14, Sheet1!H14.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- neighbourhood: F6: 0.0818713450292398 | G6: 0.0818713450292398 | H6: 0.909681611435997 | I6: 0.909681611435997 | F7: 0.0867052023121387 | G7: 0.0867052023121387 | H7: 0.867052023121387 | I7: 0.867052023121387 | F8: '=IF(AND(NOT(ISBLANK(E8)),B8>0,$AW10>0),IFERROR(E8/B8,""),"")' -> None | G8: '=IF(AND(NOT(ISBLANK(E8)),B8>0,$AW10>0),IFERROR(E8/B8,""),"")' -> None | H8: '=IF(AND(NOT(ISBLANK($N10)),$K10>0,$AW10>0),IFERROR(F8/D8,""),"")' -> None | I8: '=IF(MAX(G8,H8)=0,"",MAX(G8,H8))' -> None | F9: '=IF(AND(NOT(ISBLANK(E9)),B9>0,$AW11>0),IFERROR(E9/B9,""),"")' -> None | G9: '=IF(AND(NOT(ISBLANK(E9)),B9>0,$AW11>0),IFERROR(E9/B9,""),"")' -> None | H9: '=IF(AND(NOT(ISBLANK($N11)),$K11>0,$AW11>0),IFERROR(F9/D9,""),"")' -> None | I9: '=IF(MAX(G9,H9)=0,"",MAX(G9,H9))' -> None | F10: '=IF(AND(NOT(ISBLANK(E10)),B10>0,$AW12>0),IFERROR(E10/B10,""),"")' -> None | G10: '=IF(AND(NOT(ISBLANK(E10)),B10>0,$AW12>0),IFERROR(E10/B10,""),"")' -> None | H10: '=IF(AND(NOT(ISBLANK($N12)),$K12>0,$AW12>0),IFERROR(F10/D10,""),"")' -> None | I10: '=IF(MAX(G10,H10)=0,"",MAX(G10,H10))' -> None

### `158be0e0e878|HIDDEN_STRUCTURE_IN_TOTAL|Employee3!U3`

- workbook: `all_data_912_v0.1/spreadsheet/382-29/1_382-29_input.xlsx`
- location: `Employee 3!U3`  severity: Medium  confidence: Review
- formula: `=$B23`
- evidence: Hidden row 23 on Employee 3 feeds 24 visible formula(s): Employee 3!U3, Employee 3!AB5, Employee 3!AB6, Employee 3!AB7, Employee 3!AB8, Employee 3!AB9, Employee 3!AB10, Employee 3!AB11, ....
- cached value: 'Test 19'; row labels: []; column header: ''; used range: A1:AB30
- neighbourhood: S3: '=$B21' -> 'Test 17' | T3: '=$B22' -> 'Test 18' | U3: '=$B23' -> 'Test 19' | V3: '=$B24' -> 'Test 20' | W3: '=$B25' -> 'Test 21' | S4: 'Q' | T4: 'R' | U4: 'S' | V4: 'T' | W4: 'U' | S5: 'X' | T5: 'X' | U5: 'X' | V5: 'X' | W5: 'X'

## IFERROR_MASK

### `ad4d62f904c7|IFERROR_MASK|Sheet1!L31`

- workbook: `all_data_912_v0.1/spreadsheet/45738/1_45738_input.xlsx`
- location: `Sheet1!L31`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B10,0)+(EOMONTH($D10,0)=L$4)*$A10`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: J29: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | K29: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | L29: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | M29: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 1040 | N29: '=IFERROR((MOD(DATEDIF(N$4+1,EOMONTH($D8,0)+1,"m"),12/$C8)=0)*$B8,0... -> 0 | J30: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | K30: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | L30: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | M30: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | N30: '=IFERROR((MOD(DATEDIF(N$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | J31: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | K31: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | L31: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | M31: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | N31: '=IFERROR((MOD(DATEDIF(N$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | J32: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | K32: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | L32: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | M32: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | N32: '=IFERROR((MOD(DATEDIF(N$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | J33: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 1110 | K33: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | L33: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | M33: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | N33: '=IFERROR((MOD(DATEDIF(N$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0

### `1a947d3f59c7|IFERROR_MASK|Sheet1!K35`

- workbook: `all_data_912_v0.1/spreadsheet/45738/3_45738_input.xlsx`
- location: `Sheet1!K35`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B14,0)+(EOMONTH($D14,0)=K$4)*$A14`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: I33: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | J33: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 111111 | K33: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | L33: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | M33: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | I34: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | J34: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | K34: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | L34: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 1160 | M34: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | I35: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 1180 | J35: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 0 | K35: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 0 | L35: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 0 | M35: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 0 | I36: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D15,0)+1,"m"),12/$C15)=0)*$B1... -> 0 | J36: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D15,0)+1,"m"),12/$C15)=0)*$B1... -> 0 | K36: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D15,0)+1,"m"),12/$C15)=0)*$B1... -> 0 | L36: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D15,0)+1,"m"),12/$C15)=0)*$B1... -> 0 | M36: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D15,0)+1,"m"),12/$C15)=0)*$B1... -> 0 | I37: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D16,0)+1,"m"),12/$C16)=0)*$B1... -> 0 | J37: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D16,0)+1,"m"),12/$C16)=0)*$B1... -> 0 | K37: '=IFERROR((MOD(DATEDIF(K$4+1,EOMONTH($D16,0)+1,"m"),12/$C16)=0)*$B1... -> 0 | L37: '=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D16,0)+1,"m"),12/$C16)=0)*$B1... -> 0 | M37: '=IFERROR((MOD(DATEDIF(M$4+1,EOMONTH($D16,0)+1,"m"),12/$C16)=0)*$B1... -> 0

### `ad4d62f904c7|IFERROR_MASK|Sheet1!AB33`

- workbook: `all_data_912_v0.1/spreadsheet/45738/1_45738_input.xlsx`
- location: `Sheet1!AB33`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B12,0)+(EOMONTH($D12,0)=AB$4)*$A12`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: Z31: '=IFERROR((MOD(DATEDIF(Z$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | AA31: '=IFERROR((MOD(DATEDIF(AA$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B... -> 0 | AB31: '=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B... -> 0 | Z32: '=IFERROR((MOD(DATEDIF(Z$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | AA32: '=IFERROR((MOD(DATEDIF(AA$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B... -> 0 | AB32: '=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B... -> 0 | Z33: '=IFERROR((MOD(DATEDIF(Z$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | AA33: '=IFERROR((MOD(DATEDIF(AA$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B... -> 0 | AB33: '=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B... -> 0 | Z34: '=IFERROR((MOD(DATEDIF(Z$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | AA34: '=IFERROR((MOD(DATEDIF(AA$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B... -> 0 | AB34: '=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B... -> 0 | Z35: '=IFERROR((MOD(DATEDIF(Z$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B1... -> 0 | AA35: '=IFERROR((MOD(DATEDIF(AA$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B... -> 0 | AB35: '=IFERROR((MOD(DATEDIF(AB$4+1,EOMONTH($D14,0)+1,"m"),12/$C14)=0)*$B... -> 0

### `1a947d3f59c7|IFERROR_MASK|Sheet1!H32`

- workbook: `all_data_912_v0.1/spreadsheet/45738/3_45738_input.xlsx`
- location: `Sheet1!H32`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B11,0)+(EOMONTH($D11,0)=H$4)*$A11`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: F30: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 1060 | G30: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | H30: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | I30: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | J30: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D9,0)+1,"m"),12/$C9)=0)*$B9,0... -> 0 | F31: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | G31: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | H31: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | I31: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 1023 | J31: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B1... -> 0 | F32: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | G32: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | H32: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | I32: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | J32: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D11,0)+1,"m"),12/$C11)=0)*$B1... -> 0 | F33: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | G33: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | H33: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | I33: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 0 | J33: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D12,0)+1,"m"),12/$C12)=0)*$B1... -> 111111 | F34: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 1160 | G34: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | H34: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | I34: '=IFERROR((MOD(DATEDIF(I$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0 | J34: '=IFERROR((MOD(DATEDIF(J$4+1,EOMONTH($D13,0)+1,"m"),12/$C13)=0)*$B1... -> 0

### `233b4f90d078|IFERROR_MASK|Form!J17`

- workbook: `all_data_912_v0.1/spreadsheet/59969/3_59969_input.xlsx`
- location: `Form!J17`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3)*(Report!$B$2:$B$70000=Form!$B$5),ROW(Report!$A$2:$A$70000)),ROWS($A$1:G12))),"")`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:M26
- range Report!$A$2:$A$70000: values ['None', '2073000108', '2073000108', '2073000108', '2073000108', '2073000108', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116']; beyond: {'above': 'A1: None', 'below': 'A70001: None'}
- neighbourhood: H15: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I15: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J15: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K15: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | L15: '=IFERROR(INDEX(Report!O:O,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 'CS' | H16: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I16: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J16: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K16: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | L16: '=IFERROR(INDEX(Report!O:O,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 'MS' | H17: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I17: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J17: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K17: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | L17: '=IFERROR(INDEX(Report!O:O,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 'OS' | H18: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I18: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J18: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K18: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | L18: '=IFERROR(INDEX(Report!O:O,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 'BL' | H19: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 400 | I19: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 115 | J19: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K19: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | L19: '=IFERROR(INDEX(Report!O:O,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 'CC'

### `c903fcb4672b|IFERROR_MASK|RS.Food!I171`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!I171`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A171,$O$5:$O$271),)),"")`
- evidence: Formula uses IFERROR.
- cached value: 'Dessert'; row labels: ["'Ice Cream 3 Sc'"]; column header: ''; used range: A1:W607
- range $N$5:$N$271: values ["'Type'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'"]; beyond: {'above': 'N4: None', 'below': 'N272: None'}
- neighbourhood: G169: 27 | H169: 13.2962962962963 | I169: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A169,$O$5:$O$271),)),"... -> 'Dessert' | J169: '=IF(I169="","",IF(E169="","",G169))' -> 27 | K169: '=IF(J169="","",SUMPRODUCT((I169=$I$6:$I$1500)*(B169<$B$6:$B$1500))... -> 4 | G170: 151 | H170: 1.5 | I170: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A170,$O$5:$O$271),)),"... -> 'Dessert' | J170: '=IF(I170="","",IF(E170="","",G170))' -> 151 | K170: '=IF(J170="","",SUMPRODUCT((I170=$I$6:$I$1500)*(B170<$B$6:$B$1500))... -> 5 | G171: 19 | H171: 8 | I171: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A171,$O$5:$O$271),)),"... -> 'Dessert' | J171: '=IF(I171="","",IF(E171="","",G171))' -> 19 | K171: '=IF(J171="","",SUMPRODUCT((I171=$I$6:$I$1500)*(B171<$B$6:$B$1500))... -> 6 | G172: 25 | H172: 4 | I172: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A172,$O$5:$O$271),)),"... -> 'Dessert' | J172: '=IF(I172="","",IF(E172="","",G172))' -> 25 | K172: '=IF(J172="","",SUMPRODUCT((I172=$I$6:$I$1500)*(B172<$B$6:$B$1500))... -> 7 | G173: 6 | H173: 12 | I173: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A173,$O$5:$O$271),)),"... -> 'Dessert' | J173: '=IF(I173="","",IF(E173="","",G173))' -> 6 | K173: '=IF(J173="","",SUMPRODUCT((I173=$I$6:$I$1500)*(B173<$B$6:$B$1500))... -> 8

### `eb31bc468d52|IFERROR_MASK|Form!I10`

- workbook: `all_data_912_v0.1/spreadsheet/59969/2_59969_input.xlsx`
- location: `Form!I10`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3)*(Report!$B$2:$B$70000=Form!$B$5),ROW(Report!$A$2:$A$70000)),ROWS($A$1:F5))),"")`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:M26
- range Report!$A$2:$A$70000: values ['None', '2073000108', '2073000108', '2073000108', '2073000108', '2073000108', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116']; beyond: {'above': 'A1: None', 'below': 'A70001: None'}
- neighbourhood: G8: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H8: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I8: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J8: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K8: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G9: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H9: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I9: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J9: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K9: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G10: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H10: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I10: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J10: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K10: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G11: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H11: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I11: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J11: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | K11: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G12: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H12: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | I12: '=IFERROR(INDEX(Report!L:L,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | J12: '=IFERROR(INDEX(Report!M:M,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 333 | K12: '=IFERROR(INDEX(Report!N:N,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0

### `67c2c6d7849a|IFERROR_MASK|Data!J19`

- workbook: `all_data_912_v0.1/spreadsheet/44017/1_44017_input.xlsx`
- location: `Data!J19`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP(I19,$I$6:$J$8,2,FALSE),"Select freq")`
- evidence: Formula uses IFERROR.
- cached value: 1; row labels: ["'Annually'"]; column header: ''; used range: A1:BX42
- range $I$6:$J$8: values ["'Annually'", '1', "'Semi-annually'", '6', "'Quaterly'", '3']; beyond: {}
- neighbourhood: I17: 'Quaterly' | J17: '=IFERROR(VLOOKUP(I17,$I$6:$J$8,2,FALSE),"Select freq")' -> 3 | K17: 'Approved' | L17: 2022-09-01 00:00:00 | I18: 'Annually' | J18: '=IFERROR(VLOOKUP(I18,$I$6:$J$8,2,FALSE),"Select freq")' -> 1 | K18: 'Approved' | L18: 2022-07-01 00:00:00 | I19: 'Annually' | J19: '=IFERROR(VLOOKUP(I19,$I$6:$J$8,2,FALSE),"Select freq")' -> 1 | K19: 'Approved' | L19: 2022-07-01 00:00:00 | I20: 'Annually' | J20: '=IFERROR(VLOOKUP(I20,$I$6:$J$8,2,FALSE),"Select freq")' -> 1 | K20: 'Approved' | L20: 2022-07-01 00:00:00 | I21: 'Annually' | J21: '=IFERROR(VLOOKUP(I21,$I$6:$J$8,2,FALSE),"Select freq")' -> 1 | K21: 'Approved' | L21: 2022-07-01 00:00:00

### `c903fcb4672b|IFERROR_MASK|RS.Food!I164`

- workbook: `all_data_912_v0.1/spreadsheet/50193/2_50193_input.xlsx`
- location: `RS.Food!I164`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A164,$O$5:$O$271),)),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Extra Topping'"]; column header: ''; used range: A1:W607
- range $N$5:$N$271: values ["'Type'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'"]; beyond: {'above': 'N4: None', 'below': 'N272: None'}
- neighbourhood: G162: 41 | H162: 22 | I162: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A162,$O$5:$O$271),)),"... -> 'Pizza' | J162: '=IF(I162="","",IF(E162="","",G162))' -> 41 | K162: '=IF(J162="","",SUMPRODUCT((I162=$I$6:$I$1500)*(B162<$B$6:$B$1500))... -> 2 | G163: 41 | H163: 18 | I163: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A163,$O$5:$O$271),)),"... -> 'Pizza' | J163: '=IF(I163="","",IF(E163="","",G163))' -> 41 | K163: '=IF(J163="","",SUMPRODUCT((I163=$I$6:$I$1500)*(B163<$B$6:$B$1500))... -> 3 | G164: 46 | H164: 0 | I164: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A164,$O$5:$O$271),)),"... -> None | J164: '=IF(I164="","",IF(E164="","",G164))' -> None | K164: '=IF(J164="","",SUMPRODUCT((I164=$I$6:$I$1500)*(B164<$B$6:$B$1500))... -> None | G165: 385 | H165: 7.80649350649351 | I165: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A165,$O$5:$O$271),)),"... -> None | J165: '=IF(I165="","",IF(E165="","",G165))' -> None | K165: '=IF(J165="","",SUMPRODUCT((I165=$I$6:$I$1500)*(B165<$B$6:$B$1500))... -> None | G166: 66 | H166: 14 | I166: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A166,$O$5:$O$271),)),"... -> 'Dessert' | J166: '=IF(I166="","",IF(E166="","",G166))' -> 66 | K166: '=IF(J166="","",SUMPRODUCT((I166=$I$6:$I$1500)*(B166<$B$6:$B$1500))... -> 1

### `7149679332c0|IFERROR_MASK|RESULTS1!R16`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!R16`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CAP],"<=500000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),0)`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: ["'ATI'", "'100-500M'"]; column header: ''; used range: A1:W67
- neighbourhood: P14: 'TRADES' | Q14: '1-3M' | R14: '3-5M' | S14: '5-10M' | T14: '10-20M' | P15: '< 100M' | Q15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 1 | R15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 2 | S15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 6 | T15: '=IFERROR(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT],">... -> 3 | P16: '100-500M' | Q16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 3 | R16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | S16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 3 | T16: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 5 | P17: '500M-1B' | Q17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | R17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | S17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | T17: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | P18: '1B <' | Q18: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | R18: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | S18: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | T18: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0

### `21865bab73e8|IFERROR_MASK|RS.Food!I143`

- workbook: `all_data_912_v0.1/spreadsheet/50193/1_50193_input.xlsx`
- location: `RS.Food!I143`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A143,$O$5:$O$271),)),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'LunchA Junket'"]; column header: ''; used range: A1:W607
- range $N$5:$N$271: values ["'Type'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'"]; beyond: {'above': 'N4: None', 'below': 'N272: None'}
- neighbourhood: G141: 57 | H141: 38 | I141: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A141,$O$5:$O$271),)),"... -> None | J141: '=IF(I141="","",IF(E141="","",G141))' -> None | K141: '=IF(J141="","",SUMPRODUCT((I141=$I$6:$I$1500)*(B141<$B$6:$B$1500))... -> None | G142: 64 | H142: 30 | I142: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A142,$O$5:$O$271),)),"... -> None | J142: '=IF(I142="","",IF(E142="","",G142))' -> None | K142: '=IF(J142="","",SUMPRODUCT((I142=$I$6:$I$1500)*(B142<$B$6:$B$1500))... -> None | G143: 26 | H143: 20 | I143: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A143,$O$5:$O$271),)),"... -> None | J143: '=IF(I143="","",IF(E143="","",G143))' -> None | K143: '=IF(J143="","",SUMPRODUCT((I143=$I$6:$I$1500)*(B143<$B$6:$B$1500))... -> None | G144: 11 | H144: 32 | I144: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A144,$O$5:$O$271),)),"... -> None | J144: '=IF(I144="","",IF(E144="","",G144))' -> None | K144: '=IF(J144="","",SUMPRODUCT((I144=$I$6:$I$1500)*(B144<$B$6:$B$1500))... -> None | G145: 5 | H145: 60 | I145: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A145,$O$5:$O$271),)),"... -> None | J145: '=IF(I145="","",IF(E145="","",G145))' -> None | K145: '=IF(J145="","",SUMPRODUCT((I145=$I$6:$I$1500)*(B145<$B$6:$B$1500))... -> None

### `65228fa5c9a0|IFERROR_MASK|RS.Food!I180`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!I180`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A180,$O$5:$O$271),)),"")`
- evidence: Formula uses IFERROR.
- cached value: 'Dessert'; row labels: ["'Vegan Eaton Mess'"]; column header: ''; used range: A1:W607
- range $N$5:$N$271: values ["'Type'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'"]; beyond: {'above': 'N4: None', 'below': 'N272: None'}
- neighbourhood: G178: 1 | H178: 12 | I178: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A178,$O$5:$O$271),)),"... -> 'Dessert' | J178: '=IF(I178="","",IF(E178="","",G178))' -> 1 | K178: '=IF(J178="","",SUMPRODUCT((I178=$I$6:$I$1500)*(B178<$B$6:$B$1500))... -> 13 | G179: 1 | H179: 12 | I179: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A179,$O$5:$O$271),)),"... -> 'Dessert' | J179: '=IF(I179="","",IF(E179="","",G179))' -> 1 | K179: '=IF(J179="","",SUMPRODUCT((I179=$I$6:$I$1500)*(B179<$B$6:$B$1500))... -> 13 | G180: 1 | H180: 12 | I180: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A180,$O$5:$O$271),)),"... -> 'Dessert' | J180: '=IF(I180="","",IF(E180="","",G180))' -> 1 | K180: '=IF(J180="","",SUMPRODUCT((I180=$I$6:$I$1500)*(B180<$B$6:$B$1500))... -> 13 | G181: 4 | H181: 2.5 | I181: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A181,$O$5:$O$271),)),"... -> 'Dessert' | J181: '=IF(I181="","",IF(E181="","",G181))' -> 4 | K181: '=IF(J181="","",SUMPRODUCT((I181=$I$6:$I$1500)*(B181<$B$6:$B$1500))... -> 16 | G182: 5 | H182: 0 | I182: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A182,$O$5:$O$271),)),"... -> None | J182: '=IF(I182="","",IF(E182="","",G182))' -> None | K182: '=IF(J182="","",SUMPRODUCT((I182=$I$6:$I$1500)*(B182<$B$6:$B$1500))... -> None

### `5cd8c4fe9805|IFERROR_MASK|RESULTS1!U11`

- workbook: `all_data_912_v0.1/spreadsheet/49613/2_49613_input.xlsx`
- location: `RESULTS 1!U11`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">10000000",Table1[FLOAT],"<=20000000"),"")`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: ["'RULES'", "'1B <'"]; column header: ''; used range: A1:X80
- neighbourhood: S9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | T9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | U9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | V9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | W9: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET CA... -> 0 | S10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | T10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | U10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | V10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | W10: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CA... -> 0 | S11: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | T11: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | U11: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | V11: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | W11: '=IFERROR(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],"... -> 0 | S13: '3-5M' | T13: '5-10M' | U13: '10-20M' | V13: '20-50M' | W13: '50-100M'

### `f97f2feedd64|IFERROR_MASK|RESULTS1!F43`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!F43`  severity: Medium  confidence: Review
- formula: `=IFERROR(COUNTIFS(Table1[SETUP],B43,Table1[POINTS G/L],">=0",Table1[WEEK],">="&MAX(Table1[WEEK])-4)/COUNTIFS(Table1[SETUP],B43,Table1[WEEK],">="&MAX(Table1[WEEK])-4),"")`
- evidence: Formula uses IFERROR.
- cached value: 1; row labels: ["'PM Consolidation'"]; column header: ''; used range: A1:W67
- neighbourhood: D41: 'Trades %' | E41: 'Win %' | F41: 'Last 5 Wk' | G41: 'Points G/L' | H41: 'Entry %' | D42: '=SUM(COUNTIF(Table1[SETUP],B42)/COUNTA(Table1[SETUP]))' -> 0.46551724137931 | E42: '=SUM(COUNTIFS(Table1[SETUP],B42,Table1[POINTS G/L],">=0")/COUNTIF(... -> 0.592592592592593 | F42: '=IFERROR(COUNTIFS(Table1[SETUP],B42,Table1[POINTS G/L],">=0",Table... -> 0.666666666666667 | G42: '=SUMIFS(Table1[POINTS G/L],Table1[SETUP],B42)' -> 30.66 | H42: '=COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[SETUP],B42)/COUNTIFS(T... -> 0.777777777777778 | D43: '=SUM(COUNTIF(Table1[SETUP],B43)/COUNTA(Table1[SETUP]))' -> 0.310344827586207 | E43: '=SUM(COUNTIFS(Table1[SETUP],B43,Table1[POINTS G/L],">=0")/COUNTIF(... -> 1 | F43: '=IFERROR(COUNTIFS(Table1[SETUP],B43,Table1[POINTS G/L],">=0",Table... -> 1 | G43: '=SUMIFS(Table1[POINTS G/L],Table1[SETUP],B43)' -> 57.54 | H43: '=COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[SETUP],B43)/COUNTIFS(T... -> 0.9375 | D44: '=SUM(COUNTIF(Table1[SETUP],B44)/COUNTA(Table1[SETUP]))' -> 0.0689655172413793 | E44: '=SUM(COUNTIFS(Table1[SETUP],B44,Table1[POINTS G/L],">=0")/COUNTIF(... -> 0.75 | F44: '=IFERROR(COUNTIFS(Table1[SETUP],B44,Table1[POINTS G/L],">=0",Table... -> 0.5 | G44: '=SUMIFS(Table1[POINTS G/L],Table1[SETUP],B44)' -> 6.87 | H44: '=COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[SETUP],B44)/COUNTIFS(T... -> 0.333333333333333 | D45: '=SUM(COUNTIF(Table1[SETUP],B45)/COUNTA(Table1[SETUP]))' -> 0.0344827586206897 | E45: '=SUM(COUNTIFS(Table1[SETUP],B45,Table1[POINTS G/L],">=0")/COUNTIF(... -> 1 | F45: '=IFERROR(COUNTIFS(Table1[SETUP],B45,Table1[POINTS G/L],">=0",Table... -> 1 | G45: '=SUMIFS(Table1[POINTS G/L],Table1[SETUP],B45)' -> 2.52 | H45: '=COUNTIFS(Table1[ENTRY ATTEMPT],"=1",Table1[SETUP],B45)/COUNTIFS(T... -> 1

### `65228fa5c9a0|IFERROR_MASK|RS.Food!I157`

- workbook: `all_data_912_v0.1/spreadsheet/50193/3_50193_input.xlsx`
- location: `RS.Food!I157`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A157,$O$5:$O$271),)),"")`
- evidence: Formula uses IFERROR.
- cached value: 'Salads'; row labels: ["'Vegan Bowl'"]; column header: ''; used range: A1:W607
- range $N$5:$N$271: values ["'Type'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'", "'Starter'"]; beyond: {'above': 'N4: None', 'below': 'N272: None'}
- neighbourhood: G155: 5 | H155: 10 | I155: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A155,$O$5:$O$271),)),"... -> 'Salads' | J155: '=IF(I155="","",IF(E155="","",G155))' -> 5 | K155: '=IF(J155="","",SUMPRODUCT((I155=$I$6:$I$1500)*(B155<$B$6:$B$1500))... -> 9 | G156: 3 | H156: 12 | I156: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A156,$O$5:$O$271),)),"... -> 'Salads' | J156: '=IF(I156="","",IF(E156="","",G156))' -> 3 | K156: '=IF(J156="","",SUMPRODUCT((I156=$I$6:$I$1500)*(B156<$B$6:$B$1500))... -> 10 | G157: 1 | H157: 18 | I157: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A157,$O$5:$O$271),)),"... -> 'Salads' | J157: '=IF(I157="","",IF(E157="","",G157))' -> 1 | K157: '=IF(J157="","",SUMPRODUCT((I157=$I$6:$I$1500)*(B157<$B$6:$B$1500))... -> 11 | G158: 1 | H158: 15 | I158: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A158,$O$5:$O$271),)),"... -> 'Salads' | J158: '=IF(I158="","",IF(E158="","",G158))' -> 1 | K158: '=IF(J158="","",SUMPRODUCT((I158=$I$6:$I$1500)*(B158<$B$6:$B$1500))... -> 12 | G159: 1 | H159: 10 | I159: '=IFERROR(INDEX($N$5:$N$271,MATCH(TRUE,EXACT(A159,$O$5:$O$271),)),"... -> 'Salads' | J159: '=IF(I159="","",IF(E159="","",G159))' -> 1 | K159: '=IF(J159="","",SUMPRODUCT((I159=$I$6:$I$1500)*(B159<$B$6:$B$1500))... -> 13

### `125be9ba2e04|IFERROR_MASK|RESULTS1!V28`

- workbook: `all_data_912_v0.1/spreadsheet/49613/1_49613_input.xlsx`
- location: `RESULTS 1!V28`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000")>=10,AVERAGEIFS(Table1[POINTS],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">20000000",Table1[FLOAT],"<=50000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Trades'", "'500M-1B'"]; column header: ''; used range: A1:X80
- neighbourhood: T26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | V26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | W26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | X26: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | V27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | W27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[MARKET... -> None | X27: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | V28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | W28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | X28: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | V29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | W29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | X29: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `a3ce241a69c4|IFERROR_MASK|InvoicePayments!I16`

- workbook: `all_data_912_v0.1/spreadsheet/118-8/3_118-8_input.xlsx`
- location: `Invoice Payments!I16`  severity: Medium  confidence: Review
- formula: `=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[Paid Amount]],"")`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: ["'Anita Withers'"]; column header: "'Outstanding Amount'"; used range: A1:S72
- neighbourhood: I14: 'Green colored columns are automatica... | G15: 'Invoice Amount' | H15: 'Paid Amount' | I15: 'Outstanding Amount' | J15: 'Status' | K15: 'Past Due Age' | G16: 200 | H16: 200 | I16: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 0 | J16: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAID IN FULL' | K16: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> None | G17: 400 | I17: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 400 | J17: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAST DUE' | K17: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> '91+ Days' | G18: 76.04 | I18: '=IFERROR(T_INV3[[#This Row],[Invoice Amount]]-T_INV3[[#This Row],[... -> 76.04 | J18: '=IFERROR(IF(OR(T_INV3[[#This Row],[Invoice Amount]]="",T_INV3[[#Th... -> 'PAST DUE' | K18: '=IFERROR(IF(T_INV3[[#This Row],[Status]]="PAST DUE",IF(TD-T_INV3[[... -> '91+ Days'

### `7dfe4964af12|IFERROR_MASK|Sheet1!C7`

- workbook: `all_data_912_v0.1/spreadsheet/32789/3_32789_input.xlsx`
- location: `Sheet1!C7`  severity: Medium  confidence: Review
- formula: `=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BE$4:$BE$82)*$AY9,0),""),"")`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: []; column header: ''; used range: A1:BR82
- range $BD$4:$BD$82: values ['2023-10-16 00:00:00', '2023-10-23 00:00:00', '2023-10-30 00:00:00', '2023-11-06 00:00:00', '2023-11-13 00:00:00', '2023-11-13 00:00:00', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': "BD3: 'Date'", 'below': 'BD83: None'}
- neighbourhood: A5: 2023-11-06 00:00:00 | B5: 169 | C5: '=IF(AND(B5>0,$AW7>0,ISNUMBER(MATCH(#REF!,$BD$3:$BD$81,0)),ISNUMBER... -> None | D5: '=IF(AND(B5>0,$AW7>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E5: 13 | A6: 2023-10-30 00:00:00 | B6: 171 | C6: '=IF(AND(B6>0,$AW8>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D6: '=IF(AND(B6>0,$AW8>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E6: 14 | A7: 2023-11-06 00:00:00 | B7: 173 | C7: '=IF(AND(B7>0,$AW9>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$BD... -> None | D7: '=IF(AND(B7>0,$AW9>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF$... -> None | E7: 15 | A8: 2023-11-13 00:00:00 | C8: '=IF(AND(B8>0,$AW10>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D8: '=IF(AND(B8>0,$AW10>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None | A9: 2023-11-20 00:00:00 | C9: '=IF(AND(B9>0,$AW11>0),IFERROR(ROUNDUP(_xlfn.XLOOKUP(#REF!,$BD$4:$B... -> None | D9: '=IF(AND(B9>0,$AW11>0),IFERROR(_xlfn.XLOOKUP(#REF!,$BD$4:$BD$82,$BF... -> None

### `3db55cfd98cc|IFERROR_MASK|INPUTS!D15`

- workbook: `all_data_912_v0.1/spreadsheet/52216/3_52216_input.xlsx`
- location: `INPUTS!D15`  severity: Medium  confidence: Review
- formula: `=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),MATCH(INPUTS!D3,Sheet2!C1:G1,0)),0)`
- evidence: Formula uses IFNA.
- cached value: 3.17; row labels: ["'Advertising & Marketing'"]; column header: ''; used range: A1:L23
- range Sheet2!C3:G20: values ['3.44', '3.17', '4.28', '4.29', '0.88', '1.24', '1.8', '1.78', '1.4', '1.72', '2.56', '2.53']; beyond: {}
- neighbourhood: C15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 3.44 | D15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 3.17 | E15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 4.28 | F15: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 4.29 | C16: '=_xlfn.IFNA(INDEX(Sheet2!C3:G20,MATCH(INPUTS!A14,Sheet2!A3:A20,0),... -> 3.44 | D16: '=_xlfn.IFNA(INDEX(Sheet2!D3:H20,MATCH(INPUTS!B14,Sheet2!B3:B20,0),... -> 0 | E16: '=_xlfn.IFNA(INDEX(Sheet2!E3:I20,MATCH(INPUTS!C14,Sheet2!C3:C20,0),... -> 0 | F16: '=_xlfn.IFNA(INDEX(Sheet2!F3:J20,MATCH(INPUTS!D14,Sheet2!D3:D20,0),... -> 0

### `f97f2feedd64|IFERROR_MASK|RESULTS1!R36`

- workbook: `all_data_912_v0.1/spreadsheet/50442/1_50442_input.xlsx`
- location: `RESULTS 1!R36`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000")>=10,AVERAGEIFS(Table1[POINTS G/L],Table1[MARKET CAP],">1000000000",Table1[FLOAT],">3000000",Table1[FLOAT],"<=5000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'PM Trades %'", "'1B <'"]; column header: ''; used range: A1:W67
- neighbourhood: P34: '100-500M' | Q34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | P35: '500M-1B' | Q35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | P36: '1B <' | Q36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

### `ad194e63840c|IFERROR_MASK|Edit!E16`

- workbook: `all_data_912_v0.1/spreadsheet/49667/2_49667_input.xlsx`
- location: `Edit!E16`  severity: Medium  confidence: Review
- formula: `=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY(IF(_xlpm.m="m",--_xlpm.t),IF(_xlpm.m<>"m",--_xlpm.t)),_xlpm.f,_xlfn._xlws.FILTER(TRANSPOSE(_xlfn._xlws.FILTER(_xlpm.t,_xlpm.m<>"m"))-"0:15"*_xlpm.z^{0,1},_xlpm.z,""),IFERROR(SMALL(_xlpm.f,COLUMNS($B16:E16)),""))`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'Name 15'"]; column header: ''; used range: A1:AT16
- range $F$1:$AT$1: values ["'08:00'", "'08:15'", "'08:30'", "'08:45'", "'09:00'", "'09:15'", "'09:30'", "'09:45'", "'10:00'", "'10:15'", "'10:30'", "'10:45'"]; beyond: {'left': "E1: 'Meeting Finish2'", 'right': 'AU1: None'}
- neighbourhood: C14: 10:30:00 | D14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:00:00 | E14: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F14:$AT14,_xlpm.z,FREQUENCY... -> 13:15:00 | D15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | E15: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F15:$AT15,_xlpm.z,FREQUENCY... -> None | D16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | E16: '=_xlfn.LET(_xlpm.t,$F$1:$AT$1,_xlpm.m,$F16:$AT16,_xlpm.z,FREQUENCY... -> None | F16: 'x' | G16: 'x'

### `8ca781f59931|IFERROR_MASK|Sheet1!F43`

- workbook: `all_data_912_v0.1/spreadsheet/45738/2_45738_input.xlsx`
- location: `Sheet1!F43`  severity: Medium  confidence: Review
- formula: `=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D22,0)+1,"m"),12/$C22)=0)*$B22,0)+(EOMONTH($D22,0)=F$4)*$A22`
- evidence: Formula uses IFERROR.
- cached value: 0; row labels: []; column header: ''; used range: A1:AB67
- neighbourhood: E41: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D20,0)+1,"m"),12/$C20)=0)*$B2... -> 0 | F41: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D20,0)+1,"m"),12/$C20)=0)*$B2... -> 0 | G41: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D20,0)+1,"m"),12/$C20)=0)*$B2... -> 0 | H41: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D20,0)+1,"m"),12/$C20)=0)*$B2... -> 0 | E42: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D21,0)+1,"m"),12/$C21)=0)*$B2... -> 1000 | F42: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D21,0)+1,"m"),12/$C21)=0)*$B2... -> 0 | G42: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D21,0)+1,"m"),12/$C21)=0)*$B2... -> 0 | H42: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D21,0)+1,"m"),12/$C21)=0)*$B2... -> 0 | E43: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D22,0)+1,"m"),12/$C22)=0)*$B2... -> 0 | F43: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D22,0)+1,"m"),12/$C22)=0)*$B2... -> 0 | G43: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D22,0)+1,"m"),12/$C22)=0)*$B2... -> 0 | H43: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D22,0)+1,"m"),12/$C22)=0)*$B2... -> 0 | E44: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D23,0)+1,"m"),12/$C23)=0)*$B2... -> 0 | F44: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D23,0)+1,"m"),12/$C23)=0)*$B2... -> 0 | G44: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D23,0)+1,"m"),12/$C23)=0)*$B2... -> 0 | H44: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D23,0)+1,"m"),12/$C23)=0)*$B2... -> 0 | E45: '=IFERROR((MOD(DATEDIF(E$4+1,EOMONTH($D24,0)+1,"m"),12/$C24)=0)*$B2... -> 0 | F45: '=IFERROR((MOD(DATEDIF(F$4+1,EOMONTH($D24,0)+1,"m"),12/$C24)=0)*$B2... -> 0 | G45: '=IFERROR((MOD(DATEDIF(G$4+1,EOMONTH($D24,0)+1,"m"),12/$C24)=0)*$B2... -> 1420 | H45: '=IFERROR((MOD(DATEDIF(H$4+1,EOMONTH($D24,0)+1,"m"),12/$C24)=0)*$B2... -> 0

### `34d406898185|IFERROR_MASK|Sheet1!P7`

- workbook: `all_data_912_v0.1/spreadsheet/45581/2_45581_input.xlsx`
- location: `Sheet1!P7`  severity: Medium  confidence: Review
- formula: `=IFERROR(MID($B5,COLUMNS($D7:P7),1),"")`
- evidence: Formula uses IFERROR.
- cached value: 'u'; row labels: []; column header: ''; used range: A1:AF9
- range $D7:P7: values ["'d'", "'g'", "'f'", "'h'", "'i'", "'c'", "'j'", "'s'", "'k'", "'e'", "'o'", "'i'"]; beyond: {'left': 'C7: None', 'right': "Q7: '=IFERROR(MID($B5,COLUMNS($D7:Q7),1),..."}
- neighbourhood: N7: '=IFERROR(MID($B5,COLUMNS($D7:N7),1),"")' -> 'o' | O7: '=IFERROR(MID($B5,COLUMNS($D7:O7),1),"")' -> 'i' | P7: '=IFERROR(MID($B5,COLUMNS($D7:P7),1),"")' -> 'u' | Q7: '=IFERROR(MID($B5,COLUMNS($D7:Q7),1),"")' -> 'i' | R7: '=IFERROR(MID($B5,COLUMNS($D7:R7),1),"")' -> None | N9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:N)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'o' | O9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:O)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'i' | P9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:P)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'u' | Q9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Q)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> 'i' | R9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:R)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None

### `5d8557dfb652|IFERROR_MASK|July-KPIs!E12`

- workbook: `all_data_912_v0.1/spreadsheet/1726/3_1726_input.xlsx`
- location: `July-KPIs!E12`  severity: Medium  confidence: Review
- formula: `=IFERROR(((C12*1.3)+(D12*1))/((B12)),"0")`
- evidence: Formula uses IFERROR.
- cached value: '0'; row labels: []; column header: ''; used range: A1:T3212
- neighbourhood: E10: '=IFERROR(((C10*1.3)+(D10*1))/((B10)),"0")' -> '0' | E11: '=IFERROR(((C11*1.3)+(D11*1))/((B11)),"0")' -> '0' | F11: 'Total Paid Hours' | E12: '=IFERROR(((C12*1.3)+(D12*1))/((B12)),"0")' -> '0' | F12: '=SUM(B6:B36)' -> 0 | E13: '=IFERROR(((C13*1.3)+(D13*1))/((B13)),"0")' -> '0' | E14: '=IFERROR(((C14*1.3)+(D14*1))/((B14)),"0")' -> '0' | F14: 'KPI Achieved'

### `7149679332c0|IFERROR_MASK|RESULTS1!S35`

- workbook: `all_data_912_v0.1/spreadsheet/50442/2_50442_input.xlsx`
- location: `RESULTS 1!S35`  severity: Medium  confidence: Review
- formula: `=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000")>=10,AVERAGEIFS(Table1[POINTS G/L],Table1[MARKET CAP],">500000000",Table1[MARKET CAP],"<=1000000000",Table1[FLOAT],">5000000",Table1[FLOAT],"<=10000000"),""),0)`
- evidence: Formula uses IFERROR.
- cached value: None; row labels: ["'PM Trades'", "'500M-1B'"]; column header: ''; used range: A1:W67
- neighbourhood: Q33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | R33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | S33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | T33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | U33: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],"<100000000",Table1[FLOAT]... -> None | Q34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | R34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | S34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | T34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | U34: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">100000000",Table1[MARKET... -> None | Q35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | R35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | S35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | T35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | U35: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">500000000",Table1[MARKET... -> None | Q36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | R36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | S36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | T36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None | U36: '=IFERROR(IF(COUNTIFS(Table1[MARKET CAP],">1000000000",Table1[FLOAT... -> None

## LITERAL_CONSTANT

### `52f51f4cf65d|LITERAL_CONSTANT|DataImport!I10`

- workbook: `all_data_912_v0.1/spreadsheet/430-39/2_430-39_input.xlsx`
- location: `Data Import!I10`  severity: Medium  confidence: Review
- formula: `=TRIM(MID(SUBSTITUTE(CHAR(10)&$C10,CHAR(10),REPT(" ",99)),COLUMNS($C10:D10)*99,99))`
- evidence: Non-trivial numeric literal(s) found: 10, 10, 99, 99, 99.
- cached value: None; row labels: []; column header: ''; used range: A1:O13
- range $C10:D10: values ['None', 'None']; beyond: {'left': 'B10: None', 'right': 'E10: None'}
- neighbourhood: G8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | H8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | I8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | J8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | K8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | G9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | H9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | I9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | J9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | K9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | G10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | J10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | G11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | J11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | G12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | J12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None

### `7b15ef0c0d8c|LITERAL_CONSTANT|data!I7`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!I7`  severity: Medium  confidence: Review
- formula: `=HOUR(F7)+MINUTE(F7)/60+SECOND(F7)/3600`
- evidence: Non-trivial numeric literal(s) found: 60, 3600.
- cached value: 8.22; row labels: ["'andrew faulk'", "'warr clutch'"]; column header: ''; used range: A1:O48
- neighbourhood: G5: '=TEXT(F5-E5,"h:mm:ss")' -> '0:31:59' | H5: '=HOUR(E5)+MINUTE(E5)/60+SECOND(E5)/3600' -> 15.1725 | I5: '=HOUR(F5)+MINUTE(F5)/60+SECOND(F5)/3600' -> 15.7055555555556 | K5: '=SUM(I5-H5)' -> 0.533055555555556 | G6: '=TEXT(F6-E6,"h:mm:ss")' -> '1:19:50' | H6: '=HOUR(E6)+MINUTE(E6)/60+SECOND(E6)/3600' -> 15.3377777777778 | I6: '=HOUR(F6)+MINUTE(F6)/60+SECOND(F6)/3600' -> 16.6683333333333 | K6: '=SUM(I6-H6)' -> 1.33055555555555 | G7: '=TEXT(F7-E7,"h:mm:ss")' -> '0:10:33' | H7: '=HOUR(E7)+MINUTE(E7)/60+SECOND(E7)/3600' -> 8.04416666666667 | I7: '=HOUR(F7)+MINUTE(F7)/60+SECOND(F7)/3600' -> 8.22 | K7: '=SUM(I7-H7)' -> 0.175833333333333 | G8: '=TEXT(F8-E8,"h:mm:ss")' -> '1:01:39' | H8: '=HOUR(E8)+MINUTE(E8)/60+SECOND(E8)/3600' -> 8.02694444444445 | I8: '=HOUR(F8)+MINUTE(F8)/60+SECOND(F8)/3600' -> 9.05444444444445 | K8: '=SUM(I8-H8)' -> 1.0275 | G9: '=TEXT(F9-E9,"h:mm:ss")' -> '0:14:20' | H9: '=HOUR(E9)+MINUTE(E9)/60+SECOND(E9)/3600' -> 8.22083333333333 | I9: '=HOUR(F9)+MINUTE(F9)/60+SECOND(F9)/3600' -> 8.45972222222222 | K9: '=SUM(I9-H9)' -> 0.238888888888889

### `f4cc22517a5b|LITERAL_CONSTANT|master!E49`

- workbook: `all_data_912_v0.1/spreadsheet/47933/1_47933_input.xlsx`
- location: `master!E49`  severity: Medium  confidence: Review
- formula: `=IF(B49<37.5,"2",)*IF(B49>37.5,"D2,1.5,")`
- evidence: Non-trivial numeric literal(s) found: 37.5, 37.5.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C47: '=INDEX(amount!A:A,MATCH(A47,amount!B:B,0))' -> 28373.2252748092 | D47: '=ROUND(C47/52/B47,2)' -> 13.64 | E47: '=IF(B47<37.5,"2",)*IF(B47>37.5,"D2,1.5,")' -> '#VALUE!' | C48: '=INDEX(amount!A:A,MATCH(A48,amount!B:B,0))' -> 72028.3618082528 | D48: '=ROUND(C48/52/B48,2)' -> 61.56 | E48: '=IF(B48<37.5,"2",)*IF(B48>37.5,"D2,1.5,")' -> 0 | C49: '=INDEX(amount!A:A,MATCH(A49,amount!B:B,0))' -> 2762.84101382307 | D49: '=ROUND(C49/52/B49,2)' -> 1.06 | E49: '=IF(B49<37.5,"2",)*IF(B49>37.5,"D2,1.5,")' -> '#VALUE!' | C50: '=INDEX(amount!A:A,MATCH(A50,amount!B:B,0))' -> 59137.6222410491 | D50: '=ROUND(C50/52/B50,2)' -> 30.33 | E50: '=IF(B50<37.5,"2",)*IF(B50>37.5,"D2,1.5,")' -> 0 | C51: '=INDEX(amount!A:A,MATCH(A51,amount!B:B,0))' -> 11216.713156954 | D51: '=ROUND(C51/52/B51,2)' -> 4.31 | E51: '=IF(B51<37.5,"2",)*IF(B51>37.5,"D2,1.5,")' -> '#VALUE!'

### `aa0e60ece0f5|LITERAL_CONSTANT|master!E154`

- workbook: `all_data_912_v0.1/spreadsheet/47933/3_47933_input.xlsx`
- location: `master!E154`  severity: Medium  confidence: Review
- formula: `=IF(B154<37.5,"2",)*IF(B154>37.5,"D2,1.5,")`
- evidence: Non-trivial numeric literal(s) found: 37.5, 37.5.
- cached value: 0; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C152: '=INDEX(amount!A:A,MATCH(A152,amount!B:B,0))' -> 54243.8084352273 | D152: '=ROUND(C152/52/B152,2)' -> 23.71 | E152: '=IF(B152<37.5,"2",)*IF(B152>37.5,"D2,1.5,")' -> '#VALUE!' | C153: '=INDEX(amount!A:A,MATCH(A153,amount!B:B,0))' -> 92025.5931243139 | D153: '=ROUND(C153/52/B153,2)' -> 41.64 | E153: '=IF(B153<37.5,"2",)*IF(B153>37.5,"D2,1.5,")' -> '#VALUE!' | C154: '=INDEX(amount!A:A,MATCH(A154,amount!B:B,0))' -> 25127.5769375319 | D154: '=ROUND(C154/52/B154,2)' -> 12.89 | E154: '=IF(B154<37.5,"2",)*IF(B154>37.5,"D2,1.5,")' -> 0

### `e7625a973c75|LITERAL_CONSTANT|Sheet1!C28`

- workbook: `all_data_912_v0.1/spreadsheet/49196/2_49196_input.xlsx`
- location: `Sheet1!C28`  severity: Medium  confidence: Review
- formula: `=LEFT(K28,2)&"/"&MID(K28,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K28,FIND(" ",K28,1),6)`
- evidence: Non-trivial numeric literal(s) found: 6.
- cached value: '18/12/24 18:00'; row labels: []; column header: ''; used range: A1:L47
- neighbourhood: C26: '=LEFT(K26,2)&"/"&MID(K26,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K26,FIND(... -> '16/12/24 04:47' | D26: '=TEXT(C26,"mmm")' -> 'Dec' | E26: '=WEEKNUM(C26,21)' -> '#NUM!' | C27: '=LEFT(K27,2)&"/"&MID(K27,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K27,FIND(... -> '16/12/24 06:00' | D27: '=TEXT(C27,"mmm")' -> 'Dec' | E27: '=WEEKNUM(C27,21)' -> '#NUM!' | C28: '=LEFT(K28,2)&"/"&MID(K28,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K28,FIND(... -> '18/12/24 18:00' | D28: '=TEXT(C28,"mmm")' -> 'Dec' | E28: '=WEEKNUM(C28,21)' -> '#NUM!' | C29: '=LEFT(K29,2)&"/"&MID(K29,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K29,FIND(... -> '19/12/24 18:00' | D29: '=TEXT(C29,"mmm")' -> 'Dec' | E29: '=WEEKNUM(C29,21)' -> '#NUM!' | C30: '=LEFT(K30,2)&"/"&MID(K30,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K30,FIND(... -> '20/12/24 07:07' | D30: '=TEXT(C30,"mmm")' -> 'Dec' | E30: '=WEEKNUM(C30,21)' -> '#NUM!'

### `b08d423ba868|LITERAL_CONSTANT|NOMINA!E46`

- workbook: `all_data_912_v0.1/spreadsheet/31202/3_31202_input.xlsx`
- location: `NOMINA!E46`  severity: Medium  confidence: Review
- formula: `=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[FECHA INGRESO]],3,FALSE)-VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[DEDUCCIONES]],6,FALSE))/7`
- evidence: Non-trivial numeric literal(s) found: 3, 6.
- cached value: 214.285714285714; row labels: ["'GUADALUPE RUIZ'"]; column header: ''; used range: A1:R48
- neighbourhood: C44: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 5 | D44: 'CESAR RUIZ' | E44: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 242.857142857143 | F44: 6 | G44: 0 | C45: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 5 | D45: 'JESUS MAGAÑA' | E45: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 500 | F45: 6 | G45: 500 | C46: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 5 | D46: 'GUADALUPE RUIZ' | E46: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 214.285714285714 | F46: 6 | G46: 0 | C47: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 5 | D47: 'RUBEN LEYSON' | E47: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 357.142857142857 | F47: 6 | G47: 0

### `c5f1312b4027|LITERAL_CONSTANT|Data2!O18`

- workbook: `all_data_912_v0.1/spreadsheet/48357/1_48357_input.xlsx`
- location: `Data 2!O18`  severity: Medium  confidence: Review
- formula: `="Q"&ROUNDUP(MONTH(D18)/3,0)`
- evidence: Non-trivial numeric literal(s) found: 3.
- cached value: 'Q4'; row labels: ["'15/5/2022'"]; column header: ''; used range: A1:P21
- neighbourhood: M16: 2022-02-01 00:00:00 | N16: '=YEAR(D16)' -> 2021 | O16: '="Q"&ROUNDUP(MONTH(D16)/3,0)' -> 'Q4' | P16: '=TEXT(D16,"mmm")' -> 'Dec' | M17: 2022-01-21 00:00:00 | N17: '=YEAR(D17)' -> 2021 | O17: '="Q"&ROUNDUP(MONTH(D17)/3,0)' -> 'Q4' | P17: '=TEXT(D17,"mmm")' -> 'Dec' | M18: '15/5/2022' | N18: '=YEAR(D18)' -> 2021 | O18: '="Q"&ROUNDUP(MONTH(D18)/3,0)' -> 'Q4' | P18: '=TEXT(D18,"mmm")' -> 'Dec' | M19: 2022-01-06 00:00:00 | N19: '=YEAR(D19)' -> 2022 | O19: '="Q"&ROUNDUP(MONTH(D19)/3,0)' -> 'Q1' | P19: '=TEXT(D19,"mmm")' -> 'Jan' | M20: 2022-01-06 00:00:00 | N20: '=YEAR(D20)' -> 2022 | O20: '="Q"&ROUNDUP(MONTH(D20)/3,0)' -> 'Q1' | P20: '=TEXT(D20,"mmm")' -> 'Jan'

### `f1165460e328|LITERAL_CONSTANT|Sheet1!H18`

- workbook: `all_data_912_v0.1/spreadsheet/56599/2_56599_input.xlsx`
- location: `Sheet1!H18`  severity: Medium  confidence: Review
- formula: `=G18+9`
- evidence: Non-trivial numeric literal(s) found: 9.
- cached value: 5871130; row labels: []; column header: ''; used range: A1:M30
- neighbourhood: G16: '=H15+1' -> 5871101 | H16: '=G16+9' -> 5871110 | I16: 10 | J16: '=J15+1' -> 477111 | G17: '=H16+1' -> 5871111 | H17: '=G17+9' -> 5871120 | I17: 10 | J17: '=J16+1' -> 477112 | G18: '=H17+1' -> 5871121 | H18: '=G18+9' -> 5871130 | I18: 10 | J18: '=J17+1' -> 477113 | G19: '=H18+1' -> 5871131 | H19: '=G19+9' -> 5871140 | I19: 10 | J19: '=J18+1' -> 477114 | G20: '=H19+1' -> 5871141 | H20: '=G20+9' -> 5871150 | I20: 10 | J20: '=J19+1' -> 477115

### `e91e37899ef5|LITERAL_CONSTANT|DATA!D106`

- workbook: `all_data_912_v0.1/spreadsheet/58656/2_58656_input.xlsx`
- location: `DATA!D106`  severity: Medium  confidence: Review
- formula: `=IF(F106>TIME(23,59,59),DATE(A106,B106,C106)+1,DATE(A106,B106,C106))`
- evidence: Non-trivial numeric literal(s) found: 23, 59, 59.
- cached value: 2023-01-28 00:00:00; row labels: ["'1'"]; column header: ''; used range: A1:K132
- neighbourhood: B104: '1' | C104: 15 | D104: '=IF(F104>TIME(23,59,59),DATE(A104,B104,C104)+1,DATE(A104,B104,C104))' -> 2023-01-15 00:00:00 | E104: 02:10:00 | F104: '=SUM(E104+2/24)' -> 04:10:00 | B105: '1' | C105: 21 | D105: '=IF(F105>TIME(23,59,59),DATE(A105,B105,C105)+1,DATE(A105,B105,C105))' -> 2023-01-21 00:00:00 | E105: 20:53:00 | F105: '=SUM(E105+2/24)' -> 22:53:00 | B106: '1' | C106: 28 | D106: '=IF(F106>TIME(23,59,59),DATE(A106,B106,C106)+1,DATE(A106,B106,C106))' -> 2023-01-28 00:00:00 | E106: 15:19:00 | F106: '=SUM(E106+2/24)' -> 17:19:00 | B107: '2' | C107: 5 | D107: '=IF(F107>TIME(23,59,59),DATE(A107,B107,C107)+1,DATE(A107,B107,C107))' -> 2023-02-05 00:00:00 | E107: 18:29:00 | F107: '=SUM(E107+2/24)' -> 20:29:00 | B108: '2' | C108: 13 | D108: '=IF(F108>TIME(23,59,59),DATE(A108,B108,C108)+1,DATE(A108,B108,C108))' -> 2023-02-13 00:00:00 | E108: 16:01:00 | F108: '=SUM(E108+2/24)' -> 18:01:00

### `c3a1f68a40ba|LITERAL_CONSTANT|DataImport!G10`

- workbook: `all_data_912_v0.1/spreadsheet/430-39/1_430-39_input.xlsx`
- location: `Data Import!G10`  severity: Medium  confidence: Review
- formula: `=TRIM(MID(SUBSTITUTE(CHAR(10)&$B10,CHAR(10),REPT(" ",99)),COLUMNS($B10:C10)*99,99))`
- evidence: Non-trivial numeric literal(s) found: 10, 10, 99, 99, 99.
- cached value: None; row labels: []; column header: ''; used range: A1:O13
- range $B10:C10: values ['None', 'None']; beyond: {'left': 'A10: None', 'right': 'D10: None'}
- neighbourhood: F8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B8,CHAR(10),REPT(" ",99)),COLUMNS(B... -> None | G8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | H8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | I8: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C8,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | F9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B9,CHAR(10),REPT(" ",99)),COLUMNS(B... -> None | G9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | H9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | I9: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C9,CHAR(10),REPT(" ",99)),COLUMNS($... -> None | F10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | G10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | F11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | G11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | F12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | G12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | H12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | I12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$C12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None

### `67efc211ab2e|LITERAL_CONSTANT|PalletLog!L10`

- workbook: `all_data_912_v0.1/spreadsheet/34493/1_34493_input.xlsx`
- location: `Pallet Log!L10`  severity: Medium  confidence: Review
- formula: `=COUNTIF($I10:$J10,">0")+IF($K10>225,1,0)+IF($K10>382,1,0)+IF($K10>611,1,0)+IF($K10>845,1,0)+1`
- evidence: Non-trivial numeric literal(s) found: 225, 382, 611, 845.
- cached value: 2; row labels: ["'#'", "'P'"]; column header: "'White Sheets'"; used range: A1:EWJ1135
- range $I10:$J10: values ['1', '0']; beyond: {'left': 'H10: None', 'right': "K10: '=SUM(J10*2)'"}
- neighbourhood: J10: 0 | K10: '=SUM(J10*2)' -> 0 | L10: '=COUNTIF($I10:$J10,">0")+IF($K10>225,1,0)+IF($K10>382,1,0)+IF($K10... -> 2 | M10: '=SUM(L10-1)' -> 1 | N10: '=SUM(I10+M10)' -> 2 | J11: 0 | K11: '=SUM(J11*2)' -> 0 | L11: '=COUNTIF($I11:$J11,">0")+IF($K11>225,1,0)+IF($K11>382,1,0)+IF($K11... -> 2 | M11: '=SUM(L11-1)' -> 1 | N11: '=SUM(I11+M11)' -> 4 | J12: 0 | K12: '=SUM(J12*2)' -> 0 | L12: '=COUNTIF($I12:$J12,">0")+IF($K12>225,1,0)+IF($K12>382,1,0)+IF($K12... -> 2 | M12: '=SUM(L12-1)' -> 1 | N12: '=SUM(I12+M12)' -> 7

### `7b15ef0c0d8c|LITERAL_CONSTANT|data!I17`

- workbook: `all_data_912_v0.1/spreadsheet/56225/3_56225_input.xlsx`
- location: `data!I17`  severity: Medium  confidence: Review
- formula: `=HOUR(F17)+MINUTE(F17)/60+SECOND(F17)/3600`
- evidence: Non-trivial numeric literal(s) found: 60, 3600.
- cached value: 11.1008333333333; row labels: ["'gage yount'", "'full service'"]; column header: ''; used range: A1:O48
- neighbourhood: G15: '=TEXT(F15-E15,"h:mm:ss")' -> '0:00:00' | H15: '=HOUR(E15)+MINUTE(E15)/60+SECOND(E15)/3600' -> 14.7269444444444 | I15: '=HOUR(F15)+MINUTE(F15)/60+SECOND(F15)/3600' -> 14.7269444444444 | K15: '=SUM(I15-H15)' -> 0 | G16: '=TEXT(F16-E16,"h:mm:ss")' -> '0:35:11' | H16: '=HOUR(E16)+MINUTE(E16)/60+SECOND(E16)/3600' -> 15.2969444444444 | I16: '=HOUR(F16)+MINUTE(F16)/60+SECOND(F16)/3600' -> 15.8833333333333 | K16: '=SUM(I16-H16)' -> 0.586388888888889 | G17: '=TEXT(F17-E17,"h:mm:ss")' -> '0:03:03' | H17: '=HOUR(E17)+MINUTE(E17)/60+SECOND(E17)/3600' -> 11.05 | I17: '=HOUR(F17)+MINUTE(F17)/60+SECOND(F17)/3600' -> 11.1008333333333 | K17: '=SUM(I17-H17)' -> 0.0508333333333315 | G18: '=TEXT(F18-E18,"h:mm:ss")' -> '0:27:10' | H18: '=HOUR(E18)+MINUTE(E18)/60+SECOND(E18)/3600' -> 11.3344444444444 | I18: '=HOUR(F18)+MINUTE(F18)/60+SECOND(F18)/3600' -> 11.7872222222222 | K18: '=SUM(I18-H18)' -> 0.452777777777778 | G19: '=TEXT(F19-E19,"h:mm:ss")' -> '0:31:37' | H19: '=HOUR(E19)+MINUTE(E19)/60+SECOND(E19)/3600' -> 3.65416666666667 | I19: '=HOUR(F19)+MINUTE(F19)/60+SECOND(F19)/3600' -> 4.18111111111111 | K19: '=SUM(I19-H19)' -> 0.526944444444444

### `57d001666bfd|LITERAL_CONSTANT|Sheet1!F14`

- workbook: `all_data_912_v0.1/spreadsheet/52964/1_52964_input.xlsx`
- location: `Sheet1!F14`  severity: Medium  confidence: Review
- formula: `=IF(E14>14,E14,"N/A")`
- evidence: Non-trivial numeric literal(s) found: 14.
- cached value: 'N/A'; row labels: []; column header: ''; used range: A1:BE279
- neighbourhood: D12: '=IF(COUNTIF(AF12,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E12: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A12,$AA$2:$AA124,0)),0)' -> 0 | F12: '=IF(E12>14,E12,"N/A")' -> 'N/A' | D13: '=IF(COUNTIF(AF13,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E13: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A13,$AA$2:$AA124,0)),0)' -> 0 | F13: '=IF(E13>14,E13,"N/A")' -> 'N/A' | D14: '=IF(COUNTIF(AF14,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E14: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A14,$AA$2:$AA124,0)),0)' -> 3 | F14: '=IF(E14>14,E14,"N/A")' -> 'N/A' | D15: '=IF(COUNTIF(AF15,"*delirium*"),"Postoperative Delirium","No")' -> 'No' | E15: '=IFERROR(INDEX($AG$2:$AG$124,MATCH($A15,$AA$2:$AA124,0)),0)' -> 22 | F15: '=IF(E15>14,E15,"N/A")' -> 22

### `36080f34a91e|LITERAL_CONSTANT|Calendar!B135`

- workbook: `all_data_912_v0.1/spreadsheet/57716/2_57716_input.xlsx`
- location: `Calendar!B135`  severity: Medium  confidence: Review
- formula: `=Days+22+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE(Calendar10Year,Calendar10MonthOption,1),WeekdayOption)`
- evidence: Non-trivial numeric literal(s) found: 22.
- cached value: 2021-01-18 00:00:00; row labels: []; column header: ''; used range: A1:J168
- neighbourhood: B133: '=Days+15+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE... -> 2021-01-11 00:00:00 | C133: 2021-01-12 00:00:00 | D133: 2021-01-13 00:00:00 | B135: '=Days+22+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE... -> 2021-01-18 00:00:00 | C135: 2021-01-19 00:00:00 | D135: 2021-01-20 00:00:00 | B137: '=Days+29+DATE(Calendar10Year,Calendar10MonthOption,1)-WEEKDAY(DATE... -> 2021-01-25 00:00:00 | C137: 2021-01-26 00:00:00 | D137: 2021-01-27 00:00:00

### `24f6192d8cf3|LITERAL_CONSTANT|data!I4`

- workbook: `all_data_912_v0.1/spreadsheet/56225/2_56225_input.xlsx`
- location: `data!I4`  severity: Medium  confidence: Review
- formula: `=HOUR(F4)+MINUTE(F4)/60+SECOND(F4)/3600`
- evidence: Non-trivial numeric literal(s) found: 60, 3600.
- cached value: 15; row labels: ["'gage yount'", "'prem service'"]; column header: ''; used range: A1:O48
- neighbourhood: G2: '=TEXT(F2-E2,"h:mm:ss")' -> '0:37:06' | H2: '=HOUR(E2)+MINUTE(E2)/60+SECOND(E2)/3600' -> 13.2852777777778 | I2: '=HOUR(F2)+MINUTE(F2)/60+SECOND(F2)/3600' -> 13.9036111111111 | K2: '=SUM(I2-H2)' -> 0.618333333333334 | G3: '=TEXT(F3-E3,"h:mm:ss")' -> '0:55:50' | H3: '=HOUR(E3)+MINUTE(E3)/60+SECOND(E3)/3600' -> 15.8808333333333 | I3: '=HOUR(F3)+MINUTE(F3)/60+SECOND(F3)/3600' -> 16.8113888888889 | K3: '=SUM(I3-H3)' -> 0.930555555555555 | G4: '=TEXT(F4-E4,"h:mm:ss")' -> '0:39:02' | H4: '=HOUR(E4)+MINUTE(E4)/60+SECOND(E4)/3600' -> 14.3494444444444 | I4: '=HOUR(F4)+MINUTE(F4)/60+SECOND(F4)/3600' -> 15 | K4: '=SUM(I4-H4)' -> 0.650555555555554 | G5: '=TEXT(F5-E5,"h:mm:ss")' -> '0:31:59' | H5: '=HOUR(E5)+MINUTE(E5)/60+SECOND(E5)/3600' -> 15.1725 | I5: '=HOUR(F5)+MINUTE(F5)/60+SECOND(F5)/3600' -> 15.7055555555556 | K5: '=SUM(I5-H5)' -> 0.533055555555556 | G6: '=TEXT(F6-E6,"h:mm:ss")' -> '1:19:50' | H6: '=HOUR(E6)+MINUTE(E6)/60+SECOND(E6)/3600' -> 15.3377777777778 | I6: '=HOUR(F6)+MINUTE(F6)/60+SECOND(F6)/3600' -> 16.6683333333333 | K6: '=SUM(I6-H6)' -> 1.33055555555555

### `86bd0c65882c|LITERAL_CONSTANT|Sheet1!L15`

- workbook: `all_data_912_v0.1/spreadsheet/52964/2_52964_input.xlsx`
- location: `Sheet1!L15`  severity: Medium  confidence: Review
- formula: `=IF(K15<85,"75-84",">85")`
- evidence: Non-trivial numeric literal(s) found: 85.
- cached value: '75-84'; row labels: []; column header: ''; used range: A1:BE279
- neighbourhood: J13: '=IFERROR(INDEX($R$2:$R$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 1944-06-26 00:00:00 | K13: '=IFERROR(INDEX($S$2:$S$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 76 | L13: '=IF(K13<85,"75-84",">85")' -> '75-84' | M13: '=IFERROR(INDEX($T$2:$T$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 'Male' | N13: '=IFERROR(INDEX($U$2:$U$124,MATCH($A13,$Q$2:$Q124,0)),0)' -> 2021-04-13 00:00:00 | J14: '=IFERROR(INDEX($R$2:$R$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 1938-04-07 00:00:00 | K14: '=IFERROR(INDEX($S$2:$S$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 83 | L14: '=IF(K14<85,"75-84",">85")' -> '75-84' | M14: '=IFERROR(INDEX($T$2:$T$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 'Male' | N14: '=IFERROR(INDEX($U$2:$U$124,MATCH($A14,$Q$2:$Q124,0)),0)' -> 2021-05-19 00:00:00 | J15: '=IFERROR(INDEX($R$2:$R$124,MATCH($A15,$Q$2:$Q124,0)),0)' -> 1943-02-16 00:00:00 | K15: '=IFERROR(INDEX($S$2:$S$124,MATCH($A15,$Q$2:$Q124,0)),0)' -> 78 | L15: '=IF(K15<85,"75-84",">85")' -> '75-84' | M15: '=IFERROR(INDEX($T$2:$T$124,MATCH($A15,$Q$2:$Q124,0)),0)' -> 'Male' | N15: '=IFERROR(INDEX($U$2:$U$124,MATCH($A15,$Q$2:$Q124,0)),0)' -> 2021-04-15 00:00:00

### `26c0d83f1ceb|LITERAL_CONSTANT|Sheet1!H6`

- workbook: `all_data_912_v0.1/spreadsheet/56599/1_56599_input.xlsx`
- location: `Sheet1!H6`  severity: Medium  confidence: Review
- formula: `=G6+9`
- evidence: Non-trivial numeric literal(s) found: 9.
- cached value: 5871010; row labels: []; column header: "'slip to'"; used range: A1:J30
- neighbourhood: G5: 'Slip fm' | H5: 'slip to' | I5: 'total slips in book' | J5: 'BookNo' | G6: 5871001 | H6: '=G6+9' -> 5871010 | I6: 10 | J6: 477101 | G7: '=H6+1' -> 5871011 | H7: '=G7+9' -> 5871020 | I7: 10 | J7: '=J6+1' -> 477102 | G8: '=H7+1' -> 5871021 | H8: '=G8+9' -> 5871030 | I8: 10 | J8: '=J7+1' -> 477103

### `a6eb33632e4e|LITERAL_CONSTANT|WEEKDAY!C4`

- workbook: `all_data_912_v0.1/spreadsheet/55977/3_55977_input.xlsx`
- location: `WEEKDAY!C4`  severity: Medium  confidence: Review
- formula: `=WEEKDAY(B4,11)`
- evidence: Non-trivial numeric literal(s) found: 11.
- cached value: 1900-01-07 00:00:00; row labels: []; column header: ''; used range: A1:C16
- neighbourhood: A2: 1972-03-15 00:00:00 | B2: '=WEEKDAY(A2,2)' -> 3 | C2: '=WEEKDAY(B2,11)' -> 1900-01-02 00:00:00 | A3: 1983-06-22 00:00:00 | B3: '=WEEKDAY(A3,2)' -> 3 | C3: '=WEEKDAY(B3,11)' -> 1900-01-02 00:00:00 | A4: 1974-11-25 00:00:00 | B4: '=WEEKDAY(A4,2)' -> 1 | C4: '=WEEKDAY(B4,11)' -> 1900-01-07 00:00:00 | A5: 1976-01-12 00:00:00 | B5: '=WEEKDAY(A5,2)' -> 1 | C5: '=WEEKDAY(B5,11)' -> 1900-01-07 00:00:00 | A6: 1977-07-22 00:00:00 | B6: '=WEEKDAY(A6,2)' -> 5 | C6: '=WEEKDAY(B6,11)' -> 1900-01-04 00:00:00

### `29a79f5a27e4|LITERAL_CONSTANT|Sheet1!C10`

- workbook: `all_data_912_v0.1/spreadsheet/49196/1_49196_input.xlsx`
- location: `Sheet1!C10`  severity: Medium  confidence: Review
- formula: `=LEFT(K10,2)&"/"&MID(K10,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K10,FIND(" ",K10,1),6)`
- evidence: Non-trivial numeric literal(s) found: 6.
- cached value: '30/11/24 05:04'; row labels: []; column header: ''; used range: A1:L47
- neighbourhood: C8: '=LEFT(K8,2)&"/"&MID(K8,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K8,FIND(" "... -> '26/11/24 10:13' | D8: '=TEXT(C8,"mmm")' -> 'Nov' | E8: '=WEEKNUM(C8,21)' -> 48 | C9: '=LEFT(K9,2)&"/"&MID(K9,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K9,FIND(" "... -> '29/11/24 19:18' | D9: '=TEXT(C9,"mmm")' -> 'Nov' | E9: '=WEEKNUM(C9,21)' -> 47 | C10: '=LEFT(K10,2)&"/"&MID(K10,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K10,FIND(... -> '30/11/24 05:04' | D10: '=TEXT(C10,"mmm")' -> 'Nov' | E10: '=WEEKNUM(C10,21)' -> 48 | C11: '=LEFT(K11,2)&"/"&MID(K11,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K11,FIND(... -> '30/11/24 06:00' | D11: '=TEXT(C11,"mmm")' -> 'Nov' | E11: '=WEEKNUM(C11,21)' -> 48 | C12: '=LEFT(K12,2)&"/"&MID(K12,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K12,FIND(... -> '01/12/24 00:02' | D12: '=TEXT(C12,"mmm")' -> 'Dec' | E12: '=WEEKNUM(C12,21)' -> 52

### `5ec32da9071e|LITERAL_CONSTANT|Total(2)!E65`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!E65`  severity: Medium  confidence: Review
- formula: `=IFERROR(VLOOKUP($H65,$J$27:$L$35,3,0)*$C65,0)`
- evidence: Non-trivial numeric literal(s) found: 3.
- cached value: 6720; row labels: []; column header: ''; used range: A1:Z1026
- range $J$27:$L$35: values ["'PE'", 'None', '0.8', "'GS'", 'None', '0.65', "'CC'", 'None', '0.6', 'None', 'None', 'None']; beyond: {}
- neighbourhood: C63: '=(B63*1)' -> 800 | D63: '=SUM(C63-E63)' -> 160 | E63: '=IFERROR(VLOOKUP($H63,$J$27:$L$35,3,0)*$C63,0)' -> 640 | F63: 44515 | G63: 'Y' | C64: '=(B64*1)' -> 2400 | D64: '=SUM(C64-E64)' -> 480 | E64: '=IFERROR(VLOOKUP($H64,$J$27:$L$35,3,0)*$C64,0)' -> 1920 | F64: 44515 | G64: 'Y' | C65: '=(B65*2)' -> 8400 | D65: '=SUM(C65-E65)' -> 1680 | E65: '=IFERROR(VLOOKUP($H65,$J$27:$L$35,3,0)*$C65,0)' -> 6720 | F65: 44581 | G65: 'C' | C66: '=(B66*1)' -> 0 | D66: '=SUM(C66-E66)' -> 0 | E66: '=IFERROR(VLOOKUP($H66,$J$27:$L$35,3,0)*$C66,0)' -> 0 | C67: '=(B67*1)' -> 0 | D67: '=SUM(C67-E67)' -> 0 | E67: '=IFERROR(VLOOKUP($H67,$J$27:$L$35,3,0)*$C67,0)' -> 0

### `c3a1f68a40ba|LITERAL_CONSTANT|DataImport!M12`

- workbook: `all_data_912_v0.1/spreadsheet/430-39/1_430-39_input.xlsx`
- location: `Data Import!M12`  severity: Medium  confidence: Review
- formula: `=TRIM(MID(SUBSTITUTE(CHAR(10)&$E12,CHAR(10),REPT(" ",99)),COLUMNS($E12:E12)*99,99))`
- evidence: Non-trivial numeric literal(s) found: 10, 10, 99, 99, 99.
- cached value: None; row labels: []; column header: ''; used range: A1:O13
- range $E12:E12: values ['None']; beyond: {'above': 'E11: None', 'below': 'E13: None', 'left': 'D12: None', 'right': "F12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$B12,C..."}
- neighbourhood: K10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | L10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | M10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | N10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | O10: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E10,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | L11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | M11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | N11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | O11: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E11,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | L12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | M12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | N12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | O12: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E12,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | K13: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D13,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | L13: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$D13,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | M13: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E13,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | N13: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E13,CHAR(10),REPT(" ",99)),COLUMNS(... -> None | O13: '=TRIM(MID(SUBSTITUTE(CHAR(10)&$E13,CHAR(10),REPT(" ",99)),COLUMNS(... -> None

### `8e5a61e5d9f3|LITERAL_CONSTANT|NOMINA!E24`

- workbook: `all_data_912_v0.1/spreadsheet/31202/1_31202_input.xlsx`
- location: `NOMINA!E24`  severity: Medium  confidence: Review
- formula: `=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[FECHA INGRESO]],3,FALSE)-VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[DEDUCCIONES]],6,FALSE))/7`
- evidence: Non-trivial numeric literal(s) found: 3, 6.
- cached value: 242.857142857143; row labels: ["'JOSE VALDEZ'"]; column header: ''; used range: A1:R48
- neighbourhood: C22: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 3 | D22: 'GREGORIO COTA ESCOBAR' | E22: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 314.285714285714 | F22: 6 | G22: 0 | C23: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 3 | D23: 'MARTIN PARRA' | E23: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 257.142857142857 | F23: 6 | G23: 0 | C24: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 3 | D24: 'JOSE VALDEZ' | E24: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 242.857142857143 | F24: 6 | G24: 0 | C25: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 3 | D25: 'CESAR RUIZ' | E25: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 242.857142857143 | F25: 6 | G25: 0 | C26: '=WEEKNUM(tblNomina[[#This Row],[DATE]])' -> 3 | D26: 'JESUS MAGAÑA' | E26: '=(VLOOKUP(tblNomina[[#This Row],[WORKER]],tblEmpleados[[NOMBRE]:[F... -> 500 | F26: 6 | G26: 0

### `b7a7aedc0e75|LITERAL_CONSTANT|Sheet1!J6`

- workbook: `all_data_912_v0.1/spreadsheet/52541/3_52541_input.xlsx`
- location: `Sheet1!J6`  severity: Medium  confidence: Review
- formula: `=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row],[Over Due Days]]<90,"Call Customer","Bad Debts"))`
- evidence: Non-trivial numeric literal(s) found: 90.
- cached value: 'Bad Debts'; row labels: ["'ARON'"]; column header: "'Remarks'"; used range: A1:J13
- neighbourhood: H5: 'Amount Outstanding' | I5: 'Over Due Days' | J5: 'Remarks' | H6: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 25000 | I6: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1171 | J6: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | H7: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> 22000 | I7: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> 1143 | J7: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Bad Debts' | H8: '=Table2[[#This Row],[Invoice Amount]]-Table2[[#This Row],[Amount R... -> -3000 | I8: '=IF(Table2[[#This Row],[Amount Outstanding]]=0,"",TODAY()-Table2[[... -> -248 | J8: '=IF(Table2[[#This Row],[Over Due Days]]="","",IF(Table2[[#This Row... -> 'Call Customer'

### `29a79f5a27e4|LITERAL_CONSTANT|Sheet1!E38`

- workbook: `all_data_912_v0.1/spreadsheet/49196/1_49196_input.xlsx`
- location: `Sheet1!E38`  severity: Medium  confidence: Review
- formula: `=WEEKNUM(C38,21)`
- evidence: Non-trivial numeric literal(s) found: 21.
- cached value: 4; row labels: []; column header: ''; used range: A1:L47
- neighbourhood: C36: '=LEFT(K36,2)&"/"&MID(K36,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K36,FIND(... -> '01/01/24 21:52' | D36: '=TEXT(C36,"mmm")' -> 'Jan' | E36: '=WEEKNUM(C36,21)' -> 4 | C37: '=LEFT(K37,2)&"/"&MID(K37,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K37,FIND(... -> '03/01/24 10:42' | D37: '=TEXT(C37,"mmm")' -> 'Jan' | E37: '=WEEKNUM(C37,21)' -> 4 | C38: '=LEFT(K38,2)&"/"&MID(K38,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K38,FIND(... -> '11/01/24 17:25' | D38: '=TEXT(C38,"mmm")' -> 'Jan' | E38: '=WEEKNUM(C38,21)' -> 4 | C39: '=LEFT(K39,2)&"/"&MID(K39,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K39,FIND(... -> '13/01/24 01:33' | D39: '=TEXT(C39,"mmm")' -> 'Jan' | E39: '=WEEKNUM(C39,21)' -> 4 | C40: '=LEFT(K40,2)&"/"&MID(K40,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K40,FIND(... -> '13/01/24 17:11' | D40: '=TEXT(C40,"mmm")' -> 'Jan' | E40: '=WEEKNUM(C40,21)' -> 4

### `c212843d66a8|LITERAL_CONSTANT|LeadTimes!F10`

- workbook: `all_data_912_v0.1/spreadsheet/47741/2_47741_input.xlsx`
- location: `Lead Times!F10`  severity: Medium  confidence: Review
- formula: `=WORKDAY(F8,18,O19:O25)`
- evidence: Non-trivial numeric literal(s) found: 18.
- cached value: 2022-02-02 00:00:00; row labels: []; column header: ''; used range: A1:O31
- range O19:O25: values ['2022-11-25 00:00:00', '2022-12-26 00:00:00', 'None', 'None', 'None', 'None', 'None']; beyond: {'above': 'O18: 2022-11-24 00:00:00', 'below': 'O26: None'}
- neighbourhood: D8: 2022-01-05 00:00:00 | E8: 2022-01-06 00:00:00 | F8: 2022-01-07 00:00:00 | G8: 2022-01-08 00:00:00 | H8: 2022-01-09 00:00:00 | D9: '=WORKDAY(D8,10,M18:M24)' -> 2022-01-19 00:00:00 | E9: '=WORKDAY(E8,10,N18:N24)' -> 2022-01-20 00:00:00 | F9: '=WORKDAY(F8,10,O18:O24)' -> 2022-01-21 00:00:00 | D10: '=WORKDAY(D8,18,M19:M25)' -> 2022-01-31 00:00:00 | E10: '=WORKDAY(E8,18,N19:N25)' -> 2022-02-01 00:00:00 | F10: '=WORKDAY(F8,18,O19:O25)' -> 2022-02-02 00:00:00 | D11: '1/10/22-1/12/22' | E11: '1/11/22-1/13/22' | F11: '1/12/22-1/14/22' | D12: 2022-01-12 00:00:00 | E12: 2022-01-13 00:00:00 | F12: 2022-01-14 00:00:00 | G12: 2022-01-15 00:00:00 | H12: 2022-01-16 00:00:00

## LIVE_ERROR

### `192a19040f63|LIVE_ERROR|Sheettwo!E218`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E218`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0070220212'"]; column header: ''; used range: A1:G6234
- neighbourhood: C216: '1D' | D216: '0070200840' | E216: '=VLOOKUP(G216,Suppliers2[],2,FALSE)' -> '#N/A' | F216: '015755' | G216: '88713000' | C217: '1D' | D217: '0070205212' | E217: '=VLOOKUP(G217,Suppliers2[],2,FALSE)' -> '#N/A' | F217: '015977' | G217: '32577900' | C218: '1D' | D218: '0070220212' | E218: '=VLOOKUP(G218,Suppliers2[],2,FALSE)' -> '#N/A' | F218: '015995' | G218: '48160000' | C219: '2D' | D219: '0070222425' | E219: '=VLOOKUP(G219,Suppliers2[],2,FALSE)' -> '#N/A' | F219: '016076' | G219: '48160000' | C220: '2D' | D220: '0070237733' | E220: '=VLOOKUP(G220,Suppliers2[],2,FALSE)' -> '#N/A' | F220: '016111' | G220: '48160000'

### `40c60acd7755|LIVE_ERROR|Sort!K70`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!K70`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2011_Q3'"]; column header: ''; used range: A1:T147
- neighbourhood: I68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 16639 | J68: "=VLOOKUP($B68,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 17.91 | K68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L68: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A68,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M68: '=D68*P68' -> '#VALUE!' | I69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 19552 | J69: "=VLOOKUP($B69,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 20.979999999999997 | K69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L69: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A69,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M69: '=D69*P69' -> '#VALUE!' | I70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 23607 | J70: "=VLOOKUP($B70,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 25.26 | K70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L70: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A70,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M70: '=D70*P70' -> '#VALUE!' | I71: "=VLOOKUP($B71,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 25922 | J71: "=VLOOKUP($B71,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 27.67 | K71: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A71,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L71: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A71,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M71: '=D71*P71' -> '#VALUE!' | I72: "=VLOOKUP($B72,'[1]<2030Cal'!$A:$BE,39,FALSE)" -> 32982 | J72: "=VLOOKUP($B72,'[1]<2030Cal'!$A:$BE,37,FALSE)" -> 35.11 | K72: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A72,'[1]<2030Cal'!$S$12:$S$... -> '#VALUE!' | L72: "=SUMIF('[1]<2030Cal'!$A$12:$A$112,Sort!A72,'[1]<2030Cal'!$T$12:$T$... -> '#VALUE!' | M72: '=D72*P72' -> '#VALUE!'

### `7cc6b0fe1206|LIVE_ERROR|Sort!K18`

- workbook: `all_data_912_v0.1/spreadsheet/59932/1_59932_input.xlsx`
- location: `Sort!K18`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'1998_Q3'"]; column header: ''; used range: A1:T147
- neighbourhood: I16: "=VLOOKUP($B16,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> -878 | J16: "=VLOOKUP($B16,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> -7.01 | K16: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A16,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L16: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A16,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M16: '=D16*P16' -> '#VALUE!' | I17: "=VLOOKUP($B17,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> -115 | J17: "=VLOOKUP($B17,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> -0.99 | K17: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A17,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L17: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A17,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M17: '=D17*P17' -> '#VALUE!' | I18: "=VLOOKUP($B18,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 42 | J18: "=VLOOKUP($B18,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 0.10000000000000009 | K18: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A18,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L18: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A18,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M18: '=D18*P18' -> '#VALUE!' | I19: "=VLOOKUP($B19,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 309 | J19: "=VLOOKUP($B19,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 2.04 | K19: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A19,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L19: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A19,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M19: '=D19*P19' -> '#VALUE!' | I20: "=VLOOKUP($B20,'[1]<2010Cal'!$A:$BE,39,FALSE)" -> 414 | J20: "=VLOOKUP($B20,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 2.1799999999999997 | K20: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A20,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L20: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A20,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M20: '=D20*P20' -> '#VALUE!'

### `30c6f4937476|LIVE_ERROR|HR!BT14`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !BT14`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 2 dependent cell(s): HR !BT24, HR !CW14. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'N/A'", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: BS12: 2019-12-01 00:00:00 | BT12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BU12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BV12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BS14: 2019-12-01 00:00:00 | BT14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BU14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BV14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BS16: 2019-12-01 00:00:00 | BT16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | BU16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | BV16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!'

### `30c6f4937476|LIVE_ERROR|HR!AB14`

- workbook: `all_data_912_v0.1/spreadsheet/54590/1_54590_input.xlsx`
- location: `HR !AB14`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 1 dependent cell(s): HR !AB24. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'Month 1'", "'June + July '"]; column header: ''; used range: A1:GT37
- neighbourhood: AA12: 2019-08-01 00:00:00 | AB12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AC12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | AD12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | Z14: 'June + July ' | AA14: 2019-08-01 00:00:00 | AB14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AC14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AD14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | AA16: 2019-08-01 00:00:00 | AB16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | AC16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | AD16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!'

### `e3e5ae270e30|LIVE_ERROR|Sheet1!AO8`

- workbook: `all_data_912_v0.1/spreadsheet/52450/2_52450_input.xlsx`
- location: `Sheet1!AO8`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 1 dependent cell(s): Sheet1!AO4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Trainer'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: AM6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AP6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AP$1,\'[1]X... -> '#VALUE!' | AQ6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AM7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AP7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AP$1,\'[1]X... -> '#VALUE!' | AQ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AM8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AP8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AP$1,\'[1]X... -> '#VALUE!' | AQ8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AM9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]X... -> '#VALUE!' | AN9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]X... -> '#VALUE!' | AO9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]X... -> '#VALUE!' | AP9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AP$1,\'[1]X... -> '#VALUE!' | AQ9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AM10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AM$1,\'[1]... -> None | AN10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AN$1,\'[1]... -> None | AO10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AO$1,\'[1]... -> None | AP10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AP$1,\'[1]... -> None | AQ10: '=IF($E10<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]... -> None

### `e3e5ae270e30|LIVE_ERROR|Sheet1!AA7`

- workbook: `all_data_912_v0.1/spreadsheet/52450/2_52450_input.xlsx`
- location: `Sheet1!AA7`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 8 dependent cell(s): Sheet1!AA4, Sheet1!P4, Sheet1!P7, Sheet1!S4, Sheet1!S7, Sheet1!T4, Sheet1!T7, Sheet1!V4. Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Tornado'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: Y5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Y$1,\'[1]XA... -> '#VALUE!' | Z5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Z$1,\'[1]XA... -> '#VALUE!' | AA5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AA$1,\'[1]X... -> '#VALUE!' | AB5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AB$1,\'[1]X... -> '#VALUE!' | AC5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AC$1,\'[1]X... -> '#VALUE!' | Y6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Y$1,\'[1]XA... -> '#VALUE!' | Z6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Z$1,\'[1]XA... -> '#VALUE!' | AA6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AA$1,\'[1]X... -> '#VALUE!' | AB6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AB$1,\'[1]X... -> '#VALUE!' | AC6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AC$1,\'[1]X... -> '#VALUE!' | Y7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Y$1,\'[1]XA... -> '#VALUE!' | Z7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Z$1,\'[1]XA... -> '#VALUE!' | AA7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AA$1,\'[1]X... -> '#VALUE!' | AB7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AB$1,\'[1]X... -> '#VALUE!' | AC7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AC$1,\'[1]X... -> '#VALUE!' | Y8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Y$1,\'[1]XA... -> '#VALUE!' | Z8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Z$1,\'[1]XA... -> '#VALUE!' | AA8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AA$1,\'[1]X... -> '#VALUE!' | AB8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AB$1,\'[1]X... -> '#VALUE!' | AC8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AC$1,\'[1]X... -> '#VALUE!' | Y9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Y$1,\'[1]XA... -> '#VALUE!' | Z9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&Z$1,\'[1]XA... -> '#VALUE!' | AA9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AA$1,\'[1]X... -> '#VALUE!' | AB9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AB$1,\'[1]X... -> '#VALUE!' | AC9: '=IF($E9<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AC$1,\'[1]X... -> '#VALUE!'

### `63a66071d918|LIVE_ERROR|Sheettwo!E276`

- workbook: `all_data_912_v0.1/spreadsheet/54196/2_54196_input.xlsx`
- location: `Sheet two!E276`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0096169500'"]; column header: ''; used range: A1:G6234
- neighbourhood: C274: '1D' | D274: '0000009148' | E274: '=VLOOKUP(G274,Suppliers2[],2,FALSE)' -> '#N/A' | F274: '019099' | G274: '46771045' | C275: '4D' | D275: '0000009291' | E275: '=VLOOKUP(G275,Suppliers2[],2,FALSE)' -> '#N/A' | F275: '019112' | G275: '88713000' | C276: '1D' | D276: '0096169500' | E276: '=VLOOKUP(G276,Suppliers2[],2,FALSE)' -> '#N/A' | F276: '019121' | G276: '46771045' | C277: '1D' | D277: '0097654133' | E277: '=VLOOKUP(G277,Suppliers2[],2,FALSE)' -> '#N/A' | F277: '019132' | G277: '46771045' | C278: '4D' | D278: '0000000991' | E278: '=VLOOKUP(G278,Suppliers2[],2,FALSE)' -> '#N/A' | F278: '019282' | G278: '32577900'

### `02333185f919|LIVE_ERROR|Sheet1!G19`

- workbook: `all_data_912_v0.1/spreadsheet/56419/1_56419_input.xlsx`
- location: `Sheet1!G19`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- evidence: The error propagates to 1 dependent cell(s): Sheet1!H19. Fixing this cell clears them.
- cached value: '#N/A'; row labels: ["'R'"]; column header: ''; used range: A1:H100
- neighbourhood: E17: '=SUM($D$2:D17)' -> 8 | G17: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H17: '=INDIRECT("A"&G17)' -> '#N/A' | E18: '=SUM($D$2:D18)' -> 8 | G18: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H18: '=INDIRECT("A"&G18)' -> '#N/A' | E19: '=SUM($D$2:D19)' -> 8 | G19: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H19: '=INDIRECT("A"&G19)' -> '#N/A' | E20: '=SUM($D$2:D20)' -> 8 | G20: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H20: '=INDIRECT("A"&G20)' -> '#N/A' | E21: '=SUM($D$2:D21)' -> 9 | G21: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H21: '=INDIRECT("A"&G21)' -> '#N/A'

### `40c60acd7755|LIVE_ERROR|Sort!L57`

- workbook: `all_data_912_v0.1/spreadsheet/59932/3_59932_input.xlsx`
- location: `Sort!L57`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'2008_Q2'"]; column header: ''; used range: A1:T147
- neighbourhood: J55: "=VLOOKUP($B55,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 3.9399999999999995 | K55: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A55,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L55: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A55,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M55: '=D55*P55' -> '#VALUE!' | N55: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A55,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J56: "=VLOOKUP($B56,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 4.56 | K56: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A56,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L56: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A56,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M56: '=D56*P56' -> '#VALUE!' | N56: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A56,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J57: "=VLOOKUP($B57,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 4.85 | K57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M57: '=D57*P57' -> '#VALUE!' | N57: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A57,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J58: "=VLOOKUP($B58,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 5.119999999999999 | K58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M58: '=D58*P58' -> '#VALUE!' | N58: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A58,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!' | J59: "=VLOOKUP($B59,'[1]<2010Cal'!$A:$BE,37,FALSE)" -> 5.369999999999999 | K59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$S$12:$S$... -> '#VALUE!' | L59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$T$12:$T$... -> '#VALUE!' | M59: '=D59*P59' -> '#VALUE!' | N59: "=SUMIF('[1]<2010Cal'!$A$12:$A$112,Sort!A59,'[1]<2010Cal'!$M$12:$M$... -> '#VALUE!'

### `1f2994e91d0b|LIVE_ERROR|Sheet1!D239`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/1_189-9_input.xlsx`
- location: `Sheet1!D239`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'LB03Z9'"]; column header: ''; used range: A1:E613
- neighbourhood: B237: 2014-01-01 00:00:00 | C237: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D237: '=INT(C237)-INT(B237)' -> '#VALUE!' | B238: 2014-10-31 00:00:00 | C238: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D238: '=INT(C238)-INT(B238)' -> '#VALUE!' | B239: 2014-10-31 00:00:00 | C239: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D239: '=INT(C239)-INT(B239)' -> '#VALUE!' | B240: 2014-10-31 00:00:00 | C240: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D240: '=INT(C240)-INT(B240)' -> '#VALUE!' | B241: 2014-10-31 00:00:00 | C241: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D241: '=INT(C241)-INT(B241)' -> '#VALUE!'

### `b6d10437377d|LIVE_ERROR|Sheettwo!E192`

- workbook: `all_data_912_v0.1/spreadsheet/54196/1_54196_input.xlsx`
- location: `Sheet two!E192`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'1D'", "'0050603231'"]; column header: ''; used range: A1:G6234
- neighbourhood: C190: '1D' | D190: '0049138342' | E190: '=VLOOKUP(G190,Suppliers2[],2,FALSE)' -> '#N/A' | F190: '013957' | G190: '70263016' | C191: '1D' | D191: '0049264406' | E191: '=VLOOKUP(G191,Suppliers2[],2,FALSE)' -> '#N/A' | F191: '013958' | G191: '70263016' | C192: '1D' | D192: '0050603231' | E192: '=VLOOKUP(G192,Suppliers2[],2,FALSE)' -> '#N/A' | F192: '013971' | G192: '39168400' | C193: '1D' | D193: '0051291845' | E193: '=VLOOKUP(G193,Suppliers2[],2,FALSE)' -> '#N/A' | F193: '013978' | G193: '70263016' | C194: '2D' | D194: '0051717547' | E194: '=VLOOKUP(G194,Suppliers2[],2,FALSE)' -> '#N/A' | F194: '013982' | G194: '39168400'

### `1f2994e91d0b|LIVE_ERROR|Sheet1!D148`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/1_189-9_input.xlsx`
- location: `Sheet1!D148`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'LB06M9'"]; column header: ''; used range: A1:E613
- neighbourhood: B146: 2015-11-30 00:00:00 | C146: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D146: '=INT(C146)-INT(B146)' -> '#VALUE!' | B147: 2013-04-01 00:00:00 | C147: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D147: '=INT(C147)-INT(B147)' -> '#VALUE!' | B148: 2014-10-31 00:00:00 | C148: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D148: '=INT(C148)-INT(B148)' -> '#VALUE!' | B149: 2013-04-01 00:00:00 | C149: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D149: '=INT(C149)-INT(B149)' -> '#VALUE!' | B150: 2013-04-01 00:00:00 | C150: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> '22-10-202211:59:00 PM' | D150: '=INT(C150)-INT(B150)' -> '#VALUE!'

### `acb548947286|LIVE_ERROR|Statistics!G39`

- workbook: `all_data_912_v0.1/spreadsheet/55572/3_55572_input.xlsx`
- location: `Statistics!G39`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- cached value: '#REF!'; row labels: []; column header: ''; used range: A1:AF100
- neighbourhood: E37: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G37: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E38: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G38: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E39: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G39: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E40: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G40: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!' | E41: '=IFERROR(INDEX(\'WK1\'!$A:$R,_xlfn.AGGREGATE(15,6,ROW(\'WK1\'!$B$2... -> None | G41: '=COUNTIF(#REF!,Statistics!$A$3)' -> '#REF!'

### `a94eb6a7585f|LIVE_ERROR|HR!BK14`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !BK14`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 3 dependent cell(s): HR !BK24, HR !BM14, HR !BW14. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'June + July '", "'N/A'"]; column header: ''; used range: A1:GT37
- neighbourhood: BI12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BJ12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BK12: "=INDEX(#REF!,MATCH('HR '!$A12,#REF!,0))" -> '#REF!' | BL12: '=BB12' -> '#REF!' | BM12: '=IF(BK12>99.99,"Yes","No")' -> '#REF!' | BI14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BJ14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BK14: "=INDEX(#REF!,MATCH('HR '!$A14,#REF!,0))" -> '#REF!' | BL14: '=BB14' -> '#REF!' | BM14: '=IF(BK14>99.99,"Yes","No")' -> '#REF!' | BI16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | BJ16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | BK16: "=INDEX(#REF!,MATCH('HR '!$A16,#REF!,0))" -> '#REF!' | BL16: '=BB16' -> '#REF!' | BM16: '=IF(BK16>99.99,"Yes","No")' -> '#REF!'

### `f4cc22517a5b|LIVE_ERROR|master!E10`

- workbook: `all_data_912_v0.1/spreadsheet/47933/1_47933_input.xlsx`
- location: `master!E10`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C8: '=INDEX(amount!A:A,MATCH(A8,amount!B:B,0))' -> 57110.658652939 | D8: '=ROUND(C8/52/B8,2)' -> 27.46 | E8: '=IF(B8<37.5,"2",)*IF(B8>37.5,"D2,1.5,")' -> '#VALUE!' | C9: '=INDEX(amount!A:A,MATCH(A9,amount!B:B,0))' -> 13903.9430568232 | D9: '=ROUND(C9/52/B9,2)' -> 5.35 | E9: '=IF(B9<37.5,"2",)*IF(B9>37.5,"D2,1.5,")' -> '#VALUE!' | C10: '=INDEX(amount!A:A,MATCH(A10,amount!B:B,0))' -> 46996.9587513857 | D10: '=ROUND(C10/52/B10,2)' -> 18.08 | E10: '=IF(B10<37.5,"2",)*IF(B10>37.5,"D2,1.5,")' -> '#VALUE!' | C11: '=INDEX(amount!A:A,MATCH(A11,amount!B:B,0))' -> 94239.707142188 | D11: '=ROUND(C11/52/B11,2)' -> 36.25 | E11: '=IF(B11<37.5,"2",)*IF(B11>37.5,"D2,1.5,")' -> '#VALUE!' | C12: '=INDEX(amount!A:A,MATCH(A12,amount!B:B,0))' -> 30916.9398842618 | D12: '=ROUND(C12/52/B12,2)' -> 14.86 | E12: '=IF(B12<37.5,"2",)*IF(B12>37.5,"D2,1.5,")' -> '#VALUE!'

### `192a19040f63|LIVE_ERROR|Sheettwo!E194`

- workbook: `all_data_912_v0.1/spreadsheet/54196/3_54196_input.xlsx`
- location: `Sheet two!E194`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'2D'", "'0051717547'"]; column header: ''; used range: A1:G6234
- neighbourhood: C192: '1D' | D192: '0050603231' | E192: '=VLOOKUP(G192,Suppliers2[],2,FALSE)' -> '#N/A' | F192: '013971' | G192: '39168400' | C193: '1D' | D193: '0051291845' | E193: '=VLOOKUP(G193,Suppliers2[],2,FALSE)' -> '#N/A' | F193: '013978' | G193: '70263016' | C194: '2D' | D194: '0051717547' | E194: '=VLOOKUP(G194,Suppliers2[],2,FALSE)' -> '#N/A' | F194: '013982' | G194: '39168400' | C195: '1D' | D195: '0051929932' | E195: '=VLOOKUP(G195,Suppliers2[],2,FALSE)' -> '#N/A' | F195: '014094' | G195: '70263016' | C196: '1D' | D196: '0054528660' | E196: '=VLOOKUP(G196,Suppliers2[],2,FALSE)' -> '#N/A' | F196: '014415' | G196: '42812888'

### `79139a88c691|LIVE_ERROR|Sheet1!AS6`

- workbook: `all_data_912_v0.1/spreadsheet/52450/1_52450_input.xlsx`
- location: `Sheet1!AS6`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- evidence: The error propagates to 9 dependent cell(s): Sheet1!AS4, Sheet1!P4, Sheet1!P6, Sheet1!S4, Sheet1!S6, Sheet1!T4, Sheet1!T6, Sheet1!V4, .... Fixing this cell clears them.
- cached value: '#VALUE!'; row labels: ["'Freezing'", "'Scott '"]; column header: ''; used range: A1:NX104
- neighbourhood: AQ4: '=IF($H5="",0,IF($H5<"",SUM(AQ5:AQ104)))' -> '#VALUE!' | AR4: '=IF($H5="",0,IF($H5<"",SUM(AR5:AR104)))' -> '#VALUE!' | AS4: '=IF($H5="",0,IF($H5<"",SUM(AS5:AS104)))' -> '#VALUE!' | AT4: '=IF($H5="",0,IF($H5<"",SUM(AT5:AT104)))' -> '#VALUE!' | AU4: '=IF($H5="",0,IF($H5<"",SUM(AU5:AU104)))' -> '#VALUE!' | AQ5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AR5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AR$1,\'[1]X... -> '#VALUE!' | AS5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AS$1,\'[1]X... -> '#VALUE!' | AT5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AT$1,\'[1]X... -> '#VALUE!' | AU5: '=IF($E5<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AU$1,\'[1]X... -> '#VALUE!' | AQ6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AR6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AR$1,\'[1]X... -> '#VALUE!' | AS6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AS$1,\'[1]X... -> '#VALUE!' | AT6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AT$1,\'[1]X... -> '#VALUE!' | AU6: '=IF($E6<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AU$1,\'[1]X... -> '#VALUE!' | AQ7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AR7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AR$1,\'[1]X... -> '#VALUE!' | AS7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AS$1,\'[1]X... -> '#VALUE!' | AT7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AT$1,\'[1]X... -> '#VALUE!' | AU7: '=IF($E7<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AU$1,\'[1]X... -> '#VALUE!' | AQ8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AQ$1,\'[1]X... -> '#VALUE!' | AR8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AR$1,\'[1]X... -> '#VALUE!' | AS8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AS$1,\'[1]X... -> '#VALUE!' | AT8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AT$1,\'[1]X... -> '#VALUE!' | AU8: '=IF($E8<>"",IF(COUNTIFS(\'[1]XA Data Pull\'!$J:$J,">="&AU$1,\'[1]X... -> '#VALUE!'

### `f98021ebb2e8|LIVE_ERROR|master!E23`

- workbook: `all_data_912_v0.1/spreadsheet/47933/2_47933_input.xlsx`
- location: `master!E23`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: []; column header: ''; used range: A1:E154
- neighbourhood: C21: '=INDEX(amount!A:A,MATCH(A21,amount!B:B,0))' -> 46599.4846328232 | D21: '=ROUND(C21/52/B21,2)' -> 17.92 | E21: '=IF(B21<37.5,"2",)*IF(B21>37.5,"D2,1.5,")' -> '#VALUE!' | C22: '=INDEX(amount!A:A,MATCH(A22,amount!B:B,0))' -> 29027.7828315894 | D22: '=ROUND(C22/52/B22,2)' -> 14.89 | E22: '=IF(B22<37.5,"2",)*IF(B22>37.5,"D2,1.5,")' -> 0 | C23: '=INDEX(amount!A:A,MATCH(A23,amount!B:B,0))' -> 83106.1973090378 | D23: '=ROUND(C23/52/B23,2)' -> 31.96 | E23: '=IF(B23<37.5,"2",)*IF(B23>37.5,"D2,1.5,")' -> '#VALUE!' | C24: '=INDEX(amount!A:A,MATCH(A24,amount!B:B,0))' -> 57222.8582600114 | D24: '=ROUND(C24/52/B24,2)' -> 27.51 | E24: '=IF(B24<37.5,"2",)*IF(B24>37.5,"D2,1.5,")' -> '#VALUE!' | C25: '=INDEX(amount!A:A,MATCH(A25,amount!B:B,0))' -> 64631.2776217746 | D25: '=ROUND(C25/52/B25,2)' -> 31.07 | E25: '=IF(B25<37.5,"2",)*IF(B25>37.5,"D2,1.5,")' -> '#VALUE!'

### `c2bacd4fd237|LIVE_ERROR|Data!H53`

- workbook: `all_data_912_v0.1/spreadsheet/510-3/3_510-3_input.xlsx`
- location: `Data!H53`  severity: Critical  confidence: Defect
- evidence: Cell contains #VALUE!.
- cached value: '#VALUE!'; row labels: ["'\\u202d08'", "'07\\u202c'"]; column header: "'#VALUE!'"; used range: A1:H78
- neighbourhood: F51: 1 | G51: '07\u202c' | H51: '#VALUE!' | F52: 1 | G52: '07\u202c' | H52: '#VALUE!' | F53: 1 | G53: '07\u202c' | H53: '#VALUE!' | F54: 1 | G54: '07\u202c' | H54: '#VALUE!' | F55: 1 | G55: '07\u202c' | H55: '#VALUE!'

### `ab88bab5d14b|LIVE_ERROR|Sheet1!G13`

- workbook: `all_data_912_v0.1/spreadsheet/50154/2_50154_input.xlsx`
- location: `Sheet1!G13`  severity: Critical  confidence: Defect
- evidence: Cell contains #DIV/0!.
- evidence: The error propagates to 2 dependent cell(s): Sheet1!H13, Sheet1!L4. Fixing this cell clears them.
- cached value: '#DIV/0!'; row labels: []; column header: ''; used range: A1:O15
- neighbourhood: F11: '=IF(D11="Y",1,0)' -> 0 | G11: '=AVERAGE(B11:C11,E11)' -> '#DIV/0!' | H11: '=SUM(G11,F11)' -> '#DIV/0!' | F12: '=IF(D12="Y",1,0)' -> 0 | G12: '=AVERAGE(B12:C12,E12)' -> '#DIV/0!' | H12: '=SUM(G12,F12)' -> '#DIV/0!' | F13: '=IF(D13="Y",1,0)' -> 0 | G13: '=AVERAGE(B13:C13,E13)' -> '#DIV/0!' | H13: '=SUM(G13,F13)' -> '#DIV/0!' | F14: '=IF(D14="Y",1,0)' -> 0 | G14: '=AVERAGE(B14:C14,E14)' -> '#DIV/0!' | H14: '=SUM(G14,F14)' -> '#DIV/0!'

### `a94eb6a7585f|LIVE_ERROR|HR!BV5`

- workbook: `all_data_912_v0.1/spreadsheet/54590/2_54590_input.xlsx`
- location: `HR !BV5`  severity: Critical  confidence: Defect
- evidence: Formula contains #REF!, so the cell evaluates to that error whatever its inputs.
- evidence: The error propagates to 4 dependent cell(s): HR !BV24, HR !BX5, HR !CH5, HR !CN5. Fixing this cell clears them.
- cached value: '#REF!'; row labels: ["'Aug - Oct'", "'Month 1'"]; column header: ''; used range: A1:GT37
- neighbourhood: BT3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | BU3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | BV3: "=INDEX(#REF!,MATCH('HR '!$A3,#REF!,0))" -> '#REF!' | BW3: '=BM3' -> 'Yes' | BX3: '=IF(BV3>99.99,"Yes","No")' -> '#REF!' | BT4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | BU4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | BV4: "=INDEX(#REF!,MATCH('HR '!$A4,#REF!,0))" -> '#REF!' | BW4: '=BM4' -> '#REF!' | BX4: '=IF(BV4>99.99,"Yes","No")' -> '#REF!' | BT5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BU5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BV5: "=INDEX(#REF!,MATCH('HR '!$A5,#REF!,0))" -> '#REF!' | BW5: '=BM5' -> '#REF!' | BX5: '=IF(BV5>99.99,"Yes","No")' -> '#REF!' | BT7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BU7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BV7: "=INDEX(#REF!,MATCH('HR '!$A7,#REF!,0))" -> '#REF!' | BW7: '=BM7' -> '#REF!' | BX7: '=IF(BV7>99.99,"Yes","No")' -> '#REF!'

### `241b116795b4|LIVE_ERROR|Sheet1!S8`

- workbook: `all_data_912_v0.1/spreadsheet/38969/3_38969_input.xlsx`
- location: `Sheet1!S8`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'Upload'"]; column header: "'#N/A'"; used range: A1:U20
- neighbourhood: R6: 'Upload' | S6: '#N/A' | U6: -14794.53 | R7: 'Upload' | S7: '#N/A' | U7: -12593.64 | R8: 'Upload' | S8: '#N/A' | U8: -605590.29 | R9: 'Upload' | S9: '#N/A' | U9: -96197.98 | R10: 'Upload' | S10: '#N/A' | U10: -130013.51

### `891d500f03e7|LIVE_ERROR|Exp-DB!G29`

- workbook: `all_data_912_v0.1/spreadsheet/524-31/2_524-31_input.xlsx`
- location: `Exp-DB!G29`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'misc'", "'LINCOLN AFS FORDCREDIT'"]; column header: ''; used range: A1:G53
- neighbourhood: E27: '=VLOOKUP(D27 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G27: '=INDEX(cats,MATCH("*"&D27&"*",exDB,0))' -> '#N/A' | E28: '=VLOOKUP(D28 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G28: '=INDEX(cats,MATCH("*"&D28&"*",exDB,0))' -> '#N/A' | E29: '=VLOOKUP(D29 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G29: '=INDEX(cats,MATCH("*"&D29&"*",exDB,0))' -> '#N/A' | E30: '=VLOOKUP(D30 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G30: '=INDEX(cats,MATCH("*"&D30&"*",exDB,0))' -> '#N/A' | E31: '=VLOOKUP(D31 & "*",$A$1:$B$37,2,0)' -> '#N/A' | G31: '=INDEX(cats,MATCH("*"&D31&"*",exDB,0))' -> '#N/A'

### `6fd6aa9b279e|LIVE_ERROR|PRINT!H39`

- workbook: `all_data_912_v0.1/spreadsheet/49490/2_49490_input.xlsx`
- location: `PRINT!H39`  severity: Critical  confidence: Defect
- evidence: Cell contains #N/A.
- cached value: '#N/A'; row labels: ["'STORE'"]; column header: "'#N/A'"; used range: A1:L1001
- neighbourhood: F37: 0 | G37: 0 | H37: '#N/A' | I37: 'STITCHING' | J37: 0 | F38: 0 | G38: 0 | H38: '#N/A' | I38: 'STITCHING' | J38: 0 | F39: 0 | G39: 0 | H39: '#N/A' | I39: 'STITCHING' | J39: 0 | F40: 0 | G40: 0 | H40: '#N/A' | I40: 'STITCHING' | J40: 0 | F41: 0 | G41: 0 | H41: '#N/A' | I41: 'STITCHING' | J41: 0

## MERGED_CELL_IN_DATA_RANGE

### `3a2b74c70f66|MERGED_CELL_IN_DATA_RANGE|Total(2)!A39:H39`

- workbook: `all_data_912_v0.1/spreadsheet/47766/2_47766_input.xlsx`
- location: `Total (2)!A39:H39`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Sales'; row labels: []; column header: ''; used range: A1:Z1026
- neighbourhood: B37: 0 | C37: '=(B37*12)/12' -> 0 | B38: '=SUM(B8:B37)' -> 55429 | C38: '=SUM(C8:C37)' -> 54029 | A39: 'Sales' | A40: 'Address' | B40: 'Price' | C40: 'Commission' | A41: 1 | B41: 430000 | C41: '=B41*0.02' -> 8600

### `0e8785562296|MERGED_CELL_IN_DATA_RANGE|DATA!N12:Q12`

- workbook: `all_data_912_v0.1/spreadsheet/56915/2_56915_input.xlsx`
- location: `DATA!N12:Q12`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'D - 2222'; row labels: ["'V - 6666'", "'D - 1111'"]; column header: ''; used range: A1:AC24
- neighbourhood: N12: 'D - 2222' | L13: 'YTD' | M13: '% age' | N13: 'January' | O13: '% age' | P13: 'YTD'

### `59dd5b78ebc8|MERGED_CELL_IN_DATA_RANGE|results!A69:A71`

- workbook: `all_data_912_v0.1/spreadsheet/54490/3_54490_input.xlsx`
- location: `results!A69:A71`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-23 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: B67: 'Late' | C67: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 186.753846153846 | B68: 'Night' | C68: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 165.814323607427 | A69: 2021-04-23 00:00:00 | B69: 'Early' | C69: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 145.615384615385 | B70: 'Late' | C70: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 177.263736263736 | B71: 'Night' | C71: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 165.08875739645

### `d6b8caaa9b61|MERGED_CELL_IN_DATA_RANGE|Transactions!A1:D1`

- workbook: `all_data_912_v0.1/spreadsheet/46121/1_46121_input.xlsx`
- location: `Transactions!A1:D1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Income'; row labels: []; column header: ''; used range: A1:L22
- neighbourhood: A1: 'Income' | A2: 'Month' | B2: 'Description' | C2: 'Amount' | A3: 'March' | B3: '2 Guineas' | C3: 40

### `59dd5b78ebc8|MERGED_CELL_IN_DATA_RANGE|results!A87:A89`

- workbook: `all_data_912_v0.1/spreadsheet/54490/3_54490_input.xlsx`
- location: `results!A87:A89`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-29 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: B85: 'Late' | C85: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 173.300248138958 | B86: 'Night' | C86: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 134.064777327935 | A87: 2021-04-29 00:00:00 | B87: 'Early' | C87: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 0 | B88: 'Late' | C88: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 156.738461538462 | B89: 'Night' | C89: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 182.254945054945

### `e3281236e4b3|MERGED_CELL_IN_DATA_RANGE|results!A90:A92`

- workbook: `all_data_912_v0.1/spreadsheet/54490/2_54490_input.xlsx`
- location: `results!A90:A92`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-30 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: B88: 'Late' | C88: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 156.738461538462 | B89: 'Night' | C89: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 182.254945054945 | A90: 2021-04-30 00:00:00 | B90: 'Early' | C90: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 0 | B91: 'Late' | C91: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 142.925373134328 | B92: 'Night' | C92: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 159.146473779385

### `0c8efee86893|MERGED_CELL_IN_DATA_RANGE|Input!A7:A8`

- workbook: `all_data_912_v0.1/spreadsheet/48975/2_48975_input.xlsx`
- location: `Input!A7:A8`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Nr.'; row labels: []; column header: ''; used range: A1:F34
- neighbourhood: B5: 'Header' | C5: 'Header' | A7: 'Nr.' | B7: 'Text' | C7: 'Yes' | A9: 1 | B9: 'Text 100'

### `7c3edf13b7c6|MERGED_CELL_IN_DATA_RANGE|Malaga!A6:M6`

- workbook: `all_data_912_v0.1/spreadsheet/40809/2_40809_input.xlsx`
- location: `Malaga!A6:M6`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Golf'; row labels: []; column header: "'Not Inc: Flights available from Birmingham & Gatwick, Lu..."; used range: A1:AJ57
- neighbourhood: A4: '7 nights All-Inclusive, Transfers, 4... | A5: 'Not Inc: Flights available from Birm... | A6: 'Golf' | A7: 'Golf at La Cala America, La Cala Asi... | A8: 'No' | B8: 'Room' | C8: 'NAME'

### `e3281236e4b3|MERGED_CELL_IN_DATA_RANGE|results!A81:A83`

- workbook: `all_data_912_v0.1/spreadsheet/54490/2_54490_input.xlsx`
- location: `results!A81:A83`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-27 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: B79: 'Late' | C79: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 153.668839634941 | B80: 'Night' | C80: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 174.626373626374 | A81: 2021-04-27 00:00:00 | B81: 'Early' | C81: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 0 | B82: 'Late' | C82: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 182.065934065934 | B83: 'Night' | C83: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 177.028451001054

### `d9d042a38e4d|MERGED_CELL_IN_DATA_RANGE|Transactions!A1:D1`

- workbook: `all_data_912_v0.1/spreadsheet/46121/2_46121_input.xlsx`
- location: `Transactions!A1:D1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Income'; row labels: []; column header: ''; used range: A1:L22
- neighbourhood: A1: 'Income' | A2: 'Month' | B2: 'Description' | C2: 'Amount' | A3: 'March' | B3: '2 Guineas' | C3: 40

### `d7e27f29097e|MERGED_CELL_IN_DATA_RANGE|Malaga!J5:K5`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!J5:K5`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: '**SINGLE SUPPLEMENT'; row labels: ["'Not Inc: Flights available from Birmingham & Gatwick, Lu..."]; column header: "'*Non-Golfer'"; used range: A1:AJ57
- neighbourhood: J4: '*Non-Golfer' | L4: 449 | J5: '**SINGLE SUPPLEMENT' | L5: 1044 | H7: 'La Cala Europa & Santa Monica'

### `4cfd58a6f68f|MERGED_CELL_IN_DATA_RANGE|DATA!B12:E12`

- workbook: `all_data_912_v0.1/spreadsheet/56915/1_56915_input.xlsx`
- location: `DATA!B12:E12`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Total'; row labels: ["' '"]; column header: ''; used range: A1:AC24
- neighbourhood: A11: ' ' | A12: ' ' | B12: 'Total' | A13: ' ' | B13: 'January' | C13: '% age' | D13: 'YTD'

### `a110c7e07fc9|MERGED_CELL_IN_DATA_RANGE|results!A3:A5`

- workbook: `all_data_912_v0.1/spreadsheet/54490/1_54490_input.xlsx`
- location: `results!A3:A5`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-01 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: C2: 'T48 - Machine 1 (Oliver)' | A3: 2021-04-01 00:00:00 | B3: 'Early' | C3: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 132.218181818182 | B4: 'Late' | C4: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 185.929595827901 | B5: 'Night' | C5: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 185.922077922078

### `623070110cdb|MERGED_CELL_IN_DATA_RANGE|Leave_Record!G4:AK4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13024/2_CF_13024_input.xlsx`
- location: `Leave_Record!G4:AK4`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2022-06-01 00:00:00; row labels: []; column header: ''; used range: A1:BI34
- neighbourhood: G4: 2022-06-01 00:00:00 | F5: 'Roster' | G5: '=G4' -> 2022-06-01 00:00:00 | H5: '=G5+1' -> 2022-06-02 00:00:00 | I5: '=H5+1' -> 2022-06-03 00:00:00 | E6: 'Shift Type' | F6: 'A/B' | G6: '=TEXT(G5,"ddd")' -> 'Wed' | H6: '=TEXT(H5,"ddd")' -> 'Thu' | I6: '=TEXT(I5,"ddd")' -> 'Fri'

### `5ec32da9071e|MERGED_CELL_IN_DATA_RANGE|Total(2)!J32:K32`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!J32:K32`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: None; row labels: ["'C'", "'GS'"]; column header: "'CC'"; used range: A1:Z1026
- neighbourhood: H30: 'GS' | I30: '=D30/C30' -> 0.383333333333333 | H31: 'CC' | I31: '=D31/C31' -> 0.5 | H32: 'GS' | I32: '=D32/C32' -> 0.35 | H33: 'PE' | I33: '=D33/C33' -> 0.2 | I34: '=D34/C34' -> '#DIV/0!'

### `a110c7e07fc9|MERGED_CELL_IN_DATA_RANGE|results!A45:A47`

- workbook: `all_data_912_v0.1/spreadsheet/54490/1_54490_input.xlsx`
- location: `results!A45:A47`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2021-04-15 00:00:00; row labels: []; column header: ''; used range: A1:Z98
- neighbourhood: B43: 'Late' | C43: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 175.542510121457 | B44: 'Night' | C44: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 187.006134969325 | A45: 2021-04-15 00:00:00 | B45: 'Early' | C45: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 0 | B46: 'Late' | C46: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 180.936454849498 | B47: 'Night' | C47: '=SUMIFS(\'data April\'!$D$2:$D$2161,\'data April\'!$A$2:$A$2161,LO... -> 170.186234817814

### `7c3edf13b7c6|MERGED_CELL_IN_DATA_RANGE|Malaga!A2:M2`

- workbook: `all_data_912_v0.1/spreadsheet/40809/2_40809_input.xlsx`
- location: `Malaga!A2:M2`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'at Gran Hotel Cervantes'; row labels: []; column header: "'Holiday in Malaga, Spain'"; used range: A1:AJ57
- neighbourhood: A1: 'Holiday in Malaga, Spain' | A2: 'at Gran Hotel Cervantes' | A3: 'Wednesday 11th October to Wednesday ... | A4: '7 nights All-Inclusive, Transfers, 4...

### `5d8e01837ace|MERGED_CELL_IN_DATA_RANGE|Leave_Record!G4:AK4`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13024/3_CF_13024_input.xlsx`
- location: `Leave_Record!G4:AK4`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 2022-06-01 00:00:00; row labels: []; column header: ''; used range: A1:BI34
- neighbourhood: G4: 2022-06-01 00:00:00 | F5: 'Roster' | G5: '=G4' -> 2022-06-01 00:00:00 | H5: '=G5+1' -> 2022-06-02 00:00:00 | I5: '=H5+1' -> 2022-06-03 00:00:00 | E6: 'Shift Type' | F6: 'A/B' | G6: '=TEXT(G5,"ddd")' -> 'Wed' | H6: '=TEXT(H5,"ddd")' -> 'Thu' | I6: '=TEXT(I5,"ddd")' -> 'Fri'

### `0e8785562296|MERGED_CELL_IN_DATA_RANGE|DATA!J12:M12`

- workbook: `all_data_912_v0.1/spreadsheet/56915/2_56915_input.xlsx`
- location: `DATA!J12:M12`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'D - 1111'; row labels: ["'Total'", "'V - 6666'"]; column header: ''; used range: A1:AC24
- neighbourhood: H10: ' ' | J12: 'D - 1111' | H13: 'YTD' | I13: '% age' | J13: 'January' | K13: '% age' | L13: 'YTD'

### `d7e27f29097e|MERGED_CELL_IN_DATA_RANGE|Malaga!L4:M4`

- workbook: `all_data_912_v0.1/spreadsheet/40809/3_40809_input.xlsx`
- location: `Malaga!L4:M4`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 449; row labels: ["'7 nights All-Inclusive, Transfers, 4 rounds with Buggies ='", "'*Non-Golfer'"]; column header: ''; used range: A1:AJ57
- neighbourhood: J4: '*Non-Golfer' | L4: 449 | J5: '**SINGLE SUPPLEMENT' | L5: 1044

### `bc56a9f2824a|MERGED_CELL_IN_DATA_RANGE|Total(2)!G75:H75`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!G75:H75`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 0.2; row labels: []; column header: "'C'"; used range: A1:Z1026
- neighbourhood: E73: '=IFERROR(VLOOKUP($H73,$J$27:$L$35,3,0)*$C73,0)' -> 0 | I73: '=D73/C73' -> '#DIV/0!' | E74: '=IFERROR(VLOOKUP($H74,$J$27:$L$35,3,0)*$C74,0)' -> 0 | I74: '=D74/C74' -> '#DIV/0!' | E75: '=SUM(E62:E74)' -> 9868 | G75: '=D75/C75' -> 0.2

### `bc56a9f2824a|MERGED_CELL_IN_DATA_RANGE|Total(2)!A1:H1`

- workbook: `all_data_912_v0.1/spreadsheet/47766/1_47766_input.xlsx`
- location: `Total (2)!A1:H1`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: None; row labels: []; column header: ''; used range: A1:Z1026

### `4cfd58a6f68f|MERGED_CELL_IN_DATA_RANGE|COVER!B12:E12`

- workbook: `all_data_912_v0.1/spreadsheet/56915/1_56915_input.xlsx`
- location: `COVER!B12:E12`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'V - 6666'; row labels: ["'Entity >>'"]; column header: ''; used range: A1:E23
- neighbourhood: A11: ' ' | A12: 'Entity >>' | B12: 'V - 6666' | A13: ' ' | B13: 'January' | C13: '% age' | D13: 'YTD'

### `ef479c030de6|MERGED_CELL_IN_DATA_RANGE|Sheet1!BI2:BJ2`

- workbook: `all_data_912_v0.1/spreadsheet/32789/1_32789_input.xlsx`
- location: `Sheet1!BI2:BJ2`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'Customers Helped / Cases Solved'; row labels: ["'Case Replies'", "'Case Replies'"]; column header: ''; used range: A1:BR82
- neighbourhood: BG2: 'Case Replies' | BH2: 'Case Replies' | BI2: 'Customers Helped / Cases Solved' | BK2: 'ABC' | BG3: 'Goal #' | BH3: 'Goal %' | BI3: 'Goal #' | BJ3: 'Goal %' | BK3: 'Goal #' | BG4: 6 | BH4: 8 | BI4: 7 | BJ4: 9 | BK4: 8

### `5ec32da9071e|MERGED_CELL_IN_DATA_RANGE|Total(2)!J27:K27`

- workbook: `all_data_912_v0.1/spreadsheet/47766/3_47766_input.xlsx`
- location: `Total (2)!J27:K27`  severity: Medium  confidence: Review
- evidence: Merged region lies inside a range that formulas read; only its top-left cell holds a value, so aggregates and lookups over it see blanks.
- cached value: 'PE'; row labels: ["'C'", "'CC'"]; column header: "'Agent Name'"; used range: A1:Z1026
- neighbourhood: H25: 'GS' | I25: '=D25/C25' -> 0.4 | J25: 'AGENT SCORECARD' | H26: 'CC' | I26: '=D26/C26' -> 0.478260869565217 | J26: 'Agent Name' | L26: 'Split A' | H27: 'CC' | I27: '=D27/C27' -> 0.478260869565217 | J27: 'PE' | L27: 0.8 | H28: 'PE' | I28: '=D28/C28' -> 0.2 | J28: 'GS' | L28: 0.65 | H29: 'PE' | I29: '=D29/C29' -> 0.2 | J29: 'CC' | L29: 0.6

## NUMBERS_STORED_AS_TEXT

### `8a63f3e46c57|NUMBERS_STORED_AS_TEXT|RawData!D14`

- workbook: `all_data_912_v0.1/spreadsheet/6435/3_6435_input.xlsx`
- location: `Raw Data!D14`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '0013' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '0013'; row labels: []; column header: "'0013'"; used range: A1:P110
- neighbourhood: B12: 3 | C12: 2017-05-31 00:00:00 | D12: '0013' | E12: '9940' | F12: '=IF(D12="","",IF(E12="","",IF(ISODD(COUNTIFS(D$4:D12,D12,E$4:E12,E... -> 'In' | B13: 4 | C13: 2017-05-31 00:00:00 | D13: '0013' | E13: '9940' | F13: '=IF(D13="","",IF(E13="","",IF(ISODD(COUNTIFS(D$4:D13,D13,E$4:E13,E... -> 'Out' | B14: 5 | C14: 2017-07-20 00:00:00 | D14: '0013' | E14: '9940' | F14: '=IF(D14="","",IF(E14="","",IF(ISODD(COUNTIFS(D$4:D14,D14,E$4:E14,E... -> 'In' | B15: 10 | C15: 2017-08-24 00:00:00 | D15: '0013' | E15: '9940' | F15: '=IF(D15="","",IF(E15="","",IF(ISODD(COUNTIFS(D$4:D15,D15,E$4:E15,E... -> 'Out' | B16: 11 | C16: 2017-09-06 00:00:00 | D16: '0013' | E16: '0142' | F16: '=IF(D16="","",IF(E16="","",IF(ISODD(COUNTIFS(D$4:D16,D16,E$4:E16,E... -> 'Out'

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A1016`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A1016`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1463' in a column that otherwise holds 1547 numbers.
- cached value: '1463'; row labels: []; column header: "'1462'"; used range: A1:K2802
- neighbourhood: A1014: '1453' | B1014: 1500006150 | C1014: 2018-09-10 00:00:00 | A1015: '1462' | B1015: 1500006150 | C1015: 2018-09-10 00:00:00 | A1016: '1463' | B1016: 1500006150 | C1016: 2018-09-10 00:00:00 | A1017: '1474' | B1017: 1500006150 | C1017: 2018-09-10 00:00:00 | A1018: '1475' | B1018: 1500006150 | C1018: 2018-09-10 00:00:00

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A1057`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A1057`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1593' in a column that otherwise holds 1547 numbers.
- cached value: '1593'; row labels: []; column header: "'1557'"; used range: A1:K2802
- neighbourhood: A1055: '1535' | B1055: 1500006150 | C1055: 2018-09-21 00:00:00 | A1056: '1557' | B1056: 1500006150 | C1056: 2018-09-21 00:00:00 | A1057: '1593' | B1057: 1500006150 | C1057: 2018-09-21 00:00:00 | A1058: '1615' | B1058: 1500006150 | C1058: 2018-09-21 00:00:00 | A1059: '2756' | B1059: '2500074720' | C1059: 2018-09-25 00:00:00

### `d7ea7b98cf47|NUMBERS_STORED_AS_TEXT|KPI1!C156`

- workbook: `all_data_912_v0.1/spreadsheet/49455/2_49455_input.xlsx`
- location: `KPI 1!C156`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '223143' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '223143'; row labels: []; column header: "'220276'"; used range: A1:K208
- neighbourhood: C154: '222873' | D154: 'Apple' | C155: '220276' | D155: 'Banana' | C156: '223143' | D156: 'Newspaper' | C157: '223821' | D157: 'Apple' | C158: '223363' | D158: 'Newspaper'

### `d7ea7b98cf47|NUMBERS_STORED_AS_TEXT|KPI1!C50`

- workbook: `all_data_912_v0.1/spreadsheet/49455/2_49455_input.xlsx`
- location: `KPI 1!C50`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '218430' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '218430'; row labels: []; column header: "'222390'"; used range: A1:K208
- neighbourhood: C48: '223543' | D48: 'Apple' | C49: '222390' | D49: 'Apple' | C50: '218430' | D50: 'Newspaper' | C51: '223597' | D51: 'Apple' | C52: '223078' | D52: 'Apple'

### `7fc97bb4d304|NUMBERS_STORED_AS_TEXT|Sheet1!A112`

- workbook: `all_data_912_v0.1/spreadsheet/57090/3_57090_input.xlsx`
- location: `Sheet1!A112`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1094' in a column that otherwise holds 1547 numbers.
- cached value: '1094'; row labels: []; column header: "'1093'"; used range: A1:K2802
- neighbourhood: A110: '1092' | B110: 2500072970 | C110: 2018-03-08 00:00:00 | A111: '1093' | B111: 2500072970 | C111: 2018-03-08 00:00:00 | A112: '1094' | B112: 2500072970 | C112: 2018-03-08 00:00:00 | A113: '1095' | B113: 2500072970 | C113: 2018-03-08 00:00:00 | A114: '1255' | B114: 4500041932 | C114: 2018-03-08 00:00:00

### `f90e8e67dffb|NUMBERS_STORED_AS_TEXT|KPI1!C156`

- workbook: `all_data_912_v0.1/spreadsheet/49455/1_49455_input.xlsx`
- location: `KPI 1!C156`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '223143' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '223143'; row labels: []; column header: "'220276'"; used range: A1:K208
- neighbourhood: C154: '222873' | D154: 'Apple' | C155: '220276' | D155: 'Banana' | C156: '223143' | D156: 'Newspaper' | C157: '223821' | D157: 'Apple' | C158: '223363' | D158: 'Newspaper'

### `7f9746d5c513|NUMBERS_STORED_AS_TEXT|DATA!B127`

- workbook: `all_data_912_v0.1/spreadsheet/58656/3_58656_input.xlsx`
- location: `DATA!B127`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '7' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '7'; row labels: []; column header: "'6'"; used range: A1:K132
- neighbourhood: A125: 2023 | B125: '6' | C125: 18 | D125: '=IF(F125>TIME(23,59,59),DATE(A125,B125,C125)+1,DATE(A125,B125,C125))' -> 2023-06-18 00:00:00 | A126: 2023 | B126: '6' | C126: 26 | D126: '=IF(F126>TIME(23,59,59),DATE(A126,B126,C126)+1,DATE(A126,B126,C126))' -> 2023-06-26 00:00:00 | A127: 2023 | B127: '7' | C127: 3 | D127: '=IF(F127>TIME(23,59,59),DATE(A127,B127,C127)+1,DATE(A127,B127,C127))' -> 2023-07-03 00:00:00 | A128: 2023 | B128: '7' | C128: 10 | D128: '=IF(F128>TIME(23,59,59),DATE(A128,B128,C128)+1,DATE(A128,B128,C128))' -> 2023-07-10 00:00:00 | A129: 2023 | B129: '7' | C129: 17 | D129: '=IF(F129>TIME(23,59,59),DATE(A129,B129,C129)+1,DATE(A129,B129,C129))' -> 2023-07-17 00:00:00

### `f90e8e67dffb|NUMBERS_STORED_AS_TEXT|KPI1!C208`

- workbook: `all_data_912_v0.1/spreadsheet/49455/1_49455_input.xlsx`
- location: `KPI 1!C208`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '221405' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '221405'; row labels: []; column header: "'224161'"; used range: A1:K208
- neighbourhood: C206: '214998' | C207: '224161' | C208: '221405'

### `03acf31e2499|NUMBERS_STORED_AS_TEXT|Sheet1!A1075`

- workbook: `all_data_912_v0.1/spreadsheet/57090/1_57090_input.xlsx`
- location: `Sheet1!A1075`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2724' in a column that otherwise holds 1547 numbers.
- cached value: '2724'; row labels: []; column header: "'2723'"; used range: A1:K2802
- neighbourhood: A1073: '2715' | B1073: '8700000120' | C1073: 2018-09-26 00:00:00 | A1074: '2723' | B1074: '3500030040' | C1074: 2018-09-27 00:00:00 | A1075: '2724' | B1075: '3500030040' | C1075: 2018-09-27 00:00:00 | A1076: '2725' | B1076: '3500030040' | C1076: 2018-09-27 00:00:00 | A1077: '2726' | B1077: '3500030040' | C1077: 2018-09-27 00:00:00

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet1!E30`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet1!E30`  severity: Medium  confidence: Review
- evidence: Cell contains text value '40045' in a column that otherwise holds 53 numbers.
- cached value: '40045'; row labels: ["'3G'"]; column header: "'15334'"; used range: A1:J168
- neighbourhood: C28: 'Network ' | D28: 'Generation' | E28: 'Serving Cells' | C29: 'O2' | D29: '2G' | E29: '15334' | D30: '3G' | E30: '40045' | F30: '50045' | D31: '4G' | E31: 134333352 | C32: 'Network ' | D32: 'Generation' | E32: 'Serving Cells'

### `7f9746d5c513|NUMBERS_STORED_AS_TEXT|EXAMPLE!B5`

- workbook: `all_data_912_v0.1/spreadsheet/58656/3_58656_input.xlsx`
- location: `EXAMPLE!B5`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '1' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '1'; row labels: []; column header: "'1'"; used range: A1:K36
- neighbourhood: A3: 'YEAR' | B3: 'MONTH' | C3: 'DAY' | D3: 'DATE' | A4: 2021 | B4: '1' | C4: 6 | D4: '=IF(F4>TIME(23,59,59),DATE(A4,B4,C4)+1,DATE(A4,B4,C4))' -> 2021-01-06 00:00:00 | A5: 2021 | B5: '1' | C5: 13 | D5: '=IF(F5>TIME(23,59,59),DATE(A5,B5,C5)+1,DATE(A5,B5,C5))' -> 2021-01-13 00:00:00 | A6: 2021 | B6: '1' | C6: 20 | D6: '=IF(F6>TIME(23,59,59),DATE(A6,B6,C6)+1,DATE(A6,B6,C6))' -> 2021-01-20 00:00:00 | A7: 2021 | B7: '1' | C7: 28 | D7: '=IF(F7>TIME(23,59,59),DATE(A7,B7,C7)+1,DATE(A7,B7,C7))' -> 2021-01-28 00:00:00

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1017`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1017`  severity: Medium  confidence: Review
- evidence: Cell contains text value '1474' in a column that otherwise holds 1547 numbers.
- cached value: '1474'; row labels: []; column header: "'1463'"; used range: A1:K2802
- neighbourhood: A1015: '1462' | B1015: 1500006150 | C1015: 2018-09-10 00:00:00 | A1016: '1463' | B1016: 1500006150 | C1016: 2018-09-10 00:00:00 | A1017: '1474' | B1017: 1500006150 | C1017: 2018-09-10 00:00:00 | A1018: '1475' | B1018: 1500006150 | C1018: 2018-09-10 00:00:00 | A1019: '1482' | B1019: 1500006150 | C1019: 2018-09-10 00:00:00

### `e91e37899ef5|NUMBERS_STORED_AS_TEXT|DATA!B130`

- workbook: `all_data_912_v0.1/spreadsheet/58656/2_58656_input.xlsx`
- location: `DATA!B130`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '7' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '7'; row labels: []; column header: "'7'"; used range: A1:K132
- neighbourhood: A128: 2023 | B128: '7' | C128: 10 | D128: '=IF(F128>TIME(23,59,59),DATE(A128,B128,C128)+1,DATE(A128,B128,C128))' -> 2023-07-10 00:00:00 | A129: 2023 | B129: '7' | C129: 17 | D129: '=IF(F129>TIME(23,59,59),DATE(A129,B129,C129)+1,DATE(A129,B129,C129))' -> 2023-07-17 00:00:00 | A130: 2023 | B130: '7' | C130: 25 | D130: '=IF(F130>TIME(23,59,59),DATE(A130,B130,C130)+1,DATE(A130,B130,C130))' -> 2023-07-26 00:00:00 | A131: 2023 | B131: '8' | C131: 1 | D131: '=IF(F131>TIME(23,59,59),DATE(A131,B131,C131)+1,DATE(A131,B131,C131))' -> 2023-08-01 00:00:00 | A132: 2023 | B132: '8' | C132: 8 | D132: '=IF(F132>TIME(23,59,59),DATE(A132,B132,C132)+1,DATE(A132,B132,C132))' -> 2023-08-08 00:00:00

### `876eccba2276|NUMBERS_STORED_AS_TEXT|Sheet2!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/2_124-46_input.xlsx`
- location: `Sheet2!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 41 numbers.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: E3: 10433 | F3: 11114 | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `4dea3614ed1b|NUMBERS_STORED_AS_TEXT|Sheet1!A1163`

- workbook: `all_data_912_v0.1/spreadsheet/57090/2_57090_input.xlsx`
- location: `Sheet1!A1163`  severity: Medium  confidence: Review
- evidence: Cell contains text value '2854' in a column that otherwise holds 1547 numbers.
- cached value: '2854'; row labels: []; column header: "'2853'"; used range: A1:K2802
- neighbourhood: A1161: '1638' | B1161: 1500006150 | C1161: 2018-10-08 00:00:00 | A1162: '2853' | B1162: '6500035904' | C1162: 2018-10-08 00:00:00 | A1163: '2854' | B1163: '6500035904' | C1163: 2018-10-08 00:00:00 | A1164: '2855' | B1164: '6500035904' | C1164: 2018-10-08 00:00:00 | A1165: '2856' | B1165: '6500035904' | C1165: 2018-10-08 00:00:00

### `9e41b3b532ac|NUMBERS_STORED_AS_TEXT|KPI1!C206`

- workbook: `all_data_912_v0.1/spreadsheet/49455/3_49455_input.xlsx`
- location: `KPI 1!C206`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '214998' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '214998'; row labels: []; column header: "'222393'"; used range: A1:K208
- neighbourhood: C204: '218552' | C205: '222393' | C206: '214998' | C207: '224161' | C208: '221405'

### `e8ad2d127d26|NUMBERS_STORED_AS_TEXT|DATA!B119`

- workbook: `all_data_912_v0.1/spreadsheet/58656/1_58656_input.xlsx`
- location: `DATA!B119`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '5' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '5'; row labels: []; column header: "'4'"; used range: A1:K132
- neighbourhood: A117: 2023 | B117: '4' | C117: 20 | D117: '=IF(F117>TIME(23,59,59),DATE(A117,B117,C117)+1,DATE(A117,B117,C117))' -> 2023-04-20 00:00:00 | A118: 2023 | B118: '4' | C118: 27 | D118: '=IF(F118>TIME(23,59,59),DATE(A118,B118,C118)+1,DATE(A118,B118,C118))' -> 2023-04-27 00:00:00 | A119: 2023 | B119: '5' | C119: 5 | D119: '=IF(F119>TIME(23,59,59),DATE(A119,B119,C119)+1,DATE(A119,B119,C119))' -> 2023-05-05 00:00:00 | A120: 2023 | B120: '5' | C120: 12 | D120: '=IF(F120>TIME(23,59,59),DATE(A120,B120,C120)+1,DATE(A120,B120,C120))' -> 2023-05-12 00:00:00 | A121: 2023 | B121: '5' | C121: 19 | D121: '=IF(F121>TIME(23,59,59),DATE(A121,B121,C121)+1,DATE(A121,B121,C121))' -> 2023-05-19 00:00:00

### `489956137c75|NUMBERS_STORED_AS_TEXT|Sheet1!J11`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/3_124-46_input.xlsx`
- location: `Sheet1!J11`  severity: Medium  confidence: Review
- evidence: Cell contains text value '25234' in a column that otherwise holds 10 numbers.
- cached value: '25234'; row labels: ["'11540\\n 30113'", "'12111\\n 32443'"]; column header: ''; used range: A1:J168
- neighbourhood: H11: 13424 | I11: 20352 | J11: '25234' | H13: '10311014\n 15053012'

### `e91e37899ef5|NUMBERS_STORED_AS_TEXT|DATA!B124`

- workbook: `all_data_912_v0.1/spreadsheet/58656/2_58656_input.xlsx`
- location: `DATA!B124`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '6' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '6'; row labels: []; column header: "'6'"; used range: A1:K132
- neighbourhood: A122: 2023 | B122: '5' | C122: 27 | D122: '=IF(F122>TIME(23,59,59),DATE(A122,B122,C122)+1,DATE(A122,B122,C122))' -> 2023-05-27 00:00:00 | A123: 2023 | B123: '6' | C123: 4 | D123: '=IF(F123>TIME(23,59,59),DATE(A123,B123,C123)+1,DATE(A123,B123,C123))' -> 2023-06-04 00:00:00 | A124: 2023 | B124: '6' | C124: 10 | D124: '=IF(F124>TIME(23,59,59),DATE(A124,B124,C124)+1,DATE(A124,B124,C124))' -> 2023-06-10 00:00:00 | A125: 2023 | B125: '6' | C125: 18 | D125: '=IF(F125>TIME(23,59,59),DATE(A125,B125,C125)+1,DATE(A125,B125,C125))' -> 2023-06-18 00:00:00 | A126: 2023 | B126: '6' | C126: 26 | D126: '=IF(F126>TIME(23,59,59),DATE(A126,B126,C126)+1,DATE(A126,B126,C126))' -> 2023-06-26 00:00:00

### `9e41b3b532ac|NUMBERS_STORED_AS_TEXT|KPI1!C188`

- workbook: `all_data_912_v0.1/spreadsheet/49455/3_49455_input.xlsx`
- location: `KPI 1!C188`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '223243' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '223243'; row labels: []; column header: "'224329'"; used range: A1:K208
- neighbourhood: C186: '215057' | D186: 'Apple' | C187: '224329' | C188: '223243' | C189: '223151' | C190: '223946'

### `4593cb55309d|NUMBERS_STORED_AS_TEXT|Sheet1!B19`

- workbook: `all_data_912_v0.1/spreadsheet/41937/3_41937_input.xlsx`
- location: `Sheet1!B19`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '045' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '045'; row labels: ["'T20'"]; column header: "'045'"; used range: A1:Q31
- neighbourhood: A17: 'T20' | B17: '045' | C17: 'BLANK' | D17: 'Y' | A18: 'T20' | B18: '045' | C18: 'BLANK' | D18: 'P' | A19: 'T20' | B19: '045' | C19: 'MATT' | D19: 'Y'

### `fbcb24cf156d|NUMBERS_STORED_AS_TEXT|RawData!D24`

- workbook: `all_data_912_v0.1/spreadsheet/6435/2_6435_input.xlsx`
- location: `Raw Data!D24`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '0009' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '0009'; row labels: []; column header: "'0009'"; used range: A1:P110
- neighbourhood: B22: 27 | C22: 2017-10-23 00:00:00 | D22: '0033' | E22: '0007' | F22: '=IF(D22="","",IF(E22="","",IF(ISODD(COUNTIFS(D$4:D22,D22,E$4:E22,E... -> 'Out' | B23: 19 | C23: 2017-10-05 00:00:00 | D23: '0009' | E23: '0026' | F23: '=IF(D23="","",IF(E23="","",IF(ISODD(COUNTIFS(D$4:D23,D23,E$4:E23,E... -> 'Out' | B24: 24 | C24: 2017-10-11 00:00:00 | D24: '0009' | E24: '0026' | F24: '=IF(D24="","",IF(E24="","",IF(ISODD(COUNTIFS(D$4:D24,D24,E$4:E24,E... -> 'In' | B25: 30 | C25: 2017-11-06 00:00:00 | D25: '0100' | E25: '0037' | F25: '=IF(D25="","",IF(E25="","",IF(ISODD(COUNTIFS(D$4:D25,D25,E$4:E25,E... -> 'Out' | B26: 2 | C26: 2017-02-03 00:00:00 | D26: '00216' | E26: '0142' | F26: '=IF(D26="","",IF(E26="","",IF(ISODD(COUNTIFS(D$4:D26,D26,E$4:E26,E... -> 'Out'

### `63df53e988c8|NUMBERS_STORED_AS_TEXT|Sheet2!G5`

- workbook: `all_data_912_v0.1/spreadsheet/124-46/1_124-46_input.xlsx`
- location: `Sheet2!G5`  severity: Medium  confidence: Review
- evidence: Cell contains text value '42533' in a column that otherwise holds 41 numbers.
- cached value: '42533'; row labels: ["'EE'", "'2G'"]; column header: ''; used range: A1:Z168
- neighbourhood: E3: 10433 | F3: 11114 | G3: 13104 | H3: 12010 | I3: 21513 | E4: 122243430 | F4: 122434202 | G4: 122434204 | H4: 122434203 | E5: 12505 | F5: 31332 | G5: '42533' | H5: 42533 | E6: 12324 | F6: 40421 | G6: 44212 | E7: '15142013' | F7: 22103013 | G7: 22310012 | H7: 22310014

### `fbcb24cf156d|NUMBERS_STORED_AS_TEXT|RawData!D5`

- workbook: `all_data_912_v0.1/spreadsheet/6435/2_6435_input.xlsx`
- location: `Raw Data!D5`  severity: High  confidence: Likely defect
- evidence: Cell contains text value '0009' and is referenced by a formula; numeric functions such as SUM ignore text.
- cached value: '0009'; row labels: []; column header: "'0009'"; used range: A1:P110
- neighbourhood: B3: 'S/No' | C3: 'Date ' | D3: 'Unit S/No' | E3: 'Unit Datecode' | F3: 'Unit In/Out' | B4: 28 | C4: 2017-10-30 00:00:00 | D4: '0009' | E4: '0007' | F4: '=IF(D4="","",IF(E4="","",IF(ISODD(COUNTIFS(D$4:D4,D4,E$4:E4,E4)),"... -> 'Out' | B5: 32 | C5: 2017-11-07 00:00:00 | D5: '0009' | E5: '9940' | F5: '=IF(D5="","",IF(E5="","",IF(ISODD(COUNTIFS(D$4:D5,D5,E$4:E5,E5)),"... -> 'Out' | B6: 18 | C6: 2017-09-28 00:00:00 | D6: '0010' | E6: '9940' | F6: '=IF(D6="","",IF(E6="","",IF(ISODD(COUNTIFS(D$4:D6,D6,E$4:E6,E6)),"... -> 'Out' | B7: 21 | C7: 2017-10-05 00:00:00 | D7: '0010' | E7: '9940' | F7: '=IF(D7="","",IF(E7="","",IF(ISODD(COUNTIFS(D$4:D7,D7,E$4:E7,E7)),"... -> 'In'

## RANGE_EXCLUSION

### `e95c516a52a3|RANGE_EXCLUSION|Sheet1!C9`

- workbook: `all_data_912_v0.1/spreadsheet/58687/2_58687_input.xlsx`
- location: `Sheet1!C9`  severity: Critical  confidence: Likely defect
- formula: `=COUNT($A$9:A9)`
- evidence: Sheet1!A9:A9 stops short of Sheet1!B9 (value 1), which sits right of the range, between it and the total.
- cached value: 1; row labels: []; column header: "'Count'"; used range: A1:V100
- range $A$9:A9: values ['1']; beyond: {'above': "A8: 'Apple index'", 'below': "A10: '=A9+1'", 'right': 'B9: 1'}
- neighbourhood: A8: 'Apple index' | B8: '=B4' -> 'Month No.' | C8: 'Count' | A9: 1 | B9: 1 | C9: '=COUNT($A$9:A9)' -> 1 | A10: '=A9+1' -> 2 | B10: 2 | C10: '=COUNT($A$9:A10)' -> 2 | A11: '=A10+1' -> 3 | B11: 2 | C11: '=COUNT($A$9:A11)' -> 3

### `c69ca54b316e|RANGE_EXCLUSION|Sheet1!C9`

- workbook: `all_data_912_v0.1/spreadsheet/58687/3_58687_input.xlsx`
- location: `Sheet1!C9`  severity: Critical  confidence: Likely defect
- formula: `=COUNT($A$9:A9)`
- evidence: Sheet1!A9:A9 stops short of Sheet1!B9 (value 2), which sits right of the range, between it and the total.
- cached value: 1; row labels: []; column header: "'Count'"; used range: A1:V100
- range $A$9:A9: values ['1']; beyond: {'above': "A8: 'Apple index'", 'below': "A10: '=A9+1'", 'right': 'B9: 2'}
- neighbourhood: A8: 'Apple index' | B8: '=B4' -> 'Month No.' | C8: 'Count' | A9: 1 | B9: 2 | C9: '=COUNT($A$9:A9)' -> 1 | A10: '=A9+1' -> 2 | B10: 3 | C10: '=COUNT($A$9:A10)' -> 2 | A11: '=A10+1' -> 3 | B11: 3 | C11: '=COUNT($A$9:A11)' -> 3

### `eac762a790d7|RANGE_EXCLUSION|Sheet1!C9`

- workbook: `all_data_912_v0.1/spreadsheet/58687/1_58687_input.xlsx`
- location: `Sheet1!C9`  severity: Critical  confidence: Likely defect
- formula: `=COUNT($A$9:A9)`
- evidence: Sheet1!A9:A9 stops short of Sheet1!B9 (value 1), which sits right of the range, between it and the total.
- cached value: 1; row labels: []; column header: "'Count'"; used range: A1:V100
- range $A$9:A9: values ['1']; beyond: {'above': "A8: 'Apple index'", 'below': "A10: '=A9+1'", 'right': 'B9: 1'}
- neighbourhood: A8: 'Apple index' | B8: '=B4' -> 'Month No.' | C8: 'Count' | A9: 1 | B9: 1 | C9: '=COUNT($A$9:A9)' -> 1 | A10: '=A9+1' -> 2 | B10: 2 | C10: '=COUNT($A$9:A10)' -> 2 | A11: '=A10+1' -> 3 | B11: 2 | C11: '=COUNT($A$9:A11)' -> 3

### `070be904b648|RANGE_EXCLUSION|Vat!F24`

- workbook: `all_data_912_v0.1/spreadsheet/49859/2_49859_input.xlsx`
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

## RANGE_INCLUDES_SUBTOTAL

### `e02ef7183006|RANGE_INCLUDES_SUBTOTAL|SCORES!Y6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_24784/2_CF_24784_input.xlsx`
- location: `SCORES!Y6`  severity: Medium  confidence: Review
- formula: `=SUM(U6:W6)`
- evidence: SCORES!U6:W6 includes column W, headed 'last weeks total', which holds constants rather than formulas.
- cached value: 150; row labels: ["'HOME'", "'AWAY'"]; column header: "'TOTAL OVERALL'"; used range: A1:Z29
- range U6:W6: values ['8', 'None', '142']; beyond: {'left': 'T6: None', 'right': 'X6: None'}
- neighbourhood: W4: 'LAST WEEKS TOTAL' | Y4: 'TOTAL OVERALL' | Z5: 'PLAYERS' | W6: 142 | Y6: '=SUM(U6:W6)' -> 150 | Z6: 'Dunalin' | W7: 134 | Y7: '=SUM(U7:W7)' -> 142 | Z7: 'Biggin' | W8: 132 | Y8: '=SUM(U8:W8)' -> 141 | Z8: 'Albert'

### `736a1dfb4636|RANGE_INCLUDES_SUBTOTAL|SCORES!Y6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_24784/3_CF_24784_input.xlsx`
- location: `SCORES!Y6`  severity: Medium  confidence: Review
- formula: `=SUM(U6:W6)`
- evidence: SCORES!U6:W6 includes column W, headed 'last weeks total', which holds constants rather than formulas.
- cached value: 150; row labels: ["'HOME'", "'AWAY'"]; column header: "'TOTAL OVERALL'"; used range: A1:Z29
- range U6:W6: values ['8', 'None', '142']; beyond: {'left': 'T6: None', 'right': 'X6: None'}
- neighbourhood: W4: 'LAST WEEKS TOTAL' | Y4: 'TOTAL OVERALL' | Z5: 'PLAYERS' | W6: 142 | Y6: '=SUM(U6:W6)' -> 150 | Z6: 'Dunalin' | W7: 134 | Y7: '=SUM(U7:W7)' -> 142 | Z7: 'Biggin' | W8: 132 | Y8: '=SUM(U8:W8)' -> 141 | Z8: 'Albert'

### `9ba8f22c1ad0|RANGE_INCLUDES_SUBTOTAL|SCORES!Y6`

- workbook: `all_data_912_v0.1/spreadsheet/CF_24784/1_CF_24784_input.xlsx`
- location: `SCORES!Y6`  severity: Medium  confidence: Review
- formula: `=SUM(U6:W6)`
- evidence: SCORES!U6:W6 includes column W, headed 'last weeks total', which holds constants rather than formulas.
- cached value: 150; row labels: ["'HOME'", "'AWAY'"]; column header: "'TOTAL OVERALL'"; used range: A1:Z29
- range U6:W6: values ['8', 'None', '142']; beyond: {'left': 'T6: None', 'right': 'X6: None'}
- neighbourhood: W4: 'LAST WEEKS TOTAL' | Y4: 'TOTAL OVERALL' | Z5: 'PLAYERS' | W6: 142 | Y6: '=SUM(U6:W6)' -> 150 | Z6: 'Dunalin' | W7: 134 | Y7: '=SUM(U7:W7)' -> 142 | Z7: 'Biggin' | W8: 132 | Y8: '=SUM(U8:W8)' -> 141 | Z8: 'Albert'

## RANGE_LENGTH_MISMATCH

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!H213`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!H213`  severity: High  confidence: Likely defect
- formula: `=SUM(G213:G213)`
- evidence: This aggregate spans 1 cell(s) while peer formulas in this row span 3.
- cached value: 335; row labels: []; column header: ''; used range: A1:CJ782
- range G213:G213: values ['335']; beyond: {'above': "G212: '=SUM(D212:F212)'", 'below': "G214: '=SUM(D214:F214)'", 'left': 'F213: 124', 'right': "H213: '=SUM(G213:G213)'"}
- neighbourhood: G211: '=SUM(D211:F211)' -> 0 | G212: '=SUM(D212:F212)' -> 0 | F213: 124 | G213: '=SUM(D213:F213)' -> 335 | H213: '=SUM(G213:G213)' -> 335 | I213: '=COUNT(D213:F213)' -> 3 | J213: '=IF(I213=0,0,(ROUNDDOWN(H213/I213,0)))' -> 111 | F214: 98 | G214: '=SUM(D214:F214)' -> 339 | H214: '=SUM(G213:G214)' -> 674 | I214: '=COUNT(D213:F214)' -> 6 | J214: '=IF(I214=0,0,(ROUNDDOWN(H214/I214,0)))' -> 112 | F215: 116 | G215: '=SUM(D215:F215)' -> 357 | H215: '=SUM(G213:G215)' -> 1031 | I215: '=COUNT(D213:F215)' -> 9 | J215: '=IF(I215=0,0,(ROUNDDOWN(H215/I215,0)))' -> 114

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!I89`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!I89`  severity: High  confidence: Likely defect
- formula: `=COUNT(D87:F89)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 6; row labels: []; column header: ''; used range: A1:CJ782
- range D87:F89: values ['103', '129', '110', 'None', 'None', 'None', '97', '96', '105']; beyond: {}
- neighbourhood: G87: '=SUM(D87:F87)' -> 342 | H87: '=SUM(G87:G87)' -> 342 | I87: '=COUNT(D87:F87)' -> 3 | J87: '=IF(I87=0,0,(ROUNDDOWN(H87/I87,0)))' -> 114 | K87: '=IFERROR(IF(I86>=12,IF($J86<=100,0+SUBSTITUTE(IF($D87>=125,","&$D8... -> None | G88: '=SUM(D88:F88)' -> 0 | H88: '=SUM(G87:G88)' -> 342 | I88: '=COUNT(D87:F88)' -> 3 | J88: '=IF(I88=0,0,(ROUNDDOWN(H88/I88,0)))' -> 114 | K88: '=IFERROR(IF(I87>=12,IF($J87<=100,0+SUBSTITUTE(IF($D88>=125,","&$D8... -> None | G89: '=SUM(D89:F89)' -> 298 | H89: '=SUM(G87:G89)' -> 640 | I89: '=COUNT(D87:F89)' -> 6 | J89: '=IF(I89=0,0,(ROUNDDOWN(H89/I89,0)))' -> 106 | K89: '=IFERROR(IF(I88>=12,IF($J88<=100,0+SUBSTITUTE(IF($D89>=125,","&$D8... -> None | G90: '=SUM(D90:F90)' -> 287 | H90: '=SUM(G87:G90)' -> 927 | I90: '=COUNT(D87:F90)' -> 9 | J90: '=IF(I90=0,0,(ROUNDDOWN(H90/I90,0)))' -> 103 | K90: '=IFERROR(IF(I89>=12,IF($J89<=100,0+SUBSTITUTE(IF($D90>=125,","&$D9... -> None | G91: '=SUM(D91:F91)' -> 319 | H91: '=SUM(G87:G91)' -> 1246 | I91: '=COUNT(D87:F91)' -> 12 | J91: '=IF(I91=0,0,(ROUNDDOWN(H91/I91,0)))' -> 103 | K91: '=IFERROR(IF(I90>=12,IF($J90<=100,0+SUBSTITUTE(IF($D91>=125,","&$D9... -> None

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I257`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I257`  severity: High  confidence: Likely defect
- formula: `=COUNT(D255:F257)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 9; row labels: []; column header: ''; used range: A1:CJ782
- range D255:F257: values ['126', '116', '114', '119', '94', '96', '83', '107', '126']; beyond: {}
- neighbourhood: G255: '=SUM(D255:F255)' -> 356 | H255: '=G255' -> 356 | I255: '=COUNT(D255:F255)' -> 3 | J255: '=IF(I255=0,0,(ROUNDDOWN(H255/I255,0)))' -> 118 | K255: '=IFERROR(IF(I254>=12,IF($J254<=100,0+SUBSTITUTE(IF($D255>=125,","&... -> None | G256: '=SUM(D256:F256)' -> 309 | H256: '=SUM(G255:G256)' -> 665 | I256: '=COUNT(D255:F256)' -> 6 | J256: '=IF(I256=0,0,(ROUNDDOWN(H256/I256,0)))' -> 110 | K256: '=IFERROR(IF(I255>=12,IF($J255<=100,0+SUBSTITUTE(IF($D256>=125,","&... -> None | G257: '=SUM(D257:F257)' -> 316 | H257: '=SUM(G255:G257)' -> 981 | I257: '=COUNT(D255:F257)' -> 9 | J257: '=IF(I257=0,0,(ROUNDDOWN(H257/I257,0)))' -> 109 | K257: '=IFERROR(IF(I256>=12,IF($J256<=100,0+SUBSTITUTE(IF($D257>=125,","&... -> None | G258: '=SUM(D258:F258)' -> 364 | H258: '=SUM(G255:G258)' -> 1345 | I258: '=COUNT(D255:F258)' -> 12 | J258: '=IF(I258=0,0,(ROUNDDOWN(H258/I258,0)))' -> 112 | K258: '=IFERROR(IF(I257>=12,IF($J257<=100,0+SUBSTITUTE(IF($D258>=125,","&... -> None | G259: '=SUM(D259:F259)' -> 428 | H259: '=SUM(G255:G259)' -> 1773 | I259: '=COUNT(D255:F259)' -> 15 | J259: '=IF(I259=0,0,(ROUNDDOWN(H259/I259,0)))' -> 118 | K259: '=IFERROR(IF(I258>=12,IF($J258<=100,0+SUBSTITUTE(IF($D259>=125,","&... -> None

### `74d967658eee|RANGE_LENGTH_MISMATCH|Sheet1!H234`

- workbook: `all_data_912_v0.1/spreadsheet/50051/1_50051_input.xlsx`
- location: `Sheet1!H234`  severity: High  confidence: Likely defect
- formula: `=SUM(G234:G234)`
- evidence: This aggregate spans 1 cell(s) while peer formulas in this row span 3.
- cached value: 487; row labels: []; column header: ''; used range: A1:CJ782
- range G234:G234: values ['487']; beyond: {'above': "G233: '=SUM(D233:F233)'", 'below': "G235: '=SUM(D235:F235)'", 'left': 'F234: 203', 'right': "H234: '=SUM(G234:G234)'"}
- neighbourhood: G232: '=SUM(D232:F232)' -> 0 | G233: '=SUM(D233:F233)' -> 0 | F234: 203 | G234: '=SUM(D234:F234)' -> 487 | H234: '=SUM(G234:G234)' -> 487 | I234: '=COUNT(D234:F234)' -> 3 | J234: '=IF(I234=0,0,(ROUNDDOWN(H234/I234,0)))' -> 162 | F235: 158 | G235: '=SUM(D235:F235)' -> 407 | H235: '=SUM(G234:G235)' -> 894 | I235: '=COUNT(D234:F235)' -> 6 | J235: '=IF(I235=0,0,(ROUNDDOWN(H235/I235,0)))' -> 149 | F236: 125 | G236: '=SUM(D236:F236)' -> 396 | H236: '=SUM(G234:G236)' -> 1290 | I236: '=COUNT(D234:F236)' -> 9 | J236: '=IF(I236=0,0,(ROUNDDOWN(H236/I236,0)))' -> 143

### `4ea284d68c01|RANGE_LENGTH_MISMATCH|Sheet1!I131`

- workbook: `all_data_912_v0.1/spreadsheet/50051/3_50051_input.xlsx`
- location: `Sheet1!I131`  severity: High  confidence: Likely defect
- formula: `=COUNT(D129:F131)`
- evidence: This aggregate spans 9 cell(s) while peer formulas in this row span 3.
- cached value: 6; row labels: []; column header: ''; used range: A1:CJ782
- range D129:F131: values ['105', '122', '94', '69', '81', '92', 'None', 'None', 'None']; beyond: {}
- neighbourhood: G129: '=SUM(D129:F129)' -> 321 | H129: '=SUM(G129:G129)' -> 321 | I129: '=COUNT(D129:F129)' -> 3 | J129: '=IF(I129=0,0,(ROUNDDOWN(H129/I129,0)))' -> 107 | K129: '=IFERROR(IF(I128>=12,IF($J128<=100,0+SUBSTITUTE(IF($D129>=125,","&... -> None | G130: '=SUM(D130:F130)' -> 242 | H130: '=SUM(G129:G130)' -> 563 | I130: '=COUNT(D129:F130)' -> 6 | J130: '=IF(I130=0,0,(ROUNDDOWN(H130/I130,0)))' -> 93 | K130: '=IFERROR(IF(I129>=12,IF($J129<=100,0+SUBSTITUTE(IF($D130>=125,","&... -> None | G131: '=SUM(D131:F131)' -> 0 | H131: '=SUM(G129:G131)' -> 563 | I131: '=COUNT(D129:F131)' -> 6 | J131: '=IF(I131=0,0,(ROUNDDOWN(H131/I131,0)))' -> 93 | K131: '=IFERROR(IF(I130>=12,IF($J130<=100,0+SUBSTITUTE(IF($D131>=125,","&... -> None | G132: '=SUM(D132:F132)' -> 364 | H132: '=SUM(G129:G132)' -> 927 | I132: '=COUNT(D129:F132)' -> 9 | J132: '=IF(I132=0,0,(ROUNDDOWN(H132/I132,0)))' -> 103 | K132: '=IFERROR(IF(I131>=12,IF($J131<=100,0+SUBSTITUTE(IF($D132>=125,","&... -> None | G133: '=SUM(D133:F133)' -> 339 | H133: '=SUM(G129:G133)' -> 1266 | I133: '=COUNT(D129:F133)' -> 12 | J133: '=IF(I133=0,0,(ROUNDDOWN(H133/I133,0)))' -> 105 | K133: '=IFERROR(IF(I132>=12,IF($J132<=100,0+SUBSTITUTE(IF($D133>=125,","&... -> None

### `1ee00a60f590|RANGE_LENGTH_MISMATCH|Sheet1!H45`

- workbook: `all_data_912_v0.1/spreadsheet/50051/2_50051_input.xlsx`
- location: `Sheet1!H45`  severity: High  confidence: Likely defect
- formula: `=SUM(G45:G45)`
- evidence: This aggregate spans 1 cell(s) while peer formulas in this row span 3.
- cached value: 360; row labels: []; column header: ''; used range: A1:CJ782
- range G45:G45: values ['360']; beyond: {'above': "G44: '=SUM(D44:F44)'", 'below': "G46: '=SUM(D46:F46)'", 'left': 'F45: 112', 'right': "H45: '=SUM(G45:G45)'"}
- neighbourhood: G43: '=SUM(D43:F43)' -> 0 | G44: '=SUM(D44:F44)' -> 0 | F45: 112 | G45: '=SUM(D45:F45)' -> 360 | H45: '=SUM(G45:G45)' -> 360 | I45: '=COUNT(D45:F45)' -> 3 | J45: '=IF(I45=0,0,(ROUNDDOWN(H45/I45,0)))' -> 120 | F46: 92 | G46: '=SUM(D46:F46)' -> 347 | H46: '=SUM(G45:G46)' -> 707 | I46: '=COUNT(D45:F46)' -> 6 | J46: '=IF(I46=0,0,(ROUNDDOWN(H46/I46,0)))' -> 117 | G47: '=SUM(D47:F47)' -> 0 | H47: '=SUM(G45:G47)' -> 707 | I47: '=COUNT(D45:F47)' -> 6 | J47: '=IF(I47=0,0,(ROUNDDOWN(H47/I47,0)))' -> 117

### `09478d797a42|RANGE_LENGTH_MISMATCH|BankBalance!AJ3`

- workbook: `all_data_912_v0.1/spreadsheet/55392/3_55392_input.xlsx`
- location: `Bank Balance!AJ3`  severity: High  confidence: Likely defect
- formula: `=SUM(C3:I3)`
- evidence: This aggregate spans 7 cell(s) while peer formulas in this row span 26.
- cached value: 2000; row labels: []; column header: "'Debit'"; used range: A1:AL3000
- range C3:I3: values ['2000', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'B3: "=+\'Journal Entries\'!I6"', 'right': 'J3: \'=IF(AND(\\\'Journal Entries\\\'!$H6="cre...'}
- neighbourhood: AJ1: 'Balance Brought Forward' | AL1: 2000000 | AH2: 'ETF' | AI2: 'Bonus' | AJ2: 'Debit' | AK2: 'Credit' | AL2: 'Acc. Balance' | AH3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AI3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AJ3: '=SUM(C3:I3)' -> 2000 | AK3: '=SUM(J3:AI3)' -> 0 | AL3: '=SUM(K3:AJ3)+AL1' -> 2002000 | AH4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AI4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AJ4: '=SUM(C4:I4)' -> 2000 | AK4: '=SUM(J4:AI4)' -> 35000 | AL4: '=IF(AND(AJ4="",AK4=""),"",AL3+AJ4-AK4)' -> 1969000 | AH5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AI5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AJ5: '=SUM(C5:I5)' -> 0 | AK5: '=SUM(J5:AI5)' -> 1500 | AL5: '=IF(AND(AJ5="",AK5=""),"",AL4+AJ5-AK5)' -> 1967500

### `c5ab9001d952|RANGE_LENGTH_MISMATCH|BankBalance!AJ3`

- workbook: `all_data_912_v0.1/spreadsheet/55392/1_55392_input.xlsx`
- location: `Bank Balance!AJ3`  severity: High  confidence: Likely defect
- formula: `=SUM(C3:I3)`
- evidence: This aggregate spans 7 cell(s) while peer formulas in this row span 26.
- cached value: 2000; row labels: []; column header: "'Debit'"; used range: A1:AL3000
- range C3:I3: values ['2000', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'B3: "=+\'Journal Entries\'!I6"', 'right': 'J3: \'=IF(AND(\\\'Journal Entries\\\'!$H6="cre...'}
- neighbourhood: AJ1: 'Balance Brought Forward' | AL1: 2000000 | AH2: 'ETF' | AI2: 'Bonus' | AJ2: 'Debit' | AK2: 'Credit' | AL2: 'Acc. Balance' | AH3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AI3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AJ3: '=SUM(C3:I3)' -> 2000 | AK3: '=SUM(J3:AI3)' -> 0 | AL3: '=SUM(K3:AJ3)+AL1' -> 2002000 | AH4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AI4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AJ4: '=SUM(C4:I4)' -> 0 | AK4: '=SUM(J4:AI4)' -> 35000 | AL4: '=IF(AND(AJ4="",AK4=""),"",AL3+AJ4-AK4)' -> 1967000 | AH5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AI5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AJ5: '=SUM(C5:I5)' -> 0 | AK5: '=SUM(J5:AI5)' -> 1500 | AL5: '=IF(AND(AJ5="",AK5=""),"",AL4+AJ5-AK5)' -> 1965500

### `5a98e72c8ee6|RANGE_LENGTH_MISMATCH|BankBalance!AJ3`

- workbook: `all_data_912_v0.1/spreadsheet/55392/2_55392_input.xlsx`
- location: `Bank Balance!AJ3`  severity: High  confidence: Likely defect
- formula: `=SUM(C3:I3)`
- evidence: This aggregate spans 7 cell(s) while peer formulas in this row span 26.
- cached value: 2000; row labels: []; column header: "'Debit'"; used range: A1:AL3000
- range C3:I3: values ['2000', 'None', 'None', 'None', 'None', 'None', 'None']; beyond: {'left': 'B3: "=+\'Journal Entries\'!I6"', 'right': 'J3: \'=IF(AND(\\\'Journal Entries\\\'!$H6="cre...'}
- neighbourhood: AJ1: 'Balance Brought Forward' | AL1: 2000000 | AH2: 'ETF' | AI2: 'Bonus' | AJ2: 'Debit' | AK2: 'Credit' | AL2: 'Acc. Balance' | AH3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AI3: '=IF(AND(\'Journal Entries\'!$H6="credit",\'Journal Entries\'!$E6=\... -> None | AJ3: '=SUM(C3:I3)' -> 2000 | AK3: '=SUM(J3:AI3)' -> 0 | AL3: '=SUM(K3:AJ3)+AL1' -> 2002000 | AH4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AI4: '=IF(AND(\'Journal Entries\'!$H7="credit",\'Journal Entries\'!$E7=\... -> None | AJ4: '=SUM(C4:I4)' -> 0 | AK4: '=SUM(J4:AI4)' -> 35000 | AL4: '=IF(AND(AJ4="",AK4=""),"",AL3+AJ4-AK4)' -> 1967000 | AH5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AI5: '=IF(AND(\'Journal Entries\'!$H8="credit",\'Journal Entries\'!$E8=\... -> None | AJ5: '=SUM(C5:I5)' -> 0 | AK5: '=SUM(J5:AI5)' -> 1500 | AL5: '=IF(AND(AJ5="",AK5=""),"",AL4+AJ5-AK5)' -> 1965500

## VOLATILE_FUNCTION

### `cf1c0902ee66|VOLATILE_FUNCTION|GDPRTrg!S30`

- workbook: `all_data_912_v0.1/spreadsheet/237-21/2_237-21_input.xlsx`
- location: `GDPR Trg!S30`  severity: Medium  confidence: Review
- formula: `=IF(A30="","",IF(U30="LTA","LTA",IF(AND(G30="",J30<>"",J30<TODAY()),"Overdue",IF(OR(F30="not_started",F30="Not Attempted"),"Not Attempted",IF(OR(F30="incomplete",F30="in_progress"),"incomplete",IF(COUNTIFS(C$6:C30,C30,F$6:F30,"Complete",E$6:E30,"GDPR*")>1,"Upgraded","Complete"))))))`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'GDPR UK: Advanced'", "'in_progress'"]; column header: ''; used range: A1:AL65
- range C$6:C30: values ['38001962', '38005850', '38033440', '38036637', '38001317', '38035136', '38033561', '38038578', '38038518', '38031798', '38009771', '38012325']; beyond: {'above': "C5: 'EmployeeNumber'", 'below': 'C31: 38001221'}
- neighbourhood: S28: '=IF(A28="","",IF(U28="LTA","LTA",IF(AND(G28="",J28<>"",J28<TODAY()... -> None | T28: 10006 | S29: '=IF(A29="","",IF(U29="LTA","LTA",IF(AND(G29="",J29<>"",J29<TODAY()... -> None | T29: 10007 | S30: '=IF(A30="","",IF(U30="LTA","LTA",IF(AND(G30="",J30<>"",J30<TODAY()... -> None | T30: 10008 | S31: 'Complete' | T31: 100018 | S32: 'Complete' | T32: 100029

### `2c824f83a09c|VOLATILE_FUNCTION|Open!P10`

- workbook: `all_data_912_v0.1/spreadsheet/105-24/3_105-24_input.xlsx`
- location: `Open!P10`  severity: Medium  confidence: Review
- formula: `=INT(TODAY()-D10+(1))`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'Perform peer review'", "'spk12633'"]; column header: ''; used range: A1:S23
- neighbourhood: N8: 2023-05-03 00:00:00 | O8: 21:45:19 | P8: '=INT(TODAY()-D8+(1))' -> None | N9: 2023-05-03 00:00:00 | O9: 10:48:54 | P9: '=INT(TODAY()-D9+(1))' -> None | N10: 2023-05-04 00:00:00 | O10: 07:53:14 | P10: '=INT(TODAY()-D10+(1))' -> None | N11: 2023-05-04 00:00:00 | O11: 14:10:38 | P11: '=INT(TODAY()-D11+(1))' -> None | N12: 2023-05-03 00:00:00 | O12: 21:01:07 | P12: '=INT(TODAY()-D12+(1))' -> None

### `b7e4ec773e1c|VOLATILE_FUNCTION|Sheet1!O13`

- workbook: `all_data_912_v0.1/spreadsheet/44296/1_44296_input.xlsx`
- location: `Sheet1!O13`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.393257849227395; row labels: ["'GA'"]; column header: ''; used range: A1:R53
- neighbourhood: M11: '=RAND()' -> 0.884582377880271 | N11: '=RAND()' -> 0.572823756875486 | O11: '=RAND()' -> 0.308446032224807 | P11: '=RAND()' -> 0.54690431686283 | Q11: '=RAND()' -> 0.260404067206347 | M12: '=RAND()' -> 0.246210741232532 | N12: '=RAND()' -> 0.52403331584194 | O12: '=RAND()' -> 0.812677316208991 | P12: '=RAND()' -> 0.0763955822157374 | Q12: '=RAND()' -> 0.0366485572388655 | M13: '=RAND()' -> 0.119008513876091 | N13: '=RAND()' -> 0.566405440305978 | O13: '=RAND()' -> 0.393257849227395 | P13: '=RAND()' -> 0.0823092635983078 | Q13: '=RAND()' -> 0.873603894727371 | M14: '=RAND()' -> 0.465134644233499 | N14: '=RAND()' -> 0.161418113998701 | O14: '=RAND()' -> 0.322512082128967 | P14: '=RAND()' -> 0.536987193295193 | Q14: '=RAND()' -> 0.958557590981718 | M15: '=RAND()' -> 0.177476716203947 | N15: '=RAND()' -> 0.275544070397883 | O15: '=RAND()' -> 0.41468557810835 | P15: '=RAND()' -> 0.989666724112911 | Q15: '=RAND()' -> 0.661757026977794

### `5e54f3a7fa8a|VOLATILE_FUNCTION|Sheet1!C189`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/3_189-9_input.xlsx`
- location: `Sheet1!C189`  severity: Medium  confidence: Review
- formula: `=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'LB0RT9'"]; column header: ''; used range: A1:E613
- neighbourhood: A187: 'LB0P0B' | B187: 2015-01-31 00:00:00 | C187: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D187: '=INT(C187)-INT(B187)' -> None | A188: 'LB0RR9' | B188: 2014-10-31 00:00:00 | C188: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D188: '=INT(C188)-INT(B188)' -> None | A189: 'LB0RT9' | B189: 2014-10-31 00:00:00 | C189: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D189: '=INT(C189)-INT(B189)' -> None | A190: 'LB0SP9' | B190: 2013-04-01 00:00:00 | C190: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D190: '=INT(C190)-INT(B190)' -> None | A191: 'LB0TN9' | B191: 2014-10-31 00:00:00 | C191: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D191: '=INT(C191)-INT(B191)' -> None

### `cf1c0902ee66|VOLATILE_FUNCTION|GDPRTrg!S8`

- workbook: `all_data_912_v0.1/spreadsheet/237-21/2_237-21_input.xlsx`
- location: `GDPR Trg!S8`  severity: Medium  confidence: Review
- formula: `=IF(A8="","",IF(U8="LTA","LTA",IF(AND(G8="",J8<>"",J8<TODAY()),"Overdue",IF(OR(F8="not_started",F8="Not Attempted"),"Not Attempted",IF(OR(F8="incomplete",F8="in_progress"),"incomplete",IF(COUNTIFS(C$6:C8,C8,F$6:F8,"Complete",E$6:E8,"GDPR*")>1,"Upgraded","Complete"))))))`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'Data Protection V9'", "'Not Attempted'"]; column header: ''; used range: A1:AL65
- range C$6:C8: values ['38001962', '38005850', '38033440']; beyond: {'above': "C5: 'EmployeeNumber'", 'below': 'C9: 38036637'}
- neighbourhood: S6: '=IF(A6="","",IF(U6="LTA","LTA",IF(AND(G6="",J6<>"",J6<TODAY()),"Ov... -> None | T6: 1001 | S7: '=IF(A7="","",IF(U7="LTA","LTA",IF(AND(G7="",J7<>"",J7<TODAY()),"Ov... -> None | T7: 1002 | S8: '=IF(A8="","",IF(U8="LTA","LTA",IF(AND(G8="",J8<>"",J8<TODAY()),"Ov... -> None | T8: 1003 | S9: '=IF(A9="","",IF(U9="LTA","LTA",IF(AND(G9="",J9<>"",J9<TODAY()),"Ov... -> None | T9: 1004 | S10: '=IF(A10="","",IF(U10="LTA","LTA",IF(AND(G10="",J10<>"",J10<TODAY()... -> None | T10: 1005

### `e7625a973c75|VOLATILE_FUNCTION|Sheet1!C24`

- workbook: `all_data_912_v0.1/spreadsheet/49196/2_49196_input.xlsx`
- location: `Sheet1!C24`  severity: Medium  confidence: Review
- formula: `=LEFT(K24,2)&"/"&MID(K24,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K24,FIND(" ",K24,1),6)`
- evidence: Function(s) found: TODAY.
- cached value: '14/12/24 06:00'; row labels: []; column header: ''; used range: A1:L47
- neighbourhood: C22: '=LEFT(K22,2)&"/"&MID(K22,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K22,FIND(... -> '10/12/24 18:00' | D22: '=TEXT(C22,"mmm")' -> 'Dec' | E22: '=WEEKNUM(C22,21)' -> '#NUM!' | C23: '=LEFT(K23,2)&"/"&MID(K23,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K23,FIND(... -> '11/12/24 18:00' | D23: '=TEXT(C23,"mmm")' -> 'Dec' | E23: '=WEEKNUM(C23,21)' -> '#NUM!' | C24: '=LEFT(K24,2)&"/"&MID(K24,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K24,FIND(... -> '14/12/24 06:00' | D24: '=TEXT(C24,"mmm")' -> 'Dec' | E24: '=WEEKNUM(C24,21)' -> '#NUM!' | C25: '=LEFT(K25,2)&"/"&MID(K25,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K25,FIND(... -> '15/12/24 06:00' | D25: '=TEXT(C25,"mmm")' -> 'Dec' | E25: '=WEEKNUM(C25,21)' -> '#NUM!' | C26: '=LEFT(K26,2)&"/"&MID(K26,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K26,FIND(... -> '16/12/24 04:47' | D26: '=TEXT(C26,"mmm")' -> 'Dec' | E26: '=WEEKNUM(C26,21)' -> '#NUM!'

### `9cb56a79b057|VOLATILE_FUNCTION|Sheet1!C166`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/2_189-9_input.xlsx`
- location: `Sheet1!C166`  severity: Medium  confidence: Review
- formula: `=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'LB08KB'"]; column header: ''; used range: A1:E613
- neighbourhood: A164: 'LB08HB' | B164: 2015-04-30 00:00:00 | C164: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D164: '=INT(C164)-INT(B164)' -> None | A165: 'LB08IB' | B165: 2015-04-30 00:00:00 | C165: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D165: '=INT(C165)-INT(B165)' -> None | A166: 'LB08KB' | B166: 2015-04-30 00:00:00 | C166: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D166: '=INT(C166)-INT(B166)' -> None | A167: 'LB08MB' | B167: 2015-04-30 00:00:00 | C167: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D167: '=INT(C167)-INT(B167)' -> None | A168: 'LB08NB' | B168: 2015-04-30 00:00:00 | C168: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D168: '=INT(C168)-INT(B168)' -> None

### `b7e4ec773e1c|VOLATILE_FUNCTION|Sheet1!O51`

- workbook: `all_data_912_v0.1/spreadsheet/44296/1_44296_input.xlsx`
- location: `Sheet1!O51`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.842323129647594; row labels: ["'WI'"]; column header: ''; used range: A1:R53
- neighbourhood: M49: '=RAND()' -> 0.891403952698722 | N49: '=RAND()' -> 0.73221234545805 | O49: '=RAND()' -> 0.752891628748054 | P49: '=RAND()' -> 0.15149900655289 | Q49: '=RAND()' -> 0.944406949287182 | M50: '=RAND()' -> 0.40284292334738 | N50: '=RAND()' -> 0.12480684511032 | O50: '=RAND()' -> 0.976928409923557 | P50: '=RAND()' -> 0.987904269389694 | Q50: '=RAND()' -> 0.197861688601977 | M51: '=RAND()' -> 0.287525706837115 | N51: '=RAND()' -> 0.642351999178677 | O51: '=RAND()' -> 0.842323129647594 | P51: '=RAND()' -> 0.210334046725237 | Q51: '=RAND()' -> 0.951786823056012 | M52: '=RAND()' -> 0.58857329449086 | N52: '=RAND()' -> 0.727941107226458 | O52: '=RAND()' -> 0.282662927134594 | P52: '=RAND()' -> 0.655981818991116 | Q52: '=RAND()' -> 0.358069275654014 | M53: '=RAND()' -> 0.1144127492441 | N53: '=RAND()' -> 0.227812000129721 | O53: '=RAND()' -> 0.500965056083427 | P53: '=RAND()' -> 0.33100755008728 | Q53: '=RAND()' -> 0.438667117443841

### `bcd47f3628af|VOLATILE_FUNCTION|Sheet1!O39`

- workbook: `all_data_912_v0.1/spreadsheet/44296/2_44296_input.xlsx`
- location: `Sheet1!O39`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.0448410463152524; row labels: ["'OK'"]; column header: ''; used range: A1:R53
- neighbourhood: M37: '=RAND()' -> 0.861457695705347 | N37: '=RAND()' -> 0.740398425962286 | O37: '=RAND()' -> 0.358504641544265 | P37: '=RAND()' -> 0.192237003180719 | Q37: '=RAND()' -> 0.895041037292871 | M38: '=RAND()' -> 0.162430208037748 | N38: '=RAND()' -> 0.562348930997158 | O38: '=RAND()' -> 0.365743372865361 | P38: '=RAND()' -> 0.972675287544537 | Q38: '=RAND()' -> 0.0403170101757047 | M39: '=RAND()' -> 0.0742039874728939 | N39: '=RAND()' -> 0.561865038749315 | O39: '=RAND()' -> 0.0448410463152524 | P39: '=RAND()' -> 0.122086896673461 | Q39: '=RAND()' -> 0.808313131755632 | M40: '=RAND()' -> 0.654202293477929 | N40: '=RAND()' -> 0.671870928505032 | O40: '=RAND()' -> 0.0874402030088335 | P40: '=RAND()' -> 0.770406540472039 | Q40: '=RAND()' -> 0.25876206780834 | M41: '=RAND()' -> 0.248761704374924 | N41: '=RAND()' -> 0.154331264759476 | O41: '=RAND()' -> 0.619950786433173 | P41: '=RAND()' -> 0.651830168171836 | Q41: '=RAND()' -> 0.209626262897491

### `b8b201e9eb11|VOLATILE_FUNCTION|Sheet1!D22`

- workbook: `all_data_912_v0.1/spreadsheet/57376/1_57376_input.xlsx`
- location: `Sheet1!D22`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(50,750)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 205; row labels: []; column header: ''; used range: A1:G30002
- neighbourhood: C20: 1018 | D20: '=RANDBETWEEN(50,750)' -> 602 | E20: 2021-01-03 00:00:00 | F20: '=RANDBETWEEN(E20+14,E20+RAND()*100)' -> 2021-01-22 00:00:00 | C21: 1019 | D21: '=RANDBETWEEN(50,750)' -> 648 | E21: 2021-01-03 00:00:00 | F21: '=RANDBETWEEN(E21+14,E21+RAND()*100)' -> '#NUM!' | C22: 1020 | D22: '=RANDBETWEEN(50,750)' -> 205 | E22: 2021-01-03 00:00:00 | F22: '=RANDBETWEEN(E22+14,E22+RAND()*100)' -> '#NUM!' | C23: 1021 | D23: '=RANDBETWEEN(50,750)' -> 617 | E23: 2021-01-03 00:00:00 | F23: '=RANDBETWEEN(E23+14,E23+RAND()*100)' -> 2021-02-17 00:00:00 | C24: 1022 | D24: '=RANDBETWEEN(50,750)' -> 635 | E24: 2021-01-03 00:00:00 | F24: '=RANDBETWEEN(E24+14,E24+RAND()*100)' -> 2021-02-03 00:00:00

### `9cb56a79b057|VOLATILE_FUNCTION|Sheet1!C248`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/2_189-9_input.xlsx`
- location: `Sheet1!C248`  severity: Medium  confidence: Review
- formula: `=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'LB04K9'"]; column header: ''; used range: A1:E613
- neighbourhood: A246: 'LB04G9' | B246: 2014-10-31 00:00:00 | C246: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D246: '=INT(C246)-INT(B246)' -> None | A247: 'LB04H9' | B247: 2014-10-31 00:00:00 | C247: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D247: '=INT(C247)-INT(B247)' -> None | A248: 'LB04K9' | B248: 2014-10-31 00:00:00 | C248: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D248: '=INT(C248)-INT(B248)' -> None | A249: 'LB04L9' | B249: 2014-10-31 00:00:00 | C249: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D249: '=INT(C249)-INT(B249)' -> None | A250: 'LB04V7' | B250: 2014-01-01 00:00:00 | C250: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D250: '=INT(C250)-INT(B250)' -> None

### `bcd47f3628af|VOLATILE_FUNCTION|Sheet1!M19`

- workbook: `all_data_912_v0.1/spreadsheet/44296/2_44296_input.xlsx`
- location: `Sheet1!M19`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.683224971022115; row labels: ["'KS'"]; column header: ''; used range: A1:R53
- neighbourhood: L17: '=RAND()' -> 0.217525570331599 | M17: '=RAND()' -> 0.962043940400228 | N17: '=RAND()' -> 0.632614630660983 | O17: '=RAND()' -> 0.415611412656371 | L18: '=RAND()' -> 0.230713133225426 | M18: '=RAND()' -> 0.287883658758687 | N18: '=RAND()' -> 0.142319418098398 | O18: '=RAND()' -> 0.0452115659964478 | L19: '=RAND()' -> 0.466598080496788 | M19: '=RAND()' -> 0.683224971022115 | N19: '=RAND()' -> 0.711573260101486 | O19: '=RAND()' -> 0.470311440947991 | L20: '=RAND()' -> 0.29235600521891 | M20: '=RAND()' -> 0.447967314004938 | N20: '=RAND()' -> 0.462178800589485 | O20: '=RAND()' -> 0.879628839364224 | L21: '=RAND()' -> 0.396731729277261 | M21: '=RAND()' -> 0.750698934043281 | N21: '=RAND()' -> 0.688903058736939 | O21: '=RAND()' -> 0.160489861099716

### `02333185f919|VOLATILE_FUNCTION|Sheet1!H7`

- workbook: `all_data_912_v0.1/spreadsheet/56419/1_56419_input.xlsx`
- location: `Sheet1!H7`  severity: Medium  confidence: Review
- formula: `=INDIRECT("A"&G7)`
- evidence: Function(s) found: INDIRECT.
- cached value: 'I'; row labels: ["'F'"]; column header: ''; used range: A1:H100
- neighbourhood: G5: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> 6 | H5: '=INDIRECT("A"&G5)' -> 'E' | G6: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> 9 | H6: '=INDIRECT("A"&G6)' -> 'H' | G7: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> 10 | H7: '=INDIRECT("A"&G7)' -> 'I' | G8: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> 13 | H8: '=INDIRECT("A"&G8)' -> 'L' | G9: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> 15 | H9: '=INDIRECT("A"&G9)' -> 'N'

### `5635b3c618d2|VOLATILE_FUNCTION|example!C11`

- workbook: `all_data_912_v0.1/spreadsheet/56996/3_56996_input.xlsx`
- location: `example!C11`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(1,5)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 1; row labels: ["'Salt Biscuit'"]; column header: ''; used range: A1:O18
- neighbourhood: B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 3 | D9: '=RANDBETWEEN(5,10)' -> 5 | E9: '=RANDBETWEEN(10,15)' -> 10 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 5 | D10: '=RANDBETWEEN(5,10)' -> 7 | E10: '=RANDBETWEEN(10,15)' -> 11 | B11: 'Salt Biscuit' | C11: '=RANDBETWEEN(1,5)' -> 1 | D11: '=RANDBETWEEN(5,10)' -> 10 | E11: '=RANDBETWEEN(10,15)' -> 14 | B12: 'Vinegar' | C12: '=RANDBETWEEN(1,5)' -> 3 | D12: '=RANDBETWEEN(5,10)' -> 6 | E12: '=RANDBETWEEN(10,15)' -> 13

### `c4229dd05b85|VOLATILE_FUNCTION|example!C9`

- workbook: `all_data_912_v0.1/spreadsheet/56996/2_56996_input.xlsx`
- location: `example!C9`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(1,5)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 1; row labels: ["'Milk'"]; column header: ''; used range: A1:O18
- neighbourhood: C7: 'IZHAR' | D7: 'INAM' | E7: 'AMIN' | B8: 'Egg' | C8: '=RANDBETWEEN(1,5)' -> 4 | D8: '=RANDBETWEEN(5,10)' -> 6 | E8: '=RANDBETWEEN(10,15)' -> 13 | B9: 'Milk' | C9: '=RANDBETWEEN(1,5)' -> 1 | D9: '=RANDBETWEEN(5,10)' -> 9 | E9: '=RANDBETWEEN(10,15)' -> 14 | B10: 'Masala' | C10: '=RANDBETWEEN(1,5)' -> 3 | D10: '=RANDBETWEEN(5,10)' -> 9 | E10: '=RANDBETWEEN(10,15)' -> 15 | B11: 'Salt Biscuit' | C11: '=RANDBETWEEN(1,5)' -> 2 | D11: '=RANDBETWEEN(5,10)' -> 5 | E11: '=RANDBETWEEN(10,15)' -> 13

### `fa1153650228|VOLATILE_FUNCTION|Sheet1!D49`

- workbook: `all_data_912_v0.1/spreadsheet/57376/2_57376_input.xlsx`
- location: `Sheet1!D49`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(50,750)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 525; row labels: []; column header: ''; used range: A1:G30002
- neighbourhood: C47: 1045 | D47: '=RANDBETWEEN(50,750)' -> 310 | E47: 2021-01-05 00:00:00 | F47: '=RANDBETWEEN(E47+14,E47+RAND()*100)' -> 2021-02-10 00:00:00 | C48: 1046 | D48: '=RANDBETWEEN(50,750)' -> 61 | E48: 2021-01-05 00:00:00 | F48: '=RANDBETWEEN(E48+14,E48+RAND()*100)' -> 2021-01-21 00:00:00 | C49: 1047 | D49: '=RANDBETWEEN(50,750)' -> 525 | E49: 2021-01-06 00:00:00 | F49: '=RANDBETWEEN(E49+14,E49+RAND()*100)' -> '#NUM!' | C50: 1048 | D50: '=RANDBETWEEN(50,750)' -> 141 | E50: 2021-01-06 00:00:00 | F50: '=RANDBETWEEN(E50+14,E50+RAND()*100)' -> 2021-02-01 00:00:00 | C51: 1049 | D51: '=RANDBETWEEN(50,750)' -> 485 | E51: 2021-01-07 00:00:00 | F51: '=RANDBETWEEN(E51+14,E51+RAND()*100)' -> '#NUM!'

### `5e54f3a7fa8a|VOLATILE_FUNCTION|Sheet1!C236`

- workbook: `all_data_912_v0.1/spreadsheet/189-9/3_189-9_input.xlsx`
- location: `Sheet1!C236`  severity: Medium  confidence: Review
- formula: `=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'LB03R9'"]; column header: ''; used range: A1:E613
- neighbourhood: A234: 'LB03P9' | B234: 2014-10-31 00:00:00 | C234: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D234: '=INT(C234)-INT(B234)' -> None | A235: 'LB03Q9' | B235: 2014-10-31 00:00:00 | C235: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D235: '=INT(C235)-INT(B235)' -> None | A236: 'LB03R9' | B236: 2014-10-31 00:00:00 | C236: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D236: '=INT(C236)-INT(B236)' -> None | A237: 'LB03V7' | B237: 2014-01-01 00:00:00 | C237: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D237: '=INT(C237)-INT(B237)' -> None | A238: 'LB03X9' | B238: 2014-10-31 00:00:00 | C238: '=TEXT(TODAY()-1,"dd-mm-yyyy")&"11:59:00 PM"' -> None | D238: '=INT(C238)-INT(B238)' -> None

### `0b213825e4f4|VOLATILE_FUNCTION|Result!J31`

- workbook: `all_data_912_v0.1/spreadsheet/118-10/2_118-10_input.xlsx`
- location: `Result!J31`  severity: Medium  confidence: Review
- formula: `=IF(I31>0,TODAY()-(A31),"")`
- evidence: Function(s) found: TODAY.
- cached value: None; row labels: ["'Alaksa'"]; column header: ''; used range: A1:J46
- neighbourhood: H29: 'Alaksa' | J29: '=IF(I29>0,TODAY()-(A29),"")' -> None | H30: 'Alaksa' | J30: '=IF(I30>0,TODAY()-(A30),"")' -> None | H31: 'Alaksa' | J31: '=IF(I31>0,TODAY()-(A31),"")' -> None | H32: 'Alaksa' | J32: '=IF(I32>0,TODAY()-(A32),"")' -> None

### `6a12a787eb96|VOLATILE_FUNCTION|Sheet1!L42`

- workbook: `all_data_912_v0.1/spreadsheet/44296/3_44296_input.xlsx`
- location: `Sheet1!L42`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.841783976094931; row labels: ["'RI'"]; column header: ''; used range: A1:R53
- neighbourhood: L40: '=RAND()' -> 0.0518804045996761 | M40: '=RAND()' -> 0.507606277485631 | N40: '=RAND()' -> 0.262069669374194 | L41: '=RAND()' -> 0.626540663849331 | M41: '=RAND()' -> 0.179902034598991 | N41: '=RAND()' -> 0.451449977485588 | L42: '=RAND()' -> 0.841783976094931 | M42: '=RAND()' -> 0.70358260197481 | N42: '=RAND()' -> 0.572610785093715 | L43: '=RAND()' -> 0.0986922885954646 | M43: '=RAND()' -> 0.48026677406048 | N43: '=RAND()' -> 0.503544913654336 | L44: '=RAND()' -> 0.830302449462296 | M44: '=RAND()' -> 0.864900002605893 | N44: '=RAND()' -> 0.464454348622037

### `5124d0617e42|VOLATILE_FUNCTION|example!H9`

- workbook: `all_data_912_v0.1/spreadsheet/56996/1_56996_input.xlsx`
- location: `example!H9`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(25,30)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 26; row labels: ["'Milk'"]; column header: ''; used range: A1:O18
- neighbourhood: F7: 'NOOR' | G7: 'SHAMS' | H7: 'AHSAN' | J7: 'Product' | F8: '=RANDBETWEEN(15,20)' -> 15 | G8: '=RANDBETWEEN(20,25)' -> 25 | H8: '=RANDBETWEEN(25,30)' -> 26 | J8: 'Egg' | F9: '=RANDBETWEEN(15,20)' -> 16 | G9: '=RANDBETWEEN(20,25)' -> 21 | H9: '=RANDBETWEEN(25,30)' -> 26 | J9: 'Milk' | F10: '=RANDBETWEEN(15,20)' -> 15 | G10: '=RANDBETWEEN(20,25)' -> 21 | H10: '=RANDBETWEEN(25,30)' -> 28 | J10: 'Masala' | F11: '=RANDBETWEEN(15,20)' -> 17 | G11: '=RANDBETWEEN(20,25)' -> 22 | H11: '=RANDBETWEEN(25,30)' -> 26 | J11: 'Salt Biscuit'

### `02333185f919|VOLATILE_FUNCTION|Sheet1!H25`

- workbook: `all_data_912_v0.1/spreadsheet/56419/1_56419_input.xlsx`
- location: `Sheet1!H25`  severity: Medium  confidence: Review
- formula: `=INDIRECT("A"&G25)`
- evidence: Function(s) found: INDIRECT.
- cached value: '#N/A'; row labels: ["'X'"]; column header: ''; used range: A1:H100
- neighbourhood: G23: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H23: '=INDIRECT("A"&G23)' -> '#N/A' | G24: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H24: '=INDIRECT("A"&G24)' -> '#N/A' | G25: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H25: '=INDIRECT("A"&G25)' -> '#N/A' | G26: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H26: '=INDIRECT("A"&G26)' -> '#N/A' | G27: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H27: '=INDIRECT("A"&G27)' -> '#N/A'

### `b8b201e9eb11|VOLATILE_FUNCTION|Sheet1!D14`

- workbook: `all_data_912_v0.1/spreadsheet/57376/1_57376_input.xlsx`
- location: `Sheet1!D14`  severity: Medium  confidence: Review
- formula: `=RANDBETWEEN(50,750)`
- evidence: Function(s) found: RANDBETWEEN.
- cached value: 291; row labels: []; column header: ''; used range: A1:G30002
- neighbourhood: C12: 1010 | D12: '=RANDBETWEEN(50,750)' -> 574 | E12: 2021-01-02 00:00:00 | F12: '=RANDBETWEEN(E12+14,E12+RAND()*100)' -> 2021-01-16 00:00:00 | C13: 1011 | D13: '=RANDBETWEEN(50,750)' -> 152 | E13: 2021-01-02 00:00:00 | F13: '=RANDBETWEEN(E13+14,E13+RAND()*100)' -> 2021-01-19 00:00:00 | C14: 1012 | D14: '=RANDBETWEEN(50,750)' -> 291 | E14: 2021-01-02 00:00:00 | F14: '=RANDBETWEEN(E14+14,E14+RAND()*100)' -> 2021-01-23 00:00:00 | C15: 1013 | D15: '=RANDBETWEEN(50,750)' -> 397 | E15: 2021-01-03 00:00:00 | F15: '=RANDBETWEEN(E15+14,E15+RAND()*100)' -> 2021-01-31 00:00:00 | C16: 1014 | D16: '=RANDBETWEEN(50,750)' -> 287 | E16: 2021-01-03 00:00:00 | F16: '=RANDBETWEEN(E16+14,E16+RAND()*100)' -> 2021-02-16 00:00:00

### `6a12a787eb96|VOLATILE_FUNCTION|Sheet1!M15`

- workbook: `all_data_912_v0.1/spreadsheet/44296/3_44296_input.xlsx`
- location: `Sheet1!M15`  severity: Medium  confidence: Review
- formula: `=RAND()`
- evidence: Function(s) found: RAND.
- cached value: 0.713393951425198; row labels: ["'IA'"]; column header: ''; used range: A1:R53
- neighbourhood: L13: '=RAND()' -> 0.860551289535587 | M13: '=RAND()' -> 0.607291275625343 | N13: '=RAND()' -> 0.608764428941481 | O13: '=RAND()' -> 0.496891640800003 | L14: '=RAND()' -> 0.264186511365355 | M14: '=RAND()' -> 0.908540285101723 | N14: '=RAND()' -> 0.714663077206663 | O14: '=RAND()' -> 0.557780797793822 | L15: '=RAND()' -> 0.479773693901442 | M15: '=RAND()' -> 0.713393951425198 | N15: '=RAND()' -> 0.18441682604985 | O15: '=RAND()' -> 0.0039478601228613 | L16: '=RAND()' -> 0.0544665116900354 | M16: '=RAND()' -> 0.610682230030722 | N16: '=RAND()' -> 0.229869066081385 | O16: '=RAND()' -> 0.0689629878447349 | L17: '=RAND()' -> 0.378544681241819 | M17: '=RAND()' -> 0.996715164261082 | N17: '=RAND()' -> 0.531406163246732 | O17: '=RAND()' -> 0.680651263481024

### `0a1e0f59bad2|VOLATILE_FUNCTION|Sheet1!D19`

- workbook: `all_data_912_v0.1/spreadsheet/45181/1_45181_input.xlsx`
- location: `Sheet1!D19`  severity: Medium  confidence: Review
- formula: `=C19-TODAY()`
- evidence: Function(s) found: TODAY.
- cached value: -381; row labels: []; column header: ''; used range: A1:I20
- neighbourhood: B17: 2022-05-14 00:00:00 | C17: '=B17+365' -> 2023-05-14 00:00:00 | D17: '=C17-TODAY()' -> -383 | B18: 2022-05-15 00:00:00 | C18: '=B18+365' -> 2023-05-15 00:00:00 | D18: '=C18-TODAY()' -> -382 | B19: 2022-05-16 00:00:00 | C19: '=B19+365' -> 2023-05-16 00:00:00 | D19: '=C19-TODAY()' -> -381 | B20: 2022-05-17 00:00:00 | C20: '=B20+365' -> 2023-05-17 00:00:00 | D20: '=C20-TODAY()' -> -380

### `29a79f5a27e4|VOLATILE_FUNCTION|Sheet1!C45`

- workbook: `all_data_912_v0.1/spreadsheet/49196/1_49196_input.xlsx`
- location: `Sheet1!C45`  severity: Medium  confidence: Review
- formula: `=LEFT(K45,2)&"/"&MID(K45,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K45,FIND(" ",K45,1),6)`
- evidence: Function(s) found: TODAY.
- cached value: '15/01/24 11:33'; row labels: []; column header: ''; used range: A1:L47
- neighbourhood: C43: '=LEFT(K43,2)&"/"&MID(K43,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K43,FIND(... -> '14/01/24 23:53' | D43: '=TEXT(C43,"mmm")' -> 'Jan' | E43: '=WEEKNUM(C43,21)' -> 4 | C44: '=LEFT(K44,2)&"/"&MID(K44,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K44,FIND(... -> '15/01/24 06:08' | D44: '=TEXT(C44,"mmm")' -> 'Jan' | E44: '=WEEKNUM(C44,21)' -> 4 | C45: '=LEFT(K45,2)&"/"&MID(K45,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K45,FIND(... -> '15/01/24 11:33' | D45: '=TEXT(C45,"mmm")' -> 'Jan' | E45: '=WEEKNUM(C45,21)' -> 4 | C46: '=LEFT(K46,2)&"/"&MID(K46,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K46,FIND(... -> '15/01/24 18:13' | D46: '=TEXT(C46,"mmm")' -> 'Jan' | E46: '=WEEKNUM(C46,21)' -> 4 | C47: '=LEFT(K47,2)&"/"&MID(K47,4,2)&"/"&TEXT(TODAY(),"yy")&MID(K47,FIND(... -> '16/01/24 00:53' | D47: '=TEXT(C47,"mmm")' -> 'Jan' | E47: '=WEEKNUM(C47,21)' -> 3

## WHITESPACE_KEY

### `3ff3de7d24e5|WHITESPACE_KEY|Sheet3!A143`

- workbook: `all_data_912_v0.1/spreadsheet/49333/2_49333_input.xlsx`
- location: `Sheet3!A143`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fibrillation        '.
- cached value: 'Fibrillation        '; row labels: []; column header: "'Pablo Mouse         '"; used range: A1:D300
- neighbourhood: A141: 'Sierra Moon         ' | B141: 72 | C141: 81 | A142: 'Pablo Mouse         ' | B142: 83 | C142: 2.9 | A143: 'Fibrillation        ' | B143: 88 | C143: 2.2 | A144: 'Gnarley Time        ' | B144: 82 | C144: 2.7 | A145: 'Naturally Gifted    ' | B145: 72 | C145: 9

### `3495d17364fb|WHITESPACE_KEY|Sheet2!A253`

- workbook: `all_data_912_v0.1/spreadsheet/36764/1_36764_input.xlsx`
- location: `Sheet2!A253`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fully linked                                      '.
- cached value: 'Fully linked                                      '; row labels: []; column header: "'Fully linked                                      '"; used range: A1:S363
- neighbourhood: A251: 'To be actioned                      ... | A252: 'Fully linked                        ... | A253: 'Fully linked                        ... | A254: 'To be actioned                      ... | A255: 'Fully linked                        ...

### `b328dd851137|WHITESPACE_KEY|Sheet2!A212`

- workbook: `all_data_912_v0.1/spreadsheet/36764/3_36764_input.xlsx`
- location: `Sheet2!A212`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fully linked                                      '.
- cached value: 'Fully linked                                      '; row labels: []; column header: "'To be actioned                                    '"; used range: A1:S362
- neighbourhood: A210: 'Fully linked                        ... | A211: 'To be actioned                      ... | A212: 'Fully linked                        ... | A213: 'Fully linked                        ... | A214: 'Fully linked                        ...

### `df8c7fc9d14b|WHITESPACE_KEY|test!A10172`

- workbook: `all_data_912_v0.1/spreadsheet/307-46/2_307-46_input.xlsx`
- location: `test!A10172`  severity: Medium  confidence: Review
- evidence: Raw value is ' 100-717   ;                   ;                                                                                                   ;20                 ;CU31               ;                   ;'.
- cached value: ' 100-717   ;                   ;                        ...; row labels: []; column header: "' 100-717   ;                   ;                        ..."; used range: A1:U22319
- neighbourhood: A10170: ' 100-717   ;                   ;    ... | A10172: ' 100-717   ;                   ;    ... | A10174: ' 100-717   ;                   ;    ...

### `b328dd851137|WHITESPACE_KEY|Sheet2!A240`

- workbook: `all_data_912_v0.1/spreadsheet/36764/3_36764_input.xlsx`
- location: `Sheet2!A240`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fully linked                                      '.
- cached value: 'Fully linked                                      '; row labels: []; column header: "'To be actioned                                    '"; used range: A1:S362
- neighbourhood: A238: 'Fully linked                        ... | A239: 'To be actioned                      ... | A240: 'Fully linked                        ... | A241: 'To be actioned                      ... | A242: 'To be actioned                      ...

### `ed000e28cd42|WHITESPACE_KEY|Sheet3!A244`

- workbook: `all_data_912_v0.1/spreadsheet/49333/1_49333_input.xlsx`
- location: `Sheet3!A244`  severity: Medium  confidence: Review
- evidence: Raw value is 'Snowys Sister      '.
- cached value: 'Snowys Sister      '; row labels: []; column header: "'Panda Mick          '"; used range: A1:D300
- neighbourhood: A242: 'Downstream          ' | B242: 81 | C242: 5.5 | A243: 'Panda Mick          ' | B243: 88 | C243: 7 | A244: 'Snowys Sister      ' | B244: 100 | C244: 1.65 | A245: 'Torquay Bale        ' | B245: 84 | C245: 15 | A246: 'Bow Thai            ' | B246: 82 | C246: 13

### `d6b8caaa9b61|WHITESPACE_KEY|2022!A13`

- workbook: `all_data_912_v0.1/spreadsheet/46121/1_46121_input.xlsx`
- location: `2022!A13`  severity: Medium  confidence: Review
- evidence: Raw value is '     Live Birds'.
- cached value: '     Live Birds'; row labels: []; column header: "'Poultry'"; used range: A1:AH902
- neighbourhood: A11: 'Expenses' | A12: 'Poultry' | A13: '     Live Birds' | A14: '     Feed' | A15: 'Total' | B15: '=SUM(B13:B14)' -> 0 | C15: '=SUM(C12:C14)' -> 0

### `2cf461190da8|WHITESPACE_KEY|test!A1015`

- workbook: `all_data_912_v0.1/spreadsheet/307-46/1_307-46_input.xlsx`
- location: `test!A1015`  severity: Medium  confidence: Review
- evidence: Raw value is ' 100-678   ;                   ;                                                                                                   ;20                 ;CU13               ;60.00              ;40'.
- cached value: ' 100-678   ;                   ;                        ...; row labels: []; column header: "' 100-678   ;                   ;                        ..."; used range: A1:U22319
- neighbourhood: A1013: ' 100-678   ;                   ;    ... | A1015: ' 100-678   ;                   ;    ... | A1017: ' 100-678   ;                   ;    ...

### `9324c9b68159|WHITESPACE_KEY|Sheet2!A271`

- workbook: `all_data_912_v0.1/spreadsheet/36764/2_36764_input.xlsx`
- location: `Sheet2!A271`  severity: Medium  confidence: Review
- evidence: Raw value is 'To be actioned                                    '.
- cached value: 'To be actioned                                    '; row labels: []; column header: "'Fully linked                                      '"; used range: A1:S363
- neighbourhood: A269: 'To be actioned                      ... | A270: 'Fully linked                        ... | A271: 'To be actioned                      ... | A272: 'To be actioned                      ... | A273: 'To be actioned                      ...

### `ed000e28cd42|WHITESPACE_KEY|Sheet3!A172`

- workbook: `all_data_912_v0.1/spreadsheet/49333/1_49333_input.xlsx`
- location: `Sheet3!A172`  severity: Medium  confidence: Review
- evidence: Raw value is 'Rev Up Zeus         '.
- cached value: 'Rev Up Zeus         '; row labels: []; column header: "'Turn The Key        '"; used range: A1:D300
- neighbourhood: A170: 'Georgio Bale        ' | B170: 78 | C170: 26 | A171: 'Turn The Key        ' | B171: 81 | C171: 61 | A172: 'Rev Up Zeus         ' | B172: 63 | C172: 41 | A173: 'Copper Canyon       ' | B173: 88 | C173: 5 | A174: 'Resounding          ' | B174: 72 | C174: 41

### `3ff3de7d24e5|WHITESPACE_KEY|Sheet3!A13`

- workbook: `all_data_912_v0.1/spreadsheet/49333/2_49333_input.xlsx`
- location: `Sheet3!A13`  severity: Medium  confidence: Review
- evidence: Raw value is 'Shakey Graves       '.
- cached value: 'Shakey Graves       '; row labels: []; column header: "'Ria                 '"; used range: A1:D300
- neighbourhood: A11: 'Aston Texan         ' | B11: 100 | C11: 2.7 | A12: 'Ria                 ' | B12: 80 | C12: 16 | A13: 'Shakey Graves       ' | B13: 98 | C13: 5 | A14: 'Summer Scorcher     ' | B14: 63 | C14: 4.2 | A15: 'Hillbilly Blaze     ' | B15: 57 | C15: 34

### `d724d7c85d8e|WHITESPACE_KEY|NOV23!A14`

- workbook: `all_data_912_v0.1/spreadsheet/50534/3_50534_input.xlsx`
- location: `NOV 23!A14`  severity: Medium  confidence: Review
- evidence: Raw value is 'COURTNEY '.
- cached value: 'COURTNEY '; row labels: []; column header: "'DONITA'"; used range: A1:I27
- neighbourhood: A12: 'ANDREW' | B12: '(206)571-7535' | C12: '7A-3P' | A13: 'DONITA' | B13: '(253)431-9941' | C13: '11P-7A' | A14: 'COURTNEY ' | B14: '(602)918-4633' | A15: 'TOM' | B15: '206-852-5614' | C15: '3-11' | A16: 'EDITH' | B16: '509-778-2033'

### `c0e824eb4422|WHITESPACE_KEY|MB!A4`

- workbook: `all_data_912_v0.1/spreadsheet/166-27/1_166-27_input.xlsx`
- location: `MB!A4`  severity: Medium  confidence: Review
- evidence: Raw value is '                   No items delivered -'.
- cached value: '                   No items delivered -'; row labels: []; column header: "'Invoice No: 8675814'"; used range: A1:A52
- neighbourhood: A2: 'Order No: RLS1123389' | A3: 'Invoice No: 8675814' | A4: '                   No items delivere... | A5: '                   NITROFURANTOIN 50... | A6: '                   '

### `df8c7fc9d14b|WHITESPACE_KEY|test!A10084`

- workbook: `all_data_912_v0.1/spreadsheet/307-46/2_307-46_input.xlsx`
- location: `test!A10084`  severity: Medium  confidence: Review
- evidence: Raw value is ' 300-831   ;                   ;                                                                                                   ;50                 ;                   ;0.00               ;'.
- cached value: ' 300-831   ;                   ;                        ...; row labels: []; column header: "' 300-830   ;                   ;                        ..."; used range: A1:U22319
- neighbourhood: A10082: ' 300-830   ;                   ;    ... | A10084: ' 300-831   ;                   ;    ... | A10086: ' 300-830   ;                   ;    ...

### `3495d17364fb|WHITESPACE_KEY|Sheet2!A197`

- workbook: `all_data_912_v0.1/spreadsheet/36764/1_36764_input.xlsx`
- location: `Sheet2!A197`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fully linked                                      '.
- cached value: 'Fully linked                                      '; row labels: []; column header: "'Fully linked                                      '"; used range: A1:S363
- neighbourhood: A195: 'Fully linked                        ... | A196: 'Fully linked                        ... | A197: 'Fully linked                        ... | A198: 'Fully linked                        ... | A199: 'Fully linked                        ...

### `368038bf0531|WHITESPACE_KEY|Sheet3!A227`

- workbook: `all_data_912_v0.1/spreadsheet/49333/3_49333_input.xlsx`
- location: `Sheet3!A227`  severity: Medium  confidence: Review
- evidence: Raw value is 'Hot Tzarina         '.
- cached value: 'Hot Tzarina         '; row labels: []; column header: "'Victory Chico       '"; used range: A1:D300
- neighbourhood: A225: 'Rockstar Harley     ' | B225: 78 | C225: 34 | A226: 'Victory Chico       ' | B226: 81 | C226: 23 | A227: 'Hot Tzarina         ' | B227: 86 | C227: 3.5 | A228: 'Awesome Asset       ' | B228: 62 | C228: 71 | A229: 'Ishmy Lady          ' | B229: 56 | C229: 51

### `c0a3e20a326e|WHITESPACE_KEY|test!A10088`

- workbook: `all_data_912_v0.1/spreadsheet/307-46/3_307-46_input.xlsx`
- location: `test!A10088`  severity: Medium  confidence: Review
- evidence: Raw value is ' 300-830   ;                   ;                                                                                                   ;50                 ;                   ;0.00               ;'.
- cached value: ' 300-830   ;                   ;                        ...; row labels: []; column header: "' 300-830   ;                   ;                        ..."; used range: A1:U22319
- neighbourhood: A10086: ' 300-830   ;                   ;    ... | A10088: ' 300-830   ;                   ;    ... | A10090: ' 300-735A  ;                   ;    ...

### `c0a3e20a326e|WHITESPACE_KEY|test!A10348`

- workbook: `all_data_912_v0.1/spreadsheet/307-46/3_307-46_input.xlsx`
- location: `test!A10348`  severity: Medium  confidence: Review
- evidence: Raw value is ' 100-601   ;                   ;                                                                                                   ;100                ;CU31               ;260.00             ;230'.
- cached value: ' 100-601   ;                   ;                        ...; row labels: []; column header: "' 100-601   ;                   ;                        ..."; used range: A1:U22319
- neighbourhood: A10346: ' 100-601   ;                   ;    ... | A10348: ' 100-601   ;                   ;    ... | A10350: ' 100-601   ;                   ;    ...

### `9324c9b68159|WHITESPACE_KEY|Sheet2!A100`

- workbook: `all_data_912_v0.1/spreadsheet/36764/2_36764_input.xlsx`
- location: `Sheet2!A100`  severity: Medium  confidence: Review
- evidence: Raw value is 'Fully linked                                      '.
- cached value: 'Fully linked                                      '; row labels: []; column header: "'Fully linked                                      '"; used range: A1:S363
- neighbourhood: A98: 'To be actioned                      ... | A99: 'Fully linked                        ... | A100: 'Fully linked                        ... | A101: 'To be actioned                      ... | A102: 'Fully linked                        ...

### `c42da7e96040|WHITESPACE_KEY|Okay!A1`

- workbook: `all_data_912_v0.1/spreadsheet/57427/1_57427_input.xlsx`
- location: `Okay!A1`  severity: Medium  confidence: Review
- evidence: Raw value is ' Name'.
- cached value: ' Name'; row labels: []; column header: ''; used range: A1:I277
- neighbourhood: A1: ' Name' | B1: 'Area' | C1: 'Area Time' | A2: 'Abdelnour, Habig' | B2: 'YMCA' | C2: 09:00:00 | A3: 'Abdelnour, Habig' | B3: 'YMCA' | C3: 17:00:00

### `fd3bd0e9c845|WHITESPACE_KEY|Sheet1!A1`

- workbook: `all_data_912_v0.1/spreadsheet/54675/3_54675_input.xlsx`
- location: `Sheet1!A1`  severity: Medium  confidence: Review
- evidence: Raw value is 'Month '.
- cached value: 'Month '; row labels: []; column header: ''; used range: A1:F2452
- neighbourhood: A1: 'Month ' | B1: 'Investigating Officer (s)' | A2: 4 | B2: 'Gary Stoddard' | A3: 4 | B3: 'Gary Stoddard'

### `0e8785562296|WHITESPACE_KEY|COVER!A11`

- workbook: `all_data_912_v0.1/spreadsheet/56915/2_56915_input.xlsx`
- location: `COVER!A11`  severity: Medium  confidence: Review
- evidence: Raw value is ' '.
- cached value: ' '; row labels: []; column header: ''; used range: A1:E23
- neighbourhood: A11: ' ' | A12: 'Entity >>' | B12: 'V - 6666' | A13: ' ' | B13: 'January' | C13: '% age'

### `d7dbbad9a96d|WHITESPACE_KEY|Sheet1!A13`

- workbook: `all_data_912_v0.1/spreadsheet/50472/3_50472_input.xlsx`
- location: `Sheet1!A13`  severity: Medium  confidence: Review
- evidence: Raw value is '606270 Acc. Social Charges - Expense '.
- cached value: '606270 Acc. Social Charges - Expense '; row labels: []; column header: "'205035 Accrued Social Charges '"; used range: A1:A17
- neighbourhood: A11: '205035 Accrued Social Charges ' | A13: '606270 Acc. Social Charges - Expense ' | A14: '205035 Accrued Social Charges '

### `b2d0d6365d71|WHITESPACE_KEY|Sheet1!B24`

- workbook: `all_data_912_v0.1/spreadsheet/54675/1_54675_input.xlsx`
- location: `Sheet1!B24`  severity: Medium  confidence: Review
- evidence: Raw value is 'Angela McConnell '.
- cached value: 'Angela McConnell '; row labels: []; column header: "'Angela McConnell '"; used range: A1:F2452
- neighbourhood: A22: 4 | B22: 'Building Services' | A23: 4 | B23: 'Angela McConnell ' | A24: 4 | B24: 'Angela McConnell ' | A25: 4 | B25: 'Phyllis McFadyen' | A26: 4 | B26: 'Sandy Ross'

### `fc00b2b9b781|WHITESPACE_KEY|Sheet1!A1`

- workbook: `all_data_912_v0.1/spreadsheet/50233/3_50233_input.xlsx`
- location: `Sheet1!A1`  severity: Medium  confidence: Review
- evidence: Raw value is 'WORK ORDER '.
- cached value: 'WORK ORDER '; row labels: []; column header: ''; used range: A1:D39
- neighbourhood: A1: 'WORK ORDER ' | A2: 10111 | A3: 10112

## WHOLE_COLUMN_REFERENCE

### `a4affba670e1|WHOLE_COLUMN_REFERENCE|Sheet1!B17`

- workbook: `all_data_912_v0.1/spreadsheet/55515/2_55515_input.xlsx`
- location: `Sheet1!B17`  severity: Medium  confidence: Review
- formula: `=COUNTIFS(Main!H:H,A17,Main!D:D,"<>")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: ["'retailer_specific_comments'"]; column header: ''; used range: A1:M20
- neighbourhood: A15: 'Re-moderation reject' | B15: '=COUNTIFS(Main!H:H,A15,Main!D:D,"<>")' -> 0 | C15: '=COUNTIFS(Main!I:I,B15,Main!E:E,"<>")' -> 0 | D15: '=COUNTIFS(Main!J:J,C15,Main!F:F,"<>")' -> 0 | A16: 'reference_individuals_in_a_malicious... | B16: '=COUNTIFS(Main!H:H,A16,Main!D:D,"<>")' -> 0 | C16: '=COUNTIFS(Main!I:I,B16,Main!E:E,"<>")' -> 0 | D16: '=COUNTIFS(Main!J:J,C16,Main!F:F,"<>")' -> 0 | A17: 'retailer_specific_comments' | B17: '=COUNTIFS(Main!H:H,A17,Main!D:D,"<>")' -> 0 | C17: '=COUNTIFS(Main!I:I,B17,Main!E:E,"<>")' -> 0 | D17: '=COUNTIFS(Main!J:J,C17,Main!F:F,"<>")' -> 0 | A18: 'reviewer_cannot_review' | B18: '=COUNTIFS(Main!H:H,A18,Main!D:D,"<>")' -> 0 | C18: '=COUNTIFS(Main!I:I,B18,Main!E:E,"<>")' -> 0 | D18: '=COUNTIFS(Main!J:J,C18,Main!F:F,"<>")' -> 0 | A19: 'reviewer_does_not_have_product' | B19: '=COUNTIFS(Main!H:H,A19,Main!D:D,"<>")' -> 1 | C19: '=COUNTIFS(Main!I:I,B19,Main!E:E,"<>")' -> 0 | D19: '=COUNTIFS(Main!J:J,C19,Main!F:F,"<>")' -> 0

### `8738ef8d70bc|WHOLE_COLUMN_REFERENCE|Sheet1!B279`

- workbook: `all_data_912_v0.1/spreadsheet/17049/2_17049_input.xlsx`
- location: `Sheet1!B279`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A279,G:G,""))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 00:00:00; row labels: []; column header: ''; used range: A1:G1998
- neighbourhood: A277: 276 | B277: '=MAX(IF(F:F=A277,G:G,"")) {array B277}' -> 00:00:00 | A278: 277 | B278: '=MAX(IF(F:F=A278,G:G,"")) {array B278}' -> 00:00:00 | A279: 278 | B279: '=MAX(IF(F:F=A279,G:G,"")) {array B279}' -> 00:00:00 | A280: 279 | B280: '=MAX(IF(F:F=A280,G:G,"")) {array B280}' -> 00:00:00 | A281: 280 | B281: '=MAX(IF(F:F=A281,G:G,"")) {array B281}' -> 00:00:00

### `338c1c07a8c4|WHOLE_COLUMN_REFERENCE|Sheet1!AA9`

- workbook: `all_data_912_v0.1/spreadsheet/45581/1_45581_input.xlsx`
- location: `Sheet1!AA9`  severity: Medium  confidence: Review
- formula: `=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AA)-1,COUNTA($D$7:$AQ$7))+1)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: []; column header: ''; used range: A1:AF9
- range $D$7:$AQ$7: values ["'d'", "'g'", "'f'", "'h'", "'i'", "'c'", "'j'", "'s'", "'k'", "'e'", "'o'", "'i'"]; beyond: {'left': 'C7: None', 'right': 'AR7: None'}
- neighbourhood: Y7: '=IFERROR(MID($B5,COLUMNS($D7:Y7),1),"")' -> None | Z7: '=IFERROR(MID($B5,COLUMNS($D7:Z7),1),"")' -> None | AA7: '=IFERROR(MID($B5,COLUMNS($D7:AA7),1),"")' -> None | AB7: '=IFERROR(MID($B5,COLUMNS($D7:AB7),1),"")' -> None | AC7: '=IFERROR(MID($B5,COLUMNS($D7:AC7),1),"")' -> None | Y9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Y)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | Z9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:Z)-1,COUNTA($D$7:$AQ$7))+1) {arra... -> None | AA9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AA)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AB9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AB)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None | AC9: '=INDEX($D$7:$AQ$7,MOD(COLUMNS($D:AC)-1,COUNTA($D$7:$AQ$7))+1) {arr... -> None

### `93e74f622cb1|WHOLE_COLUMN_REFERENCE|Sheet1!B8`

- workbook: `all_data_912_v0.1/spreadsheet/57743/2_57743_input.xlsx`
- location: `Sheet1!B8`  severity: Medium  confidence: Review
- formula: `=INDEX(D:D,MATCH(A8,C:C,0))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: '#N/A'; row labels: ["'4GXCC005AC6HUA'"]; column header: ''; used range: A1:D19
- neighbourhood: A6: '4GXCB006AC6HUA' | B6: '=INDEX(D:D,MATCH(A6,C:C,0))' -> '#N/A' | C6: 'A4MXB4248AC6HA' | D6: 376 | A7: '4GXCB016AC6HUA' | B7: '=INDEX(D:D,MATCH(A7,C:C,0))' -> '#N/A' | C7: 'A4MXC4248AC6HA' | D7: 386 | A8: '4GXCC005AC6HUA' | B8: '=INDEX(D:D,MATCH(A8,C:C,0)) {array B8}' -> '#N/A' | C8: 'A4MXD4248AC6HA' | D8: 418 | A9: '4GXCC007AC6HUA' | B9: '=INDEX(D:D,MATCH(A9,C:C,0)) {array B9}' -> '#N/A' | C9: 'A4MXC4260AC3HA' | D9: 468 | A10: '4GXCC009AC6HUA' | B10: '=INDEX(D:D,MATCH(A10,C:C,0)) {array B10}' -> '#N/A' | C10: 'A4MXD4260AC3HA' | D10: 488

### `a4affba670e1|WHOLE_COLUMN_REFERENCE|Sheet1!I20`

- workbook: `all_data_912_v0.1/spreadsheet/55515/2_55515_input.xlsx`
- location: `Sheet1!I20`  severity: Medium  confidence: Review
- formula: `=COUNTIFS(Main!O:O,H20,Main!K:K,"<>")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: ["'spam'"]; column header: ''; used range: A1:M20
- neighbourhood: G18: '=COUNTIFS(Main!M:M,F18,Main!I:I,"<>")' -> 0 | H18: '=COUNTIFS(Main!N:N,G18,Main!J:J,"<>")' -> 0 | I18: '=COUNTIFS(Main!O:O,H18,Main!K:K,"<>")' -> 0 | J18: '=COUNTIFS(Main!P:P,I18,Main!L:L,"<>")' -> 0 | K18: '=COUNTIFS(Main!Q:Q,J18,Main!M:M,"<>")' -> 0 | G19: '=COUNTIFS(Main!M:M,F19,Main!I:I,"<>")' -> 0 | H19: '=COUNTIFS(Main!N:N,G19,Main!J:J,"<>")' -> 0 | I19: '=COUNTIFS(Main!O:O,H19,Main!K:K,"<>")' -> 0 | J19: '=COUNTIFS(Main!P:P,I19,Main!L:L,"<>")' -> 0 | K19: '=COUNTIFS(Main!Q:Q,J19,Main!M:M,"<>")' -> 0 | G20: '=COUNTIFS(Main!M:M,F20,Main!I:I,"<>")' -> 0 | H20: '=COUNTIFS(Main!N:N,G20,Main!J:J,"<>")' -> 0 | I20: '=COUNTIFS(Main!O:O,H20,Main!K:K,"<>")' -> 0 | J20: '=COUNTIFS(Main!P:P,I20,Main!L:L,"<>")' -> 0 | K20: '=COUNTIFS(Main!Q:Q,J20,Main!M:M,"<>")' -> 0

### `22ba7e38ecb1|WHOLE_COLUMN_REFERENCE|Leave_Record!C12`

- workbook: `all_data_912_v0.1/spreadsheet/CF_13024/1_CF_13024_input.xlsx`
- location: `Leave_Record!C12`  severity: Medium  confidence: Review
- formula: `=VLOOKUP(B12,'Staff Database'!B:C,2,FALSE)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 27106465; row labels: ["'Betty'"]; column header: ''; used range: A1:BI34
- neighbourhood: A10: 4 | B10: 'Henry' | C10: "=VLOOKUP(B10,'Staff Database'!B:C,2,FALSE)" -> 27102649 | D10: "=VLOOKUP(A10,'Staff Database'!A:F,6,FALSE)" -> 'David' | E10: "=VLOOKUP(B10,'Staff Database'!B:D,3,FALSE)" -> 'N' | A11: 5 | B11: 'Richard' | C11: "=VLOOKUP(B11,'Staff Database'!B:C,2,FALSE)" -> 27104104 | D11: "=VLOOKUP(A11,'Staff Database'!A:F,6,FALSE)" -> 'Ricky' | E11: "=VLOOKUP(B11,'Staff Database'!B:D,3,FALSE)" -> 'D' | A12: 6 | B12: 'Betty' | C12: "=VLOOKUP(B12,'Staff Database'!B:C,2,FALSE)" -> 27106465 | D12: "=VLOOKUP(A12,'Staff Database'!A:F,6,FALSE)" -> 'David' | E12: "=VLOOKUP(B12,'Staff Database'!B:D,3,FALSE)" -> 'D' | A13: 7 | B13: 'Paul' | C13: "=VLOOKUP(B13,'Staff Database'!B:C,2,FALSE)" -> 27101775 | D13: "=VLOOKUP(A13,'Staff Database'!A:F,6,FALSE)" -> 'Ricky' | E13: "=VLOOKUP(B13,'Staff Database'!B:D,3,FALSE)" -> 'N' | A14: 8 | B14: 'Mandy' | C14: "=VLOOKUP(B14,'Staff Database'!B:C,2,FALSE)" -> 27100893 | D14: "=VLOOKUP(A14,'Staff Database'!A:F,6,FALSE)" -> 'David' | E14: "=VLOOKUP(B14,'Staff Database'!B:D,3,FALSE)" -> 'D'

### `5358e587d475|WHOLE_COLUMN_REFERENCE|Sheet1!B139`

- workbook: `all_data_912_v0.1/spreadsheet/17049/1_17049_input.xlsx`
- location: `Sheet1!B139`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A139,G:G,""))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 2014-03-08 00:00:00; row labels: []; column header: ''; used range: A1:G1998
- neighbourhood: A137: 136 | B137: '=MAX(IF(F:F=A137,G:G,"")) {array B137}' -> 2014-03-08 00:00:00 | A138: 137 | B138: '=MAX(IF(F:F=A138,G:G,"")) {array B138}' -> 2014-03-08 00:00:00 | A139: 138 | B139: '=MAX(IF(F:F=A139,G:G,"")) {array B139}' -> 2014-03-08 00:00:00 | A140: 139 | B140: '=MAX(IF(F:F=A140,G:G,"")) {array B140}' -> 2014-04-10 00:00:00 | A141: 140 | B141: '=MAX(IF(F:F=A141,G:G,"")) {array B141}' -> 2014-04-09 00:00:00

### `be35c3601fd1|WHOLE_COLUMN_REFERENCE|Sheet2!B152`

- workbook: `all_data_912_v0.1/spreadsheet/57072/1_57072_input.xlsx`
- location: `Sheet2!B152`  severity: Medium  confidence: Review
- formula: `=_xlfn.XLOOKUP("*"&A152&"*",Sheet1!A:A,Sheet1!D:D,"",2)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: ["'M152'"]; column header: ''; used range: A1:B300
- neighbourhood: A150: 'M150' | B150: '=_xlfn.XLOOKUP("*"&A150&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A151: 'M151' | B151: '=_xlfn.XLOOKUP("*"&A151&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A152: 'M152' | B152: '=_xlfn.XLOOKUP("*"&A152&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A153: 'M153' | B153: '=_xlfn.XLOOKUP("*"&A153&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A154: 'M154' | B154: '=_xlfn.XLOOKUP("*"&A154&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None

### `f06ab49c2656|WHOLE_COLUMN_REFERENCE|Sheet1!J10`

- workbook: `all_data_912_v0.1/spreadsheet/55515/1_55515_input.xlsx`
- location: `Sheet1!J10`  severity: Medium  confidence: Review
- formula: `=COUNTIFS(Main!P:P,I10,Main!L:L,"<>")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: ["'factually_incorrect_may_confuse'"]; column header: ''; used range: A1:M20
- neighbourhood: H8: '=COUNTIFS(Main!N:N,G8,Main!J:J,"<>")' -> 0 | I8: '=COUNTIFS(Main!O:O,H8,Main!K:K,"<>")' -> 0 | J8: '=COUNTIFS(Main!P:P,I8,Main!L:L,"<>")' -> 0 | K8: '=COUNTIFS(Main!Q:Q,J8,Main!M:M,"<>")' -> 0 | L8: '=COUNTIFS(Main!R:R,K8,Main!N:N,"<>")' -> 0 | H9: '=COUNTIFS(Main!N:N,G9,Main!J:J,"<>")' -> 0 | I9: '=COUNTIFS(Main!O:O,H9,Main!K:K,"<>")' -> 0 | J9: '=COUNTIFS(Main!P:P,I9,Main!L:L,"<>")' -> 0 | K9: '=COUNTIFS(Main!Q:Q,J9,Main!M:M,"<>")' -> 0 | L9: '=COUNTIFS(Main!R:R,K9,Main!N:N,"<>")' -> 0 | H10: '=COUNTIFS(Main!N:N,G10,Main!J:J,"<>")' -> 0 | I10: '=COUNTIFS(Main!O:O,H10,Main!K:K,"<>")' -> 0 | J10: '=COUNTIFS(Main!P:P,I10,Main!L:L,"<>")' -> 0 | K10: '=COUNTIFS(Main!Q:Q,J10,Main!M:M,"<>")' -> 0 | L10: '=COUNTIFS(Main!R:R,K10,Main!N:N,"<>")' -> 0 | H11: '=COUNTIFS(Main!N:N,G11,Main!J:J,"<>")' -> 0 | I11: '=COUNTIFS(Main!O:O,H11,Main!K:K,"<>")' -> 0 | J11: '=COUNTIFS(Main!P:P,I11,Main!L:L,"<>")' -> 0 | K11: '=COUNTIFS(Main!Q:Q,J11,Main!M:M,"<>")' -> 0 | L11: '=COUNTIFS(Main!R:R,K11,Main!N:N,"<>")' -> 0 | H12: '=COUNTIFS(Main!N:N,G12,Main!J:J,"<>")' -> 0 | I12: '=COUNTIFS(Main!O:O,H12,Main!K:K,"<>")' -> 0 | J12: '=COUNTIFS(Main!P:P,I12,Main!L:L,"<>")' -> 0 | K12: '=COUNTIFS(Main!Q:Q,J12,Main!M:M,"<>")' -> 0 | L12: '=COUNTIFS(Main!R:R,K12,Main!N:N,"<>")' -> 0

### `eb31bc468d52|WHOLE_COLUMN_REFERENCE|Form!F11`

- workbook: `all_data_912_v0.1/spreadsheet/59969/2_59969_input.xlsx`
- location: `Form!F11`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3)*(Report!$B$2:$B$70000=Form!$B$5),ROW(Report!$A$2:$A$70000)),ROWS($A$1:C6))),"")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: []; column header: ''; used range: A1:M26
- range Report!$A$2:$A$70000: values ['None', '2073000108', '2073000108', '2073000108', '2073000108', '2073000108', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116']; beyond: {'above': 'A1: None', 'below': 'A70001: None'}
- neighbourhood: D9: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 393.75 | E9: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F9: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G9: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H9: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D10: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | E10: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F10: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G10: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H10: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D11: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 542 | E11: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F11: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G11: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H11: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D12: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 102.51 | E12: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 726.49 | F12: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G12: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H12: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D13: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 53.56 | E13: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F13: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | G13: '=IFERROR(INDEX(Report!J:J,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | H13: '=IFERROR(INDEX(Report!K:K,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!G9`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!G9`  severity: Medium  confidence: Review
- formula: `=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!E:E,,,-1),"")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: ["'ABC8'"]; column header: ''; used range: A1:K10
- neighbourhood: E7: '=_xlfn.IFNA(_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D),"")' -> 200000009 | F7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H7: '=IF(B7="Yes",_xlfn.XLOOKUP(A7,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I7: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A7=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | E8: '=_xlfn.IFNA(_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!D:D),"")' -> 200000010 | F8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I8: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A8=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | E9: '=_xlfn.IFNA(_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!D:D),"")' -> 200000011 | F9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I9: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A9=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | E10: '=_xlfn.IFNA(_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!D:D),"")' -> 200000012 | F10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I10: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A10=ZORD!A:A,ZORD!C:... -> '2022-12-31'

### `68be09e637ed|WHOLE_COLUMN_REFERENCE|Sheet1!D3`

- workbook: `all_data_912_v0.1/spreadsheet/56451/1_56451_input.xlsx`
- location: `Sheet1!D3`  severity: Medium  confidence: Review
- formula: `=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 'car'; row labels: ["'Mary'"]; column header: ''; used range: A1:U11
- range 'Sheet 2'!$A$1:$F$7: values ["'NAME'", "'transport'", "'weight'", "'location'", "'food'", "'height'", "'John '", "'bike'", '150', "'north'", "'high'", '180']; beyond: {}
- neighbourhood: B1: 'transport' | C1: 'weight' | D1: 'location' | E1: 'food' | F1: 'height' | B2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | C2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | D2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | E2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | F2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | B3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | C3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | D3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | E3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | F3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | B4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | C4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | D4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | E4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | F4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | B5: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A5,'Sheet 2'!$A:$A,0),2)" -> 0 | C5: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A5,'Sheet 2'!$A:$A,0),2)" -> 0 | D5: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A5,'Sheet 2'!$A:$A,0),2)" -> 0 | E5: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A5,'Sheet 2'!$A:$A,0),2)" -> 0 | F5: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A5,'Sheet 2'!$A:$A,0),2)" -> 0

### `740614797bbb|WHOLE_COLUMN_REFERENCE|Sheet1!N10`

- workbook: `all_data_912_v0.1/spreadsheet/33935/1_33935_input.xlsx`
- location: `Sheet1!N10`  severity: Medium  confidence: Review
- formula: `=IF(L11>1,LOOKUP(2,1/(J:J<>""),J:J))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 'PEPEPEPEPE'; row labels: ["'B'", "'B'"]; column header: ''; used range: A1:S30
- neighbourhood: L8: '=IF(AND(G8<1,L7<>""),1,L7+1)' -> 1 | N8: '=IF(L9>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N8}' -> 'PEPEPEPEPE' | L9: '=IF(AND(G9<1,L8<>""),1,L8+1)' -> 2 | N9: '=IF(L10>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N9}' -> 'PEPEPEPEPE' | L10: '=IF(AND(G10<1,L9<>""),1,L9+1)' -> 3 | N10: '=IF(L11>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N10}' -> 'PEPEPEPEPE' | L11: '=IF(AND(G11<1,L10<>""),1,L10+1)' -> 4 | N11: '=IF(L12>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N11}' -> 'PEPEPEPEPE' | L12: '=IF(AND(G12<1,L11<>""),1,L11+1)' -> 5 | N12: '=IF(L13>1,LOOKUP(2,1/(J:J<>""),J:J)) {array N12}' -> 'PEPEPEPEPE'

### `1e818dae8f1b|WHOLE_COLUMN_REFERENCE|Sheet2!B165`

- workbook: `all_data_912_v0.1/spreadsheet/57072/2_57072_input.xlsx`
- location: `Sheet2!B165`  severity: Medium  confidence: Review
- formula: `=_xlfn.XLOOKUP("*"&A165&"*",Sheet1!A:A,Sheet1!D:D,"",2)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: ["'M165'"]; column header: ''; used range: A1:B300
- neighbourhood: A163: 'M163' | B163: '=_xlfn.XLOOKUP("*"&A163&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A164: 'M164' | B164: '=_xlfn.XLOOKUP("*"&A164&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A165: 'M165' | B165: '=_xlfn.XLOOKUP("*"&A165&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A166: 'M166' | B166: '=_xlfn.XLOOKUP("*"&A166&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A167: 'M167' | B167: '=_xlfn.XLOOKUP("*"&A167&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None

### `68be09e637ed|WHOLE_COLUMN_REFERENCE|Sheet1!E2`

- workbook: `all_data_912_v0.1/spreadsheet/56451/1_56451_input.xlsx`
- location: `Sheet1!E2`  severity: Medium  confidence: Review
- formula: `=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 'bike'; row labels: ["'John '"]; column header: "'food'"; used range: A1:U11
- range 'Sheet 2'!$A$1:$F$7: values ["'NAME'", "'transport'", "'weight'", "'location'", "'food'", "'height'", "'John '", "'bike'", '150', "'north'", "'high'", '180']; beyond: {}
- neighbourhood: C1: 'weight' | D1: 'location' | E1: 'food' | F1: 'height' | C2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | D2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | E2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | F2: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A2,'Sheet 2'!$A:$A,0),2)" -> 'bike' | C3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | D3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | E3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | F3: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A3,'Sheet 2'!$A:$A,0),2)" -> 'car' | C4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | D4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | E4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk' | F4: "=INDEX('Sheet 2'!$A$1:$F$7,MATCH(Sheet1!$A4,'Sheet 2'!$A:$A,0),2)" -> 'walk'

### `5358e587d475|WHOLE_COLUMN_REFERENCE|Sheet1!B272`

- workbook: `all_data_912_v0.1/spreadsheet/17049/1_17049_input.xlsx`
- location: `Sheet1!B272`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A272,G:G,""))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 00:00:00; row labels: []; column header: ''; used range: A1:G1998
- neighbourhood: A270: 269 | B270: '=MAX(IF(F:F=A270,G:G,"")) {array B270}' -> 00:00:00 | A271: 270 | B271: '=MAX(IF(F:F=A271,G:G,"")) {array B271}' -> 00:00:00 | A272: 271 | B272: '=MAX(IF(F:F=A272,G:G,"")) {array B272}' -> 00:00:00 | A273: 272 | B273: '=MAX(IF(F:F=A273,G:G,"")) {array B273}' -> 00:00:00 | A274: 273 | B274: '=MAX(IF(F:F=A274,G:G,"")) {array B274}' -> 00:00:00

### `a34787c22768|WHOLE_COLUMN_REFERENCE|Sheet1!G10`

- workbook: `all_data_912_v0.1/spreadsheet/55515/3_55515_input.xlsx`
- location: `Sheet1!G10`  severity: Medium  confidence: Review
- formula: `=COUNTIFS(Main!M:M,F10,Main!I:I,"<>")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: ["'factually_incorrect_may_confuse'"]; column header: ''; used range: A1:M20
- neighbourhood: E8: '=COUNTIFS(Main!K:K,D8,Main!G:G,"<>")' -> 0 | F8: '=COUNTIFS(Main!L:L,E8,Main!H:H,"<>")' -> 0 | G8: '=COUNTIFS(Main!M:M,F8,Main!I:I,"<>")' -> 0 | H8: '=COUNTIFS(Main!N:N,G8,Main!J:J,"<>")' -> 0 | I8: '=COUNTIFS(Main!O:O,H8,Main!K:K,"<>")' -> 0 | E9: '=COUNTIFS(Main!K:K,D9,Main!G:G,"<>")' -> 0 | F9: '=COUNTIFS(Main!L:L,E9,Main!H:H,"<>")' -> 0 | G9: '=COUNTIFS(Main!M:M,F9,Main!I:I,"<>")' -> 0 | H9: '=COUNTIFS(Main!N:N,G9,Main!J:J,"<>")' -> 0 | I9: '=COUNTIFS(Main!O:O,H9,Main!K:K,"<>")' -> 0 | E10: '=COUNTIFS(Main!K:K,D10,Main!G:G,"<>")' -> 0 | F10: '=COUNTIFS(Main!L:L,E10,Main!H:H,"<>")' -> 0 | G10: '=COUNTIFS(Main!M:M,F10,Main!I:I,"<>")' -> 0 | H10: '=COUNTIFS(Main!N:N,G10,Main!J:J,"<>")' -> 0 | I10: '=COUNTIFS(Main!O:O,H10,Main!K:K,"<>")' -> 0 | E11: '=COUNTIFS(Main!K:K,D11,Main!G:G,"<>")' -> 0 | F11: '=COUNTIFS(Main!L:L,E11,Main!H:H,"<>")' -> 0 | G11: '=COUNTIFS(Main!M:M,F11,Main!I:I,"<>")' -> 0 | H11: '=COUNTIFS(Main!N:N,G11,Main!J:J,"<>")' -> 0 | I11: '=COUNTIFS(Main!O:O,H11,Main!K:K,"<>")' -> 0 | E12: '=COUNTIFS(Main!K:K,D12,Main!G:G,"<>")' -> 0 | F12: '=COUNTIFS(Main!L:L,E12,Main!H:H,"<>")' -> 0 | G12: '=COUNTIFS(Main!M:M,F12,Main!I:I,"<>")' -> 0 | H12: '=COUNTIFS(Main!N:N,G12,Main!J:J,"<>")' -> 0 | I12: '=COUNTIFS(Main!O:O,H12,Main!K:K,"<>")' -> 0

### `8738ef8d70bc|WHOLE_COLUMN_REFERENCE|Sheet1!B149`

- workbook: `all_data_912_v0.1/spreadsheet/17049/2_17049_input.xlsx`
- location: `Sheet1!B149`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A149,G:G,""))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 00:00:00; row labels: []; column header: ''; used range: A1:G1998
- neighbourhood: A147: 146 | B147: '=MAX(IF(F:F=A147,G:G,"")) {array B147}' -> 00:00:00 | A148: 147 | B148: '=MAX(IF(F:F=A148,G:G,"")) {array B148}' -> 00:00:00 | A149: 148 | B149: '=MAX(IF(F:F=A149,G:G,"")) {array B149}' -> 00:00:00 | A150: 149 | B150: '=MAX(IF(F:F=A150,G:G,"")) {array B150}' -> 00:00:00 | A151: 150 | B151: '=MAX(IF(F:F=A151,G:G,"")) {array B151}' -> 00:00:00

### `9ffa652c7e85|WHOLE_COLUMN_REFERENCE|VolymP5_P6_2023!H10`

- workbook: `all_data_912_v0.1/spreadsheet/45896/3_45896_input.xlsx`
- location: `Volym P5_P6_2023!H10`  severity: Medium  confidence: Review
- formula: `=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!D:D,,,-1),"")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: ["'ABC9'"]; column header: ''; used range: A1:K10
- neighbourhood: F8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H8: '=IF(B8="Yes",_xlfn.XLOOKUP(A8,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I8: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A8=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J8: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A8=ZORD!A:A,ZORD!D:D,""))... -> '200000010' | F9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H9: '=IF(B9="Yes",_xlfn.XLOOKUP(A9,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I9: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A9=ZORD!A:A,ZORD!C:C... -> '2022-12-31' | J9: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A9=ZORD!A:A,ZORD!D:D,""))... -> '200000011' | F10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!C:C,,,-1),"")' -> None | G10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!E:E,,,-1),"")' -> None | H10: '=IF(B10="Yes",_xlfn.XLOOKUP(A10,ZORD!A:A,ZORD!D:D,,,-1),"")' -> None | I10: '=TEXT(_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A10=ZORD!A:A,ZORD!C:... -> '2022-12-31' | J10: '=_xlfn.TEXTJOIN(",",TRUE,_xlfn.UNIQUE(IF(A10=ZORD!A:A,ZORD!D:D,"")... -> '200000012'

### `48e3d7dd2f3a|WHOLE_COLUMN_REFERENCE|Sheet1!G20`

- workbook: `all_data_912_v0.1/spreadsheet/56419/3_56419_input.xlsx`
- location: `Sheet1!G20`  severity: Medium  confidence: Review
- formula: `=MATCH(ROW()-ROW($B$1),$E:$E,0)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: '#N/A'; row labels: ["'S'"]; column header: ''; used range: A1:H100
- neighbourhood: E18: '=SUM($D$2:D18)' -> 8 | G18: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H18: '=INDIRECT("A"&G18)' -> '#N/A' | E19: '=SUM($D$2:D19)' -> 8 | G19: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H19: '=INDIRECT("A"&G19)' -> '#N/A' | E20: '=SUM($D$2:D20)' -> 8 | G20: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H20: '=INDIRECT("A"&G20)' -> '#N/A' | E21: '=SUM($D$2:D21)' -> 9 | G21: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H21: '=INDIRECT("A"&G21)' -> '#N/A' | E22: '=SUM($D$2:D22)' -> 10 | G22: '=MATCH(ROW()-ROW($B$1),$E:$E,0)' -> '#N/A' | H22: '=INDIRECT("A"&G22)' -> '#N/A'

### `be35c3601fd1|WHOLE_COLUMN_REFERENCE|Sheet2!B221`

- workbook: `all_data_912_v0.1/spreadsheet/57072/1_57072_input.xlsx`
- location: `Sheet2!B221`  severity: Medium  confidence: Review
- formula: `=_xlfn.XLOOKUP("*"&A221&"*",Sheet1!A:A,Sheet1!D:D,"",2)`
- evidence: Whole-column references can hide range and performance issues.
- cached value: None; row labels: ["'M221'"]; column header: ''; used range: A1:B300
- neighbourhood: A219: 'M219' | B219: '=_xlfn.XLOOKUP("*"&A219&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A220: 'M220' | B220: '=_xlfn.XLOOKUP("*"&A220&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A221: 'M221' | B221: '=_xlfn.XLOOKUP("*"&A221&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A222: 'M222' | B222: '=_xlfn.XLOOKUP("*"&A222&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None | A223: 'M223' | B223: '=_xlfn.XLOOKUP("*"&A223&"*",Sheet1!A:A,Sheet1!D:D,"",2)' -> None

### `d7cd8ee7e5c8|WHOLE_COLUMN_REFERENCE|Sheet1!B205`

- workbook: `all_data_912_v0.1/spreadsheet/17049/3_17049_input.xlsx`
- location: `Sheet1!B205`  severity: Medium  confidence: Review
- formula: `=MAX(IF(F:F=A205,G:G,""))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 00:00:00; row labels: []; column header: ''; used range: A1:G1998
- neighbourhood: A203: 202 | B203: '=MAX(IF(F:F=A203,G:G,"")) {array B203}' -> 2014-03-29 00:00:00 | A204: 203 | B204: '=MAX(IF(F:F=A204,G:G,"")) {array B204}' -> 2014-04-02 00:00:00 | A205: 204 | B205: '=MAX(IF(F:F=A205,G:G,"")) {array B205}' -> 00:00:00 | A206: 205 | B206: '=MAX(IF(F:F=A206,G:G,"")) {array B206}' -> 00:00:00 | A207: 206 | B207: '=MAX(IF(F:F=A207,G:G,"")) {array B207}' -> 00:00:00

### `a34787c22768|WHOLE_COLUMN_REFERENCE|Sheet1!H9`

- workbook: `all_data_912_v0.1/spreadsheet/55515/3_55515_input.xlsx`
- location: `Sheet1!H9`  severity: Medium  confidence: Review
- formula: `=COUNTIFS(Main!N:N,G9,Main!J:J,"<>")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 0; row labels: ["'entirely_off_topic_wrong_section'"]; column header: ''; used range: A1:M20
- neighbourhood: F7: '=COUNTIFS(Main!L:L,E7,Main!H:H,"<>")' -> 0 | G7: '=COUNTIFS(Main!M:M,F7,Main!I:I,"<>")' -> 0 | H7: '=COUNTIFS(Main!N:N,G7,Main!J:J,"<>")' -> 0 | I7: '=COUNTIFS(Main!O:O,H7,Main!K:K,"<>")' -> 0 | J7: '=COUNTIFS(Main!P:P,I7,Main!L:L,"<>")' -> 0 | F8: '=COUNTIFS(Main!L:L,E8,Main!H:H,"<>")' -> 0 | G8: '=COUNTIFS(Main!M:M,F8,Main!I:I,"<>")' -> 0 | H8: '=COUNTIFS(Main!N:N,G8,Main!J:J,"<>")' -> 0 | I8: '=COUNTIFS(Main!O:O,H8,Main!K:K,"<>")' -> 0 | J8: '=COUNTIFS(Main!P:P,I8,Main!L:L,"<>")' -> 0 | F9: '=COUNTIFS(Main!L:L,E9,Main!H:H,"<>")' -> 0 | G9: '=COUNTIFS(Main!M:M,F9,Main!I:I,"<>")' -> 0 | H9: '=COUNTIFS(Main!N:N,G9,Main!J:J,"<>")' -> 0 | I9: '=COUNTIFS(Main!O:O,H9,Main!K:K,"<>")' -> 0 | J9: '=COUNTIFS(Main!P:P,I9,Main!L:L,"<>")' -> 0 | F10: '=COUNTIFS(Main!L:L,E10,Main!H:H,"<>")' -> 0 | G10: '=COUNTIFS(Main!M:M,F10,Main!I:I,"<>")' -> 0 | H10: '=COUNTIFS(Main!N:N,G10,Main!J:J,"<>")' -> 0 | I10: '=COUNTIFS(Main!O:O,H10,Main!K:K,"<>")' -> 0 | J10: '=COUNTIFS(Main!P:P,I10,Main!L:L,"<>")' -> 0 | F11: '=COUNTIFS(Main!L:L,E11,Main!H:H,"<>")' -> 0 | G11: '=COUNTIFS(Main!M:M,F11,Main!I:I,"<>")' -> 0 | H11: '=COUNTIFS(Main!N:N,G11,Main!J:J,"<>")' -> 0 | I11: '=COUNTIFS(Main!O:O,H11,Main!K:K,"<>")' -> 0 | J11: '=COUNTIFS(Main!P:P,I11,Main!L:L,"<>")' -> 0

### `d6b8caaa9b61|WHOLE_COLUMN_REFERENCE|2022!D7`

- workbook: `all_data_912_v0.1/spreadsheet/46121/1_46121_input.xlsx`
- location: `2022!D7`  severity: Medium  confidence: Review
- formula: `=IF(Transactions!D3=Transactions!D2,"",SUMIF(Transactions!D:D,Transactions!D3,Transactions!C:C))`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 90; row labels: ["'Guineas'"]; column header: "'March'"; used range: A1:AH902
- neighbourhood: D7: '=IF(Transactions!D3=Transactions!D2,"",SUMIF(Transactions!D:D,Tran... -> 90 | B9: '=SUM(B5:B8)' -> 0 | C9: '=SUM(C5:C8)' -> 0 | D9: '=SUM(D5:D8)' -> 90 | E9: '=SUM(E5:E8)' -> 0 | F9: '=SUM(F5:F8)' -> 0

### `233b4f90d078|WHOLE_COLUMN_REFERENCE|Form!D7`

- workbook: `all_data_912_v0.1/spreadsheet/59969/3_59969_input.xlsx`
- location: `Form!D7`  severity: Medium  confidence: Review
- formula: `=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3)*(Report!$B$2:$B$70000=Form!$B$5),ROW(Report!$A$2:$A$70000)),ROWS($A$1:A2))),"")`
- evidence: Whole-column references can hide range and performance issues.
- cached value: 73.97; row labels: []; column header: ''; used range: A1:M26
- range Report!$A$2:$A$70000: values ['None', '2073000108', '2073000108', '2073000108', '2073000108', '2073000108', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116', '2053000116']; beyond: {'above': 'A1: None', 'below': 'A70001: None'}
- neighbourhood: B5: 110018401 | D5: 'NA Balance' | E5: 'PA Balance' | F5: 'TA Balance' | D6: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 250 | E6: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F6: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D7: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 73.97 | E7: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F7: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D8: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | E8: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F8: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | D9: '=IFERROR(INDEX(Report!G:G,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 393.75 | E9: '=IFERROR(INDEX(Report!H:H,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0 | F9: '=IFERROR(INDEX(Report!I:I,SMALL(IF((Report!$A$2:$A$70000=Form!$B$3... -> 0
