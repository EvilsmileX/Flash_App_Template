# -*- coding: utf-8 -*-

from app import db

def create_db():
    """ Create db tables when app starts """
    # from app.core.models import User, Social

    # Create all tables
    db.create_all()

