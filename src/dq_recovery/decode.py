"""Source-adapter decode contract. XML unescape then exactly one unquote_plus."""

from __future__ import annotations
from urllib.parse import unquote_plus


def decode_expression(raw: str | None) -> str:
    if raw is None:
        return ""
    return unquote_plus(raw)


def decode_pair(raw: str | None) -> tuple[str | None, str]:
    return raw, decode_expression(raw)
