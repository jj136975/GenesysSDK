from serde import serde


@serde(rename_all='camelcase')
class Attachment:
    attachment_id: str = ""
    name: str = ""
    content_uri: str = ""
    content_type: str = ""
    content_length: int = 0
    inline_image: bool = False
