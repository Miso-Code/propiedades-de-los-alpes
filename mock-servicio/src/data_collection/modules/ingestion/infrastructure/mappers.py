from uuid import UUID

from .dto import PropertyIngestionDTO
from ..domain.entities import PropertyIngestion
from ..domain.value_objects import Location, City, Country, Coordinates
from ....seedwork.domain.repositories import Mapper


class PropertyIngestionMapper(Mapper):

    def get_type(self) -> type:
        return PropertyIngestion.__class__

    def entity_to_dto(self, entity: PropertyIngestion) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO()
        property_ingestion_dto.id = str(entity.id)
        property_ingestion_dto.agent_id = entity.agent_id
        property_ingestion_dto.location_city_name = entity.location.city.name
        property_ingestion_dto.location_city_code = entity.location.city.code
        property_ingestion_dto.location_country_name = entity.location.city.country.name
        property_ingestion_dto.location_country_code = entity.location.city.country.code
        property_ingestion_dto.location_address = entity.location.address
        property_ingestion_dto.location_building = entity.location.building
        property_ingestion_dto.location_floor = entity.location.floor
        property_ingestion_dto.location_inner_code = entity.location.inner_code
        property_ingestion_dto.location_coordinates_latitude = entity.location.coordinates.latitude
        property_ingestion_dto.location_coordinates_longitude = entity.location.coordinates.longitude
        property_ingestion_dto.location_additional_info = entity.location.additional_info
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
        property_ingestion = PropertyIngestion(
            id=UUID(dto.id)
            , agent_id=dto.agent_id
            , location=Location(
                city=City(
                    name=dto.location_city_name
                    , code=dto.location_city_code
                    , country=Country(
                        name=dto.location_country_name
                        , code=dto.location_country_code
                    )
                )
                , address=dto.location_address
                , building=dto.location_building
                , floor=dto.location_floor
                , inner_code=dto.location_inner_code
                , coordinates=Coordinates(
                    latitude=dto.location_coordinates_latitude
                    , longitude=dto.location_coordinates_longitude
                )
                , additional_info=dto.location_additional_info
            )
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
