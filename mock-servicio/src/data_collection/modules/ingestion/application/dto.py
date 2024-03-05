from dataclasses import dataclass
from typing import Optional

from ..domain.value_objects import Location
from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class PropertyIngestionDTO(DTO):
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
    id: Optional[str] = None
