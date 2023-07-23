#!/usr/bin/python3
"""0-hello_route module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route definition"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """App entering point"""
    app.run(host='0.0.0.0', port=5000)
