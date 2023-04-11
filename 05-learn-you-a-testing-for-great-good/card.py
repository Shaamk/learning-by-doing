def parse_card(card):
    card_dict = {}
    if card[0] == 'A':
        card_dict["rank"] = "ace"
    elif card[0] == 'K':
        card_dict["rank"] = "king"
    elif card[0] == 'Q':
        card_dict["rank"] = "queen"        
    elif card[0] == 'J':
        card_dict["rank"] = "jack"
    elif card[0] == '1':
        card_dict["rank"] = "10"
    else:
        card_dict["rank"] = card[0]
        

    if card[1] == 'C':
        card_dict["suit"] = "clubs"
    elif card[1] == 'D':
        card_dict["suit"] = "diamonds"
    elif card[1] == 'H':
        card_dict["suit"] = "hearts"    
    elif card[1] == 'S':
        card_dict["suit"] = "spades"
        

    if card[0] == 'A':
        card_dict["description"] = "an ace"
    elif card[0] == 'K':
        card_dict["description"] = "a king"        
    elif card[0] == 'Q':
        card_dict["description"] = "a queen"        
    elif card[0] == 'J':
        card_dict["description"] = "a jack"        
    elif card[0] == '10':
        card_dict["description"] = "a ten"        
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


    if card[1] == 'C':
        card_dict["description"] += " of clubs"
    elif card[1] == 'D':
        card_dict["description"] += " of diamonds"        
    elif card[1] == 'H':
        card_dict["description"] += " of hearts"        
    elif card[1] == 'S':
        card_dict["description"] += " of spades"  
    
    # ranks_list = ['a two ', 'a three ', 'a four ', 'a five ', 'a six ', 'a seven ', 'an eight ', 'a nine ', 'a ten ']
    
    # if not isinstance(card):
    #     raise ValueError('Oh my God, what happend!')

    return card_dict
