"""Check base class, registry, and context object."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from ..finding import Finding


@dataclass
class CheckContext:
    """Everything a check might need to inspect a workbook."""

    workbook_path: Any  # pathlib.Path
    formula_wb: Any  # openpyxl Workbook (formulas)
    value_wb: Any  # openpyxl Workbook (cached values)
    allowed_sheet_names: set[str]
    formulas: list[dict]
    config: dict
    inventory: dict
    unsupported_features: set[str] = field(default_factory=set)
    #: Defined names and structured table references resolved to A1 ranges
    #: (``spreadsheet_auditor.names.NameTable``). May be None in unit tests.
    names: Any = None
    #: Cooperative time budget (``spreadsheet_auditor.budget.Budget``). Long
    #: loops should call ``budget.tick()`` once per row or formula; it raises
    #: ``AuditTimeout`` when the audit's deadline has passed. May be None.
    budget: Any = None
    #: False when ``limits.max_cells`` was exceeded: checks that walk the cell
    #: grid (hardcodes, cross-foot, data hygiene) must return nothing and let
    #: the orchestrator's limitation note explain why.
    grid_scan_allowed: bool = True


class Check:
    """Base class for an auditor check.

    Subclasses set the class attributes below and implement `run`. Keep
    `run` side-effect-free: detectors may be invoked in parallel or skipped
    when the orchestrator hits a timeout.
    """

    #: Stable rule IDs this check can emit. Used by the docs generator and the
    #: catalog test; the orchestrator does not enforce it at runtime.
    rule_ids: tuple[str, ...] = ()
    #: Default detection mode ("DET" or "HEUR"). Individual findings may override.
    mode: str = "DET"
    #: Human-readable name (used in error messages and the registry table).
    name: str = ""
    #: One-line description shown in catalog/docs.
    description: str = ""

    def run(self, ctx: CheckContext) -> list[Finding]:  # pragma: no cover - abstract
        raise NotImplementedError


_REGISTRY: list[type[Check]] = []
_DISCOVERED: list[str] = []


def register(cls: type[Check]) -> type[Check]:
    """Register a check class. Idempotent."""
    if cls not in _REGISTRY:
        _REGISTRY.append(cls)
        _DISCOVERED.append(cls.__module__)
    return cls


def checks() -> list[type[Check]]:
    """Return the registered check classes in registration order."""
    return list(_REGISTRY)


def discovered_modules() -> list[str]:
    """Return modules from which checks were imported."""
    return list(_DISCOVERED)


def make_runner(name: str, fn: Callable[[CheckContext], list[Finding]], **attrs: Any) -> type[Check]:
    """Helper: build a Check subclass from a function. Reduces boilerplate."""
    body: dict[str, Any] = {"run": lambda self, ctx: fn(ctx)}
    body.update(attrs)
    return type(name, (Check,), body)
