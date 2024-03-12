from uuid import UUID

from .dto import SagaLogDTO, TransactionDTO
from .mappers import SagaLogMapper, TransactionMapper
from ..domain.factories import SagaLogFactory, TransactionFactory
from ....config.db import db
from ..domain.entities import SagaLog
from ..domain.repositories import SagaLogRepository, TransactionRepository


class SQLAlchemySagaLogRepository(SagaLogRepository):

    def __init__(self):
        self._saga_log_factory: SagaLogFactory = SagaLogFactory()

    @property
    def saga_log_factory(self) -> SagaLogFactory:
        return self._saga_log_factory

    def get_by_id(self, id: UUID) -> SagaLog:
        saga_log_db = db.query(SagaLogDTO).filter_by(id=str(id)).first()
        saga_log_mapper = SagaLogMapper()
        saga_log: SagaLog = SagaLogFactory().create_object(saga_log_db, saga_log_mapper)
        return saga_log

    def get_all(self) -> list[SagaLog]:
        all_saga_logs_db = db.query(SagaLogDTO).all()
        saga_log_mapper = SagaLogMapper()

        all_saga_logs: list[SagaLog] = [
            SagaLogFactory().create_object(saga_log, saga_log_mapper) for saga_log in
            all_saga_logs_db
        ]

        return all_saga_logs

    def add(self, entity: SagaLog):
        saga_log_dto = SagaLogFactory().create_object(entity, SagaLogMapper())
        db.add(saga_log_dto)
        db.commit()
        db.refresh(saga_log_dto)

    def update(self, entity: SagaLog):
        saga_log_dto = SagaLogFactory().create_object(entity, SagaLogMapper())
        db.query(SagaLogDTO).filter_by(id=str(entity.id)).update({
            "status": entity.status,
            "correlation_id": entity.correlation_id,
            "transaction_id": entity.transaction_id
        })
        db.commit()

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class SQLAlchemyTransactionRepository(TransactionRepository):

    def __init__(self):
        self._transaction_factory: TransactionFactory = TransactionFactory()

    @property
    def transaction_factory(self) -> TransactionFactory:
        return self._transaction_factory

    def get_by_id(self, id: UUID) -> SagaLog:
        transaction_db = db.query(TransactionDTO).filter_by(id=str(id)).first()
        transaction_mapper = TransactionMapper()
        transaction: SagaLog = TransactionFactory().create_object(transaction_db, transaction_mapper)
        return transaction

    def get_all(self) -> list[SagaLog]:
        all_transactions_db = db.query(TransactionDTO).all()
        transaction_mapper = TransactionMapper()

        all_transactions: list[SagaLog] = [
            TransactionFactory().create_object(transaction, transaction_mapper) for transaction in
            all_transactions_db
        ]

        return all_transactions

    def add(self, entity: SagaLog):
        transaction_dto = TransactionFactory().create_object(entity, TransactionMapper())
        db.add(transaction_dto)
        db.commit()
        db.refresh(transaction_dto)

    def update(self, entity: SagaLog):
        transaction_dto = TransactionFactory().create_object(entity, TransactionMapper())
        db.query(TransactionDTO).filter_by(id=str(entity.id)).update(transaction_dto)
        db.commit()

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
