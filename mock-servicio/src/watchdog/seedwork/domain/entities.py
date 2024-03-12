import uuid
from dataclasses import dataclass, field
from datetime import datetime
from .events import DomainEvent
from .mixins import ValidateRulesMixin
from .rules import ImmutableEntityId
from .exceptions import ImmutableIdException


@dataclass
class Entity:
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    id: uuid.UUID = field(hash=True)
    creation_date: datetime = field(default=datetime.now())
    update_date: datetime = field(default=datetime.now())

    @classmethod
    def next_id(cls) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, input_id: uuid.UUID) -> None:
        if not ImmutableEntityId(self).is_valid():
            raise ImmutableIdException()
        self._id = input_id if isinstance(input_id, uuid.UUID) else self.next_id()


@dataclass
class RootAggregate(Entity, ValidateRulesMixin):
    events: list[DomainEvent] = field(default_factory=list)

    def add_event(self, event: DomainEvent) -> object:
        self.events.append(event)

    def clear_events(self):
        self.events = list()
