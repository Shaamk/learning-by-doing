def get_description_for_poker_hand(user_data):
    if user_data == None:
        return "Sorry, that's invalid"
    elif user_data == "":
        return "Sorry, that's invalid"
    elif len(user_data) < 14 or len(user_data) > 18:
        return "Sorry, that's invalid"


def parse_card(card):
    card_dict = {}
    if type(card) != str or len(card) <1:
        raise ValueError()
    elif card == card.lower():
        raise ValueError()    
    elif len(card) < 2 or len(card)> 3:
        raise ValueError()
    elif len(card) == 3:
        if card[:2] != "10":
            raise ValueError()
    elif len(card) == 2:
        if card[:1] == "1":
            raise ValueError()

    if len(card) == 2:
        if card[0] == 'A':
            card_dict["rank"] = "ace"
        elif card[0] == 'K':
            card_dict["rank"] = "king"
        elif card[0] == 'Q':
            card_dict["rank"] = "queen"        
        elif card[0] == 'J':
            card_dict["rank"] = "jack"
        elif card[0] == '9':
            card_dict["rank"] = "9"
        elif card[0] == '8':
            card_dict["rank"] = "8"
        elif card[0] == '7':
            card_dict["rank"] = "7"
        elif card[0] == '6':
            card_dict["rank"] = "6"
        elif card[0] == '5':
            card_dict["rank"] = "5"
        elif card[0] == '4':
            card_dict["rank"] = "4"
        elif card[0] == '3':
            card_dict["rank"] = "3"
        elif card[0] == '2':
            card_dict["rank"] = "2"

        if card[1] == 'C':
            card_dict["suit"] = "clubs"
        elif card[1] == 'D':
            card_dict["suit"] = "diamonds"
        elif card[1] == 'H':
            card_dict["suit"] = "hearts"    
        elif card[1] == 'S':
            card_dict["suit"] = "spades"
        else:
            raise ValueError()
        if card[0] == 'A':
            card_dict["description"] = "an ace"
        elif card[0] == 'K':
            card_dict["description"] = "a king"        
        elif card[0] == 'Q':
            card_dict["description"] = "a queen"        
        elif card[0] == 'J':
            card_dict["description"] = "a jack"       
        elif card[0] == '9':
            card_dict["description"] = "a nine"        
        elif card[0] == '8':
            card_dict["description"] = "an eight"
        elif card[0] == '7':
            card_dict["description"] = "a seven"        
        elif card[0] == '6':
            card_dict["description"] = "a six"        
        elif card[0] == '5':
            card_dict["description"] = "a five"
        elif card[0] == '4':
            card_dict["description"] = "a four"        
        elif card[0] == '3':
            card_dict["description"] = "a three"        
        elif card[0] == '2':
            card_dict["description"] = "a two"
        else:
            raise ValueError()

        if card[1] == 'C':
            card_dict["description"] += " of clubs"
        elif card[1] == 'D':
            card_dict["description"] += " of diamonds"        
        elif card[1] == 'H':
            card_dict["description"] += " of hearts"        
        elif card[1] == 'S':
            card_dict["description"] += " of spades"

        
    elif len(card) == 3:
        if card[:2] == "10":
            card_dict["rank"] = "10"
            card_dict["description"] = "a ten"
        if card[2] == 'C':
            card_dict["suit"] = "clubs"
        elif card[2] == 'D':
            card_dict["suit"] = "diamonds"
        elif card[2] == 'H':
            card_dict["suit"] = "hearts"    
        elif card[2] == 'S':
            card_dict["suit"] = "spades"    
        if card[2] == 'C':
            card_dict["description"] += " of clubs"
        elif card[2] == 'D':
            card_dict["description"] += " of diamonds"        
        elif card[2] == 'H':
            card_dict["description"] += " of hearts"        
        elif card[2] == 'S':
            card_dict["description"] += " of spades"
        else:
            raise ValueError()


    return card_dict
