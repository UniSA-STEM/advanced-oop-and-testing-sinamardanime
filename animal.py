'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Animal:
    """
    Base class for all animals in the zoo.

    Attributes (private):
        __name (str): The animal's name.
        __species (str): The species of the animal.
        __age (int): The age of the animal.
        __diet (str): The dietary preference of the animal.

    Methods:
        get_name(), get_species(), get_age(), get_diet()
        set_age(), set_diet()
        make_sound(), eat(), sleep()
        __str__()
    """

    def __init__(self, name, species, age, diet):
        """
        Constructor for the Animal class.

        Args:
            name (str): The name of the animal.
            species (str): The type/species of the animal.
            age (int): The age of the animal.
            diet (str): The animal's dietary preference.
        """
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet

    def get_name(self):
        """Return the animal's name."""
        return self.__name

    def get_species(self):
        """Return the animal's species."""
        return self.__species

    def get_age(self):
        """Return the animal's age."""
        return self.__age

    def get_diet(self):
        """Return the animal's diet."""
        return self.__diet


    def set_age(self, new_age):
        """Set a new age for the animal."""

        def set_age(self, new_age):
            """
            Set a new age for the animal.
            If the provided value is invalid, a default value of 0 is used.
            """
            if isinstance(new_age, int) and new_age >= 0:
                self.__age = new_age
            else:
                print("Invalid age provided. Defaulting to 0.")
                self.__age = 0

    def set_diet(self, new_diet):
        if isinstance(new_diet, str) and len(new_diet.strip()) > 0:
            self.__diet = new_diet
        else:
            print("Invalid diet provided. Defaulting to 'Unknown'.")
            self.__diet = "Grass"
