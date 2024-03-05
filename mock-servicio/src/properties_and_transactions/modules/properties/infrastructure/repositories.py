from uuid import UUID

from ....config.db import db

from .dto import PropertyDTO

from .mappers import PropertyMapper

from ..domain.factories import PropertyFactory
from ..domain.repositories import PropertyPropertiesRepository
from ..domain.entities import Property


class SQLAlchemyPropertyPropertiesRepository(PropertyPropertiesRepository):

    def __init__(self):
        self._property_properties_factory: PropertyFactory = PropertyFactory()

    @property
    def property_properties_factory(self) -> PropertyFactory:
        return self._property_properties_factory

    def get_by_id(self, id: UUID) -> Property:
        # TODO
        raise NotImplementedError

    def get_all(self) -> list[Property]:
        try:
            all_properties_db = db.session.query(PropertyDTO).all()
            property_properties_mapper = PropertyMapper()

            return [property_properties_mapper.dto_to_entity(property) for property in all_properties_db]
        except Exception as e:
            print(e)
            return []

    def update(self, entity: Property):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError

    def add(self, entity: Property):
        property_dto = PropertyFactory().create_object(entity, PropertyMapper())
        db.session.add(property_dto)
        db.session.commit()
        db.session.refresh(property_dto)
