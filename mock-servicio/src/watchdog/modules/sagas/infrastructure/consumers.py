import logging
import traceback

import _pulsar
import pulsar
from colorama import Fore, Style
from pulsar.schema import *
from pydispatch import dispatcher

from src.watchdog.seedwork.infrastructure import utils
from src.watchdog.seedwork.infrastructure.utils import get_topic_name, pulsar_auth


# More abstract
def subscribe_to_events(topic, event_schema, domain_event):
    client = None
    try:
        client = pulsar.Client(utils.broker_host(), authentication=pulsar_auth())
        consumer = client.subscribe(get_topic_name(topic),
                                    consumer_type=_pulsar.ConsumerType.Shared,
                                    subscription_name='watch-dog-sub-events',
                                    schema=AvroSchema(event_schema),
                                    initial_position=pulsar.InitialPosition.Earliest)
        while True:
            message = consumer.receive()
            data: event_schema = message.value()
            print(Fore.LIGHTYELLOW_EX + f'[Watchdog Saga] [{domain_event.__name__}] Integration Event received: ', data)
            print(Style.RESET_ALL)

            # I'm not sure if this is the correct way to convert integration events to domain events
            dispatcher.send(signal=domain_event.__name__,
                            event=data)

            consumer.acknowledge(message)
    except Exception as e:
        logging.error(f'ERROR: Error while consuming events from topic {topic}')
        traceback.print_exc()
        if client:
            client.close()

# Subscribe to commands
