#!/usr/bin/python3
"""
This is module 8-cities_by_state
In this module we combine flask with sqlAlchemy for the first time
Run this script from AirBnB_v2 directory for imports
"""
from models import storage
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states/')
@app.route('/states/<id_d>')
def cities_by_states(id_d="all"):
    if id_d == "all":
        states = storage.all("State").values()
        return render_template("9-states.html",
                               Query_name="States", states=states, result=None)
    else:
        result = storage.get_cities(id_d)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
