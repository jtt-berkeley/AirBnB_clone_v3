#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column
from sqlalchemy.orm import relationship, backref

class User(BaseModel, Base):
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
