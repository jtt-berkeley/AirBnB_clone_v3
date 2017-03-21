#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenvb


class DBstorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenvb('HBNB_MYSQL_USER'),
            getenvb('HBNB_MYSQL_PWD'),
            getenvb('HBNB_MYSQL_HOST'),
            getenvb(' HBNB_MYSQL_DB')))

    def all(self, cls=None):
        orm_objects = {}
        if cls:
            cls_obj = self.__session.query(cls).all()
            
        else:
            for i in ['User', 'State', 'Amenity', 'Place', 'Review']:
                self.__session.query(i).all()
        self.__session.
    def new(self, obj):
    def save(self):
    def delete(self, obj=None):
    def reload(self):
