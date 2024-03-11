from dataclasses import dataclass

from src.watchdog.seedwork.domain.events import DomainEvent


class PropertiesAndTransactionsEvent(DomainEvent):
    ...


@dataclass
class PropertyCreatedEvent(PropertiesAndTransactionsEvent):
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


@dataclass
class PropertyNotCreatedEvent(PropertiesAndTransactionsEvent):
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
