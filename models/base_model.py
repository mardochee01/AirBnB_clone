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

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            value, date_format)

    def __str__(self):
        """
        Returns string representation of the class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_r = self.__dict__.copy()
        dict_r["__class__"] = self.__class__.__name__
        dict_r["created_at"] = self.created_at.isoformat()
        dict_r["updated_at"] = self.updated_at.isoformat()
        return dict_r
