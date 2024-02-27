from pulsar.schema import *

from ......seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class CreatePropertyIngestionPayload(IntegrationCommand):
    agent_id = String()
    location = String()
    property_type = String()
    property_subtype = String()
    rooms = Integer()
    bathrooms = Integer()
    parking_spaces = Integer()
    construction_area = Float()
    land_area = Float()
    price = Float()
    currency = String()
    price_per_m2 = Float()
    price_per_ft2 = Float()
    property_url = String()
    property_images = String()


class CreatePropertyIngestionCommand(IntegrationCommand):
    data = CreatePropertyIngestionPayload()
