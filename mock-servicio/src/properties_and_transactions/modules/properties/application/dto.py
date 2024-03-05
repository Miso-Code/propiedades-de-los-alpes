from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class PropertyPropertiesDTO(DTO):
    agent_id: str
    property_id: str
    property_address: str
    property_city: str
    property_state: str
    property_zip: str
    property_price: int
    property_bedrooms: int
    property_bathrooms: int
    property_square_feet: int
    property_lot_size: int
    property_type: str
    id: Optional[str] = None
    