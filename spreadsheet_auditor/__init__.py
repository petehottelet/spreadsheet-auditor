"""Audit existing spreadsheets for correctness defects.

`spreadsheet-auditor` is an audit-only Agent Skill and CLI for reviewing
existing Excel workbooks and financial models. It identifies formula errors,
broken references, range mistakes, hardcoded values, reconciliation failures,
circular references, hidden-structure risks, and data-quality issues without
modifying the source workbook.
"""

from __future__ import annotations

__version__ = "0.1.0"
__all__ = ["__version__"]
