#!/usr/bin/python3
"""
Creates a new view for Places
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import storage, Place


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def places_all():
    """
    displays all places
    """
    myArr = []
    s = storage.all("Place")
    for k, v in s.items():
        myArr.append(v.to_json())
    return jsonify(myArr)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def placeId(place_id):
    """
    retrieves a place by ID
    """
    try:
        place = storage.get("Place", place_id).to_json()
        return jsonify(place)
    except:
        abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def deletePlace(place_id):
    """
    delete place by ID
    """
    try:
        place = storage.get("Place", place_id)
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    except:
        abort(404)


@app_views.route("/places", methods=['POST'], strict_slashes=False)
def createPlace():
    """
    creates new place
    """
    placeJson = request.get_json()
    try:
        if "email" not in placeJson:
            return "Missing email", 400
        if "password" not in placeJson:
            return "Missing password", 400
        placeNew = Place(placeJson)
        placeNew.save()
        placeNew = storage.get("Place", placeNew.id).to_json()
        return jsonify(placeNew), 201
    except:
        return "Not a JSON", 400


@app_views.route("/places/<place_id>", methods=['PUT'],
                 strict_slashes=False)
def updatePlace(place_id):
    """
    updates place by ID
    """
    try:
        updatedPlace = request.get_json()
    except:
        return "Not a JSON", 400
    placeObject = storage.get("Place", user_id)
    if placeObject is None:
        abort(404)
    for k, v in updatedPlace.items():
        if k == "id" or k == "updated_at" or k == "created_at":
            continue
        setattr(placeObject, k, v)
    placeObject.save()
    place = placeObject.to_json()
    return jsonify(place), 200
