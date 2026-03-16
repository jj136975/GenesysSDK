from __future__ import annotations

from datetime import datetime
from serde import serde

from .annotation import Annotation

@serde(rename_all = 'camelcase')
class RecordingMetadata:
    #Annotations that belong to the recording. Populated when recording filestate is AVAILABLE.
    annotations: list[Annotation] | None = None
    #The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    archive_date: datetime | None = None
    #The type of archive medium used. Example: CloudArchive
    archive_medium: str = ""
    #
    conversation_id: str = ""
    #The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    delete_date: datetime | None = None
    #
    end_time: datetime | None = None
    #The date the recording will be exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    export_date: datetime | None = None
    #The date the recording was exported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    exported_date: datetime | None = None
    #Represents the current file state for a recording. Examples: Uploading, Archived, etc
    file_state: str = ""
    #The globally unique identifier for the object.
    id: str = ""
    #How many archive restorations the organization is allowed to have.
    max_allowed_restorations_for_org: int = 0
    #The type of media that the recording is. At the moment that could be audio, chat, email, or message.
    media: str = ""
    #The recording media subject.
    media_subject: str = ""
    #The recording media subtype.
    media_subtype: str = ""
    #
    name: str = ""
    #
    path: str = ""
    #The remaining archive restorations the organization has.
    remaining_restorations_allowed_for_org: int = 0
    #The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    restore_expiration_time: datetime | None = None
    #The URI for this object
    self_uri: str = ""
    #The session id represents an external resource id, such as email, call, chat, etc
    session_id: str = ""
    #The start time of the recording for screen recordings. Null for other types.
    start_time: datetime | None = None
