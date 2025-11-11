ChatGPT said:

Perfect, Sina 👍 — now that I’ve read your mammal.py, here’s a complete pytest file that tests it professionally (with fixtures, validation, and subclass-specific behaviour).

✅ test_mammal.py

Create a new file next to your others (in the same folder) called:

test_mammal.py


Paste this code inside:

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
    return Mammal("Dusty", "Camel", -2, "", "", "", None, -5, -50)


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