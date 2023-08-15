import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)
    

def test_repr_1(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_1(phone1):
    assert str(phone1) == "iPhone 14"

def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
