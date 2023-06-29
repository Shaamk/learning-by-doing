class Pokerhand:
    def __init__(self, pokerhands):
        self.hands_of_poker = []
        if pokerhands:
            for pokerhand in pokerhands:
                self.hands_of_poker.append(pokerhand)


pokerhands = [
    Pokerhand("High Card", 1),
    Pokerhand("One Pair", 2),
    Pokerhand("Two Pair", 3),
    Pokerhand("Three of a kind", 4),
    Pokerhand("Straight", 5),
    Pokerhand("Flush", 6),
    Pokerhand("Full House", 7),
    Pokerhand("Four of A Kind", 8),
    Pokerhand("Straight Flush", 9),
    Pokerhand("Royal Flush", 10),
]
