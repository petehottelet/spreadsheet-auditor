# GitHub Actions examples

Drop-in workflows for auditing spreadsheets in your own repository.

> [!IMPORTANT]
> These files are templates. GitHub only runs workflows that live in
> `.github/workflows/`, so nothing here runs while it sits under `examples/`.
> Copy the one you want into your repo's `.github/workflows/` directory (see the
> install steps below) before expecting it to execute.

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

## `code-scanning.yml`

Audits every `.xlsx`/`.xlsm` workbook, emits one merged SARIF 2.1.0 report, and
uploads it to GitHub code scanning so findings appear inline on pull requests
and under the repo's **Security -> Code scanning** tab.

### Install

1. Copy this file to `.github/workflows/code-scanning.yml` in your repo (it does
   nothing while it lives under `examples/`).
2. Enable code scanning for the repo: **Settings -> Code security -> Code
   scanning** (GitHub Advanced Security is free on public repos).
3. The workflow already declares the required permissions
   (`security-events: write`, `contents: read`) and uses `--fail-on None` so the
   SARIF upload succeeds even when findings exist; severities are shown as code
   scanning alerts instead of failing the job.
4. Pin the version as above (`spreadsheet-auditor[all]==0.1.0`).

> [!NOTE]
> This is for auditing the spreadsheets *in your repository*. It is separate
> from GitHub's CodeQL code scanning, which analyzes source code (e.g. Python)
> for security issues. The two can coexist.
