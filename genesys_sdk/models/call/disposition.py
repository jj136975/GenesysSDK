from __future__ import annotations

from datetime import datetime

from serde import serde

from .disposition_parameters import DispositionParameters


@serde(rename_all='camelcase')
class Disposition:
    # The final media analyzer result that triggered the disposition result, if any.
    analyzer: str = ""
    # Absolute time when the speech ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    detected_speech_end: datetime | None = None
    # Absolute time when the speech started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    detected_speech_start: datetime | None = None
    # Contains various parameters related to call analysis.
    disposition_parameters: DispositionParameters | None = None
    # Name of the disposition. Either a platform predefined value, or the name of the disposition in the disposition table..
    name: str = ""
