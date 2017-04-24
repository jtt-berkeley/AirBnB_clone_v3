#!/usr/bin/python3
"""
Creates a new view for State
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import City, State, storage

@app_views.route("/states/<state_id>/cities", methods=['GET'],
                 strict_slashes=False)
def city_get_all(state_id):
    """
    list all City objects with state_id
    """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    try:
        cities = []
        citiesAll = storage.all("City")
        for cityObjects in citiesAll.values():
            if cityObjects.state_id == state_id:
                cityJson = cityObjects.to_json()
                cities.append(cityJson)
        return jsonify(cities)
    except:
        abort(404)


# server works with this one
@app_views.route('cities/<city_id>', methods=['GET'], strict_slashes=False)
def getCity(city_id):
    try:
        city = storage.get("City", city_id).to_json()
        return jsonify(city)
    except:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteCity(city_id):
    """
    delete city object by cityId
    """
    try:
        stateObject = storage.get("City", city_id)
        storage.delete(stateObject)
        storage.save()
        return jsonify({}), 200
    except:
        abort(404)
