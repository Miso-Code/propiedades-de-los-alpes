import time
import uuid

import pulsar
import _pulsar
from pulsar.schema import *
from colorama import Fore, Back, Style

import os


def time_millis():
    return int(time.time() * 1000)


class IntegrationEvent(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()


class PropertyIngestionCreatedEvent(IntegrationEvent):
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


class PropertyIngestionValidatedEvent(PropertyIngestionCreatedEvent):
    validation_date = String()
    validation_result = String()
    validation_message = String()


HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('property-regulation-events', consumer_type=_pulsar.ConsumerType.Shared,
                            subscription_name='watcher-property-ingestion-events',
                            schema=AvroSchema(PropertyIngestionCreatedEvent))

total_messages = 0
while True:
    msg = consumer.receive()
    print(Back.WHITE, Fore.BLACK)
    print('=========================================')
    print(f'Message received for PropertyIngestionCreated Integration Event: {msg.value()}')
    print('=========================================')
    print(Style.RESET_ALL)
    total_messages += 1
    print(Fore.LIGHTMAGENTA_EX + f'Total messages received: {total_messages}')

    consumer.acknowledge(msg)
client.close()
