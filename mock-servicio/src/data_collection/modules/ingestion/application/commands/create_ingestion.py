from dataclasses import dataclass

from ..commands.base import CreateIngestionBaseHandler
from ..dto import PropertyIngestionDTO
from ..mappers import PropertyIngestionMapper
from ...domain.entities import PropertyIngestion
from ...domain.repositories import PropertyIngestionRepository
from ...infrastructure.schema.v1.commands import CreatePropertyIngestionPayload
from ......data_collection.seedwork.application.commands import Command
from ...domain.value_objects import Location
from .....seedwork.application.commands import execute_command as command
from .....seedwork.infrastructure.uow import UnitOfWorkPort


@dataclass
class CreatePropertyIngestionCommand(Command):
    agent_id: str
    location: Location
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
    property_images: list

    def __init__(self, property_ingestion_data: CreatePropertyIngestionPayload | PropertyIngestionDTO):
        self.agent_id = property_ingestion_data.agent_id
        self.location = property_ingestion_data.location
        self.property_type = property_ingestion_data.property_type
        self.property_subtype = property_ingestion_data.property_subtype
        self.rooms = property_ingestion_data.rooms
        self.bathrooms = property_ingestion_data.bathrooms
        self.parking_spaces = property_ingestion_data.parking_spaces
        self.construction_area = property_ingestion_data.construction_area
        self.land_area = property_ingestion_data.land_area
        self.price = property_ingestion_data.price
        self.currency = property_ingestion_data.currency
        self.price_per_m2 = property_ingestion_data.price_per_m2
        self.price_per_ft2 = property_ingestion_data.price_per_ft2
        self.property_url = property_ingestion_data.property_url
        self.property_images = property_ingestion_data.property_images


class CreateIngestionHandler(CreateIngestionBaseHandler):

    def handle(self, command: CreatePropertyIngestionCommand):
        property_ingestion_dto = PropertyIngestionDTO(
            agent_id=command.agent_id
            , location=command.location
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
