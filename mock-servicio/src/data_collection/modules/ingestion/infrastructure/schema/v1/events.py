from pulsar.schema import *
from ......seedwork.infrastructure.schema.v1.events import IntegrationEvent


class PropertyIngestionCreatedEvent(IntegrationEvent):
    id_property_ingestion = String()
    status = String()
    creation_date = String()
