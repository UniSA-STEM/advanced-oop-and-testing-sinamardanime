'''
File: enclosure.py
Description: Defines the Enclosure class which manages animal habitats in the zoo.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
repository link: https://github.com/UniSA-STEM/advanced-oop-and-testing-sinamardanime.git
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal
from bird import Bird
from reptile import Reptile


class Enclosure:
    """
    This class represents a zoo enclosure that houses animals of compatible
    types in a safe and controlled environment.
    """

    def __init__(self, name: str, environment_type: str, size: int = 100, cleanliness: int = 100):
        """
        This function initializes a new Enclosure object and sets its core attributes.

        Parameters:
            name (str): The name of the enclosure.
            environment_type (str): The type of environment (e.g., Savannah, Forest, Rainforest).
            size (int): The total size of the enclosure in square meters.
            cleanliness (int): The cleanliness level of the enclosure (0–100).

        Returns:
            None
        """
        self.__name = name
        self.__environment_type = environment_type
        self.__size = size
        self.__cleanliness = cleanliness
        self.__animals = []  # A list that stores Animal objects

    def get_name(self) -> str:
        """
        This function returns the name of the enclosure.

        Returns:
            str: The enclosure's name.
        """
        return self.__name

    def set_name(self, new_name: str) -> None:
        """
        This function sets or updates the name of the enclosure.
        If the input is invalid, it defaults to 'Unnamed Enclosure'.

        Parameters:
            new_name (str): The new name to assign.

        Returns:
            None
        """
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            print("Invalid name. Defaulting to 'Unnamed Enclosure'.")
            self.__name = "Unnamed Enclosure"

    name = property(get_name, set_name)

    def get_environment_type(self) -> str:
        """
        This function returns the environment type of the enclosure.

        Returns:
            str: The environment type (e.g., Savannah, Forest, Rainforest).
        """
        return self.__environment_type

    def set_environment_type(self, new_env: str) -> None:
        """
        This function updates the environment type of the enclosure.
        If invalid, it defaults to 'General'.

        Parameters:
            new_env (str): The new environment type.

        Returns:
            None
        """
        if isinstance(new_env, str) and len(new_env.strip()) > 0:
            self.__environment_type = new_env
        else:
            print("Invalid environment type. Defaulting to 'General'.")
            self.__environment_type = "General"

    environment_type = property(get_environment_type, set_environment_type)

    def get_size(self) -> float:
        """
        This function returns the total size of the enclosure.

        Returns:
            float: The size in square meters.
        """
        return self.__size

    def set_size(self, new_size: float) -> None:
        """
        This function sets or updates the size of the enclosure.
        If invalid, it defaults to 100.

        Parameters:
            new_size (float): The new size value in square meters.

        Returns:
            None
        """
        if isinstance(new_size, (int, float)) and new_size > 0:
            self.__size = new_size
        else:
            print("Invalid size. Defaulting to 100.")
            self.__size = 100

    size = property(get_size, set_size)

    def get_cleanliness(self) -> float:
        """
        This function returns the current cleanliness level of the enclosure.

        Returns:
            float: A value between 0 and 100.
        """
        return self.__cleanliness

    def set_cleanliness(self, new_clean: float) -> None:
        """
        This function updates the cleanliness level of the enclosure.
        If invalid, it defaults to 100.

        Parameters:
            new_clean (float): A number between 0 and 100.

        Returns:
            None
        """
        if isinstance(new_clean, (int, float)) and 0 <= new_clean <= 100:
            self.__cleanliness = new_clean
        else:
            print("Invalid cleanliness. Defaulting to 100.")
            self.__cleanliness = 100

    cleanliness = property(get_cleanliness, set_cleanliness)

    def get_animals(self) -> list:
        """
        This function returns the list of animals currently in the enclosure.

        Returns:
            list: A list containing Animal objects.
        """
        return self.__animals

    animals = property(get_animals)

    def add_animal(self, animal) -> None:
        """
        This function adds an animal to the enclosure only if its type matches
        the correct environment.

        Parameters:
            animal (Animal): The animal object to add.

        Returns:
            None
        """
        try:
            # Check that animal type suits the enclosure environment
            if isinstance(animal, Mammal) and self.__environment_type.lower() != "savannah":
                print(animal.get_name() + " the " + animal.get_species() +
                      " cannot live in a " + self.__environment_type + " enclosure.")
                return

            elif isinstance(animal, Bird) and self.__environment_type.lower() != "forest":
                print(animal.get_name() + " the " + animal.get_species() +
                      " cannot live in a " + self.__environment_type + " enclosure.")
                return

            elif isinstance(animal, Reptile) and self.__environment_type.lower() != "rainforest":
                print(animal.get_name() + " the " + animal.get_species() +
                      " cannot live in a " + self.__environment_type + " enclosure.")
                return

            # Add animal if all checks pass
            self.__animals.append(animal)
            print(animal.get_name() + " has been added to the " + self.__name + " enclosure.")

        except Exception as e:
            print("Error while adding animal: " + str(e))

    def remove_animal(self, animal) -> None:
        """
        This function removes an animal from the enclosure if it exists.

        Parameters:
            animal (Animal): The animal object to remove.

        Returns:
            None
        """
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal.get_name()} has been removed from the {self.__name} enclosure.")
        else:
            print(f"{animal.get_name()} is not found in the {self.__name} enclosure.")

    def report_status(self) -> None:
        """
        This function prints a full report of the enclosure’s current state,
        including environment type, size, cleanliness, and a list of housed animals.

        Returns:
            None
        """
        print("\nEnclosure Report:")
        print(f"Name: {self.__name}")
        print(f"Environment Type: {self.__environment_type}")
        print(f"Size: {self.__size} m²")
        print(f"Cleanliness Level: {self.__cleanliness}%")

        if self.__animals:
            print("Animals currently in this enclosure:")
            for animal in self.__animals:
                print(f"- {animal.get_name()} ({animal.get_species()})")
        else:
            print("No animals are currently housed here.")

    def clean_enclosure(self) -> None:
        """
        This function simulates cleaning of the enclosure by increasing
        the cleanliness level by 10%, up to a maximum of 100%.

        Returns:
            None
        """
        if self.__cleanliness < 100:
            self.__cleanliness += 10
            if self.__cleanliness > 100:
                self.__cleanliness = 100
            print("The " + self.__name + " enclosure has been cleaned and is now spotless.")
        else:
            print("The " + self.__name + " enclosure is already perfectly clean.")
