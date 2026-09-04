"""REQ-R01 — prove nothing was dropped."""
from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
from lxml import etree

def load_catalog(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

@dataclass
class AccountingReport:
    elements_read: int
    attributes_read: int
    text_non_whitespace: int
    elements_mapped: int
    elements_marked_unknown: int
    elements_explicitly_ignored: int
    attributes_mapped: int
    attributes_evidence_only: int
    attributes_marked_unknown: int
    attributes_explicitly_ignored: int
    text_mapped: int
    text_marked_unknown: int
    text_explicitly_ignored: int
    unknown_elements: list[str]
    unknown_attributes: list[str]
    ok: bool
    failures: list[str]

EVIDENCE_ONLY_ATTRS = frozenset({"id", "idref"})

def account_files(xml_paths: list[Path], catalog: dict[str, Any]) -> AccountingReport:
    known_elems = set(catalog.get("element_names", []))
    known_attrs = set(catalog.get("attribute_local_names", []))
    ign_elems = set(catalog.get("explicitly_ignored_elements", []))
    ign_attrs = set(catalog.get("explicitly_ignored_attributes", []))
    e_read = a_read = text_nw = 0
    e_map = e_unk = e_ign = 0
    a_map = a_evi = a_unk = a_ign = 0
    t_map = t_unk = t_ign = 0
    unk_e: list[str] = []
    unk_a: list[str] = []
    for path in xml_paths:
        tree = etree.parse(str(path))
        for el in tree.iter():
            e_read += 1
            ln = etree.QName(el).localname
            if ln in ign_elems:
                e_ign += 1
            elif ln in known_elems:
                e_map += 1
            else:
                e_unk += 1
                if ln not in unk_e:
                    unk_e.append(ln)
            for k in el.attrib:
                a_read += 1
                kn = etree.QName(k).localname
                if kn in ign_attrs:
                    a_ign += 1
                elif kn in EVIDENCE_ONLY_ATTRS:
                    a_evi += 1
                elif kn in known_attrs:
                    a_map += 1
                else:
                    a_unk += 1
                    if kn not in unk_a:
                        unk_a.append(kn)
            if el.text and el.text.strip():
                text_nw += 1
                t_map += 1
    failures: list[str] = []
    if e_map + e_unk + e_ign != e_read:
        failures.append("element_denominator mismatch")
    if a_map + a_evi + a_unk + a_ign != a_read:
        failures.append("attribute_denominator mismatch")
    if t_map + t_unk + t_ign != text_nw:
        failures.append("text_denominator mismatch")
    return AccountingReport(
        elements_read=e_read, attributes_read=a_read, text_non_whitespace=text_nw,
        elements_mapped=e_map, elements_marked_unknown=e_unk, elements_explicitly_ignored=e_ign,
        attributes_mapped=a_map, attributes_evidence_only=a_evi, attributes_marked_unknown=a_unk,
        attributes_explicitly_ignored=a_ign, text_mapped=t_map, text_marked_unknown=t_unk,
        text_explicitly_ignored=t_ign, unknown_elements=unk_e, unknown_attributes=unk_a,
        ok=not failures, failures=failures,
    )

def report_as_dict(report: AccountingReport) -> dict[str, Any]:
    return asdict(report)
