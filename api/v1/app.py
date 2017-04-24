#!/usr/bin/python3
from api.v1.views import app_views
from flask import Blueprint, Flask
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def appteardown(exception):
    storage.close()


@app_views.errorhandler(404)
def page_not_found():
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
