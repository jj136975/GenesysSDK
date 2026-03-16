from __future__ import annotations

from serde import serde

from ..domain import DomainEntityRef


@serde(rename_all='camelcase')
class ScoredAgent:
    # The agent
    agent: DomainEntityRef | None = None
    # Agent's score for the current conversation, from 0 - 100, higher being better
    score: int = 0
