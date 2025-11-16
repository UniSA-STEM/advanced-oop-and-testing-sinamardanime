'''
File: test_bird.py
Description: Contains pytest unit tests for the Bird class. These tests verify
             that bird-specific attributes (wingspan, beak type, song, weight,
             flight ability) are stored correctly, that movement and sound
             behaviours work as expected, and that the string description is
             formatted properly.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from bird import Bird


@pytest.fixture
def basic_bird():
    """
    Fixture: Creates a basic bird using default attribute values.
    Used for simple behaviour tests such as movement and sound.
    """
    return Bird("Polly", "Parrot", 2, "Seeds")


@pytest.fixture
def custom_bird():
    """
    Fixture: Creates a bird with custom attributes for more detailed tests
    such as __str__, wingspan, beak type, flying behaviour, and song.
    """
    return Bird(
        name="Aquila",
        species="Eagle",
        age=5,
        diet="Meat",
        wing_span=2.5,
        can_fly=True,
        beak_type="Hooked",
        song_type="Screech",
        weight=6.2
    )


def test_initialisation(custom_bird):
    """
    Tests that all attributes (inherited and bird-specific) are assigned
    correctly during initialisation.
    """
    b = custom_bird

    # Inherited attributes
    assert b.get_name() == "Aquila"
    assert b.get_species() == "Eagle"
    assert b.age == 5
    assert b.diet == "Meat"

    # Bird-specific attributes
    assert b.wing_span == 2.5
    assert b.can_fly is True
    assert b.beak_type == "Hooked"
    assert b.song_type == "Screech"
    assert b.weight == 6.2

