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
        self.__models_available = { "User": User,
                                 "Amenity": Amenity, "city": City,
                                 "Place": Place, "Review": Review,
                                 "State": State}
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        orm_objects = {}
        if cls:
            cls_obj = self.__session.query(cls).all()
        else:
            for a, i in self.__models_available.items():
                j = self.__session.query(i).all()
                if j:
                    for k in j:
                        print(k.id)
                        orm_objects[k.__dict__['id']] = k
            return orm_objects

                #     print(type(j))
                # print(,self.__session.query(i).all())
    def new(self, obj):
        print(obj, type(obj))
        print("in new")
        self.__session.add(obj)
        self.__session.commit()
        print("able to add session")
    def save(self):
        print("enter save")
        self.__session.flush()
        print("able to save")
    def delete(self, obj=None):
        if obj is not None:
            self.__session.commit()
            self.__session.delete(obj)
    def reload(self):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
