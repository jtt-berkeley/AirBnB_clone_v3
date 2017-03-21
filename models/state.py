#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from sqlalchemy.orm import relationship, backref
from os import getenvb
"""
state module
    contain
        State class
"""


class State(BaseModel, Base):
    """
    This is the State class
    """
    if getenvb('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes from BaseModel Class
        """
        super(State, self).__init__(*args, **kwargs)
