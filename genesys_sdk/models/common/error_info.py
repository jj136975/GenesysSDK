from serde import serde


@serde(rename_all='camelcase')
class ErrorInfo:
    #
    code: str = ""
    #
    message: str = ""
