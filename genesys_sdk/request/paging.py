import asyncio
from abc import ABC, abstractmethod
from typing import Callable, TypeVar, List, Type, Self, Coroutine, Any, Tuple, \
    Awaitable, TYPE_CHECKING, AsyncIterator, Protocol, Optional, Generator

from aiohttp.typedefs import StrOrURL
from serde import to_dict

from ..api.base_api import GenesysBaseApi
from simple_sdk.errors import ClientError


class IPageQuery(ABC):
    @abstractmethod
    def update_page(self, page: int) -> Self:
        ...

    @abstractmethod
    def get_page_size(self) -> int:
        ...

    @abstractmethod
    def set_page_size(self, page_size: int):
        ...


class PagesInfo:
    def __init__(self, page_size: int, total_items: int):
        self.page_size = page_size
        self.total_items = total_items
        self.total_pages = (total_items - 1) // page_size + 1

    def iter_query(self, start: int, query: IPageQuery) -> Generator[Tuple[int, IPageQuery], None, None]:
        """
        Iterate over the pages starting from the given page number.
        :param start: The page number to start from.
        :param query: The query object to update with the page number.
        :return: A generator that yields tuples of page number and updated query object.
        """
        for i in range(start, self.total_pages):
            q = query.update_page(i)
            yield i, q
        q = query.update_page(self.total_pages)
        q.set_page_size(self.total_items - self.page_size * (self.total_pages - 1))
        yield self.total_pages, q


TContent = TypeVar("TContent")


class IPageResponse(Protocol):
    @abstractmethod
    def get_content(self) -> List[TContent]:
        ...

    @abstractmethod
    def get_content_size(self) -> int:
        ...

    @abstractmethod
    def get_total_items(self) -> int:
        ...


TRet = TypeVar("TRet")


class PagedResponse[TPage: IPageResponse, TContent]:
    if TYPE_CHECKING:
        from typing import Unpack
        from simple_sdk.api import RetryOptions

        def __init__(
                self,
                client: GenesysBaseApi,
                methode: str,
                url: StrOrURL,
                query: IPageQuery,
                cls: Type[TPage],
                batch_size: Optional[int] = None,
                **kwargs: Unpack[RetryOptions]
        ):
            ...
    else:
        def __init__(
                self,
                client: GenesysBaseApi,
                methode: str,
                url: StrOrURL,
                query: IPageQuery,
                cls: Type[TPage],
                batch_size: Optional[int] = None,
                **kwargs: Any
        ):
            self._client = client
            self._methode = methode
            self._url = url
            self._query = query
            self._cls = cls
            self._batch_size = batch_size
            self._kwargs = kwargs

            if methode == "POST":
                self._query_request = lambda q: self._client.request(self._methode, self._url, self._cls, json=q,
                                                                     **self._kwargs)
            else:
                self._query_request = lambda q: self._client.request(self._methode, self._url, self._cls,
                                                                     params=to_dict(q, skip_none=True), **self._kwargs)

    async def get_page(self, page: int) -> TPage:
        query = self._query.update_page(page)
        return await self._query_request(query)

    async def with_processor(self, processor: Callable[[int, List[TContent]], Coroutine[Any, Any, TRet]]) -> Tuple[
            List[TRet], List[ClientError]]:

        async def process_page(page_number: int, query: IPageQuery) -> Tuple[TRet, TPage] | ClientError:
            try:
                response = await self._query_request(query)
            except ClientError as err:
                return err
            return await processor(page_number, response.get_content()), response

        q = self._query.update_page(1)
        if self._batch_size and q.get_page_size() > self._batch_size:
            q.set_page_size(self._batch_size)
        res = await process_page(1, q)
        if isinstance(res, ClientError):
            return [], [res]

        ret, page = res

        if self._batch_size:
            info = PagesInfo(self._query.get_page_size(), min(page.get_total_items(), self._batch_size))
        else:
            info = PagesInfo(self._query.get_page_size(), page.get_total_items())

        if info.total_pages <= 1:
            return [ret], []

        results = [ret]
        errors = []

        tasks = [process_page(i, q) for i, q in info.iter_query(2, self._query)]

        for res in asyncio.as_completed(tasks):
            res = await res
            if isinstance(res, ClientError):
                errors.append(res)
            else:
                results.append(res[0])
        return results, errors

    def __aiter__(self) -> AsyncIterator[Awaitable[Tuple[int, List[TContent]]]]:

        async def to_aiter() -> AsyncIterator[Awaitable[Tuple[int, List[TContent]]]]:
            fut = asyncio.Future()
            try:
                page = await self._query_request(self._query)
            except ClientError as err:
                fut.set_exception(err)
                yield fut
                return
            if self._batch_size and page.get_total_items() > self._batch_size:
                fut.set_result((1, page.get_content()[:self._batch_size]))
            else:
                fut.set_result((1, page.get_content()))
            yield fut

            if self._batch_size:
                info = PagesInfo(self._query.get_page_size(), min(page.get_total_items(), self._batch_size))
            else:
                info = PagesInfo(self._query.get_page_size(), page.get_total_items())

            if info.total_pages <= 1:
                return

            async def create_task(page_number: int, query: IPageQuery) -> Tuple[int, List[TContent]]:
                response = await self._query_request(query)
                return page_number, response.get_content()

            tasks = [create_task(i, q) for i, q in info.iter_query(2, self._query)]
            for task in asyncio.as_completed(tasks):
                yield task

        return to_aiter()
