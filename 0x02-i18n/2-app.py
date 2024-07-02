#!/usr/bin/env python3
"""define a flask app"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    """gets the locale lang of the website"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """ home route """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
