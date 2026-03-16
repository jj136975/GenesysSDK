from __future__ import annotations

from serde import serde


@serde(rename_all='camelcase')
class AggregationResultEntry:
    #
    count: int = 0
    # For numericRange aggregations
    gte: float = 0.0
    # For numericRange aggregations
    lt: float = 0.0
    # For termFrequency aggregations
    value: str = ""


@serde(rename_all='camelcase')
class AggregationResult:
    #
    count: int = 0
    # For termFrequency aggregations
    dimension: str = ""
    # For numericRange aggregations
    metric: str = ""
    #
    results: list[AggregationResultEntry] | None = None
    #
    type: str = ""
