"""Reusable mixins part of the project's seedwork

In this file, you will find the reusable mixins part of the project's seedwork.

"""

from .rules import BusinessRule
from .exceptions import BusinessRuleException

class ValidateRulesMixin:
    def validate_rule(self, rule: BusinessRule):
        if not rule.is_valid():
            raise BusinessRuleException(rule)
