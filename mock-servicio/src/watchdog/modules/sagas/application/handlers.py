from colorama import Fore, Style

from src.watchdog.modules.sagas.application.coordinators.property_ingestion_saga import PropertyIngestionCoordinator
from src.watchdog.seedwork.application.handlers import Handler


class HandleDomainEvents(Handler):

    @staticmethod
    def handle_domain_event(event):
        try:
            print(Fore.CYAN + f'[Watchdog Saga] [{type(event).__name__}] Domain event received', event.__dict__)
            print(Style.RESET_ALL)
            coordinator = PropertyIngestionCoordinator()
            coordinator.process_event(event)

        except Exception as e:
            print(e)
            print(Fore.CYAN + f'[Watchdog Saga] [{type(event).__name__}] Error while handling the domain event')
            print(Style.RESET_ALL)
            raise e

class HandleCompensationEvents(Handler):

    @staticmethod
    def handle_compensation_event(event):
        try:
            print(Fore.CYAN + f'[Watchdog Saga] [{type(event).__name__}] Compensation event received', event.__dict__)
            print(Style.RESET_ALL)
            coordinator = PropertyIngestionCoordinator()
            coordinator.rollback(event)

        except Exception as e:
            print(e)
            print(Fore.CYAN + f'[Watchdog Saga] [{type(event).__name__}] Error while handling the compensation event')
            print(Style.RESET_ALL)
            raise e