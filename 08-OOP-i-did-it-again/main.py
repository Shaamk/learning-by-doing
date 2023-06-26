from card_class import do_something

def main():



    player1 = input("Enter Player 1's cards: ")
    player2 = input("Enter Player 2's cards: ")
    message1, message2 = do_something(player1, player2)
    print(message1, message2)



if __name__ == '__main__':
    main()