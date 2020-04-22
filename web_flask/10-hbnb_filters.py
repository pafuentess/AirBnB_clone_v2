#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_list():
    """ doc """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
