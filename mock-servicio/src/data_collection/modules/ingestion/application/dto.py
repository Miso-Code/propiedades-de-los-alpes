from dataclasses import dataclass

from ..domain.value_objects import Location
from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class PropertyIngestionDTO(DTO):
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
