#!/usr/bin/python3
"""
Module that serializes and deserializes JSON file
"""

class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class.__name, obj.id)
        self.__object[key] = obj  

