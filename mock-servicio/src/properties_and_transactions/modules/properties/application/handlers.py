from ..domain.events import PropertyCreatedEvent
from ..application.mappers import PropertyMapper
from ....seedwork.application.handlers import Handler
from ..infrastructure.dispatchers import Dispatcher


class HandlerPropertyDomain(Handler):

    @staticmethod
    def handle_property_created(event: PropertyCreatedEvent):
        dispatcher = Dispatcher()
        dispatcher.publish_created_event(event.__dict__, 'property-events')

    @staticmethod
    def handle_property_not_created(event: PropertyCreatedEvent):
        dispatcher = Dispatcher()
        dispatcher.publish_not_created_event(event.__dict__, 'property-failed-events')
