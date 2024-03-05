from ..mappers import PropertyIngestionMapper
from ...domain.repositories import PropertyIngestionRepository
from .....seedwork.application.queries import Query, QueryHandler, QueryResult, execute_query as query
from .base import IngestionQueryBaseHandler


class GetAllIngestions(Query):
    ...


class GetAllIngestionsHandler(IngestionQueryBaseHandler):

    def handle(self, query: GetAllIngestions) -> QueryResult:
        repository = self.repository_factory.create_object(PropertyIngestionRepository.__class__)
        ingestion_dtos = repository.get_all()
        ingestions = [self.property_ingestion_factory.create_object(ingestion_dto, PropertyIngestionMapper()) for
                      ingestion_dto in ingestion_dtos]
        return QueryResult(ingestions)


@query.register(GetAllIngestions)
def execute_query_get_all_ingestions(query: GetAllIngestions) -> QueryResult:
    handler = GetAllIngestionsHandler()
    return handler.handle(query)
