from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "scope": {},
    "checks": {},
    "limits": {
        "max_formulas": 50000,
        "max_reported_findings": 200,
    },
    "recalc": {
        "enabled": True,
        "timeout_seconds": 60,
    },
    "suppressions": [],
}

CHECK_KEY_TO_RULE_ID = {
    "live_errors": "LIVE_ERROR",
    "formula_drift": "FORMULA_DRIFT",
    "range_exclusion": "RANGE_EXCLUSION",
    "range_includes_subtotal": "RANGE_INCLUDES_SUBTOTAL",
    "literal_constants": "LITERAL_CONSTANT",
    "hidden_rows_in_totals": "HIDDEN_STRUCTURE_IN_TOTAL",
    "hidden_structure_in_total": "HIDDEN_STRUCTURE_IN_TOTAL",
    "color_conventions": "COLOR_CONVENTION",
    "hardcode_in_formula_block": "HARDCODE_IN_FORMULA_BLOCK",
    "numbers_stored_as_text": "NUMBERS_STORED_AS_TEXT",
    "whitespace_key": "WHITESPACE_KEY",
    "iferror_mask": "IFERROR_MASK",
    "broken_reference": "BROKEN_REFERENCE",
    "blank_precedent": "BLANK_PRECEDENT",
    "total_mismatch": "TOTAL_MISMATCH",
    "circular_reference": "CIRCULAR_REFERENCE",
    "fragile_function": "FRAGILE_FUNCTION",
}


def load_config(path: str | None) -> dict[str, Any]:
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path:
        return config

    config_path = Path(path)
    if not config_path.exists():
        raise ValueError(f"Config file does not exist: {config_path}")

    suffix = config_path.suffix.lower()
    if suffix == ".json":
        loaded = json.loads(config_path.read_text(encoding="utf-8"))
    elif suffix in {".yml", ".yaml"}:
        loaded = _load_yaml(config_path)
    else:
        raise ValueError("Config must be .json, .yml, or .yaml")

    if not isinstance(loaded, dict):
        raise ValueError("Config root must be an object")
    _merge_dict(config, loaded)
    return config


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except Exception as exc:
        raise ValueError(
            "YAML config requires PyYAML in this runtime. Use JSON config or install PyYAML before running this script."
        ) from exc
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data or {}


def _merge_dict(base: dict[str, Any], update: dict[str, Any]) -> None:
    for key, value in update.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _merge_dict(base[key], value)
        else:
            base[key] = value


def allowed_sheets(config: dict[str, Any]) -> tuple[set[str] | None, set[str]]:
    scope = config.get("scope") or {}
    include = scope.get("include_sheets")
    exclude = scope.get("exclude_sheets") or []
    include_set = set(include) if include else None
    return include_set, set(exclude)


def sheet_is_allowed(sheet_name: str, include: set[str] | None, exclude: set[str]) -> bool:
    if include is not None and sheet_name not in include:
        return False
    return sheet_name not in exclude


def check_setting(config: dict[str, Any], rule_id: str) -> str:
    checks = config.get("checks") or {}
    reverse = {rule: key for key, rule in CHECK_KEY_TO_RULE_ID.items()}
    key = reverse.get(rule_id, rule_id.lower())
    value = checks.get(key, checks.get(rule_id, "error"))
    if isinstance(value, bool):
        return "error" if value else "off"
    return str(value).lower()


def apply_check_settings(findings, config: dict[str, Any]):
    kept = []
    for finding in findings:
        setting = check_setting(config, finding.rule_id)
        if setting in {"off", "false", "disabled", "disable"}:
            continue
        if setting in {"warn", "warning", "review"} and finding.severity in {"Critical", "High"}:
            finding.severity = "Medium"
            finding.error_confidence = "Review"
        kept.append(finding)
    return kept
