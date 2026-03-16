from __future__ import annotations

from datetime import datetime

from serde import serde

from .analytics_participant_without_attributes import AnalyticsParticipantWithoutAttributes


@serde(rename_all='camelcase')
class AnalyticsResolution:
    # Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    event_time: datetime | None = None
    #
    n_next_contact_avoided: int = 0
    # The ID of the last queue on which the conversation was handled.
    queue_id: str = ""
    # The ID of the last user who handled the conversation.
    user_id: str = ""


@serde(rename_all='camelcase')
class AnalyticsEvaluation:
    # Indicates whether an assignee is applicable for the evaluation. Set to false when assignee is not applicable
    assignee_applicable: bool = False
    # UserId of the assignee
    assignee_id: str = ""
    # The calibration ID used for the purpose of training evaluators
    calibration_id: str = ""
    # A unique identifier for an evaluation form, regardless of version
    context_id: str = ""
    # Whether the evaluation has been deleted
    deleted: bool = False
    # Unique identifier for the evaluation
    evaluation_id: str = ""
    # Status of evaluation
    evaluation_status: str = ""
    # A unique identifier of the user who evaluated the interaction
    evaluator_id: str = ""
    # Specifies when an evaluation occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    event_time: datetime | None = None
    # ID of the evaluation form used
    form_id: str = ""
    # Name of the evaluation form used
    form_name: str = ""
    #
    o_total_critical_score: int = 0
    #
    o_total_score: int = 0
    # The ID of the associated queue
    queue_id: str = ""
    # Whether the evaluation has been released
    released: bool = False
    # Whether the evaluation has been rescored at least once
    rescored: bool = False
    # ID of the agent the evaluation was performed against
    user_id: str = ""


@serde(rename_all='camelcase')
class AnalyticsSurvey:
    # Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    event_time: datetime | None = None
    #
    o_survey_total_score: int = 0
    # The ID of the associated queue
    queue_id: str = ""
    # Completion datetime of the survey in ISO 8601 format
    survey_completed_date: datetime | None = None
    # Unique identifier for the survey form, regardless of version
    survey_form_context_id: str = ""
    # ID of the survey form used
    survey_form_id: str = ""
    # Name of the survey form used
    survey_form_name: str = ""
    # ID of the survey
    survey_id: str = ""
    # Whether the survey was completed with any required questions unanswered.
    survey_partial_response: bool = False
    # Score of the survey used with NPS
    survey_promoter_score: int = 0
    # The status of the survey
    survey_status: str = ""
    # The type of the survey
    survey_type: str = ""
    # ID of the agent the survey was performed against
    user_id: str = ""


@serde(rename_all='camelcase')
class AnalyticsConversationWithoutAttributes:
    # The start time of a conference call. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    conference_start: datetime | None = None
    # The end time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    conversation_end: datetime | None = None
    # Unique identifier for the conversation
    conversation_id: str = ""
    # Indicates the participant purpose of the participant initiating a message conversation
    conversation_initiator: str = ""
    # The start time of a conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    conversation_start: datetime | None = None
    # Indicates a messaging conversation in which the customer participated by sending at least one message
    customer_participation: bool = False
    # Identifier(s) of division(s) associated with a conversation
    division_ids: list[str] | None = None
    # Evaluations associated with this conversation
    evaluations: list[AnalyticsEvaluation] | None = None
    # External tag for the conversation
    external_tag: str = ""
    # The unique identifier(s) of the knowledge base(s) used
    knowledge_base_ids: list[str] | None = None
    # The lowest estimated average MOS among all the audio streams belonging to this conversation
    media_stats_min_conversation_mos: float = 0.0
    # The lowest R-factor value among all of the audio streams belonging to this conversation
    media_stats_min_conversation_r_factor: float = 0.0
    # The original direction of the conversation
    originating_direction: str = ""
    # Participants in the conversation
    participants: list[AnalyticsParticipantWithoutAttributes] | None = None
    # Resolutions associated with this conversation
    resolutions: list[AnalyticsResolution] | None = None
    # Indicates whether all flow sessions were self serviced
    self_served: bool = False
    # Surveys associated with this conversation
    surveys: list[AnalyticsSurvey] | None = None


@serde(rename_all='camelcase')
class AnalyticsConversationWithoutAttributesMultiGetResponse:
    # List of conversations
    conversations: list[AnalyticsConversationWithoutAttributes]
