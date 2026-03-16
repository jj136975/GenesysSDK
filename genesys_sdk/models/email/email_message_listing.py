from __future__ import annotations

from serde import serde

from .email_message import EmailMessage


@serde(rename_all='camelcase')
class EmailMessageListing:
    entities: list[EmailMessage] | None = None
    page_size: int = 0
    page_number: int = 0
    total: int = 0
    first_uri: str = ""
    last_uri: str = ""
    self_uri: str = ""
    page_count: int = 0
