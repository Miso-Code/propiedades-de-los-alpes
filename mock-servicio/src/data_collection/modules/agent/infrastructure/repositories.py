from datetime import datetime
from uuid import UUID

from .dto import AgentDTO
from .mappers import AutomationAgentMapper
from ..domain.factories import AutomationAgentFactory
from ....config.db import db
from ..domain.entities import AutomationAgent
from ..domain.repositories import AgentRepository


class SQLAlchemyAutomationAgentRepository(AgentRepository):

    def __init__(self):
        self._property_ingestion_factory: AutomationAgentFactory = AutomationAgentFactory()

    @property
    def property_ingestion_factory(self) -> AutomationAgentFactory:
        return self._property_ingestion_factory

    def get_by_id(self, id: UUID) -> AutomationAgent:
        agent_db = db.session.query(AgentDTO).filter_by(id=str(id)).first()
        mapper = AutomationAgentMapper()
        agent: AutomationAgent = AutomationAgentFactory().create_object(agent_db, mapper)
        return agent

    def get_all(self) -> list[AutomationAgent]:
        all_agents_db = db.session.query(AgentDTO).all()
        mapper = AutomationAgentMapper()
        all_agents: list[AutomationAgent] = [
            AutomationAgentFactory().create_object(agent, mapper) for agent in all_agents_db
        ]
        return all_agents

    def add(self, entity: AutomationAgent):
        property_ingestion_dto = AutomationAgentFactory().create_object(entity, AutomationAgentMapper())
        db.session.add(property_ingestion_dto)
        db.session.commit()
        db.session.refresh(property_ingestion_dto)

    def update(self, entity: AutomationAgent):
        update_entity: AgentDTO = AutomationAgentFactory().create_object(entity, AutomationAgentMapper())
        db.session.query(AgentDTO).filter_by(id=str(entity.id)).update({
            "first_name": update_entity.first_name,
            "last_name": update_entity.last_name,
            "automation_source": update_entity.automation_source,
            "automation_protocol": update_entity.automation_protocol,
            "automation_port": update_entity.automation_port,
            "automation_username": update_entity.automation_username,
            "automation_password": update_entity.automation_password,
            "automation_frequency_unit": update_entity.automation_frequency_unit,
            "automation_frequency_value": update_entity.automation_frequency_value,
            "automation_last_run": datetime.strptime(update_entity.automation_last_run, "%Y-%m-%dT%H:%M:%S.%f"),
            "started_executions": update_entity.started_executions
        })

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
