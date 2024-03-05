import pulsar
from pulsar.schema import *
from colorama import Fore, Style

from .schema.v1.events import PropertyCreatedEvent
from .schema.v1.commands import PublishPropertyCommand , PublishPropertyPayload
from ....seedwork.infrastructure import utils


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def publish_created_event(self, event: dict, topic: str):
        integration_event = PropertyCreatedEvent(**event)
        print(Fore.LIGHTMAGENTA_EX + "[Properties & Transactions] Integration Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyCreatedEvent))
