#!/usr/bin/python3
""" doc """

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ doc """
    check_text = text.replace("_", " ")
    return ("Python {}".format(check_text))


@app.route('/number/<n>', strict_slashes=False)
def is_int(n):
    """ doc """
    if "." not in n:
        return ("{} is number".format(n))


@app.route('/number_template/<n>', strict_slashes=False)
def display_html(n):
    """ doc """
    if "." not in n:
        return (render_template("5-number.html", n=n))


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_even(n):
    """ doc """
    if "." not in n:
        return (render_template("6-number_odd_or_even.html", n=int(n)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
