#!/usr/bin/env python3
"""
"""

from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def hello():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
