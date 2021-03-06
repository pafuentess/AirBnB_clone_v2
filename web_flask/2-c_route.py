#!/usr/bin/python3
""" doc """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ doc """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display():
    """ doc """
    return ("HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ doc """
    check_text = text.replace("_", " ")
    return ("C {}".format(check_text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
