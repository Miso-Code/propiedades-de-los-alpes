from __future__ import annotations

import uuid
from dataclasses import dataclass
from ....seedwork.domain.events import (DomainEvent)
from datetime import datetime


@dataclass
class PropertyIngestionStartedEvent(DomainEvent):
    id_property_ingestion: str = None
    status: str = None
    started_at: str = None
