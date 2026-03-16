from __future__ import annotations

from serde import serde

from ..division import DivisionEntityRef
from ..domain import DomainEntityRef


@serde(rename_all='camelcase')
class ConversationDivisionMembership:
    # A division the conversation belongs to.
    division: DomainEntityRef | None = None
    # The entities on the conversation within the division. These are the users, queues, work flows, etc. that can be on conversations and and be assigned to different divisions.
    entities: list[DivisionEntityRef] | None = None
