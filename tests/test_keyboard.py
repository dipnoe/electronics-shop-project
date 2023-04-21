import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('cat keyboard', 7_000, 5)


def test_keyboard(keyboard):
    assert keyboard.__str__() == 'cat keyboard'
    assert keyboard.price == 7_000
    assert keyboard.quantity == 5


def test_positive_lang(keyboard):
    assert keyboard.language == "EN"


def test_negative_lang(keyboard):
    with pytest.raises(AssertionError):
        assert keyboard.change_lang() == 'KZ'
