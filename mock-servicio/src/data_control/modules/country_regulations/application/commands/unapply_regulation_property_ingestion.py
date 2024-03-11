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
class UnApplyCountryRegulationToPropertyIngestionCommand(Command):
    property_ingestion_id: str

class UnApplyCountryRegulationHandler(CountryRegulationBaseHandler):

    def handle(self, command: UnApplyCountryRegulationToPropertyIngestionCommand):
        try:
            # Nothing to do here, just print the command since there is no data stored to compensate
            print(f"{Fore.LIGHTYELLOW_EX} [Country Regulations] UnApplying CountryRegulation to PropertyIngestion: {command.property_ingestion_id}{Style.RESET_ALL}")
        except DomainException as e:
            print(f"{Fore.RED}Error:{Fore.LIGHTYELLOW_EX} [Country Regulations] CountryRegulation Failed: {e}{Style.RESET_ALL}")
            UnitOfWorkPort.rollback()
            #TODO: fire RollbackEvent


@command.register(UnApplyCountryRegulationToPropertyIngestionCommand)
def execute_apply_country_regulation_command(command: UnApplyCountryRegulationToPropertyIngestionCommand):
    handler = UnApplyCountryRegulationHandler()
    handler.handle(command)
