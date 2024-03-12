import logging
import traceback

import _pulsar
import pulsar
from colorama import Fore, Style
from pulsar.schema import *

from .schema.v1.commands import DisapprovePropertyIngestionCommand as DisapprovePropertyIngestionCommandSchema
from .schema.v1.events import PropertyIngestionCreatedEvent as PropertyIngestionCreatedEventSchema
from ..application.commands.apply_regulation_property_ingestion import ApplyCountryRegulationToPropertyIngestionCommand
from ..application.commands.unapply_regulation_property_ingestion import \
    UnApplyCountryRegulationToPropertyIngestionCommand
from ....seedwork.application.commands import execute_command
from ....seedwork.infrastructure import utils
from ....seedwork.infrastructure.utils import get_topic_name, pulsar_auth


def subscribe_to_events(app=None):
    client = None
    try:
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        consumer = client.subscribe(get_topic_name('property-ingestion-events'),
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='data-control-sub-events',
                                    schema=AvroSchema(PropertyIngestionCreatedEventSchema),
                                    initial_position=pulsar.InitialPosition.Earliest)

        while True:
            message = consumer.receive()
            data: PropertyIngestionCreatedEventSchema = message.value()
            print(Fore.LIGHTYELLOW_EX + '[Country Regulations] Integration Event received: ', data)
            print(Style.RESET_ALL)
            command = ApplyCountryRegulationToPropertyIngestionCommand(
                property_ingestion_id=str(data.property_ingestion_id),
                status=str(data.status),
                agent_id=str(data.agent_id),
                location_city_name=str(data.location_city_name),
                location_city_code=str(data.location_city_code),
                location_country_name=str(data.location_country_name),
                location_country_code=str(data.location_country_code),
                location_address=str(data.location_address),
                location_building=str(data.location_building),
                location_floor=str(data.location_floor),
                location_inner_code=str(data.location_inner_code),
                location_coordinates_latitude=float(data.location_coordinates_latitude),
                location_coordinates_longitude=float(data.location_coordinates_longitude),
                location_additional_info=str(data.location_additional_info),
                property_type=str(data.property_type),
                property_subtype=str(data.property_subtype),
                rooms=int(data.rooms),
                bathrooms=int(data.bathrooms),
                parking_spaces=int(data.parking_spaces),
                construction_area=float(data.construction_area),
                land_area=float(data.land_area),
                price=float(data.price),
                currency=str(data.currency),
                price_per_m2=float(data.price_per_m2),
                price_per_ft2=float(data.price_per_ft2),
                property_url=str(data.property_url),
                property_images=str(data.property_images),
            )
            execute_command(command)
            consumer.acknowledge(message)

        client.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if client:
            client.close()


def subscribe_to_commands():
    client = None
    try:
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        consumer = client.subscribe(get_topic_name('data-control-commands'),
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='data-control-sub-commands',
                                    schema=AvroSchema(DisapprovePropertyIngestionCommandSchema))

        while True:
            message = consumer.receive()
            print(Fore.GREEN + '[Ingestion] Integration Command received: ', message.value().data)
            print(Style.RESET_ALL)

            data = message.value().data
            command = UnApplyCountryRegulationToPropertyIngestionCommand(
                property_ingestion_id=data.property_ingestion_id
            )

            execute_command(command)
            consumer.acknowledge(message)

        client.close()
    except Exception:
        logging.error('[Ingestion] ERROR: Subscribing to commands topic!')
        traceback.print_exc()
        if client:
            client.close()
