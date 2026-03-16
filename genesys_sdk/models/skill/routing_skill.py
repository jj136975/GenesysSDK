from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Self, override

from serde import serde

from ...request.paging import IPageResponse, IPageQuery

@serde(rename_all='camelcase')
class SkillListingQuery(IPageQuery):
    page_size: int = 100
    page_number: int = 1
    name: str | None = None
    id: list[str] | None = None

    @override
    def get_page_size(self) -> int:
        return self.page_size

    @override
    def update_page(self, page: int) -> Self:
        return SkillListingQuery(page_size=self.page_size, page_number=page, name=self.name, id=self.id)

    @override
    def set_page_size(self, page_size: int):
        self.page_size = page_size

@serde(rename_all='camelcase')
class RoutingSkill:
    # Date last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
    date_modified: datetime | None = None
    # The globally unique identifier for the object.
    id: str = ""
    # The name of the skill.
    name: str = ""
    # The URI for this object
    self_uri: str = ""
    # The current state for this skill.
    state: str = ""
    # Required when updating. Version must be the current version. Only the system can assign version.
    version: str = ""


@serde(rename_all='camelcase')
class SkillEntityListing(IPageResponse, ABC):
    #
    entities: list[RoutingSkill] | None = None
    #
    first_uri: str = ""
    #
    last_uri: str = ""
    #
    next_uri: str = ""
    #
    page_count: int = 0
    #
    page_number: int = 0
    #
    page_size: int = 0
    #
    previous_uri: str = ""
    #
    self_uri: str = ""
    #
    total: int = 0

    @override
    def get_content(self) -> list[RoutingSkill]:
        return self.entities if self.entities else []

    @override
    def get_content_size(self) -> int:
        return len(self.entities) if self.entities else 0

    @override
    def get_total_items(self) -> int:
        return self.total
