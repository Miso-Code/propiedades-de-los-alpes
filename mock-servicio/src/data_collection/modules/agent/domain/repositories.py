from abc import ABC

from ....seedwork.domain.repositories import Repository


class AgentRepository(Repository, ABC):
    ...