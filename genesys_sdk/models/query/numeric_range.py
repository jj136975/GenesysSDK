from serde import serde


@serde(rename_all='camelcase')
class NumericRange:
    # Greater than
    gt: float = 0.0
    # Greater than or equal to
    gte: float = 0.0
    # Less than
    lt: float = 0.0
    # Less than or equal to
    lte: float = 0.0
