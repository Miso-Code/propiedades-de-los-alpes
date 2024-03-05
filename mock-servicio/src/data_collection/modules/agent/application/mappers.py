from uuid import UUID

from ..application.dto import AutomationAgentDTO
from ..domain.entities import AutomationAgent
from ..domain.value_objects import Name, Automation, Authentication, ExecutionFrequency
from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepoMapper


class AutomationAgentDTOJsonMapper(AppMapper):

    def dto_to_external(self, dto: AutomationAgentDTO) -> dict:
        return dict(
            id=dto.id
            , creator_name=dict(
                first_name=dto.creator_name_first_name
                , last_name=dto.creator_name_last_name
            )
            , automation=dict(
                source=dto.automation_source
                , protocol=dto.automation_protocol
                , port=dto.automation_port
                , auth=dict(
                    username=dto.automation_username
                    , password=dto.automation_password
                )
                , frequency=dict(
                    unit=dto.automation_frequency_unit
                    , value=dto.automation_frequency_value
                ),
                last_execution=dto.automation_last_run.isoformat() if dto.automation_last_run else None
            )
            , started_executions=dto.started_executions
        )

    def external_to_dto(self, external: dict) -> AutomationAgentDTO:
        automation_agent_dto = AutomationAgentDTO(
            id=external.get('id', None)
            , creator_name_first_name=external['creator_name']['first_name']
            , creator_name_last_name=external['creator_name']['last_name']
            , automation_source=external['automation']['source']
            , automation_protocol=external['automation']['protocol']
            , automation_port=external['automation']['port']
            , automation_username=external['automation']['auth']['username']
            , automation_password=external['automation']['auth']['password']
            , automation_frequency_unit=external['automation']['frequency']['unit']
            , automation_frequency_value=external['automation']['frequency']['value']
            , automation_last_run=external['automation'].get('last_execution')
            , started_executions=external.get('started_executions', 0)
        )
        return automation_agent_dto


class AutomationAgentMapper(RepoMapper):

    def get_type(self) -> type:
        return AutomationAgent.__class__

    def entity_to_dto(self, entity: AutomationAgent) -> AutomationAgentDTO:
        automation_agent_dto = AutomationAgentDTO(
            id=str(entity.id)
            , creator_name_first_name=entity.creator_name.name
            , creator_name_last_name=entity.creator_name.last_name
            , automation_source=entity.automation.source
            , automation_protocol=entity.automation.protocol
            , automation_port=entity.automation.port
            , automation_username=entity.automation.auth.username
            , automation_password=entity.automation.auth.password
            , automation_frequency_unit=entity.automation.frequency.unit
            , automation_frequency_value=entity.automation.frequency.value
            , automation_last_run=entity.automation.last_execution
            , started_executions=entity.started_executions
        )
        return automation_agent_dto

    def dto_to_entity(self, dto: AutomationAgentDTO) -> AutomationAgent:
        automation_agent = AutomationAgent(
            id=UUID(dto.id) if dto.id else None
            , creator_name=Name(
                name=dto.creator_name_first_name
                , last_name=dto.creator_name_last_name
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
            , started_executions=dto.started_executions
        )
        return automation_agent
