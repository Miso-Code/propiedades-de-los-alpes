import uuid

from pulsar.schema import *

from ...utils import time_millis


class Message(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()


class IntegrationEvent(Message):
    ...


class PropertyCreatedEvent(IntegrationEvent):
    agent_id = String()
    property_id = String()
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
