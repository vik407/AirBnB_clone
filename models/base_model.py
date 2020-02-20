#!/usr/bin/python3
""" BaseModel class. Used as base for future classes.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """ BaseModel class. Used as base for future classes.
    """
    def __init__(self, *args, **kwargs):
        """Validate non interactive and init method
        """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """if it’s a new instance (not from a dictionary representation),
            add a call to the method new(self) on storage
            """
            models.storage.new(self)

    def __str__(self):
        """Return the string representation
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.to_dict()))

    def save(self):
        """Update date
        """
        self.updated_at = datetime.now()
        """In the method save(self):
        call save(self) method of storage
        """
        models.storage.save()

    def to_dict(self):
        """ Return the dictionary
        """
        _dict = self.__dict__.copy()
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        _dict['__class__'] = self.__class__.__name__
        return(_dict)
