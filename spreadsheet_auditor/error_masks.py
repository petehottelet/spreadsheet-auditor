"""Which IFERROR and IFNA wrappers hide an error behind a value that reads as data.

Most wrappers on real workbooks are deliberate: ``IFERROR(VLOOKUP(...), "")``
blanks a lookup miss, an end-of-list extraction returns ``""`` when the rows run
out, a chain of lookups tries one list after another, and a wrapper around
``COUNTIFS`` or an ``IF`` that already handles its cases hides nothing. What
deserves a reviewer's eye is narrower: an expression that can really fail (a
division, a lookup, an average, a date or text conversion) whose error is
replaced by something a reader or a total takes as a real value, such as ``0``,
``"0"``, a cell, or a calculation.
"""

from __future__ import annotations

from dataclasses import dataclass

from openpyxl.formula.tokenizer import Token

from .formula_parser import tokens

# Functions that return an error in ordinary use: lookups that miss, averages
# and ratios of nothing, conversions of text, date arithmetic, and so on.
FAILING_FUNCTIONS = {
    "VLOOKUP", "HLOOKUP", "LOOKUP", "MATCH", "XLOOKUP", "XMATCH", "INDEX", "INDIRECT", "OFFSET",
    "GETPIVOTDATA", "FILTER", "SORTBY",
    "AVERAGE", "AVERAGEA", "AVERAGEIF", "AVERAGEIFS", "TRIMMEAN", "MEDIAN", "MODE", "GEOMEAN", "HARMEAN",
    "STDEV", "STDEV.S", "STDEV.P", "STDEVA", "VAR", "VAR.S", "VAR.P", "PERCENTILE", "PERCENTILE.INC",
    "PERCENTILE.EXC", "QUARTILE", "QUARTILE.INC", "QUARTILE.EXC", "RANK", "RANK.EQ", "RANK.AVG",
    "SMALL", "LARGE", "AGGREGATE", "MOD", "QUOTIENT", "SQRT", "LN", "LOG", "LOG10", "POWER",
    "VALUE", "NUMBERVALUE", "DATEVALUE", "TIMEVALUE", "FIND", "SEARCH", "DATEDIF", "EDATE", "EOMONTH",
    "WORKDAY", "NETWORKDAYS", "IRR", "XIRR", "RATE", "NPER", "__XLUDF.DUMMYFUNCTION",
}
# A fallback that is itself a lookup or another wrapper tries a second source.
FALLBACK_LOOKUPS = {"VLOOKUP", "HLOOKUP", "LOOKUP", "INDEX", "MATCH", "XLOOKUP", "IFERROR", "IFNA", "NA"}
# A wrapped expression that is itself a conditional already handles its cases.
CONDITIONALS = {"IF", "IFS", "SWITCH"}
WRAPPERS = {"IFERROR", "IFNA"}


@dataclass(frozen=True)
class Mask:
    """One wrapper that replaces a possible error with a value that reads as data."""

    function: str  # IFERROR or IFNA
    sources: tuple[str, ...]  # what can fail inside it, e.g. ("VLOOKUP",) or ("division",)
    fallback: str  # the replacement, as written


def _name(value: str) -> str:
    name = value.rstrip("(").upper()
    for prefix in ("_XLFN._XLWS.", "_XLFN.", "_XLWS."):
        name = name.removeprefix(prefix)
    return name


def _arguments(toks: list, open_index: int) -> list[list]:
    """The top-level arguments of the function call opening at ``open_index``."""
    args: list[list] = [[]]
    depth = 0
    for tok in toks[open_index + 1:]:
        _value, ttype, subtype = tok
        if ttype in (Token.FUNC, Token.PAREN) and subtype == Token.OPEN:
            depth += 1
        elif ttype in (Token.FUNC, Token.PAREN) and subtype == Token.CLOSE:
            if depth == 0:
                return args
            depth -= 1
        elif ttype == Token.SEP and subtype == Token.ARG and depth == 0:
            args.append([])
            continue
        args[-1].append(tok)
    return args


def _meaningful(toks: list) -> list:
    return [tok for tok in toks if tok[1] != Token.WSPACE]


def _is_conditional(toks: list) -> bool:
    """True when the whole expression is one IF, IFS or SWITCH call."""
    toks = _meaningful(toks)
    if not toks or toks[0][1] != Token.FUNC or toks[0][2] != Token.OPEN or _name(toks[0][0]) not in CONDITIONALS:
        return False
    depth = 0
    for index, (_value, ttype, subtype) in enumerate(toks):
        if ttype in (Token.FUNC, Token.PAREN) and subtype == Token.OPEN:
            depth += 1
        elif ttype in (Token.FUNC, Token.PAREN) and subtype == Token.CLOSE:
            depth -= 1
            if depth == 0:
                return index == len(toks) - 1
    return False


def _sources(toks: list) -> tuple[str, ...]:
    """What inside the wrapped expression can produce an error."""
    found: list[str] = []
    toks = _meaningful(toks)
    for index, (value, ttype, subtype) in enumerate(toks):
        if ttype == Token.FUNC and subtype == Token.OPEN and _name(value) in FAILING_FUNCTIONS:
            found.append(_name(value).replace("__XLUDF.DUMMYFUNCTION", "a Google Sheets placeholder"))
        elif ttype == Token.OPERAND and subtype == Token.ERROR:
            found.append(value.upper())
        elif ttype == Token.OP_IN and value == "/":
            found.append("a division")
        elif ttype == Token.OP_IN and value == "^":
            found.append("a power")
        elif ttype == Token.OP_IN and value in "+-*":
            # Arithmetic fails when a cell it reads holds text.
            neighbours = [toks[i] for i in (index - 1, index + 1) if 0 <= i < len(toks)]
            if any(n[1] == Token.OPERAND and n[2] == Token.RANGE for n in neighbours):
                found.append("arithmetic on a cell")
    return tuple(dict.fromkeys(found))


def _reads_as_data(toks: list) -> bool:
    """True when the fallback is something a reader or a total takes as a real value."""
    toks = _meaningful(toks)
    if not toks:
        return True  # IFERROR(x,) returns 0
    if len(toks) == 1:
        value, ttype, subtype = toks[0]
        if ttype == Token.OPERAND and subtype == Token.TEXT:
            text = value[1:-1].replace('""', '"').strip()
            try:
                float(text.replace(",", ""))
                return True  # "0": a number written as text
            except ValueError:
                return False  # "" or a message such as "n/a" or "Select freq" says there is no value
        # A number, TRUE/FALSE, or a cell reads as data; an error value is not a mask.
        return not (ttype == Token.OPERAND and subtype == Token.ERROR)
    # A calculation reads as data; a second lookup, another wrapper, or NA() does not.
    first_value, first_type, first_subtype = toks[0]
    return not (first_type == Token.FUNC and first_subtype == Token.OPEN and _name(first_value) in FALLBACK_LOOKUPS)


def masks(formula: str) -> list[Mask]:
    """The IFERROR/IFNA calls in ``formula`` that hide a possible error behind a value that reads as data.

    Google Sheets exports formulas Excel lacks as
    ``IFERROR(__xludf.DUMMYFUNCTION(...), <cached value>)``; those cells are
    frozen values, so they are always reported.
    """
    toks = list(tokens(formula) or ())
    found: list[Mask] = []
    for index, (value, ttype, subtype) in enumerate(toks):
        if ttype != Token.FUNC or subtype != Token.OPEN or _name(value) not in WRAPPERS:
            continue
        args = _arguments(toks, index)
        wrapped, fallback = args[0], (args[1] if len(args) > 1 else [])
        sources = _sources(wrapped)
        fallback_text = "".join(tok[0] for tok in fallback).strip() or "0"
        if "a Google Sheets placeholder" in sources:
            found.append(Mask(_name(value), ("a Google Sheets placeholder",), fallback_text))
            continue
        if not sources or _is_conditional(wrapped) or not _reads_as_data(fallback):
            continue
        found.append(Mask(_name(value), sources, fallback_text))
    return found
