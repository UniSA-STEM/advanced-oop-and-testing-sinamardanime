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

    def get_name(self):
        """Gets the staff member's name."""
        return self.__name

    def get_role(self):
        """Gets the staff member's role."""
        return self.__role

    def get_assigned_animals(self):
        """Gets the animals assigned to this staff member."""
        return self.__assigned_animals

    def get_assigned_enclosures(self):
        """Gets the enclosures assigned to this staff member."""
        return self.__assigned_enclosures

    # --- Properties ---
    name = property(get_name)
    role = property(get_role)
    assigned_animals = property(get_assigned_animals)
    assigned_enclosures = property(get_assigned_enclosures)


class Zookeeper(Staff):
    """Zookeeper feeds animals and cleans their enclosures."""

    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, animal):
        """Feeds an assigned animal."""
        print(self.name + " feeds " + animal.name + " (" + animal.species + ").")

