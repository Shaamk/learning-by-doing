from suit import Suit
import pytest

def test_suit_class_exists():
    assert Suit

def test_suit_constructor():
    assert Suit("S")

def test_suit_property():
    result = Suit('S')
    assert result.suit == 'S'

def test_invalid():
    with pytest.raises(ValueError):
        Suit("B")

def test_invalid_two():
    with pytest.raises(ValueError):
        Suit("")

def test_equal_method():
    result1 = Suit('H')
    result2 = Suit('H')
    assert result1.suit == result2.suit

def test_equal_method_two():
    result1 = Suit('S')
    result2 = Suit('C')
    assert result1.suit != result2.suit