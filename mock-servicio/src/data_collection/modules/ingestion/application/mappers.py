from uuid import UUID

from ..application.dto import PropertyIngestionDTO
from ..domain.entities import PropertyIngestion
from ..domain.value_objects import Location, City, Country, Coordinates
from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepoMapper


class PropertyIngestionDTOJsonMapper(AppMapper):

    def dto_to_external(self, dto: PropertyIngestionDTO) -> dict:
        return {
            'id': dto.id
            , 'agent_id': dto.agent_id
            , 'location': {
                'city': {
                    'name': dto.location_city_name
                    , 'code': dto.location_city_code
                    , 'country': {
                        'name': dto.location_country_name
                        , 'code': dto.location_country_code
                    }

                }
                , 'address': dto.location_address
                , 'building': dto.location_building
                , 'floor': dto.location_floor
                , 'inner_code': dto.location_inner_code
                , 'coordinates': {
                    'latitude': dto.location_coordinates_latitude
                    , 'longitude': dto.location_coordinates_longitude
                }
                , 'additional_info': dto.location_additional_info
            }
            , 'property_type': dto.property_type
            , 'property_subtype': dto.property_subtype
            , 'rooms': dto.rooms
            , 'bathrooms': dto.bathrooms
            , 'parking_spaces': dto.parking_spaces
            , 'construction_area': dto.construction_area
            , 'land_area': dto.land_area
            , 'price': dto.price
            , 'currency': dto.currency
            , 'price_per_m2': dto.price_per_m2
            , 'price_per_ft2': dto.price_per_ft2
            , 'property_url': dto.property_url
            , 'property_images': dto.property_images
        }

    def external_to_dto(self, external: dict) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO(
            id=external.get('id')
            , agent_id=external.get('agent_id')
            , location_city_name=external.get('location', {}).get('city', {}).get('name')
            , location_city_code=external.get('location', {}).get('city', {}).get('code')
            , location_country_name=external.get('location', {}).get('city', {}).get('country').get('name')
            , location_country_code=external.get('location', {}).get('city', {}).get('country').get('code')
            , location_address=external.get('location', {}).get('address')
            , location_building=external.get('location', {}).get('building')
            , location_floor=external.get('location', {}).get('floor')
            , location_inner_code=external.get('location', {}).get('inner_code')
            , location_coordinates_latitude=external.get('location', {}).get('coordinates', {}).get('latitude')
            , location_coordinates_longitude=external.get('location', {}).get('coordinates', {}).get('longitude')
            , location_additional_info=external.get('location', {}).get('additional_info')
            , property_type=external.get('property_type')
            , property_subtype=external.get('property_subtype')
            , rooms=external.get('rooms')
            , bathrooms=external.get('bathrooms')
            , parking_spaces=external.get('parking_spaces')
            , construction_area=external.get('construction_area')
            , land_area=external.get('land_area')
            , price=external.get('price')
            , currency=external.get('currency')
            , price_per_m2=external.get('price_per_m2')
            , price_per_ft2=external.get('price_per_ft2')
            , property_url=external.get('property_url')
            , property_images=external.get('property_images')
        )
        return property_ingestion_dto


class PropertyIngestionMapper(RepoMapper):

    def get_type(self) -> type:
        return PropertyIngestion.__class__

    def entity_to_dto(self, entity: PropertyIngestion) -> PropertyIngestionDTO:
        property_ingestion_dto = PropertyIngestionDTO(
            id=str(entity.id)
            , agent_id=entity.agent_id
            , location_city_name=entity.location.city.name
            , location_city_code=entity.location.city.code
            , location_country_name=entity.location.city.country.name
            , location_country_code=entity.location.city.country.code
            , location_address=entity.location.address
            , location_building=entity.location.building
            , location_floor=entity.location.floor
            , location_inner_code=entity.location.inner_code
            , location_coordinates_latitude=entity.location.coordinates.latitude
            , location_coordinates_longitude=entity.location.coordinates.longitude
            , location_additional_info=entity.location.additional_info
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
            id=UUID(dto.id) if dto.id else None
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
