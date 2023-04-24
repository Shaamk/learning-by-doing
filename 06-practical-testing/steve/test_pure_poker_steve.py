from pure_poker_steve import description_poker_hand

INVALID_STRING = 'Invalid Input'

def test_find_function():
    assert description_poker_hand

def test_invalid_input_empty_string():
    helper_function('')

def test_invalid_input_none():
    helper_function(None)

def test_invalid_input_int():
    helper_function(12)

def test_invalid_input_list():
    helper_function([])

def helper_function(data):
    result = description_poker_hand(data)
    assert result == INVALID_STRING

def test_wrong_number_of_cards():
    helper_function("AS")

def test_valid():
    result = description_poker_hand("AS 3C 5H 7D 8D")
    assert result == 'High Card'

def test_one_pair():
    result = description_poker_hand("7S 10H 7D 2C 4D")
    assert result == 'One Pair'
    