import pytest
from card import parse_card


def test_parse_card_returns_dictionary():
    result = parse_card('5H')
    assert isinstance(result, dict)

def test_5H_has_rank_5():
    result = parse_card('5H')
    assert result["rank"] == '5'

def test_4H_has_rank_4():
    result = parse_card('4H')
    assert result["rank"] == '4'

def test_AS_has_rank_A():
    result = parse_card('AS')
    assert result["rank"] == 'ace'

def test_KC_has_rank_K():
    result = parse_card('KC')
    assert result["rank"] == 'king'

def test_6H_has_suit_H():
    result = parse_card('6H')
    assert result["suit"] == 'hearts'

def test_5C_has_suit_C():
    result = parse_card('5C')
    assert result["suit"] == 'clubs'

def test_AS_has_desription():
    result = parse_card('AS')
    assert result["description"] == 'an ace of spades'

def test_KC_has_description():
    result = parse_card('KC')
    assert result["description"] == 'a king of clubs'

def test_10D_has_rank():
    result = parse_card('10D')
    assert result["rank"] == '10'

def test_10D_has_suit_D():
    result = parse_card('10D')
    assert result["suit"] == 'diamonds'
    

# def test_wrong_input():
#     with pytest.raises(ValueError):
#         result = parse_card(None,)
#         assert result == ''