import pytest
from pure_poker import get_description_for_poker_hand

def test_exists():
    assert get_description_for_poker_hand

def test_one_card_5H():
    result = get_description_for_poker_hand("5H")
    assert result == "Sorry, that's invalid"

def test_None():
    result = get_description_for_poker_hand(None)
    assert result == "Sorry, that's invalid"

def test_empty_string():
    result = get_description_for_poker_hand("")
    assert result == "Sorry, that's invalid"

def test_two_cards_4H_5H():
    result = get_description_for_poker_hand("4H 5H")
    assert result == "Sorry, that's invalid"

def test_three_cards_3D_4C_5D():
    result = get_description_for_poker_hand("3D 4C 5D")
    assert result == "Sorry, that's invalid"

def test_too_much_characters():
    result = get_description_for_poker_hand("10C 10D 10H 10S 10C")
    assert result == "Sorry, that's invalid"

def test_invalid_card():
    result = get_description_for_poker_hand("10C 10D 10H 10S 8X")
    assert result == "Sorry, that's invalid"

def test_high_card():
    result = get_description_for_poker_hand("AS 10S 5H 7C 6S")
    assert result == "High card"

def test_one_pair():
    result = get_description_for_poker_hand("AS 10S 5H 10C 6S")
    assert result == "One pair"

def test_two_pair():
    result = get_description_for_poker_hand("3H 8C 8H 9S 3D")
    assert result == "Two pair"

def test_three_of_a_kind():
    result = get_description_for_poker_hand("6S 6H 7C JD 6D")
    assert result == "Three of a kind"

def test_straight():
    result = get_description_for_poker_hand("2H 3C 4S 5H 6D")
    assert result == "Straight"

def test_one_more_straight():
    result = get_description_for_poker_hand("JD 8C 10S 9S 7D")
    assert result == "Straight"