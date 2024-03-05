from dataclasses import dataclass

from .repositories import SQLAlchemyPropertyPropertiesRepository
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.repositories import Repository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        return SQLAlchemyPropertyPropertiesRepository()
