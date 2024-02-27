from ..application.dto import PropertyIngestionDTO
from ..domain.entities import PropertyIngestion
from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepoMapper


class PropertyIngestionDTOJsonMapper(AppMapper):

    def dto_to_external(self, dto: PropertyIngestionDTO) -> dict:
        return dto.__dict__

    def external_to_dto(self, external: dict) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO(**external)
        return property_ingestion_dto


class PropertyIngestionMapper(RepoMapper):

    def get_type(self) -> type:
        return PropertyIngestion.__class__

    def entity_to_dto(self, entity: PropertyIngestion) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO(
            location=entity.location
            , property_type=entity.property_type
            , property_subtype=entity.property_subtype
            , rooms=entity.rooms
            , bathrooms=entity.bathrooms
            , parking_spaces=entity.parking_spaces
            , construction_area=entity.construction_area
            , land_area=entity.land_area
            , price=entity.price
            , currency=entity.currency
            , price_per_m2=entity.price_per_m2
            , price_per_ft2=entity.price_per_ft2
            , property_url=entity.property_url
            , property_images=entity.property_images
        )
        return property_ingestion_dto

    def dto_to_entity(self, dto: PropertyIngestionDTO) -> PropertyIngestion:
        property_ingestion = PropertyIngestion(
            location=dto.location
            , property_type=dto.property_type
            , property_subtype=dto.property_subtype
            , rooms=dto.rooms
            , bathrooms=dto.bathrooms
            , parking_spaces=dto.parking_spaces
            , construction_area=dto.construction_area
            , land_area=dto.land_area
            , price=dto.price
            , currency=dto.currency
            , price_per_m2=dto.price_per_m2
            , price_per_ft2=dto.price_per_ft2
            , property_url=dto.property_url
            , property_images=dto.property_images
        )
        return property_ingestion
