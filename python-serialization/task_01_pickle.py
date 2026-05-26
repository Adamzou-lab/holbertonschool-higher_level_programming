#!/usr/bin/env python3
"""Module that defines a CustomObject class with pickle serialization."""

import pickle


class CustomObject:
    """A custom class with name, age and is_student attributes
    and pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initializes CustomObject with name, age and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def age(self):
        """Retrieves the age attribute."""
        return self.__age

    @age.setter
    def age(self, value):
        """Sets and validates the age attribute."""
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        self.__age = value

    @property
    def name(self):
        """Retrieves the name attribute."""
        return self.__name

    @name.setter
    def name(self, value):
        """Sets and validates the name attribute."""
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def is_student(self):
        """Retrieves the is_student attribute."""
        return self.__is_student

    @is_student.setter
    def is_student(self, value):
        """Sets and validates the is_student attribute."""
        if not isinstance(value, bool):
            raise TypeError("is_student must be a bool")
        self.__is_student = value

    def display(self):
        """Prints the object's attributes to stdout."""
        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        """Serializes the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes and returns a CustomObject from a pickle file."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
