import logging
import traceback

import _pulsar
import pulsar
from flask import Flask
from pulsar.schema import *

from colorama import Fore, Style

from .schema.v1.events import PropertyIngestionValidatedEvent
from ..application.commands.register_property import RegisterPropertiesCommand
from ....seedwork.application.commands import execute_command
from ....seedwork.infrastructure import utils


def subscribe_to_events(app: Flask =None):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('property-regulation-events', 
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='propiedades-de-los-alpes-sub-events',
                                    schema=AvroSchema(PropertyIngestionValidatedEvent))
                  
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