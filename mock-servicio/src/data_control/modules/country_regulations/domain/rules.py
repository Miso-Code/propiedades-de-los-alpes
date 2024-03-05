from enum import Enum
from typing import Any
from colorama import Fore, Style

from .value_objects import CountryRegulationCondition, CountryRegulationOnFail, CountryRegulationConditionType
from ....seedwork.domain.rules import BusinessRule


class CountryRegulationRule(BusinessRule):
    entity: object
    fields: list[str] = []
    conditions: list[CountryRegulationCondition] = []
    on_fail: CountryRegulationOnFail = CountryRegulationOnFail.CANCEL
    target = "Property"

    def __init__(self, entity: object, fields: list[str], conditions: list[CountryRegulationCondition],
                 on_fail=CountryRegulationOnFail.CANCEL,
                 target="Property", message='The country regulation is invalid'):
        super().__init__(message)
        self.entity = entity
        self.fields = fields
        self.conditions = conditions
        self.on_fail = on_fail
        self.target = target

    def is_valid(self) -> bool:
        for field in self.fields:
            value = getattr(self.entity, field)
            for condition in self.conditions:
                return self._check_condition(value, condition)

    def _check_condition(self, value: Any, condition: CountryRegulationCondition) -> bool:
        try:
            if condition.type == CountryRegulationConditionType.EQUALS:
                return str(value) == str(condition.value)
            elif condition.type == CountryRegulationConditionType.NOT_EQUALS:
                return str(value) != str(condition.value)
            elif condition.type == CountryRegulationConditionType.GREATER_THAN:
                return float(value) > float(condition.value)
            elif condition.type == CountryRegulationConditionType.LESS_THAN:
                return float(value) < float(condition.value)
            elif condition.type == CountryRegulationConditionType.GREATER_THAN_OR_EQUALS:
                return float(value) >= float(condition.value)
            elif condition.type == CountryRegulationConditionType.LESS_THAN_OR_EQUALS:
                return float(value) <= float(condition.value)
            elif condition.type == CountryRegulationConditionType.IN:
                return str(value) in list(condition.value)
            elif condition.type == CountryRegulationConditionType.NOT_IN:
                return str(value) not in list(condition.value)
            elif condition.type == CountryRegulationConditionType.BETWEEN:
                return float(condition.value[0]) <= float(value) <= float(condition.value[1])
            elif condition.type == CountryRegulationConditionType.NOT_BETWEEN:
                return float(condition.value[0]) > float(value) or float(value) > float(condition.value[1])
            elif condition.type == CountryRegulationConditionType.LIKE:
                return condition.value in value
            elif condition.type == CountryRegulationConditionType.NOT_LIKE:
                return condition.value not in value
            elif condition.type == CountryRegulationConditionType.IS_NULL:
                return str(value) is None
            elif condition.type == CountryRegulationConditionType.IS_NOT_NULL:
                return str(value) is not None
            elif condition.type == CountryRegulationConditionType.IS_EMPTY:
                return str(value) == ""
            elif condition.type == CountryRegulationConditionType.IS_NOT_EMPTY:
                return str(value) != ""
            else:
                return False
        except:
            print(
                Fore.RED + "Error " + Fore.LIGHTYELLOW_EX + f"checking condition {condition.type} for value {value} "
                                                            f"in entity {getattr(self.entity, 'id')}" + Style.RESET_ALL)
            return False
