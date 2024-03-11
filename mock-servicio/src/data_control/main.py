import os

from flask import Flask

from src.data_control.config.db import init_db

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


# Identify the base directory


def register_handlers():
    from src.data_control.modules.country_regulations import application


def import_alchemy_models():
    from src.data_control.modules.country_regulations.infrastructure import dto


def import_seeds():
    from src.data_control.modules.country_regulations.infrastructure import seeds


def start_consumer():
    import threading
    from src.data_control.modules.country_regulations.infrastructure import consumers as ingestion

    # Command subscription
    threading.Thread(target=ingestion.subscribe_to_commands).start()

    # Event subscription
    threading.Thread(target=ingestion.subscribe_to_events).start()


config = {
    "DATABASE_URL": os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db')),
    "TESTING": os.getenv('TESTING', False)
}

import_alchemy_models()
init_db(config)
import_seeds()  # Warning: This will seed the database with some data, use with caution

if not config.get('TESTING'):
    start_consumer()

# Health check
app = Flask(__name__)


@app.route('/')
def my_function(request):
    return 'ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
