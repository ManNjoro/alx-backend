 # Flask Internationalization Example

This Flask application demonstrates internationalization (i18n) using Flask Babel. It allows users to select their preferred language and timezone, and displays localized strings and dates/times accordingly.

## Step-by-Step Explanation

### 1. Configuration

The application's configuration is defined in the `Config` class. It specifies the supported languages, the default language, and the default timezone.

```python
class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
```

### 2. Flask App Setup

The Flask app is created and configured with the `Config` class. Babel is initialized and registered with the app.

```python
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
```

### 3. User Data

A dictionary of users is defined, each with a name, preferred language, and timezone. This data is used to dynamically set the user's locale and timezone based on their login.

```python
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```

### 4. Locale Selection

The `get_locale` function determines the best matching language for the user based on the Accept-Language header in the HTTP request. It also checks if the user is logged in and has a preferred language set.

```python
@babel.localeselector
def get_locale() -> str:
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if hasattr(g, 'user') and g.user and g.user['locale']\
            and g.user['locale'] in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_
```