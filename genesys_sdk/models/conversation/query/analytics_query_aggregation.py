from __future__ import annotations

from serde import serde


@serde(rename_all='camelcase')
class AggregationRange:
    # Greater than or equal to
    gte: float = 0.0
    # Less than
    lt: float = 0.0


@serde(rename_all='camelcase')
class AnalyticsQueryAggregation:
    # For use with termFrequency aggregations
    dimension: str = ""
    # For use with numericRange aggregations
    metric: str = ""
    # For use with numericRange aggregations
    ranges: list[AggregationRange] | None = None
    # For use with termFrequency aggregations
    size: int = 0
    # Optional type, can usually be inferred
    type: str = ""
