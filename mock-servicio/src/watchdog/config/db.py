# create a db engine for sqlalchemy
from flask_sqlalchemy.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db: Session = None
Base = declarative_base()
def init_db(config: dict):
    engine = create_engine(config.get('DATABASE_URL'), echo=True)
    session_factory = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    global db
    db = session_factory()