from abc import ABC, abstractmethod
from typing import Optional, Any
from .repositories import Mapper
from .mixins import ValidateRulesMixin


class Factory(ABC, ValidateRulesMixin):
    @abstractmethod
    def create_object(self, obj: Any, mapper: Optional[Mapper] = None) -> any:
        ...
