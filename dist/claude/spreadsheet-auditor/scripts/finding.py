from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


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
    suppressed: bool = False
    id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "rule_id": self.rule_id,
            "severity": self.severity,
            "error_confidence": self.error_confidence,
            "detection_mode": self.detection_mode,
            "location": self.location,
            "title": self.title,
            "formula": self.formula,
            "evidence": self.evidence,
            "impact": self.impact,
            "suggested_fix": self.suggested_fix,
            "suppressed": self.suppressed,
        }


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
