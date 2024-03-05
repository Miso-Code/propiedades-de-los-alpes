from dataclasses import dataclass
from uuid import UUID

from ..mappers import AutomationAgentMapper
from ...domain.repositories import AgentRepository
from .....seedwork.application.queries import Query, QueryHandler, QueryResult, execute_query as query
from .base import AgentQueryBaseHandler


@dataclass
class GetAgent(Query):
    id: str


class GetAgentHandler(AgentQueryBaseHandler):

    def handle(self, query: GetAgent) -> QueryResult:
        repository = self.repository_factory.create_object(AgentRepository.__class__)
        agent_dto = repository.get_by_id(UUID(query.id))
        agents = self.agent_factory.create_object(agent_dto, AutomationAgentMapper())
        return QueryResult(agents)


@query.register(GetAgent)
def execute_query_get_all_agents(query: GetAgent) -> QueryResult:
    handler = GetAgentHandler()
    return handler.handle(query)
