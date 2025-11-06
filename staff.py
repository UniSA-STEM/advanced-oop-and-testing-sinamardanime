'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


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


    name = property(get_name)
    role = property(get_role)
    assigned_animals = property(get_assigned_animals)
    assigned_enclosures = property(get_assigned_enclosures)


    def assign_animal(self, animal):
        """Assigns an animal to this staff member."""
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        """Assigns an enclosure to this staff member."""
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    @abstractmethod
    def perform_duty(self):
        """Abstract method that describes the staff member’s daily duties."""
        pass




class Zookeeper(Staff):
    """
    The Zookeeper class represents a staff member responsible for
    maintaining animal welfare and enclosure cleanliness.
    Zookeepers ensure that animals are fed, their habitats are kept
    clean, and daily care routines are followed.
    """

    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, animal):
        """
        Feeds an assigned animal and reports the action.

        Parameters:
            animal (Animal): The animal being fed.
        """
        print(self.name + " carefully feeds " + animal.name + ", the " + animal.species + ".")
        print(animal.name + " seems happy and continues eating its " + animal.diet + ".")

    def clean_enclosure(self, enclosure):
        """
        Cleans the assigned enclosure and ensures it is suitable for its animals.

        Parameters:
            enclosure (Enclosure): The enclosure being cleaned.
        """
        print(self.name + " starts cleaning the " + enclosure.name + " enclosure.")
        print("After thorough cleaning, the " + enclosure.name + " enclosure is now spotless and safe.")

    def perform_duty(self):
        """
        Describes the zookeeper's daily responsibilities in the zoo.
        This method overrides the abstract method from the Staff class.
        """
        print(self.name + " begins the day by checking the animals' well being.")
        print(self.name + " feeds all assigned animals, refills water supplies, and cleans each enclosure.")
        print("Before finishing, " + self.name + " ensures every animal is healthy and comfortable for the day.")