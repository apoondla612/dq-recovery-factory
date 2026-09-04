"""dq recover — REQ-R17 entry point."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
from .recover import recover

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="dq")
    sub = parser.add_subparsers(dest="cmd", required=True)
    rec = sub.add_parser("recover", help="run stream 1 recovery")
    rec.add_argument("--export", required=True, type=Path)
    rec.add_argument("--out", type=Path, default=Path("artifacts/run"))
    rec.add_argument("--repo", type=Path, default=Path("."))
    args = parser.parse_args(argv)
    if args.cmd == "recover":
        summary = recover(args.export, args.out, args.repo)
        print(json_summary(summary))
        return 0 if summary["ok"] else 1
    return 2

def json_summary(summary: dict) -> str:
    import json
    return json.dumps({"ok": summary["ok"], "elements": summary["elements"], "attributes": summary["attributes"], "records": summary["records"], "primary_rules": summary["primary_rules"], "companions": summary["companions"], "clusters": summary["clusters"], "questions": summary["questions"], "rule_failures": len(summary["rule_failures"])}, indent=2)

if __name__ == "__main__":
    sys.exit(main())
