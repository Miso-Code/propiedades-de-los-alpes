from .dto import PropertyIngestionDTO
from ..domain.entities import PropertyIngestion
from ....seedwork.domain.repositories import Mapper


class PropertyIngestionMapper(Mapper):

    def get_type(self) -> type:
        return PropertyIngestion.__class__

    def entity_to_dto(self, entity: PropertyIngestion) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO()
        property_ingestion_dto.id = str(entity.id)
        # property_ingestion_dto.location = entity.location #TODO: Implment nested mapper
        property_ingestion_dto.property_type = entity.property_type
        property_ingestion_dto.property_subtype = entity.property_subtype
        property_ingestion_dto.rooms = entity.rooms
        property_ingestion_dto.bathrooms = entity.bathrooms
        property_ingestion_dto.parking_spaces = entity.parking_spaces
        property_ingestion_dto.construction_area = entity.construction_area
        property_ingestion_dto.land_area = entity.land_area
        property_ingestion_dto.price = entity.price
        property_ingestion_dto.currency = entity.currency
        property_ingestion_dto.price_per_m2 = entity.price_per_m2
        property_ingestion_dto.price_per_ft2 = entity.price_per_ft2
        property_ingestion_dto.property_url = entity.property_url
        property_ingestion_dto.property_images = entity.property_images
        return property_ingestion_dto

    def dto_to_entity(self, dto: PropertyIngestionDTO) -> PropertyIngestion:
        property_ingestion = PropertyIngestion(dto)
        return property_ingestion
