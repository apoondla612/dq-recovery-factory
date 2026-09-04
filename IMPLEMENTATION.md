# Implementation map

Each URS requirement has one owner module and one acceptance command.
Implementation proceeds in this order. Do not skip to matching.

| REQ | Module | Acceptance |
|---|---|---|
| R00 | specs/REQ-R00-rule-identity.md (frozen) | reviewed spec |
| R01 | src/dq_recovery/accounting.py | python -m unittest tests.test_accounting |
| R02 | specs/REQ-R02-normalisation.md (frozen) | reviewed spec |
| R02A | specs/REQ-R02A-record-kinds.md (frozen) | reviewed spec |
| R02B | src/dq_recovery/parser.py | python -m unittest tests.test_expression_parser |
| R02C | src/dq_recovery/binding.py | python -m unittest tests.test_binding |
| R03 / R04 | src/dq_recovery/normalise.py | tests.test_normalise / test_normalise_determinism |
| R05 | src/dq_recovery/descriptors.py | tests.test_ruletype_descriptors |
| R05A | specs/REQ-R05A-shape-signature.md (frozen) | reviewed spec |
| R05B | src/dq_recovery/shape.py | tests.test_shape_signature |
| R06 | recover.py clusters | tests.test_clustering |
| R07 / R08 | src/dq_recovery/matcher.py | tests.test_matcher / test_ambiguity |
| R09 | src/dq_recovery/emit.py | tests.test_emit |
| R10 | src/dq_recovery/render.py | tests.test_render |
| R11 | recover + render | tests.test_roundtrip |
| R12 / R12A | deferred | needs semantics spec first |
| R13-R16 | recover.py | construct_matrix / coverage / questions / run_record |
| R17 | src/dq_recovery/cli.py | dq recover --export packages/Test-Mappings-Export.zip |
| R18 | after first measured run | not yet gated |

Tests that need the sealed zip skip when it is absent.
