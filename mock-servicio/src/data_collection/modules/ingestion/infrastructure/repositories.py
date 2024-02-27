from uuid import UUID

from .dto import PropertyIngestionDTO
from .mappers import PropertyIngestionMapper
from ..domain.factories import PropertyIngestionFactory
from ....config.db import db
from ..domain.entities import PropertyIngestion
from ..domain.repositories import PropertyIngestionRepository


class SQLAlchemyPropertyIngestionRepository(PropertyIngestionRepository):

    def __init__(self):
        self._property_ingestion_factory: PropertyIngestionFactory = PropertyIngestionFactory()

    @property
    def property_ingestion_factory(self) -> PropertyIngestionFactory:
        return self._property_ingestion_factory

    def get_by_id(self, id: UUID) -> PropertyIngestion:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[PropertyIngestion]:
        all_ingestions_db = db.session.query(PropertyIngestionDTO).all()
        mapper = PropertyIngestionMapper()
        all_ingestions: list[PropertyIngestion] = [
            PropertyIngestionFactory().create_object(ingestion, mapper) for ingestion in all_ingestions_db
        ]

        return all_ingestions

    def add(self, entity: PropertyIngestion):
        property_ingestion_dto = PropertyIngestionFactory().create_object(entity, PropertyIngestionMapper())
        db.session.add(property_ingestion_dto)
        db.session.commit()
        db.session.refresh(property_ingestion_dto)

    def update(self, entity: PropertyIngestion):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
