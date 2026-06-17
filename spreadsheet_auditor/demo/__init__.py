"""Bundled demo assets.

This subpackage ships the demo workbook (`demo_bad_budget.xlsx`) inside the
installed wheel so `spreadsheet-auditor --demo` works from an installed package
or an unpacked skill, not just from a repository checkout. The canonical source
is `examples/demo_bad_budget.xlsx`; `examples/make_demo.py` keeps this copy in
sync.
"""

from __future__ import annotations
