from serde import serde


@serde(rename_all='camelcase')
class EmailAddress:
    email: str = ""
    name: str = ""
