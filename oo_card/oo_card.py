RANKS = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7','8': '8',
         '9': '9', '10': '10', 'A': 'ace', 'J': 'jack', 'Q': 'queen', 'K': 'king'}

SUITS = {'D': 'diamonds', 'H': 'hearts', 'S': 'spades', 'C': 'clubs'}

DESCRIPTION = {'2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
 '8': 'eight', '9': 'nine', '10': 'ten', 'A': 'ace', 'J':'jack', 'Q': 'queen', 'K': 'king'}

class Card:
    def __init__(self, short_description):
        self.ranks = RANKS[short_description[:-1]]
        self.suits = SUITS[short_description[-1]]
        
