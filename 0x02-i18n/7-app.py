#!/usr/bin/env python3
"""
A simple Flask application demonstrating internationalization (i18n)
using Flask Babel.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config(object):
    """
    A configuration class that sets up the application's settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best matching language for the user
    based on the Accept-Language header.

    Returns:
        str: Best matching language code (e.g., 'en', 'fr').
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if hasattr(g, 'user') and g.user and g.user['locale']\
            and g.user['locale'] in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Function to get the timezone
    """
    tz = request.args.get("timezone")
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if hasattr(g, 'user') and g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user["timezone"])
            return g.user["timezone"]
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """
    Function to get user by ID
    """
    user_id = request.args.get('login_as', None)
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Finds a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


@app.route('/')
def hello() -> str:
    """
    Render the home page template with translated strings.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
