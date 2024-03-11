import typing

import strawberry

from .schemas.property import Property
from .schemas.property_ingestion import PropertyIngestion
from .services.property_ingestion_services import get_property_ingestion, get_property_ingestion_by_id
from .services.property_services import get_properties, get_property_by_id


@strawberry.type
class Query:
    properties_ingestion: typing.List[PropertyIngestion] = strawberry.field(resolver=get_property_ingestion)
    property_ingestion_by_id: PropertyIngestion = strawberry.field(resolver=get_property_ingestion_by_id)
    properties: typing.List[Property] = strawberry.field(resolver=get_properties)
    property_by_id: Property = strawberry.field(resolver=get_property_by_id)

