from __future__ import annotations

RECOGNISED_BUILTINS = {
    "IN", "IIF", "SQL_LIKE", "ISNULL", "DECODE", "LENGTH", "CONCAT",
    "LTRIM", "RTRIM", "SUBSTR", "UPPER", "IS_NUMBER", "TO_INTEGER",
    "REG_MATCH", "TO_CHAR", "INSTR", "TO_DATE", "REPLACECHR", "IS_DATE",
    "LPAD", "TO_DECIMAL", "SYSTIMESTAMP",
}

PARSEABLE_KINDS = frozenset({"expression", "lookup-condition", "filter-condition"})
OPAQUE_KINDS = frozenset({"join-condition", "sql-query", "update-dynamic-cache-condition"})

OUTCOME_LITERALS = {
    "VALID": "VALID",
    "Valid": "VALID",
    "INVALID": "INVALID",
    "Invalid": "INVALID",
    "DONTEVAL": "NOT_EVALUATED",
}

BOUNDED_OUTCOME_VALUES = frozenset(OUTCOME_LITERALS.keys()) | frozenset(OUTCOME_LITERALS.values())

LOGIC_ATTRS = {
    "expression": "expression",
    "lookupCondition": "lookup-condition",
    "filterCondition": "filter-condition",
    "joinCondition": "join-condition",
    "sqlQuery": "sql-query",
    "updateDynamicCacheCondition": "update-dynamic-cache-condition",
}
