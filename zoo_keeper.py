



from staff import Staff  #

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
            if not self.assigned_animals and not self.assigned_enclosures:
                print(self.name + " has no current assignments today.")
                return

            print("\n" + self.name + " begins the day by checking assigned animals and enclosures.")

            # Feed assigned animals
            if self.assigned_animals:
                print(self.name + " starts feeding time:")
                for animal in self.assigned_animals:
                    print(" - " + self.name + " feeds " + animal.get_name() + " the " + animal.get_species() +
                          " with their " + animal.get_diet().lower() + " diet.")
                    print("   " + animal.get_name() + " seems happy and makes a sound: " + animal.make_sound())

            # Clean assigned enclosures
            if self.assigned_enclosures:
                print("\n" + self.name + " begins cleaning assigned enclosures:")
                for enclosure in self.assigned_enclosures:
                    print(" - " + self.name + " cleans the " + enclosure.get_name() +
                          " (" + enclosure.get_environment_type() + " environment, size " +
                          str(enclosure.get_size()) + ").")
                    enclosure.clean_enclosure()

            print(
                "\nBefore finishing, " + self.name + " checks that all animals are healthy and comfortable for the day.")
            print(self.name + " completes the day's work successfully.\n")