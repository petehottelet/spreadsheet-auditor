from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE_DIRS = ["scripts", "references", "schemas", "assets"]
EXCLUDED_SCRIPTS = {"build_dist.py"}


def copy_package(destination: Path, include_agents: bool) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    shutil.copy2(ROOT / "SKILL.md", destination / "SKILL.md")

    for directory in PACKAGE_DIRS:
        source = ROOT / directory
        if not source.exists():
            continue
        if directory == "scripts":
            target = destination / directory
            target.mkdir()
            for script in sorted(source.glob("*.py")):
                if script.name not in EXCLUDED_SCRIPTS:
                    shutil.copy2(script, target / script.name)
        else:
            shutil.copytree(source, destination / directory)

    if include_agents and (ROOT / "agents").exists():
        shutil.copytree(ROOT / "agents", destination / "agents")


def zip_directory(source: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(path for path in source.rglob("*") if path.is_file()):
            archive.write(file_path, file_path.relative_to(source).as_posix())


def main() -> int:
    claude_dir = DIST / "claude" / "spreadsheet-auditor"
    codex_dir = DIST / "codex" / "spreadsheet-auditor"

    copy_package(claude_dir, include_agents=False)
    copy_package(codex_dir, include_agents=True)
    zip_directory(claude_dir, DIST / "claude" / "spreadsheet-auditor.zip")

    print(f"Built {claude_dir}")
    print(f"Built {codex_dir}")
    print(f"Built {DIST / 'claude' / 'spreadsheet-auditor.zip'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
