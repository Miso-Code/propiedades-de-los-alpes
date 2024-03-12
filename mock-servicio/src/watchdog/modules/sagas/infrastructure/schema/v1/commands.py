from pulsar.schema import *

from src.watchdog.seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class DeletePropertyIngestionPayload(IntegrationCommand):
    property_ingestion_id = String()


class DeletePropertyIngestionCommand(IntegrationCommand):
    data = DeletePropertyIngestionPayload()


class DisapprovePropertyIngestionPayload(IntegrationCommand):
    property_ingestion_id = String()


class DisapprovePropertyIngestionCommand(IntegrationCommand):
    data = DisapprovePropertyIngestionPayload()
