'''
File: test_reptile.py
Description: This file contains a set of pytest unit tests for the Reptile class.
             These tests check that reptiles are created correctly, that their
             behaviours (such as moving, making sounds, and shedding skin) work
             as intended, and that the class returns clear and accurate
             descriptions through its string output.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
repository link: https://github.com/UniSA-STEM/advanced-oop-and-testing-sinamardanime.git
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




def test_shed_skin(basic_reptile):
    """
    Tests the unique reptile behaviour of shedding skin.
    The message should include the reptile's name.
    """
    expected_output = "Rango is shedding its old skin to grow a new layer."

    # Confirm behaviour output
    assert basic_reptile.shed_skin() == expected_output


def test_str(custom_reptile):
    """
    Tests the __str__ method to ensure that the formatted description
    contains all relevant reptile details (habitat, temperature, diet, etc.).
    """
    r = custom_reptile
    output = str(r)

    # Checking important sections of the formatted string
    assert "Togo is a Gecko" in output
    assert "desert" in output.lower()
    assert "smooth scales" in output.lower()
    assert "non-venomous" in output.lower()
    assert "25°C" in output
    assert "insects diet" in output.lower()
    assert "1 years old" in output.lower()

def test_default_values():
    """
       Tests that the Reptile class correctly applies default values
       when optional arguments are not provided during creation.
       """
    r = Reptile("Lizzy", "Lizard", 2, "Insects")
    assert r.scale_type == "Smooth"
    assert r.habitat == "Desert"
    assert r.is_venomous is False
    assert r.temperature == 30