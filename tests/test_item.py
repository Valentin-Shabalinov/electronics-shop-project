import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"


def test_str(item_1):
    assert str(item_1) == "Смартфон"


def test_add(item_1, phone1):
    assert item_1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    assert item_1.apply_discount() * 0.8 == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_item_instantiate_from_csv_raises():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    with pytest.raises(Item.InstantiateCSVError):
        Item.instantiate_from_csv()
