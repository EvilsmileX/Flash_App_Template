# -*- coding: utf-8 -*-

from flask import request, redirect, make_response, Response, Blueprint

# Exception
from sqlalchemy.exc import IntegrityError, OperationalError

from app import app, db, logger

bp = Blueprint('views', __name__, url_prefix='/')

@bp.route('index')
def home():
	return 'Hello World'

# Register blueprint
app.register_blueprint(bp)

