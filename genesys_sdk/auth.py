from dataclasses import dataclass

from aiohttp import ClientSession, BasicAuth

from simple_sdk.auth import CredentialLoader


@dataclass
class GenesysCredentialLoader(CredentialLoader[str]):
    """OAuth2 client credentials flow for Genesys Cloud."""

    login_host: str
    client_id: str
    client_secret: str

    async def load_credentials(self) -> str:
        """Authenticate using OAuth2 client credentials and return the access token."""
        async with ClientSession() as session:
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
                else:
                    raise Exception(f"Failed to get OAuth token: {response.status} {await response.text()}")
