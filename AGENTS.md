# Agent operating model

You are implementing DQ-RCV-URS-001 / DQ-RCV-DS-001. Those documents, plus `specs/`, are inputs. They are not yours to edit unless a human opens a specification change.

## Loop

1. Read the requirement and its must-not list.
2. Change only factory code or add a regression fixture.
3. Run the named acceptance command. It exits 0 or you are not done.
4. If a gate is wrong, stop. Do not weaken it. File the discrepancy.

## Must not

- Invent an acceptance criterion.
- Edit specs/ to match an implementation.
- Default an unclassified record kind into the expression grammar.
- Cluster on semantic hash.
- Report a record as matched when parse_status is not complete.
- Put Informatica or Snowflake tokens in rules/*/semantics.
- Name a rule type.
- Choose between two readings. Emit both.
- Stop the run because one rule failed.
- Depend on network or on state outside the working directory.

## Proof

The sealed zip under packages/ is the oracle when present. A change that cannot be shown on that zip is not a baseline change.
