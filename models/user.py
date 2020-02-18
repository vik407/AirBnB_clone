#!/usr/bin/python3
""" User class. Used as base for future users."""

from models.base_model import BaseModel


class User(BaseModel):
    """ User class. Used as base for future users."""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
