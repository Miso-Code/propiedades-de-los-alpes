from uuid import UUID

from colorama import Fore, Style

from .mappers import AutomationAgentMapper, AutomationAgentDTOJsonMapper
from .services import AgentService
from ....seedwork.application.handlers import Handler


class HandleAgentDomain(Handler):

    @staticmethod
    def handle_property_ingestion_started(event):
        try:
            print(Fore.CYAN + f'[Agent] Ingestion started for agent {event.agent_id}. Ingestion: ', event)
            print(Style.RESET_ALL)

            agent_service = AgentService()
            agent = agent_service.get_automation_agent_by_id(UUID(event.agent_id))

            mapper = AutomationAgentMapper()
            json_mapper = AutomationAgentDTOJsonMapper()

            agent_dto = mapper.entity_to_dto(agent)
            updated_agent = json_mapper.dto_to_external(agent_dto)
            updated_agent['started_executions'] += 1

            updated_agent_dto = json_mapper.external_to_dto(updated_agent)

            print(Fore.CYAN +
                  f'[Agent] Agent {updated_agent_dto.id} started executions: ', updated_agent_dto.started_executions)
            print(Style.RESET_ALL)
            agent_service.update_automation_agent(updated_agent_dto)
        except Exception:
            print(Fore.CYAN + '[Agent] Error while handling ingestion started event.', event)
            print(Style.RESET_ALL)
