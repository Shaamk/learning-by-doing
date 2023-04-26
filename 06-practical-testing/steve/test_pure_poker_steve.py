from pure_poker_steve import description_poker_hand

INVALID_STRING = 'Invalid Input'

def test_find_function():
    assert description_poker_hand

def test_invalid_input_empty_string():
    compare_input_to_expected_result('')

def test_invalid_input_none():
    compare_input_to_expected_result(None)

def test_invalid_input_int():
    compare_input_to_expected_result(12)

def test_invalid_input_list():
    compare_input_to_expected_result([])

def test_wrong_number_of_cards():
    compare_input_to_expected_result("AS")

def test_valid():
    compare_input_to_expected_result("AS 3C 5H 7D 8D", 'High Card')

def test_one_pair():
    compare_input_to_expected_result('7S 10H 7D 2C 4D', 'One Pair')

def test_two_pair():
    compare_input_to_expected_result('7S 10S JD 10H 7D', 'Two Pair')

def test_three_of_a_kind():
    compare_input_to_expected_result('8S JH 8D KH 8C', 'Three of a Kind')

def test_straight():
    compare_input_to_expected_result('2H 3C 4S 5H 6D', 'Straight')

def test_for_flush():
    compare_input_to_expected_result('4H 8H 2H 9H 7H', 'Flush')

def test_for_full_house():
    compare_input_to_expected_result('4H 4D 4C 8S 8D', 'Full House')

def test_for_four_of_a_kind():
    compare_input_to_expected_result('JC JD JS JH 5H', 'Four Of A Kind')

def test_for_straight_flush():
    compare_input_to_expected_result('AC 2C 3C 4C 5C', 'Straight Flush')

def test_for_royal_flush():
    compare_input_to_expected_result('10S JS QS KS AS', 'Royal Flush')

def compare_input_to_expected_result(data, poker_hand=INVALID_STRING):
    result = description_poker_hand(data)
    assert result == poker_hand