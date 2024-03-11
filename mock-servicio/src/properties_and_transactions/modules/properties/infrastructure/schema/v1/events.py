from pulsar.schema import *
from ......seedwork.infrastructure.schema.v1.events import IntegrationEvent    


class PropertyIngestionValidatedEvent(IntegrationEvent):
    property_ingestion_id = String()
    status = String()
    creation_date = String()
    agent_id = String()
    location_city_name = String()
    location_city_code = String()
    location_country_name = String()
    location_country_code = String()
    location_address = String()
    location_building = String()
    location_floor = String()
    location_inner_code = String()
    location_coordinates_latitude = Float()
    location_coordinates_longitude = Float()
    location_additional_info = String()
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
    validation_date = String()
    validation_result = String()
    validation_message = String()


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

class PropertyNotCreatedEvent(IntegrationEvent):
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