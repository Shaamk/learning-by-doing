class Card:
    def __init__(self, card):
        self.card = card
        self.invalid_input()
        self.get_rank()
        self.get_suit()


    def __str__(self):
        return str(self.card)
    
    def get_rank(self):
        self.rank = self.card[:-1]
        return self.rank

    def get_suit(self):
        self.suit = self.card[-1:]
        return self.suit

    def invalid_input(self):
        suits_list = ["C", "D", "H", "S"]
        ranks_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if not isinstance(self.card, str) or self.card == "":
            raise TypeError("Invalid Input")
        elif len(self.card.split()) != 5 or self.rank not in ranks_list or self.suit not in suits_list:
            return "Invalid Input"
        return self.card

        
    # def play_poker(self, player1, player2):
    #     message1, message2 = get_pokerhand(player1, player2)
    #     return message1, message2


# invalid input : string ?