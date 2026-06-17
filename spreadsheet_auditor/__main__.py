"""Enable `python -m spreadsheet_auditor` invocation."""

from __future__ import annotations

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
