"""Which IFERROR and IFNA wrappers hide an error behind a value that reads as data.

Most wrappers on real workbooks are deliberate: ``IFERROR(VLOOKUP(...), "")``
blanks a lookup miss, an end-of-list extraction returns ``""`` when the rows run
out, a chain of lookups tries one list after another, and a wrapper around
``COUNTIFS`` or an ``IF`` that already handles its cases hides nothing. What
deserves a reviewer's eye is narrower: an expression that can really fail (a
division, a lookup, an average, a date or text conversion) whose error is
replaced by something a reader or a total takes as a real value, such as ``0``,
``"0"``, a cell, or a calculation.

An error only counts when it can reach the wrapper: ``IFNA`` catches nothing
but ``#N/A`` (a lookup miss), and an error that an ``ISNUMBER`` or an inner
``IFERROR`` already turns into a value never gets that far.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from openpyxl.formula.tokenizer import Token

from .formula_parser import tokens

# Functions that return an error in ordinary use: lookups that miss, averages
# and ratios of nothing, conversions of text, date arithmetic, and so on.
FAILING_FUNCTIONS = {
    "VLOOKUP", "HLOOKUP", "LOOKUP", "MATCH", "XLOOKUP", "XMATCH", "INDEX", "INDIRECT", "OFFSET",
    "GETPIVOTDATA", "FILTER", "SORTBY", "TEXTBEFORE", "TEXTAFTER",
    "AVERAGE", "AVERAGEA", "AVERAGEIF", "AVERAGEIFS", "TRIMMEAN", "MEDIAN", "MODE", "MODE.SNGL", "GEOMEAN", "HARMEAN",
    "STDEV", "STDEV.S", "STDEV.P", "STDEVP", "STDEVA", "STDEVPA", "VAR", "VAR.S", "VAR.P", "VARP", "VARA", "VARPA",
    "SLOPE", "INTERCEPT", "CORREL", "PEARSON", "RSQ", "FORECAST", "FORECAST.LINEAR",
    "PERCENTILE", "PERCENTILE.INC", "PERCENTILE.EXC", "QUARTILE", "QUARTILE.INC", "QUARTILE.EXC", "RANK", "RANK.EQ",
    "RANK.AVG", "SMALL", "LARGE", "MOD", "QUOTIENT", "SQRT", "LN", "LOG", "LOG10", "POWER",
    "VALUE", "NUMBERVALUE", "DATEVALUE", "TIMEVALUE", "FIND", "SEARCH", "DATEDIF", "EDATE", "EOMONTH",
    "WORKDAY", "NETWORKDAYS", "IRR", "XIRR", "RATE", "NPER", "__XLUDF.DUMMYFUNCTION",
}
# SUBTOTAL and AGGREGATE fail only for the function numbers whose function can
# (an average of nothing is #DIV/0!, SMALL past the last value is #NUM!), not
# for a sum, count, max, min or product.
FAILING_FUNCTION_NUMBERS = {
    "SUBTOTAL": {"1", "7", "8", "10", "11", "101", "107", "108", "110", "111"},
    "AGGREGATE": {"1", "7", "8", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"},
}
PLACEHOLDER = "a Google Sheets placeholder"
# IFNA catches only #N/A: a lookup that misses, a text split that finds no delimiter, NA().
NA_SOURCES = {
    "VLOOKUP", "HLOOKUP", "LOOKUP", "MATCH", "XLOOKUP", "XMATCH", "TEXTBEFORE", "TEXTAFTER", "#N/A", "NA()",
    PLACEHOLDER,
}
# An error inside one of these never reaches the wrapper: ISNUMBER(MATCH(...))
# is TRUE or FALSE. ISEVEN and ISODD are not among them; they pass an error on.
ABSORBING = {
    "ISNUMBER", "ISERROR", "ISERR", "ISNA", "ISTEXT", "ISBLANK", "ISLOGICAL", "ISNONTEXT", "ISREF", "ISFORMULA",
    "ERROR.TYPE",
}
# Conversions of text; when one fails, keeping the text it read is deliberate.
CONVERSIONS = {"FIND", "SEARCH", "VALUE", "NUMBERVALUE", "DATEVALUE", "TIMEVALUE"}
# A fallback that is itself a lookup or another wrapper tries a second source.
FALLBACK_LOOKUPS = {
    "VLOOKUP", "HLOOKUP", "LOOKUP", "INDEX", "MATCH", "XLOOKUP", "XMATCH", "INDIRECT", "OFFSET", "FILTER",
    "IFERROR", "IFNA", "NA",
}
# A fallback that joins text, like "Missing: "&C1, is a message.
TEXT_JOINS = {"CONCATENATE", "CONCAT", "TEXTJOIN"}
# A wrapped expression that is itself a conditional already handles its cases.
CONDITIONALS = {"IF", "IFS", "SWITCH"}
WRAPPERS = {"IFERROR", "IFNA"}

_BRACKETS = (Token.FUNC, Token.PAREN, Token.ARRAY)
# Text Excel reads as a number in arithmetic: "0", "1.5", "1,000", "$0", "0%", "1E3".
_NUMBER_TEXT_RE = re.compile(r"\$?(?:(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?%?")


@dataclass(frozen=True)
class Mask:
    """One wrapper that replaces a possible error with a value that reads as data."""

    function: str  # IFERROR or IFNA
    sources: tuple[str, ...]  # what can fail inside it, e.g. ("VLOOKUP",) or ("division",)
    fallback: str  # the replacement, as written


def _name(value: str) -> str:
    # The tokenizer glues a range start to a call in ``A1:OFFSET(...)``; the name follows the colon.
    name = value.rstrip("(").rsplit(":", 1)[-1].upper()
    for prefix in ("_XLFN._XLWS.", "_XLFN.", "_XLWS."):
        name = name.removeprefix(prefix)
    return name


def _arguments(toks: list, open_index: int) -> list[list]:
    """The top-level arguments of the function call opening at ``open_index``."""
    args: list[list] = [[]]
    depth = 0
    for tok in toks[open_index + 1:]:
        _value, ttype, subtype = tok
        if ttype in _BRACKETS and subtype == Token.OPEN:
            depth += 1
        elif ttype in _BRACKETS and subtype == Token.CLOSE:
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


def _whole_call(toks: list) -> str | None:
    """The function's name when the whole expression is one call, such as ``IF(...)``."""
    toks = _meaningful(toks)
    if not toks or toks[0][1] != Token.FUNC or toks[0][2] != Token.OPEN:
        return None
    depth = 0
    for index, (_value, ttype, subtype) in enumerate(toks):
        if ttype in _BRACKETS and subtype == Token.OPEN:
            depth += 1
        elif ttype in _BRACKETS and subtype == Token.CLOSE:
            depth -= 1
            if depth == 0:
                return _name(toks[0][0]) if index == len(toks) - 1 else None
    return None


def _is_conditional(toks: list) -> bool:
    """True when the whole expression is one IF, IFS or SWITCH call."""
    return _whole_call(toks) in CONDITIONALS


def _can_fail(toks: list, index: int) -> bool:
    """True when the call opening at ``toks[index]`` returns an error in ordinary use."""
    name = _name(toks[index][0])
    if name in FAILING_FUNCTIONS:
        return True
    numbers = FAILING_FUNCTION_NUMBERS.get(name)
    if numbers is None:
        return False
    # SUBTOTAL(101,...): the function number is the first argument.
    following = toks[index + 1:index + 3]
    return (
        len(following) == 2
        and following[0][1] == Token.OPERAND
        and following[0][2] == Token.NUMBER
        and following[0][0] in numbers
        and following[1][1] == Token.SEP
    )


def _is_cell(toks: list, index: int, step: int) -> bool:
    """True when the operand before (``step=-1``) or after (``step=1``) ``toks[index]`` is a cell: ``A1`` or ``(A1)``."""
    inner, outer = (Token.CLOSE, Token.OPEN) if step < 0 else (Token.OPEN, Token.CLOSE)
    j, depth = index + step, 0
    while 0 <= j < len(toks) and toks[j][1] == Token.PAREN and toks[j][2] == inner:
        j, depth = j + step, depth + 1
    if not (0 <= j < len(toks) and toks[j][1] == Token.OPERAND and toks[j][2] == Token.RANGE):
        return False
    return all(
        0 <= k < len(toks) and toks[k][1] == Token.PAREN and toks[k][2] == outer
        for k in range(j + step, j + step * (depth + 1), step)
    )


def _absorbed(calls: list[list], source: str) -> bool:
    """True when an enclosing call turns the error from ``source`` into a value before the wrapper sees it."""
    for name, argument in calls:
        if name in ABSORBING:
            return True
        if argument == 0 and (name == "IFERROR" or (name == "IFNA" and source in NA_SOURCES)):
            return True
    return False


def _sources(toks: list, na_only: bool = False) -> tuple[str, ...]:
    """What inside the wrapped expression can produce an error that reaches the wrapper.

    ``na_only`` keeps only what returns #N/A, the one error IFNA catches.
    """
    found: list[str] = []
    toks = _meaningful(toks)
    calls: list[list] = []  # enclosing calls and brackets, innermost last: [name, argument index]
    for index, (value, ttype, subtype) in enumerate(toks):
        source = None
        if ttype == Token.FUNC and subtype == Token.OPEN and _can_fail(toks, index):
            source = _name(value).replace("__XLUDF.DUMMYFUNCTION", PLACEHOLDER)
        elif ttype == Token.FUNC and subtype == Token.OPEN and _name(value) == "NA":
            source = "NA()"  # IFERROR(VLOOKUP(...),NA()) passes the miss on as #N/A
        elif ttype == Token.OPERAND and subtype == Token.ERROR:
            source = value.upper()
        elif ttype == Token.OP_IN and value == "/":
            source = "a division"
        elif ttype == Token.OP_IN and value == "^":
            source = "a power"
        elif ttype == Token.OP_IN and value in ("+", "-", "*"):
            # Arithmetic fails when a cell it reads holds text.
            if _is_cell(toks, index, -1) or _is_cell(toks, index, 1):
                source = "arithmetic on a cell"
        elif ttype == Token.OP_PRE and value == "-" and _is_cell(toks, index, 1):
            source = "arithmetic on a cell"  # -A1 fails on text as A1*1 does
        if source and (not na_only or source in NA_SOURCES) and not _absorbed(calls, source):
            found.append(source)
        if ttype in _BRACKETS and subtype == Token.OPEN:
            calls.append([_name(value) if ttype == Token.FUNC else "", 0])
        elif ttype in _BRACKETS and subtype == Token.CLOSE and calls:
            calls.pop()
        elif ttype == Token.SEP and subtype == Token.ARG and calls:
            calls[-1][1] += 1
    return tuple(dict.fromkeys(found))


def _is_number_text(text: str) -> bool:
    """True for text Excel reads as a number in arithmetic: "0", "-1,000", "$0", "0%", "(1)"."""
    text = text.strip(" ")
    if text.startswith("(") and text.endswith(")"):
        text = text[1:-1]  # (1), the accounting form of -1
    elif text[:1] in ("-", "+"):
        text = text[1:]
    return _NUMBER_TEXT_RE.fullmatch(text) is not None


def _joins_text(toks: list) -> bool:
    """True when the expression's outermost operation is ``&``, as in ``"Missing: "&C1``."""
    depth = 0
    for value, ttype, subtype in toks:
        if ttype in _BRACKETS and subtype == Token.OPEN:
            depth += 1
        elif ttype in _BRACKETS and subtype == Token.CLOSE:
            depth -= 1
        elif depth == 0 and ttype == Token.OP_IN and value == "&":
            return True
    return False


def _reads_as_data(toks: list) -> bool:
    """True when the fallback is something a reader or a total takes as a real value."""
    toks = _meaningful(toks)
    if not toks:
        return True  # IFERROR(x,) returns 0
    if len(toks) == 1:
        value, ttype, subtype = toks[0]
        if ttype == Token.OPERAND and subtype == Token.TEXT:
            # "0" is a number written as text; "" or a message such as "n/a" or "Select freq" says there is no value.
            return _is_number_text(value[1:-1].replace('""', '"'))
        # A number, TRUE/FALSE, or a cell reads as data; an error value is not a mask.
        return not (ttype == Token.OPERAND and subtype == Token.ERROR)
    # A calculation reads as data; a second lookup, another wrapper, NA(), or a message built from text does not.
    first_value, first_type, first_subtype = toks[0]
    if first_type == Token.FUNC and first_subtype == Token.OPEN and _name(first_value) in FALLBACK_LOOKUPS:
        return False
    return not (_whole_call(toks) in TEXT_JOINS or _joins_text(toks))


def _falls_back_to_input(wrapped: list, fallback: list, sources: tuple[str, ...]) -> bool:
    """True for ``IFERROR(VALUE(A1),A1)``: convert the text when it converts, keep it as it is when not."""
    fallback = _meaningful(fallback)
    if not set(sources) <= CONVERSIONS or len(fallback) != 1:
        return False
    value, ttype, subtype = fallback[0]
    if ttype != Token.OPERAND or subtype != Token.RANGE or ":" in value:
        return False
    read = {tok[0].replace("$", "").upper() for tok in wrapped if tok[1] == Token.OPERAND and tok[2] == Token.RANGE}
    return value.replace("$", "").upper() in read


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
        function = _name(value)
        args = _arguments(toks, index)
        wrapped, fallback = args[0], (args[1] if len(args) > 1 else [])
        sources = _sources(wrapped, na_only=function == "IFNA")
        fallback_text = "".join(tok[0] for tok in fallback).strip() or "0"
        if PLACEHOLDER in sources:
            found.append(Mask(function, (PLACEHOLDER,), fallback_text))
            continue
        if (
            not sources
            or _is_conditional(wrapped)
            or not _reads_as_data(fallback)
            or _falls_back_to_input(wrapped, fallback, sources)
        ):
            continue
        found.append(Mask(function, sources, fallback_text))
    return found
