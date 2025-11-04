'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from mammal import Mammal


def main():
    print("=== MAMMAL CLASS DEMONSTRATION ===\n")
    print("Creating a mammal with full details:\n")
    lion = Mammal("Leo", "Lion", 7, "Meat", "Thick", "Golden", "Savannah", 80, 190)
    print(lion)
    print(lion.make_sound())
    print(lion.feed_young())
    print(lion.move())
    print()

if __name__ == "__main__":
    main()


