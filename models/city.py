#a!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column, String
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
        print("enter HBNB")
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        print("able to set attributes")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
