from pure_palindrome_shorter import check_for_invalid
from pure_palindrome_shorter import clean_user_input
from pure_palindrome_shorter import check_for_palindrome
from pure_palindrome_shorter import is_palindrome

INVALID_INPUT = 'Sorry, that is invalid input'


def test_if_input_is_invalid_None():
    compare_input_to_expected_result(None)

def test_if_input_is_invalid_empty_string():
    compare_input_to_expected_result('')

def test_if_input_is_invalid_integer():
    compare_input_to_expected_result(7)

def test_if_input_is_invalid_list():
    compare_input_to_expected_result([])

def test_if_input_only_contains_comma():
    compare_input_to_expected_result(',')

def test_if_input_is_comma_and_letter():
    compare_input_to_expected_result('a,', None)

def test_if_input_clean_punctuation():
    result = clean_user_input('a:a')
    assert result == 'aa'

def test_if_input_clean_different_punctuation():
    result = clean_user_input('a,a:b"c;')
    assert result == 'aabc'

def test_if_input_clean_different_punctuation_extended():
    result = clean_user_input('a a:b "c')
    assert result == 'aabc'

def test_is_not_palindrome():
    result = check_for_palindrome('pie')
    assert result == 'Not a palindrome'

def test_is_palindrome():
    result = check_for_palindrome('otto')
    assert result == 'Palindrome'
    
def test_if_it_is_a_palindrome():
    result = check_for_palindrome('evacaniseebeesinacave')
    assert result == 'Palindrome'

def test_is_palindrome_capitals():
    result = clean_user_input('Eva, can I see bees in a cave?')
    assert result == 'evacaniseebeesinacave'
    
def compare_input_to_expected_result(user_input, output= INVALID_INPUT):
    result = check_for_invalid(user_input)
    assert result == output

def test_for_helper_function_palindrome():
    result = is_palindrome('otto')
    assert result == 'Palindrome'

def test_for_helper_function_not_palindrome():
    result = is_palindrome('pie')
    assert result == "Not a palindrome"

def test_for_helper_function_invalid():
    result = is_palindrome(None)
    assert result == "Sorry, that is invalid input"

def test_for_helper_function_invalid_punctuatio():
    result = is_palindrome(':,{}')
    assert result == "Sorry, that is invalid input"
