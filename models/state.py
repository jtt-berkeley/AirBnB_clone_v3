#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from sqlalchemy.orm import relationship, backref

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
