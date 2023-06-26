# > Enter Player 1's cards: 10H 10C 4H 4S 10S
# > Enter Player 2's cards: AH 3H 2H 5H 4H
# > Player 2 wins!
# > A Straight Flush beats A Full House!


# user
# shorthand strings
# hand of cards
# card
# 5 cards


# class Card
    # rank
    # suit


# class PokerHand
    # the bunch of pokerhands
    # compare hand of players
    # return the win


# class Player1
    # get cards of player1
    # check cards to sort out the hand
    # get from the bunch of pokerhands the ranking of the player - happens in class PokerHand


# class Player2
    # get cards of player2
    # check cards to sort out the hand
    # get from the bunch of pokerhands the ranking of the player - happens in class PokerHand


class Card:
    # rank, suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    

