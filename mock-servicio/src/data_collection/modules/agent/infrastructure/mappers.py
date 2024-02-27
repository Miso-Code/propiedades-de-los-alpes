from uuid import UUID
from .dto import AgentDTO
from ..domain.entities import AutomationAgent
from ..domain.value_objects import Name, Automation, Authentication, ExecutionFrequency
from ....seedwork.domain.repositories import Mapper


class AutomationAgentMapper(Mapper):

    def get_type(self) -> type:
        return AutomationAgent.__class__

    def entity_to_dto(self, entity: AutomationAgent) -> AgentDTO:
        automation_agent_dto = AgentDTO()
        automation_agent_dto.id = str(entity.id)
        automation_agent_dto.first_name = entity.creator_name.name
        automation_agent_dto.last_name = entity.creator_name.last_name
        automation_agent_dto.automation_source = entity.automation.source
        automation_agent_dto.automation_protocol = entity.automation.protocol
        automation_agent_dto.automation_port = entity.automation.port
        automation_agent_dto.automation_username = entity.automation.auth.username
        automation_agent_dto.automation_password = entity.automation.auth.password
        automation_agent_dto.automation_frequency_unit = entity.automation.frequency.unit
        automation_agent_dto.automation_frequency_value = entity.automation.frequency.value
        automation_agent_dto.automation_last_run = entity.automation.last_execution
        return automation_agent_dto

    def dto_to_entity(self, dto: AgentDTO) -> AutomationAgent:
        automation_agent = AutomationAgent(
            id=UUID(dto.id)
            , creator_name=Name(
                name=dto.first_name
                , last_name=dto.last_name
            )
            , automation=Automation(
                source=dto.automation_source
                , protocol=dto.automation_protocol
                , port=dto.automation_port
                , auth=Authentication(
                    username=dto.automation_username
                    , password=dto.automation_password
                )
                , frequency=ExecutionFrequency(
                    unit=dto.automation_frequency_unit
                    , value=dto.automation_frequency_value
                )
                , last_execution=dto.automation_last_run
            )
        )
        return automation_agent
