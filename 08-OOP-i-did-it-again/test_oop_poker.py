from card_class import Card
#from pokerhand_class import Pokerhand



def test_card_class_exists():
    assert Card

# def test_class_pokerhand_exists():
#     result = Pokerhand

def test_rank_7C():
    result = Card("7C")
    assert result.rank == '7'

def test_suit_7C():
    result = Card("7C")
    assert result.suit == 'C'
    
def test_invalid_input_list():
    result = Card([])
    assert result.invalid_input() == 'Invalid Input'

def test_invalid_input_none():
    result = Card(None)
    assert result.invalid_input() == 'Invalid Input'

def test_invalid_input_empty_string():
    result = Card("")
    assert result.invalid_input() == 'Invalid Input'

def test_invalid_input_integer():
    result = Card(5)
    assert result.invalid_input() == 'Invalid Input'

def test_invalid_input_CC():
    result = Card('CC')
    assert result.invalid_input() == 'Invalid Input'

def test_invalid_input_lenght():
    result = Card('2S 3S 4S')
    assert result.invalid_input() == 'Invalid Input'
