from sqlalchemy import Column, String, Integer, Float
from ....config.db import Base


class CountryRegulationDTO(Base):
    __tablename__ = "country_regulations"
    id = Column(String, primary_key=True)
    country_code = Column(String, nullable=False)
    country_name = Column(String, nullable=False)
    fields = Column(String, nullable=False)  # comma separated
    regulation_condition_type = Column(Integer, nullable=False)
    regulation_condition_value = Column(String, nullable=False)
