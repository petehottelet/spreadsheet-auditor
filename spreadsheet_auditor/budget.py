"""Cooperative wall-clock budget shared by the orchestrator and the checks."""

from __future__ import annotations

import time


class AuditTimeout(Exception):
    """Raised inside a check when the audit's time budget is exhausted."""


class Budget:
    """Wall-clock budget. ``seconds`` of zero or None disables the deadline."""

    __slots__ = ("seconds", "deadline")

    def __init__(self, seconds: float | None, start: float | None = None) -> None:
        self.seconds = float(seconds or 0)
        base = time.monotonic() if start is None else start
        self.deadline = base + self.seconds if self.seconds > 0 else None

    def expired(self) -> bool:
        return self.deadline is not None and time.monotonic() > self.deadline

    def tick(self) -> None:
        """Raise :class:`AuditTimeout` once the deadline has passed.

        Cheap enough to call once per row or per formula inside a check.
        """
        if self.deadline is not None and time.monotonic() > self.deadline:
            raise AuditTimeout(f"audit time budget of {self.seconds:g}s exhausted")


def tick(budget: Budget | None) -> None:
    if budget is not None:
        budget.tick()
