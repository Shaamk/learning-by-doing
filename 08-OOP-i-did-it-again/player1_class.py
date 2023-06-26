

class Player1:
    def __init__(self, player1):
        self.player1 = player1
    
    
    def get_player1_hand(self):
        self.player1_frequency_ranks = {}
        self.player1_frequency_suits = {}
        player1_ranks_list = [i[:-1] for i in self.player1.split()]   # list with all ranks
        player1_suits_list = [i[-1:] for i in self.player1.split()]   # list with all suits

        for rank in player1_ranks_list:
            if rank not in self.player1_frequency_ranks:
                self.player1_frequency_ranks[rank] = 0
            self.player1_frequency_ranks += 1

        for suit in player1_suits_list:
            if suit not in self.player1_frequency_suits:
                self.player1_frequency_suits[suit] = 0
            self.player1_frequency_suits += 1