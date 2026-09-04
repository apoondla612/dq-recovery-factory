# Recovery Factory (stream 1)

Implementation of **DQ-RCV-URS-001** and **DQ-RCV-DS-001** against the sealed ten-mapping pilot export `Test-Mappings-Export`.

The two documents are the system of record. Specs under `specs/` are those documents sliced into the six human-owned decisions. Code implements them. Code does not rewrite them to make a test pass.

## One command

```bash
PYTHONPATH=src python -m dq_recovery.cli recover \
  --export packages/Test-Mappings-Export.zip \
  --out artifacts/proof \
  --repo .
```

## Proof on the sealed zip (this workspace run)

| Denominator | Value |
|---|---|
| Structural elements | 52,313 |
| Structural attributes | 249,774 |
| Non-whitespace text nodes | 0 |
| Technical-logic records | 2,764 |
| Primary rules (REQ-R00) | 108 |
| Companions | 336 |
| Ambiguous endpoints | 65 |
| Shape clusters | 81 |
| Round-trip passed | 108 / 108 |
| Matched rule types | 0 (naming is ratification; none named) |

Record kinds regenerated from the zip: expression 2,084, lookup-condition 235, filter-condition 5, join-condition 11, sql-query 194, update-dynamic-cache-condition 235.

## Agentic rule

An agent may change code and tests. An agent may not author acceptance criteria, rewrite `specs/`, name a rule type, choose a reading, or relax a gate.
