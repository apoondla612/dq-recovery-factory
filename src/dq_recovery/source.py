"""REQ-R17 input — register a sealed export to a deterministic manifest."""
from __future__ import annotations
import hashlib, json, zipfile
from pathlib import Path
from typing import Any

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def register_export(export_path: Path, dest_dir: Path) -> dict[str, Any]:
    export_path = export_path.resolve()
    dest_dir.mkdir(parents=True, exist_ok=True)
    members: list[dict[str, Any]] = []
    extracted_root = dest_dir / "members"
    extracted_root.mkdir(parents=True, exist_ok=True)
    if export_path.suffix.lower() != ".zip":
        raise ValueError("export must be a zip archive")
    archive_sha = sha256_file(export_path)
    with zipfile.ZipFile(export_path) as zf:
        for info in sorted(zf.infolist(), key=lambda i: i.filename):
            if info.is_dir() or not info.filename.lower().endswith(".xml"):
                continue
            data = zf.read(info.filename)
            parts = Path(info.filename).parts
            out = extracted_root / parts[-2] / parts[-1] if len(parts) >= 2 else extracted_root / Path(info.filename).name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
            members.append({"name": info.filename, "path": str(out.relative_to(dest_dir)), "sha256": sha256_bytes(data), "bytes": len(data)})
    manifest = {"kind": "pilot-source.manifest", "archive": str(export_path), "archive_sha256": archive_sha, "member_count": len(members), "members": members}
    (dest_dir / "pilot-source.manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest

def member_paths(dest_dir: Path, manifest: dict[str, Any]) -> list[Path]:
    return [dest_dir / m["path"] for m in manifest["members"]]
