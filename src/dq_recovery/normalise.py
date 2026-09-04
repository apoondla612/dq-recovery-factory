"""REQ-R03 / REQ-R04 — apply only the REQ-R02 transformations."""
from __future__ import annotations
import hashlib, json
from typing import Any
from .constants import OUTCOME_LITERALS, RECOGNISED_BUILTINS

def _flatten(op: str, node: dict[str, Any]) -> list[dict[str, Any]]:
    if node.get("op") != op:
        return [normalise_tree(node)]
    out: list[dict[str, Any]] = []
    for child in node.get("args", []):
        out.extend(_flatten(op, child))
    return out

def normalise_tree(node: dict[str, Any] | None) -> dict[str, Any]:
    if not node or not isinstance(node, dict) or "op" not in node:
        raise ValueError("malformed tree rejected by normaliser")
    op = node["op"]
    if op in {"AND", "OR"}:
        return {"op": op, "args": _flatten(op, node)}
    if op == "CALL":
        name = node.get("name", "")
        recognised = bool(node.get("recognised")) or name.upper() in RECOGNISED_BUILTINS
        return {"op": "CALL", "name": name.upper() if recognised else name, "recognised": recognised, "args": [normalise_tree(a) for a in node.get("args", [])]}
    if op == "LKP":
        return {"op": "LKP", "name": node.get("name"), "args": [normalise_tree(a) for a in node.get("args", [])]}
    if op == "IDENT":
        return {"op": "IDENT", "name": node.get("name")}
    if op == "LIT":
        kind, value = node.get("kind"), node.get("value")
        if kind == "string" and value in OUTCOME_LITERALS:
            return {"op": "LIT", "kind": "string", "value": value, "outcome": OUTCOME_LITERALS[value]}
        return {"op": "LIT", "kind": kind, "value": value}
    if op == "OPAQUE":
        return {"op": "OPAQUE", "text": node.get("text", ""), "offset": node.get("offset", 0)}
    if "args" in node:
        return {"op": op, "args": [normalise_tree(a) for a in node.get("args", [])]}
    return {"op": op, **{k: v for k, v in node.items() if k != "op"}}

def canonical_bytes(tree: dict[str, Any]) -> bytes:
    return json.dumps(tree, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def semantic_hash(tree: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(tree)).hexdigest()

def normalise_expression_tree(tree: dict[str, Any]) -> tuple[dict[str, Any], bytes, str]:
    norm = normalise_tree(tree)
    blob = canonical_bytes(norm)
    return norm, blob, hashlib.sha256(blob).hexdigest()
