from dataclasses import dataclass
from colorama import Fore, Style

from .base import CountryRegulationBaseHandler
from ...domain.entities import CountryRegulation
from ...domain.repositories import CountryRegulationRepository
from ...domain.rules import CountryRegulationRule
from .....seedwork.domain.exceptions import DomainException
from .....seedwork.application.commands import Command
from ...domain.value_objects import Location
from .....seedwork.application.commands import execute_command as command
from .....seedwork.infrastructure.uow import UnitOfWorkPort

"""
Take a Property Ingestion Command and apply the country regulation to it
We need to create a new Property Ingestion with the country regulation applied
a country regulation is a set of rules that apply to a property ingestion
for example, a country regulation can define that a property must have a minimum of 2 bathrooms
or that the price of the property must be in a specific range.
Sine we are using deferred binding, we would have those rules in a CountryRegulation entity
"""


@dataclass
class ApplyCountryRegulationToPropertyIngestionCommand(Command):
    property_ingestion_id: str
    status: str
    agent_id: str
    location_city_name: str
    location_city_code: str
    location_country_name: str
    location_country_code: str
    location_address: str
    location_building: str
    location_floor: str
    location_inner_code: str
    location_coordinates_latitude: float
    location_coordinates_longitude: float
    location_additional_info: str
    property_type: str
    property_subtype: str
    rooms: int
    bathrooms: int
    parking_spaces: int
    construction_area: float
    land_area: float
    price: float
    currency: str
    price_per_m2: float
    price_per_ft2: float
    property_url: str
    property_images: str


class ApplyCountryRegulationHandler(CountryRegulationBaseHandler):

    def handle(self, command: ApplyCountryRegulationToPropertyIngestionCommand):
        try:
            country_code = command.location_country_code
            repository = self.repository_factory.create_object(CountryRegulationRepository.__class__)
            country_regulation: CountryRegulation = repository.get_by_country_code(country_code)

            if not country_regulation:
                raise DomainException(f"Country Regulation not found for country code {country_code}")

            def validate_country_regulation(country: CountryRegulation):
                for regulation in country.regulations:
                    rule = CountryRegulationRule(
                        entity=command,
                        fields=regulation.fields,
                        conditions=regulation.conditions
                    )
                    #TODO: shall we use a UnitOfWorkPort to register the batch? or just call the validate_rule method?

                    country_regulation.validate_rule(rule)

            country_regulation.approve_property_ingestion(command.__dict__)
            UnitOfWorkPort.register_batch(validate_country_regulation, country_regulation)
            UnitOfWorkPort.savepoint()
            UnitOfWorkPort.commit()
        except DomainException as e:
            print(f"{Fore.RED}Error:{Fore.LIGHTYELLOW_EX} [Country Regulations] CountryRegulation Failed: {e}{Style.RESET_ALL}")
            UnitOfWorkPort.rollback()
            #TODO: fire RollbackEvent


@command.register(ApplyCountryRegulationToPropertyIngestionCommand)
def execute_apply_country_regulation_command(command: ApplyCountryRegulationToPropertyIngestionCommand):
    handler = ApplyCountryRegulationHandler()
    handler.handle(command)
