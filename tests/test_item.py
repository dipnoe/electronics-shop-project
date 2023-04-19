"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10_000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_init(item):
    assert item.__class__ == Item
    assert item.name == "Смартфон"
    assert item.price == 10_000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200_000


def test_apply_discount(item):
    assert item.apply_discount() is None


def test_name_length(item):
    item.name = 'Наушники'
    assert item.name == 'Наушники'
    with pytest.raises(ValueError):
        item.name = 'Отвратительно длинное название'


def test_string_to_number():
    assert Item.string_to_number('2') == 2


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_add(phone, item):
    assert item + phone == 25
    assert item + item == 40
    assert phone + phone == 10
    assert phone + item == 25


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 4
    assert phone.number_of_sim == 4
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
        phone.number_of_sim = 'u'


def test_repr_phone(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
