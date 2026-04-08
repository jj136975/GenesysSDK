import asyncio
from dataclasses import dataclass

import serde
from aiohttp import ClientSession, BasicAuth
from serde import SerdeError
from simple_sdk import Raise, InvalidStatus

from simple_sdk.auth import CredentialLoader

from .errors import RateLimitExceeded
from .models.error import ErrorBody


@dataclass
class GenesysCredentialLoader(CredentialLoader[str]):
    """OAuth2 client credentials flow for Genesys Cloud."""

    login_host: str
    client_id: str
    client_secret: str

    async def load_credentials(self) -> str:
        """Authenticate using OAuth2 client credentials and return the access token."""
        tries = 3
        error = None

        async with ClientSession() as session:

            while tries > 0:
                async with session.post(
                        self.login_host + "/oauth/token",
                        data={'grant_type': 'client_credentials'},
                        auth=BasicAuth(self.client_id, self.client_secret),
                        headers={'Content-Type': 'application/x-www-form-urlencoded'},
                ) as response:
                    if response.status == 200:
                        data: dict = await response.json()
                        token = data.get('access_token')
                        if not token:
                            raise ValueError("OAuth response did not contain an access token.")
                        return token
                    elif response.status == 400:
                        try:
                            error_data = await response.json(
                                loads=lambda obj: serde.json.from_json(ErrorBody, obj))
                            error = RateLimitExceeded(error_data)
                            print(f"Rate limit exceeded. Retrying in {error.retry_delay} seconds...")
                            await asyncio.sleep(error.retry_delay)
                            tries -= 1
                        except SerdeError:
                            raise InvalidStatus(await response.text(), response.status)
                    else:
                        raise Exception(f"Failed to get OAuth token: {response.status} {await response.text()}")

            assert error is not None
            raise error
