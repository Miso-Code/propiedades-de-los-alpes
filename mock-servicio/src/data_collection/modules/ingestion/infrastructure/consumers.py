import logging
import traceback

import _pulsar
import pulsar
from flask.ctx import AppContext, RequestContext
from pulsar.schema import *

from .schema.v1.commands import CreatePropertyIngestionCommand as CreatePropertyIngestionCommandSchema
from ..application.commands.create_ingestion import CreatePropertyIngestionCommand
from ....seedwork.infrastructure import utils
from ....seedwork.application.commands import execute_command


def subscribe_to_commands(context: AppContext, req_context: RequestContext):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('property-ingestion-commands', consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='propiedades-de-los-alpes-sub-commands',
                                    schema=AvroSchema(CreatePropertyIngestionCommandSchema))

        while True:
            message = consumer.receive()
            print(f'Command received: {message.value().data}')

            data = message.value().data
            command = CreatePropertyIngestionCommand(data)
            with context and req_context:
                execute_command(command)
            consumer.acknowledge(message)

        client.close()
    except Exception:
        logging.error('ERROR: Subscribing to commands topic!')
        traceback.print_exc()
        if client:
            client.close()
