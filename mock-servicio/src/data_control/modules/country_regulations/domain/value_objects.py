from dataclasses import dataclass
from enum import Enum
from typing import Any

from src.data_control.seedwork.domain.value_objects import ValueObject


class CountryRegulationOnFail(Enum):
    CANCEL = 1
    FIX = 2
    REMOVE = 3


class CountryRegulationConditionType(Enum):
    EQUALS = 1
    NOT_EQUALS = 2
    GREATER_THAN = 3
    LESS_THAN = 4
    GREATER_THAN_OR_EQUALS = 5
    LESS_THAN_OR_EQUALS = 6
    IN = 7
    NOT_IN = 8
    BETWEEN = 9
    NOT_BETWEEN = 10
    LIKE = 11
    NOT_LIKE = 12
    IS_NULL = 13
    IS_NOT_NULL = 14
    IS_EMPTY = 15
    IS_NOT_EMPTY = 16


@dataclass(frozen=True)
class CountryRegulationCondition(ValueObject):
    type: CountryRegulationConditionType
    value: Any
    pass


@dataclass(frozen=True)
class CountryRegulationRule(ValueObject):
    fields: list[str]
    conditions: list[CountryRegulationCondition]


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
