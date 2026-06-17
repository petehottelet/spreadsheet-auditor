"""Skill metadata validation gate.

These tests ensure the Spreadsheet Auditor skill remains discoverable and
installable across Claude/Codex by enforcing the YAML frontmatter contract.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "quick_validate.py"

# Import the validator module directly so we can unit-test internals.
sys.path.insert(0, str(ROOT / "scripts"))
import quick_validate  # noqa: E402


def test_validator_passes_for_repo_root():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ROOT)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Skill validation passed" in result.stdout


def test_skill_md_frontmatter_is_well_formed():
    fields = quick_validate._parse_frontmatter((ROOT / "SKILL.md").read_text(encoding="utf-8"))
    assert fields is not None, "SKILL.md frontmatter could not be parsed"
    errors = quick_validate._validate_frontmatter(fields)
    assert errors == [], errors


@pytest.mark.parametrize(
    "frontmatter, expect_error_substring",
    [
        ("name: bad NAME\ndescription: ok", "invalid skill name"),
        ("name: ok-name\ndescription: \"\"", "non-empty"),
        ("name: ok-name\ndescription: ok\nextra: x", "unexpected key"),
        ("description: ok", "missing required key"),
    ],
)
def test_validator_rejects_invalid_frontmatter(frontmatter, expect_error_substring, tmp_path):
    skill = tmp_path / "SKILL.md"
    skill.write_text(f"---\n{frontmatter}\n---\n\n# Body\n", encoding="utf-8")
    fields = quick_validate._parse_frontmatter(skill.read_text(encoding="utf-8"))
    errors = quick_validate._validate_frontmatter(fields or {})
    joined = " ".join(errors).lower()
    assert any(expect_error_substring in err.lower() for err in errors) or expect_error_substring in joined


def test_folded_description_block_is_parsed():
    raw = "---\nname: spreadsheet-auditor\ndescription: >\n  Audit existing\n  Excel workbooks.\n---\n"
    fields = quick_validate._parse_frontmatter(raw)
    assert fields is not None
    assert fields["description"].startswith("Audit existing Excel workbooks")
    assert quick_validate._validate_frontmatter(fields) == []
