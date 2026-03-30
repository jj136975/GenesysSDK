from __future__ import annotations

from datetime import datetime
from typing import Self, override

from serde import serde

from ...request.paging import IPageResponse, IPageQuery


@serde(rename_all='camelcase')
class WrapupListingQuery(IPageQuery):
    page_size: int = 100
    page_number: int = 1
    name: str | None = None
    id: list[str] | None = None

    @override
    def get_page_size(self) -> int:
        return self.page_size

    @override
    def update_page(self, page: int) -> Self:
        return WrapupListingQuery(page_size=self.page_size, page_number=page, name=self.name, id=self.id)

    @override
    def set_page_size(self, page_size: int):
        self.page_size = page_size


@serde(rename_all='camelcase')
class RoutingWrapup:
    # Date last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    date_modified: datetime | None = None
    # The globally unique identifier for the object.
    id: str | None = None
    # The name of the skill.
    name: str | None = None
    # The URI for this object
    self_uri: str | None = None
    # The wrap-up code description.
    description: str | None = None


@serde(rename_all='camelcase')
class WrapupEntityListing(IPageResponse):
    #
    entities: list[RoutingWrapup] | None = None
    #
    first_uri: str | None = None
    #
    last_uri: str | None = None
    #
    next_uri: str | None = None
    #
    page_count: int = 0
    #
    page_number: int = 0
    #
    page_size: int = 0
    #
    previous_uri: str | None = None
    #
    self_uri: str | None = None
    #
    total: int = 0

    @override
    def get_content(self) -> list[RoutingWrapup]:
        return self.entities if self.entities else []

    @override
    def get_content_size(self) -> int:
        return len(self.entities) if self.entities else 0

    @override
    def get_total_items(self) -> int:
        return self.total
