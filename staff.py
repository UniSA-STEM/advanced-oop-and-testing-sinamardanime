'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


from abc import ABC, abstractmethod

class Staff(ABC):
    """
    The Staff class is an abstract base class representing all staff members in the zoo.
    It defines common attributes and enforces the implementation of specific methods
    (e.g., perform_duty) in subclasses.
    """

    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    def get_name(self):
        """Gets the staff member's name."""
        return self.__name

    def get_role(self):
        """Gets the staff member's role."""
        return self.__role

    def get_assigned_animals(self):
        """Gets the animals assigned to this staff member."""
        return self.__assigned_animals

    def get_assigned_enclosures(self):
        """Gets the enclosures assigned to this staff member."""
        return self.__assigned_enclosures


    name = property(get_name)
    role = property(get_role)
    assigned_animals = property(get_assigned_animals)
    assigned_enclosures = property(get_assigned_enclosures)


    def assign_animal(self, animal):
        """Assigns an animal to this staff member."""
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        """Assigns an enclosure to this staff member."""
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    @abstractmethod
    def perform_duty(self):
        """Abstract method that describes the staff member’s daily duties."""
        pass




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
        print(self.name + " begins the day by checking the animals' well being.")
        print(self.name + " feeds all assigned animals, refills water supplies, and cleans each enclosure.")
        print("Before finishing, " + self.name + " ensures every animal is healthy and comfortable for the day.")







class Veterinarian(Staff):
    """
    The Veterinarian class represents a staff member responsible for
    monitoring animal health, diagnosing issues, and providing treatment.
    Veterinarians perform health checks and record medical observations.
    """

    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conduct_health_check(self, animal):
        """
        Conducts a health check on an assigned animal.

        Parameters:
            animal (Animal): The animal being examined.
        """
        print(self.name + " conducts a routine health check on " + animal.name + ".")
        print("After a careful examination, " + animal.name + " appears healthy and active.")

    def treat_animal(self, animal, issue):
        """
        Treats an animal for a given health issue.

        Parameters:
            animal (Animal): The animal receiving treatment.
            issue (str): The issue being treated.
        """
        print(self.name + " treats " + animal.name + " for " + issue + ".")
        print("The treatment is successful and " + animal.name + " shows signs of recovery.")

 def update_health_record(self, animal, note):
        """
        Updates the health record for an animal with a medical note.

        Parameters:
            animal (Animal): The animal whose record is being updated.
            note (str): The health note to record.
        """
        print(self.name + " updates " + animal.name + "'s health record with note: " + note)

    def perform_duty(self):
        """
        Describes the veterinarian’s daily responsibilities in the zoo.
        This method overrides the abstract method from the Staff class.
        """
        print(self.name + " begins the day by reviewing recent health reports.")
        print(self.name + " conducts examinations on animals and provides medical care when needed.")
        print(self.name + " ensures all health records are up to date before ending the shift.")
