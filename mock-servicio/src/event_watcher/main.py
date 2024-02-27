import uuid
from datetime import datetime

import pulsar
import _pulsar
from pulsar.schema import *

import os


class PropertyIngestionCreatedEvent(Record):
    id_property_ingestion = String()
    status = String()
    creation_date = String()


HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('property-ingestion-events', consumer_type=_pulsar.ConsumerType.Shared,
                            subscription_name='watcher-property-ingestion-events',
                            schema=AvroSchema(PropertyIngestionCreatedEvent))

while True:
    msg = consumer.receive()
    print('=========================================')
    print(f'Message received for PropertyIngestionCreated Integration Event: {msg.value()}')
    print('=========================================')

    consumer.acknowledge(msg)
client.close()
