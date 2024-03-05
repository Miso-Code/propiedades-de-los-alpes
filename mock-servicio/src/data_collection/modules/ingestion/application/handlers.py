from .services import PropertyIngestionService
from ..domain.events import PropertyIngestionStartedEvent
from ..application.mappers import PropertyIngestionMapper
from ....seedwork.application.handlers import Handler
from ..infrastructure.dispatchers import Dispatcher


class HandlerPropertyIngestionDomain(Handler):

    @staticmethod
    def handle_property_ingestion_started(event: PropertyIngestionStartedEvent):
        dispatcher = Dispatcher()

        # Instead of sending a delta event, we submit a stateful event
        property_ingestion = PropertyIngestionService().get_ingestion_by_id(event.property_ingestion_id)

        property_ingestion_dto = PropertyIngestionMapper().entity_to_dto(property_ingestion)

        stateful_event = {
            "property_ingestion_id": event.property_ingestion_id,
            "agent_id": event.agent_id,
            "status": event.status,
            "started_at": event.started_at,
            **property_ingestion_dto.__dict__  # This is not a good practice, but it is a quick fix
        }

        dispatcher.publish_created_event(stateful_event, 'property-ingestion-events')
