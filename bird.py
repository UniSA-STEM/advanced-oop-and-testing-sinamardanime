from animal import Animal

class Bird(Animal):
    """
    The Bird class represents animals that have feathers, lay eggs,
    and may have the ability to fly. It inherits from the Animal class
    and adds bird-specific traits.
    """

    def __init__(self, name, species, age, diet, wing_span=1.0, can_fly=True, beak_type="Short", song_type="Chirp", weight=1.0):
        """
        Constructor for the Bird subclass.

        Parameters:
            name (str): The bird's name.
            species (str): The bird's species.
            age (int): The bird's age.
            diet (str): The bird's dietary preference.
            wing_span (float): The bird's wingspan in meters.
            can_fly (bool): Whether the bird can fly.
            beak_type (str): The type of beak the bird has.
            song_type (str): The sound or song the bird makes.
            weight (float): The bird's weight in kilograms.
        """
        super().__init__(name, species, age, diet)
        self.wing_span = wing_span
        self.can_fly = can_fly
        self.beak_type = beak_type
        self.song_type = song_type
        self.weight = weight

    def get_wing_span(self):
        """Return the bird's wingspan."""
        return self.__wing_span

    def set_wing_span(self, new_span):
        """Set the bird's wingspan."""
        self.__wing_span = new_span

    wing_span = property(get_wing_span, set_wing_span)

    def get_can_fly(self):
        """Return whether the bird can fly."""
        return self.__can_fly

    def set_can_fly(self, new_status):
        """Set whether the bird can fly."""
        self.__can_fly = new_status

    can_fly = property(get_can_fly, set_can_fly)

    def get_beak_type(self):
        """Return the bird's beak type."""
        return self.__beak_type

    def set_beak_type(self, new_type):
        """Set the bird's beak type."""
        self.__beak_type = new_type

    beak_type = property(get_beak_type, set_beak_type)

    def get_song_type(self):
        """Return the bird's song type."""
        return self.__song_type

    def set_song_type(self, new_song):
        """Set the bird's song type."""
        self.__song_type = new_song

    song_type = property(get_song_type, set_song_type)

    def get_weight(self):
        """Return the bird's weight."""
        return self.__weight

    def set_weight(self, new_weight):
        """Set the bird's weight."""
        self.__weight = new_weight

    weight = property(get_weight, set_weight)

    def make_sound(self):
        """Override the make_sound method for birds."""
        return self.get_name() + " sings a " + self.__song_type.lower() + " tune."

    def fly(self):
        """Describe how the bird moves based on its flying ability."""
        if self.__can_fly:
            return self.get_name() + " soars gracefully through the sky with a wingspan of " + str(self.__wing_span) + " meters."
        else:
            return self.get_name() + " cannot fly and prefers to walk or hop around."

    def move(self):
        if self.can_fly:
            return f"{self.get_name()} flies gracefully."
        else:
            return f"{self.get_name()} hops on the ground."

    def __str__(self):
        """Return a descriptive summary of the bird."""
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
