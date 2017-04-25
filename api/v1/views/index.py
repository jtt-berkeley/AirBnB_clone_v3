#!/usr/bin/python3
from api.v1.views import app_views
from flask import app, jsonify
from models import storage
"""
create a route /status on the object
app_views that returns a JSON: "status": "OK"
"""


@app_views.route('/status', strict_slashes=False)
def appviews():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def appstats():
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
