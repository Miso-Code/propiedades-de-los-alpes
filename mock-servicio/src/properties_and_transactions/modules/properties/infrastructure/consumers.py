import logging
import traceback

import _pulsar
import pulsar
from colorama import Fore, Style
from flask import Flask
from pulsar.schema import *

from .schema.v1.events import PropertyIngestionValidatedEvent
from ..application.commands.register_property import RegisterPropertiesCommand
from ....seedwork.application.commands import execute_command
from ....seedwork.infrastructure import utils
from ....seedwork.infrastructure.utils import get_topic_name, pulsar_auth


def subscribe_to_events(app: Flask = None):
    client = None
    try:
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        consumer = client.subscribe(get_topic_name('property-regulation-events'),
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='propiedades-de-los-alpes-sub-events',
                                    schema=AvroSchema(PropertyIngestionValidatedEvent),
                                    initial_position=pulsar.InitialPosition.Earliest)

        while True:
            with app.app_context() and app.test_request_context():
                message = consumer.receive()
                data: PropertyIngestionValidatedEvent = message.value()
                print(Fore.LIGHTMAGENTA_EX + '[Properties & Transactions] Integration Event received: ', data)
                print(Style.RESET_ALL)
                command = RegisterPropertiesCommand(
                    property_id=str(data.property_ingestion_id),
                    agent_id=str(data.agent_id),
                    property_address=str(data.location_address),
                    property_city=str(data.location_city_name),
                    property_state=str(data.location_country_name),
                    property_zip=str(data.location_inner_code),
                    property_price=int(data.price),
                    property_bedrooms=int(data.rooms),
                    property_bathrooms=int(data.bathrooms),
                    property_square_feet=int(data.construction_area),
                    property_lot_size=int(data.land_area),
                    property_type=str(data.property_type),
                )
                execute_command(command)
                consumer.acknowledge(message)

        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if client:
            client.close()
