from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

REQUIRED_FILES = [
    "SKILL.md",
    "scripts/audit.py",
    "references/check_catalog.md",
    "references/severity_rubric.md",
    "references/report_template.md",
]

def main(path: str) -> int:
    root = Path(path)
    if root.is_file() and root.suffix.lower() == ".zip":
        return validate_zip(root)
    skill = root / "SKILL.md"
    if not skill.exists():
        print("Missing SKILL.md", file=sys.stderr)
        return 1
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        print("SKILL.md missing YAML frontmatter", file=sys.stderr)
        return 1
    frontmatter = match.group(1)
    fields = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if set(fields) != {"name", "description"}:
        print("Frontmatter must contain only name and description", file=sys.stderr)
        return 1
    if not re.fullmatch(r"[a-z0-9-]{1,63}", fields["name"]):
        print("Invalid skill name", file=sys.stderr)
        return 1
    if not fields["description"] or len(fields["description"]) > 1024:
        print("Description must be non-empty and <= 1024 chars", file=sys.stderr)
        return 1
    for required in REQUIRED_FILES[1:]:
        if not (root / required).exists():
            print(f"Missing required file: {required}", file=sys.stderr)
            return 1
    print("Skill validation passed")
    return 0


def validate_zip(path: Path) -> int:
    try:
        with zipfile.ZipFile(path) as archive:
            names = {entry.filename.replace("\\", "/") for entry in archive.infolist()}
    except zipfile.BadZipFile as exc:
        print(f"Invalid ZIP: {exc}", file=sys.stderr)
        return 1
    if "SKILL.md" not in names:
        print("ZIP must contain SKILL.md at the archive root", file=sys.stderr)
        return 1
    missing = [name for name in REQUIRED_FILES if name not in names]
    if missing:
        print("ZIP missing required file(s): " + ", ".join(missing), file=sys.stderr)
        return 1
    print("Skill ZIP validation passed")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: quick_validate.py <skill-folder>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
