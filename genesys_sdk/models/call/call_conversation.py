from __future__ import annotations

from serde import serde

from .call_media_participant import CallMediaParticipant
from ..common.conversation_division_membership import ConversationDivisionMembership
from ..common.transfer_response import TransferResponse


@serde(rename_all='camelcase')
class CallConversation:
    # Identifiers of divisions associated with this conversation.
    divisions: list[ConversationDivisionMembership] | None = None
    # The globally unique identifier for the object.
    id: str = ""
    # If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference.
    max_participants: int = 0
    #
    name: str = ""
    # The list of other media channels involved in the conversation.
    other_media_uris: list[str] | None = None
    # The list of participants involved in the conversation.
    participants: list[CallMediaParticipant] | None = None
    # The list of the most recent 20 transfer commands applied to this conversation.
    recent_transfers: list[TransferResponse] | None = None
    #
    recording_state: str = ""
    # True when the recording of this conversation is in secure pause status.
    secure_pause: bool = False
    # The URI for this object
    self_uri: str = ""
    # An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level
    utilization_label_id: str = ""
