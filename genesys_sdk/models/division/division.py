from __future__ import annotations

from datetime import datetime

from serde import serde


@serde(rename_all='camelcase')
class DivisionEntityRef:
    #
    id: str = ""
    #
    name: str = ""
    #
    self_uri: str = ""
