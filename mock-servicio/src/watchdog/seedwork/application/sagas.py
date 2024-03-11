import datetime
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from src.watchdog.seedwork.domain.events import DomainEvent
from .commands import execute_command
from ..application.commands import Command


class SagaCoordinator(ABC):
    correlation_id: uuid.UUID

    @abstractmethod
    def persist_in_saga_log(self, message):
        ...

    @abstractmethod
    def build_command(self, event: DomainEvent, command_type: type) -> Command:
        ...

    def publish_command(self, event: DomainEvent, command_type: type):
        command = self.build_command(event, command_type)
        execute_command(command)

    @abstractmethod
    def initialize_steps(self):
        ...

    @abstractmethod
    def process_event(self, event: DomainEvent):
        ...

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def end(self):
        ...


class Step:
    correlation_id: uuid.UUID
    event_date: datetime.datetime
    index: int


@dataclass
class Start(Step):
    index: int = 0


@dataclass
class End(Step):
    ...


@dataclass
class Transaction(Step):
    command: Command
    event: DomainEvent
    error: DomainEvent
    compensation: Command
    successful: bool


class ChoreographyCoordinator(SagaCoordinator, ABC):

    def __init__(self):
        super().__init__()
        self.transactions: List[Transaction] = []

    def initialize_steps(self, steps: List[Transaction]):
        self.transactions = steps

    def start(self):
        self.persist_in_saga_log(self.transactions[0])

    def end(self):
        self.persist_in_saga_log(self.transactions[-1])

    def process_event(self, event: DomainEvent):
        for transaction in self.transactions:
            if isinstance(event, transaction.event):
                self.execute_command(transaction.command, event)
                break

    def execute_command(self, command_type: Command, event):
        ...

    @abstractmethod
    def persist_in_saga_log(self, message):
        ...
