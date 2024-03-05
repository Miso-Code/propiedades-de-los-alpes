from ...domain.factories import AutomationAgentFactory
from ...infrastructure.factories import RepositoryFactory
from .....seedwork.application.queries import QueryHandler


class AgentQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._agent_factory: AutomationAgentFactory = AutomationAgentFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def agent_factory(self):
        return self._agent_factory
