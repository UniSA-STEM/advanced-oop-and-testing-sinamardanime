'''
File: reptile.py
Description: Defines the Reptile class, a subclass of Animal, representing cold-blooded creatures like snakes and lizards.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    """
    The Reptile class represents cold-blooded animals such as snakes or lizards.
    It inherits from the Animal base class and adds reptile-specific attributes
    and behaviors.
    """

    def __init__(self, name, species, age, diet, scale_type="Smooth", habitat="Desert", is_venomous=False, temperature=30):
        """
        Constructor for the Reptile subclass.

        Parameters:
            name (str): The reptile's name.
            species (str): The reptile's species.
            age (int): The reptile's age.
            diet (str): The reptile's dietary preference.
            scale_type (str): The type of scales (e.g., smooth, rough).
            habitat (str): The environment the reptile lives in.
            is_venomous (bool): Whether the reptile is venomous.
            temperature (float): The body temperature (approximate).
        """
        super().__init__(name, species, age, diet)
        self.scale_type = scale_type
        self.habitat = habitat
        self.is_venomous = is_venomous
        # === Methods ===

    def make_sound(self):
        """Override make_sound for reptiles."""
        return self.get_name() + " hisses softly."

    def move(self):
        """Describe reptile movement."""
        return self.get_name() + " slithers or crawls across the " + self.habitat.lower() + "."

    def shed_skin(self):
        """Unique reptile behaviour."""
        return self.get_name() + " is shedding its old skin to grow a new layer."

    def __str__(self):
        """Return a detailed description of the reptile."""
        venom_status = "venomous" if self.is_venomous else "non-venomous"
        return (
                self.get_name() + " is a " + self.get_species() +
                " that lives in the " + self.habitat.lower() + ". " +
                "It has " + self.scale_type.lower() + " scales, is " + venom_status +
                ", and maintains a body temperature around " + str(self.temperature) + "°C. " +
                self.get_name() + " follows a " + self.diet.lower() +
                " diet and is currently " + str(self.age) + " years old."
        )