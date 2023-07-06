from card_class import Card
import pytest


def test_card_class_exists():
    assert Card

def test_rank_7C():
    result = Card("7C")
    other = Card("AH")
    assert result.get_rank() == "7"
    assert other.get_rank() == "A"

def test_suit_7C():
    result = Card("7C")
    assert result.get_suit() == 'C'
    
def test_invalid_input_list():
    with pytest.raises(TypeError):
        result = Card([])

def test_invalid_input_none():
    with pytest.raises(TypeError):
        result = Card(None)

def test_invalid_input_empty_string():
    with pytest.raises(TypeError):
        result = Card("")

def test_invalid_input_integer():
    with pytest.raises(TypeError):
        result = Card(5)

def test_invalid_input_CC():
    result = Card("CC")
    assert result.invalid_input() == "Invalid Input"

def test_invalid_input_three_cards():
    result = Card('2S 3S 4S')
    assert result.invalid_input() == "Invalid Input"
    
def test_invalid_input_six_cards():
    result = Card('2C 4D 6H 8S 10C QD')
    assert result.invalid_input() == "Invalid Input"


