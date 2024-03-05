from dataclasses import dataclass, field
from datetime import datetime

from .events import PropertyCreatedEvent

from ....seedwork.domain.entities import RootAggregate

@dataclass
class Property(RootAggregate):
    agent_id: str = field(default_factory=str)
    property_id: str = field(default_factory=str)
    property_address: str = field(default_factory=str)
    property_city: str = field(default_factory=str)
    property_state: str = field(default_factory=str)
    property_zip: str = field(default_factory=str)
    property_price: int = field(default_factory=int)
    property_bedrooms: int = field(default_factory=int)
    property_bathrooms: int = field(default_factory=int)
    property_square_feet: int = field(default_factory=int)
    property_lot_size: int = field(default_factory=int)
    property_type: str = field(default_factory=str)
    
    def create_property(self):
        self.add_event(PropertyCreatedEvent(
            agent_id=self.agent_id,
            property_id=self.property_id,
            property_address=self.property_address,
            property_city=self.property_city,
            property_state=self.property_state,
            property_zip=self.property_zip,
            property_price=self.property_price,
            property_bedrooms=self.property_bedrooms,
            property_bathrooms=self.property_bathrooms,
            property_square_feet=self.property_square_feet,
            property_lot_size=self.property_lot_size,
            property_type=self.property_type,
        ))