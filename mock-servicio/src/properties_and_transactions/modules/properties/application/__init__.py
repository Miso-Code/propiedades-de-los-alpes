from pydispatch import dispatcher

from .handlers import HandlerPropertyDomain
from ..domain.events import PropertyCreatedEvent

dispatcher.connect(HandlerPropertyDomain.handle_property_created,
                   signal=f"{PropertyCreatedEvent.__name__}Integration")

dispatcher.connect(HandlerPropertyDomain.handle_property_not_created,
                   signal=f"{PropertyCreatedEvent.__name__}Rollback")
