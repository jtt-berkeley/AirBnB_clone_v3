#!/usr/bin/python3
"""
Creates a new view for State
objects that handles all default
RestFul API actions
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
import json

@app_views.route('/states')
def states_all():
    myArr = []
    s = storage.all("State")
    for k, v in s.items():
        myArr.append(v.to_json())
    #print(storage.all("State"))
    return jsonify(myArr)