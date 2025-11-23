'''
File: zoo_keeper.py
Description: Defines the Zookeeper class, a subclass of Staff,
             responsible for feeding animals, cleaning enclosures,
             and ensuring the overall welfare of the zoo’s inhabitants.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from staff import Staff  # Imports the parent Staff class for inheritance


class Zookeeper(Staff):
    """
    This class represents a zookeeper who cares for animals
    and maintains the cleanliness and safety of their enclosures.
    Zookeepers feed animals, clean habitats, and ensure daily
    welfare routines are performed correctly.
    """


    def __init__(self, name):
        """
        This function initializes a Zookeeper object using the
        parent Staff constructor and assigns the role "Zookeeper".

        Parameters:
            name (str): The zookeeper’s full name.

        Returns:
            None
        """
        # Calls the parent Staff constructor to assign the name and role
        super().__init__(name, "Zookeeper")


    def feed_animal(self, animal):
        """
        This function feeds an assigned animal and reports the action.

        Parameters:
            animal (Animal): The animal being fed.

        Returns:
            None
        """
        # Prints that the zookeeper begins feeding the assigned animal
        print(self.name + " carefully feeds " + animal.name + ", the " + animal.species + ".")
        # Prints that the animal reacts happily to feeding
        print(animal.name + " seems happy and continues eating its " + animal.diet + ".")


    def clean_enclosure(self, enclosure):
        """
        This function cleans a specific enclosure and ensures that
        the environment is suitable and safe for the animals.

        Parameters:
            enclosure (Enclosure): The enclosure being cleaned.

        Returns:
            None
        """
        # Prints that the zookeeper begins cleaning the assigned enclosure
        print(self.name + " begins cleaning the " + enclosure.name + " enclosure.")
        # Prints that the enclosure is clean after the process
        print("After thorough cleaning, the " + enclosure.name + " enclosure is now spotless and safe.")


    def perform_duty(self):
        """
        This function describes the zookeeper’s daily responsibilities in the zoo.
        It overrides the abstract method from the Staff class and prints out
        the steps of feeding animals and cleaning enclosures.

        Returns:
            None
        """
        # Checks if the zookeeper has any assigned animals or enclosures
        if not self.assigned_animals and not self.assigned_enclosures:
            print(self.name + " has no current assignments today.")
            return

        # Prints that the zookeeper begins their daily routine
        print("\n" + self.name + " begins the day by checking assigned animals and enclosures.")


        # Checks if the zookeeper has assigned animals to feed
        if self.assigned_animals:
            print(self.name + " begins feeding time:")
            # Loops through each assigned animal
            for animal in self.assigned_animals:
                # Prints detailed feeding information
                print(" - " + self.name + " feeds " + animal.get_name() + " the " + animal.get_species() +
                      " with their " + animal.get_diet().lower() + " diet.")
                # Prints the animal’s sound after being fed
                print("   " + animal.get_name() + " seems happy and makes a sound: " + animal.make_sound())


        # Checks if there are enclosures assigned for cleaning
        if self.assigned_enclosures:
            print("\n" + self.name + " begins cleaning assigned enclosures:")
            # Loops through each assigned enclosure
            for enclosure in self.assigned_enclosures:
                # Prints a message before cleaning
                print(" - " + self.name + " cleans the " + enclosure.get_name() +
                      " (" + enclosure.get_environment_type() + " environment, size " +
                      str(enclosure.get_size()) + ").")
                # Calls the enclosure’s cleaning method
                enclosure.clean_enclosure()

        # Prints that the zookeeper finishes the daily routine
        print("\nBefore finishing, " + self.name +
              " checks that all animals are healthy and comfortable for the day.")
        print(self.name + " completes the day’s work successfully.\n")
