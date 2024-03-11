import strawberry
from strawberry.types import Info

from .commands.property_ingestion_commands import CreatePropertyIngestionPayload, \
    CreatePropertyIngestionCommandSchema
from .schemas.property_ingestion import PropertyIngestionInput
from .schemas.response import PropertyIngestionResponse
from ...constants import CommandTopics
from ...dispatchers import Dispatcher


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_property_ingestion(self, data: PropertyIngestionInput, info: Info) -> PropertyIngestionResponse:

        command = CreatePropertyIngestionPayload(
            agent_id=data.agent_id,
            location_city_name=data.location.city.name,
            location_city_code=data.location.city.code,
            location_country_name=data.location.city.country.name,
            location_country_code=data.location.city.country.code,
            location_address=data.location.address,
            location_building=data.location.building,
            location_floor=data.location.floor,
            location_inner_code=data.location.inner_code,
            location_coordinates_latitude=data.location.coordinates.latitude,
            location_coordinates_longitude=data.location.coordinates.longitude,
            location_additional_info=data.location.additional_info,
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
        message = CreatePropertyIngestionCommandSchema(data=command)
        dispatcher = Dispatcher()
        ingestion_command_topic = CommandTopics.CREATE_PROPERTY_INGESTION_COMMAND_TOPIC.value
        info.context["background_tasks"].add_task(dispatcher.publish_message,
                                                  message,
                                                  ingestion_command_topic,)

        return PropertyIngestionResponse(
            message="Property ingestion created successfully",
            code=201
        )
