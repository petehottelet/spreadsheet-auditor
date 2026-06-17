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

## Security Behavior

- Macros/VBA are inventoried and never executed. LibreOffice recalculation runs headless in an isolated profile.
- External workbook links are inventoried and reported, never followed by default.
- XML parsing uses `defusedxml` when available. When it is missing, the audit continues but records a coverage limitation noting that XML parsing relied on library defaults. A future `--strict-security` option may turn this into a hard failure.
- Preflight checks archive structure and uncompressed size to reduce zip-bomb risk, and never overwrites the source workbook.

## Exit Codes

| Code | Meaning |
|---:|---|
| 0 | Completed; no findings at or above the `--fail-on` threshold |
| 1 | Completed; findings at or above the `--fail-on` threshold |
| 2 | Completed with coverage limitations, only when `--strict` or `--fail-on None` is set |
| 4 | Preflight/security failure (unreadable, unsupported, oversized, or invalid input) |
| 5 | Internal audit error |

Benign limitations such as missing recalculation or optional packages do not fail a normal run; use `--strict` to surface them as exit code 2 in CI.
