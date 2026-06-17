from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


def soffice_path() -> str | None:
    return shutil.which("soffice") or shutil.which("libreoffice")


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
