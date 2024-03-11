import pulsar
from colorama import Fore, Style
from pulsar.schema import *

from .schema.v1.events import PropertyCreatedEvent, PropertyNotCreatedEvent
from ....seedwork.infrastructure import utils
from ....seedwork.infrastructure.utils import get_topic_name, pulsar_auth


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        producer = client.create_producer(get_topic_name(topic), schema=schema)
        producer.send(message)
        client.close()

    def publish_created_event(self, event: dict, topic: str):
        integration_event = PropertyCreatedEvent(**event)
        print(Fore.LIGHTMAGENTA_EX + "[Properties & Transactions] Integration Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyCreatedEvent))

    def publish_not_created_event(self, event: dict, topic: str):
        rollback_event = PropertyNotCreatedEvent(**event)
        print(Fore.LIGHTMAGENTA_EX + "[Properties & Transactions] Integration Rollback Event published: ",
              rollback_event)
        print(Style.RESET_ALL)
        self._publish_message(rollback_event, topic, AvroSchema(PropertyNotCreatedEvent))
