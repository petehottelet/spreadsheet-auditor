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

A reason is required for every suppression. Suppressions missing a reason (or
otherwise malformed) are dropped and a note is appended to the optional
``warnings`` list passed by the caller, which surfaces in the report's
``coverage.limitations`` so an ignored suppression is never silent.

Suppressed findings remain in the JSON payload (with `suppressed: true`) so
they can be audited, but the Markdown/HTML reports hide them by default and
require `--show-suppressed` to surface them.
"""

from __future__ import annotations

from pathlib import Path


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
        for entry in config.get("suppressions", []) or []:
            if not isinstance(entry, dict):
                warn(f"Suppression ignored (not a mapping): {entry!r}")
                continue
            if not entry.get("reason"):
                warn(f"Suppression ignored (missing required 'reason'): {entry!r}")
                continue
            suppressions.append(entry)
    if ignore_path and Path(ignore_path).exists():
        for line_no, raw in enumerate(
            Path(ignore_path).read_text(encoding="utf-8").splitlines(), start=1
        ):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            entry = _parse_ignore_line(line)
            if entry is not None:
                suppressions.append(entry)
            else:
                warn(
                    f"Suppression ignored ({ignore_path}:{line_no}); expected "
                    f"'<rule_id> <range> <reason>' or 'fingerprint:<fp> <reason>': {line!r}"
                )
    return suppressions


def _parse_ignore_line(line: str) -> dict | None:
    if line.lower().startswith("fingerprint:"):
        # `fingerprint:<fp> <reason>`
        body = line.split(":", 1)[1].strip()
        parts = body.split(None, 1)
        if len(parts) < 2:
            return None
        return {"fingerprint": parts[0].lower(), "reason": parts[1]}
    parts = line.split(None, 2)
    if len(parts) < 3:
        return None  # rule_id + range + reason are all required
    rule_id, target, reason = parts
    return {"rule_id": rule_id, "range": target, "reason": reason}


def apply_suppressions(findings, suppressions: list[dict]):
    if not suppressions:
        return findings
    for finding in findings:
        for suppression in suppressions:
            if _matches(finding, suppression):
                finding.suppressed = True
                finding.impact["suppression_reason"] = suppression.get("reason", "")
                break
    return findings


def _matches(finding, suppression: dict) -> bool:
    fp = suppression.get("fingerprint")
    if fp:
        return str(fp).lower() == finding.fingerprint.lower()
    if suppression.get("rule_id") != finding.rule_id:
        return False
    target = str(suppression.get("range", ""))
    if not target:
        return False
    return (
        finding.location == target
        or finding.location.startswith(target)
        or target in finding.location
    )
