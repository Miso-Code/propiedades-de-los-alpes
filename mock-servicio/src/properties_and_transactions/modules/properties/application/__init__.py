from pydispatch import dispatcher

from .handlers import HandlerPropertyDomain
from ..domain.events import PropertyCreatedEvent

dispatcher.connect(HandlerPropertyDomain.handle_property_ingestion_started,
                   signal=f"{PropertyCreatedEvent.__name__}Integration")
