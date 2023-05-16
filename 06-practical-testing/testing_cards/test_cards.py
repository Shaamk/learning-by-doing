from pure_cards import parse_card

INVALID = 'Sorry, that is invalid'

def test_exists():
    assert parse_card   # zonder: ()

def test_users_input_invalid_empty_string():
    compare_input_with_expected_result('')

def test_user_input_invalid_list():
    compare_input_with_expected_result([])

def test_user_input_invalid_integer():
    compare_input_with_expected_result(9)

def test_invalid_input_100C():
    compare_input_with_expected_result("100C")

def test_invalid_input_C():
    compare_input_with_expected_result("C")

def test_invalid_input_C2():
    compare_input_with_expected_result("C2")

def test_invalid_input_22():
    compare_input_with_expected_result("22")

def test_user_input_invalid_none():
    compare_input_with_expected_result(None)

def compare_input_with_expected_result(user_input, output=INVALID):
    result = parse_card(user_input)
    assert result == output

def test_rank_2D():
    result = parse_card('2D')
    assert 'rank' in result

def test_suit_3H():
    result = parse_card('3H')
    assert 'suit' in result

def test_description_4S():
    result = parse_card('4S')
    assert 'description' in result

# ===================================

def test_rank_2D_helper():
    helper_function('2D', 'rank')

def test_suit_3H_helper():
    helper_function('3H', 'suit')

def test_description_4S_helper():
    helper_function('4S', 'description')

def helper_function(user_input, dict_key):
    result = parse_card(user_input)
    assert dict_key in result

def test_valid_input_10C():
    compare_input_with_expected_result("10C", {"rank": "10", "suit": "clubs", "description": "a ten of clubs"})

def test_with_an_AS():
    compare_input_with_expected_result('AS', {"rank": "ace", "suit": "spades", "description": "an ace of spades"})

def test_with_an_8S():
    compare_input_with_expected_result('8S', {"rank": "8", "suit": "spades", "description": "an eight of spades"})
