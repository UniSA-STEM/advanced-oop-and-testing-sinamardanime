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
        Constructor for the Animal class.
            name (str): The name of the animal.
            species (str): The type/species of the animal.
            age (int): The age of the animal.
            diet (str): The animal's dietary preference.
        """

    def __init__(self, name, species, age, diet):
        # Use property assignments so validation is applied
        self.__name = name  # read-only, can be private
        self.__species = species  # read-only, can be private
        self.age = age  # uses the property setter
        self.diet = diet  # uses the property setter



    def get_name(self):
        """Return the animal's name."""
        return self.__name

    def get_species(self):
        """Return the animal's species."""
        return self.__species


    def get_age(self):
        """Return the animal's age."""
        return self.__age


    def set_age(self, new_age):
        """
        Validate and set the animal's age.
        If invalid, defaults to 0.
         """
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            print("Invalid age provided. Defaulting to 0.")
            self.__age = 0

    age = property(get_age, set_age)



    def get_diet(self):
        """Return the animal's diet."""
        return self.__diet

    def set_diet(self, new_diet):
        if isinstance(new_diet, str) and len(new_diet.strip()) > 0:
            self.__diet = new_diet
        else:
            print("Invalid diet provided. Defaulting to 'Unknown'.")
            self.__diet = "Grass"

    diet = property(get_diet, set_diet)