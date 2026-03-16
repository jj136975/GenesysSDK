from __future__ import annotations

from datetime import datetime

from serde import serde

from .analytics_conversation_segment import AnalyticsConversationSegment


@serde(rename_all='camelcase')
class AnalyticsAgentGroup:
    # Conditional group routing agent group identifier
    agent_group_id: str = ""
    # Conditional group routing agent group type
    agent_group_type: str = ""


@serde(rename_all='camelcase')
class AnalyticsProposedAgent:
    # Proposed agent rank for this conversation from predictive routing (lower is better)
    agent_rank: int = 0
    # Unique identifier for the agent that was proposed by predictive routing
    proposed_agent_id: str = ""


@serde(rename_all='camelcase')
class AnalyticsSessionMetric:
    # Metric emission date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    emit_date: datetime | None = None
    # Unique name of this metric
    name: str = ""
    # The metric value
    value: int = 0


@serde(rename_all='camelcase')
class AnalyticsFlowOutcome:
    # Combination of unique flow outcome identifier and its value separated by colon
    flow_outcome: str = ""
    # The outcome ending timestamp in ISO 8601 format. This may be null if the outcome did not succeed.
    flow_outcome_end_timestamp: datetime | None = None
    # Unique identifier of a flow outcome
    flow_outcome_id: str = ""
    # The outcome starting timestamp in ISO 8601 format
    flow_outcome_start_timestamp: datetime | None = None
    # Flow outcome value, e.g. SUCCESS
    flow_outcome_value: str = ""


@serde(rename_all='camelcase')
class AnalyticsFlow:
    # Flow ending language, e.g. en-us
    ending_language: str = ""
    # The particular entry reason for this flow, e.g. an address, userId, or flowId
    entry_reason: str = ""
    # The entry type for this flow, e.g. dnis, dialer, agent, flow, or direct
    entry_type: str = ""
    # The exit reason for this flow, e.g. DISCONNECT
    exit_reason: str = ""
    # The unique identifier of this flow
    flow_id: str = ""
    # The name of this flow at the time of flow execution
    flow_name: str = ""
    # The type of this flow
    flow_type: str = ""
    # The version of this flow
    flow_version: str = ""
    # Flag indicating whether the flow issued a callback
    issued_callback: bool = False
    # Flow outcomes
    outcomes: list[AnalyticsFlowOutcome] | None = None
    # The recognition failure reason causing to exit/disconnect
    recognition_failure_reason: str = ""
    # Flow starting language, e.g. en-us
    starting_language: str = ""
    # The address of a flow transfer target, e.g. a phone number, an email address, or a queueId
    transfer_target_address: str = ""
    # The name of a flow transfer target
    transfer_target_name: str = ""
    # The type of transfer for flows that ended with a transfer
    transfer_type: str = ""


@serde(rename_all='camelcase')
class AnalyticsMediaEndpointStat:
    # The MIME type(s) of the audio encodings used by the audio streams belonging to this endpoint
    codecs: list[str] | None = None
    # The total number of packets received too late or too early, jitter queue overrun or underrun, for all audio streams belonging to this endpoint
    discarded_packets: int = 0
    # The total number of packets received with the same sequence number as another one recently received (window of 64 packets), for all audio streams belonging to this endpoint
    duplicate_packets: int = 0
    # Specifies when an event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    event_time: datetime | None = None
    # The total number of malformed or not RTP packets, unknown payload type, or discarded probation packets for all audio streams belonging to this endpoint
    invalid_packets: int = 0
    # The maximum latency experienced by any audio stream belonging to this endpoint, in milliseconds
    max_latency_ms: int = 0
    # The lowest estimated average MOS among all the audio streams belonging to this endpoint
    min_mos: float = 0.0
    # The lowest R-factor value among all of the audio streams belonging to this endpoint
    min_r_factor: float = 0.0
    # The total number of packets for which there was no room in the jitter queue when it was received, for all audio streams belonging to this endpoint (also counted in discarded)
    overrun_packets: int = 0
    # The total number of packets received for all audio streams belonging to this endpoint (includes invalid, duplicate, and discarded packets)
    received_packets: int = 0
    # The total number of packets received after their timestamp/seqnum has been played out, for all audio streams belonging to this endpoint (also counted in discarded)
    underrun_packets: int = 0


@serde(rename_all='camelcase')
class AnalyticsSession:
    # ID(s) of Skill(s) that are active on the conversation
    active_skill_ids: list[str] | None = None
    # Marker for an agent that skipped after call work
    acw_skipped: bool = False
    # The address that initiated an action
    address_from: str = ""
    # The email address for the participant on the other side of the email conversation
    address_other: str = ""
    # The email address for the participant on this side of the email conversation
    address_self: str = ""
    # The address receiving an action
    address_to: str = ""
    # Unique identifier of the active virtual agent assistant
    agent_assistant_id: str = ""
    # Bullseye ring of the targeted agent
    agent_bullseye_ring: int = 0
    # Conditional group routing agent groups
    agent_groups: list[AnalyticsAgentGroup] | None = None
    # Flag indicating an agent-owned callback
    agent_owned: bool = False
    # Automatic Number Identification (caller's number)
    ani: str = ""
    # ID of the user that manually assigned a conversation
    assigner_id: str = ""
    # Flag that indicates that the identity of the customer has been asserted as verified by the provider.
    authenticated: bool = False
    # The participantId being barged in on (if someone (e.g. an agent) is being barged in on, this would correspond to one of the other participantIds present in the conversation)
    barged_participant_id: str = ""
    # Blind carbon copy email address(es)
    bcc: list[str] | None = None
    # Callback phone number(s)
    callback_numbers: list[str] | None = None
    # Scheduled callback date/time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    callback_scheduled_time: datetime | None = None
    # The name of the user requesting a call back
    callback_user_name: str = ""
    # Carbon copy email address(es)
    cc: list[str] | None = None
    # Flag that indicates that the conversation has been cleared by the customer
    cleared: bool = False
    # The participantId being coached (if someone (e.g. an agent) is being coached, this would correspond to one of the other participantIds present in the conversation)
    coached_participant_id: str = ""
    # Describes side of the cobrowse (sharer or viewer)
    cobrowse_role: str = ""
    # A unique identifier for a Genesys Cloud cobrowse room
    cobrowse_room_id: str = ""
    # Flag that indicates that the push delivery mechanism was used
    delivery_pushed: bool = False
    # The email or SMS delivery status
    delivery_status: str = ""
    # Date and time of the most recent delivery status change. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    delivery_status_change_date: datetime | None = None
    # Destination address(es) of transfers or consults
    destination_addresses: list[str] | None = None
    # Absolute time when the speech ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    detected_speech_end: datetime | None = None
    # Absolute time when the speech started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    detected_speech_start: datetime | None = None
    # The direction of the communication
    direction: str = ""
    # (Dialer) Analyzer (for example speech.person)
    disposition_analyzer: str = ""
    # (Dialer) Result of the analysis (for example disposition.classification.callable.machine)
    disposition_name: str = ""
    # Dialed number identification service (number dialed by the calling party)
    dnis: str = ""
    # Unique identifier of the edge device
    edge_id: str = ""
    # Number of eligible agents for each predictive routing attempt
    eligible_agent_counts: list[int] | None = None
    # Extended delivery status
    extended_delivery_status: str = ""
    # IVR flow execution associated with this session
    flow: AnalyticsFlow | None = None
    # Type of flow in that occurred when entering ACD.
    flow_in_type: str = ""
    # Type of flow out that occurred when emitting tFlowOut.
    flow_out_type: str = ""
    # Identifier of the journey action.
    journey_action_id: str = ""
    # Identifier of the journey action map that triggered the action.
    journey_action_map_id: str = ""
    # Version of the journey action map that triggered the action.
    journey_action_map_version: int = 0
    # Primary identifier of the journey customer in the source where the activities originate from.
    journey_customer_id: str = ""
    # Type of primary identifier of the journey customer (e.g. cookie).
    journey_customer_id_type: str = ""
    # Unique identifier of the journey session.
    journey_customer_session_id: str = ""
    # Type or category of journey sessions (e.g. web, ticket, delivery, atm).
    journey_customer_session_id_type: str = ""
    # Media bridge ID for the conference session consistent across all participants
    media_bridge_id: str = ""
    # Count of any media (images, files, etc) included in this session
    media_count: int = 0
    # MediaEndpointStats associated with this session
    media_endpoint_stats: list[AnalyticsMediaEndpointStat] | None = None
    # The session media type
    media_type: str = ""
    # Message type for messaging services. E.g.: sms, facebook, twitter, line
    message_type: str = ""
    # List of metrics for this session
    metrics: list[AnalyticsSessionMetric] | None = None
    # The participantId being monitored (if someone (e.g. an agent) is being monitored, this would correspond to one of the other participantIds present in the conversation)
    monitored_participant_id: str = ""
    # (Dialer) Unique identifier of the outbound campaign
    outbound_campaign_id: str = ""
    # (Dialer) Unique identifier of the contact
    outbound_contact_id: str = ""
    # (Dialer) Unique identifier of the contact list that this contact belongs to
    outbound_contact_list_id: str = ""
    # This identifies pairs of related sessions on a conversation. E.g. an external session�s peerId will be the session that the call originally connected to, e.g. if an IVR was dialed, the IVR session, which will also have the external session�s ID as its peer. After that point, any transfers of that session to other internal components (acd, agent, etc.) will all spawn new sessions whose peerIds point back to that original external session.
    peer_id: str = ""
    # Proposed agents
    proposed_agents: list[AnalyticsProposedAgent] | None = None
    # The original voice protocol call ID, e.g. a SIP call ID
    protocol_call_id: str = ""
    # The source provider for the communication.
    provider: str = ""
    # Flag determining if an audio recording was started or not
    recording: bool = False
    # Name, phone number, or email address of the remote party.
    remote: str = ""
    # Unique identifier for the remote party
    remote_name_displayable: str = ""
    # ID(s) of Skill(s) that have been removed by bullseye routing
    removed_skill_ids: list[str] | None = None
    # Routing type(s) for requested/attempted routing methods.
    requested_routings: list[str] | None = None
    # Unique identifier for the room
    room_id: str = ""
    # Routing ring for bullseye or preferred agent routing
    routing_ring: int = 0
    # Routing rule for preferred, conditional and predictive routing type
    routing_rule: str = ""
    # Routing rule type
    routing_rule_type: str = ""
    # Direct screen share address
    screen_share_address_self: str = ""
    # A unique identifier for a Genesys Cloud screen share room
    screen_share_room_id: str = ""
    # A unique identifier for a script
    script_id: str = ""
    # List of segments for this session
    segments: list[AnalyticsConversationSegment] | None = None
    # Selected agent ID
    selected_agent_id: str = ""
    # Selected agent GPR rank
    selected_agent_rank: int = 0
    # Dialed number for the current session; this can be different from dnis, e.g. if the call was transferred
    session_dnis: str = ""
    # The unique identifier of this session
    session_id: str = ""
    # Flag determining if screen share is started or not (true/false)
    sharing_screen: bool = False
    # (Dialer) Whether the agent can skip the dialer contact
    skip_enabled: bool = False
    # The number of seconds before Genesys Cloud begins the call for a call back (0 disables automatic calling)
    timeout_seconds: int = 0
    # Complete routing method
    used_routing: str = ""
    # Direct Video address
    video_address_self: str = ""
    # A unique identifier for a Genesys Cloud video room
    video_room_id: str = ""
    # Number of waiting interactions for each predictive routing attempt
    waiting_interaction_counts: list[int] | None = None
