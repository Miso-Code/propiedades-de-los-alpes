from dataclasses import dataclass
from src.watchdog.seedwork.domain.events import DomainEvent


class DataCollectionEvent(DomainEvent):
    ...


@dataclass
class PropertyIngestionStartedEvent(DataCollectionEvent):
    property_ingestion_id: str = None
    agent_id: str = None
    status: str = None
    started_at: str = None
