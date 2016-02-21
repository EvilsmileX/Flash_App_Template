# -*- coding: utf-8 -*-

from flask import request, redirect, make_response, Response, Blueprint
from functools import partial

# Exception
from sqlalchemy.exc import IntegrityError, OperationalError

from app import app, db, logger
# from app.core.models import Example

MakeResponse = partial(Response, mimetype='text/json')

bp = Blueprint('apis', __name__, url_prefix='/api')

@bp.route('/')
def entry():
	return 'Hello APIs'


# Register blueprint
app.register_blueprint(bp)
