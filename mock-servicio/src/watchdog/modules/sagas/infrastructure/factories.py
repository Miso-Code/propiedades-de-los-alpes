from dataclasses import dataclass

from .repositories import SQLAlchemySagaLogRepository, SQLAlchemyTransactionRepository
from ..domain.repositories import SagaLogRepository
from ....seedwork.domain.exceptions import FactoryException
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.repositories import Repository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == SagaLogRepository:
            return SQLAlchemySagaLogRepository()
        return SQLAlchemyTransactionRepository()
