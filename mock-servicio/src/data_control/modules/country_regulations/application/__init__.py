from pydispatch import dispatcher

from .handlers import HandlerPropertyIngestionDomain
from ..domain.events import PropertyIngestionApprovedEvent

dispatcher.connect(HandlerPropertyIngestionDomain.handle_property_ingestion_approved,
                   signal=f"{PropertyIngestionApprovedEvent.__name__}Integration")