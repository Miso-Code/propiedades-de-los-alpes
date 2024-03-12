from datetime import datetime

from colorama import Fore, Style

from ..domain.events import PropertyIngestionApprovedEvent
from ....seedwork.application.handlers import Handler
from ..infrastructure.dispatchers import Dispatcher


class HandlerPropertyIngestionDomain(Handler):

    @staticmethod
    def handle_property_ingestion_approved(event: PropertyIngestionApprovedEvent):
        print(
            f"{Fore.GREEN}Success:{Fore.LIGHTYELLOW_EX} [Country Regulations] CountryRegulation Applied{Style.RESET_ALL}")
        dispatcher = Dispatcher()

        full_event = {
            **event.__dict__,
            "validation_date": datetime.now().isoformat(),
            "validation_result": "approved",
            "validation_message": "The property ingestion was approved successfully",
        }

        dispatcher.publish_validated_event(full_event, 'property-regulation-events')

    @staticmethod
    def handle_property_ingestion_rejected(event: PropertyIngestionApprovedEvent):
        print(
            f"{Fore.RED}Error:{Fore.LIGHTYELLOW_EX} [Country Regulations] Dispatching error event {Style.RESET_ALL}")
        dispatcher = Dispatcher()

        full_event = {
            **event.__dict__,
            "validation_date": datetime.now().isoformat(),
            "validation_result": "rejected",
        }

        dispatcher.publish_rejected_event(full_event, 'property-regulation-failed-events')
