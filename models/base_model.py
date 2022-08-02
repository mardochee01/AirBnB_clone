#!/usr/bin/python3
"""
Module that implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initialize the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of the class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dict_r = {}
        dict_r["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at": 
                dict_r[key] = value.isoformat()
            else:
                dict_r[key] = value
            return dict_r
