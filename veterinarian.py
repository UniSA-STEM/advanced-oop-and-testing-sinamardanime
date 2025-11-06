

from staff import Staff

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
