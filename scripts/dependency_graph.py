from __future__ import annotations

from formula_parser import extract_references
from reference_resolver import expand_reference


def build_dependency_graph(formulas: list[dict], expansion_limit: int = 500) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for item in formulas:
        deps: set[str] = set()
        for ref in extract_references(item["formula"]):
            for loc in expand_reference(ref, item["sheet"], limit=expansion_limit):
                deps.add(loc)
        graph[item["location"]] = deps
    return graph


def find_cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    try:
        import networkx as nx  # type: ignore

        directed = nx.DiGraph()
        for src, deps in graph.items():
            for dep in deps:
                directed.add_edge(src, dep)
        return [list(cycle) for cycle in nx.simple_cycles(directed)]
    except Exception:
        return _find_cycles_dfs(graph)


def _find_cycles_dfs(graph: dict[str, set[str]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> None:
        if node in visiting:
            if node in stack:
                cycles.append(stack[stack.index(node) :] + [node])
            return
        if node in visited:
            return
        visiting.add(node)
        stack.append(node)
        for dep in graph.get(node, set()):
            if dep in graph:
                visit(dep)
        stack.pop()
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)
    return cycles
