from __future__ import annotations

import difflib
import json
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "scope": {},
    "checks": {},
    "limits": {
        "max_formulas": 50000,
        "max_reported_findings": 200,
        # Wall-clock budget for the check phase. Checks poll it cooperatively,
        # so a pathological workbook degrades to a partial report with a
        # limitation note instead of running for hours. 0 disables it.
        "timeout_seconds": 120,
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
    "range_length_mismatch": "RANGE_LENGTH_MISMATCH",
    "literal_constants": "LITERAL_CONSTANT",
    "hidden_rows_in_totals": "HIDDEN_STRUCTURE_IN_TOTAL",
    "hidden_structure_in_total": "HIDDEN_STRUCTURE_IN_TOTAL",
    "hardcode_in_formula_block": "HARDCODE_IN_FORMULA_BLOCK",
    "numbers_stored_as_text": "NUMBERS_STORED_AS_TEXT",
    "whitespace_key": "WHITESPACE_KEY",
    "duplicate_key": "DUPLICATE_KEY",
    "merged_cell": "MERGED_CELL_IN_DATA_RANGE",
    "merged_cell_in_data_range": "MERGED_CELL_IN_DATA_RANGE",
    "iferror_mask": "IFERROR_MASK",
    "broken_reference": "BROKEN_REFERENCE",
    "blank_precedent": "BLANK_PRECEDENT",
    "total_mismatch": "TOTAL_MISMATCH",
    "cross_foot_failure": "CROSS_FOOT_FAILURE",
    "circular_reference": "CIRCULAR_REFERENCE",
    "fragile_function": "VOLATILE_FUNCTION",
    "volatile_function": "VOLATILE_FUNCTION",
    "whole_column_reference": "WHOLE_COLUMN_REFERENCE",
}


class ConfigError(ValueError):
    """A config file that cannot be read, parsed, or used as written. The CLI exits 4."""


def load_config(path: str | None, known_rules: set[str] | None = None) -> dict[str, Any]:
    """The default config merged with the file at ``path``.

    With ``known_rules`` (the rule IDs the registered checks report), the file
    is also checked against the sections, settings, value types and rule names
    the auditor understands, so a typo stops the audit instead of being ignored.
    """
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    if not path:
        return config

    config_path = Path(path)
    if not config_path.is_file():
        raise ConfigError(f"Config file not found: {config_path}")
    suffix = config_path.suffix.lower()
    if suffix not in {".json", ".yml", ".yaml"}:
        raise ConfigError(f"Config file {config_path} must be .json, .yml or .yaml")
    try:
        text = config_path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ConfigError(f"Config file {config_path} is not UTF-8 text") from exc
    if suffix == ".json":
        try:
            loaded = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ConfigError(
                f"Config file {config_path} is not valid JSON: {exc.msg} at line {exc.lineno}, column {exc.colno}"
            ) from exc
    else:
        loaded = _load_yaml(config_path, text)

    if not isinstance(loaded, dict):
        raise ConfigError(f"Config file {config_path} must hold a mapping of sections such as checks and limits")
    if known_rules is not None:
        validate_config(loaded, known_rules)
    _merge_dict(config, loaded)
    return config


def _load_yaml(path: Path, text: str) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except Exception as exc:
        raise ConfigError(
            "YAML config requires PyYAML in this runtime. Use JSON config or install PyYAML before running this script."
        ) from exc
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ConfigError(f"Config file {path} is not valid YAML: {exc}") from exc
    return data or {}


# What each setting may hold. The same shapes are published in
# schemas/config.schema.json.
_TEXT, _TEXTS, _NUMBER, _COUNT, _POSITIVE, _FLAG = "text", "texts", "number", "count", "positive", "flag"
SECTIONS: dict[str, Any] = {
    "mode": _TEXT,
    "scope": {"include_sheets": _TEXTS, "exclude_sheets": _TEXTS, "headline_outputs": _TEXTS},
    "materiality": {"absolute": _NUMBER, "relative": _NUMBER, "percent_points": _NUMBER},
    "limits": {
        "max_cells": _COUNT,
        "max_formulas": _COUNT,
        "max_range_expansion_cells": _COUNT,
        "max_reported_findings": _COUNT,
        "timeout_seconds": _COUNT,
    },
    "recalc": {"enabled": _FLAG, "timeout_seconds": _POSITIVE},
    "finance": {"enabled": _FLAG},
    "checks": None,  # rule -> setting; checked against the known rules
    "suppressions": None,  # entries are checked, with warnings, by load_suppressions
}
CHECK_SETTINGS = {"error", "on", "true", "warn", "warning", "review", "off", "false", "disabled", "disable"}
_DESCRIPTIONS = {
    _TEXT: "text",
    _TEXTS: "a list of text values",
    _NUMBER: "a number",
    _COUNT: "a whole number of 0 or more",
    _POSITIVE: "a whole number of 1 or more",
    _FLAG: "true or false",
}


def _unknown(what: str, name: str, known) -> ConfigError:
    # Matched in any case, suggested as written in the auditor; a rule ID sorts
    # last, so it wins over an alias spelled the same (volatile_function).
    by_lower = {key.lower(): key for key in sorted(map(str, known), reverse=True)}
    match = difflib.get_close_matches(str(name).lower(), by_lower, n=1, cutoff=0.6)
    hint = f"; did you mean '{by_lower[match[0]]}'?" if match else f"; known {what}s: {', '.join(sorted(by_lower.values()))}"
    return ConfigError(f"Unknown {what} '{name}' in config{hint}")


def _fits(value: Any, kind: str) -> bool:
    is_int = isinstance(value, int) and not isinstance(value, bool)
    if kind == _TEXT:
        return isinstance(value, str)
    if kind == _TEXTS:
        return isinstance(value, list) and all(isinstance(item, str) for item in value)
    if kind == _NUMBER:
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if kind == _COUNT:
        return is_int and value >= 0
    if kind == _POSITIVE:
        return is_int and value >= 1
    return isinstance(value, bool)


def validate_config(loaded: dict[str, Any], known_rules: set[str]) -> None:
    """Raise :class:`ConfigError` for a section, setting, rule or value the auditor does not understand."""
    for section, value in loaded.items():
        if section not in SECTIONS:
            raise _unknown("section", section, SECTIONS)
        shape = SECTIONS[section]
        if section == "checks":
            if not isinstance(value, dict):
                raise ConfigError("Config section 'checks' must map rule names to settings")
            rules = {rule.lower() for rule in known_rules} | set(CHECK_KEY_TO_RULE_ID)
            for rule, setting in value.items():
                if str(rule).lower() not in rules:
                    raise _unknown("rule", rule, {*known_rules, *CHECK_KEY_TO_RULE_ID})
                if not isinstance(setting, bool) and str(setting).lower() not in CHECK_SETTINGS:
                    raise ConfigError(
                        f"checks.{rule} must be true, false, or one of error, warn, review, off; not {setting!r}"
                    )
        elif section == "suppressions":
            if not isinstance(value, list):
                raise ConfigError("Config section 'suppressions' must be a list")
        elif isinstance(shape, dict):
            if not isinstance(value, dict):
                raise ConfigError(f"Config section '{section}' must be a mapping of settings")
            for key, item in value.items():
                if key not in shape:
                    raise _unknown(f"{section} setting", key, shape)
                if not _fits(item, shape[key]):
                    raise ConfigError(f"{section}.{key} must be {_DESCRIPTIONS[shape[key]]}, not {item!r}")
        elif not _fits(value, shape):
            raise ConfigError(f"{section} must be {_DESCRIPTIONS[shape]}, not {value!r}")


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


# Rules that stay off unless a config turns them on (for example
# ``"checks": {"BLANK_PRECEDENT": "error"}``). On real workbooks their findings
# were almost never mistakes: BLANK_PRECEDENT was right in none of 25 sampled.
OFF_BY_DEFAULT = {"BLANK_PRECEDENT"}


def check_setting(config: dict[str, Any], rule_id: str) -> str:
    # Rule names and their aliases match in any case, as the validator accepts them.
    checks = {str(key).lower(): value for key, value in (config.get("checks") or {}).items()}
    value: Any = checks.get(rule_id.lower())
    if value is None:
        for key, rule in CHECK_KEY_TO_RULE_ID.items():
            if rule == rule_id and key in checks:
                value = checks[key]
                break
    if value is None:
        return "off" if rule_id in OFF_BY_DEFAULT else "error"
    if isinstance(value, bool):
        return "error" if value else "off"
    return str(value).lower()


OFF_SETTINGS = {"off", "false", "disabled", "disable"}


def rule_enabled(config: dict[str, Any], rule_id: str) -> bool:
    return check_setting(config, rule_id) not in OFF_SETTINGS


def apply_check_settings(findings, config: dict[str, Any]):
    kept = []
    for finding in findings:
        setting = check_setting(config, finding.rule_id)
        if setting in OFF_SETTINGS:
            continue
        if setting in {"warn", "warning", "review"} and finding.severity in {"Critical", "High"}:
            finding.severity = "Medium"
            finding.error_confidence = "Review"
        kept.append(finding)
    return kept
