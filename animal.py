'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Animal:
    """
    Base class for all animals in the zoo.
    Each animal has a name, species, age, and dietary needs.
    """
    def __init__(self, name, species, age, diet):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    # Common behaviours shared by all animals
    def make_sound(self):
        return self.name + " makes a generic animal sound."

    def eat(self):
        return self.name + " is eating " + self.diet + "."

    def sleep(self):
        return self.name + " is sleeping peacefully."

    def __str__(self):
        return self.species + " named " + self.name + ", Age: " + str(self.age) + ", Diet: " + self.diet

