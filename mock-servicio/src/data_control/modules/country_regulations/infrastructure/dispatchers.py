import pulsar
from colorama import Fore, Style
from pulsar.schema import *

from .schema.v1.events import PropertyIngestionValidatedEvent, PropertyIngestionRejectedEvent
from ....seedwork.infrastructure import utils
from ....seedwork.infrastructure.utils import get_topic_name, pulsar_auth


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        producer = client.create_producer(get_topic_name(topic), schema=schema)
        producer.send(message)
        client.close()

    def publish_validated_event(self, event: dict, topic: str):
        integration_event = PropertyIngestionValidatedEvent(**event)
        print(Fore.LIGHTYELLOW_EX + "[Ingestion] Integration Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyIngestionValidatedEvent))

    def publish_rejected_event(self, event: dict, topic: str):
        integration_event = PropertyIngestionRejectedEvent(**event)
        print(Fore.LIGHTYELLOW_EX + "[Ingestion] Integration Rollback Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyIngestionRejectedEvent))
