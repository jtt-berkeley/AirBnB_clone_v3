#!/usr/bin/python3
from models.base_model import BaseMode, Base, Table, Column
from sqlalchemy import ForeignKey
from os import getenvb
"""
review module
    contains
         Review class
"""


class Review(BaseModel, Base):
    """
    The review class
    """
    if getenvb('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey(places.id), nullable=False)
        user_id = Column(String(60), ForeignKey(users.id), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """
        initialize from the BaseModel class 
        """
        super().__init__(*args, **kwargs)
