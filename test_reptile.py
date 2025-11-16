'''
File: test_reptile.py
Description: This file contains a set of pytest unit tests for the Reptile class.
             These tests check that reptiles are created correctly, that their
             behaviours (such as moving, making sounds, and shedding skin) work
             as intended, and that the class returns clear and accurate
             descriptions through its string output.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''



import pytest
from reptile import Reptile



@pytest.fixture
def basic_reptile():
    """
    Fixture: Creates a simple reptile with default attribute values.
    This reptile is reused across multiple tests to avoid repetition.
    """
    return Reptile("Rango", "Lizard", 3, "Insects")


@pytest.fixture
def custom_reptile():
    """
    Fixture: Creates a reptile with custom attributes.
    Used to test string formatting, custom values, and initialisation.
    """
    return Reptile(
        "Togo", "Gecko", 1, "Insects",
        scale_type="Smooth",
        habitat="Desert",
        is_venomous=False,
        temperature=25
    )


def test_make_sound(basic_reptile):
    """
    Tests the overridden make_sound() method to ensure
    the reptile returns the correct hissing sound.
    """
    # Reptile should hiss using its name
    assert basic_reptile.make_sound() == "Rango hisses softly."


def test_move():
    """
    Tests movement behaviour. The movement string should include the
    reptile's name and the habitat, converted to lowercase.
    """
    r = Reptile("Spike", "Lizard", 2, "Insects", habitat="Forest")

    expected_output = "Spike slithers or crawls across the forest."

    # Confirm correct movement description
    assert r.move() == expected_output