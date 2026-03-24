from typing import override, Self

from serde import serde

from ..division import DivisionEntityRef
from ...request.paging import IPageResponse, IPageQuery


@serde(rename_all='camelcase')
class QueueEntity:
    # The globally unique identifier for the object.
    id: str = ""
    #
    name: str = ""
    # The URI for this object.
    self_uri: str = ""
    # The queue description.
    description: str = ""
    # The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z.
    date_created: str = ""
    # The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z.
    date_modified: str = ""
    # The ID of the user that last modified the queue.
    modified_by: str = ""
    # The ID of the user that created the queue.
    created_by: str = ""
    # The total number of members in the queue.
    member_count: int = 0
    # The number of user members (i.e., non-group members) in the queue.
    user_member_count: int = 0
    # The number of joined members in the queue.
    joined_member_count: int = 0
    # The division to which this entity belongs.
    division: DivisionEntityRef | None = None


@serde(rename_all='camelcase')
class QueueListingQuery(IPageQuery):
    page_size: int = 100
    page_number: int = 1
    name: str | None = None
    id: list[str] | None = None

    @override
    def get_page_size(self) -> int:
        return self.page_size

    @override
    def update_page(self, page: int) -> Self:
        return QueueListingQuery(page_size=self.page_size, page_number=page, name=self.name, id=self.id)

    @override
    def set_page_size(self, page_size: int):
        self.page_size = page_size


@serde(rename_all='camelcase')
class QueueEntityListing(IPageResponse):
    #
    entities: list[QueueEntity] | None = None
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
    def get_content(self) -> list[QueueEntity]:
        return self.entities if self.entities else []

    @override
    def get_content_size(self) -> int:
        return len(self.entities) if self.entities else 0

    @override
    def get_total_items(self) -> int:
        return self.total
