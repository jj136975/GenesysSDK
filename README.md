# Genesys Light SDK

Lightweight async Python SDK for the Genesys Cloud API.

Built on `aiohttp` and [`pyserde`](https://github.com/yukinarit/pyserde) for fast, typed API interactions with minimal overhead.

## Requirements

- Python 3.13+
- [SimpleSDK](https://github.com/jj136975/SimpleSDK)

## Installation

```bash
pip install genesys_sdk
```

## Configuration

```python
from genesys_sdk.configuration import GenesysConfiguration
from genesys_sdk.region import PureCloudRegionHosts

config = GenesysConfiguration(
    host=PureCloudRegionHosts.eu_central_1,
)
```

The SDK also reads settings from `~/.genesyscloudpython/config` (INI or JSON), where you can configure logging and the host region.

### SSL and Proxy

```python
config = GenesysConfiguration(
    verify_ssl=True,
    ssl_ca_cert="/path/to/ca.pem",
    cert_file="/path/to/client.pem",
    key_file="/path/to/client.key",
)
```

For proxy support, set the `HTTP_PROXY` / `HTTPS_PROXY` environment variables. The client uses `trust_env=True` by default.

## Authentication

The SDK uses OAuth2 client credentials:

```python
from genesys_sdk.auth import GenesysCredentialLoader
from genesys_sdk.region import PureCloudRegionHosts

region = PureCloudRegionHosts.eu_central_1

auth = GenesysCredentialLoader(
    login_host=region.login_host,
    client_id="your-client-id",
    client_secret="your-client-secret",
)
```

## Usage

Use the client as an async context manager:

```python
from genesys_sdk.api_client import GenesysClient

async with GenesysClient(config, auth) as client:
    ...
```

### Analytics Queries

Query conversation analytics with automatic pagination:

```python
from genesys_sdk.models.conversation.query import ConversationQuery, PagingSpec
from genesys_sdk.utils.interval import create_days_before_interval

query = ConversationQuery(
    interval=create_days_before_interval(days=7),
    paging=PagingSpec(page_size=100),
)

response = client.conversation_api.post_analytics_conversations_details_query(query)

# Async iteration
async for page in response:
    page_number, conversations = await page
    for conv in conversations:
        print(conv.conversation_id)

# Or process all pages in parallel
results, errors = await response.with_processor(
    lambda page_num, convs: process(convs)
)
```

### Conversation Details

```python
# Single conversation
conv = await client.conversation_api.get_analytics_conversation_details("conversation-id")

# Multiple conversations
convs = await client.conversation_api.get_analytics_conversations_details(
    ["id-1", "id-2", "id-3"]
)

# Call conversation
call = await client.conversation_api.get_conversation_call("conversation-id")

# Email conversation
email = await client.conversation_api.get_conversation_email("conversation-id")
```

### Email Messages

```python
# List messages in an email conversation
listing = await client.conversation_api.get_conversation_email_messages("conversation-id")

# Get a specific message
message = await client.conversation_api.get_conversation_email_message(
    "conversation-id", "message-id"
)
```

### Routing Skills

```python
from genesys_sdk.models.skill.routing_skill import SkillListingQuery

response = client.conversation_api.get_routing_skills(
    SkillListingQuery(name="SomeSkill")
)

async for page in response:
    page_number, skills = await page
    for skill in skills:
        print(skill.name)
```

### Recordings

```python
# Get recording metadata
metadata = await client.recording_api.get_conversation_recordingmetadata("conversation-id")

# Get recordings with download URIs
recordings = await client.recording_api.get_conversation_recordings("conversation-id")

# Download media files (returns list of (channel, bytes) tuples)
for recording in recordings:
    files = await client.recording_api.download_recordings(recording)
    for channel, data in files:
        print(f"{channel}: {len(data)} bytes")
```

## Error Handling

The SDK raises typed exceptions:

- **`GenesysError`** -- API errors (4xx) with a parsed `ErrorBody`
- **`RateLimitExceeded`** -- 429 responses, automatically retried by default with the delay from the error message
- **`RequestNotReady`** -- 202 responses, automatically retried with a configurable delay

```python
from genesys_sdk.errors import GenesysError, RateLimitExceeded

try:
    conv = await client.conversation_api.get_conversation_call("bad-id")
except GenesysError as e:
    print(e.error.status, e.error.message)
```

## Logging

Configure logging through the `Logger` on the configuration:

```python
from genesys_sdk.logger import LogLevel, LogFormat

config.logger.log_level = LogLevel.LTrace
config.logger.log_format = LogFormat.JSON
config.logger.log_to_console = True
config.logger.log_file_path = "/tmp/genesys.log"
config.logger.log_request_body = True
config.logger.log_response_body = True
```

Authorization headers are automatically redacted in log output.

## License

This project is licensed under the [MIT License](LICENSE).
