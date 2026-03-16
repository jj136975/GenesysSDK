from __future__ import annotations

from serde import serde


@serde(rename_all='camelcase')
class JourneyActionMap:
    # The ID of the actionMap in the Journey System which triggered this action
    id: str = ""
    # The version number of the actionMap in the Journey System at the time this action was triggered
    version: int = 0


@serde(rename_all='camelcase')
class JourneyAction:
    # Details about the action map from the Journey System which triggered this action
    action_map: JourneyActionMap | None = None
    # The ID of an action from the Journey System (an action is spawned from an actionMap)
    id: str = ""


@serde(rename_all='camelcase')
class JourneyCustomer:
    # An ID of a customer within the Journey System at a point-in-time.  Note that a customer entity can have multiple customerIds based on the stitching process.  Depending on the context within the PureCloud conversation, this may or may not be mutable.
    id: str = ""
    # The type of the customerId within the Journey System (e.g. cookie).
    id_type: str = ""


@serde(rename_all='camelcase')
class JourneyCustomerSession:
    # An ID of a Customer/User's session within the Journey System at a point-in-time
    id: str = ""
    # The type of the Customer/User's session within the Journey System (e.g. web, app)
    type: str = ""


@serde(rename_all='camelcase')
class JourneyContext:
    # A subset of the Journey System's customer data at a point-in-time (for external linkage and internal usage/context)
    customer: JourneyCustomer | None = None
    # A subset of the Journey System's tracked customer session data at a point-in-time (for external linkage and internal usage/context)
    customer_session: JourneyCustomerSession | None = None
    # A subset of the Journey System's action data relevant to a part of a conversation (for external linkage and internal usage/context)
    triggering_action: JourneyAction | None = None
