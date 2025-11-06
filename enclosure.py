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
        pass


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