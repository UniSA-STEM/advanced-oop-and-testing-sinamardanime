'''
File: main.py
Description: Demonstrates the functionality of the Zoo Management System by
             creating animals, staff, enclosures, and health records while
             showing how each component interacts.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from zoo_keeper import Zookeeper
from veterinarian import Veterinarian
from health_record import HealthRecord


def main():
    """
    This function serves as the main driver for the Zoo Management System.
    It creates instances of animals, enclosures, staff, and health records,
    then demonstrates how these interact through various operations.
    """

    print("\n=== ZOO MANAGEMENT SYSTEM DEMONSTRATION ===")


    # This section creates sample animal objects of different subclasses.
    lion = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 50, 190)
    parrot = Bird("Rio", "Parrot", 3, "Seeds", 0.6, True, "Curved", "Chirp", 1.2)
    snake = Reptile("Slither", "Python", 4, "Rodents", "Smooth", "Rainforest", True, 28)

    print("\n--- Animals Created ---")
    print(lion)
    print(parrot)
    print(snake)


    # This section demonstrates polymorphism by calling the same method (make_sound)
    # on each animal object, producing unique outputs for each subclass.
    print("\n--- Testing Animal Sounds ---")
    print(lion.make_sound())
    print(parrot.make_sound())
    print(snake.make_sound())


    # This section creates three types of enclosures representing different habitats.
    savannah_enclosure = Enclosure("Savannah Habitat", "Savannah", 200, 90)
    aviary_enclosure = Enclosure("Tropical Aviary", "Forest", 120, 85)
    reptile_enclosure = Enclosure("Reptile House", "Rainforest", 150, 95)

    print("\n--- Enclosures Created ---")
    savannah_enclosure.report_status()
    aviary_enclosure.report_status()
    reptile_enclosure.report_status()


    # This function adds animals to their corresponding enclosures based on
    # environment type validation in the Enclosure class.
    print("\n--- Adding Animals to Enclosures ---")
    savannah_enclosure.add_animal(lion)
    aviary_enclosure.add_animal(parrot)
    reptile_enclosure.add_animal(snake)


    # This section creates Zookeeper and Veterinarian objects and assigns them
    # to animals and enclosures for management and health duties.
    zookeeper = Zookeeper("Liam the Zookeeper")
    veterinarian = Veterinarian("Dr. Kate")

    # Assigns responsibilities
    zookeeper.assign_animal(lion)
    zookeeper.assign_enclosure(savannah_enclosure)
    veterinarian.assign_animal(lion)

    print("\n--- Staff Created ---")
    print(f"{zookeeper.get_name()} assigned to {savannah_enclosure.get_name()}")
    print(f"{veterinarian.get_name()} assigned to {lion.get_name()}")


    # This section simulates the daily operations where each staff member
    # performs their role (cleaning, caring, or treating animals).
    print("\n--- Zookeeper Performing Duties ---")
    zookeeper.perform_duty()

    print("\n--- Veterinarian Performing Duties ---")
    veterinarian.perform_duty()


    # This section demonstrates how veterinarians can record and treat
    # animal health issues, then update their recovery status.
    print("\n--- Health Management ---")
    veterinarian.treat_animal(lion, "Leg Injury", "2025-11-10", "High", "Pending")

    print("\nTrying to move Leo while under treatment...")
    aviary_enclosure.add_animal(lion)  # Should be prevented since Leo is in treatment

    veterinarian.update_health_record(lion, "Recovered and healthy again.")

    # Create and display a sample health record
    record = HealthRecord("Broken Wing", "2025-11-09", "Medium", "Healed", "Flying normally again.")
    print("\nSample Health Record:")
    print(record)


    # This section prints the final state of all enclosures and animals after
    # performing all interactions and operations.
    print("\n--- Enclosure Reports ---")
    savannah_enclosure.report_status()
    aviary_enclosure.report_status()
    reptile_enclosure.report_status()


    # This function demonstrates how animals can be safely removed or relocated.
    print("\n--- Removing Animals from Enclosures ---")
    print("A wildlife organisation has decided to temporarily move Leo for medical observation.\n")
    savannah_enclosure.remove_animal(lion)

    print("\n----------- Updated Enclosure Report after moving Leo ----------------------")
    savannah_enclosure.report_status()


if __name__ == "__main__":
    # This function runs the main program sequence when executed directly.
    main()
