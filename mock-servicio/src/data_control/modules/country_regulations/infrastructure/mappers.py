from uuid import UUID

from .dto import CountryRegulationDTO
from ..domain.entities import CountryRegulation
from ..domain.value_objects import Country, CountryRegulationRule, CountryRegulationCondition, \
    CountryRegulationConditionType
from ....seedwork.domain.repositories import Mapper


class CountryRegulationMapper(Mapper):

    def get_type(self) -> type:
        return CountryRegulation.__class__

    def entity_to_dto(self, entity: CountryRegulation) -> list[CountryRegulationDTO]:
        country_regulation_dto = []
        for rule in entity.regulations:
            for condition in rule.conditions:
                country_regulation_dto.append(CountryRegulationDTO(
                    id=str(entity.id)
                    , country_code=entity.country.code
                    , country_name=entity.country.name
                    , fields=','.join(rule.fields)
                    , regulation_condition_type=condition.type.value
                    , regulation_condition_value=condition.value

                ))
        return country_regulation_dto

    def dto_to_entity(self, dto: list[CountryRegulationDTO]) -> CountryRegulation:

        regulations: dict[str, list[CountryRegulationCondition]] = {}
        for entry in dto:
            if entry.fields in regulations:
                regulations[entry.fields].append(CountryRegulationCondition(
                    type=CountryRegulationConditionType(entry.regulation_condition_type)
                    , value=entry.regulation_condition_value
                ))
            else:
                regulations[entry.fields] = [CountryRegulationCondition(
                    type=CountryRegulationConditionType(entry.regulation_condition_type)
                    , value=entry.regulation_condition_value
                )]

        property_ingestion = CountryRegulation(
            # First element of the list would handle the id, this is not a good practice, but it is just for the example
            id=UUID(dto[0].id) if dto[0].id else None
            , country=Country(code=dto[0].country_code, name=dto[0].country_name)
            , regulations=[
                CountryRegulationRule(
                    fields=fields.split(',')
                    , conditions=conditions
                ) for fields, conditions in regulations.items()
            ]
        )
        return property_ingestion
