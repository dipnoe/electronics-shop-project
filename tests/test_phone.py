import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item():
    return Item("Смартфон", 10_000, 20)


def test_add(phone, item):
    assert item + phone == 25
    assert item + item == 40
    assert phone + phone == 10
    assert phone + item == 25
    with pytest.raises(ValueError):
        phone + str


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 4
    assert phone.number_of_sim == 4
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
        phone.number_of_sim = 'u'


def test_repr_phone(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
