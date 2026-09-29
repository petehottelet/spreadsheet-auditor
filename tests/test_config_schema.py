"""Validate a representative config against the published config schema."""

import json
from pathlib import Path

import pytest

from spreadsheet_auditor.audit import _known_rules
from spreadsheet_auditor.config_loader import (
    CHECK_SETTINGS,
    SECTIONS,
    ConfigError,
    validate_config,
)

ROOT = Path(__file__).resolve().parents[1]

SAMPLE_CONFIG = {
    "mode": "financial_model",
    "scope": {
        "include_sheets": ["Summary", "Returns"],
        "exclude_sheets": ["Scratch"],
        "headline_outputs": ["Summary!B12", "Returns!C35"],
    },
    "materiality": {"absolute": 1000, "relative": 0.001, "percent_points": 0.1},
    "limits": {
        "max_formulas": 50000,
        "max_range_expansion_cells": 250000,
        "max_reported_findings": 200,
    },
    "checks": {
        "live_errors": "error",
        "cross_foot_failure": "error",
        "range_length_mismatch": "warn",
        "volatile_function": "off",
    },
    "recalc": {"enabled": True, "timeout_seconds": 60},
    "suppressions": [
        {"rule_id": "LITERAL_CONSTANT", "range": "Assumptions!B10:B20", "reason": "Board-approved"}
    ],
}


def _schema() -> dict:
    return json.loads((ROOT / "schemas" / "config.schema.json").read_text(encoding="utf-8"))


def test_sample_config_validates():
    jsonschema = pytest.importorskip("jsonschema")
    jsonschema.validate(instance=SAMPLE_CONFIG, schema=_schema())


def test_sample_and_bundled_configs_pass_the_auditors_own_check():
    for config in (SAMPLE_CONFIG, json.loads((ROOT / "evals" / "files" / "legacy-config.json").read_text(encoding="utf-8"))):
        validate_config(config, _known_rules())


def test_schema_publishes_the_sections_settings_and_levels_the_auditor_accepts():
    schema = _schema()
    assert set(schema["properties"]) == set(SECTIONS)
    assert schema["additionalProperties"] is False
    for section, shape in SECTIONS.items():
        if isinstance(shape, dict):
            assert set(schema["properties"][section]["properties"]) == set(shape), section
            assert schema["properties"][section]["additionalProperties"] is False, section
    levels = schema["properties"]["checks"]["additionalProperties"]["oneOf"][0]["enum"]
    assert set(levels) == CHECK_SETTINGS


def test_schema_rejects_a_mistyped_section_as_the_auditor_does():
    jsonschema = pytest.importorskip("jsonschema")
    config = {"limit": {"max_formulas": 10}}
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=config, schema=_schema())
    with pytest.raises(ConfigError, match="did you mean 'limits'"):
        validate_config(config, _known_rules())
