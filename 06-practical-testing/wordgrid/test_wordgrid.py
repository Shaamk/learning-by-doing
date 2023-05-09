from pure_wordgrid import build_word_grid
from pure_wordgrid import check_if_invalid

INVALID = 'Sorry that is invalid'

def test_userinput_invalid_None():
    compare_input_to_expected_result(None)

def test_for_empty_string():
    compare_input_to_expected_result('')

def test_user_input_invalid_interger():
    compare_input_to_expected_result(7)

def test_user_input_invalid_list():
    compare_input_to_expected_result([])

def test_user_input_invalid_numbers_and_letters():
    compare_input_to_expected_result('123abc')

def test_user_input_is_valid():
    compare_input_to_expected_result('pot', None)

# def test_build_word_capitalize_first_letter():
#     result = build_word_grid('pot')
#     assert result == 'Pot'

# def test_build_word_grid_upper():
#     result = build_word_grid('POT')
#     assert result == 'Pot'


def compare_input_to_expected_result(user_input, output=INVALID):
    result = check_if_invalid(user_input)
    assert result == output


def test_second_letter_is_upper():
    result = build_word_grid('pot')
    assert result == ['Pot', 'pOt', 'poT']
