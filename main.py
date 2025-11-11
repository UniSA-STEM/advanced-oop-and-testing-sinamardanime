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


def main():

    print("\n===  ANIMAL CREATION  ===")
    lion = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 190, 80)
    parrot = Bird("Rio", "Parrot",3, "Seeds", 0.6, True, "Squawk")

    print(lion)
    print(parrot)


  # -------------------------------------------------
    # 2. Create Enclosures
    # -------------------------------------------------
    savannah_enclosure = Enclosure("Savannah Habitat", "Savannah", 200, 90)
    aviary_enclosure = Enclosure("Tropical Aviary", "Forest", 120, 85)

    print("\n--- Enclosures Created ---")
    savannah_enclosure.report_status()
    aviary_enclosure.report_status()



if __name__ == "__main__":
    main()