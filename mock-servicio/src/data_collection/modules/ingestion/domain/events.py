from __future__ import annotations

import uuid
from dataclasses import dataclass
from ....seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class PropertyIngestionStartedEvent(DomainEvent):
    property_ingestion_id: str = None
    agent_id: str = None
    status: str = None
    started_at: str = None
