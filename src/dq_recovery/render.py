"""REQ-R10 — render a canonical tree back to an Informatica-equivalent expression."""
from __future__ import annotations
from typing import Any

_PREC = {"OR": 1, "AND": 2, "=": 3, "<>": 3, "!=": 3, "^=": 3, "<": 4, "<=": 4, ">": 4, ">=": 4, "||": 5, "+": 6, "-": 6, "*": 7, "/": 7, "%": 7, "NOT": 8, "U+": 9, "U-": 9, "CALL": 10, "LKP": 10, "IDENT": 11, "LIT": 11}

def _prec(node: dict[str, Any]) -> int:
    return _PREC.get(node.get("op"), 0)

def _wrap(child: dict[str, Any], parent_prec: int) -> str:
    text = render(child)
    return f"({text})" if _prec(child) < parent_prec else text

def render(node: dict[str, Any]) -> str:
    op = node.get("op")
    if op == "LIT":
        if node.get("kind") == "string":
            return "'" + (node.get("value") or "").replace("'", "''") + "'"
        if node.get("kind") == "null":
            return "NULL"
        if node.get("kind") == "empty":
            return ""
        if node.get("kind") == "bool":
            return str(node.get("value"))
        return str(node.get("value"))
    if op == "IDENT":
        return str(node.get("name"))
    if op == "CALL":
        return f"{node.get('name')}({','.join(render(a) for a in node.get('args', []))})"
    if op == "LKP":
        return f"{node.get('name')}({','.join(render(a) for a in node.get('args', []))})"
    if op == "NOT":
        return f"NOT {_wrap(node['args'][0], _PREC['NOT'])}"
    if op in {"U+", "U-"}:
        return f"{op[1]}{_wrap(node['args'][0], _PREC[op])}"
    if op in {"AND", "OR"}:
        return f" {op} ".join(_wrap(a, _PREC[op]) for a in node.get("args", []))
    if op == "OPAQUE":
        return node.get("text", "")
    if "args" in node and len(node["args"]) == 2:
        prec = _PREC.get(op, 0)
        return f"{_wrap(node['args'][0], prec)} {op} {_wrap(node['args'][1], prec)}"
    raise ValueError(f"cannot render op={op}")
