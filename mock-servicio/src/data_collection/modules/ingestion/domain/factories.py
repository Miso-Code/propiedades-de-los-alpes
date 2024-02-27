from dataclasses import dataclass

from .entities import PropertyIngestion
from ....seedwork.domain.entities import Entity
from ....seedwork.domain.factories import Factory
from ....seedwork.domain.repositories import Mapper


@dataclass
class PropertyIngestionFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            property_ingestion: PropertyIngestion = mapper.dto_to_entity(obj)
            return property_ingestion
