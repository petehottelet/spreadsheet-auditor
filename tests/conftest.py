"""Make the `spreadsheet_auditor` package importable when running tests
without installing the project (e.g. `python -m pytest` in a fresh checkout).
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
