from pydispatch import dispatcher

from .handlers import HandleAgentDomain
from ...ingestion.domain.events import PropertyIngestionStartedEvent

dispatcher.connect(HandleAgentDomain.handle_property_ingestion_started,
                   signal=PropertyIngestionStartedEvent.__name__)
