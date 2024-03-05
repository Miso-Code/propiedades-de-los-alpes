from ...domain.factories import CountryRegulationFactory
from ...infrastructure.factories import RepositoryFactory
from .....seedwork.application.commands import CommandHandler


class CountryRegulationBaseHandler(CommandHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._country_regulation_factory: CountryRegulationFactory = CountryRegulationFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def country_regulation_factory(self):
        return self._country_regulation_factory
