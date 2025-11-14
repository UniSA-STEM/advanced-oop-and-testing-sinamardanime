"""
File: test_mammal.py
Description: Unit tests for the Mammal subclass.
Author: Sina Mardani Mehrabad
"""

import pytest
from mammal import Mammal


# ---------- FIXTURES ----------
@pytest.fixture
def normal_mammal():
    """Create a normal mammal."""
    return Mammal("Leo", "Lion", 5, "Meat", "Short", "Golden", "Savanna", 80, 190)


@pytest.fixture
def invalid_mammal():
    """Create a mammal with invalid inputs."""
    return Mammal("Dusty", "Camel", -2, "", "", "", None, -1, -50)


# ---------- TESTS ----------

def test_initialization(normal_mammal):
    """Check basic mammal attributes."""
    assert normal_mammal.get_name() == "Leo"
    assert normal_mammal.get_species() == "Lion"
    assert normal_mammal.get_age() == 5
    assert normal_mammal.get_diet() == "Meat"
    assert normal_mammal.get_fur_color() == "Golden"
    assert normal_mammal.get_fur_type() == "Short"
    assert normal_mammal.get_habitat() == "Savanna"
    assert normal_mammal.get_speed() == 80
    assert normal_mammal.get_weight() == 190


def test_invalid_data_handling(invalid_mammal):
    """Ensure invalid data defaults are applied."""
    assert invalid_mammal.get_age() == 0
    assert invalid_mammal.get_diet() == "Grass"
    assert invalid_mammal.get_fur_color() == "Brown"
    assert invalid_mammal.get_fur_type() == "Short"
    assert invalid_mammal.get_habitat() == "Grassland"
    assert invalid_mammal.get_speed() == 20
    assert invalid_mammal.get_weight() == -50


def test_make_sound_and_move(normal_mammal):
    """Test sound and movement output."""
    result_move = normal_mammal.move()
    assert "growls" in normal_mammal.make_sound().lower()
    assert "moves at" in result_move.lower()
    assert "80 km/h" in result_move
    assert "savanna" in result_move.lower()


def test_feed_young(normal_mammal):
    """Ensure unique mammal behavior works."""
    result = normal_mammal.feed_young()
    assert "feeding" in result.lower()
    assert "milk" in result.lower()


def test_setters_and_getters(normal_mammal):
    """Check setter and getter behaviour for attributes."""
    normal_mammal.fur_color = "Black"
    normal_mammal.fur_type = "Thick"
    normal_mammal.habitat = "Forest"
    normal_mammal.speed = 60
    normal_mammal.weight = 210

    assert normal_mammal.get_fur_color() == "Black"
    assert normal_mammal.get_fur_type() == "Thick"
    assert normal_mammal.get_habitat() == "Forest"
    assert normal_mammal.get_speed() == 60
    assert normal_mammal.get_weight() == 210


def test_str_output(normal_mammal):
    """Check that __str__ returns a descriptive string."""
    description = str(normal_mammal).lower()  # make it case-insensitive
    assert "lion" in description
    assert "golden" in description
    assert "short" in description
    assert "savanna" in description
    assert "80 km/h" in description
    assert "meat" in description
