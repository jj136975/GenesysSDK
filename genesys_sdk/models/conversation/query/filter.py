from __future__ import annotations

from serde import serde

from ...query.numeric_range import NumericRange


@serde(rename_all='camelcase')
class QueryClause[T]:
    # Like a three-word sentence: (attribute-name) (operator) (target-value).
    predicates: list[T] | None = None
    # Boolean operation to apply to the provided predicates
    type: str | None = None


@serde(rename_all='camelcase')
class QueryFilter[T]:
    # Boolean 'and/or' logic with up to two-levels of nesting
    clauses: list[QueryClause[T]] | None = None
    # Like a three-word sentence: (attribute-name) (operator) (target-value).
    predicates: list[T] | None = None
    # Boolean operation to apply to the provided predicates and clauses
    type: str | None = None


@serde(rename_all='camelcase')
class ConversationDetailQueryPredicate:
    # Left hand side for dimension predicates
    dimension: str | None = None
    # Left hand side for metric predicates
    metric: str | None = None
    # Optional operator, default is matches
    operator: str | None = None
    # Right hand side for dimension or metric predicates
    range: NumericRange | None = None
    # Optional type, can usually be inferred
    type: str | None = None
    # Right hand side for dimension or metric predicates
    value: str | None = None


@serde(rename_all='camelcase')
class EvaluationDetailQueryPredicate:
    # Left hand side for dimension predicates
    dimension: str | None = None
    # Left hand side for metric predicates
    metric: str | None = None
    # Optional operator, default is matches
    operator: str | None = None
    # Right hand side for dimension or metric predicates
    range: NumericRange | None = None
    # Optional type, can usually be inferred
    type: str | None = None
    # Right hand side for dimension or metric predicates
    value: str | None = None


@serde(rename_all='camelcase')
class ResolutionDetailQueryPredicate:
    # Left hand side for metric predicates
    metric: str | None = None
    # Optional operator, default is matches
    operator: str | None = None
    # Right hand side for metric predicates
    range: NumericRange | None = None
    # Optional type, can usually be inferred
    type: str | None = None
    # Right hand side for metric predicates
    value: str | None = None


@serde(rename_all='camelcase')
class SegmentDetailQueryPredicate:
    # Left hand side for dimension predicates
    dimension: str | None = None
    # # Left hand side for metric predicates
    metric: str | None = None
    # # Optional operator, default is matches
    operator: str | None = None
    # # Left hand side for property predicates
    pcProperty: str | None = None
    # # Left hand side for property predicates
    property_type: str | None = None
    # # Right hand side for dimension, metric, or property predicates
    range: NumericRange | None = None
    # # Optional type, can usually be inferred
    type: str | None = None
    # Right hand side for dimension, metric, or property predicates
    value: str | None = None


@serde(rename_all='camelcase')
class SurveyDetailQueryPredicate:
    # Left hand side for dimension predicates
    dimension: str | None = None
    # Left hand side for metric predicates
    metric: str | None = None
    # Optional operator, default is matches
    operator: str | None = None
    # Right hand side for dimension or metric predicates
    range: NumericRange | None = None
    # Optional type, can usually be inferred
    type: str | None = None
    # Right hand side for dimension or metric predicates
    value: str | None = None
