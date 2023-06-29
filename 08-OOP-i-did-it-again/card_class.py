class Card:
    def __init__(self, card):
        self.card = card
        self.get_rank()
        self.get_suit()
        self.invalid_input()
        self.play_poker()

    def __str__(self):
        return str(self.card)    
    
    def get_rank(self):
        if not isinstance(self.card, str):
            return "Invalid Input"
        self.rank = self.card[:-1]
        return self.rank

    def get_suit(self):
        if not isinstance(self.card, str):
            return "Invalid Input"
        self.suit = self.card[-1:]
        return self.suit

    def invalid_input(self):
        suits_list = ["C", "D", "H", "S"]
        ranks_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if not isinstance(self.card, str) or self.card == "" or self.card[:-1] in suits_list or self.card[-1:] in ranks_list or len(self.card.split()) != 5:
            return "Invalid Input"
        
    def play_poker():
        pass
