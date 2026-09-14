"""Formula dependency graph and cycle detection.

The graph only contains formula cells: a non-formula precedent can never be
part of a cycle, so it is omitted rather than expanded cell by cell. Range
references (including whole-column and whole-row references, clamped to the
sheet's used extent) are resolved against a per-sheet column index, so a
``SUM`` over ten thousand rows costs a few bisections instead of ten thousand
graph nodes. Cycles are reported as strongly connected components, one per
component, which keeps a filled-down self-inclusive total from exploding into
millions of elementary cycles.
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import defaultdict
from collections.abc import Iterator

from .formula_parser import extract_references
from .reference_resolver import clamped_boundaries


def build_dependency_graph(
    formulas: list[dict],
    expansion_limit: int | None = None,
    names=None,
    extents: dict[str, tuple[int, int]] | None = None,
    budget=None,
) -> dict[str, set[str]]:
    """Map each formula location to the formula locations it depends on.

    ``expansion_limit`` is accepted for backward compatibility and ignored:
    ranges are resolved against an index of formula cells, so no reference is
    ever dropped for being large.
    """
    per_sheet: dict[str, dict[int, list[tuple[int, str]]]] = defaultdict(lambda: defaultdict(list))
    max_seen: dict[str, tuple[int, int]] = {}
    for item in formulas:
        key = item["sheet"].casefold()
        per_sheet[key][item["col"]].append((item["row"], item["location"]))
        row_max, col_max = max_seen.get(key, (0, 0))
        max_seen[key] = (max(row_max, item["row"]), max(col_max, item["col"]))
    index: dict[str, dict[int, tuple[list[int], list[str]]]] = {}
    for key, cols in per_sheet.items():
        index[key] = {}
        for col, entries in cols.items():
            entries.sort()
            index[key][col] = ([row for row, _ in entries], [loc for _, loc in entries])
    extent_lookup = {sheet.casefold(): ext for sheet, ext in (extents or {}).items()}

    graph: dict[str, set[str]] = {item["location"]: set() for item in formulas}
    for item in formulas:
        if budget is not None:
            budget.tick()
        deps = graph[item["location"]]
        origin = (item["sheet"], item["row"], item["col"])
        for ref in extract_references(item["formula"], names=names, origin=origin):
            key = (ref.sheet or item["sheet"]).casefold()
            cols = index.get(key)
            if not cols:
                continue
            ext_row, ext_col = extent_lookup.get(key) or max_seen.get(key, (1, 1))
            box = clamped_boundaries(
                ref.ref,
                max_row=max(int(ext_row or 1), 1),
                max_col=max(int(ext_col or 1), 1),
            )
            if box is None:
                continue
            min_col, min_row, max_col, max_row = box
            if max_col - min_col + 1 <= len(cols):
                candidates: Iterator[int] | list[int] = range(min_col, max_col + 1)
            else:
                candidates = [col for col in cols if min_col <= col <= max_col]
            for col in candidates:
                entry = cols.get(col)
                if entry is None:
                    continue
                rows, locations = entry
                lo = bisect_left(rows, min_row)
                hi = bisect_right(rows, max_row)
                if lo < hi:
                    deps.update(locations[lo:hi])
    return graph


def strongly_connected_components(graph: dict[str, set[str]]) -> list[list[str]]:
    """Iterative Tarjan's algorithm; safe on dependency chains thousands deep."""
    index_of: dict[str, int] = {}
    low: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    components: list[list[str]] = []
    counter = 0
    for root in graph:
        if root in index_of:
            continue
        index_of[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        work: list[tuple[str, Iterator[str]]] = [(root, iter(graph.get(root, ())))]
        while work:
            node, neighbours = work[-1]
            advanced = False
            for nxt in neighbours:
                if nxt not in graph:
                    continue
                if nxt not in index_of:
                    index_of[nxt] = low[nxt] = counter
                    counter += 1
                    stack.append(nxt)
                    on_stack.add(nxt)
                    work.append((nxt, iter(graph.get(nxt, ()))))
                    advanced = True
                    break
                if nxt in on_stack:
                    low[node] = min(low[node], index_of[nxt])
            if advanced:
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
            if low[node] == index_of[node]:
                component: list[str] = []
                while True:
                    member = stack.pop()
                    on_stack.discard(member)
                    component.append(member)
                    if member == node:
                        break
                components.append(component)
    return components


def find_cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    """Return one sorted member list per cyclic strongly connected component.

    A single-node component is returned only when the node depends on itself
    (for example a total whose range includes the total cell).
    """
    cycles: list[list[str]] = []
    for component in strongly_connected_components(graph):
        if len(component) > 1 or component[0] in graph.get(component[0], ()):
            cycles.append(sorted(component))
    cycles.sort()
    return cycles
