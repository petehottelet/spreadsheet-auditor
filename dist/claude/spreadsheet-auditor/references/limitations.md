# Limitations

`spreadsheet-auditor` is a static-first audit tool. It does not guarantee Excel calculation parity.

Always disclose when:

- LibreOffice recalculation is unavailable or fails.
- Cached values are stale or missing.
- External workbooks are referenced but not available.
- Formulas use unsupported syntax, dynamic arrays, data tables, structured references, Power Query, Data Model, add-ins, UDFs, or macros.
- Runtime limits cause expensive graph or range checks to be skipped.
- The workbook is password-protected or corrupt.

Never execute macros. Never follow external links without explicit user approval and sandbox controls.
