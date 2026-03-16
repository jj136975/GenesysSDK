from __future__ import annotations

from datetime import datetime

from serde import serde
from serde.core import field

from .attachment import Attachment
from .email_address import EmailAddress


@serde(rename_all='camelcase')
class EmailMessage:
    id: str = ""
    to: list[EmailAddress] | None = None
    cc: list[EmailAddress] | None = None
    bcc: list[EmailAddress] | None = None
    pc_from: EmailAddress | None = field(default=None, rename="from")
    reply_to: EmailAddress | None = None
    subject: str = ""
    attachments: list[Attachment] | None = None
    text_body: str = ""
    html_body: str = ""
    text_body_preview: str = ""
    time: datetime | None = None
    history_included: bool = False
    state: str = ""
    draft_type: str = ""
    email_size_bytes: int = 0
    max_email_size_bytes: int = 0
    self_uri: str = ""
