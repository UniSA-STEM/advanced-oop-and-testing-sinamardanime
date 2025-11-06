'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Enclosure:
    """
    The Enclosure class represents a specific area within the zoo that houses
    animals of a compatible type and environment. It tracks size, environment type,
    cleanliness level, and the animals it contains.
    """

    def __init__(self, name, environment_type, size=100, cleanliness=100):
        self.name = name
        self.environment_type = environment_type
        self.size = size
        self.cleanliness = cleanliness
        self.__animals = []


    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            print("Invalid name. Defaulting to 'Unnamed Enclosure'.")
            self.__name = "Unnamed Enclosure"

    name = property(get_name, set_name)


    def get_environment_type(self):
        return self.__environment_type

    def set_environment_type(self, new_env):
        if isinstance(new_env, str) and len(new_env.strip()) > 0:
            self.__environment_type = new_env
        else:
            print("Invalid environment type. Defaulting to 'General'.")
            self.__environment_type = "General"

    environment_type = property(get_environment_type, set_environment_type)



   def get_size(self):
        return self.__size

    def set_size(self, new_size):
        if isinstance(new_size, (int, float)) and new_size > 0:
            self.__size = new_size
        else:
            print("Invalid size. Defaulting to 100.")
            self.__size = 100

    size = property(get_size, set_size)


    def get_cleanliness(self):
        return self.__cleanliness


    def set_cleanliness(self, new_clean):
        if isinstance(new_clean, (int, float)) and 0 <= new_clean <= 100:
            self.__cleanliness = new_clean
        else:
            print("Invalid cleanliness. Defaulting to 100.")
            self.__cleanliness = 100


    cleanliness = property(get_cleanliness, set_cleanliness)


    def get_animals(self):
        """Returns a list of animals currently in the enclosure."""
        return self.__animals


    animals = property(get_animals)


def add_animal(self, animal):
    """
    Adds an animal to the enclosure if it's not already inside.
    Parameters:
        animal (Animal): The animal to add.
    """
    if animal not in self.__animals:
        self.__animals.append(animal)
        print(animal.name + " has been added to the " + self.__name + " enclosure.")
    else:
        print(animal.name + " is already in the " + self.__name + " enclosure.")


 def remove_animal(self, animal):
        """
        Removes an animal from the enclosure.
        Parameters:
            animal (Animal): The animal to remove.
        """
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(animal.name + " has been removed from the " + self.__name + " enclosure.")
        else:
            print(animal.name + " is not found in the " + self.__name + " enclosure.")