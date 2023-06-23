from oo_card import Card
import pytest

def test_exist():
    my_card = Card("2D")

def test_rank_5():
    my_card = Card("5H")
    assert my_card.ranks == "5"

def test_rank_J():
    my_card = Card("JH")
    assert my_card.ranks == "jack"

def test_suit_H():
    my_card = Card("JH")
    assert my_card.suits == "hearts"

def test_suit_D():
    my_card = Card("5D")
    assert my_card.suits == "diamonds"

