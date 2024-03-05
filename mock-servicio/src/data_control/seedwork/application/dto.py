from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass(frozen=True)
class DTO:
    ...

class Mapper(ABC):
    @abstractmethod
    def external_to_dto(self, external: any) -> DTO:
        ...

    @abstractmethod
    def dto_to_external(self, dto: DTO) -> any:
        ...
