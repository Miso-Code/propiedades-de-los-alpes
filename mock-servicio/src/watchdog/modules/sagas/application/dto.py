from dataclasses import dataclass
from typing import Optional

from ....seedwork.application.dto import DTO


@dataclass(frozen=True)
class SagaLogDTO(DTO):
    correlation_id: str
    status: str
    transaction_id: str
    id: Optional[str] = None

@dataclass(frozen=True)
class TransactionDTO(DTO):
    event: str
    error: str
    compensation: str
    order: int
    is_last: bool
    compensation_topic: Optional[str] = None
    id: Optional[str] = None
