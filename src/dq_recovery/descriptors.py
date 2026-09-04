"""REQ-R05 — rule-type descriptors are data files."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
from typing import Any

class DescriptorError(ValueError):
    pass

def load_descriptors(directory: Path) -> list[dict[str, Any]]:
    descriptors: list[dict[str, Any]] = []
    if not directory.exists():
        return descriptors
    for path in sorted(directory.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        _validate(data)
        descriptors.append(data)
    return descriptors

def _validate(d: dict[str, Any]) -> None:
    for key in ("name", "version", "shape", "parameters", "outcomes"):
        if key not in d:
            raise DescriptorError(f"descriptor missing {key}")
    if not isinstance(d["shape"], str) or not d["shape"]:
        raise DescriptorError(f"descriptor {d.get('name')} has empty shape")

def descriptor_set_hash(descriptors: list[dict[str, Any]]) -> str:
    blob = json.dumps([{"name": d["name"], "version": d["version"], "shape": d["shape"]} for d in descriptors], sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()
