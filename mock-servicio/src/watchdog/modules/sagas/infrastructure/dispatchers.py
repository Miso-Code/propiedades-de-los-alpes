import pulsar
from colorama import Fore, Style
from pulsar.schema import *

from .schema.v1.commands import DeletePropertyIngestionPayload, DeletePropertyIngestionCommand, \
    DisapprovePropertyIngestionPayload, DisapprovePropertyIngestionCommand
from .schema.v1.events import PropertyIngestionRejectedEvent
from ....seedwork.infrastructure.utils import broker_host, get_topic_name, pulsar_auth

compensation_schemas = {
    "PropertyIngestionRejectedEvent": PropertyIngestionRejectedEvent,
    "DeletePropertyIngestionCommand": [DeletePropertyIngestionPayload, DeletePropertyIngestionCommand],
    "DisapprovePropertyIngestionCommand": [DisapprovePropertyIngestionPayload, DisapprovePropertyIngestionCommand]
}


class Dispatcher:
    def _schema_name_to_instance(self, class_name, data):
        schema_class = compensation_schemas[class_name]
        # check if data has a key called data
        if "data" in data and isinstance(schema_class, list):
            payload_class = schema_class[0]
            command_class = schema_class[1]
            payload = payload_class(**data["data"])
            return command_class(data=payload)
        else:
            return schema_class(data)

    def _schema_name_to_class(self, class_name):
        schema_class = compensation_schemas[class_name]
        if isinstance(schema_class, list):
            return schema_class[1]
        else:
            return schema_class

    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(broker_host(), authentication=pulsar_auth())
        producer = client.create_producer(get_topic_name(topic), schema=schema)
        producer.send(message)
        client.close()

    def publish_compensation_to_topic(self, payload: dict, schema: str, topic: str):
        body = self._schema_name_to_instance(schema, payload)

        if not body:
            print(Fore.LIGHTRED_EX + f"[Watchdog Saga] No schema found for {schema}", Style.RESET_ALL)
            return

        print(
            Fore.LIGHTYELLOW_EX + f"[Watchdog Saga] Publishing compensation {body.__class__.__name__} event to {topic}",
            Style.RESET_ALL)
        self._publish_message(body, topic, AvroSchema(self._schema_name_to_class(schema)))
