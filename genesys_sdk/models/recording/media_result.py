from __future__ import annotations

from serde import serde

@serde(rename_all = 'camelcase')
class MediaResult:
    # Link to the downloadable media file
    media_uri: str = ""
    # Removed for memory reasons
    # waveform_data: list[float] | None = None
