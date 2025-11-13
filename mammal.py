'''
File: mammal.py
Description: Defines the Mammal subclass which inherits from the Animal class.
             It represents warm-blooded animals that feed their young with milk
             and includes additional attributes such as fur type, colour, habitat,
             speed, and weight.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Animal


class Mammal(Animal):
    """
    This class represents a mammal in the zoo system.
    Mammals are warm-blooded animals that feed their young with milk and
    typically have fur or hair. This class extends Animal by including
    mammal-specific traits and behaviours.
    """

    # ==========================================================
    # Constructor
    # ==========================================================
    def __init__(self, name, species, age, diet,
                 fur_type="Short", fur_color="Brown",
                 habitat="Grassland", speed=20, weight=50):
        """
        This function initializes a Mammal object by setting both
        the inherited Animal attributes and mammal-specific traits.

        Parameters:
            name (str): The mammal’s name.
            species (str): The species name of the mammal.
            age (int): The mammal’s age in years.
            diet (str): The mammal’s dietary preference (e.g., Meat, Plants).
            fur_type (str): The type of fur the mammal has (default: Short).
            fur_color (str): The colour of the mammal’s fur (default: Brown).
            habitat (str): The environment where the mammal lives (default: Grassland).
            speed (int): The mammal’s top running speed in km/h (default: 20).
            weight (float): The mammal’s body weight in kilograms (default: 50).

        Returns:
            None
        """
        # Initialize attributes inherited from Animal
        super().__init__(name, species, age, diet)

        # Initialize mammal-specific attributes
        self.fur_type = fur_type
        self.fur_color = fur_color
        self.habitat = habitat
        self.speed = speed
        self.weight = weight


    def get_fur_type(self):
        """
        This function returns the mammal’s fur type.

        Returns:
            str: The mammal’s fur type (e.g., Short, Thick, Curly).
        """
        return self.__fur_type

    def set_fur_type(self, new_fur_type):
        """
        This function sets the mammal’s fur type.
        It validates the input and defaults to 'Short' if invalid.

        Parameters:
            new_fur_type (str): The new type of fur to assign.

        Returns:
            None
        """
        if isinstance(new_fur_type, str) and len(new_fur_type.strip()) > 0:
            self.__fur_type = new_fur_type
        else:
            print("Invalid fur type provided. Defaulting to 'Short'.")
            self.__fur_type = "Short"

    fur_type = property(get_fur_type, set_fur_type)


    def get_fur_color(self):
        """
        This function returns the mammal’s fur colour.

        Returns:
            str: The mammal’s fur colour.
        """
        return self.__fur_color

    def set_fur_color(self, new_color):
        """
        This function sets the mammal’s fur colour.
        It validates the input and defaults to 'Brown' if invalid.

        Parameters:
            new_color (str): The new fur colour to assign.

        Returns:
            None
        """
        if isinstance(new_color, str) and len(new_color.strip()) > 0:
            self.__fur_color = new_color
        else:
            print("Invalid colour provided. Defaulting to 'Brown'.")
            self.__fur_color = "Brown"

    fur_color = property(get_fur_color, set_fur_color)


    def get_habitat(self):
        """
        This function returns the mammal’s habitat.

        Returns:
            str: The environment type where the mammal lives.
        """
        return self.__habitat

    def set_habitat(self, new_habitat):
        """
        This function sets the mammal’s habitat and validates it
        against a predefined list of allowed environments.

        Parameters:
            new_habitat (str): The new habitat name to assign.

        Returns:
            None
        """
        # Defines a list of valid habitats where mammals can live
        valid_habitats = ["Grassland", "Savanna", "Savannah", "Forest", "Jungle", "Desert"]

        # Checks if the provided habitat is empty, None, or not a string
        # If any of these conditions are true, the program assigns 'Grassland' by default
        if new_habitat is None or not isinstance(new_habitat, str) or len(new_habitat.strip()) == 0:
            print("Invalid habitat provided. Defaulting to 'Grassland'.")
            self.__habitat = "Grassland"
            return # Exits the function early to avoid further checks

        # Removes extra spaces and capitalize the first letter for consistency
        clean_habitat = new_habitat.strip().capitalize()

        # Checks if the cleaned habitat exists in the valid list
        if clean_habitat in valid_habitats:
            # If it is valid, store it in the private attribute
            self.__habitat = clean_habitat
        else:
            # If invalid, displays a warning and default to 'Grassland'
            print("Invalid habitat provided. Defaulting to 'Grassland'.")
            self.__habitat = "Grassland"

    habitat = property(get_habitat, set_habitat)


    def get_speed(self):
        """
        This function returns the mammal’s running speed.

        Returns:
            float: The speed of the mammal in km/h.
        """
        return self.__speed

    def set_speed(self, new_speed):
        """
        This function sets the mammal’s running speed and validates
        it to ensure it is a positive number.

        Parameters:
            new_speed (float or int): The new speed to assign.

        Returns:
            None
        """
        try:
            # Checks if the new_speed value is a number (int or float)
            if not isinstance(new_speed, (int, float)):
                raise TypeError("Speed must be a number")
            # Checks if the speed is positive (cannot be zero or negative)
            if new_speed <= 0:
                raise ValueError("Speed must be positive")
            # If all checks pass, set the private speed attribute
            self.__speed = new_speed
        except (TypeError, ValueError) as e:
            # This handles any invalid input by printing an error message
            # e stores the specific error raised (TypeError or ValueError)
            print("Invalid speed: " + str(e) + ". Defaulting to 20 km/h.")
            self.__speed = 20

    speed = property(get_speed, set_speed)


    def get_weight(self):
        """
        This function returns the mammal’s body weight.

        Returns:
            float: The mammal’s weight in kilograms.
        """
        return self.__weight

    def set_weight(self, new_weight):
        """
        This function sets the mammal’s body weight.

        Parameters:
            new_weight (float): The new weight in kilograms.

        Returns:
            None
        """
        self.__weight = new_weight

    weight = property(get_weight, set_weight)


    def make_sound(self):
        """
        This function overrides the abstract make_sound method from the Animal class.
        It returns the specific sound made by a mammal.

        Returns:
            str: A string describing the mammal’s sound.
        """
        return self.get_name() + " growls and purrs."

    def feed_young(self):
        """
        This function describes a unique mammal behaviour where the mammal
        feeds its young with milk.

        Returns:
            str: A message describing the mammal feeding its young.
        """
        return self.get_name() + " is feeding its young baby with milk."

    def move(self):
        """
        This function overrides the abstract move method from the Animal class.
        It describes how a mammal moves within its environment.

        Returns:
            str: A message describing the mammal’s movement speed and habitat.
        """
        return self.get_name() + " moves at " + str(self.__speed) + " km/h through the " + self.__habitat + "."


    def __str__(self):
        """
        This function returns a descriptive sentence summarising
        the mammal’s details in a readable format.

        Returns:
            str: A formatted string describing the mammal’s key attributes.
        """
        return (
            f"{self.get_name()} is a {self.get_species()} that lives in the {self.__habitat}. "
            f"It has {self.__fur_color.lower()} {self.__fur_type.lower()} fur, "
            f"moves at around {self.__speed} km/h, weighs about {self.__weight} kg, "
            f"and follows a {self.diet.lower()} diet. "
            f"{self.get_name()} is currently {self.age} years old."
        )
