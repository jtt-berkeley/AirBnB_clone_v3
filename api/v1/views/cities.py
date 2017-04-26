#!/usr/bin/python3
"""
Creates a new view for City
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


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def getCity(city_id):
    """
    displays city by city ID
    """
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


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def createCity(state_id):
    """
    create city object
    """
    getState = storage.get("State", state_id)
    if getState is None:
        abort(404)
    try:
        cityJson = request.get_json()
        if "name" not in cityJson:
            return "Missing name", 400
        cityJson["state_id"] = state_id
        cityNew = City(cityJson)
        cityNew.save()
        cityNewCreated = storage.get("City", cityNew.id).to_json()
        return jsonify(cityNewCreated), 201
    except:
        return "Not a JSON", 400


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def updateCity(city_id):
    """
    updates city by ID
    """
    try:
        updatedCity = request.get_json()
    except:
        updatedCity = None
    if updatedCity is None:
        return "Not a JSON", 400
    cityObject = storage.get("City", city_id)
    if cityObject is None:
        abort(404)
    ignoredKeys = ["id", "state_id", "created_at", "updated_at"]
    for k, v in updatedCity.items():
        if k not in ignoredKeys:
            setattr(cityObject, k, v)
    cityObject.save()
    city = cityObject.to_json()
    return jsonify(city), 200
