# REQ-R02 · What normalisation removes

**Status:** Frozen from DQ-RCV-URS-001 / DQ-RCV-DS-001 v1.0.
**Owner:** Architecture. Implementation applies this table and nothing else.

## Precedence (tightest first)

| Level | Operators | Reordering |
|---|---|---|
| 1 | parentheses | — |
| 2 | unary `+` `-` `NOT` | never |
| 3 | `*` `/` `%` | never |
| 4 | `+` `-` | never |
| 5 | `||` string concatenation | never |
| 6 | `<` `<=` `>` `>=` | never |
| 7 | `=` `<>` `!=` `^=` | not initially |
| 8 | `AND` | flatten, ordered, never sorted |
| 9 | `OR` | flatten, ordered, never sorted |

`IN(...)` is a function-like construct, not a binary operator.
`%`, `<>` and `^=` are supported. They are never reordered.

## Removed

- Whitespace and formatting between tokens
- Redundant parentheses
- Nesting of boolean AND and OR, flattened to an ordered n-ary node. Child order preserved. Operands never sorted.
- Function-name case for the 22 recognised built-ins only

## Not removed

- Operand order for `=` and `!=`, comparisons, arithmetic, IN lists, function args
- Comments (lexer trivia)
- Whitespace inside string literals, identifier case, null-handling form, empty-string versus null
- Unknown and external identifier spelling, `:LKP.*` invocations

## Outcome literals

Handle `Valid` and `Invalid` explicitly. Canonical universe: VALID, INVALID, NOT_EVALUATED.

## Recognised built-ins (22)

IN, IIF, SQL_LIKE, ISNULL, DECODE, LENGTH, CONCAT, LTRIM, RTRIM, SUBSTR, UPPER, IS_NUMBER, TO_INTEGER, REG_MATCH, TO_CHAR, INSTR, TO_DATE, REPLACECHR, IS_DATE, LPAD, TO_DECIMAL, SYSTIMESTAMP

## Assumption

Do not reorder `=` / `!=`. Side-effect question is not ratified.
