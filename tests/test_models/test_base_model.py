#!/usr/bin/python3
"""
Unit test for the base class base model
"""


import unittest
from models.base_model import BaseModel
from models import base_model
from datetime import datetime


class TestBasemodel(unittest.TestCase):
    """TestBasemodel Test the basemodel class """

    model = BaseModel()

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_datetime_type(self):
        """ Test datetime type """
        self.assertTrue(type(self.model.created_at) == datetime)

    def test_str(self):
        """ Test str output """
        self.assertEqual(self.model.__str__(), "[" + self.model.__class__.__name__ + "]"
                         " (" + self.model.id + ") " + str(self.model.__dict__))

    def test_id_creation(self):
        """ check for module documentation """
        my_first = BaseModel()
        my_second = BaseModel()
        my_third = BaseModel()
        self.assertTrue(my_first.id != my_second.id)
        self.assertTrue(my_third.id != my_second.id)
        self.assertTrue(my_first.id != my_third.id)

    def test_base_from_emp_dict(self):
        """test with an empty dictionary"""
        my_dict = {}
        my_new_model = BaseModel(**my_dict)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_non_dict(self):
        """test with a None dictionary"""
        my_new_model = BaseModel(None)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_save(self):
        """ test save method of basemodel """
        my_new_model = BaseModel()
        previous = my_new_model.updated_at
        my_new_model.save()
        actual = my_new_model.updated_at
        self.assertTrue(actual > previous)

    def test_isinstance(self):
        """ Check if object is basemodel instance """
        self.assertIsInstance(self.model, BaseModel)

if __name__ == "__main__":
    unittest.main()
