#!/usr/bin/python3
"""
Module that implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BassModel:
    """
    Class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """
