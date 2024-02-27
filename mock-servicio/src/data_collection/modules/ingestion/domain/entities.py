from dataclasses import dataclass, field
from datetime import datetime

from ..infrastructure.schema.v1.events import PropertyIngestionCreatedEvent
from ....seedwork.domain.entities import RootAggregate
from .value_objects import Location, PropertyIngestionStatus
from .events import PropertyIngestionStartedEvent


@dataclass
class PropertyIngestion(RootAggregate):
    status: PropertyIngestionStatus = field(default=PropertyIngestionStatus.PENDING)
    location: Location = field(default_factory=str)
    property_type: str = field(default_factory=str)
    property_subtype: str = field(default_factory=str)
    rooms: int = field(default_factory=int)
    bathrooms: int = field(default_factory=int)
    parking_spaces: int = field(default_factory=int)
    construction_area: float = field(default_factory=float)
    land_area: float = field(default_factory=float)
    price: float = field(default_factory=float)
    currency: str = field(default_factory=str)
    price_per_m2: float = field(default_factory=float)
    price_per_ft2: float = field(default_factory=float)
    property_url: str = field(default_factory=str)
    property_images: list = field(default_factory=list)

    def create_property_ingestion(self):
        self.add_event(PropertyIngestionStartedEvent(
            id_property_ingestion=str(self.id),
            status=PropertyIngestionStatus.IN_PROGRESS,
            started_at=datetime.now().isoformat()
        ))
