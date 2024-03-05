from ....config.db import db

Base = db.declarative_base()


class PropertyIngestionDTO(db.Model):
    __tablename__ = "property_ingestion"
    id = db.Column(db.String, primary_key=True)
    agent_id = db.Column(db.String, nullable=False)
    location_city_name = db.Column(db.String, nullable=False)
    location_city_code = db.Column(db.String, nullable=False)
    location_country_name = db.Column(db.String, nullable=False)
    location_country_code = db.Column(db.String, nullable=False)
    location_address = db.Column(db.String, nullable=False)
    location_building = db.Column(db.String, nullable=False)
    location_floor = db.Column(db.String, nullable=False)
    location_inner_code = db.Column(db.String, nullable=False)
    location_coordinates_latitude = db.Column(db.Float, nullable=False)
    location_coordinates_longitude = db.Column(db.Float, nullable=False)
    location_additional_info = db.Column(db.String, nullable=False)
    property_type = db.Column(db.String, nullable=False)
    property_subtype = db.Column(db.String, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    parking_spaces = db.Column(db.Integer, nullable=False)
    construction_area = db.Column(db.Float, nullable=False)
    land_area = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String, nullable=False)
    price_per_m2 = db.Column(db.Float, nullable=False)
    price_per_ft2 = db.Column(db.Float, nullable=False)
    property_url = db.Column(db.String, nullable=False)
    property_images = db.Column(db.String, nullable=False)
