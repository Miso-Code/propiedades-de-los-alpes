from datetime import datetime
from uuid import UUID

from .dto import SagaLogDTO, TransactionDTO
from .mappers import SagaLogMapper, TransactionMapper
from ..domain.entities import SagaLog, Transaction
from ..domain.factories import SagaLogFactory, TransactionFactory
from ..domain.repositories import SagaLogRepository, TransactionRepository
from ..infrastructure.factories import RepositoryFactory
from ....seedwork.domain.services import Service
from ....seedwork.infrastructure.uow import UnitOfWorkPort


class SagaLogService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._saga_log_factory: SagaLogFactory = SagaLogFactory()
        self._transaction_factory: TransactionFactory = TransactionFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def saga_log_factory(self):
        return self._saga_log_factory

    def create_saga_log(self, saga_log_dto: SagaLogDTO) -> SagaLogDTO:
        saga_log: SagaLog = self.saga_log_factory.create_object(saga_log_dto,
                                                                SagaLogMapper())
        repository = self.repository_factory.create_object(SagaLogRepository)

        UnitOfWorkPort.register_batch(repository.add, saga_log)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()

        return self.saga_log_factory.create_object(saga_log, SagaLogMapper())

    def update_saga_log_status(self, saga_log_id: str, status: str) -> SagaLogDTO:
        repository = self.repository_factory.create_object(SagaLogRepository)
        saga_log: SagaLog = repository.get_by_id(UUID(saga_log_id))
        saga_log.status = status

        UnitOfWorkPort.register_batch(repository.update, saga_log)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()

        return self.saga_log_factory.create_object(saga_log, SagaLogMapper())

    def get_saga_logs_by_correlation_id(self, correlation_id: str) -> list[SagaLogDTO]:
        repository = self.repository_factory.create_object(SagaLogRepository)
        saga_logs: list[SagaLog] = repository.get_all()  # this is not efficient, but it's just for mock purposes

        return [self.saga_log_factory.create_object(saga_log, SagaLogMapper()) for saga_log in saga_logs
                if saga_log.correlation_id == correlation_id]


    def get_transaction_by_id(self, transaction_id: str) -> TransactionDTO:
        repository = self.repository_factory.create_object(TransactionRepository)
        transaction: Transaction = repository.get_by_id(UUID(transaction_id))
        return self._transaction_factory.create_object(transaction, TransactionMapper()) if transaction else None

    def get_transaction_by_name(self, name: str) -> TransactionDTO:
        repository = self.repository_factory.create_object(TransactionRepository)

        transactions: list[Transaction] = repository.get_all()  # this is not efficient, but it's just for mock purposes

        transaction = next((x for x in transactions if x.event == name), None)

        return self._transaction_factory.create_object(transaction, TransactionMapper()) if transaction else None

    def get_transaction_by_error_name(self, name: str) -> TransactionDTO:
        repository = self.repository_factory.create_object(TransactionRepository.__class__)

        transactions: list[Transaction] = repository.get_all()

        transaction = next((x for x in transactions if x.error == name), None)

        return self._transaction_factory.create_object(transaction, TransactionMapper()) if transaction else None
