'''
File: veterinarian.py
Description: Defines the Veterinarian class, a subclass of Staff,
             responsible for monitoring animal health, performing checks,
             treating illnesses, and maintaining medical records.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from staff import Staff  # Imports the parent Staff class for inheritance


class Veterinarian(Staff):
    """
    This class represents a veterinarian in the zoo.
    The veterinarian monitors animal health, performs checkups, provides treatment,
    and manages health records to ensure animals remain healthy and safe.
    """


    def __init__(self, name):
        """
        This function initializes a Veterinarian object by setting
        their name and role through the parent Staff class constructor.

        Parameters:
            name (str): The veterinarian’s name.

        Returns:
            None
        """
        # Calls the parent constructor and assigns the veterinarian role
        super().__init__(name, "Veterinarian")


    def conduct_health_check(self, animal):
        """
        This function performs a basic health inspection on an animal
        to ensure there are no visible injuries or signs of illness.

        Parameters:
            animal (Animal): The animal object being checked.

        Returns:
            None
        """
        # Prints a message showing that the veterinarian checks the animal
        print(self.name + " checks " + animal.name + ". No visible issues found.")


    def treat_animal(self, animal, issue, date_reported, severity="Medium", treatment_plan="Observation"):
        """
        This function treats an animal for a reported health issue
        and records the details into its health record.

        Parameters:
            animal (Animal): The animal being treated.
            issue (str): The medical issue or condition identified.
            date_reported (str): The date the issue was recorded.
            severity (str): The seriousness of the issue (default: "Medium").
            treatment_plan (str): The treatment method applied (default: "Observation").

        Returns:
            None
        """
        # Prints that the veterinarian begins treating the animal
        print(self.name + " treats " + animal.name + " for " + issue + ".")

        # Adds a health record entry to the animal’s medical history
        animal.add_health_record(issue, date_reported, severity, treatment_plan, "Treated by " + self.name)

        # Confirms that the treatment is complete
        print(animal.name + " is now recovering.")


    def update_health_record(self, animal, note):
        """
        This function safely adds a new note to the most recent
        health record of a specific animal, using exception handling
        to manage errors such as invalid inputs or missing data.

        Parameters:
            animal (Animal): The animal whose record is updated.
            note (str): The additional note to be added.

        Returns:
            None
        """
        try:
            # Checks if the animal argument exists
            if animal is None:
                raise ValueError("Animal cannot be None")

            # Checks that the note is a valid non-empty string
            if not isinstance(note, str) or not note.strip():
                raise ValueError("Note must be a non-empty string")

            # Retrieves the list of health records from the animal
            records = animal.get_health_records()

            # Checks that the animal has at least one existing record
            if len(records) == 0:
                raise IndexError(f"No health records found for {animal.name}")

            # Gets the latest health record entry
            latest = records[-1]

            # Adds the new note to that record
            latest.notes += " | " + note

            # Prints confirmation of the update
            print(self.name + " adds a note for " + animal.name + ": " + note)

        # Handles possible errors gracefully
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError as e:
            print(f"Error: {e}")
        except AttributeError:
            print("Error: Invalid animal object provided")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def perform_duty(self):
        """
        This function describes the veterinarian’s daily routine,
        including animal checkups, treatments, and health record updates.

        It loops through assigned animals and prints detailed steps
        showing how the veterinarian interacts with each animal.

        Returns:
            None
        """
        # Checks if the veterinarian has any animals assigned
        if len(self.assigned_animals) == 0:
            print(self.name + " has no assigned animals today, so assists with routine health checks around the zoo.")
            return

        # Prints that the veterinarian begins their daily tasks
        print("\n" + self.name + " begins the day by reviewing charts and preparing medical tools in the clinic.")

        # Loops through all assigned animals for inspection
        for animal in self.assigned_animals:
            # Prints that the veterinarian visits each animal
            print("\n" + self.name + " visits " + animal.get_name() + " the " + animal.get_species() + ".")
            print("They carefully examine " + animal.get_name() + ", checking breathing, eyes, and movement.")

            # Retrieves health records of the animal
            records = animal.get_health_records()

            # Checks if the animal has existing records
            if len(records) > 0:
                print(self.name + " reviews " + animal.get_name() + "'s health record and begins treatment:")
                for record in records:
                    # Prints information about each health record
                    print(" - Issue: " + record.get_issue() +
                          " | Severity: " + record.get_severity_level() +
                          " | Treatment: " + record.get_treatment_plan())
                    print("   Treatment applies successfully. " + animal.get_name() + " recovers steadily.")
            else:
                # Prints when the animal is healthy
                print("No current issues found for " + animal.get_name() + ". " + self.name +
                      " gives a vitamin injection and a friendly pat.")

        # Prints that the veterinarian ends their day
        print("\nAs the day ends, " + self.name + " updates all medical records and checks on resting animals.")
        print(self.name + " leaves the zoo feeling satisfied with another healthy day.\n")
