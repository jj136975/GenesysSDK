from __future__ import annotations

from datetime import datetime

from serde import serde


@serde(rename_all='camelcase')
class AnalyticsProperty:
    # User-defined rather than intrinsic system-observed values. These are tagged onto segments by other components within PureCloud or by API users directly.  This is the name of the user-defined property.
    pcProperty: str = ""
    # Indicates what the data type is (e.g. integer vs string) and therefore how to evaluate what would constitute a match
    property_type: str = ""
    # What property value to match against
    value: str = ""


@serde(rename_all='camelcase')
class AnalyticsScoredAgent:
    # Assigned agent score for this conversation (0 - 100, higher being better)
    agent_score: int = 0
    # Unique identifier for the agent that was scored for this conversation
    scored_agent_id: str = ""


@serde(rename_all='camelcase')
class AnalyticsConversationSegment:
    # Flag indicating if audio is muted or not (true/false)
    audio_muted: bool = False
    # Indicates whether the segment was a conference
    conference: bool = False
    # The unique identifier of a new conversation when a conversation is ended for a conference
    destination_conversation_id: str = ""
    # The unique identifier of a new session when a session is ended for a conference
    destination_session_id: str = ""
    # The session disconnect type
    disconnect_type: str = ""
    # A code corresponding to the error that occurred
    error_code: str = ""
    # Unique identifier for a Genesys Cloud group
    group_id: str = ""
    # Additional segment properties
    properties: list[AnalyticsProperty] | None = None
    # Q.850 response code(s)
    q850_response_codes: list[int] | None = None
    # Queue identifier
    queue_id: str = ""
    # Unique identifier for the language requested for an interaction
    requested_language_id: str = ""
    # Unique identifier(s) for skill(s) requested for an interaction
    requested_routing_skill_ids: list[str] | None = None
    # Unique identifier(s) for agent(s) requested for an interaction
    requested_routing_user_ids: list[str] | None = None
    # Scored agents
    scored_agents: list[AnalyticsScoredAgent] | None = None
    # The end time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    segment_end: datetime | None = None
    # The start time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    segment_start: datetime | None = None
    # The activity that takes place in the segment, such as hold or interact
    segment_type: str = ""
    # SIP response code(s)
    sip_response_codes: list[int] | None = None
    # The unique identifier of the previous conversation when a new conversation is created for a conference
    source_conversation_id: str = ""
    # The unique identifier of the previous session when a new session is created for a conference
    source_session_id: str = ""
    # The subject for the initial email that started this conversation
    subject: str = ""
    # Flag indicating if video is muted/paused or not (true/false)
    video_muted: bool = False
    # Wrap up code
    wrap_up_code: str = ""
    # Note entered by an agent during after-call work
    wrap_up_note: str = ""
    # Tag(s) assigned during after-call work
    wrap_up_tags: list[str] | None = None
