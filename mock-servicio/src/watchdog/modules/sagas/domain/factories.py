from dataclasses import dataclass

from .entities import SagaLog, Transaction
from ....seedwork.domain.entities import Entity
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.repositories import Mapper


@dataclass
class SagaLogFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            saga_log: SagaLog = mapper.dto_to_entity(obj)
            return saga_log

@dataclass
class TransactionFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            transaction: Transaction = mapper.dto_to_entity(obj)
            return transaction