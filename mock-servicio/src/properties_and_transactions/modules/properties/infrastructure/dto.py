from ....config.db import db

Base = db.declarative_base()


class PropertyDTO(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.String, primary_key=True)
    agent_id = db.Column(db.String)
    property_id = db.Column(db.String)
    property_address = db.Column(db.String, unique=True)
    property_city = db.Column(db.String)
    property_state = db.Column(db.String)
    property_zip = db.Column(db.String)
    property_price = db.Column(db.Float)
    property_bedrooms = db.Column(db.Integer)
    property_bathrooms = db.Column(db.Integer)
    property_square_feet = db.Column(db.Integer)
    property_lot_size = db.Column(db.Integer)
    property_type = db.Column(db.String)
