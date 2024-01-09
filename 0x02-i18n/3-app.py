#!/usr/bin/env python3
"""
A simple Flask application demonstrating internationalization (i18n)
using Flask Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    A configuration class that sets up the application's settings.
    """
    LANGUAGES = ["en", "fr"]


app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best matching language for the user
    based on the Accept-Language header.

    Returns:
        str: Best matching language code (e.g., 'en', 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """
    Render the home page template with translated strings.
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template(
        '3-index.html', home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
