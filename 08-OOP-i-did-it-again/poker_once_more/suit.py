class Suit:
    def __init__(self, suit) -> None:
        self.suit = suit
        self.valid = ['S', 'H', 'C', 'D']
        self.check_invalid()

    def check_invalid(self):
        if self.suit not in self.valid:
            raise ValueError()
    
    def __eq__(self, other: object) -> bool:
        return self.suit == other.suit