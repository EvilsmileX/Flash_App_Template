# -*- coding: utf-8 -*-

from app import app
import os

def create_app(extra_config_settings={}):
    """
    Initialize Flask applicaton
    """

    # Read Framework settings from 'config/env_settings.py' file
    app.config.from_object('config.env_settings')

    # Read environment-specific settings from file defined by OS environment variable 'ENV_SETTINGS_FILE'
    env_settings_file = os.environ.get('ENV_SETTINGS_FILE', 'env_settings.py.example')
    if os.path.isfile(env_settings_file):
    	app.config.from_pyfile(env_settings_file)

    # Read extra config settings from function parameter 'extra_config_settings'
    app.config.update(extra_config_settings)  # Overwrite with 'extra_config_settings' parameter

    return app

