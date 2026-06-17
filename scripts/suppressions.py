from __future__ import annotations

import json
from pathlib import Path


def load_suppressions(config: dict | None = None, ignore_path: str | None = None) -> list[dict]:
    suppressions: list[dict] = []
    if config:
        suppressions.extend(config.get("suppressions", []))
    if ignore_path and Path(ignore_path).exists():
        for line in Path(ignore_path).read_text(encoding="utf-8").splitlines():
            text = line.strip()
            if not text or text.startswith("#"):
                continue
            parts = text.split(None, 2)
            if len(parts) >= 2:
                suppressions.append(
                    {
                        "rule_id": parts[0],
                        "range": parts[1],
                        "reason": parts[2] if len(parts) == 3 else "No reason provided",
                    }
                )
    return suppressions


def apply_suppressions(findings, suppressions: list[dict]):
    for finding in findings:
        for suppression in suppressions:
            if suppression.get("rule_id") != finding.rule_id:
                continue
            target = str(suppression.get("range", ""))
            if target and (finding.location == target or finding.location.startswith(target) or target in finding.location):
                finding.suppressed = True
                finding.impact["suppression_reason"] = suppression.get("reason", "")
    return findings
