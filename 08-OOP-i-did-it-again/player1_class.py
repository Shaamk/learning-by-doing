from card_class import Card
from pokerhand_class import Pokerhand, pokerhands

class Player1:
    def __init__(self, cards):
        self.cards = cards
        ranks_collection = []
        for rank in self.cards:
            ranks_collection.append(rank)
        
    
    def get_high_card(self):
        pass

        



        
# cards = Card()
# ranks = cards.get_rank()
# hand = Pokerhand(pokerhands)