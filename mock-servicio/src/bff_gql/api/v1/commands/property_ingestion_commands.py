from pulsar.schema import *

from src.bff_gql.api.v1.commands.integration_command import IntegrationCommand


class CreatePropertyIngestionPayload(IntegrationCommand):
    agent_id: str = String()
    location_city_name: str = String()
    location_city_code: str = String()
    location_country_name: str = String()
    location_country_code: str = String()
    location_address: str = String()
    location_building: str = String()
    location_floor: str = String()
    location_inner_code: str = String()
    location_coordinates_latitude: float = Float()
    location_coordinates_longitude: float = Float()
    location_additional_info: str = String()
    property_type: str = String()
    property_subtype: str = String()
    rooms: int = Integer()
    bathrooms: int = Integer()
    parking_spaces: int = Integer()
    construction_area: float = Float()
    land_area: float = Float()
    price: float = Float()
    currency: str = String()
    price_per_m2: float = Float()
    price_per_ft2: float = Float()
    property_url: str = String()
    property_images: str = String()


class CreatePropertyIngestionCommandSchema(IntegrationCommand):
    data = CreatePropertyIngestionPayload()
