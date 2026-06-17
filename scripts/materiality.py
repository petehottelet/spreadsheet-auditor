from __future__ import annotations


SEVERITY_ORDER = ["Critical", "High", "Medium", "Low"]


def exceeds_materiality(delta: float | None, absolute: float = 1000.0, relative_base: float | None = None, relative: float = 0.001) -> bool:
    if delta is None:
        return False
    if abs(delta) >= absolute:
        return True
    if relative_base not in (None, 0):
        return abs(delta) / abs(relative_base) >= relative
    return False


def escalate(severity: str) -> str:
    try:
        index = SEVERITY_ORDER.index(severity)
    except ValueError:
        return severity
    return SEVERITY_ORDER[max(0, index - 1)]
