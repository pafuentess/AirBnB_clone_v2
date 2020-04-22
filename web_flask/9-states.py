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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """ doc """
    states = storage.all("State")
    cities = storage.all("City").values()
    if id is not None:
        id = "State." + id
    return render_template("9-states.html",
                           states=states, cities=cities, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
