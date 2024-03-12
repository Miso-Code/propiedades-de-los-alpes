from uuid import UUID

from ..application.dto import SagaLogDTO, TransactionDTO
from ..domain.entities import SagaLog, Transaction
from ....seedwork.application.dto import Mapper as AppMapper
from ....seedwork.domain.repositories import Mapper as RepoMapper


class SagaLogDTOJsonMapper(AppMapper):

    def dto_to_external(self, dto: SagaLogDTO) -> dict:
        return dto.__dict__

    def external_to_dto(self, external: dict) -> SagaLogDTO:
        saga_log_dto = SagaLogDTO(
            id=external.get('id')
            , correlation_id=external.get('correlation_id')
            , status=external.get('status')
            , transaction_id=external.get('transaction_id')
        )
        return saga_log_dto


class SagaLogMapper(RepoMapper):

    def get_type(self) -> type:
        return SagaLog.__class__

    def entity_to_dto(self, entity: SagaLog) -> SagaLogDTO:
        saga_log_dto = SagaLogDTO(
            id=str(entity.id) if entity.id else None
            , correlation_id=entity.correlation_id
            , status=entity.status
            , transaction_id=entity.transaction_id
        )
        return saga_log_dto

    def dto_to_entity(self, dto: SagaLogDTO) -> SagaLog:
        saga_log = SagaLog(
            id=UUID(dto.id) if dto.id else None
            , correlation_id=dto.correlation_id
            , status=dto.status
            , transaction_id=dto.transaction_id
        )
        return saga_log


class TransactionMapper(RepoMapper):

    def get_type(self) -> type:
        return Transaction.__class__

    def entity_to_dto(self, entity: Transaction) -> TransactionDTO:
        transaction_dto = TransactionDTO(
            id=str(entity.id)
            , event=entity.event
            , error=entity.error
            , compensation=entity.compensation
            , order=entity.order
            , is_last=entity.is_last
            , compensation_topic=entity.compensation_topic
        )
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
