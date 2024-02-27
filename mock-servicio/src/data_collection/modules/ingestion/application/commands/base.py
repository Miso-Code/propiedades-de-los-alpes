from ...domain.factories import PropertyIngestionFactory
from ...infrastructure.factories import RepositoryFactory
from .....seedwork.application.commands import CommandHandler


class CreateIngestionBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._property_ingestion_factory: PropertyIngestionFactory = PropertyIngestionFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def property_ingestion_factory(self):
        return self._property_ingestion_factory
