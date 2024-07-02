#!/usr/bin/env python3
"""define a flask app"""
from flask import FLask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


class config:
    """Configration for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = FLask(__name__)
app.config.from_object(config)
app.url_map_strict_slashes = False
babel = Babel(app=app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """uses get user """
    user = get_user()
    g.user = user


def get_user() -> dict:
    """gets a user
    Return:
        (dict): a user dictionary or None
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@babel.localeselector
def get_locale() -> str:
    """gets the locale lang of the website"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('locale')
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """gets the locale timezone"""
    time_zone = request.args.get('timezone')
    if not time_zone and g.user:
        time_zone = g.user['timezone']

    try:
        return pytz.timezone(time_zone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route('/')
def get_index() -> str:
    """ home route """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
