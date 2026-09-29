"""IFERROR/IFNA wrappers are reported only when they pass off a failure as data."""

from __future__ import annotations

import pytest

from spreadsheet_auditor.error_masks import masks


@pytest.mark.parametrize(
    "formula, sources, fallback",
    [
        # An average of nothing shown as an average of 0.
        ('=IFERROR(AVERAGEIFS(T[P],T[G],">=75%"),0)', ("AVERAGEIFS",), "0"),
        # A missing record read as an age of 0.
        ("=IFERROR(INDEX($S$2:$S$124,MATCH($A9,$Q$2:$Q124,0)),0)", ("INDEX", "MATCH"), "0"),
        ("=_xlfn.IFNA(INDEX(S!C3:G20,MATCH(A14,S!A3:A20,0)),0)", ("INDEX", "MATCH"), "0"),
        # A bad date or a blank frequency becomes a zero payment.
        ('=IFERROR((MOD(DATEDIF(L$4+1,EOMONTH($D10,0)+1,"m"),12/$C10)=0)*$B10,0)', ("MOD", "DATEDIF", "arithmetic on a cell", "EOMONTH", "a division"), "0"),
        # A division by zero written as the text "0", which totals skip.
        ('=IFERROR(((C12*1.3)+(D12*1))/((B12)),"0")', ("arithmetic on a cell", "a division"), '"0"'),
        ("=IFERROR(B2*C2,)", ("arithmetic on a cell",), "0"),
        ("=IFERROR(B2/C2,D2)", ("a division",), "D2"),
    ],
)
def test_failures_passed_off_as_data_are_reported(formula, sources, fallback):
    [mask] = masks(formula)
    assert mask.sources == sources
    assert mask.fallback == fallback


@pytest.mark.parametrize(
    "formula",
    [
        '=IFERROR(VLOOKUP(C3,DATA!$A:$E,2,0),"")',  # a lookup miss shown as blank
        '=IFERROR(VLOOKUP(I19,$I$6:$J$8,2,FALSE),"Select freq")',  # an explicit message
        '=IFERROR(VLOOKUP(A10,S1!A2:D10,3,FALSE),IFERROR(VLOOKUP(A10,S2!A2:D10,3,FALSE),""))',  # a chain of lists
        "=IFERROR(VLOOKUP(A1,B:C,2,FALSE),NA())",  # turns any error into #N/A
        '=IFERROR(IF(COUNTIFS(T[C],"<1")>=10,AVERAGEIFS(T[P],T[C],"<1"),0),0)',  # the IF already guards it
        '=IFERROR(COUNTIFS(T[C],"<1",T[F],">3"),0)',  # COUNTIFS cannot error
        "=IFERROR(MID($B5,COLUMNS($D7:P7),1),\"\")",  # MID cannot error here
        '=IFERROR(INDEX(R!M:M,SMALL(IF(R!$A$2:$A$70=F!$B$3,ROW(R!$A$2:$A$70)),ROWS($1:1))),"")',  # end of list
        '=IFERROR(LOOKUP(1,0/COUNTIFS(O5:AA5,O$1),{1,0,-1}),"")',
        "=IFERROR(SUM(A1:A5),0)",
    ],
)
def test_deliberate_wrappers_are_left_alone(formula):
    assert masks(formula) == []


def test_google_sheets_placeholders_are_always_reported():
    [mask] = masks('=IFERROR(__xludf.DUMMYFUNCTION("""COMPUTED_VALUE"""),"60*90")')
    assert mask.sources == ("a Google Sheets placeholder",)
    assert mask.fallback == '"60*90"'


def test_each_wrapper_in_a_formula_is_judged_on_its_own():
    formula = '=IFERROR(A1/B1,0)+IFERROR(VLOOKUP(C1,D:E,2,FALSE),"")'
    assert [(m.function, m.sources) for m in masks(formula)] == [("IFERROR", ("a division",))]
