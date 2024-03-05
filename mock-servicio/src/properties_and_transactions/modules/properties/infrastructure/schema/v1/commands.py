from pulsar.schema import *

from ......seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class PublishPropertyPayload(IntegrationCommand):
    property_id = String()
    agent_id = String()
    property_address = String()
    property_city = String()
    property_state = String()
    property_zip = String()
    property_price = Float()
    property_bedrooms = Integer()
    property_bathrooms = Integer()
    property_square_feet = Integer()
    property_lot_size = Integer()
    property_type = String()


class PublishPropertyCommand(IntegrationCommand):
    data = PublishPropertyPayload()
