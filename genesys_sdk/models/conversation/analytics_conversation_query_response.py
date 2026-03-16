from __future__ import annotations

from abc import ABC
from typing import override

from serde import serde

from ...request.paging import IPageResponse
from .aggregation_result import AggregationResult
from .analytics_conversation_without_attributes import AnalyticsConversationWithoutAttributes


@serde(rename_all='camelcase')
class AnalyticsConversationQueryResponse(IPageResponse, ABC):
    #
    aggregations: list[AggregationResult] | None = None
    #
    conversations: list[AnalyticsConversationWithoutAttributes] | None = None
    #
    total_hits: int = 0

    @override
    def get_content(self) -> list[AnalyticsConversationWithoutAttributes]:
        return self.conversations if self.conversations else []

    @override
    def get_content_size(self) -> int:
        return len(self.conversations) if self.conversations else 0

    @override
    def get_total_items(self) -> int:
        return self.total_hits
