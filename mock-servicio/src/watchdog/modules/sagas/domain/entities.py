from dataclasses import dataclass, field
from ....seedwork.domain.entities import Entity, RootAggregate


@dataclass
class SagaLog(RootAggregate):
    correlation_id: str = field(default_factory=str)
    status: str = field(default_factory=str)
    transaction_id: str = field(default_factory=str)


@dataclass
class Transaction(Entity):
    event: str = field(default_factory=str)
    error: str = field(default_factory=str)
    compensation: str = field(default_factory=str)
    order: int = field(default_factory=int)
    is_last: bool = field(default_factory=bool)
    compensation_topic: str = field(default_factory=str)
