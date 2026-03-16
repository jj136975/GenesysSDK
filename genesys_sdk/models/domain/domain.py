from serde import serde


@serde(rename_all='camelcase')
class DomainEntityRef:
    #
    id: str = ""
    #
    name: str = ""
    #
    self_uri: str = ""
