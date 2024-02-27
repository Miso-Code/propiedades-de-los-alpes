from .dto import PropertyIngestionDTO
from .mappers import PropertyIngestionMapper
from ..domain.entities import PropertyIngestion
from ..domain.factories import PropertyIngestionFactory
from ..domain.repositories import PropertyIngestionRepository
from ..infrastructure.factories import RepositoryFactory
from ....seedwork.domain.services import Service
from ....seedwork.infrastructure.uow import UnitOfWorkPort


class PropertyIngestionService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._property_ingestion_factory: PropertyIngestionFactory = PropertyIngestionFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def property_ingestion_factory(self):
        return self._property_ingestion_factory

    def create_property_ingestion(self, ingestion_dto: PropertyIngestionDTO) -> PropertyIngestionDTO:
        property_ingestion: PropertyIngestion = self.property_ingestion_factory.create_object(ingestion_dto,
                                                                                              PropertyIngestionMapper())
        repository = self.repository_factory.create_object(PropertyIngestionRepository.__class__)

        UnitOfWorkPort.register_batch(repository.add, property_ingestion)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()

        return self.property_ingestion_factory.create_object(property_ingestion, PropertyIngestionMapper())

    def get_all_ingestions(self) -> list[PropertyIngestion]:
        repository = self.repository_factory.create_object(PropertyIngestionRepository.__class__)
        ingestions: list[PropertyIngestion] = repository.get_all()
        return ingestions

