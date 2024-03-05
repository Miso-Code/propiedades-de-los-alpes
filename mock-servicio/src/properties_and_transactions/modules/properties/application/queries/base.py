

from .....seedwork.application.queries import QueryHandler

from ...infrastructure.factories import RepositoryFactory

from ...domain.factories import PropertyFactory

class PropertiesQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._property_factory: PropertyFactory = PropertyFactory()
        
    @property
    def repository_factory(self):
        return self._repository_factory
    
    @property
    def property_factory(self):
        return self._property_factory