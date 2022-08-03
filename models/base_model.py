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

    def __init__(self, *keys, **kwkeys):
        """
        Initialize the BaseModel class
        """
        if kwkeys:
            for key, value in kwkeys.items():
                if key in ('created_at', 'updated_at'):
                    print("i Got it !", key)
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                if key != '__class__':
                    exec("self.{} = '{}'".format(key, value))
        else:
            self.id = uuid4().hex
            self.created_at = datetime.now()
            self.updated_at = self.created_at


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
        Returns a dictionary containing all keys/valueues
        of __dict__ of the instance
        """
        dict_r = self.__dict__.copy()
        dict_r['__class__'] = self.__class__.__name__
        dict_r['created_at'] = self.created_at.isoformat()
        dict_r['updated_at'] = self.updated_at.isoformat()

        return dict_r
