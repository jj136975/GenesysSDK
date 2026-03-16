from __future__ import annotations

from dataclasses import dataclass

from serde import serde

@dataclass
class Annotation:
    #Duration of annotation (milliseconds).
    absolute_duration_ms: int = 0
    #Offset of annotation (milliseconds) from start of recording (after removing the cumulative duration of all pauses).
    absolute_location: int = 0
    #List of annotations
    annotations: list['Annotation'] | None = None
    #Text of annotation. Maximum character limit is 500.
    description: str = ""
    #Duration of annotation in milliseconds.
    duration_ms: int = 0
    #Annotation id. All pause annotations on a recording will share an ID value, bookmark annotations will have unique IDs, and hold annotations will have randomly generated UUIDs (i.e. the ID will change at each request).
    id: str = ""
    #Offset of annotation in milliseconds.
    location: int = 0
    #
    name: str = ""
    #Offset of annotation (milliseconds) from start of the recording before removing the cumulative duration of all pauses before this annotation
    realtime_location: int = 0
    #Reason for a pause annotation. Valid values: Hold,SecurePause,FlowOrQueue,Pause
    reason: str = ""
    #Duration of annotation (milliseconds), adjusted for any recording cuts.
    recording_duration_ms: int = 0
    #Offset of annotation (milliseconds) from start of recording, adjusted for any recording cuts
    recording_location: int = 0
    #The URI for this object
    self_uri: str = ""
    #
    type: str = ""

serde(rename_all = 'camelcase')(Annotation)