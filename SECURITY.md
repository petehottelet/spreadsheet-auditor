# Security Policy

## Threat model

Spreadsheet Auditor treats every input workbook as **untrusted**. Workbooks
can carry macros, external links, ActiveX, dynamic arrays, and Power Query
connections that, if executed, could:

- Read or exfiltrate local files.
- Make outbound network requests (e.g. to refresh a query).
- Run arbitrary VBA or OOXML payloads.

The auditor's defaults are designed to *never* trigger any of these.

## What the auditor does and does not do

| Activity                                  | What the auditor does                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------- |
| **Macros (`.xlsm`)**                      | **Inventoried only.** Macro modules are listed in `coverage.macros_present` but never executed. The auditor opens the workbook with `keep_vba=False` semantics. |
| **External links**                        | **Inventoried only.** Linked workbooks are not followed; cached values are read where present. |
| **External data sources / Power Query**   | **Not refreshed.** Cached values are read; the connection is not opened.              |
| **Web queries / data tables**             | Not refreshed. Cached values only.                                                    |
| **OOXML parsing**                         | When `defusedxml` is installed it is used to mitigate billion-laughs and XXE patterns. When `defusedxml` is missing the run records this as a coverage limitation rather than silently falling back. |
| **Recalculation**                         | When LibreOffice / `soffice` is available, it is invoked headless inside a private user profile in a temporary directory. Macros are disabled (`--norestore --headless --convert-to xlsx`). |
| **Annotation**                            | Always written to a *separate* file path supplied via `--annotated`. The source workbook is never modified. |
| **Network access**                        | None during normal audit operation. HTML and SARIF outputs are self-contained. |

## Defenses against known vectors

- **Path traversal / zip slip**: only the user-provided workbook path is read;
  no zip extraction outside of openpyxl's own parsing.
- **OOXML XXE / billion laughs**: `defusedxml` is installed when you `pip
  install "spreadsheet-auditor[xml]"` or `[all]`. Without it, the run is
  flagged in `coverage.limitations` so you know the risk applies.
- **Macro execution**: never enabled. LibreOffice is invoked with
  `--norestore --headless --convert-to xlsx`. If you suspect a workbook
  contains malware, audit it on a disposable VM.
- **Resource exhaustion**: per-check workload is bounded by
  `limits.max_cells`, `limits.max_formulas`, `limits.max_reported_findings`,
  and `limits.timeout_seconds` in the config. Exceeded limits are recorded
  in `coverage.truncated`.
- **Privacy**: the auditor does not phone home. The HTML/SARIF reports use
  only inline CSS and no remote assets.

## Reporting a vulnerability

Please report privately via GitHub's
[private vulnerability reporting](https://github.com/petehottelet/spreadsheet-auditor/security/advisories/new)
(**Security -> Report a vulnerability**). Include a description and, when safe to
share, a minimal workbook that demonstrates the issue. We will acknowledge
within 7 days and aim to provide a fix or mitigation within 30 days.

If you cannot use private reporting, you may reach the maintainer at
`36128338+petehottelet@users.noreply.github.com`.

Please do **not** open a public issue for security reports.

## Supported versions

Only the latest minor release receives security fixes. Pinning a release in
your CI is recommended; see
[Releases](https://github.com/petehottelet/spreadsheet-auditor/releases).
