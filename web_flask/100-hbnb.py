#!/usr/bin/python3
""" A script to start Flask web application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to display HTML page for hbnb home"""
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")
    return render_template("100-hbnb.html",
                           amenities=amenities,
                           places=places,
                           states=states)


@app.teardown_appcontext
def teardown(excpt=None):
    """Function to remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
