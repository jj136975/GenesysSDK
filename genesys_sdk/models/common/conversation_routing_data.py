from __future__ import annotations

from serde import serde

from .addressable_entity_ref import AddressableEntityRef
from .scored_agent import ScoredAgent


@serde(rename_all='camelcase')
class ConversationRoutingData:
    # An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level
    label: str = ""
    # The language to use for routing decisions
    language: AddressableEntityRef | None = None
    # The priority of the conversation to use for routing decisions
    priority: int = 0
    # The queue to use for routing decisions
    queue: AddressableEntityRef | None = None
    # A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents
    scored_agents: list[ScoredAgent] | None = None
    # The skills to use for routing decisions
    skills: list[AddressableEntityRef] | None = None
