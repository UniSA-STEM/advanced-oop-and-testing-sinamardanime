'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

# staff.py
from abc import ABC, abstractmethod

class Staff(ABC):
    """
    The Staff class is an abstract base class representing all staff members in the zoo.
    It defines common attributes and enforces the implementation of specific methods
    (e.g., perform_duty) in subclasses.
    """

    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []

