from serde import serde


@serde(rename_all='camelcase')
class AddressableEntityRef:
    #
    id: str = ""
    #
    self_uri: str = ""
