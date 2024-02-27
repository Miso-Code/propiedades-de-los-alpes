from ....seedwork.application.handlers import Handler
from ..infrastructure.dispatchers import Dispatcher


class HandlerPropertyIngestionDomain(Handler):

    @staticmethod
    def handle_property_ingestion_started(event):
        dispatcher = Dispatcher()
        dispatcher.publish_created_event(event, 'property-ingestion-events')
