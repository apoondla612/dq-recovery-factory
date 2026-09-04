"""REQ-R07 / REQ-R08 — match a shape to descriptors; emit both readings on ambiguity."""
from __future__ import annotations
from typing import Any

def match_rule(shape: str, parse_status: str, descriptors: list[dict[str, Any]]) -> dict[str, Any]:
    candidates = [d for d in descriptors if d.get("shape") == shape]
    if parse_status != "complete":
        return {"recovery_status": "partial", "matches": [d["name"] for d in candidates], "reason": f"parse_status={parse_status} caps match"}
    if not candidates:
        return {"recovery_status": "unmatched", "matches": []}
    if len(candidates) == 1:
        return {"recovery_status": "matched", "matches": [candidates[0]["name"]], "descriptor": candidates[0]["name"], "parameters": candidates[0].get("parameters", [])}
    return {"recovery_status": "semantic_ambiguity", "matches": [d["name"] for d in candidates], "ambiguity": {"readings": [{"descriptor": d["name"], "reading": d.get("reading", d["name"])} for d in candidates]}}
