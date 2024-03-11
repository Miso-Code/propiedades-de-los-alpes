from sqlalchemy import Column, String, Integer, Boolean
from ....config.db import Base


class SagaLogDTO(Base):
    __tablename__ = "saga_logs"
    id = Column(String, primary_key=True)
    correlation_id = Column(String, nullable=False)
    status = Column(String, nullable=False)
    transaction_id = Column(String, nullable=False)

class TransactionDTO(Base):
    __tablename__ = "transactions"
    id = Column(String, primary_key=True)
    event = Column(String, nullable=False)
    error = Column(String, nullable=False)
    compensation = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    is_last = Column(Boolean, nullable=False, default=False)
    compensation_topic = Column(String, nullable=True)