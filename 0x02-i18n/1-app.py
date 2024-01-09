#!/usr/bin/env python3
"""
"""

from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    A configuration class that sets up the application's settings.
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)

babel.default_locale = 'en'
babel.timezone = 'UTC'
