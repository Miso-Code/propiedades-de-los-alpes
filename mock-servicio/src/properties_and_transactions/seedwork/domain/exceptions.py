""" Reusable exceptions part of the project's seedwork

In this file, you will find the reusable exceptions part of the project's seedwork.

"""

from .rules import BusinessRule

class DomainException(Exception):
    ...

class ImmutableIdException(DomainException):
    def __init__(self, message='The identifier must be immutable'):
        self.__message = message
    def __str__(self):
        return str(self.__message)

class BusinessRuleException(DomainException):
    def __init__(self, rule: BusinessRule):
        self.rule = rule

    def __str__(self):
        return str(self.rule)

class FactoryException(DomainException):
    def __init__(self, message):
        self.__message = message
    def __str__(self):
        return str(self.__message)
