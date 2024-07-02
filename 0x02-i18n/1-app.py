#!/usr/bin/env python3
"""define a flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class config:
    """Configration for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = FLask(__name__)
app.config.from_object(config)
app.url_map_strict_slashes = False
babel = Babel(app=app)


@app.route('/')
def get_index() -> str:
    """ home route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
