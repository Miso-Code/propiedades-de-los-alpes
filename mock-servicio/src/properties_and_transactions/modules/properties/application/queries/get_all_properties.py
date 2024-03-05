from ..mappers import PropertyMapper
from ...domain.repositories import PropertyPropertiesRepository

from .....seedwork.application.queries import Query, QueryResult, execute_query as query

from .base import PropertiesQueryBaseHandler

class GetAllProperties(Query):
    ...
    
class GetAllPropertiesHandler(PropertiesQueryBaseHandler):
    def handle(self, query: GetAllProperties) -> QueryResult:
        repository = self.repository_factory.create_object(PropertyPropertiesRepository.__class__)
        properties_dtos = repository.get_all()
        properties = [self.property_factory.create_object(property_dto, PropertyMapper()) for
                      property_dto in properties_dtos]
        return QueryResult(properties)
    
@query.register(GetAllProperties)
def execute_query_get_all_properties(query: GetAllProperties) -> QueryResult:
    handler = GetAllPropertiesHandler()
    return handler.handle(query)