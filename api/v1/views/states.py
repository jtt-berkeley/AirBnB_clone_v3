#!/usr/bin/python3
"""
Creates a new view for State
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
import json
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_all():
    """
    retrieves list of all state objects
    """
    myArr = []
    s = storage.all("State")
    for k, v in s.items():
        myArr.append(v.to_json())
    return jsonify(myArr)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def stateId(state_id):
    """
    retrieves a state object by stateId
    """
    try:
        state = storage.get("State", state_id).to_json()
        return jsonify(state)
    except:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteState(state_id):
    """
    delete state object by stateId
    """
    try:
        stateObject = storage.get("State", state_id)
        storage.delete(stateObject)
        storage.save()
        return jsonify({}), 200
    except:
        abort(404)


@app_views.route("/states", methods=['POST'], strict_slashes=False)
def createState():
    """
    creates a state
    """
    try:
        createdState = request.get_json()
    except:
        return "Not a JSON", 400

    if "name" not in createdState:
        return "Missing name", 400
    stateNew = State(**createdState)
    stateNew.save()
    stateObject = storage.get("State", stateNew.id).to_json()
    return jsonify(stateObject), 201


@app_views.route("/states/<state_id>", methods=['PUT'], strict_slashes=False)
def updateState(state_id):
    """
    updates state by ID
    """
    try:
        updatedState = request.get_json()
    except:
        return "Not a JSON", 400
    stateObject = storage.get("State", state_id)
    if stateObject is None:
        abort(404)
    for k, v in updatedState.items():
        if k == "id" or k == "updated_at" or k == "created_at":
            continue
        setattr(stateObject, k, v)
    stateObject.save()
    state = stateObject.to_json()
    return jsonify(state), 200
