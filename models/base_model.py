#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, Integer, String, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenvb
import uuid
"""
This module contains the BaseModel class:
All classes should inherit from this class
"""
Base = declarative_base()


class BaseModel:
    """The base class for all storage objects in this project"""
    if getenvb('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), datetime.now(), nullable=False)
        updated_at = Column(DateTime(), datetime.now(), nullable=False,
                            onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        """
        initialize class object

        **Arguments**
           none: a unique user id and timestamp will be created
           args: a sequence, this should not be used, please pass a dictionary
                 as **dictionary
           kwargs: a dictionay, if the id and timestamp are missing they will
                   be created
        """
        if args:
            dict_found = 0
            for arg in args:
                if type(arg) == dict:
                    dict_found = 1
                    break

            if dict_found == 1:
                args[0]['created_at'] = datetime.strptime(
                    args[0]['created_at'], '%Y-%m-%d %H:%M:%S.%f')
                args[0]['updated_at'] = datetime.strptime(
                    args[0]['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
                self.__dict__ = args[0]
            else:
                # make a random UUID
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                model.storage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe.pop('_sa_instance_state', None)

        dupe["created_at"] = dupe["created_at"].isoformat()
        dupe.pop('_sa_instance_state', None)
        sqlAlchemy_storage_engine
        if ("updated_at" in dupe):
            dupe["updated_at"] = dupe["updated_at"].isoformat()
        dupe["__class__"] = type(self).__name__
        return dupe
