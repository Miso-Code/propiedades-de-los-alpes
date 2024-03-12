from ..config.db import db
from ..seedwork.infrastructure.uow import UnitOfWork, Batch


class AgnosticUnitOfWork(UnitOfWork):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnitOfWork:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _clear_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return list[db.get_nested_transaction()]

    @property
    def batches(self) -> list[Batch]:
        return self._batches

    def commit(self):

        for batch in self.batches:
            lock = batch.lock
            batch.operation(*batch.args, **batch.kwargs)

        db.commit()

        super().commit()

    def rollback(self, savepoint=None):
        if savepoint:
            savepoint.rollback()
        else:
            db.rollback()

        super().rollback()

    def savepoint(self):
        db.begin_nested()
