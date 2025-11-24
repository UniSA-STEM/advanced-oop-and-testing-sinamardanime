'''
File: animal.py
Description: Contains the abstract Animal class and core functionality
             for managing animal attributes, behaviour, and health records.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
repository link: https://github.com/UniSA-STEM/advanced-oop-and-testing-sinamardanime.git
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
from health_record import HealthRecord

class Animal(ABC):
    """
       The Animal class represents a general animal in the zoo.

       It defines shared attributes such as name, species, age, and diet.
       It also includes functionality for basic animal behaviors like eating,
       sleeping, and managing health records.

       This class is abstract and must be subclassed by specific animal types
       (e.g., Mammal, Bird, Reptile) which implement their own sound and movement behaviors.
       """

    def __init__(self, name, species, age, diet):
        """
               Initialises a new Animal object and validates the given attributes.

               Parameters:
                   name (str): The animal’s name (private attribute).
                   species (str): The species or type of the animal (private attribute).
                   age (int): The animal’s current age. Must be a non-negative integer.
                   diet (str): The animal’s dietary preference (e.g., Carnivore, Herbivore).

               Returns:
                   None
               """
        # Private attributes for encapsulation (cannot be accessed directly)
        self.__name = name
        self.__species = species

        # Uses properties to apply validation automatically through setters
        self.age = age
        self.diet = diet
        # Initialises an empty list to store the animal's health records
        self.__health_records = []


    def get_name(self) -> str:
        """
        Returns the animal's name.

        Returns:
            Str: The current name of the animal.
        """
        return self.__name # Returns the private attribute __name

    def get_species(self)  -> str:
         """
        Returns the animal’s species.

        Returns:
            str: The type or species of the animal.
        """
         return self.__species


    def get_age(self) -> int:
        """
        Return the animal's age.

        Returns:
            int: The animal's current age.
        """
        return self.__age

    """
 This function Validates and sets the animal’s age.

 Parameters:
     new_age (int): The new age to assign to the animal.

 Validation Rules:
     - Must be an integer value.
     - Must be greater than or equal to 0.
     - If invalid, defaults to 0.

 Returns:
     None
 """
    def set_age(self, new_age) -> None:


        # Checks if new_age is valid
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            # If it is  invalid, set a default safe value and warn the user
            print("Invalid age provided. Defaulting to 0.")
            self.__age = 0




    def get_diet(self) -> str:
        """
               Returns the animal’s dietary preference.

               Returns:
                   str: The diet type (e.g., Carnivore, Herbivore, Omnivore).
               """
        return self.__diet

    def set_diet(self, new_diet)  -> None:
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



    @abstractmethod
    def make_sound(self) -> str:
        """
        Represents how the animal makes a sound.

        This method is abstract and must be overridden by all subclasses
        to define unique sound behavior (e.g., roar, chirp, hiss).

        Returns:
            str: A description of the animal’s sound.
        """
        pass

    @abstractmethod
    def move(self) -> str:
        """
        Represents how the animal moves.

        This method is abstract and must be implemented in all subclasses
        to describe specific movement styles (e.g., runs, flies, slithers).

        Returns:
            str: A message describing the animal’s movement behavior.
             """
        pass

    def eat(self) -> str:
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
    # this section defines the properties, which link the getters and setter methods to the actual attribute name
    name = property(get_name)
    species = property(get_species)
    age = property(get_age, set_age)
    diet = property(get_diet, set_diet)

    """
           Adds a new health record entry for this animal.

           Parameters:
               issue (str): The health problem or diagnosis.
               date_reported (str): The date the issue was first recorded.
               severity (str): The seriousness of the issue (e.g., Low, Medium, High).
               treatment_plan (str): The suggested plan or status of treatment.
               notes (str): Optional notes about the issue or progress.

           Returns:
               None
           """
    def add_health_record(self, issue, date_reported, severity, treatment_plan="Pending", notes="") -> None:

        # Creates a HealthRecord object and add it to the internal list
        record = HealthRecord(issue, date_reported, severity, treatment_plan, notes)
        self.__health_records.append(record)
        # Prints confirmation for user feedback
        print(self.__name + "'s health record updated: " + issue)

    def get_health_records(self) -> list:
        """
        Returns all health records associated with this animal.

        Returns:
            list: A list of HealthRecord objects stored for this animal.
        """
        return self.__health_records

    def display_health_records(self) -> None:


         # Checks if there are any records to display
        if self.__health_records:
            print("\nHealth Records for " + self.__name + ":")
            for record in self.__health_records:
                print(" - " + str(record))
        else:
            print("\nNo health issues recorded for " + self.__name + ".")

    def __str__(self):
        """
        Returns a formatted string representation of the animal’s details.

         Purpose:
                Helps display animal details clearly when printed or logged.

        Returns:
                str: The formatted description containing species, name, age, and diet.
        """
        return (self.__species + " named " + self.__name + ", Age: " + str(self.__age) + ", Diet: " + self.__diet)








