from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class AutomationAgentDTO(DTO):
    creator_name_first_name: str
    creator_name_last_name: str
    automation_source: str
    automation_protocol: str
    automation_port: int
    automation_username: str
    automation_password: str
    automation_frequency_unit: str
    automation_frequency_value: int
    started_executions: int = 0
    automation_last_run: Optional[datetime] = None
    id: Optional[str] = None
