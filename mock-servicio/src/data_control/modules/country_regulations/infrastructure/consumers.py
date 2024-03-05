import logging
import traceback

import _pulsar
import pulsar
from pulsar.schema import *

from colorama import Fore, Style

from .schema.v1.events import PropertyIngestionCreatedEvent as PropertyIngestionCreatedEventSchema
from ..application.commands.apply_regulation_property_ingestion import ApplyCountryRegulationToPropertyIngestionCommand
from ....seedwork.application.commands import execute_command
from ....seedwork.infrastructure import utils


def subscribe_to_events(app=None):
    client = None
    try:
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumer = client.subscribe('property-ingestion-events', consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='propiedades-de-los-alpes-sub-events',
                                       schema=AvroSchema(PropertyIngestionCreatedEventSchema))

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