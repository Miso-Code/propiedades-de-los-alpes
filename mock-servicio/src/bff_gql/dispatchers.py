import pulsar
from pulsar.schema import AvroSchema

from . import utils
from .api.v1.commands.property_ingestion_commands import CreatePropertyIngestionCommandSchema
from .utils import get_topic_name, pulsar_auth


class Dispatcher:
    def __init__(self):
        ...

    async def publish_message(self, message, topic):
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        producer = client.create_producer(get_topic_name(topic),
                                          schema=AvroSchema(CreatePropertyIngestionCommandSchema))
        producer.send(message)
        client.close()
