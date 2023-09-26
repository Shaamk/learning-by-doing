from rank import Rank
import pytest

def test_class_exists():
    assert Rank

def test_rank_constructor():
    assert Rank('10')

def test_rank_property():
    result = Rank('K')
    assert result.rank == 'K'

def test_invalid_input():
    with pytest.raises(ValueError):
        Rank("H")

def test_equal_function():
    result1 = Rank('7')
    result2 = Rank('7')
    assert result1 == result2

def test_equal_function_again():
    result1 = Rank('7')
    result2 = Rank('8')
    assert result1 != result2

def test_less_then_function():
    result1 = Rank('7')
    result2 = Rank('8')
    assert result1 < result2

def test_greater_then_function():
    result1 = Rank("K")
    result2 = Rank("10")
    assert result1 > result2

def test_greater_than_again():
    result1 = Rank("K")
    result2 = Rank("Q")
    assert result1 > result2