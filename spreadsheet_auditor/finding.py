from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from .locations import split_location


SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}


@dataclass
class Finding:
    rule_id: str
    severity: str
    error_confidence: str
    detection_mode: str
    location: str
    title: str
    evidence: list[str]
    suggested_fix: str
    formula: str | None = None
    impact: dict[str, Any] = field(default_factory=dict)
    limitations: list[str] = field(default_factory=list)
    suppressed: bool = False
    id: str = ""
    #: Every cell the finding stands for, its location first, when it reports
    #: a mistake repeated in several cells (a formula filled down a column, a
    #: list of repeated keys). Empty means the cells of ``location``.
    members: list[str] = field(default_factory=list)
    #: What the flagged cell holds, set by
    #: :func:`spreadsheet_auditor.identity.assign_identities`; the fingerprint
    #: hashes it instead of the location when present.
    identity: str | None = field(default=None, repr=False, compare=False)
    #: Extra text a check adds to the identity when the cell alone does not
    #: say what the finding is about (the repeated keys of a lookup list).
    identity_hint: str | None = field(default=None, repr=False, compare=False)
    #: True when another finding of the rule has the same identity apart from
    #: its place in sheet order; a pinned suppression must then also match the
    #: finding's address.
    identity_shared: bool = field(default=False, repr=False, compare=False)

    def covered(self) -> list[str]:
        """The locations this finding stands for: its members, or the pieces of its location."""
        return list(self.members) if self.members else split_location(self.location)

    @property
    def fingerprint(self) -> str:
        """Stable hash used for suppressions and cross-run diffs.

        An audit hashes the rule with the flagged cell's content (see
        ``identity``), so the fingerprint follows the cell through inserted
        rows and columns and never passes to whatever lands on its old
        address. A finding built without a workbook (a unit test, a custom
        caller, a CSV row) hashes (rule_id, normalized location) instead;
        "Sheet1!B2:B10" and " sheet1 ! B2 : B10 " hash alike.
        """
        basis = self.identity if self.identity is not None else _normalize_location(self.location)
        digest = hashlib.sha256(f"{self.rule_id}|{basis}".encode("utf-8")).hexdigest()
        return digest[:16]

    @property
    def sheet(self) -> str | None:
        return _parse_sheet(self.location)

    @property
    def cell(self) -> str | None:
        return _parse_cell(self.location)

    @property
    def range(self) -> str | None:  # noqa: A003 - intentional name
        return _parse_range(self.location)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "fingerprint": self.fingerprint,
            "rule_id": self.rule_id,
            "severity": self.severity,
            "error_confidence": self.error_confidence,
            # Aliases per PRD: external consumers may prefer the shorter names.
            "confidence": self.error_confidence,
            "detection_mode": self.detection_mode,
            "mode": self.detection_mode,
            "location": self.location,
            "members": self.covered(),
            "sheet": self.sheet,
            "cell": self.cell,
            "range": self.range,
            "title": self.title,
            "formula": self.formula,
            "evidence": self.evidence,
            "impact": self.impact,
            "limitations": list(self.limitations),
            "suggested_fix": self.suggested_fix,
            "suppressed": self.suppressed,
        }


_RANGE_RE = re.compile(r"^\$?[A-Z]+\$?\d+:\$?[A-Z]+\$?\d+$")
_CELL_RE = re.compile(r"^\$?[A-Z]+\$?\d+$")


def _normalize_location(location: str) -> str:
    if not location:
        return ""
    parts = [part.strip() for part in location.split(",")]
    return ",".join(part.replace(" ", "").upper() for part in parts)


def _primary(location: str) -> tuple[str, str] | None:
    """(sheet, address) of the first piece; sheet names may hold commas or ``!``."""
    pieces = split_location(location)
    if not pieces or "!" not in pieces[0]:
        return None
    sheet, addr = pieces[0].rsplit("!", 1)
    return sheet.strip(), addr.strip()


def _parse_sheet(location: str) -> str | None:
    primary = _primary(location)
    return primary[0] if primary else None


def _parse_cell(location: str) -> str | None:
    primary = _primary(location)
    if primary and _CELL_RE.match(primary[1].upper()):
        return primary[1]
    return None


def _parse_range(location: str) -> str | None:
    primary = _primary(location)
    if primary and _RANGE_RE.match(primary[1].upper()):
        return primary[1]
    return None


def assign_ids(findings: list[Finding]) -> list[Finding]:
    counts: dict[str, int] = {}
    for finding in sorted(findings, key=lambda f: (SEVERITY_ORDER.get(f.severity, 99), f.rule_id, f.location)):
        counts[finding.rule_id] = counts.get(finding.rule_id, 0) + 1
        finding.id = f"{finding.rule_id}-{counts[finding.rule_id]:03d}"
    return findings


def sort_findings(findings: list[Finding]) -> list[Finding]:
    return sorted(
        findings,
        key=lambda f: (
            SEVERITY_ORDER.get(f.severity, 99),
            f.suppressed,
            f.rule_id,
            f.location,
        ),
    )
