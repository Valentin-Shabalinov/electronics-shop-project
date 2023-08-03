import pytest

from src.item import Item


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    assert item_1.apply_discount() * 0.8 == 8000.0
