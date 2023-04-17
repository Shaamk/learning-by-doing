from pure_poker import get_description_for_poker_hand

def main():

    user_data = input("What's your hand ?")
    thing_to_print = get_description_for_poker_hand(user_data)
    print(thing_to_print)

def get_desciption_for_poker_hand():
    pass

if __name__ =='__main__':
    main()