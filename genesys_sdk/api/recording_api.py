from __future__ import annotations

import asyncio
from typing import Coroutine, Any, TYPE_CHECKING

from aiohttp import ClientSession
from yarl import URL

from .base_api import GenesysBaseApi

if TYPE_CHECKING:
    from ..models.recording.annotation import Annotation
    from ..models.recording.recording import Recording
    from ..models.recording.recording_metadata import RecordingMetadata

_DOWNLOAD_HEADERS = {"Accept": "application/octet-stream"}


async def _download_recordings(recording: Recording) -> list[tuple[str, bytes]]:

    async with ClientSession(headers=_DOWNLOAD_HEADERS) as session:
        async def _download(uri: str, channel: str) -> tuple[str, bytes]:
            print(uri)
            async with session.get(URL(uri, encoded=True)) as response:
                if response.status != 200:
                    raise Exception(f"Failed to download recording: {response.status}")
                return channel, await response.read()

        tasks = [_download(media.media_uri, channel) for channel, media in recording.media_uris.items()]
        return await asyncio.gather(*tasks)


class RecordingApi(GenesysBaseApi):
    async def get_conversation_recording_annotations(self, conversation_id: str, recording_id: str) -> list[Annotation]:
        from ..models.recording.annotation import Annotation

        return await self.get(
            f" /api/v2/conversations/{conversation_id}/recordings/{recording_id}/annotations",
            model=list[Annotation],
        )

    async def get_conversation_recordingmetadata(self, conversation_id: str) -> list[RecordingMetadata]:
        from ..models.recording.recording_metadata import RecordingMetadata

        return await self.get(
            f"/api/v2/conversations/{conversation_id}/recordingmetadata",
            model=list[RecordingMetadata],
        )

    async def get_conversation_recordings(self, conversation_id: str, format_id: str = "WAV") -> list[Recording]:
        from ..models.recording.recording import Recording

        return await self.get(
            f"/api/v2/conversations/{conversation_id}/recordings",
            params={"formatId": format_id},
            model=list[Recording],
        )

    def download_recordings(self, recording: Recording) -> Coroutine[Any, Any, list[tuple[str, bytes]]]:
        return _download_recordings(recording)
