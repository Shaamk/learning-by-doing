class Pokerhand:
    def __init__(self, hand, rating):
        self.hand = hand
        self.rating = rating
    
    def __str__(self):
        return f"{self.hand}, {self.rating}"
    
    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating
    

# other = [
#     Pokerhand("High Card", 1),
#     Pokerhand("One Pair", 2),
#     Pokerhand("Two Pair", 3),
#     Pokerhand("Three of a kind", 4),
#     Pokerhand("Straight", 5),
#     Pokerhand("Flush", 6),
#     Pokerhand("Full House", 7),
#     Pokerhand("Four Of A Kind", 8),
#     Pokerhand("Straight Flush", 9),
#     Pokerhand("Royal Flush", 10),
# ]
