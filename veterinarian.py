

from staff import Staff

class Veterinarian(Staff):
    """
    The Veterinarian monitors animal health, performs checks,
    and updates medical records.
    """

    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conduct_health_check(self, animal):
        """Performs a health inspection."""
        print(self.name + " checks " + animal.name + ". No visible issues found.")

    def treat_animal(self, animal, issue, date_reported, severity="Medium", treatment_plan="Observation"):
        """Treats an animal and records the treatment."""
        print(self.name + " treats " + animal.name + " for " + issue + ".")
        animal.add_health_record(issue, date_reported, severity, treatment_plan, "Treated by " + self.name)
        print(animal.name + " is now recovering.")

    def update_health_record(self, animal, note):
        """Adds a note with error handling."""
        try:
            if animal is None:
                raise ValueError("Animal cannot be None")

            if not isinstance(note, str) or not note.strip():
                raise ValueError("Note must be a non-empty string")

            records = animal.get_health_records()

            if len(records) == 0:
                raise IndexError(f"No health records found for {animal.name}")

            latest = records[-1]
            latest.notes += " | " + note
            print(self.name + " adds a note for " + animal.name + ": " + note)

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
        Describes the veterinarian's daily routine and interactions
        with assigned animals in a detailed and engaging way.
        """
        if len(self.assigned_animals) == 0:
            print(
                self.name + " has no assigned animals today, so they assist with routine health checks around the zoo.")
            return

        print(
            "\n" + self.name + " arrives at the zoo clinic early in the morning, reviewing medical charts and preparing supplies.")

        for animal in self.assigned_animals:
            print("\n" + self.name + " visits " + animal.get_name() + " the " + animal.get_species() + ".")
            print("They gently examine " + animal.get_name() + ", checking breathing, eyes, and movement.")


            records = animal.get_health_records()

            if len(records) > 0:
                print(self.name + " reviews " + animal.get_name() + "'s health record and begins treatment:")
                for record in records:
                    print(" - Issue: " + record.get_issue() +
                          " | Severity: " + record.get_severity_level() +
                          " | Treatment: " + record.get_treatment_plan())
                    print("   Treatment applied successfully. " + animal.get_name() + " is recovering well.")
            else:
                print("No current issues found for " + animal.get_name() + ". " + self.name +
                      " gives a vitamin injection and a friendly pat.")

        print(
            "\nAs the day ends, " + self.name + " updates all medical files and checks on animals resting in the clinic.")
        print(self.name + " leaves the zoo feeling proud of keeping every creature healthy and strong.\n")
