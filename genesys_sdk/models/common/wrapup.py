from __future__ import annotations

from datetime import datetime

from serde import serde


@serde(rename_all='camelcase')
class Wrapup:
    # The user configured wrap up code id.
    code: str = ""
    # The length of time in seconds that the agent spent doing after call work.
    duration_seconds: int = 0
    # The timestamp when the wrapup was finished. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    end_time: datetime | None = None
    # The user configured wrap up code name.
    name: str = ""
    # Text entered by the agent to describe the call or disposition.
    notes: str = ""
    # Indicates if this is a pending save and should not require a code to be specified.  This allows someone to save some temporary wrapup that will be used later.
    provisional: bool = False
    # List of tags selected by the agent to describe the call or disposition.
    tags: list[str] | None = None
