#!/usr/bin/python3
from api.v1.views import app_views
from flask import Blueprint, Flask
from models import storage


# instance of Flask
app = Flask(__name__) 
# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)

# declare a method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def appteardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
