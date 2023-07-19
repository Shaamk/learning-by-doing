from card_class import Card
from players_class import Player


def main():



    player_1_input = input("Enter Player 1's cards: ")
    player_2_input = input("Enter Player 2's cards: ")

    player_1 = Player(player_1_input)
    player_2 = Player(player_2_input)

    p1 = player_1.get_hand()
    p2 = player_2.get_hand()
    print(type(p1))
    print(p1)
    if p1 > p2:
        print(f"Player 1 wins!\n{p1.hand} is better than {p2.hand}")
    else:
        print(f"Player 2 wins!\n{p2.hand} is better than {p1.hand}")



if __name__ == '__main__':
    main()



#   > Enter Player 1's cards: 10H 10C 4H 4S 10S
#   > Enter Player 2's cards: AH 3H 2H 5H 4H
#   > Player 2 wins!
#   > A Straight Flush beats A Full House!