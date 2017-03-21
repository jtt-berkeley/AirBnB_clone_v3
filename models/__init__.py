#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.engine import file_storage
# from models.engine import db_engine
from os import getenv


if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
    storage = db_storage.DBStorage()
    print("USING DB")
else:
    storage = file_storage.FileStorage()
    print("USING FS")
storage.reload()
