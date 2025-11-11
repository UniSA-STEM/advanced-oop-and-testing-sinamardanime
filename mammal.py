





from animal import Animal

class Mammal(Animal):
    """
    The Mammal class represents animals that are warm-blooded and
    feed their young with milk. It inherits all attributes and
    behaviours from the Animal class and adds mammal-specific traits.
    """

    def __init__(self, name, species, age, diet, fur_type="Short", fur_color="Brown", habitat="Grassland", speed=20, weight=50):
        """
        Constructor for the Mammal subclass.

        Parameters:
            name (str): The mammal's name.
            species (str): The mammal's species.
            age (int): The mammal's age.
            diet (str): The mammal's dietary preference.
            fur_type (str): The type of fur the mammal has.
            fur_color (str): The colour of the mammal's fur.
            habitat (str): The type of environment the mammal lives in.
            speed (int): The mammal's top running speed (km/h).
        """
        super().__init__(name, species, age, diet)
        self.fur_type = fur_type
        self.fur_color = fur_color
        self.habitat = habitat
        self.speed = speed
        self.weight = weight

    def get_fur_type(self):
        """Return the mammal's fur type."""
        return self.__fur_type

    def set_fur_type(self, new_fur_type):
        """Set a new fur type for the mammal, defaults to 'Short' if invalid."""
        if isinstance(new_fur_type, str) and len(new_fur_type.strip()) > 0:
            self.__fur_type = new_fur_type
        else:
            print("Invalid fur type provided. Defaulting to 'Short'.")
            self.__fur_type = "Short"

    fur_type = property(get_fur_type, set_fur_type)

    def get_fur_color(self):
        """Return the mammal's fur colour."""
        return self.__fur_color

    def set_fur_color(self, new_color):
        """Set the mammal's fur colour, defaults to 'Brown' if invalid."""
        if isinstance(new_color, str) and len(new_color.strip()) > 0:
            self.__fur_color = new_color
        else:
            print("Invalid color provided. Defaulting to 'Brown'.")
            self.__fur_color = "Brown"

    fur_color = property(get_fur_color, set_fur_color)

    def get_habitat(self):
        """Return the mammal's habitat."""
        return self.__habitat

    def set_habitat(self, new_habitat):
        valid_habitats = ["Grassland", "Savanna", "Savannah", "Forest", "Jungle", "Desert"]

        # Handle None or empty string
        if new_habitat is None or not isinstance(new_habitat, str) or len(new_habitat.strip()) == 0:
            print("Invalid habitat provided. Defaulting to 'Grassland'.")
            self.__habitat = "Grassland"
            return

        clean_habitat = new_habitat.strip().capitalize()

        if clean_habitat in valid_habitats:
            self.__habitat = clean_habitat
        else:
            print("Invalid habitat provided. Defaulting to 'Grassland'.")
            self.__habitat = "Grassland"

    habitat = property(get_habitat, set_habitat)

    def get_speed(self):
        """Return the mammal's speed."""
        return self.__speed

    def set_speed(self, new_speed):
        """Set the mammal's speed with exception handling."""
        try:
            if not isinstance(new_speed, (int, float)):
                raise TypeError("Speed must be a number")
            if new_speed <= 0:
                raise ValueError("Speed must be positive")
            self.__speed = new_speed
        except (TypeError, ValueError) as e:
            print("Invalid speed: " + str(e) + ". Defaulting to 20 km/h.")
            self.__speed = 20

    speed = property(get_speed, set_speed)

    speed = property(get_speed, set_speed)

    def make_sound(self):
        """Override the make_sound method for mammals."""
        return self.get_name() + " growls and purrs."

    def feed_young(self):
        """Unique behaviour for mammals."""
        return self.get_name() + " is feeding its young baby with milk."

    def move(self):
        """Describe how the mammal moves."""
        return self.get_name() + " runs moves " + str(self.__speed) + " km/h through the " + self.__habitat + "."


    def get_weight(self):
        """Return the mammal's body weight."""
        return self.__weight

    def set_weight(self, new_weight):
        """Set the mammal's body weight."""
        self.__weight = new_weight

    weight = property(get_weight, set_weight)

    def __str__(self):
        """Return a descriptive sentence summarising the mammal’s details."""
        return (
                self.get_name() + " is a " + self.get_species() +
                " that lives in the " + self.__habitat + ". " +
                "It has " + self.__fur_color.lower() + " " + self.__fur_type.lower() +
                " fur, moves at around " + str(self.__speed) + " km/h, " +
                "weighs about " + str(self.__weight) + " kg, " +
                "and follows a " + self.diet.lower() + " diet. " +
                self.get_name() + " is also currently " + str(self.age) + " years old."
        )

