from __future__ import annotations

from pathlib import Path

from openpyxl import load_workbook
from openpyxl.comments import Comment

from .locations import anchor

# A finding repeated in more cells than this marks the first ones and says
# how many more there are; a comment per cell on a 20,000-row column would
# bury the workbook.
MAX_MEMBER_COMMENTS = 500


def annotate_workbook(source_path: str | Path, output_path: str | Path, findings: list[dict]) -> None:
    source = Path(source_path)
    keep_vba = source.suffix.lower() == ".xlsm"
    wb = load_workbook(source, keep_vba=keep_vba)
    # One comment per cell listing every finding there, in payload order
    # (most severe first); assigning a comment per finding kept only the last.
    # A finding anchors on the top-left cell of its first location piece; the
    # other cells it stands for (its members) point back to it.
    notes: dict[tuple[str, int, int], list[str]] = {}
    for finding in findings:
        if finding.get("suppressed"):
            continue
        location = finding.get("location", "")
        spot = anchor(location)
        if spot is None or spot[0] not in wb.sheetnames:
            continue
        others = [member for member in finding.get("members") or [] if anchor(member) not in (None, spot)]
        text = f"{finding.get('severity')} {finding.get('rule_id')}\n{finding.get('title')}\nFix: {finding.get('suggested_fix')}"
        if others:
            text += f"\nThe same issue is in {len(others)} other cell(s); fixing it here usually fixes them."
        notes.setdefault(spot, []).append(text)
        for member in others[:MAX_MEMBER_COMMENTS]:
            where = anchor(member)
            if where is None or where[0] not in wb.sheetnames:
                continue
            notes.setdefault(where, []).append(
                f"{finding.get('severity')} {finding.get('rule_id')}\nSame issue as {location}; see the comment there."
            )
        if len(others) > MAX_MEMBER_COMMENTS:
            notes[spot][-1] += f" Only the first {MAX_MEMBER_COMMENTS} are marked; the findings JSON lists them all."
    for (sheet_name, row, col), texts in notes.items():
        wb[sheet_name].cell(row=row, column=col).comment = Comment("\n\n".join(texts), "Spreadsheet Auditor")
    wb.save(output_path)
