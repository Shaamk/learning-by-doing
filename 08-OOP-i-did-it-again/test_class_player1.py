from player1_class import Player1

def test_player1_exists():
    assert Player1

def test_player_hand_high_card():
    result = Player1("AS 10S 5H 7C 6S")
    assert result.get_high_card() == "High Card"