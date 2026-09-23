from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


SUPPORTED_EXTENSIONS = {".xlsx", ".xlsm", ".csv"}
# Encrypted (password-to-open) OOXML files and legacy .xls are OLE2 compound files, not zips.
OLE2_SIGNATURE = bytes.fromhex("D0CF11E0A1B11AE1")
# Package parts openpyxl does not round-trip; an annotated copy drops them.
DRAWING_PART_PREFIXES = (
    "xl/drawings/",
    "xl/charts/",
    "xl/media/",
    "xl/ctrlprops/",
    "xl/embeddings/",
    "xl/activex/",
    "xl/slicers/",
    "xl/timelines/",
)


class PreflightError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def preflight(path: str | Path, max_uncompressed_mb: int = 250) -> dict:
    workbook_path = Path(path)
    if not workbook_path.exists():
        raise PreflightError(f"Input file does not exist: {workbook_path}")
    if workbook_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise PreflightError(
            f"Unsupported file type: {workbook_path.suffix}. Convert it to .xlsx first "
            "(soffice --headless --convert-to xlsx FILE) or re-save it from Excel."
        )

    result = {
        "path": str(workbook_path),
        "extension": workbook_path.suffix.lower(),
        "size_bytes": workbook_path.stat().st_size,
        "sha256": sha256_file(workbook_path),
        "archive_checked": False,
        "macros_present": False,
    }

    if workbook_path.suffix.lower() in {".xlsx", ".xlsm"}:
        try:
            with zipfile.ZipFile(workbook_path) as archive:
                total_uncompressed = sum(info.file_size for info in archive.infolist())
                result["archive_checked"] = True
                result["uncompressed_bytes"] = total_uncompressed
                result["macros_present"] = any(info.filename.lower() == "xl/vbaproject.bin" for info in archive.infolist())
                result["drawing_parts"] = sum(
                    1
                    for info in archive.infolist()
                    if not info.is_dir() and info.filename.lower().startswith(DRAWING_PART_PREFIXES)
                )
                if total_uncompressed > max_uncompressed_mb * 1024 * 1024:
                    raise PreflightError(
                        f"Workbook expands to {total_uncompressed} bytes, above configured limit"
                    )
        except zipfile.BadZipFile as exc:
            with workbook_path.open("rb") as handle:
                if handle.read(8) == OLE2_SIGNATURE:
                    raise PreflightError(
                        "Workbook is password-protected, or is a legacy .xls under an .xlsx name; "
                        "save an unprotected .xlsx copy and audit that."
                    ) from exc
            raise PreflightError(f"Workbook is not a valid XLSX/XLSM archive: {exc}") from exc

    return result
