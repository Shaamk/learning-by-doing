from card_class import Card
from pokerhand_class import Pokerhand

class Players:

    def __init__(self, cards):
        self.cards = cards
        self.ranks_collection()
        self.suits_collection()
        self.straight_collection()

    def ranks_collection(self):
        self.ranks_list = [rank[:-1] for rank in self.cards.split()]
        self.ranks_dict = {k:self.ranks_list.count(k) for k in self.ranks_list}
    
    def suits_collection(self):
        suits_list = [suit[-1:] for suit in self.cards.split()]
        self.suits_dict = {k:suits_list.count(k) for k in suits_list}

    def straight_collection(self):
        straight_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.collection_for_straight = [sorted(straight_list[0 + straight: 5 + straight]) for straight in range(10)]
        
    def total_ranks(self):
        return len(self.ranks_dict.values())
        
    def high_card(self):
        if self.total_ranks() == 5:
            return "High Card"
    
    def one_pair(self):
        if 2 in self.ranks_dict.values() and self.total_ranks() == 4:
            return "One Pair"

    def two_pair(self):
        if 2 in self.ranks_dict.values() and self.total_ranks() == 3:
            return "Two Pair"

    def three_of_a_kind(self):
        if 3 in self.ranks_dict.values() and self.total_ranks() == 3:
            return "Three Of A Kind"

    def straight(self):
        if sorted(self.ranks_list) in self.collection_for_straight:
            return "Straight"

    def flush(self):
        if 5 in self.suits_dict.values():
            return "Flush"

    def full_house(self):
        if 3 in self.ranks_dict.values() and 2 in self.ranks_dict.values():
            return "Full House"

    def four_of_a_kind(self):
        if 4 in self.ranks_dict.values() and 1 in self.ranks_dict.values():
            return "Four Of A Kind"
        
    def straight_flush(self):
        if sorted(self.ranks_list) in self.collection_for_straight and 5 in self.suits_dict.values():
            return "Straight Flush"

    def royal_flush(self):
        if sorted(self.ranks_list) == sorted(["10", "J", "Q", "K", "A"]) and 5 in self.suits_dict.values():
            return "Royal Flush"





# ranks = [
#     Player1("2", 1),
#     Player1("3", 2),
#     Player1("4", 3),
#     Player1("5", 4),
#     Player1("6", 5),
#     Player1("7", 6),
#     Player1("8", 7),
#     Player1("9", 8),
#     Player1("10", 9),
#     Player1("J", 10),
#     Player1("Q", 11),
#     Player1("K", 12),
#     Player1("A", 13),
# ]
        
# cards = Card()
# ranks = cards.get_rank()
# hand = Pokerhand(pokerhands)