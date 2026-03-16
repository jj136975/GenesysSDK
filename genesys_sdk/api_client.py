from simple_sdk.auth import TokenAuthenticator
from simple_sdk.client import JsonApiClient

from .api.conversation_api import ConversationApi
from .api.recording_api import RecordingApi
from .auth import GenesysCredentialLoader
from .configuration import GenesysConfiguration


class GenesysClient(JsonApiClient):
    def __init__(self, config: GenesysConfiguration, auth: GenesysCredentialLoader):
        super().__init__(config, TokenAuthenticator(auth))
        self._conversation_api: ConversationApi | None = None
        self._recording_api: RecordingApi | None = None

    @property
    def conversation_api(self) -> ConversationApi:
        if self._conversation_api is None:
            if self._session is None:
                raise RuntimeError(
                    "Client session not initialized. Use 'async with GenesysClient(...) as client' to initialize the session.")
            self._conversation_api = ConversationApi(self._session, self._config)
        return self._conversation_api

    @property
    def recording_api(self) -> RecordingApi:
        if self._recording_api is None:
            if self._session is None:
                raise RuntimeError(
                    "Client session not initialized. Use 'async with GenesysClient(...) as client' to initialize the session.")
            self._recording_api = RecordingApi(self._session, self._config)
        return self._recording_api
