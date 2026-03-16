from serde import serde


@serde(rename_all='camelcase')
class FaxStatus:
    # Active page of the transmission.
    active_page: int = 0
    # Current signaling rate of transmission, baud rate.
    baud_rate: int = 0
    # Number of bytes that have competed transmission.
    bytes_transmitted: int = 0
    # The fax direction, either "send" or "receive".
    direction: str = ""
    # Total number of expected pages, if known.
    expected_pages: int = 0
    # Number of line errors.
    line_errors: int = 0
    # Number of lines that have completed transmission.
    lines_transmitted: int = 0
    # Number of page errors.
    page_errors: int = 0
