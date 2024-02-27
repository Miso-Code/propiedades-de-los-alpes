from dataclasses import dataclass
from datetime import datetime

from ....seedwork.domain.value_objects import ValueObject


@dataclass(frozen=True)
class Authentication(ValueObject):
    username: str
    password: str

@dataclass(frozen=True)
class ExecutionFrequency(ValueObject):
    unit: str # seconds, minutes, hours, days, weeks or months
    value: int # every X unit

@dataclass(frozen=True)
class Automation(ValueObject):
    source: str
    protocol: str
    port: int
    auth: Authentication
    frequency: ExecutionFrequency
    last_execution: datetime


@dataclass(frozen=True)
class Name(ValueObject):
    name: str
    last_name: str


@dataclass(frozen=True)
class Email(ValueObject):
    address: str
    domain: str
    is_enterprise: bool


