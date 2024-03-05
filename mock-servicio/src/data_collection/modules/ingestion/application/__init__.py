from pydispatch import dispatcher

from .handlers import HandlerPropertyIngestionDomain
from ..domain.events import PropertyIngestionStartedEvent

dispatcher.connect(HandlerPropertyIngestionDomain.handle_property_ingestion_started,
                   signal=f"{PropertyIngestionStartedEvent.__name__}Integration")
