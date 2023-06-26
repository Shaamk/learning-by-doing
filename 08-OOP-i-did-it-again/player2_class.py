

class Player2:
    def __init__(self, player2):
        self.player2 = player2
    
    
    def get_player2_hand(self):
        self.player2_frequency_ranks = {}
        self.player2_frequency_suits = {}
        player1_ranks_list = [i[:-1] for i in self.player2.split()]   # list with all ranks
        player1_suits_list = [i[-1:] for i in self.player2.split()]   # list with all suits

        for rank in player1_ranks_list:
            if rank not in self.player2_frequency_ranks:
                self.player2_frequency_ranks[rank] = 0
            self.player2_frequency_ranks += 1

        for suit in player1_suits_list:
            if suit not in self.player2_frequency_suits:
                self.player2_frequency_suits[suit] = 0
            self.player2_frequency_suits += 1