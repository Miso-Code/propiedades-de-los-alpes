import os
from enum import Enum

from src.bff_gql.api.v1.schemas.property import Property
from src.bff_gql.api.v1.schemas.property_ingestion import Country, City, Coordinates, Location, PropertyIngestion

DATA_COLLECTION_PATH = os.getenv("DATA_COLLECTION_PATH", default="http://localhost:5000")
PROPERTIES_AND_TRANSACTIONS_PATH = os.getenv("PROPERTY_AND_TRANSACTIONS_PATH", default="http://localhost:5001")
PULSAR_HOST = os.getenv("PULSAR_HOST", default="localhost")
PULSAR_PORT = os.getenv("PULSAR_PORT", default="6650")
PULSAR_SCHEMA = os.getenv("PULSAR_SCHEMA", default="pulsar")
PULSAR_API_KEY = os.getenv("PULSAR_API_KEY", default="")

CLASS_MAPPER = {
    "country": Country,
    "city": City,
    "coordinates": Coordinates,
    "location": Location,
    "property_ingestion": PropertyIngestion,
    "property": Property,
}


class CommandTopics(Enum):
    CREATE_PROPERTY_INGESTION_COMMAND_TOPIC = "property-ingestion-create-commands"
    DELETE_PROPERTY_INGESTION_COMMAND_TOPIC = "property-ingestion-delete-commands"
    DATA_CONTROL_COMMAND_TOPIC = "data-control-commands"


class EventTopics(Enum):
    PROPERTY_INGESTION_EVENT_TOPIC = "property-ingestion-events"
    PROPERTY_REGULATION_EVENT_TOPIC = "property-regulation-events"
    PROPERTY_REGULATION_FAILED_EVENT_TOPIC = "property-regulation-failed-events"
    PROPERTY_EVENT_TOPIC = "property-events"
    PROPERTY_FAILED_EVENT_TOPIC = "property-failed-events"
