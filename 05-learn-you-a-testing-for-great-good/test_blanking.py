import pytest
from blanking import blank

def test_blank():
    with pytest.raises(TypeError, match='hangman'):
        result = blank(None, None)
        assert result == ''

def test_blank_valid_word_no_characters():
    result = blank('asparagus', None)
    assert isinstance(result, str)
    assert result == '_________'

def test_blank_no_word_valid_characters():
    result = blank('aspargus', 'a')
    assert result == 'a__a____'

def test_blank_word_complete():
    result = blank('asparagus', 'asrgpu')
    assert result == 'asparagus'

def test_blank_characters_not_in_word():
    result = blank('coffee', 'fsa')
    assert result == '__ff__'

def test_blank_two_guessed_correctly():
    result = blank('cabbage', 'xbog')
    assert result == '__bb_g_'

def test_blank_same_char_guessed_multiple_times():
    result = blank('broccoli', 'leql')
    assert result == '______l_'

def test_blank_word_is_wrong_type():
    with pytest.raises(TypeError, match=r'.*hangman.*'):
        result = blank(23, 'ohdear')
        assert result == ''