#!/usr/bin/python3
from api.v1.views import app_views
from flask import Blueprint, Flask, make_response
from models import storage
import os

"""
first endpoint (route) will
be to return the status of your API
"""
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def appteardown(exception):
    storage.close()


@app_views.errorhandler(404)
def page_not_found():
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    myHost = os.getenv(HBNB_API_HOST, '0.0.0.0')
    myPort = os.getenv(HBNB_API_PORT, 5000)
    app.run(host=myHost, port=myPort)
