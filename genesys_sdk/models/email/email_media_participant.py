from __future__ import annotations

from datetime import datetime

from serde import serde

from ..common.conversation_routing_data import ConversationRoutingData
from ..common.error_info import ErrorInfo
from ..common.journey_context import JourneyContext
from ..common.wrapup import Wrapup
from ..domain import DomainEntityRef
from .attachment import Attachment


@serde(rename_all='camelcase')
class EmailMediaParticipant:
    # The participant address.
    address: str = ""
    # Specifies how long the agent has to answer an interaction before being marked as not responding.
    alerting_timeout_ms: int = 0
    # A list of ad-hoc attributes for the participant.
    attributes: dict[str, str] | None = None
    # The time when this participant went connected for this media.
    connected_time: datetime | None = None
    # Information on how a communication should be routed to an agent.
    conversation_routing_data: ConversationRoutingData | None = None
    # The participant's direction.  Values can be: 'inbound' or 'outbound'
    direction: str = ""
    # The reason the participant was disconnected from the conversation.
    disconnect_type: str = ""
    # Email-specific: draft attachments for this participant.
    draft_attachments: list[Attachment] | None = None
    # The timestamp when this participant ended after-call work.
    end_acw_time: datetime | None = None
    # The time when this participant went disconnected for this media.
    end_time: datetime | None = None
    # If the conversation ends in error, contains additional error details.
    error_info: ErrorInfo | None = None
    # If this participant represents an external contact, then this will be the reference for the external contact.
    external_contact: DomainEntityRef | None = None
    # If this participant represents an external contact, then this will be the initial division for the external contact.
    external_contact_initial_division_id: str = ""
    # If this participant represents an external org, then this will be the reference for the external org.
    external_organization: DomainEntityRef | None = None
    # The reason specifying why participant flagged the conversation.
    flagged_reason: str = ""
    # Value is true when the participant is on hold.
    held: bool = False
    # The unique participant ID.
    id: str = ""
    # Journey System data/context that is applicable to this communication.
    journey_context: JourneyContext | None = None
    # List of roles this participant's media has had on the conversation, ie monitor, coach, etc
    media_roles: list[str] | None = None
    # Email-specific: the message ID.
    message_id: str = ""
    # Email-specific: the number of messages sent.
    messages_sent: int = 0
    # Email-specific: whether the message was auto-generated.
    auto_generated: bool = False
    # The display friendly name of the participant.
    name: str = ""
    # The time when this participant's communication was last parked.
    park_time: datetime | None = None
    # The peer communication corresponding to a matching leg for this communication.
    peer: str = ""
    # The source provider for the communication.
    provider: str = ""
    # The participant's purpose.
    purpose: str = ""
    # The PureCloud queue for this participant.
    queue: DomainEntityRef | None = None
    # The time when this participant's communications will resume.
    resume_time: datetime | None = None
    # The Engage script that should be used by this participant.
    script: DomainEntityRef | None = None
    # Email-specific: whether the message is spam.
    spam: bool = False
    # The timestamp when this participant started after-call work.
    start_acw_time: datetime | None = None
    # The time when this participant's hold started.
    start_hold_time: datetime | None = None
    # The time when this participant first joined the conversation.
    start_time: datetime | None = None
    # The participant's state.
    state: str = ""
    # Email-specific: the subject of the email.
    subject: str = ""
    # The PureCloud team for this participant.
    team: DomainEntityRef | None = None
    # The PureCloud user for this participant.
    user: DomainEntityRef | None = None
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
