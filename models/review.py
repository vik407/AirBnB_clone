#!/usr/bin/python3
""" Review class. Used as base for future Reviews."""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class. Used as base for future Reviews."""

    place_id = ''
    user_id = ''
    text = ''
