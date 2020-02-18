#!/usr/bin/python3
"""Filstorage requirement
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
"""Update models/__init__.py: to create a unique FileStorage instance for your
application:
import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
"""

storage = FileStorage()
storage.reload()
