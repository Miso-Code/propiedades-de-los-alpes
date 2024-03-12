from pydispatch import dispatcher

from .handlers import HandleDomainEvents

from src.watchdog.modules.sagas.domain.events.data_collection import PropertyIngestionStartedEvent
from src.watchdog.modules.sagas.domain.events.data_control import PropertyIngestionApprovedEvent, PropertyIngestionRejectedEvent
from src.watchdog.modules.sagas.domain.events.properties_and_transactions import PropertyCreatedEvent, \
    PropertyNotCreatedEvent

dispatcher.connect(HandleDomainEvents.handle_domain_event,
                   signal=PropertyIngestionStartedEvent.__name__)

dispatcher.connect(HandleDomainEvents.handle_domain_event,
                   signal=PropertyIngestionApprovedEvent.__name__)

dispatcher.connect(HandleDomainEvents.handle_domain_event,
                   signal=PropertyIngestionRejectedEvent.__name__)

dispatcher.connect(HandleDomainEvents.handle_domain_event,
                   signal=PropertyCreatedEvent.__name__)

dispatcher.connect(HandleDomainEvents.handle_domain_event,
                   signal=PropertyNotCreatedEvent.__name__)