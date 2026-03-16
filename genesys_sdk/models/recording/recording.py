from __future__ import annotations

from datetime import datetime
from serde import serde

from .annotation import Annotation
from .media_result import MediaResult

@serde(rename_all = 'camelcase')
class Recording:
    #
    actual_transcode_time_ms: int = 0
    #Annotations that belong to the recording.
    annotations: list[Annotation] | None = None
    #The date the recording will be archived. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    archive_date: datetime | None = None
    #The type of archive medium used. Example: CloudArchive
    archive_medium: str = ""
    #
    conversation_id: str = ""
    #The creation time of the recording. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    creation_time: datetime | None = None
    #The date the recording will be deleted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    delete_date: datetime | None = None
    #The end time of the recording. Null when there is no playable media.
    end_time: datetime | None = None
    #
    estimated_transcode_time_ms: int = 0
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
    #The media type of the recording. This could be audio, chat, messaging, email, or screen.
    media: str = ""
    #The media subject of the recording.
    media_subject: str = ""
    #The media subtype of the recording.
    media_subtype: str = ""
    #The different mediaUris for the recording. Null when there is no playable media.
    media_uris: dict[str, MediaResult] | None = None
    #
    name: str = ""
    #The start time of the full recording, before any segment access restrictions are applied. Null when there is no playable media. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    original_recording_start_time: datetime | None = None
    #Duration of transcoded media in milliseconds
    output_duration_ms: int = 0
    #Size of transcoded media in bytes. 0 if there is no transcoded media.
    output_size_in_bytes: int = 0
    #
    path: str = ""
    #Status of a recording that cannot be returned because of an error
    recording_error_status: str = ""
    #Role of the file recording. It can be either customer_experience or adhoc.
    recording_file_role: str = ""
    #The remaining archive restorations the organization has.
    remaining_restorations_allowed_for_org: int = 0
    #The amount of time a restored recording will remain restored before being archived again. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    restore_expiration_time: datetime | None = None
    #The URI for this object
    self_uri: str = ""
    #The session id represents an external resource id, such as email, call, chat, etc
    session_id: str = ""
    #The start time of the recording. Null when there is no playable media.
    start_time: datetime | None = None
