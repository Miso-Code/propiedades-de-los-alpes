import pulsar
from pulsar.schema import *

import datetime

from ...ingestion.infrastructure.schema.v1.commands import CreatePropertyIngestionCommand, \
    CreatePropertyIngestionPayload
from ....seedwork.infrastructure import utils

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def publish_command(self, command, topic):
        payload = CreatePropertyIngestionPayload(
            agent_id=str(command['agent_id']),
            location=str(command['location']),
            property_type=str(command['property_type']),
            property_subtype=str(command['property_subtype']),
            rooms=int(command['rooms']),
            bathrooms=int(command['bathrooms']),
            parking_spaces=int(command['parking_spaces']),
            construction_area=float(command['construction_area']),
            land_area=float(command['land_area']),
            price=float(command['price']),
            currency=str(command['currency']),
            price_per_m2=float(command['price_per_m2']),
            price_per_ft2=float(command['price_per_ft2']),
            property_url=str(command['property_url']),
            property_images=str(command['property_images']),
        )

        integration_command = CreatePropertyIngestionCommand(data=payload)
        self._publish_message(integration_command, topic, AvroSchema(CreatePropertyIngestionCommand))
