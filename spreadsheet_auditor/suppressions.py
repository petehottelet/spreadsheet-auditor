"""Finding suppression logic.

Suppressions can be supplied two ways:

1. **Suppression file** (default `.audit-ignore`). One suppression per line, in
   one of two grammars:

       <rule_id>  <range_or_location>  <reason>
       fingerprint:<fp> <reason>

   Lines starting with `#` are comments. A reason is required for every
   suppression; suppressions missing a reason are dropped with a warning.

2. **Config section** (`[suppressions]`). A list of `{rule_id, range, reason}`
   or `{fingerprint, reason}` mappings. Same semantics as the file.

A suppression's `range` may be a single cell (`Budget!B14`), a range
(`Imports!A1:A100`), a whole column or row (`Imports!A:A`), or a bare sheet
name (`Imports`). A finding is suppressed when its cell or range lies inside
that target on the same sheet; a multi-cell finding matches when any of its
cells does. Sheet names are case-insensitive and `$` markers are ignored.
Nothing is matched by substring, so `Imports!A1` never hides `Imports!A10`.
A target without `!` is always a sheet, even `Q1` or `FY2025`. In the file,
quote a sheet name that contains spaces: `'Revenue Detail'!B1`.

To accept one finding, suppress its fingerprint: it is built from the flagged
cell's content, so it follows the cell through inserted rows and columns. A
location target follows the address instead, which suits an area (a raw-data
sheet, an import range) but lets a one-cell target hide whatever later lands
on that cell.

A reason is required for every suppression. Suppressions missing a reason (or
otherwise malformed) are dropped and a note is appended to the optional
``warnings`` list passed by the caller, which surfaces in the report's
``coverage.limitations`` so an ignored suppression is never silent. So is a
suppression that matches no finding (see :func:`unmatched_suppressions`):
the finding was fixed, or the cells moved and the target is stale.

Suppressed findings remain in the JSON payload (with `suppressed: true`) so
they can be audited, but the Markdown/HTML reports hide them by default and
require `--show-suppressed` to surface them.
"""

from __future__ import annotations

from pathlib import Path

from .locations import location_matches


def load_suppressions(
    config: dict | None = None,
    ignore_path: str | None = None,
    warnings: list[str] | None = None,
) -> list[dict]:
    def warn(message: str) -> None:
        if warnings is not None:
            warnings.append(message)

    suppressions: list[dict] = []
    if config:
        for index, entry in enumerate(config.get("suppressions", []) or []):
            if not isinstance(entry, dict):
                warn(f"Suppression ignored (not a mapping): {entry!r}")
                continue
            if not entry.get("reason"):
                warn(f"Suppression ignored (missing required 'reason'): {entry!r}")
                continue
            # A copy: apply_suppressions counts matches on the entry.
            suppressions.append(dict(entry, source=f"config suppressions[{index}]"))
    if ignore_path and Path(ignore_path).exists():
        for line_no, raw in enumerate(
            Path(ignore_path).read_text(encoding="utf-8").splitlines(), start=1
        ):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            entry, problem = _parse_ignore_line(line)
            if entry is not None:
                suppressions.append(dict(entry, source=f"{ignore_path}:{line_no}"))
            else:
                warn(f"Suppression ignored ({ignore_path}:{line_no}); {problem}: {line!r}")
    return suppressions


_EXPECTED = "expected '<rule_id> <range> <reason>' or 'fingerprint:<fp> <reason>'"


def _parse_ignore_line(line: str) -> tuple[dict | None, str | None]:
    """Parse one `.audit-ignore` line into a suppression, or say what is wrong with it."""
    if line.lower().startswith("fingerprint:"):
        # `fingerprint:<fp> <reason>`
        body = line.split(":", 1)[1].strip()
        parts = body.split(None, 1)
        if len(parts) < 2:
            return None, _EXPECTED
        return {"fingerprint": parts[0].lower(), "reason": parts[1]}, None
    parts = line.split(None, 1)
    if len(parts) < 2:
        return None, _EXPECTED
    rule_id, rest = parts
    target, reason = _take_target(rest)
    if target is None:
        return None, "unterminated quote in the sheet name"
    if not reason:
        return None, _EXPECTED  # rule_id + range + reason are all required
    first_word = reason.split(None, 1)[0]
    if "!" not in target and "!" in first_word:
        # `Revenue Detail!B1` split at the space would suppress the whole
        # sheet `Revenue` (or nothing) and file the address under the reason.
        tail, address = first_word.rsplit("!", 1)
        return None, f"quote a sheet name that contains spaces, as in '{target} {tail}'!{address}"
    return {"rule_id": rule_id, "range": target, "reason": reason}, None


def _take_target(text: str) -> tuple[str | None, str]:
    """Split ``text`` into its first target and the rest.

    A target that opens with a single quote runs to the closing quote and
    then to the next whitespace, so ``'Revenue Detail'!B1 approved`` yields
    ``'Revenue Detail'!B1``; inside the quotes ``''`` is a literal apostrophe,
    as in Excel. Any other target ends at the first whitespace. ``None`` when
    the quote is never closed.
    """
    index = 0
    if text.startswith("'"):
        index = 1
        while True:
            close = text.find("'", index)
            if close < 0:
                return None, ""
            if text[close + 1 : close + 2] == "'":
                index = close + 2
                continue
            index = close + 1
            break
    while index < len(text) and not text[index].isspace():
        index += 1
    return text[:index], text[index:].strip()


def apply_suppressions(findings, suppressions: list[dict]):
    """Mark findings covered by a suppression, and count each suppression's matches.

    A finding takes the reason of the first suppression that covers it; every
    covering suppression counts the match, so none is reported as unused just
    because an earlier one covered the same finding.
    """
    if not suppressions:
        return findings
    for finding in findings:
        for suppression in suppressions:
            if _matches(finding, suppression):
                if not finding.suppressed:
                    finding.suppressed = True
                    finding.impact["suppression_reason"] = suppression.get("reason", "")
                suppression["matched"] = suppression.get("matched", 0) + 1
    return findings


def unmatched_suppressions(suppressions: list[dict]) -> list[dict]:
    """Suppressions that covered no finding in the last :func:`apply_suppressions` call."""
    return [suppression for suppression in suppressions if not suppression.get("matched")]


def describe(suppression: dict) -> str:
    if suppression.get("fingerprint"):
        return f"fingerprint:{suppression['fingerprint']}"
    return f"{suppression.get('rule_id')} {suppression.get('range')}"


def _matches(finding, suppression: dict) -> bool:
    fp = suppression.get("fingerprint")
    if fp:
        return str(fp).lower() == finding.fingerprint.lower()
    if suppression.get("rule_id") != finding.rule_id:
        return False
    target = str(suppression.get("range", "") or "").strip()
    if not target:
        return False
    return location_matches(finding.location, target)
