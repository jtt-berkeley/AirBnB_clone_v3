#!/usr/bin/python3
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')))
        self.__models_available = {"User": User,
                                   "Amenity": Amenity, "city": City,
                                   "Place": Place, "Review": Review,
                                   "State": State}

        if getenv('HBNB_MYSQL_ENV') == 'test':
            base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        orm_objects = {}
        if cls:
            for k in self.__session.query(cls):
                orm_objects[k.__dict__['id']] = k
        else:
            for i in self.__models_available.values():
                j = self.__session.query(i).all()
                if j:
                    for k in j:
                        print(k.id)
                        orm_objects[k.__dict__['id']] = k
        return orm_objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
