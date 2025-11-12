'''
File: staff.py
Description: Defines the abstract Staff class which represents all staff
             members working in the zoo. This includes shared attributes and
             behaviours common to roles such as Zookeeper or Veterinarian.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from abc import ABC, abstractmethod  # Import ABC tools for abstract class creation


class Staff(ABC):
    """
    This class represents a general staff member in the zoo.
    It acts as an abstract base class (ABC), meaning it cannot be directly instantiated.
    Subclasses such as Zookeeper and Veterinarian must inherit from this class
    and implement the abstract perform_duty() method.
    """


    def __init__(self, name, role):
        """
        This function initializes a Staff object with a name, role,
        and empty lists for assigned animals and enclosures.

        Parameters:
            name (str): The full name of the staff member.
            role (str): The position or role title (e.g., Zookeeper, Veterinarian).

        Returns:
            None
        """
        self.__name = name                     # Stores the staff member’s name
        self.__role = role                     # Stores the staff member’s role title
        self.__assigned_animals = []           # Keeps track of animals assigned to the staff member
        self.__assigned_enclosures = []        # Keeps track of enclosures assigned to the staff member


    def get_name(self):
        """
        This function returns the name of the staff member.

        Returns:
            str: The staff member’s name.
        """
        return self.__name

    def get_role(self):
        """
        This function returns the job title or role of the staff member.

        Returns:
            str: The role (e.g., Zookeeper, Veterinarian).
        """
        return self.__role

    def get_assigned_animals(self):
        """
        This function returns a list of animals assigned to the staff member.

        Returns:
            list: The animals this staff member is responsible for.
        """
        return self.__assigned_animals

    def get_assigned_enclosures(self):
        """
        This function returns a list of enclosures assigned to the staff member.

        Returns:
            list: The enclosures this staff member manages or supervises.
        """
        return self.__assigned_enclosures

    # Create read-only properties so that these values
    # can be accessed directly but not modified externally.
    name = property(get_name)
    role = property(get_role)
    assigned_animals = property(get_assigned_animals)
    assigned_enclosures = property(get_assigned_enclosures)


    def assign_animal(self, animal):
        """
        This function assigns an animal to the staff member’s responsibility list.
        It prevents duplicate entries.

        Parameters:
            animal (Animal): The animal object to be assigned.

        Returns:
            None
        """
        # Check if the animal is not already assigned before adding
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)  # Add the animal to the list



    def assign_enclosure(self, enclosure):
        """
        This function assigns an enclosure to the staff member’s responsibility list.
        It prevents duplicate entries.

        Parameters:
            enclosure (Enclosure): The enclosure object to be assigned.

        Returns:
            None
        """
        # Check if the enclosure is not already assigned before adding
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)  # Add the enclosure to the list




    @abstractmethod
    def perform_duty(self):
        """
        This function defines an abstract method that each subclass must override.
        It describes the daily tasks performed by the staff member depending on their role.

        Returns:
            None
        """
        pass  # Each subclass (e.g., Zookeeper, Veterinarian) will define this behaviour
