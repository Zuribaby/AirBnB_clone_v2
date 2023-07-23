#!/usr/bin/python3
"""0-hello_route module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb_route():
    """Renders Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """renders HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Renders C <text>"""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


if __name__ == '__main__':
    """App entering point"""
    app.run(host='0.0.0.0', port=5000)
