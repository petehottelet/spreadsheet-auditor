# Demo screenshots

The repository README links to a small set of screenshots to give first-time
visitors a clear picture of what the auditor produces. The images are not
committed yet; this folder is a placeholder so the README links don't 404 once
you drop them in.

## Shot list

1. `annotated_workbook.png` - the `demo_annotated.xlsx` file open in Excel or
   LibreOffice Calc, with cell comments visible at the seeded-defect cells
   (`B11`, `F6`, `E9`, `B6`, `B14`).
2. `report_excerpt.png` - the top of `demo_audit_report.md` rendered on GitHub,
   showing the severity summary table and the first 2-3 findings.
3. `html_report.png` - `demo_audit_report.html` open in a browser, showing the
   severity sections and a finding card with confidence + suggested fix.
4. `cli_output.png` - terminal session running
   `spreadsheet-auditor examples/demo_bad_budget.xlsx`.

## How to recapture

```bash
python examples/make_demo.py
# then take the four screenshots above and save them in this folder.
```

Recommended dimensions: ~1600px wide, JPEG/PNG, < 400 KB each, light theme.
