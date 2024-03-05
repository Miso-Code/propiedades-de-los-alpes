import time
from datetime import datetime
from colorama import Fore, Style

from faker import Faker
from flask.ctx import AppContext, RequestContext

from .dispatchers import Dispatcher
from ..application.mappers import AutomationAgentDTOJsonMapper, AutomationAgentMapper
from ..application.services import AgentService
from ..domain.entities import AutomationAgent

dispatcher = Dispatcher()
faker = Faker()


def cron_job(context: AppContext, req_context: RequestContext):
    with context and req_context:
        while True:
            agent_automation(context, req_context)
            time.sleep(5)


def agent_automation(context: AppContext, req_context: RequestContext):
    agents = AgentService().get_all_automation_agents()
    for agent in agents:
        first_time = agent.automation.last_execution is None
        time_since_last_execution = datetime.now() - (agent.automation.last_execution or datetime.now())
        if first_time or time_since_last_execution.seconds > agent.automation.frequency.value:  # only seconds for now
            print(Fore.CYAN + f"[Agent] [Job] Agent {agent.id} ready to execute." + Style.RESET_ALL)
            ingestion_data = get_property_ingestion_from_automation(agent)
            dispatcher.publish_command(ingestion_data, "property-ingestion-commands")

            agent_dto = AutomationAgentMapper().entity_to_dto(agent)
            json_agent = AutomationAgentDTOJsonMapper().dto_to_external(agent_dto)
            json_agent["automation"]["last_execution"] = datetime.now().isoformat()

            updated_agent = AutomationAgentDTOJsonMapper().external_to_dto(json_agent)

            AgentService().update_automation_agent(updated_agent)
            print(Fore.CYAN + f"[Agent] [Job] Agent {agent.id} executed." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"[Agent] [Job] Agent {agent.id} not ready, would execute in "
                              f"{agent.automation.frequency.value - time_since_last_execution.seconds} seconds." + Style.RESET_ALL)


def get_property_ingestion_from_automation(agent: AutomationAgent):
    return {
        "agent_id": agent.id,
        "location": {
            "city": {
                "name": faker.city(),
                "code": faker.country_code(),
                "country": {
                    "name": faker.country(),
                    "code": faker.country_code()
                }
            },
            "address": faker.street_address(),
            "building": faker.company(),
            "floor": faker.random_int(min=1, max=5000),
            "inner_code": faker.sentence(),
            "coordinates": {
                "latitude": str(faker.latitude()),
                "longitude": str(faker.longitude())
            },
            "additional_info": faker.text(max_nb_chars=200)
        },
        "property_type": faker.word(),
        "property_subtype": faker.word(),
        "rooms": faker.random.randint(0, 10),  # Number of rooms
        "bathrooms": faker.random.randint(0, 10),  # Number of bathrooms
        "parking_spaces": faker.random.randint(0, 10),  # Number of parking spaces
        "construction_area": faker.random.randint(100, 1000),
        "land_area": faker.random.randint(100, 10_000),  # Land area in square meters or your unit of choice
        "price": faker.random.randint(0, 10000000),  # Price of the property
        "currency": faker.currency_code(),
        "price_per_m2": faker.random.randint(100, 10_000),  # Price per square meter
        "price_per_ft2": faker.random.randint(100, 10_000),  # Price per square foot
        "property_url": faker.url(),
        "property_images": faker.url()  # List of URLs to property images
    }
