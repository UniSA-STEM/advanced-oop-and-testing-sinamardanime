

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
        """Adds a note to the most recent health record."""
        if animal.get_health_records():
            latest = animal.get_health_records()[-1]
            latest.notes += " | " + note
            print(self.name + " adds a note for " + animal.name + ": " + note)
        else:
            print("No health records found for " + animal.name + ".")

    def perform_duty(self):
        """Describes the veterinarian's daily routine."""
        print(self.name + " starts the day reviewing health reports and visiting enclosures.")