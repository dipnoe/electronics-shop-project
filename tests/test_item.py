"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10_000, 20)


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
    with pytest.raises(Exception):
        item.name = 'Отвратительно длинное название'


def test_string_to_number():
    assert Item.string_to_number('2') == 2


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
