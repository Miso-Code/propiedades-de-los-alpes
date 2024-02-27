import uuid

from .dto import AutomationAgentDTO
from .mappers import AutomationAgentMapper
from ..domain.entities import AutomationAgent
from ..domain.factories import AutomationAgentFactory
from ..domain.repositories import AgentRepository
from ..infrastructure.factories import RepositoryFactory
from ....seedwork.domain.services import Service
from ....seedwork.infrastructure.uow import UnitOfWorkPort


class AgentService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._agent_factory: AutomationAgentFactory = AutomationAgentFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def agent_factory(self):
        return self._agent_factory

    def create_automation_agent(self, agent_dto: AutomationAgentDTO) -> AutomationAgent:
        agent: AutomationAgent = self.agent_factory.create_object(agent_dto,
                                                                  AutomationAgentMapper())
        repository = self.repository_factory.create_object(AgentRepository.__class__)

        UnitOfWorkPort.register_batch(repository.add, agent)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()

        return self.agent_factory.create_object(agent, AutomationAgentMapper())

    def get_all_automation_agents(self) -> list[AutomationAgent]:
        repository = self.repository_factory.create_object(AgentRepository.__class__)
        agents: list[AutomationAgent] = repository.get_all()
        return agents

    def update_automation_agent(self, agent_id: uuid.UUID, agent_dto: AutomationAgentDTO):
        agent: AutomationAgent = self.agent_factory.create_object(agent_dto,
                                                                  AutomationAgentMapper())
        agent.id = agent_id
        repository = self.repository_factory.create_object(AgentRepository.__class__)
        UnitOfWorkPort.register_batch(repository.update, agent)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()
        return agent

