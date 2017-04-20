#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify 

# create a route /status on the object app_views that returns a JSON: "status": "OK"
@app_views.route('/status')
def appviews():
    return jsonify({"status": "OK"})
