#!/usr/bin/python3
"""
Base class defined
"""


class Base:
    """
    __nb_objects:
        Records the number of objects instanciated
    id:
        uniquely identifies the instanciated object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
