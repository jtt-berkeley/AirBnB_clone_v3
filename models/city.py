#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from sqlalchemy import ForeignKey
from os import getenv
"""
city module
    contains
        the City class inherts from BaseModel, Base
"""


class City(BaseModel, Base):
    """
    The City class
    """
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
