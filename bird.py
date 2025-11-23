'''
File: bird.py
Description: This file Defines the Bird class, a subclass of Animal, representing feathered creatures such as parrots and eagles.
             It extends Animal by including bird-specific traits like wingspan, flight ability, beak type, and song.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Animal

"""
   Represents a bird species that inherits from the Animal base class.

   This class adds specific traits such as wingspan, flight ability,
   beak type, song, and weight. It overrides the abstract methods
   from Animal to describe how birds make sounds and move.
   """
class Bird(Animal):

    def __init__(self, name, species, age, diet, wing_span=1.0, can_fly=True, beak_type="Short", song_type="Chirp", weight=1.0):
        """
        This function Initialises a new Bird object with its general and bird-specific attributes.

        Parameters:
            name (str): The bird’s name.
            species (str): The species of the bird (e.g., Parrot, Eagle).
            age (int): The bird’s current age.
            diet (str): The bird’s dietary preference (e.g., Seeds, Insects).
            wing_span (float): The wingspan in meters.
            can_fly (bool): Whether the bird is capable of flight.
            beak_type (str): The type of beak the bird has (e.g., Curved, Hooked).
            song_type (str): The sound or melody the bird makes.
            weight (float): The weight of the bird in kilograms.

        Returns:
            None
        """
        # Initialises inherited attributes from Animal
        super().__init__(name, species, age, diet)

        # Initialises bird-specific attributes
        self.wing_span = wing_span
        self.can_fly = can_fly
        self.beak_type = beak_type
        self.song_type = song_type
        self.weight = weight

    def get_wing_span(self) -> float:
        """
        Returns the bird’s wingspan in meters.

        Returns:
            float: The bird’s wingspan.
        """
        return self.__wing_span

    def set_wing_span(self, new_span: float) -> None:
        """
        Sets the bird’s wingspan with validation.

        Parameters:
            new_span (float): The new wingspan in meters.

        Returns:
            None
        """
        self.__wing_span = new_span

    wing_span = property(get_wing_span, set_wing_span)


    def get_can_fly(self) -> bool:
        """
        This function Returns whether the bird can fly.

        Returns:
            bool: True if the bird can fly, otherwise False.
        """
        return self.__can_fly

    def set_can_fly(self, new_status: bool) -> None:
        """
       This function sets whether the bird can fly.

        Parameters:
            new_status (bool): True if bird can fly, otherwise False.

        Returns:
            None
        """
        self.__can_fly = new_status

    can_fly = property(get_can_fly, set_can_fly)


    def get_beak_type(self) -> str:
        """
        This function returns the type of beak the bird has.

        Returns:
            str: The bird’s beak type (e.g., Curved, Short).
        """
        return self.__beak_type

    def set_beak_type(self, new_type: str) -> None:
        """
        This function sets the bird’s beak type.

        Parameters:
            new_type (str): The new beak type to assign.

        Returns:
            None
        """
        self.__beak_type = new_type

    beak_type = property(get_beak_type, set_beak_type)


    def get_song_type(self) -> str:
        """
        This function returns the bird’s song or sound type.

        Returns:
            str: The bird’s song type (e.g., Chirp, Tweet).
        """
        return self.__song_type

    def set_song_type(self, new_song: str) -> None:
        """
        This function sets the bird’s song type.

        Parameters:
            new_song (str): The sound or melody produced by the bird.

        Returns:
            None
        """
        self.__song_type = new_song

    song_type = property(get_song_type, set_song_type)


    def get_weight(self) -> float:
        """
        This function returns the bird’s weight in kilograms.

        Returns:
            float: The bird’s weight.
        """
        return self.__weight

    def set_weight(self, new_weight: float) -> None:
        """
        This function Sets the bird’s body weight.

        Parameters:
            new_weight (float): The new weight of the bird.

        Returns:
            None
        """
        self.__weight = new_weight

    weight = property(get_weight, set_weight)


    def make_sound(self) -> str:
        """
        This function overrides the Animal abstract method.
        Returns the sound or song made by this bird.

        Returns:
            str: A message describing the bird’s sound.
        """
        return self.get_name() + " sings a " + self.__song_type.lower() + " tune."

    def move(self) -> str:
        """
        This function overrides the Animal abstract method.
        Describes how the bird moves depending on its ability to fly.

        Returns:
            str: A message describing the bird’s movement.
        """
        if self.__can_fly:
            return f"{self.get_name()} flies gracefully across the sky."
        else:
            return f"{self.get_name()} hops or walks on the ground."


    def fly(self) -> str:
        """
        This function describes the bird’s flying behavior based on flight capability.

        Returns:
            str: A message describing how the bird moves through the air.
        """
        if self.__can_fly:
            return (self.get_name() + " soars gracefully with a wingspan of " +
                    str(self.__wing_span) + " meters.")
        else:
            return (self.get_name() + " cannot fly and prefers to hop or walk.")

    def __str__(self):
        """
               Returns a formatted description of the bird’s key details.

               Returns:
                   str: A readable string summarizing the bird’s characteristics.
               """

        flight_status = "can fly" if self.__can_fly else "cannot fly"
        return (
            self.get_name() + " is a " + self.get_species() +
            " that " + flight_status + ". " +
            "It has a " + self.__beak_type.lower() + " beak, a wingspan of " + str(self.__wing_span) +
            " meters, and weighs around " + str(self.__weight) + " kg. " +
            self.get_name() + " follows a " + self.diet.lower() + " diet and sings a " +
            self.__song_type.lower() + " melody. " +
            "It is currently " + str(self.age) + " years old."
        )
