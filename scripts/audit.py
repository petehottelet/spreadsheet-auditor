"""Backward-compatible CLI shim.

The implementation now lives in the importable `spreadsheet_auditor` package.
This shim keeps `python scripts/audit.py ...` working for skill packages,
existing tests, and external integrations that hard-coded the script path.

For new code, prefer either of:

    spreadsheet-auditor workbook.xlsx          # installed CLI entry point
    python -m spreadsheet_auditor workbook.xlsx
"""

from __future__ import annotations

import sys
from pathlib import Path


def _bootstrap() -> None:
    # When this file is executed inside a packaged skill (where the
    # `spreadsheet_auditor/` package sits next to `scripts/` but the package is
    # not installed), prepend the parent directory so the import resolves.
    here = Path(__file__).resolve().parent
    candidate = here.parent
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))


_bootstrap()

from spreadsheet_auditor.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
