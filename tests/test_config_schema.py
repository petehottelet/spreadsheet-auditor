"""Validate a representative config against the published config schema."""

import json
from pathlib import Path

import pytest

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


def test_sample_config_validates():
    jsonschema = pytest.importorskip("jsonschema")
    schema = json.loads((ROOT / "schemas" / "config.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=SAMPLE_CONFIG, schema=schema)
