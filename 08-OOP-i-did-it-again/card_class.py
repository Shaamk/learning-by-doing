class Card:
    def __init__(self, card):
        self.card = card
        self.invalid_input()
        self.get_rank()
        self.get_suit()

    def __str__(self):      # actualy not needed
        return str(self.card)
    
    def get_rank(self):
        self.rank = self.card[:-1]
        return self.rank

    def get_suit(self):
        self.suit = self.card[-1:]
        return self.suit

    def invalid_input(self):    # to players class
        suits_list = ["C", "D", "H", "S"]
        ranks_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if not isinstance(self.card, str) or self.card == "":
            raise TypeError("Invalid Input")
        elif len(self.card.split()) != 5:
            return "Invalid Input"
        for card in self.card.split():
            if card[:-1] not in ranks_list or card[-1:] not in suits_list:
                return "invalid Input"
        return self.card
    