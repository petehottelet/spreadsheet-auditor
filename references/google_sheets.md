# Auditing Google Sheets

Spreadsheet Auditor does **not** integrate with the Google Sheets API. There
are two ways to use it against a Sheets document.

## Recommended: export to `.xlsx`, then audit

Google Sheets has high-fidelity `.xlsx` export that preserves formulas,
ranges, hidden rows/columns, and most calculated values. Use that.

### Manual export

1. In Google Sheets, choose **File -> Download -> Microsoft Excel (.xlsx)**.
2. Audit the downloaded file:

   ```bash
   spreadsheet-auditor model.xlsx --out report.md --json findings.json
   ```

### Scripted export with `gspread` + `pandas`

If you need a programmatic flow, use the [`gspread`](https://pypi.org/project/gspread/)
client to fetch the spreadsheet and re-emit it. Note that this round-trip
*loses formulas*: it captures cell values only.

```python
import gspread
from openpyxl import Workbook

gc = gspread.service_account()        # use OAuth/service-account creds
sh = gc.open_by_key("<sheet-id>")

wb = Workbook()
wb.remove(wb.active)
for ws_in in sh.worksheets():
    ws = wb.create_sheet(title=ws_in.title)
    for r, row in enumerate(ws_in.get_all_values(), start=1):
        for c, value in enumerate(row, start=1):
            ws.cell(row=r, column=c, value=value)
wb.save("from_sheets.xlsx")
```

This approach is **value-only**. Static formula checks
(`FORMULA_DRIFT`, `BROKEN_REFERENCE`, `RANGE_EXCLUSION`, ...) will not fire
because the formulas are gone by the time `openpyxl` opens the file. For
real fidelity, prefer the manual `.xlsx` export above.

## Native Sheets API support?

We don't plan to add one. Reasons:

- The auditor's value comes from formula structure analysis; the Sheets API
  exposes formulas as strings but the surrounding metadata (data validation,
  named ranges, etc.) differs enough from `.xlsx` to require a parallel rule
  set.
- Auth, OAuth scopes, and rate limits would push the auditor away from being
  a pure offline tool.

If you have a strong use case for native Sheets support, open an issue and
describe the workflow.

## Limitations specific to Google Sheets exports

- **Custom Apps Script functions** are exported as `#NAME?`. The auditor will
  report them as `LIVE_ERROR`.
- **Importrange()** and **Importdata()** lose their data source on export
  and become `#REF!`. The auditor will report them as `BROKEN_REFERENCE`.
- **Filter views**, **protected ranges**, and **conditional formatting** are
  not modeled by the auditor on either platform.
- **Date locale**: Sheets exports dates using the spreadsheet's locale; if
  your audit pipeline expects US dates, set the locale before exporting.
