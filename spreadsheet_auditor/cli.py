"""Console-script entry point for spreadsheet-auditor.

This module re-exports the CLI's `main` function so it can be referenced by the
`console_scripts` entry point in `pyproject.toml`:

    spreadsheet-auditor = spreadsheet_auditor.cli:main
"""

from __future__ import annotations

from .audit import main

__all__ = ["main"]


if __name__ == "__main__":
    raise SystemExit(main())
