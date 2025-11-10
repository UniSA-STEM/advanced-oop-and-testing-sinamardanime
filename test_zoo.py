import pytest
from mammal import Mammal
from bird import Bird
from enclosure import Enclosure
from veterinarian import Veterinarian
from health_record import HealthRecord



def test_mammal_behaviour():
    m = Mammal("Leo", "Lion", 5, "Meat", "Thick", "Golden", "Savannah", 80, 190)
    assert m.get_name() == "Leo"
    assert m.get_species() == "Lion"
    assert "growls" in m.make_sound().lower()
    assert "milk" in m.feed_young().lower()
    assert "savannah" in str(m).lower()
    assert m.get_weight() == 190



def test_bird_methods():
    b = Bird("Rio", "Parrot", 3, "Seeds", 0.6, True, "Short", "Chirp", 1.2)
    result = b.make_sound().lower()
    assert "rio" in result
    assert "chirp" in result

    fly_result = b.fly().lower()

    assert "soars gracefully" in fly_result or "flies gracefully" in fly_result
    assert "wingspan" in fly_result


def test_health_record():
    h = HealthRecord("Injury", "2025-11-10", "High", "Treatment", "Healed")
    result = str(h)
    assert "injury" in result.lower()
    assert "high" in result.lower()
    assert "treatment" in result.lower()
    assert "healed" in result.lower()


def test_veterinarian_duties():
    v = Veterinarian("Dr. Kate")
    m = Mammal("Simba", "Lion", 4, "Meat")
    v.treat_animal(m, "Flu", "2025-11-10", "Low", "Rest")
    assert len(m.get_health_records()) == 1
    v.update_health_record(m, "Recovered")
    assert "recovered" in m.get_health_records()[-1].notes.lower()

