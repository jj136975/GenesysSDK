from __future__ import annotations

from datetime import datetime

from serde import serde

from ..common.conversation_division_membership import ConversationDivisionMembership
from ..common.transfer_response import TransferResponse
from .email_media_participant import EmailMediaParticipant


@serde(rename_all='camelcase')
class EmailConversation:
    # The globally unique identifier for the object.
    id: str = ""
    #
    name: str = ""
    # Identifiers of divisions associated with this conversation.
    divisions: list[ConversationDivisionMembership] | None = None
    # The list of other media channels involved in the conversation.
    other_media_uris: list[str] | None = None
    # The list of participants involved in the conversation.
    participants: list[EmailMediaParticipant] | None = None
    # The list of the most recent 20 transfer commands applied to this conversation.
    recent_transfers: list[TransferResponse] | None = None
    # An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level
    utilization_label_id: str = ""
    # Email-specific: the inactivity timeout for this email conversation.
    inactivity_timeout: datetime | None = None
    # The URI for this object
    self_uri: str = ""
