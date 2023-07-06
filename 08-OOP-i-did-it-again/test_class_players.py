from players_class import Players

def test_player1_exists():
    assert Players

def test_player_hand_high_card():
    result = Players("AS 10S 5H 7C 6S")
    assert result.high_card() == "High Card"

def test_player_hand_one_pair():
    result = Players("AS 10S 5H 10C 6S")
    assert result.one_pair() == "One Pair"

def test_player_hand_two_pair():
    result = Players("3H 8C 8H 9S 3D")
    assert result.two_pair() == "Two Pair"

def test_player_hand_three_of_a_kind():
    result = Players("6S 6H 7C JD 6D")
    assert result.three_of_a_kind() == "Three Of A Kind"

def test_player_hand_straight():
    result = Players("2H 3C 4S 5H 6D")
    assert result.straight() == "Straight"

def test_player_hand_straight_second():
    result = Players("JD 8C 10S 9S 7D")
    assert result.straight() == "Straight"

def test_player_hand_straight_third():
    result = Players("AS 2H 3C 4S 5D")
    assert result.straight() == "Straight"

def test_player_hand_straight_fourth():
    result = Players("10H JH QC KD AS")
    assert result.straight() == "Straight"

def test_player_hand_flush():
    result = Players("4H 8H 2H 9H 7H")
    assert result.flush() == "Flush"

def test_player_hand_full_house():
    result = Players("4H 4D 4C 8S 8D")
    assert result.full_house() == "Full House"

def test_player_hand_four_of_a_kind():
    result = Players("JC JD JS JC 5H")
    assert result.four_of_a_kind() == "Four Of A Kind"

def test_player_hand_straight_flush():
    result = Players("AC 2C 3C 4C 5C")
    assert result.straight_flush() == "Straight Flush"

def test_player_hand_royal_flush():
    result = Players("10S JS QS KS AS")
    assert result.royal_flush() == "Royal Flush"