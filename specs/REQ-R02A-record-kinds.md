# REQ-R02A · Which records enter the expression grammar

**Status:** Frozen from DQ-RCV-DS-001 §4, regenerated against the sealed ten-export package.

| Kind | Treatment |
|---|---|
| expression | parsed by the Informatica expression grammar |
| lookup-condition | parsed by the Informatica expression grammar |
| filter-condition | parsed by the Informatica expression grammar |
| join-condition | opaque with provenance (row assembly, not validation) |
| sql-query | opaque with provenance |
| update-dynamic-cache-condition | opaque with provenance |

Any kind not in this list is surfaced by accounting and construct discovery. It is never defaulted into the expression grammar.
