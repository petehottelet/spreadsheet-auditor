"""Validate a Spreadsheet Auditor skill package.

Usage:
    python scripts/quick_validate.py <skill-folder-or-zip>

Checks:
- `SKILL.md` exists with valid YAML frontmatter containing exactly `name` and
  `description`.
- Skill name is lowercase kebab-case (<= 63 chars).
- Skill description is non-empty and <= 1024 characters (Claude limit).
- Required reference files are present.
- Either the legacy `scripts/audit.py` shim or the new
  `spreadsheet_auditor/cli.py` package entry point exists.
"""

from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "references/check_catalog.md",
    "references/severity_rubric.md",
    "references/report_template.md",
]

ENTRY_POINTS = [
    "scripts/audit.py",
    "spreadsheet_auditor/cli.py",
]

NAME_RE = re.compile(r"[a-z0-9][a-z0-9-]{0,62}")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.S)


def _parse_frontmatter(text: str) -> dict[str, Any] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    raw = match.group(1)
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
        if not isinstance(data, dict):
            return None
        return data
    except Exception:
        return _parse_frontmatter_fallback(raw)


def _parse_frontmatter_fallback(raw: str) -> dict[str, Any] | None:
    """Minimal YAML fallback when PyYAML is unavailable.

    Handles the two shapes we actually publish:
      * single-line `key: value`
      * folded block scalar `key: >` followed by indented continuation lines.
    """
    fields: dict[str, str] = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            return None
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value in {">", ">-", "|", "|-"}:
            buffer: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith(("  ", "\t")) or not lines[i].strip()):
                if lines[i].strip():
                    buffer.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(buffer)
            continue
        fields[key] = value
        i += 1
    return fields or None


def _validate_frontmatter(fields: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    extra = set(fields) - {"name", "description"}
    missing = {"name", "description"} - set(fields)
    if extra:
        errors.append(f"frontmatter has unexpected key(s): {sorted(extra)}")
    if missing:
        errors.append(f"frontmatter missing required key(s): {sorted(missing)}")
    name = str(fields.get("name", ""))
    if not NAME_RE.fullmatch(name):
        errors.append(f"invalid skill name {name!r}; must be lowercase kebab-case, <=63 chars")
    description = str(fields.get("description", "")).strip()
    if not description:
        errors.append("description must be non-empty")
    elif len(description) > 1024:
        errors.append(f"description must be <=1024 chars (got {len(description)})")
    return errors


def validate_folder(root: Path) -> int:
    skill = root / "SKILL.md"
    if not skill.exists():
        print("Missing SKILL.md", file=sys.stderr)
        return 1
    fields = _parse_frontmatter(skill.read_text(encoding="utf-8"))
    if fields is None:
        print("SKILL.md missing valid YAML frontmatter", file=sys.stderr)
        return 1
    errors = _validate_frontmatter(fields)
    if errors:
        for err in errors:
            print(f"SKILL.md: {err}", file=sys.stderr)
        return 1

    if not any((root / entry).exists() for entry in ENTRY_POINTS):
        print(
            "Skill package is missing an entry point; expected one of: "
            + ", ".join(ENTRY_POINTS),
            file=sys.stderr,
        )
        return 1

    for required in REQUIRED_FILES:
        if not (root / required).exists():
            print(f"Missing required file: {required}", file=sys.stderr)
            return 1
    print("Skill validation passed")
    return 0


def validate_zip(path: Path) -> int:
    try:
        with zipfile.ZipFile(path) as archive:
            names = {entry.filename.replace("\\", "/") for entry in archive.infolist()}
            try:
                text = archive.read("SKILL.md").decode("utf-8")
            except KeyError:
                print("ZIP must contain SKILL.md at the archive root", file=sys.stderr)
                return 1
    except zipfile.BadZipFile as exc:
        print(f"Invalid ZIP: {exc}", file=sys.stderr)
        return 1

    fields = _parse_frontmatter(text)
    if fields is None:
        print("SKILL.md missing valid YAML frontmatter", file=sys.stderr)
        return 1
    errors = _validate_frontmatter(fields)
    if errors:
        for err in errors:
            print(f"SKILL.md: {err}", file=sys.stderr)
        return 1

    if not any(entry in names for entry in ENTRY_POINTS):
        print(
            "ZIP missing an entry point; expected one of: " + ", ".join(ENTRY_POINTS),
            file=sys.stderr,
        )
        return 1

    missing = [name for name in REQUIRED_FILES if name not in names]
    if missing:
        print("ZIP missing required file(s): " + ", ".join(missing), file=sys.stderr)
        return 1
    print("Skill ZIP validation passed")
    return 0


def main(path: str) -> int:
    root = Path(path)
    if root.is_file() and root.suffix.lower() == ".zip":
        return validate_zip(root)
    return validate_folder(root)


def _json_diagnostic(path: str) -> dict[str, Any]:
    root = Path(path)
    skill = root / "SKILL.md"
    if not skill.exists():
        return {"valid": False, "errors": ["Missing SKILL.md"]}
    fields = _parse_frontmatter(skill.read_text(encoding="utf-8"))
    if fields is None:
        return {"valid": False, "errors": ["Missing valid YAML frontmatter"]}
    errors = _validate_frontmatter(fields)
    return {"valid": not errors, "errors": errors, "fields": fields}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: quick_validate.py <skill-folder-or-zip> [--json]", file=sys.stderr)
        raise SystemExit(2)
    if "--json" in sys.argv[2:]:
        print(json.dumps(_json_diagnostic(sys.argv[1]), indent=2))
        raise SystemExit(0)
    raise SystemExit(main(sys.argv[1]))
