#!/usr/bin/env python3
"""A Basic Flask app with internationalization and timezone support.
"""
import pytz
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    
    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): The default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# Simulated user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    
    Returns:
        dict or None: A dictionary representing the user if found, None otherwise.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """Performs routines before each request's resolution.
    
    Sets the current user in the global `g` object.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for supported languages.
    
    Returns:
        str: The best match for the requested locale.
    """
    # Check for locale in the query parameters
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    
    # Check for locale in the user's settings
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    
    # Check for locale in the request headers
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    
    # Default to the app's default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """Determines the best match for supported timezones.
    
    Returns:
        str: The best match for the requested timezone.
    """
    # Check for timezone in the query parameters
    timezone = request.args.get('timezone', '').strip()
    
    # Check for timezone in the user's settings
    if not timezone and g.user:
        timezone = g.user['timezone']
    
    # Validate and return the timezone
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def get_index() -> str:
    """Renders the home/index page.
    
    Returns:
        str: The rendered HTML for the index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
