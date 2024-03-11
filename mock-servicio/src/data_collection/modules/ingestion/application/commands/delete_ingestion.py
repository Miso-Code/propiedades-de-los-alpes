from dataclasses import dataclass
from uuid import UUID

from colorama import Fore, Style

from ..commands.base import CreateIngestionBaseHandler
from ..dto import PropertyIngestionDTO
from ..mappers import PropertyIngestionMapper
from ...domain.entities import PropertyIngestion
from ...domain.repositories import PropertyIngestionRepository
from ......data_collection.seedwork.application.commands import Command
from .....seedwork.application.commands import execute_command as command
from .....seedwork.infrastructure.uow import UnitOfWorkPort


@dataclass
class DeletePropertyIngestionCommand(Command):
    id: str


class DeleteIngestionHandler(CreateIngestionBaseHandler):
    def handle(self, command: DeletePropertyIngestionCommand):
        repository = self.repository_factory.create_object(PropertyIngestionRepository.__class__)

        property_ingestion = repository.get_by_id(UUID(command.id))
        if not property_ingestion:
            raise Exception('Property Ingestion not found')  # TODO: Should raise a domain exception?

        property_ingestion.delete_property_ingestion()

        UnitOfWorkPort.register_batch(repository.delete, property_ingestion.id)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()
        print(f'{Fore.GREEN}Property Ingestion {command.id} deleted{Style.RESET_ALL}')


@command.register(DeletePropertyIngestionCommand)
def execute_delete_property_ingestion_command(command: DeletePropertyIngestionCommand):
    handler = DeleteIngestionHandler()
    handler.handle(command)
