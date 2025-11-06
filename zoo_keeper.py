




from staff import Staff


from staff import Staff  # Import the abstract base class

class Zookeeper(Staff):
    """
    The Zookeeper class represents a staff member responsible for
    maintaining animal welfare and enclosure cleanliness.
    Zookeepers ensure that animals are fed, their habitats are kept
    clean, and daily care routines are followed.
    """

    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, animal):
        """
        Feeds an assigned animal and reports the action.

        Parameters:
            animal (Animal): The animal being fed.
        """
        print(self.name + " carefully feeds " + animal.name + ", the " + animal.species + ".")
        print(animal.name + " seems happy and continues eating its " + animal.diet + ".")

    def clean_enclosure(self, enclosure):
        """
        Cleans the assigned enclosure and ensures it is suitable for its animals.

        Parameters:
            enclosure (Enclosure): The enclosure being cleaned.
        """
        print(self.name + " starts cleaning the " + enclosure.name + " enclosure.")
        print("After thorough cleaning, the " + enclosure.name + " enclosure is now spotless and safe.")

    def perform_duty(self):
        """
        Describes the zookeeper's daily responsibilities in the zoo.
        This method overrides the abstract method from the Staff class.
        """
        print(self.name + " begins the day by checking the animals' well-being.")
        print(self.name + " feeds all assigned animals, refills water supplies, and cleans each enclosure.")
        print("Before finishing, " + self.name + " ensures every animal is healthy and comfortable for the day.")