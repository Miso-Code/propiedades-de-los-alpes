import pulsar
from pulsar.schema import *
from colorama import Fore, Back, Style

import datetime

from .schema.v1.events import PropertyIngestionCreatedEvent
from .schema.v1.commands import CreatePropertyIngestionCommand, CreatePropertyIngestionPayload
from ....seedwork.infrastructure import utils


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        producer = client.create_producer(topic, schema=schema)
        producer.send(message)
        client.close()

    def publish_created_event(self, event: dict, topic: str):
        integration_event = PropertyIngestionCreatedEvent(**event)
        print(Fore.GREEN + "[Ingestion] Integration Event published: ", integration_event)
        print(Style.RESET_ALL)
        self._publish_message(integration_event, topic, AvroSchema(PropertyIngestionCreatedEvent))

    def publish_command(self, command, topic: str):
        payload = CreatePropertyIngestionPayload(
            agent_id=str(command.agent_id),
            location_city_name=str(command.location_city_name),
            location_city_code=str(command.location_city_code),
            location_country_name=str(command.location_country_name),
            location_country_code=str(command.location_country_code),
            location_address=str(command.location_address),
            location_building=str(command.location_building),
            location_floor=str(command.location_floor),
            location_inner_code=str(command.location_inner_code),
            location_coordinates_latitude=float(command.location_coordinates_latitude),
            location_coordinates_longitude=float(command.location_coordinates_longitude),
            location_additional_info=str(command.location_additional_info),
            property_type=str(command.property_type),
            property_subtype=str(command.property_subtype),
            rooms=int(command.rooms),
            bathrooms=int(command.bathrooms),
            parking_spaces=int(command.parking_spaces),
            construction_area=float(command.construction_area),
            land_area=float(command.land_area),
            price=float(command.price),
            currency=str(command.currency),
            price_per_m2=float(command.price_per_m2),
            price_per_ft2=float(command.price_per_ft2),
            property_url=str(command.property_url),
            property_images=str(command.property_images),
        )

        integration_command = CreatePropertyIngestionCommand(data=payload)
        print(Fore.GREEN + "[Ingestion] Integration Command published: ", integration_command)
        print(Style.RESET_ALL)
        self._publish_message(integration_command, topic, AvroSchema(CreatePropertyIngestionCommand))
