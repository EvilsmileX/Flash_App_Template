# -*- coding: utf-8 -*-

from app import db
from wtforms import Form, BooleanField, TextField, PasswordField, validators


class Example(db.Model):
    """docstring for Example"""
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.Unicode(255), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    

