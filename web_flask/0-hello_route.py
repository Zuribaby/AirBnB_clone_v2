#!/usr/bin/python3
# 0-hello_route module
# A script that renders a page.

from flask import Flask

app = Flask(__name__)


# Route definition
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
