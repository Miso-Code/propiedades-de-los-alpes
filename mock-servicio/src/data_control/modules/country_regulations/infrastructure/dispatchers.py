import pulsar
from pulsar.schema import *
from colorama import Fore, Style

import datetime

from .schema.v1.events import PropertyIngestionValidatedEvent
from ....seedwork.infrastructure import utils


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def publish_validated_event(self, event: dict, topic: str):
        integration_event = PropertyIngestionValidatedEvent(**event)
        print(Fore.LIGHTYELLOW_EX + "[Ingestion] Integration Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyIngestionValidatedEvent))
