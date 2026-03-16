import serde
from aiohttp import ClientSession, ClientResponse
from serde import SerdeError

from simple_sdk.api import BaseApi, Retry, Raise
from simple_sdk.errors import InvalidStatus

from ..configuration import GenesysConfiguration
from ..errors import GenesysError, RateLimitExceeded
from ..models.error.error import ErrorBody


class GenesysBaseApi(BaseApi):
    """Base class for Genesys Cloud API clients."""

    _rate_limit_retry: bool = True
    """Whether to automatically retry on 429 rate limit responses."""

    def __init__(self, session: ClientSession, config: GenesysConfiguration):
        super().__init__(session, default_error_model=ErrorBody)
        self._config = config

    async def on_status(self, status: int, response: ClientResponse) -> Retry | Raise | None:
        if status == 202:
            return Retry(delay=self._config.retry_delay)
        if status == 429:
            try:
                error_data = await response.json(
                    loads=lambda obj: serde.json.from_json(ErrorBody, obj))
                error = RateLimitExceeded(error_data)
            except SerdeError:
                return Raise(error=InvalidStatus(await response.text(), status))
            if not self._rate_limit_retry:
                return Raise(error=error)
            return Retry(delay=error.retry_delay)
        if 400 <= status < 500:
            try:
                error_data = await response.json(
                    loads=lambda obj: serde.json.from_json(ErrorBody, obj))
                return Raise(error=GenesysError(error_data))
            except SerdeError:
                return Raise(error=InvalidStatus(await response.text(), status))
        return None
