from __future__ import annotations

from datetime import datetime

from serde import serde


@serde(rename_all='camelcase')
class TransferDestination:
    # The destination address if the command destination is an endpoint.
    address: str = ""
    # The id of the user if the command destination is a user.
    user_id: str = ""


@serde(rename_all='camelcase')
class TransferInitiator:
    # The id of the user who initiated the command if it was initiated by a user.
    user_id: str = ""


@serde(rename_all='camelcase')
class TransferResponseModifiedBy:
    # The globally unique identifier for the object.
    id: str = ""
    # The URI for this object
    self_uri: str = ""


@serde(rename_all='camelcase')
class TransferResponse:
    # The date/time that this command was issued. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    date_issued: datetime | None = None
    # The destination of the command.
    destination: TransferDestination | None = None
    # The id of the command.
    id: str = ""
    # The initiator of the command.
    initiator: TransferInitiator | None = None
    # The user or entity that modified the command.
    modified_by: TransferResponseModifiedBy | None = None
    # The state of the command.
    state: str = ""
    # The type of transfer to perform.
    transfer_type: str = ""
