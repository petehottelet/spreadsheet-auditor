from __future__ import annotations

from pathlib import Path

from openpyxl import load_workbook
from openpyxl.comments import Comment

from .locations import anchor


def annotate_workbook(source_path: str | Path, output_path: str | Path, findings: list[dict]) -> None:
    source = Path(source_path)
    keep_vba = source.suffix.lower() == ".xlsm"
    wb = load_workbook(source, keep_vba=keep_vba)
    # One comment per cell listing every finding there, in payload order
    # (most severe first); assigning a comment per finding kept only the last.
    # A finding anchors on the top-left cell of its first location piece.
    notes: dict[tuple[str, int, int], list[str]] = {}
    for finding in findings:
        if finding.get("suppressed"):
            continue
        spot = anchor(finding.get("location", ""))
        if spot is None or spot[0] not in wb.sheetnames:
            continue
        notes.setdefault(spot, []).append(
            f"{finding.get('severity')} {finding.get('rule_id')}\n"
            f"{finding.get('title')}\n"
            f"Fix: {finding.get('suggested_fix')}"
        )
    for (sheet_name, row, col), texts in notes.items():
        wb[sheet_name].cell(row=row, column=col).comment = Comment("\n\n".join(texts), "Spreadsheet Auditor")
    wb.save(output_path)
