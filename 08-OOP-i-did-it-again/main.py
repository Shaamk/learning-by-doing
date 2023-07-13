from card_class import Card
from players_class import Players
from pokerhand_class import Pokerhand



def function():
    pass
    # Are we aloud to make a function here ?
    


def main():


    check_card_of_player = Card('')
    player1 = check_card_of_player.card
    player1 = input("Enter Player 1's cards: ")
    check_card_of_player.card = input("Enter Player 2's cards: ")    
    check_card_of_player.invalid_input(player1)
    check_card_of_player.invalid_input(check_card_of_player.card)
    get_hand_of_player = Players('')
    get_hand_of_player.cards
    



if __name__ == '__main__':
    main()

