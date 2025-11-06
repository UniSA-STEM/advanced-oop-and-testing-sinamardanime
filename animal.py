'''
File: animal.py
Description: A brief description of this Python module.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''

from health_record import HealthRecord

class Animal:
    """
    The Animal class represents a basic animal with attributes such as
    name, species, age, and diet. It ensures data integrity using
    encapsulation and validation through controlled access methods.
    """

    def __init__(self, name, species, age, diet):
        """
        Constructor for the Animal class.

        Parameters:
            name (str): The animal's name.
            species (str): The type/species of the animal.
            age (int): The animal's age (validated).
            diet (str): The animal's dietary preference (validated).

        Note:
            - Name and species are private, accessed only through getters.
            - Age and diet are validated through property setters.
        """
        # Private attributes for data hiding
        self.__name = name
        self.__species = species

        # Use properties for age and diet to apply validation automatically
        self.age = age
        self.diet = diet
        self.__health_records = []


    def get_name(self):
        """
        Return the animal's name.

        Returns:
            str: The name of the animal.
        """
        return self.__name

    def get_species(self):
        """
        Return the animal's species.

        Returns:
            str: The species/type of the animal.
        """
        return self.__species


    def get_age(self):
        """
        Return the animal's age.

        Returns:
            int: The animal's current age.
        """
        return self.__age

    def set_age(self, new_age):
        """
        Set the animal's age with validation.

        Validation:
            - Must be an integer.
            - Must be greater than or equal to 0.

        If invalid, the age defaults to 0.
        """
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            print("Invalid age provided. Defaulting to 0.")
            self.__age = 0

    # Property connection for age
    age = property(get_age, set_age)


    def get_diet(self):
        """
        Return the animal's diet.

        Returns:
            str: The current dietary preference of the animal.
        """
        return self.__diet

    def set_diet(self, new_diet):
        """
        Set the animal's diet with validation.

        Validation:
            - Must be a non-empty string.

        If invalid, defaults to 'Grass'.
        """
        if isinstance(new_diet, str) and len(new_diet.strip()) > 0:
            self.__diet = new_diet
        else:
            print("Invalid diet provided. Defaulting to 'Grass'.")
            self.__diet = "Grass"

    # Property connection for diet
    diet = property(get_diet, set_diet)



    def make_sound(self):
        """
        Simulate the animal making a sound.

        Returns:
            str: A generic sound message.
        """
        return self.__name + " makes a generic animal sound."

    def eat(self):
        """
        Simulate the animal eating its food.

        Returns:
            str: A message showing what the animal is eating.
        """
        return self.__name + " is eating " + self.__diet + "."

    def sleep(self):
        """
        Simulates the animal sleeping.

        Returns:
            str: A message describing the animal sleeping.
        """
        return self.__name + " is sleeping peacefully."

    name = property(get_name)
    species = property(get_species)
    age = property(get_age, set_age)
    diet = property(get_diet, set_diet)



    def add_health_record(self, issue, date_reported, severity, treatment_plan="Pending", notes=""):
        """Adds a new health record for this animal."""
        record = HealthRecord(issue, date_reported, severity, treatment_plan, notes)
        self.__health_records.append(record)
        print(self.__name + "'s health record updated: " + issue)

    def get_health_records(self):
        """Returns all health records."""
        return self.__health_records


    def __str__(self):
        """
        Return a readable summary of the animal’s details.

        Returns:
            str: The formatted animal description.
        """
        return (self.__species + " named " + self.__name + ", Age: " + str(self.__age) + ", Diet: " + self.__diet)








