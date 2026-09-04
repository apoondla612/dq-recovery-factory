"""REQ-R02C — bind identifiers to the structure map."""
from __future__ import annotations
from typing import Any

def _walk(node: dict[str, Any], visitor) -> None:
    visitor(node)
    for child in node.get("args", []):
        if isinstance(child, dict):
            _walk(child, visitor)

def bind_tree(tree: dict[str, Any], ports_by_name: dict[str, list[dict[str, Any]]], scope_parent: str | None = None) -> dict[str, Any]:
    unresolved: list[str] = []
    multiply: list[str] = []
    def visit(node: dict[str, Any]) -> None:
        if node.get("op") != "IDENT":
            return
        name = node.get("name")
        hits = ports_by_name.get(name, [])
        if scope_parent:
            scoped = [h for h in hits if h.get("parent") == scope_parent]
            if scoped:
                hits = scoped
        if not hits:
            node["binding"] = None
            unresolved.append(name)
            return
        if len(hits) > 1:
            node["binding"] = {"candidates": [h["id"] for h in hits]}
            multiply.append(name)
            return
        hit = hits[0]
        node["binding"] = {"id": hit.get("id"), "name": hit.get("name"), "type": hit.get("type"), "element": hit.get("element")}
    bound = _copy(tree)
    _walk(bound, visit)
    status = "complete" if not (unresolved or multiply) else "partial"
    return {"tree": bound, "bind_status": status, "unresolved": unresolved, "multiply": multiply}

def _copy(node: dict[str, Any]) -> dict[str, Any]:
    out = {k: v for k, v in node.items() if k != "args"}
    if "args" in node:
        out["args"] = [_copy(a) if isinstance(a, dict) else a for a in node["args"]]
    return out

def index_ports(member: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    idx: dict[str, list[dict[str, Any]]] = {}
    for p in member.get("ports", {}).values():
        idx.setdefault(p["name"], []).append(p)
    return idx
