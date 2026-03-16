from __future__ import annotations

from datetime import datetime

from serde import serde

from ..common.conversation_routing_data import ConversationRoutingData
from ..common.error_info import ErrorInfo
from ..common.journey_context import JourneyContext
from ..common.wrapup import Wrapup
from .disposition import Disposition
from .fax_status import FaxStatus
from ..domain import DomainEntityRef


@serde(rename_all='camelcase')
class CallMediaParticipant:
    # The participant address.
    address: str = ""
    # Specifies how long the agent has to answer an interaction before being marked as not responding.
    alerting_timeout_ms: int = 0
    # The call ANI.
    ani: str = ""
    # A list of ad-hoc attributes for the participant.
    attributes: dict[str, str] | None = None
    # If this participant barged in a participant's call, then this will be the id of the targeted participant.
    barged_participant_id: str = ""
    # The timestamp when this participant was connected to the barge conference in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    barged_time: datetime | None = None
    # The ID of the participant being coached when performing a call coach.
    coached_participant_id: str = ""
    # Value is true when the call is confined.
    confined: bool = False
    # The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    connected_time: datetime | None = None
    # The ID of the consult transfer target participant when performing a consult transfer.
    consult_participant_id: str = ""
    # Information on how a communication should be routed to an agent.
    conversation_routing_data: ConversationRoutingData | None = None
    # The participant's direction.  Values can be: 'inbound' or 'outbound'
    direction: str = ""
    # The reason the participant was disconnected from the conversation.
    disconnect_type: str = ""
    # Call resolution data for Dialer bulk make calls commands.
    disposition: Disposition | None = None
    # The call DNIS.
    dnis: str = ""
    # The ID of the Content Management document if the call is a fax.
    document_id: str = ""
    # The timestamp when this participant ended after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    end_acw_time: datetime | None = None
    # The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    end_time: datetime | None = None
    # If the conversation ends in error, contains additional error details.
    error_info: ErrorInfo | None = None
    # If this participant represents an external contact, then this will be the reference for the external contact.
    external_contact: DomainEntityRef | None = None
    # If this participant represents an external contact, then this will be the initial division for the external contact. This value will not be updated if the external contact is reassigned.
    external_contact_initial_division_id: str = ""
    # If this participant represents an external org, then this will be the reference for the external org.
    external_organization: DomainEntityRef | None = None
    # Extra fax information if the call is a fax.
    fax_status: FaxStatus | None = None
    # The reason specifying why participant flagged the conversation.
    flagged_reason: str = ""
    # The group involved in the group ring call.
    group: DomainEntityRef | None = None
    # Value is true when the participant is on hold.
    held: bool = False
    # The unique participant ID.
    id: str = ""
    # Journey System data/context that is applicable to this communication.  When used for historical purposes, the context should be immutable.  When null, there is no applicable Journey System context.
    journey_context: JourneyContext | None = None
    # List of roles this participant's media has had on the conversation, ie monitor, coach, etc
    media_roles: list[str] | None = None
    # The ID of the participant being monitored when performing a call monitor.
    monitored_participant_id: str = ""
    # Value is true when the call is muted.
    muted: bool = False
    # The display friendly name of the participant.
    name: str = ""
    # The time when this participant's communication was last parked.  Does not reset on resume. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    park_time: datetime | None = None
    # The peer communication corresponding to a matching leg for this communication.
    peer: str = ""
    # The source provider for the communication.
    provider: str = ""
    # The participant's purpose.  Values can be: 'agent', 'user', 'customer', 'external', 'acd', 'ivr
    purpose: str = ""
    # The PureCloud queue for this participant.
    queue: DomainEntityRef | None = None
    # Value is true when the call is being recorded.
    recording: bool = False
    # The state of the call recording.
    recording_state: str = ""
    # The time when this participant's communications will resume. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    resume_time: datetime | None = None
    # The Engage script that should be used by this participant.
    script: DomainEntityRef | None = None
    # True when the recording of this call is in secure pause status.
    secure_pause: bool = False
    # The timestamp when this participant started after-call work. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    start_acw_time: datetime | None = None
    # The time when this participant's hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    start_hold_time: datetime | None = None
    # The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    start_time: datetime | None = None
    # The participant's state.  Values can be: 'alerting', 'connected', 'disconnected', 'dialing', 'contacting
    state: str = ""
    # The PureCloud team for this participant.
    team: DomainEntityRef | None = None
    # The PureCloud user for this participant.
    user: DomainEntityRef | None = None
    # User-to-User information which maps to a SIP header field defined in RFC7433. UUI data is used in the Public Switched Telephone Network (PSTN) for use cases described in RFC6567.
    uui_data: str = ""
    # Wrapup for this participant, if it has been applied.
    wrapup: Wrapup | None = None
    # The wrap-up prompt indicating the type of wrap-up to be performed.
    wrapup_prompt: str = ""
    # Value is true when the participant requires wrap-up.
    wrapup_required: bool = False
    # Value is true when the participant has skipped wrap-up.
    wrapup_skipped: bool = False
    # The amount of time the participant has to complete wrap-up.
    wrapup_timeout_ms: int = 0
