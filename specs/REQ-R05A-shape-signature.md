# REQ-R05A · Shape signature

**Status:** Frozen from DQ-RCV-URS-001 REQ-R05A / DQ-RCV-DS-001 §6.

Normalisation preserves meaning. The shape signature deliberately discards it.

| Leaf kind | Placeholder |
|---|---|
| field / identifier reference | FIELD |
| string literal | STR |
| numeric literal | NUM |
| null literal | NULL |
| reference-table / dictionary name | REF |
| outcome vocabulary literal | OUTCOME |

Structure preserved: operators, function names, arity and order, n-ary AND/OR child order, unknown-function spelling.

Derived from the normalised primary evaluation closure only.

`A > 10` and `B > 20` must share a signature. `A > 10` and `A >= 10` must not.
