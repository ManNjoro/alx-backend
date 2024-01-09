#!/usr/bin/env python3
"""
A simple Flask application demonstrating internationalization (i18n)
using Flask Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello() -> str:
    """
    Render the home page template with translated strings.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
