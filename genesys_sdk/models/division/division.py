from __future__ import annotations

from datetime import datetime

from serde import serde


@serde(rename_all='camelcase')
class DivisionEntityRef:
    # The time the entity division was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    date_division_updated: datetime | None = None
    #
    id: str = ""
    #
    name: str = ""
    #
    self_uri: str = ""
