from __future__ import annotations

import uuid
from dataclasses import dataclass
from ....seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class PropertyCreatedEvent(DomainEvent):
    agent_id: str = None
    property_id: str = None
    property_address: str = None
    property_city: str = None
    property_state: str = None
    property_zip: str = None
    property_price: float = None
    property_bedrooms: int = None
    property_bathrooms: int = None
    property_square_feet: int = None
    property_lot_size: int = None
    property_type: str = None
