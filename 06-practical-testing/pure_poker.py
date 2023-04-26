from card import parse_card

def get_description_for_poker_hand(user_data):
    if user_data == None:
        return "Sorry, that's invalid"
    elif user_data == "":
        return "Sorry, that's invalid"
    elif len(user_data) < 14 or len(user_data) > 18:
        return "Sorry, that's invalid"
    elif len(user_data) > 14 or len(user_data) < 18:
        cards = user_data.split()
        parsed_cards = []
        for card in cards:
            try:
                parsed_cards.append(parse_card(card))                
            
            except ValueError:
                return "Sorry, that's invalid"
        
        ranks_list, parsed_cards_ranks = for_counting_ranks(parsed_cards)
        suits_list = for_counting_suits(parsed_cards)
        straight_ranks = for_a_straight()
        royal_flush_ranks = for_a_royal_flush()       
        
        # complex naar simpel
        if suits_list == [5] and parsed_cards_ranks in royal_flush_ranks:
            return "Royal Flush"
        elif suits_list == [5] and parsed_cards_ranks in straight_ranks:
            return "Straight Flush"
        elif suits_list == [5]:
            return "Flush"
        elif ranks_list == [1, 4]:
            return "Four of a kind"
        elif ranks_list == [2, 3]:
            return "Full House"
        elif ranks_list == [1, 1, 1, 1, 1] and parsed_cards_ranks in straight_ranks:
            return "Straight"
        elif ranks_list == [1, 1, 3]:
            return "Three of a kind"
        elif ranks_list == [1, 2, 2]:
            return "Two pair"
        elif ranks_list == [1, 1, 1, 2]:
            return "One pair"            
        elif ranks_list == [1, 1, 1, 1, 1]:
            return "High card"
        

def for_counting_ranks(parsed_cards):
    #print(parsed_cards)
    ranks_list = []
    parsed_cards_ranks = []
    counting_ranks = {}
    for ranks in parsed_cards:
        card_ranks = ranks["rank"]
        parsed_cards_ranks.append(card_ranks)
    parsed_cards_ranks.sort()
    print(f'parsed_cards_ranks {parsed_cards_ranks}')

    for cards_ranks in parsed_cards_ranks:
        if cards_ranks in counting_ranks:
            counting_ranks[cards_ranks] += 1
        else:
            counting_ranks[cards_ranks] = 1
    #print(f'counting_ranks {counting_ranks}')

    for numbers in counting_ranks:
        ranks_list.append(counting_ranks[numbers])
    ranks_list.sort()
    print(f'ranks_list {ranks_list}')    
    return ranks_list, parsed_cards_ranks


def for_counting_suits(parsed_cards):
    #print(parsed_cards)
    suits_list = []
    parsed_cards_suits = []
    counting_suits = {}
    for suits in parsed_cards:
        card_suits = suits["suit"]
        parsed_cards_suits.append(card_suits)
    #print(f'parsed_cards_suits {parsed_cards_suits}')
    
    for cards_suits in parsed_cards_suits:
        if cards_suits in counting_suits:
            counting_suits[cards_suits] += 1
        else:
            counting_suits[cards_suits] = 1
    #print(f'counting_suits {counting_suits}')
    
    for numbers in counting_suits:
        suits_list.append(counting_suits[numbers])
    suits_list.sort()
    print(f'suits_list {suits_list}')
    return suits_list


def for_a_royal_flush():
    royal_flush_ranks = [['10', 'A', 'J', 'K', 'Q']]
    return royal_flush_ranks


def for_a_straight():
    straight_ranks = [
        ['10', 'A', 'J', 'K', 'Q'],
        ['10', '9', 'J', 'K', 'Q'],
        ['10', '8', '9', 'J', 'Q'],
        ['10', '7', '8', '9', 'J'],
        ['10', '6', '7', '8', '9'],
        ['5', '6', '7', '8', '9'],
        ['4', '5', '6', '7', '8'],
        ['3', '4', '5', '6', '7'],
        ['2', '3', '4', '5', '6'],
        ['2', '3', '4', '5', 'A']
    ]
    return straight_ranks

