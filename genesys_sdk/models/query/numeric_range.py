from serde import serde


@serde(rename_all='camelcase')
class NumericRange:
    # Greater than
    gt: float | None = None
    # Greater than or equal to
    gte: float | None = None
    # Less than
    lt: float | None = None
    # Less than or equal to
    lte: float | None = None
