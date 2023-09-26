from rank import Rank

class Card:
    def __init__(self, card) -> None:
        self.card = card
        self.ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        self.suits = ['S', 'H', 'C', 'D']
        self.check_invalid()
        self.rank_instance = Rank(self.card[:-1])
   
    
    def valid_rank(self):
        return ''.join([rank[:-1] for rank in self.card.split() if rank[:-1] in self.ranks])
        #rank_list = []
        # for rank in self.card.split():
        #     if rank[:-1] in self.valid:
        #         rank_list.append(rank[:-1])
        # return rank_list

    def valid_suit(self):
        return ''.join([suit[-1] for suit in self.card.split() if suit[-1] in self.suits])
    
    def check_invalid(self):
        if not self.valid_rank() or not self.valid_suit():
            raise ValueError()

    def __eq__(self, other: object) -> bool:
        return self.card == other.card
    
    def __lt__(self, other: object) -> bool:
        return self.rank_instance < other.rank_instance
    
    def __gt__(self, other: object) -> bool:
        return self.rank_instance > other.rank_instance
