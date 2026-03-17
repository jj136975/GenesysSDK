from __future__ import annotations

from typing import Literal, Self, override

from serde import serde

from .filter import QueryFilter, SegmentDetailQueryPredicate, ConversationDetailQueryPredicate
from ....request.paging import IPageQuery


@serde(rename_all='camelcase')
class PagingSpec:
    # How many pages in
    page_number: int = 1
    # How many results per page
    page_size: int = 100

Order = Literal["asc", "desc"]
OrderBy = Literal["conversationStart", "segmentStart", "segmentEnd"]

@serde(rename_all='camelcase')
class ConversationQuery(IPageQuery):
    # Page size and number to control iterating through large result sets. Default page size is 25
    paging: PagingSpec
    # Specifies the date and time range of data being queried. Results will only include conversations that started on a day touched by the interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss
    interval: str = ""
    # Sort the result set in ascending/descending order. Default is ascending
    order: Order = "asc"
    # Specify which data element within the result set to use for sorting. The options  to use as a basis for sorting the results: conversationStart, segmentStart, and segmentEnd. If not specified, the default is conversationStart
    order_by: OrderBy = "conversationStart"
    # Filters that target individual segments within a conversation
    segment_filters: list[QueryFilter[SegmentDetailQueryPredicate] | None] = None

    # # Include faceted search and aggregate roll-ups describing your search results. This does not function as a filter, but rather, summary data about the data matching your filters
    # aggregations: list[AnalyticsQueryAggregation] | None = None
    # # Filters that target conversation-level data
    conversation_filters: list[QueryFilter[ConversationDetailQueryPredicate] | None] = None
    # # Filters that target evaluations
    # evaluation_filters: list[QueryFilter[EvaluationDetailQueryPredicate] | None] = None
    # # Filters that target resolutions
    # resolution_filters: list[QueryFilter[ResolutionDetailQueryPredicate] | None] = None
    # # Filters that target surveys
    # survey_filters: list[QueryFilter[SurveyDetailQueryPredicate] | None] = None

    @override
    def update_page(self, page: int) -> Self:
        query = ConversationQuery(
            interval=self.interval,
            order=self.order,
            order_by=self.order_by,
            paging=PagingSpec(page_number=page, page_size=self.paging.page_size),
            segment_filters=self.segment_filters,
            # aggregations=self.aggregations,
            conversation_filters=self.conversation_filters,
            # evaluation_filters=self.evaluation_filters,
            # resolution_filters=self.resolution_filters,
            # survey_filters=self.survey_filters
        )
        return query

    @override
    def get_page_size(self) -> int:
        if self.paging is None:
            return 1
        return self.paging.page_size

    @override
    def set_page_size(self, page_size: int):
        self.paging.page_size = page_size
