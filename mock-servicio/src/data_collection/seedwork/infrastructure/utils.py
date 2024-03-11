import time

import pulsar

from .constants import PULSAR_SCHEMA, PULSAR_HOST, PULSAR_PORT, PULSAR_API_KEY


def time_millis():
    return int(time.time() * 1000)


def broker_host():
    return f"{PULSAR_SCHEMA}://{PULSAR_HOST}:{PULSAR_PORT}"


def get_topic_name(topic: str) -> str:
    if PULSAR_API_KEY == "":
        return topic
    return f"persistent://public/default/{topic}"


def pulsar_auth():
    if PULSAR_API_KEY == '':
        return None
    return pulsar.AuthenticationToken(PULSAR_API_KEY)
