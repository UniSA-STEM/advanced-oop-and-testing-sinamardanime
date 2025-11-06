'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

hj
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from zoo_keeper import Zookeeper
from veterinarian import Veterinarian
from health_record import HealthRecord


def main():
    # ----------------------------
    # 🦁 1. Create Animal Objects
    # ----------------------------
    print("\n=== 🦁 ANIMAL CREATION TESTS ===")
    lion = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 190, 80)
    parrot = Bird("Rio", "Parrot", 3, "Seeds", 0.6, True, "Squawk")

    print(lion)
    print(parrot)


if __name__ == "__main__":
    main()