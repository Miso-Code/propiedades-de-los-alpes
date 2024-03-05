from uuid import UUID

from .dto import CountryRegulationDTO
from .mappers import CountryRegulationMapper
from ..domain.factories import CountryRegulationFactory
from ....config.db import db
from ..domain.entities import CountryRegulation
from ..domain.repositories import CountryRegulationRepository


class SQLAlchemyCountryRegulationRepository(CountryRegulationRepository):

    def __init__(self):
        self._property_country_regulations_factory: CountryRegulationFactory = CountryRegulationFactory()

    @property
    def property_country_regulations_factory(self) -> CountryRegulationFactory:
        return self._property_country_regulations_factory

    def get_by_country_code(self, country_code: str) -> CountryRegulation:
        property_country_regulations_dto = db.query(CountryRegulationDTO).filter_by(country_code=country_code).all()
        return self.property_country_regulations_factory.create_object(property_country_regulations_dto,
                                                                       CountryRegulationMapper()) if property_country_regulations_dto else None

    def get_by_id(self, id: UUID) -> CountryRegulation:
        raise NotImplementedError

    def get_all(self) -> list[CountryRegulation]:
        raise NotImplementedError

    def add(self, entity: CountryRegulation):
        property_country_regulations_dto = CountryRegulationFactory().create_object(entity, CountryRegulationMapper())
        db.session.add(property_country_regulations_dto)
        db.session.commit()
        db.session.refresh(property_country_regulations_dto)

    def update(self, entity: CountryRegulation):
        # TODO
        raise NotImplementedError

    def delete(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
