#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
"""
"""

class Amenity(BaseModel, Base):
    """
    The Amenity class
    """
    __tablename__ = 'Amenity'
    name = Column(String(128), nullable=False)
    def __init__(self, *args, **kwargs):
        """
        initializes class objects. Inherts attributes from parent
        """
        super().__init__(*args, **kwargs)
