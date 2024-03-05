import logging
import traceback

import _pulsar
import pulsar
from flask.ctx import AppContext, RequestContext
from pulsar.schema import *
from colorama import Fore, Style

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
            print(Fore.GREEN + '[Ingestion] Integration Command received: ', message.value().data)
            print(Style.RESET_ALL)

            data = message.value().data
            command = CreatePropertyIngestionCommand(
                agent_id=data.agent_id,
                location_city_name=data.location_city_name,
                location_city_code=data.location_city_code,
                location_country_name=data.location_country_name,
                location_country_code=data.location_country_code,
                location_address=data.location_address,
                location_building=data.location_building,
                location_floor=data.location_floor,
                location_inner_code=data.location_inner_code,
                location_coordinates_latitude=data.location_coordinates_latitude,
                location_coordinates_longitude=data.location_coordinates_longitude,
                location_additional_info=data.location_additional_info,
                property_type=data.property_type,
                property_subtype=data.property_subtype,
                rooms=data.rooms,
                bathrooms=data.bathrooms,
                parking_spaces=data.parking_spaces,
                construction_area=data.construction_area,
                land_area=data.land_area,
                price=data.price,
                currency=data.currency,
                price_per_m2=data.price_per_m2,
                price_per_ft2=data.price_per_ft2,
                property_url=data.property_url,
                property_images=data.property_images
            )
            with context and req_context:
                execute_command(command)
            consumer.acknowledge(message)

        client.close()
    except Exception:
        logging.error('[Ingestion] ERROR: Subscribing to commands topic!')
        traceback.print_exc()
        if client:
            client.close()
