from abc import ABC, abstractmethod

from src.data_collection.seedwork.domain.entities import Entity
from ....seedwork.domain.repositories import Repository


class CountryRegulationRepository(Repository, ABC):
    @abstractmethod
    def get_by_country_code(self, code: str) -> Entity:
        ...
