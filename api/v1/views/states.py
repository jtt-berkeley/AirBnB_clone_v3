#!/usr/bin/python3
"""
Creates a new view for State
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import abort, jsonify
import json
from models import storage

# added method GET and strict_slashes
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_all():
    myArr = []
    s = storage.all("State")
    for k, v in s.items():
        myArr.append(v.to_json())
    #print(storage.all("State"))
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


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
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

@app_views.route("/states", methods=['POST'])
def createState():
    """
    creates a state
    """
    try:
        createdState = request.get_json()
        if "name" not in createdState:
            return "Missing name", 400
        stateNew = State(createdState)
        stateNew.save()
        stateObject = storage.get("State", stateNew.id).to_json()
        return jsonify(stateObject), 201
    except:
        return "Not a JSON", 400

#@app_views.route("/states/<state_id>", methods=['PUT'])
#def updateState(state_id):
#    """
#    updates a State
#    """
#    try:
#        updatedState = request.get_json()


