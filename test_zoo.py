import pytest
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from veterinarian import Veterinarian
from health_record import HealthRecord

# ✅ Basic functionality tests
def test_mammal_behaviour():
    m = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 80, 190)
    assert m.get_name() == "Leo"
    assert m.get_species() == "Lion"
    assert "growls" in m.make_sound()
    assert "milk" in m.feed_young()
    assert "Savannah" in str(m)
    assert m.get_weight() == 190

# ✅ Bird subclass test (override make_sound, fly)
def test_bird_methods():
    # Bird inherits from Animal, but has its own attributes
    b = Bird("Rio", "Parrot", 3, "Seeds", 0.6, True, "Short", "Chirp", 1.2)
    result = b.make_sound()
    assert "Rio" in result
    assert "chirp" in result.lower()
    assert "fly" in b.fly().lower()

# ✅ Health record creation and string output
def test_health_record():
    h = HealthRecord("Injury", "2025-11-10", "High", "Treatment", "Healed")
    result = str(h)
    assert "Injury" in result
    assert "High" in result
    assert "Treatment" in result
    assert "Healed" in result

# ✅ Veterinarian treating and updating health record
def test_veterinarian_duties():
    v = Veterinarian("Dr. Kate")
    m = Mammal("Simba", "Lion", 4, "Meat")
    v.treat_animal(m, "Flu", "2025-11-10", "Low", "Rest")
    assert len(m.get_health_records()) == 1
    v.update_health_record(m, "Recovered")
    assert "Recovered" in m.get_health_records()[-1].notes

# ✅ Enclosure logic
def test_enclosure_add_remove(capsys):
    e = Enclosure("Savannah", "Grassland", 200)
    m = Mammal("Max", "Lion", 3, "Meat")
    e.add_animal(m)
    assert m in e.animals
    e.remove_animal(m)
    assert m not in e.animals

# ✅ Edge case: sick animal not allowed in enclosure
def test_enclosure_prevents_sick_animal(capsys):
    e = Enclosure("Savannah", "Grassland")
    m = Mammal("Rocky", "Tiger", 6, "Meat")
    m.add_health_record("Injury", "2025-11-10", "High", "Pending", "Needs rest")
    e.add_animal(m)
    output = capsys.readouterr().out
    assert "under treatment" in output
    assert m not in e.animals

# ✅ Validation and defaulting behaviour
def test_invalid_age_defaults_to_zero(capsys):
    m = Mammal("Tiny", "Mouse", -2, "Seeds")
    assert m.age == 0

def test_invalid_diet_defaults_to_grass(capsys):
    m = Mammal("Sheepy", "Sheep", 3, "")
    assert m.diet == "Grass"

# ✅ Check str() summarises correctly
def test_mammal_str_format():
    m = Mammal("Nala", "Lion", 3, "Meat", "Short", "Brown", "Savannah", 60, 130)
    text = str(m)
    assert "Nala" in text and "Lion" in text
    assert "Savannah" in text and "diet" in text.lower()