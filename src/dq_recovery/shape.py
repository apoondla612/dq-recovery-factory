"""REQ-R05B — shape signature from a normalised primary closure."""
from __future__ import annotations
import json
from typing import Any
from .constants import OUTCOME_LITERALS

def _shape(node: dict[str, Any]) -> Any:
    op = node.get("op")
    if op == "IDENT":
        return "FIELD"
    if op == "LIT":
        kind, value = node.get("kind"), node.get("value")
        if kind == "string" and (value in OUTCOME_LITERALS or node.get("outcome")):
            return "OUTCOME"
        if kind == "null":
            return "NULL"
        if kind == "number":
            return "NUM"
        return "STR"
    if op == "LKP":
        return ["LKP", "REF", [_shape(a) for a in node.get("args", [])]]
    if op == "CALL":
        return [node.get("name"), [_shape(a) for a in node.get("args", [])]]
    if op == "OPAQUE":
        return "OPAQUE"
    if "args" in node:
        return [op, [_shape(a) for a in node.get("args", [])]]
    return [op]

def shape_signature(tree: dict[str, Any]) -> str:
    return json.dumps(_shape(tree), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
