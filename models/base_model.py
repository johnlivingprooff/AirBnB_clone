#!/usr/bin/python3
"""Defines a BaseModel class"""

from datetime import datetime  # Import datetime module
import uuid                    # Import unique identifier


class BaseModel:
    """A basemodel that defines all common attributes/methods for
    other classes
    """

    def __init__(self):
        """Initializes once an instance is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns readable string representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with
        current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of instance
        """
        instance_dict = self.__dict__
        instance_dict['__class__'] = type(self).__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
