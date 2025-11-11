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