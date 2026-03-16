from __future__ import annotations

from .base_api import GenesysBaseApi
from ..models.conversation.analytics_conversation_query_response import AnalyticsConversationQueryResponse
from ..models.conversation.analytics_conversation_without_attributes import AnalyticsConversationWithoutAttributes, \
    AnalyticsConversationWithoutAttributesMultiGetResponse
from ..models.call.call_conversation import CallConversation
from ..models.email.email_conversation import EmailConversation
from ..models.email.email_message import EmailMessage
from ..models.email.email_message_listing import EmailMessageListing
from ..models.conversation.query.conversation_query import ConversationQuery
from ..models.skill import SkillEntityListing
from ..models.skill.routing_skill import SkillListingQuery, RoutingSkill
from ..request.paging import PagedResponse


class ConversationApi(GenesysBaseApi):
    """
    This class provides methods to interact with the Genesys Cloud Conversation API.
    """

    def __init__(self, session, config):
        super().__init__(session, config)

    def post_analytics_conversations_details_query(self, query: ConversationQuery, batch_size: int | None = None) -> PagedResponse[AnalyticsConversationQueryResponse, AnalyticsConversationWithoutAttributes]:
        """
        Query for conversation details.

        :param query: The query to execute.
        :param batch_size: The total number of items to return.
        :return: AnalyticsConversationQueryResponse
        """

        return PagedResponse[AnalyticsConversationQueryResponse, AnalyticsConversationWithoutAttributes](
            self,
            'POST',
            '/api/v2/analytics/conversations/details/query',
            query,
            AnalyticsConversationQueryResponse,
            batch_size,
            retry_status=500,
            max_retries=3,
            retry_delay=2,
        )

    async def get_analytics_conversation_details(self, conversation_id: str) -> AnalyticsConversationWithoutAttributes:
        """
        Get conversation details by ID.

        :param conversation_id: The ID of the conversation.
        :return: AnalyticsConversationWithoutAttributes
        """
        return await self.get(
            f'/api/v2/analytics/conversations/{conversation_id}/details',
            model=AnalyticsConversationWithoutAttributes,
        )

    async def get_analytics_conversations_details(self, conversation_id: list[str]) -> list[AnalyticsConversationWithoutAttributes]:
        """
        Get conversation details by IDs.

        :param conversation_id: The ID of the conversation.
        :return: AnalyticsConversationWithoutAttributes
        """
        return (await self.get(
            f'/api/v2/analytics/conversations/details',
            params={ "id": ",".join(conversation_id) },
            model=AnalyticsConversationWithoutAttributesMultiGetResponse,
        )).conversations

    async def get_conversation_call(self, conversation_id: str) -> CallConversation:
        """
        Get conversation details by ID.

        :param conversation_id: The ID of the conversation.
        :return: Conversation details.
        """
        return await self.get(
            f'/api/v2/conversations/calls/{conversation_id}',
            model=CallConversation,
        )

    async def get_conversation_email(self, conversation_id: str) -> EmailConversation:
        """
        Get email conversation details by ID.

        :param conversation_id: The ID of the conversation.
        :return: Email conversation details.
        """
        return await self.get(
            f'/api/v2/conversations/emails/{conversation_id}',
            model=EmailConversation,
        )

    async def get_conversation_email_messages(self, conversation_id: str) -> EmailMessageListing:
        """
        Get the messages for an email conversation.

        :param conversation_id: The ID of the conversation.
        :return: Email message listing.
        """
        return await self.get(
            f'/api/v2/conversations/emails/{conversation_id}/messages',
            model=EmailMessageListing,
        )

    async def get_conversation_email_message(self, conversation_id: str, message_id: str) -> EmailMessage:
        """
        Get a specific message from an email conversation.

        :param conversation_id: The ID of the conversation.
        :param message_id: The ID of the message.
        :return: Email message.
        """
        return await self.get(
            f'/api/v2/conversations/emails/{conversation_id}/messages/{message_id}',
            model=EmailMessage,
        )

    def get_routing_skills(self, query: SkillListingQuery | None = None, batch_size: int | None = None) -> PagedResponse[SkillEntityListing, RoutingSkill]:
        """
        Get routing skills.
        :param query: The query to execute.
        :param batch_size: The total number of items to return.
        :return: Routing skills.
        """
        return PagedResponse[SkillEntityListing, RoutingSkill](
            self,
            'GET',
            '/api/v2/routing/skills',
            query if query else SkillListingQuery(),
            SkillEntityListing,
            batch_size,
            retry_status=500,
            max_retries=3,
            retry_delay=2,
        )
