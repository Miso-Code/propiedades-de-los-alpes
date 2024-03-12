from dataclasses import dataclass

from src.watchdog.seedwork.domain.events import DomainEvent


class DataControlEvent(DomainEvent):
    ...


@dataclass
class PropertyIngestionApprovedEvent(DataControlEvent):
    property_ingestion_id: str = None
    status: str = None
    agent_id: str = None
    location_city_name: str = None
    location_city_code: str = None
    location_country_name: str = None
    location_country_code: str = None
    location_address: str = None
    location_building: str = None
    location_floor: str = None
    location_inner_code: str = None
    location_coordinates_latitude: float = None
    location_coordinates_longitude: float = None
    location_additional_info: str = None
    property_type: str = None
    property_subtype: str = None
    rooms: int = None
    bathrooms: int = None
    parking_spaces: int = None
    construction_area: float = None
    land_area: float = None
    price: float = None
    currency: str = None
    price_per_m2: float = None
    price_per_ft2: float = None
    property_url: str = None
    property_images: str = None

class PropertyIngestionRejectedEvent(DataControlEvent):
    property_ingestion_id: str = None
    status: str = None
    agent_id: str = None
    location_city_name: str = None
    location_city_code: str = None
    location_country_name: str = None
    location_country_code: str = None
    location_address: str = None
    location_building: str = None
    location_floor: str = None
    location_inner_code: str = None
    location_coordinates_latitude: float = None
    location_coordinates_longitude: float = None
    location_additional_info: str = None
    property_type: str = None
    property_subtype: str = None
    rooms: int = None
    bathrooms: int = None
    parking_spaces: int = None
    construction_area: float = None
    land_area: float = None
    price: float = None
    currency: str = None
    price_per_m2: float = None
    price_per_ft2: float = None
    property_url: str = None
    property_images: str = None