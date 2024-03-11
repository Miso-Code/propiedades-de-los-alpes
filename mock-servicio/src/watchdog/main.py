import os

from flask import Flask

from src.watchdog.config.db import init_db

basedir = os.path.abspath(os.path.dirname(__file__))


def import_alchemy_models():
    from src.watchdog.modules.sagas.infrastructure import dto  # noqa

def import_seeds():
    from src.watchdog.modules.sagas.infrastructure import seeds  # noqa


def register_handlers():
    from src.watchdog.modules.sagas import application  # noqa


def start_consumer():
    import threading
    from src.watchdog.modules.sagas.infrastructure import consumers as events
    from src.watchdog.modules.sagas.infrastructure.schema.v1 import events as events_schemas
    from src.watchdog.modules.sagas.domain.events import data_collection as data_collection_events
    from src.watchdog.modules.sagas.domain.events import data_control as data_control_events
    from src.watchdog.modules.sagas.domain.events import \
        properties_and_transactions as properties_and_transactions_events

    integration_events_topics = [
        ('property-ingestion-events',
         events_schemas.PropertyIngestionCreatedEvent,
         data_collection_events.PropertyIngestionStartedEvent),
        ('property-regulation-events',
         events_schemas.PropertyIngestionValidatedEvent,
         data_control_events.PropertyIngestionApprovedEvent),
        ('property-regulation-failed-events',
         events_schemas.PropertyIngestionRejectedEvent,
         data_control_events.PropertyIngestionRejectedEvent),
        ('property-events',
         events_schemas.PropertyCreatedEvent,
         properties_and_transactions_events.PropertyCreatedEvent),
        ('property-failed-events',
         events_schemas.PropertyNotCreatedEvent,
         properties_and_transactions_events.PropertyNotCreatedEvent)
    ]

    for topic, schema, domain_event in integration_events_topics:
        # Command subscription
        threading.Thread(target=events.subscribe_to_events, args=(topic, schema, domain_event)).start()

config = {
    "DATABASE_URL": os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db')),
    "TESTING": os.getenv('TESTING', False)
}

import_alchemy_models()
init_db(config)
import_seeds()

register_handlers()
start_consumer()


# Health check
app = Flask(__name__)


@app.route('/')
def my_function(request):
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))