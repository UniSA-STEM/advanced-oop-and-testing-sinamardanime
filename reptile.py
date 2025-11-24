'''
File: reptile.py
Description: Defines the Reptile class, a subclass of Animal, representing
             cold-blooded creatures like snakes and lizards that have scales
             and may be venomous.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
repository link: https://github.com/UniSA-STEM/advanced-oop-and-testing-sinamardanime.git
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Animal  # Imports the parent Animal class for inheritance


class Reptile(Animal):
    """
    This class represents cold-blooded animals such as snakes, lizards, and crocodiles.
    It inherits from the Animal base class and adds reptile-specific attributes
    and behaviours such as scales, habitat, and venom.
    """

    def __init__(self, name, species, age, diet,
                 scale_type="Smooth", habitat="Desert",
                 is_venomous=False, temperature=30):
        """
        This function initializes a Reptile object by setting both inherited
        Animal attributes and reptile-specific properties.

        Parameters:
            name (str): The reptile’s name.
            species (str): The reptile’s species name.
            age (int): The reptile’s age in years.
            diet (str): The reptile’s diet (e.g., Insects, Rodents).
            scale_type (str): The texture of scales (e.g., Smooth, Rough).
            habitat (str): The natural environment the reptile lives in.
            is_venomous (bool): True if the reptile produces venom.
            temperature (float): The reptile’s body temperature in °C.

        Returns:
            None
        """
        # Call the parent class constructor to initialize shared attributes
        super().__init__(name, species, age, diet)

        # Assign reptile-specific attributes
        self.scale_type = scale_type      # Stores the texture of the reptile’s scales
        self.habitat = habitat            # Stores the reptile’s living environment
        self.is_venomous = is_venomous    # Indicates whether the reptile is venomous
        self.temperature = temperature    # Stores approximate body temperature


    def make_sound(self):
        """
        This function overrides the abstract make_sound() method from Animal.
        It returns the typical sound that reptiles make.

        Returns:
            str: A short description of the reptile’s sound.
        """
        # Return a sentence describing the reptile’s hissing sound
        return self.get_name() + " hisses softly."

    def move(self):
        """
        This function overrides the move() method from the Animal class.
        It describes how reptiles move within their habitat.

        Returns:
            str: A message describing reptile movement.
        """
        # Describes the reptile's slithering or crawling motion
        return self.get_name() + " slithers or crawls across the " + self.habitat.lower() + "."

    def shed_skin(self):
        """
        This function describes a unique reptile behaviour where the reptile
        sheds its old skin to allow growth and remove parasites.

        Returns:
            str: A message describing the shedding process.
        """
        # Indicates that the reptile is currently shedding its skin
        return self.get_name() + " is shedding its old skin to grow a new layer."


    def __str__(self):
        """
        This function returns a descriptive string representation of the reptile.
        It summarises the reptile’s physical characteristics and lifestyle.

        Returns:
            str: A formatted sentence describing the reptile’s details.
        """
        # Determines whether the reptile is venomous or non-venomous
        venom_status = "venomous" if self.is_venomous else "non-venomous"

        # Builds a readable sentence summarising all main details
        return (
            self.get_name() + " is a " + self.get_species() +
            " that lives in the " + self.habitat.lower() + ". " +
            "It has " + self.scale_type.lower() + " scales, is " + venom_status +
            ", and maintains a body temperature around " + str(self.temperature) + "°C. " +
            self.get_name() + " follows a " + self.diet.lower() +
            " diet and is currently " + str(self.age) + " years old."
        )

