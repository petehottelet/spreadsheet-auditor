from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

# LibreOffice defaults to "never recalculate" for Excel 2007+ files
# (OOXMLRecalcMode = 1), so a headless conversion would keep whatever Excel
# cached, including stale values from a workbook saved in manual-calculation
# mode. The isolated profile is seeded with these settings before every run:
# always recalculate on load, and never run macros.
PROFILE_SETTINGS = """<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>
  <item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="ODFRecalcMode" oor:op="fuse"><value>0</value></prop></item>
  <item oor:path="/org.openoffice.Office.Common/Security/Scripting"><prop oor:name="MacroSecurityLevel" oor:op="fuse"><value>3</value></prop></item>
</oor:items>
"""


def soffice_path() -> str | None:
    return shutil.which("soffice") or shutil.which("libreoffice")


def seed_profile(profile_dir: str | Path) -> Path:
    """Write the recalculation and macro-security settings into a fresh profile."""
    user_dir = Path(profile_dir) / "user"
    user_dir.mkdir(parents=True, exist_ok=True)
    settings = user_dir / "registrymodifications.xcu"
    settings.write_text(PROFILE_SETTINGS, encoding="utf-8", newline="\n")
    return settings


def recalc_if_available(path: str | Path, timeout_seconds: int = 60, work_dir: str | Path | None = None) -> dict:
    soffice = soffice_path()
    if not soffice:
        return {
            "status": "unavailable",
            "path": str(path),
            "limitations": ["LibreOffice/soffice not available; using static analysis and cached values only."],
        }

    source = Path(path)
    if work_dir is None:
        tmp = Path(tempfile.mkdtemp(prefix="spreadsheet-auditor-lo-"))
    else:
        tmp = Path(work_dir)
        tmp.mkdir(parents=True, exist_ok=True)

    out_dir = tmp / "out"
    profile_dir = tmp / "profile"
    out_dir.mkdir(exist_ok=True)
    profile_dir.mkdir(exist_ok=True)
    seed_profile(profile_dir)
    cmd = [
        soffice,
        "--headless",
        "--nologo",
        "--nofirststartwizard",
        "--norestore",
        f"-env:UserInstallation=file:///{profile_dir.as_posix()}",
        "--convert-to",
        "xlsx",
        "--outdir",
        str(out_dir),
        str(source),
    ]
    try:
        subprocess.run(cmd, check=True, timeout=timeout_seconds, capture_output=True, text=True)
    except Exception as exc:
        return {
            "status": "failed",
            "path": str(path),
            "limitations": [f"LibreOffice recalculation failed: {exc}"],
        }
    converted = out_dir / (source.stem + ".xlsx")
    if not converted.exists():
        return {
            "status": "failed",
            "path": str(path),
            "limitations": ["LibreOffice did not produce a recalculated workbook."],
        }
    stable_copy = tmp / (source.stem + ".recalculated.xlsx")
    shutil.copy2(converted, stable_copy)
    return {"status": "completed", "path": str(stable_copy), "limitations": []}
