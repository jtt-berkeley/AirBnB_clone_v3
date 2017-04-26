#!/usr/bin/python3
"""
Creates a new view for Amenities
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import storage, User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users_all():
    """
    displays all users
    """
    myArr = []
    s = storage.all("User")
    for k, v in s.items():
        myArr.append(v.to_json())
    return jsonify(myArr)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def userId(user_id):
    """
    retrieves a user by ID
    """
    try:
        user = storage.get("User", user_id).to_json()
        return jsonify(user)
    except:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteUse(user_id):
    """
    delete user by ID
    """
    try:
        user = storage.get("User", user_id)
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    except:
        abort(404)


@app_views.route("/users", methods=['POST'], strict_slashes=False)
def createUser():
    """
    creates new user
    """
    userJson = request.get_json()
    try:
        if "email" not in userJson:
            return "Missing email", 400
        if "password" not in userJson:
            return "Missing password", 400
        userNew = User(userJson)
        userNew.save()
        userNew = storage.get("User", userNew.id).to_json()
        return jsonify(userNew), 201
    except:
        return "Not a JSON", 400


@app_views.route("/users/<user_id>", methods=['PUT'],
                 strict_slashes=False)
def updateUser(user_id):
    """
    updates user by ID
    """
    try:
        updatedUser = request.get_json()
    except:
        return "Not a JSON", 400
    userObject = storage.get("User", user_id)
    if userObject is None:
        abort(404)
    for k, v in updatedUser.items():
        if k == "id" or k == "updated_at" or k == "created_at":
            continue
        setattr(userObject, k, v)
    userObject.save()
    user = userObject.to_json()
    return jsonify(user), 200
