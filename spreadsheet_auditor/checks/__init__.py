"""Pluggable check registry.

Each module in this package registers one or more `Check` subclasses by
decorating them with `@register`. The orchestrator in `spreadsheet_auditor.audit`
discovers them by importing this package, so adding a new check only requires
adding a new module here -- no edits to `audit.py`.

Public surface:

* `Check`             - base class every check must subclass.
* `CheckContext`      - shared context object passed to `Check.run()`.
* `register(cls)`     - decorator that registers a check class.
* `checks()`          - returns the ordered list of registered check classes.
* `discovered_modules` - names of modules imported so far (mostly for tests).
"""

from __future__ import annotations

from .base import Check, CheckContext, checks, discovered_modules, register

# Import built-in check modules so their `@register` calls run.
# Custom checks added via plug-in entry points are loaded lazily by callers.
from . import data_hygiene  # noqa: F401
from . import finance  # noqa: F401
from . import formula_integrity  # noqa: F401
from . import ranges  # noqa: F401
from . import reconciliation  # noqa: F401

__all__ = [
    "Check",
    "CheckContext",
    "register",
    "checks",
    "discovered_modules",
]
