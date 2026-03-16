import re

from simple_sdk.errors import InvalidStatus
from .models.error.error import ErrorBody


class GenesysError(InvalidStatus):
    def __init__(self, error: ErrorBody):
        super().__init__(error.message, error.status)
        self._error = error

    @property
    def error(self) -> ErrorBody:
        return self._error


_RATE_LIMIT_REGEX = re.compile(r"\[(\d+)] seconds")


class RateLimitExceeded(GenesysError):
    def __init__(self, error: ErrorBody):
        super().__init__(error)
        match = _RATE_LIMIT_REGEX.search(error.message)
        self._retry_delay = int(match.group(1)) if match else 60

    @property
    def retry_delay(self) -> int:
        return self._retry_delay


class RequestNotReady(InvalidStatus):
    """Request not ready yet."""

    def __init__(self, message: str, status: int):
        super().__init__(message, status)

    def __str__(self) -> str:
        return f"Request Not Ready: {self.message}"

    def __repr__(self) -> str:
        return f"RequestNotReady(message={self.message})"
