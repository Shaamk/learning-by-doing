from card import Card
import pytest

def test_class_exists():
    assert Card

def test_card_cunstructor():
    assert Card("JC")

def test_card_property():
    result = Card("JC")
    assert result.card == "JC"

def test_method_valid_rank():
    result = Card('7H')
    assert result.valid_rank() == "7"

def test_method_valid_suit():
    result = Card('8S')
    assert result.valid_suit() == 'S'

def test_check_invalid_card():
    with pytest.raises(ValueError):
        Card("ZZ")

def test_check_invalid_input():
    with pytest.raises(ValueError):
        Card("")

def test_equal_method():
    result1 = Card('7H')
    result2 = Card('7D')
    assert result1.ranks == result2.ranks

def test_equal_method_again():
    result1 = Card('7H')
    result2 = Card('7D')
    assert result1 != result2

def test_equal_method_once_more():
    result1 = Card('2S')
    result2 = Card('2S')
    assert result1 == result2

def test_less_than_method():
    result1 = Card('10S')
    result2 = Card('JS')
    assert result1 < result2

def test_greater_than_method():
    result1 = Card('AS')
    result2 = Card('10C')
    assert result1 > result2