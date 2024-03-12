import os

PULSAR_HOST = os.getenv("PULSAR_HOST", default="localhost")
PULSAR_PORT = os.getenv("PULSAR_PORT", default="6650")
PULSAR_SCHEMA = os.getenv("PULSAR_SCHEMA", default="pulsar")
PULSAR_API_KEY = os.getenv("PULSAR_API_KEY", default="")
