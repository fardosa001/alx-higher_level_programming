#!/usr/bin/python3
"""class Student that defines a student"""


class Student():
    """Defines class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes class student
        Attributes:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
