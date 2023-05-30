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
    the_expected_result('AC AS 5C 8C 6C 7C AH', 'WIN')  # 3 ranks and straight 4

def test_rummy_hand_AH_2H_3H_4H_5H_6H_7H():
    the_expected_result('AH 2H 3H 4H 5H 6H 7H', 'WIN')  # straight 3 and straight 4

def test_rummy_hand_10H_9H_8H_7H_7C_7S_7D():
    the_expected_result('10H 9H 8H 7H 7C 7S 7D', 'WIN') # straight 3 and ranks 4

def test_rummy_hand_QC_KC_AC_AS_2S_3S_4S():
    the_expected_result('QC KC AC AS 2S 3S 4S', 'LOSE') # only straight 4

def test_rummy_hand_3C_3D_3H_3S_4S_5C_6S():
    the_expected_result('3C 3D 3H 3S 4S 5C 6S', 'LOSE') # only 4 ranks of 3