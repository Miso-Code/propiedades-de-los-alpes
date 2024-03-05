import os

from flask import Flask, jsonify
from flask_swagger import swagger

# Identify the base directory
basedir = os.path.abspath(os.path.dirname(__file__))


def import_alchemy_models():
    from ..modules.properties.infrastructure import dto
    
def register_handlers():
    from ..modules.properties import application
    
def start_consumer(app: Flask):
    import threading
    from ..modules.properties.infrastructure import consumers as ingestion

    # Command subscription
    threading.Thread(target=ingestion.subscribe_to_events,
                     args=[app]).start()

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
        
    # Import Blueprints
    from . import properties
    
    # Register Blueprints
    app.register_blueprint(properties.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Propiedades de los Alpes API - properties_and_transactions"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
