from __future__ import annotations

from serde import serde


@serde(rename_all='camelcase')
class Detail:
    #
    entity_id: str = ""
    #
    entity_name: str = ""
    #
    error_code: str = ""
    #
    field_name: str = ""


@serde(rename_all='camelcase')
class Limit:
    #
    key: str = ""
    #
    namespace: str = ""
    #
    value: int = 0


@serde(rename_all='camelcase')
class ErrorBody:
    #
    code: str = ""
    #
    context_id: str = ""
    #
    details: list[Detail] | None = None
    #
    entity_id: str = ""
    #
    entity_name: str = ""
    #
    # errors: list["ErrorBody"] | None = None
    #
    limit: Limit | None = None
    #
    message: str = ""
    #
    message_params: dict[str, str] | None = None
    #
    message_with_params: str = ""
    #
    status: int = 0
