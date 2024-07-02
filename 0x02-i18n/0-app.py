#!/usr/bin/env python3
"""defines a flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """home route index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
