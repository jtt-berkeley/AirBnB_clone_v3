#!/usr/bin/python3
"""
Handles errors
"""
from api.v1.views import app_views
from flask import Blueprint, Flask, make_response
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def appteardown(exception):
    """
    Closes
    """
    storage.close()


@app_views.errorhandler(404)
def page_not_found():
    """
    Starts the API
    """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    myHost = '0.0.0.0'
    myPort = '5000'
    if os.getenv('HBNB_API_HOST'):
        myHost = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_HOST'):
        myPort = os.getenv('HBNB_API_PORT')
    app.run(host='0.0.0.0', port='5000')
