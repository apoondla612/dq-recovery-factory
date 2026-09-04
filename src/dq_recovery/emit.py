"""REQ-R09 — write one canonical rule file. Semantics contain no vendor tokens."""
from __future__ import annotations
import json, re
from pathlib import Path
from typing import Any

VENDOR = re.compile(r"informatica|powercenter|idq|idmc|snowflake|mapplet|lookupcondition", re.IGNORECASE)

def emit_rule(rule: dict[str, Any], dest: Path) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    payload = {"semantics": rule["semantics"], "bindings": rule["bindings"], "evidence": rule["evidence"]}
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if VENDOR.search(json.dumps(payload["semantics"])):
        raise ValueError(f"vendor token in semantics for {rule.get('identity')}")
    path = dest / f"{_safe(rule['identity'])}.json"
    path.write_text(text, encoding="utf-8")
    return path

def _safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name)[:180]

def vendor_scan(rules_dir: Path) -> list[str]:
    hits: list[str] = []
    if not rules_dir.exists():
        return hits
    for path in rules_dir.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        if VENDOR.search(json.dumps(data.get("semantics", {}))):
            hits.append(str(path))
    return hits
