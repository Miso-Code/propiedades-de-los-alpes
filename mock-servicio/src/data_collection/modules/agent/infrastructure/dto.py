from ....config.db import db

Base = db.declarative_base()
"""
TODO: since there are two types of Agents, we need to create a strategy to handle both types of agents
by creating multiple tables and a common table for shared attributes
"""


class AgentDTO(db.Model):
    __tablename__ = "agent"
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False, default="automation")
    automation_source = db.Column(db.String, nullable=True)
    automation_protocol = db.Column(db.String, nullable=True)
    automation_port = db.Column(db.String, nullable=True)
    automation_username = db.Column(db.String, nullable=True)
    automation_password = db.Column(db.String, nullable=True)
    automation_frequency_unit = db.Column(db.String, nullable=True)
    automation_frequency_value = db.Column(db.Integer, nullable=True)
    automation_last_run = db.Column(db.DateTime, nullable=True)
    started_executions = db.Column(db.Integer, nullable=True, default=0)
