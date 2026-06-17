# GitHub Actions examples

Drop-in workflows for auditing spreadsheets in your own repository.

## `audit-spreadsheets.yml`

Audits every `.xlsx`/`.xlsm` workbook in your repo on push, PR, and manual
dispatch. Uploads `markdown` and `json` reports as a build artifact. Fails the
job when any workbook produces findings at or above `--fail-on High`.

### Install

1. Copy this file to `.github/workflows/audit-spreadsheets.yml` in your repo.
2. Pin the version: replace `spreadsheet-auditor[all]==0.1.0` with the
   release you want to track (see the
   [releases page](https://github.com/petehottelet/spreadsheet-auditor/releases)).
3. Optional: adjust the `--fail-on` threshold or the file glob pattern.

### Exit-code semantics

The auditor returns a distinct exit code for each outcome so workflows can
react differently to defects vs environmental problems:

| Exit code | Meaning                                                            | Workflow reaction              |
| --------: | ------------------------------------------------------------------ | ------------------------------ |
|         0 | Clean (no findings at/above `--fail-on`).                          | Success                        |
|         1 | Findings at/above `--fail-on`.                                     | **Fail** (default)             |
|         2 | `--strict` and recalculation/coverage limitations were present.    | Treat as warning (not used here) |
|         3 | Healthcheck failed: required dependency missing.                   | Fail (separate step)           |
|         4 | Preflight error: unreadable workbook or wrong extension.           | Fail                           |
|         5 | Internal auditor error.                                            | Fail                           |

If you want CI to *also* fail when recalculation could not run, add `--strict`
to the audit invocation; combine it with the healthcheck step so missing
LibreOffice is detected up front rather than silently degrading the audit.
