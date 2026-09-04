# REQ-R00 · What a rule is

**Status:** Frozen from DQ-RCV-URS-001 v1.0 and DQ-RCV-DS-001 v1.0 (3 Sep 2026).
**Owner:** Data Quality Platform Architecture. Not an implementation deliverable.

## Decision

A rule is **one governed validation outcome produced by a source validation unit**.

- A **primary outcome endpoint** identifies it.
- Companion description outputs and subordinate expressions, filters and lookups are supporting logic within it.
- Identity is **owning object path plus primary endpoint**. Evidence record identifiers are retained separately.

## Primary endpoint test

The endpoint whose expression returns values from a bounded outcome vocabulary:

`VALID`, `Valid`, `INVALID`, `Invalid`, `DONTEVAL`

A companion returns free-form text. Derived from the expression, not from naming convention.

Ambiguous cases are flagged for ratification, never assigned.

## Closure

Backward reachability over the port dependency graph from the primary endpoint. A variable port reachable from two endpoints is shared supporting logic and recorded against both.

## Must not

- Treat one output port as one rule (`o_Status` and `o_Status_Description` are one validation).
- Rely on naming conventions such as `o_Status` as the test.
- Use object path alone as identity.
