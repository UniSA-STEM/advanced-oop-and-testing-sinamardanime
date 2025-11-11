'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from zoo_keeper import Zookeeper
from veterinarian import Veterinarian
from health_record import HealthRecord
from reptile import Reptile


def main():
    print("\n=== ZOO MANAGEMENT SYSTEM DEMONSTRATION ===")

    # -------------------------------------------------
    # 1. Create Animals
    # -------------------------------------------------
    lion = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 50, 190)
    parrot = Bird("Rio", "Parrot", 3, "Seeds", 0.6, True, "Curved", "Chirp", 1.2)
    snake = Reptile("Slither", "Python", 4, "Rodents", "Smooth", "Rainforest", True, 28)

    print("\n--- Animals Created ---")
    print(lion)
    print(parrot)
    print(snake)

    # -------------------------------------------------
    # 2. Create Enclosures
    # -------------------------------------------------
    savannah_enclosure = Enclosure("Savannah Habitat", "Savannah", 200, 90)
    aviary_enclosure = Enclosure("Tropical Aviary", "Forest", 120, 85)
    reptile_enclosure = Enclosure("Reptile House", "Rainforest", 150, 95)

    print("\n--- Enclosures Created ---")
    savannah_enclosure.report_status()
    aviary_enclosure.report_status()
    reptile_enclosure.report_status()
    # -------------------------------------------------
    # 3. Add Animals to Enclosures
    # -------------------------------------------------
    print("\n--- Adding Animals to Enclosures ---")
    savannah_enclosure.add_animal(lion)
    aviary_enclosure.add_animal(parrot)
    reptile_enclosure.add_animal(snake)
    # -------------------------------------------------
    # 4. Create Staff Members
    # -------------------------------------------------
    zookeeper = Zookeeper("Liam the Zookeeper")
    veterinarian = Veterinarian("Dr. Kate")

    # Assign responsibilities
    zookeeper.assign_animal(lion)
    zookeeper.assign_enclosure(savannah_enclosure)
    veterinarian.assign_animal(lion)

    print("\n--- Staff Created ---")
    print(f"{zookeeper.get_name()} assigned to {savannah_enclosure.get_name()}")
    print(f"{veterinarian.get_name()} assigned to {lion.get_name()}")

    print("\n--- Zookeeper Performing Duties ---")
    zookeeper.perform_duty()

    print("\n--- Veterinarian Performing Duties ---")
    veterinarian.perform_duty()


    # -------------------------------------------------
    # 5. Demonstrate Health Management
    # -------------------------------------------------
    print("\n--- Health Management ---")
    veterinarian.treat_animal(lion, "Leg Injury", "2025-11-10", "High", "Pending")

    print("\nTrying to move Leo while under treatment...")
    aviary_enclosure.add_animal(lion)  # Should be prevented

    veterinarian.update_health_record(lion, "Recovered and healthy again.")

    # Sample health record
    record = HealthRecord("Broken Wing", "2025-11-09", "Medium", "Healed", "Flying normally again.")
    print("\nSample Health Record:")
    print(record)

    # -------------------------------------------------
    # 6. Final Reports
    # -------------------------------------------------
    print("\n--- Enclosure Reports ---")
    savannah_enclosure.report_status()
    aviary_enclosure.report_status()
    reptile_enclosure.report_status()

# -------------------------------------------------
    # 7. Removing Animals from Enclosures
    # -------------------------------------------------
    print("\n--- Removing Animals from Enclosures ---")
    print("A wildlife organization has decided to temporarily move Leo for medical observation.\n")
    savannah_enclosure.remove_animal(lion)

    print("\n\n-----------Updated Enclosure Report----------------------")
    savannah_enclosure.report_status()


if __name__ == "__main__":
    main()


