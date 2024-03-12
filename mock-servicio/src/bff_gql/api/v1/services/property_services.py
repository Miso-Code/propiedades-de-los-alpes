import typing

import strawberry

from src.bff_gql.constants import PROPERTIES_AND_TRANSACTIONS_PATH
from src.bff_gql.api.v1.schemas.property_ingestion import PropertyIngestion
from src.bff_gql.utils import sync_api_call, json_to_instance


def get_properties(root) -> typing.List[PropertyIngestion]:
    properties_json = sync_api_call(f"{PROPERTIES_AND_TRANSACTIONS_PATH}/properties_and_transactions", "GET")
    properties = []

    for prop in properties_json:
        properties.append(
            json_to_instance(prop, "property")
        )
    return properties

def get_property_by_id(root, id: strawberry.ID) -> PropertyIngestion:
    property_json = sync_api_call(f"{PROPERTIES_AND_TRANSACTIONS_PATH}/properties_and_transactions/{id}", "GET")
    return json_to_instance(property_json, "property")
