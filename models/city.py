#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from sqlalchemy import ForeignKey

class City(BaseModel, Base):
    """
    The city class
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
