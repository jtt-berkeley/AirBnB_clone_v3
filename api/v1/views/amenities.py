#!/usr/bin/python3
"""
Creates a new view for Amenities
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import storage, Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities_all():
    """
    displays all amenities
    """
    myArr = []
    s = storage.all("Amenity")
    for k, v in s.items():
        myArr.append(v.to_json())
    return jsonify(myArr)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def amenityId(amenity_id):
    """
    retrieves an amenity object by ID
    """
    try:
        amenity = storage.get("Amenity", amenity_id).to_json()
        return jsonify(amenity)
    except:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteAmenity(amenity_id):
    """
    delete amenity object by ID
    """
    try:
        amenityObject = storage.get("Amenity", amenity_id)
        storage.delete(amenityObject)
        storage.save()
        return jsonify({}), 200
    except:
        abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def createAmenity():
    """
    creates Amenity object
    """
    try:
        createdAmenity = request.get_json()
    except:
        return "Not a JSON", 400

    if "name" not in createdAmenity:
        return "Missing name", 400
    amenityNew = Amenity(createdAmenity)
    amenityNew.save()
    amenityObject = storage.get("Amenity", amenityNew.id).to_json()
    return jsonify(amenityObject), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def updateAmenity(amenity_id):
    """
    updated Amenity by ID
    """
    amenityObject = storage.get("Amenity", amenity_id)
    if amenityObject is None:
        abort(404)
    try:
        updatedAmenity = request.get_json()
        for k, v in updatedAmenity.items():
            if k == "id" or k == "updated_at" or k == "created_at":
                continue
            setattr(amenityObject, k, v)
        amenityObject.save()
        amenity = amenityObject.to_json()
        return jsonify(amenity), 200
    except:
        return "Not a JSON", 400
