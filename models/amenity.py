#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from os import getenvb
"""
amenity module
    contains
        the Amentiry class inherts from BaseModel and Base
"""

class Amenity(BaseModel, Base):
    """
    The Amenity class
    """
    if getenvb('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'Amenity'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes class objects. Inherts attributes from parent
        """
        super().__init__(*args, **kwargs)
