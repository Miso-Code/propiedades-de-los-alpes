from pulsar.schema import *

from ......seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class DisapprovePropertyIngestionPayload(IntegrationCommand):
    property_ingestion_id = String()


class DisapprovePropertyIngestionCommand(IntegrationCommand):
    data = DisapprovePropertyIngestionPayload()
