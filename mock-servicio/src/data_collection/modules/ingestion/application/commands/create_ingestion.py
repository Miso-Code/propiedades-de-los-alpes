from dataclasses import dataclass

from ..commands.base import CreateIngestionBaseHandler
from ..dto import PropertyIngestionDTO
from ..mappers import PropertyIngestionMapper
from ...domain.entities import PropertyIngestion
from ...domain.repositories import PropertyIngestionRepository
from ......data_collection.seedwork.application.commands import Command
from .....seedwork.application.commands import execute_command as command
from .....seedwork.infrastructure.uow import UnitOfWorkPort


@dataclass
class CreatePropertyIngestionCommand(Command):
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


class CreateIngestionHandler(CreateIngestionBaseHandler):
    def handle(self, command: CreatePropertyIngestionCommand):
        # TODO: UPDATE INGESTION STATUS!!!!!!!!! :sparkles:
        property_ingestion_dto = PropertyIngestionDTO(
            agent_id=command.agent_id
            , location_city_name=command.location_city_name
            , location_city_code=command.location_city_code
            , location_country_name=command.location_country_name
            , location_country_code=command.location_country_code
            , location_address=command.location_address
            , location_building=command.location_building
            , location_floor=command.location_floor
            , location_inner_code=command.location_inner_code
            , location_coordinates_latitude=command.location_coordinates_latitude
            , location_coordinates_longitude=command.location_coordinates_longitude
            , location_additional_info=command.location_additional_info
            , property_type=command.property_type
            , property_subtype=command.property_subtype
            , rooms=command.rooms
            , bathrooms=command.bathrooms
            , parking_spaces=command.parking_spaces
            , construction_area=command.construction_area
            , land_area=command.land_area
            , price=command.price
            , currency=command.currency
            , price_per_m2=command.price_per_m2
            , price_per_ft2=command.price_per_ft2
            , property_url=command.property_url
            , property_images=command.property_images
        )

        property_ingestion: PropertyIngestion = self._property_ingestion_factory.create_object(property_ingestion_dto,
                                                                                               PropertyIngestionMapper())
        property_ingestion.create_property_ingestion()

        repository = self.repository_factory.create_object(PropertyIngestionRepository.__class__)

        UnitOfWorkPort.register_batch(repository.add, property_ingestion)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(CreatePropertyIngestionCommand)
def execute_create_property_ingestion_command(command: CreatePropertyIngestionCommand):
    handler = CreateIngestionHandler()
    handler.handle(command)
