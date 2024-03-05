import logging
import traceback

import _pulsar
import pulsar
import aiopulsar
from flask import Flask
from pulsar.schema import *

from colorama import Fore, Style

from .schema.v1.events import PropertyCreatedEvent
from .utils import broker_host, obtener_schema_avro_de_diccionario


async def subscribe_to_topic(topic: str, subscription: str, schema: str,
                             consumer_type: _pulsar.ConsumerType = _pulsar.ConsumerType.Shared, events={}):
    try:
        # json_schema = consultar_schema_registry(schema)
        # avro_schema = obtener_schema_avro_de_diccionario(json_schema)
        avro_schema = AvroSchema(PropertyCreatedEvent)
        async with aiopulsar.connect(f'pulsar://{broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                    topic,
                    consumer_type=consumer_type,
                    subscription_name=subscription,
                    schema=avro_schema
            ) as consumer:
                while True:
                    message = await consumer.receive()
                    print(message)
                    data = message.value()
                    if data.agent_id:
                        if not events.get(data.agent_id):
                            events[data.agent_id] = list()
                        events[data.agent_id].append(str(data))
                    print(Fore.LIGHTBLUE_EX,f'[BFF WS] Integration Event received:  {data}', Style.RESET_ALL)
                    # events.append(str(datos))
                    await consumer.acknowledge(message)

    except:
        logging.error(Fore.RED,f'ERROR: {Fore.LIGHTBLUE_EX} Suscribiendose al tópico! {topic}, {subscription}, {schema}', Style.RESET_ALL)
        traceback.print_exc()
