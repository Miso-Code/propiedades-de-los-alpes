import os

from .config.db import init_db

# Identify the base directory
basedir = os.path.abspath(os.path.dirname(__file__))


def register_handlers():
    from .modules.country_regulations import application


def import_alchemy_models():
    from .modules.country_regulations.infrastructure import dto

def import_seeds():
    from .modules.country_regulations.infrastructure import seeds

def start_consumer():
    import threading
    from .modules.country_regulations.infrastructure import consumers as ingestion

    # Command subscription
    threading.Thread(target=ingestion.subscribe_to_events()).start()


config = {
    "DATABASE_URL": os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db')),
    "TESTING": os.getenv('TESTING', False)
}

import_alchemy_models()
init_db(config)
import_seeds()  # Warning: This will seed the database with some data, use with caution

if not config.get('TESTING'):
    start_consumer()
