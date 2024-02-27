import os

from flask import Flask, jsonify
from flask_swagger import swagger

# Identify the base directory
basedir = os.path.abspath(os.path.dirname(__file__))


def register_handlers():
    from ..modules.ingestion import application
    from ..modules.agent import application


def import_alchemy_models():
    from ..modules.ingestion.infrastructure import dto
    from ..modules.agent.infrastructure import dto


def start_consumer(app: Flask):
    import threading
    from ..modules.ingestion.infrastructure import consumers as ingestion

    # Command subscription
    threading.Thread(target=ingestion.subscribe_to_commands,
                     args=[app.app_context(), app.test_request_context()]).start()


def start_cron_jobs(app: Flask):
    import threading
    from ..modules.agent.infrastructure import jobs as agent

    # Automatic agent
    # threading.Timer(1, agent.agent_automation, args=[app.app_context(), app.test_request_context()]).start()
    threading.Thread(target=agent.cron_job, args=[app.app_context(), app.test_request_context()]).start()


def create_app(configuration={}):
    # Initialize the Flask application
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuration.get('TESTING')

    # Initialize the DB
    from ..config.db import init_db
    init_db(app)

    from ..config.db import db

    import_alchemy_models()
    register_handlers()

    with app.app_context():
        db.create_all()
    if not app.config.get('TESTING'):
        start_consumer(app)
        start_cron_jobs(app)

    # Import Blueprints
    from . import ingestion
    from . import agent

    # Register Blueprints
    app.register_blueprint(ingestion.bp)
    app.register_blueprint(agent.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Propiedades de los Alpes API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
