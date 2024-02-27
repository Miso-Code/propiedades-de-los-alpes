from enum import Enum

from ....seedwork.domain.value_objects import ValueObject
from dataclasses import dataclass


@dataclass(frozen=True)
class Country(ValueObject):
    name: str
    code: str


@dataclass(frozen=True)
class City(ValueObject):
    name: str
    code: str
    country: Country


@dataclass(frozen=True)
class Coordinates(ValueObject):
    latitude: float
    longitude: float


@dataclass(frozen=True)
class Location(ValueObject):
    city: City
    address: str
    building: str
    floor: str
    inner_code: str
    coordinates: Coordinates
    additional_info: str


class PropertyIngestionStatus(str, Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    ERROR = 'error'
