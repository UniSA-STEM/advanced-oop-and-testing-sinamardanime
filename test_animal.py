"""
File: test_animal.py
Description: Unit tests for the Animal class using pytest fixtures.
Author: Sina Mardani Mehrabad
"""

import pytest
from animal import Animal
from health_record import HealthRecord


"""
File: test_animal.py
Description: Unit tests for the Animal class using pytest fixtures.
Author: Sina Mardani Mehrabad
"""

import pytest
from animal import Animal
from health_record import HealthRecord


# Create a small subclass to test Animal (since it's abstract)
class TestAnimal(Animal):
    def make_sound(self):
        return f"{self.get_name()} makes a sound."

    def move(self):
        return f"{self.get_name()} moves around."


# ---------- FIXTURES ----------
@pytest.fixture
def normal_animal():
    """Create a normal healthy animal."""
    return TestAnimal("Leo", "Lion", 5, "Meat")


@pytest.fixture
def invalid_age_animal():
    """Create animal with invalid age (for validation testing)."""
    return TestAnimal("Milo", "Monkey", -3, "Fruit")


@pytest.fixture
def invalid_diet_animal():
    """Create animal with invalid diet (for validation testing)."""
    return TestAnimal("Benny", "Elephant", 10, "")


@pytest.fixture
def unhealthy_animal():
    """Create animal that already has a health record."""
    a = TestAnimal("Rex", "Tiger", 6, "Meat")
    a.add_health_record("Injury", "2025-11-10", "High", "Treatment", "Leg injury")
    return a


