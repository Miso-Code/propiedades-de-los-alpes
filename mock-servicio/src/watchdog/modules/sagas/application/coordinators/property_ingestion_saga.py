from datetime import datetime
from threading import Timer, Lock

from colorama import Fore, Style

from src.watchdog.modules.sagas.application.dto import SagaLogDTO
from src.watchdog.modules.sagas.infrastructure.dispatchers import Dispatcher
from src.watchdog.seedwork.application.commands import Command
from src.watchdog.seedwork.application.queue import PriorityQueue
from src.watchdog.seedwork.application.sagas import ChoreographyCoordinator
from src.watchdog.modules.sagas.application.services import SagaLogService
from src.watchdog.seedwork.domain.events import DomainEvent


class PropertyIngestionCoordinator(ChoreographyCoordinator):

    def persist_in_saga_log(self, message):
        raise NotImplementedError

    def build_command(self, event: DomainEvent, command_type: type) -> Command:
        raise NotImplementedError

    def build_compensation(self, event: DomainEvent, command_type: str):
        # check if ends with "Command" and add inside data:
        payload = {
                    "property_id": _get_correlation_id(event),
                    "property_ingestion_id": _get_correlation_id(event),
                }
        if command_type.endswith("Command"):
            return {
                "data": payload
            }
        return payload

    def rollback(self, saga_group: list[SagaLogDTO], event):
        # self.persist_in_saga_log(f"Rollback started for event: {event}")
        service = SagaLogService()
        dispatcher = Dispatcher()
        print(Fore.LIGHTRED_EX + f"[Watchdog Saga] Rollback started for saga: "
                                 f"{saga_group[0].correlation_id}", Style.RESET_ALL)
        for saga_log in saga_group:
            ...
            # TODO: Implement the rollback logic for each transaction
            transaction = service.get_transaction_by_id(saga_log.transaction_id)
            dispatcher.publish_compensation_to_topic(
                self.build_compensation(event, transaction.compensation),
                transaction.compensation,
                transaction.compensation_topic,
            )

            service.update_saga_log_status(saga_log.id, "Rollback")

    def process_event(self, event: DomainEvent):
        # self.persist_in_saga_log(f"Event received: {event}")
        service = SagaLogService()

        saga_group = service.get_saga_logs_by_correlation_id(_get_correlation_id(event))
        transaction = service.get_transaction_by_name(event.__class__.__name__)

        if not saga_group:
            print(Fore.LIGHTYELLOW_EX + f"[Watchdog Saga] Starting saga {_get_correlation_id(event)}"
                  , Style.RESET_ALL)

        print(Fore.LIGHTYELLOW_EX + f"[Watchdog Saga] [{event.__class__.__name__}] "
                                    f"is the {len(saga_group) + 1} in the saga {_get_correlation_id(event)}"
              , Style.RESET_ALL)

        if not transaction:
            failed_transaction = service.get_transaction_by_error_name(event.__class__.__name__)
            if failed_transaction:
                print(Fore.LIGHTRED_EX + f"[Watchdog Saga] Transaction {event.__class__.__name__} failed, "
                                         f"rolling back saga {_get_correlation_id(event)}", Style.RESET_ALL)
                self.rollback(saga_group, event)
                return
            else:
                raise Exception(f"Transaction {event.__class__.__name__} not found")

        saga_log_dto = SagaLogDTO(
            correlation_id=_get_correlation_id(event),
            status="Pending",
            transaction_id=transaction.id,
        )
        saga_log = service.create_saga_log(saga_log_dto)

        if transaction.is_last:
            for saga in saga_group:
                service.update_saga_log_status(saga.id, "Completed")
            service.update_saga_log_status(saga_log.id, "Completed")
            print(Fore.LIGHTYELLOW_EX + f"[Watchdog Saga] Saga {_get_correlation_id(event)} completed", Style.RESET_ALL)

        # in case a transaction arrives after the rollback
        if saga_group and saga_group[0].status == "Rollback":
            self.rollback([saga_log], event)


def _get_correlation_id(event: DomainEvent):
    return event.property_ingestion_id if hasattr(event, 'property_ingestion_id') else event.property_id if hasattr(
        event, 'property_id') else None
