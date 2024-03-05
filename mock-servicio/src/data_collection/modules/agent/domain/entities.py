from dataclasses import dataclass, field

from ....seedwork.domain.entities import Entity
from .value_objects import Name, Authentication, Automation, Email


@dataclass
class Agent(Entity):
    started_executions: int = 0
    ...


@dataclass
class ManualAgent(Agent):
    name: Name = field(default_factory=Name)
    email: Email = field(default_factory=Email)
    auth: Authentication = field(default_factory=Authentication)


@dataclass
class AutomationAgent(Agent):
    automation: Automation = field(default_factory=Automation)
    creator_name: Name = field(default_factory=Name)