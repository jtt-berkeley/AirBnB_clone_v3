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
        self.__session.
