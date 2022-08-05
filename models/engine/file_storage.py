#!/usr/bin/python3
"""
Module that serializes and deserializes JSON file
"""


import json

from models.base_model import BaseModel

class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class.__name, obj.id)
        self.__object[key] = obj

    def save(self):
        """
        serializes __objects to the JSON 
        file (path: __file_path)
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        
