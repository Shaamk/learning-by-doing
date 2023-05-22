from pure_rummy import has_rummy

INVALID = 'Sorry, that is invalid'

def test_exists():
    assert has_rummy

def test_invalid_input_list():
    the_expected_result([])

def test_invalid_input_empty_string():
    the_expected_result('')

def test_invalid_input_integer():
    the_expected_result(5)

def test_invalid_input_none():
    the_expected_result(None)

def the_expected_result(user_input, output=INVALID):
    result = has_rummy(user_input)
    assert result == output

def test_invalid_input_one_card():
    the_expected_result('AC')

def test_invalid_input_more_cards():
    the_expected_result('AH 2H 3H 4H 5H 6H 7H 8H')

def test_invalid_input_suit():
    the_expected_result('AH 2H 3H 4B 5H 6H 7H')

def test_invalid_input_potatopotato():
    the_expected_result('potatopotato')


def test_rummy_hand_AC_AS_5C_8C_6C_7C_AH():
    the_expected_result('AC AS 5C 8C 6C 7C AH', 'WIN')