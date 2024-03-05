from dataclasses import dataclass
from colorama import Fore, Style

from .base import CreatePropertiesBaseHandler
from .....seedwork.application.commands import Command
from .....seedwork.application.commands import execute_command as command
from .....seedwork.infrastructure.uow import UnitOfWorkPort

from ...domain.repositories import PropertyPropertiesRepository

from ..dto import PropertyPropertiesDTO

from ..mappers import PropertyMapper

@dataclass
class RegisterPropertiesCommand(Command): 
    agent_id: str
    property_id: str
    property_address: str
    property_city: str
    property_state: str
    property_zip: str
    property_price: int
    property_bedrooms: int
    property_bathrooms: int
    property_square_feet: int
    property_lot_size: int
    property_type: str

class RegisterPropertiesHandler(CreatePropertiesBaseHandler):
    def handle(self, command: RegisterPropertiesCommand):
        try:
            property_properties_dto = PropertyPropertiesDTO(
                agent_id=command.agent_id,
                property_id=command.property_id,
                property_address=command.property_address,
                property_city=command.property_city,
                property_state=command.property_state,
                property_zip=command.property_zip,
                property_price=command.property_price,
                property_bedrooms=command.property_bedrooms,
                property_bathrooms=command.property_bathrooms,
                property_square_feet=command.property_square_feet,
                property_lot_size=command.property_lot_size,
                property_type=command.property_type,
            )
            
            property = self.property_factory.create_object(property_properties_dto, PropertyMapper())
            
            property.create_property()
            
            repository = self.repository_factory.create_object(PropertyPropertiesRepository.__class__)

            UnitOfWorkPort.register_batch(repository.add,property)
            UnitOfWorkPort.savepoint()
            UnitOfWorkPort.commit()
            
        except Exception as e:
            print(Fore.RED + f'Error registering property: {e}')
            print(Style.RESET_ALL)
            UnitOfWorkPort.rollback()
            

@command.register(RegisterPropertiesCommand)
def execute_register_properties_command(command: RegisterPropertiesCommand):
    handler = RegisterPropertiesHandler()
    handler.handle(command)