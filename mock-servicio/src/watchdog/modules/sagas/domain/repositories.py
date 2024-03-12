from abc import ABC

from ....seedwork.domain.repositories import Repository


class SagaLogRepository(Repository, ABC):
    ...

class TransactionRepository(Repository, ABC):
    ...