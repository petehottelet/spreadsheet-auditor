"""Build distributable skill packages plus release-ready archives.

Outputs (under `dist/`):

    claude/spreadsheet-auditor/                <- expanded skill folder
    claude/spreadsheet-auditor.zip             <- legacy zip name (kept for backward compat)
    codex/spreadsheet-auditor/                 <- expanded skill folder (includes agents/)
    spreadsheet-auditor-claude.zip             <- release artifact (Claude)
    spreadsheet-auditor-codex.zip              <- release artifact (Codex)
    spreadsheet-auditor-source.zip             <- source-only archive (no built dist/)
    SHA256SUMS                                 <- checksums over all release artifacts
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGE_DIRS = ["scripts", "spreadsheet_auditor", "references", "schemas", "assets"]
EXCLUDED_SCRIPTS = {"build_dist.py"}

SOURCE_INCLUDE_TOP_LEVEL = [
    "spreadsheet_auditor",
    "scripts",
    "tests",
    "references",
    "schemas",
    "agents",
    "examples",
    "benchmarks",
    "assets",
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "project_logo.png",
    ".github",
]


def _ignore_caches(_, names):
    return [
        name
        for name in names
        if name == "__pycache__"
        or name.endswith(".pyc")
        or name == ".pytest_cache"
        or name == "_tmp"
    ]


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
            shutil.copytree(source, destination / directory, ignore=_ignore_caches)

    if include_agents and (ROOT / "agents").exists():
        shutil.copytree(ROOT / "agents", destination / "agents", ignore=_ignore_caches)


def zip_directory(source: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(path for path in source.rglob("*") if path.is_file()):
            archive.write(file_path, file_path.relative_to(source).as_posix())


def build_source_archive(zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for entry in SOURCE_INCLUDE_TOP_LEVEL:
            source = ROOT / entry
            if not source.exists():
                continue
            if source.is_file():
                archive.write(source, source.name)
                continue
            for file_path in sorted(p for p in source.rglob("*") if p.is_file()):
                if "__pycache__" in file_path.parts or ".pytest_cache" in file_path.parts:
                    continue
                if file_path.suffix == ".pyc":
                    continue
                archive.write(file_path, file_path.relative_to(ROOT).as_posix())


def sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release",
        action="store_true",
        help="Also build release archives (claude/codex/source zips + SHA256SUMS).",
    )
    args = parser.parse_args()

    claude_dir = DIST / "claude" / "spreadsheet-auditor"
    codex_dir = DIST / "codex" / "spreadsheet-auditor"

    copy_package(claude_dir, include_agents=False)
    copy_package(codex_dir, include_agents=True)

    # Backward-compatible per-variant zip used by CI for validation.
    zip_directory(claude_dir, DIST / "claude" / "spreadsheet-auditor.zip")

    print(f"Built {claude_dir}")
    print(f"Built {codex_dir}")
    print(f"Built {DIST / 'claude' / 'spreadsheet-auditor.zip'}")

    release_zips: list[Path] = []
    release_zips.append(DIST / "spreadsheet-auditor-claude.zip")
    release_zips.append(DIST / "spreadsheet-auditor-codex.zip")
    zip_directory(claude_dir, release_zips[0])
    zip_directory(codex_dir, release_zips[1])

    if args.release:
        source_zip = DIST / "spreadsheet-auditor-source.zip"
        build_source_archive(source_zip)
        release_zips.append(source_zip)

    # SHA256SUMS over the release artifacts.
    sums_path = DIST / "SHA256SUMS"
    with sums_path.open("w", encoding="utf-8") as fh:
        for path in sorted(release_zips):
            digest = sha256(path)
            rel = path.relative_to(DIST).as_posix()
            fh.write(f"{digest}  {rel}\n")
            print(f"sha256 {digest}  {rel}")
    print(f"Wrote {sums_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
