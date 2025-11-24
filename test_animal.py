
"""
File: test_animal.py
Description: Unit tests for the Animal class using pytest fixtures.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
repository link: https://github.com/UniSA-STEM/advanced-oop-and-testing-sinamardanime.git
This is my own work as defined by the University's Academic Integrity Policy.
"""



import pytest
from animal import Animal
from health_record import HealthRecord



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

# ---------- TESTS ----------

def test_initialization(normal_animal):
    """Check if attributes are initialized correctly."""
    assert normal_animal.get_name() == "Leo"
    assert normal_animal.get_species() == "Lion"
    assert normal_animal.get_age() == 5
    assert normal_animal.get_diet() == "Meat"


def test_invalid_age(invalid_age_animal):
    """Negative age should default to 0."""
    assert invalid_age_animal.get_age() == 0


def test_invalid_diet(invalid_diet_animal):
    """Empty diet should default to 'Grass'."""
    assert invalid_diet_animal.get_diet() == "Grass"


def test_eat_and_sleep(normal_animal):
    """Test basic actions."""
    assert "is eating Meat" in normal_animal.eat()
    assert "is sleeping" in normal_animal.sleep()


def test_make_sound_and_move(normal_animal):
    """Test subclass-specific methods."""
    assert "makes a sound" in normal_animal.make_sound()
    assert "moves around" in normal_animal.move()


def test_add_health_record(unhealthy_animal):
    """Check that health records add correctly."""
    records = unhealthy_animal.get_health_records()
    assert len(records) == 1
    record = records[0]
    assert isinstance(record, HealthRecord)
    assert record.issue == "Injury"
    assert record.severity == "High"
    assert record.treatment_plan == "Treatment"


def test_empty_health_records():
    """Animal with no health records should return empty list."""
    a = TestAnimal("Ellie", "Elephant", 5, "Grass")
    assert len(a.get_health_records()) == 0
