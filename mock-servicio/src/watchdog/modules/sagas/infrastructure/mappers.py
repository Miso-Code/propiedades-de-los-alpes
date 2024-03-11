from uuid import UUID

from .dto import SagaLogDTO, TransactionDTO
from ..domain.entities import SagaLog, Transaction
from ....seedwork.domain.repositories import Mapper


class SagaLogMapper(Mapper):

    def get_type(self) -> type:
        return SagaLog.__class__

    def entity_to_dto(self, entity: SagaLog) -> SagaLogDTO:
        saga_log_dto = SagaLogDTO()
        saga_log_dto.id = str(entity.id)
        saga_log_dto.correlation_id = entity.correlation_id
        saga_log_dto.status = entity.status
        saga_log_dto.transaction_id = entity.transaction_id
        return saga_log_dto

    def dto_to_entity(self, dto: SagaLogDTO) -> SagaLog:
        saga_log = SagaLog(
            id=UUID(dto.id)
            , correlation_id=dto.correlation_id
            , status=dto.status
            , transaction_id=dto.transaction_id
        )
        return saga_log


class TransactionMapper(Mapper):

    def get_type(self) -> type:
        return Transaction.__class__

    def entity_to_dto(self, entity: Transaction) -> TransactionDTO:
        transaction_dto = TransactionDTO()
        transaction_dto.id = str(entity.id)
        transaction_dto.event = entity.event
        transaction_dto.error = entity.error
        transaction_dto.compensation = entity.compensation
        transaction_dto.order = entity.order
        transaction_dto.is_last = entity.is_last
        transaction_dto.compensation_topic = entity.compensation_topic
        return transaction_dto

    def dto_to_entity(self, dto: TransactionDTO) -> Transaction:
        transaction = Transaction(
            id=UUID(dto.id)
            , event=dto.event
            , error=dto.error
            , compensation=dto.compensation
            , order=dto.order
            , is_last=dto.is_last
            , compensation_topic=dto.compensation_topic
        )
        return transaction
