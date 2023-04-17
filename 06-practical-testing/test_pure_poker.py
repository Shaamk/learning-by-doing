import pytest
from pure_poker import get_description_for_poker_hand

def test_exists():
    assert get_description_for_poker_hand

def test_one_card_5H():
    result = get_description_for_poker_hand("5H")
    assert result == "Sorry, that's invalid"