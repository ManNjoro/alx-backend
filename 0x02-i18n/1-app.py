#!/usr/bin/env python3
"""
A simple Flask application demonstrating internationalization (i18n)
using Flask Babel.
"""

from flask import Flask, render_template
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


@app.route('/')
def hello() -> str:
    """
    Render the index template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
