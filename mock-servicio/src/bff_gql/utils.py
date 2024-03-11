import dataclasses
import datetime
import json
import time

import pulsar
import requests

from src.bff_gql.constants import CLASS_MAPPER, PULSAR_SCHEMA, PULSAR_PORT, PULSAR_HOST, PULSAR_API_KEY

epoch = datetime.datetime.utcfromtimestamp(0)
PULSAR_ENV: str = 'BROKER_HOST'


def time_millis():
    return int(time.time() * 1000)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def millis_to_datetime(millis):
    return datetime.datetime.fromtimestamp(millis / 1000.0)


def broker_host():
    return f"{PULSAR_SCHEMA}://{PULSAR_HOST}:{PULSAR_PORT}"


def pulsar_auth():
    if PULSAR_API_KEY == '':
        return None
    return pulsar.AuthenticationToken(PULSAR_API_KEY)


def get_topic_name(topic: str) -> str:
    if PULSAR_API_KEY == "":
        return topic
    return f"persistent://public/default/{topic}"


def sync_api_call(url, method, data=None, raise_for_status=True):
    response = requests.request(
        method=method,
        url=url,
        json=data
    )
    if raise_for_status:
        response.raise_for_status()
    return response.json()


def str_to_datetime(date_str: str) -> datetime.datetime:
    return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')


def json_to_instance(data: dict, class_name: str):
    if class_name not in CLASS_MAPPER:
        raise ValueError(f"Class '{class_name}' not found in CLASS_MAPPER")

    cls = CLASS_MAPPER[class_name]

    instance = cls(**data)

    for key, value in data.items():
        if isinstance(value, dict):
            nested_instance = json_to_instance(value, key)
            setattr(instance, key, nested_instance)

    return instance


def instance_to_json(instance):
    if dataclasses.is_dataclass(instance):
        instance_dict = dataclasses.asdict(instance)
        return json.loads(json.dumps(instance_dict, indent=4))
    else:
        raise ValueError("Input must be a dataclass instance")
