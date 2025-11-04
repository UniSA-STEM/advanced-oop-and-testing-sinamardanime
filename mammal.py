





from animal import Animal

class Mammal(Animal):
    """
    The Mammal class represents animals that are warm-blooded and
    feed their young with milk. It inherits all attributes and
    behaviours from the Animal class and adds mammal-specific features.
    """

    def __init__(self, name, species, age, diet, fur_type="Short"):
        """
        Constructor for the Mammal subclass.

        Parameters:
            name (str): The mammal's name.
            species (str): The mammal's species.
            age (int): The mammal's age.
            diet (str): The mammal's dietary preference.
            fur_type (str): The type of fur the mammal has.
        """
        super().__init__(name, species, age, diet)
        self.__fur_type = fur_type

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
