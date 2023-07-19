from players_class import Player
from pokerhand_class import Pokerhand

def test_players_exists():
    assert Player

def test_player_hand_high_card():
    result = Player("AS 10S 5H 7C 6S")
    assert result.high_card() == "High Card"

def test_player_hand_one_pair():
    result = Player("AS 10S 5H 10C 6S")
    assert result.one_pair() == "One Pair"

def test_player_hand_two_pair():
    result = Player("3H 8C 8H 9S 3D")
    assert result.two_pair() == "Two Pair"

def test_player_hand_three_of_a_kind():
    result = Player("6S 6H 7C JD 6D")
    assert result.three_of_a_kind() == "Three Of A Kind"

def test_player_hand_straight():
    result = Player("2H 3C 4S 5H 6D")
    assert result.straight() == "Straight"

def test_player_hand_straight_second():
    result = Player("JD 8C 10S 9S 7D")
    assert result.straight() == "Straight"

def test_player_hand_straight_third():
    result = Player("AS 2H 3C 4S 5D")
    assert result.straight() == "Straight"

def test_player_hand_straight_fourth():
    result = Player("10H JH QC KD AS")
    assert result.straight() == "Straight"

def test_player_hand_flush():
    result = Player("4H 8H 2H 9H 7H")
    assert result.flush() == "Flush"

def test_player_hand_full_house():
    result = Player("4H 4D 4C 8S 8D")
    assert result.full_house() == "Full House"

def test_player_hand_four_of_a_kind():
    result = Player("JC JD JS JC 5H")
    assert result.four_of_a_kind() == "Four Of A Kind"

def test_player_hand_straight_flush():
    result = Player("AC 2C 3C 4C 5C")
    assert result.straight_flush() == "Straight Flush"

def test_player_hand_royal_flush():
    result = Player("10S JS QS KS AS")
    assert result.royal_flush() == "Royal Flush"

def test_player_hand_unknown():
    result = Player("10S JS QS KS AS")
    assert result.get_hand() == Pokerhand("Royal Flush", 10)

def test_player_hand_unknown_second():
    result = Player("AC 2C 3C 4C 5C")
    assert result.get_hand() == Pokerhand("Straight Flush", 9)

def test_player_hand_unknown_third():
    result = Player("JC JD JS JC 5H")
    assert result.get_hand() == Pokerhand("Four Of A Kind", 8)

def test_player_hand_unknown_fourth():
    result = Player("4H 4D 4C 8S 8D")
    assert result.get_hand() == Pokerhand("Full House", 7)

def test_player_unknown_fifth():
    result = Player('AH 6C 9H 10S JD')
    assert result.get_hand() == Pokerhand("High Card", 1)

def test_better_hand():
    result1 = Player("JC JD JS JC 5H")
    result2 = Player("4H 4D 4C 8S 8D")
    assert result1.get_hand() > result2.get_hand()