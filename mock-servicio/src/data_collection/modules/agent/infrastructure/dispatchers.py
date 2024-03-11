import pulsar
from colorama import Fore, Style
from pulsar.schema import *

import datetime

from ...ingestion.infrastructure.schema.v1.commands import CreatePropertyIngestionCommand, \
    CreatePropertyIngestionPayload
from ....seedwork.infrastructure import utils
from ....seedwork.infrastructure.utils import get_topic_name, pulsar_auth

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Dispatcher:
    def _publish_message(self, message, topic, schema):
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        producer = client.create_producer(get_topic_name(topic), schema=schema)
        producer.send(message)
        client.close()

    def publish_command(self, command, topic):
        payload = CreatePropertyIngestionPayload(
            agent_id=str(command["agent_id"]),
            location_city_name=str(command["location"]["city"]["name"]),
            location_city_code=str(command["location"]["city"]["code"]),
            location_country_name=str(command["location"]["city"]["country"]["name"]),
            location_country_code=str(command["location"]["city"]["country"]["code"]),
            location_address=str(command["location"]["address"]),
            location_building=str(command["location"]["building"]),
            location_floor=str(command["location"]["floor"]),
            location_inner_code=str(command["location"]["inner_code"]),
            location_coordinates_latitude=float(command["location"]["coordinates"]["latitude"]),
            location_coordinates_longitude=float(command["location"]["coordinates"]["longitude"]),
            location_additional_info=str(command["location"]["additional_info"]),
            property_type=str(command["property_type"]),
            property_subtype=str(command["property_subtype"]),
            rooms=int(command["rooms"]),
            bathrooms=int(command["bathrooms"]),
            parking_spaces=int(command["parking_spaces"]),
            construction_area=float(command["construction_area"]),
            land_area=float(command["land_area"]),
            price=float(command["price"]),
            currency=str(command["currency"]),
            price_per_m2=float(command["price_per_m2"]),
            price_per_ft2=float(command["price_per_ft2"]),
            property_url=str(command["property_url"]),
            property_images=str(command["property_images"]),
        )

        integration_command = CreatePropertyIngestionCommand(data=payload)
        print(Fore.CYAN, f"[Agent] Command Published: {payload}", Style.RESET_ALL)
        self._publish_message(integration_command, topic, AvroSchema(CreatePropertyIngestionCommand))
