# -*- coding: utf-8 -*-

# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.babel import Babel

import os
import logging

app = Flask(__name__)           # The WSGI compliant web application object
from app.startup.create_app import create_app
create_app()

db = SQLAlchemy(app)            # Setup Flask-SQLAlchemy
# babel = Babel(app)              # Setup Flask:Babel

# path & logs
_BASEDIR = os.path.dirname(os.path.abspath(__file__))
_FORMAT = '[%(asctime)s][%(levelname)s]\t%(message)s'
_LOG_PATH = os.path.join(_BASEDIR, '..', 'logs', 'example.log')
logger = logging.getLogger('example')
logging.basicConfig(filename=_LOG_PATH, format=_FORMAT, datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)


# Initializing all core modules ...
from app import core
