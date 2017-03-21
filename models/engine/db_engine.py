#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBstorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv(' HBNB_MYSQL_DB')))

    def all(self, cls=None):
        orm_objects = {}
        if cls:
            cls_obj = self.__session.query(cls).all()
        else:
            for i in ['User', 'State', 'Amenity', 'Place', 'Review']:
                self.__session.query(i).all()
        self.__session.
    def new(self, obj):
        self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        if !obj:
            self.__session.delete(obj)
    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
