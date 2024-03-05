from dataclasses import dataclass, field
from datetime import datetime

from ..infrastructure.schema.v1.events import PropertyIngestionCreatedEvent
from ....seedwork.domain.entities import RootAggregate
from .value_objects import Location, PropertyIngestionStatus
from .events import PropertyIngestionStartedEvent


@dataclass
class PropertyIngestion(RootAggregate):
    agent_id: str = field(default_factory=str)
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
            property_ingestion_id=str(self.id),
            agent_id=self.agent_id,
            status=PropertyIngestionStatus.IN_PROGRESS,
            started_at=datetime.now().isoformat()
        ))
