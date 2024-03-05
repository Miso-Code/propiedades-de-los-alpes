from dataclasses import dataclass, field
from .value_objects import Country, CountryRegulationRule
from ....seedwork.domain.entities import RootAggregate
from .events import PropertyIngestionApprovedEvent


@dataclass
class CountryRegulation(RootAggregate):
    country: Country = field(default_factory=Country)
    regulations: list[CountryRegulationRule] = field(default_factory=list)

    def approve_property_ingestion(self, property_ingestion):
        self.add_event(PropertyIngestionApprovedEvent(
            **property_ingestion
        ))
