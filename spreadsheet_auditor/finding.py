from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any


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

    @property
    def fingerprint(self) -> str:
        """Stable hash over (rule_id, normalized location).

        Used for suppression matching and cross-run diffs. Locations like
        "Sheet1!B2:B10" and " sheet1 ! B2 : B10 " hash to the same value so
        whitespace and case differences in user-authored suppressions still
        bind to the right finding.
        """
        normalized = _normalize_location(self.location)
        digest = hashlib.sha256(f"{self.rule_id}|{normalized}".encode("utf-8")).hexdigest()
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


def _parse_sheet(location: str) -> str | None:
    if not location or "!" not in location:
        return None
    return location.split("!", 1)[0].strip()


def _parse_cell(location: str) -> str | None:
    if not location:
        return None
    primary = location.split(",", 1)[0]
    if "!" not in primary:
        return None
    addr = primary.split("!", 1)[1].strip()
    if _CELL_RE.match(addr.upper()):
        return addr
    return None


def _parse_range(location: str) -> str | None:
    if not location:
        return None
    primary = location.split(",", 1)[0]
    if "!" not in primary:
        return None
    addr = primary.split("!", 1)[1].strip()
    if _RANGE_RE.match(addr.upper()):
        return addr
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
