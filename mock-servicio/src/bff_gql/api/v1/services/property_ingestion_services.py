import typing

import strawberry

from src.bff_gql.constants import DATA_COLLECTION_PATH
from src.bff_gql.api.v1.schemas.property_ingestion import PropertyIngestion
from src.bff_gql.utils import sync_api_call, json_to_instance


def get_property_ingestion(root) -> typing.List[PropertyIngestion]:
    url = f"{DATA_COLLECTION_PATH}/ingestion"
    properties_json = sync_api_call(url, "GET")

    properties = [json_to_instance(prop, "property_ingestion") for prop in properties_json]
    return properties


def get_property_ingestion_by_id(root, id: strawberry.ID) -> PropertyIngestion:
    url = f"{DATA_COLLECTION_PATH}/ingestion/{id}"
    property_json = sync_api_call(url, "GET")

    property_instance = json_to_instance(property_json, "property_ingestion")
    return property_instance
