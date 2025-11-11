'''
File: enclosure.py
Description: Defines the Enclosure class which manages zoo animal habitats.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:
    """
    The Enclosure class represents an area in the zoo that houses animals
    of a compatible type and environment.
    """

    def __init__(self, name, environment_type, size=100, cleanliness=100):
        # Initialize private attributes directly
        self.__name = name
        self.__environment_type = environment_type
        self.__size = size
        self.__cleanliness = cleanliness
        self.__animals = []  # always private

    # ====== Property: name ======
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            print("Invalid name. Defaulting to 'Unnamed Enclosure'.")
            self.__name = "Unnamed Enclosure"

    name = property(get_name, set_name)

    # ====== Property: environment_type ======
    def get_environment_type(self):
        return self.__environment_type

    def set_environment_type(self, new_env):
        if isinstance(new_env, str) and len(new_env.strip()) > 0:
            self.__environment_type = new_env
        else:
            print("Invalid environment type. Defaulting to 'General'.")
            self.__environment_type = "General"

    environment_type = property(get_environment_type, set_environment_type)

    # ====== Property: size ======
    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        if isinstance(new_size, (int, float)) and new_size > 0:
            self.__size = new_size
        else:
            print("Invalid size. Defaulting to 100.")
            self.__size = 100

    size = property(get_size, set_size)

    # ====== Property: cleanliness ======
    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, new_clean):
        if isinstance(new_clean, (int, float)) and 0 <= new_clean <= 100:
            self.__cleanliness = new_clean
        else:
            print("Invalid cleanliness. Defaulting to 100.")
            self.__cleanliness = 100

    cleanliness = property(get_cleanliness, set_cleanliness)

    # ====== Property: animals ======
    def get_animals(self):
        return self.__animals

    animals = property(get_animals)

    # ====== Methods ======
    def add_animal(self, animal):
        """Adds an animal with exception handling."""
        try:
            from animal import Animal
            if not isinstance(animal, Animal):
                raise TypeError("Object must be an Animal instance")

            if animal not in self.__animals:
                if animal.get_health_records():
                    for record in animal.get_health_records():
                        if record.treatment_plan.lower() == "pending":
                            raise ValueError(f"{animal.get_name()} is under treatment")
                self.__animals.append(animal)
                print(f"{animal.get_name()} has been added to {self.__name}.")
            else:
                print(f"{animal.get_name()} is already in {self.__name}.")

        except ValueError as e:
            print(f"Cannot add animal: {e}")
        except TypeError as e:
            print(f"Invalid animal object: {e}")
        except Exception as e:
            print(f"Unexpected error adding animal: {e}")

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal.get_name()} has been removed from the {self.__name} enclosure.")
        else:
            print(f"{animal.get_name()} is not found in the {self.__name} enclosure.")

    def report_status(self):
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

    def clean_enclosure(self):
        """
        Simulates cleaning the enclosure by increasing cleanliness level.
        """
        if self.__cleanliness < 100:
            self.__cleanliness += 10
            if self.__cleanliness > 100:
                self.__cleanliness = 100
            print("The " + self.__name + " enclosure has been cleaned and is now spotless.")
        else:
            print("The " + self.__name + " enclosure is already perfectly clean.")


