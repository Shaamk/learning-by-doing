from pokerhand_class import Pokerhand


def test_pokerhand_class_exists():
    assert Pokerhand

def test_pokerhand_properties():
    result = Pokerhand("High Card", 1)
    assert result.hand == "High Card"
    assert result.rating == 1

def test_str_method():
    hand = Pokerhand("One Pair", 2)
    result = str(hand)
    assert result == "One Pair, 2"

def test_lt_method():
    result1 = Pokerhand("Straight", 5)
    result2 = Pokerhand("Flush", 6)
    assert result1 < result2

def test_gt_method():
    result1 = Pokerhand("Four Of A Kind", 8)
    result2 = Pokerhand("Straight Flush", 9)
    assert result2 > result1

def test_eq_method():
    result1 = Pokerhand("Two Pair", 3)
    result2 = Pokerhand("Two Pair", 3)
    assert result1 == result2