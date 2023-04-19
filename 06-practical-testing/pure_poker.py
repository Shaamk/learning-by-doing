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
        parsed_cards_ranks = []
        parsed_cards_suits = []
        for card in cards:
            try:
                #card = parse_card(card)
                parsed_cards.append(parse_card(card))
            
            except ValueError:
                return "Sorry, that's invalid"
            ranks_list = for_counting_ranks(parsed_cards)
            
            
            # parsed_cards_ranks.append(parse_card["rank"])
            # parsed_cards_suits.append(parse_card["suit"])
            # ranks_list = for_counting_ranks(parsed_cards_ranks)
            # parsed_cards_suits = for_counting_suits(parsed_cards_suits)

            if ranks_list == [1, 1, 1, 1, 1]:
                return "High card"
            elif ranks_list == [1, 1, 1, 2, 2]:
                return "One pair"            
            elif ranks_list == [1, 2, 2]:
                return "Two pair"
            elif ranks_list == [1, 1, 3]:
                return "Three of a kind"
            elif ranks_list == [1, 1, 1, 1, 1]:
                return "Straight"

            # if len(parsed_cards_ranks) == 5:
            #     return "High card"
            # elif len(parsed_cards_ranks) == 4:
            #     return "One pair"            
            # elif len(parsed_cards_ranks) == 3:
            #     return "Two pair"
            #print(parsed_cards) # list met dictionaries
            #print(ranks_list)


def for_counting_ranks(parsed_cards):
    ranks_list = []
    counting_ranks = {}
    for card in parsed_cards:
        ranks = card["rank"]
        for card in ranks:
            if card not in counting_ranks:
                counting_ranks[card] = 1
            else:
                counting_ranks[card] += 1
    #print(counting_ranks)
    for numbers in counting_ranks:
        ranks_list.append(counting_ranks[numbers])
    ranks_list.sort()
    print(ranks_list)
    return ranks_list

# def for_counting_ranks(parsed_cards):
#     counting_ranks = {}
#     ranks_list = []
#     for card in parsed_cards:
#         if card not in counting_ranks:
#             counting_ranks[card] = 1
#         else:
#             counting_ranks[card] += 1
#     print(counting_ranks)
#     for numbers in counting_ranks:
#         ranks_list.append(counting_ranks[numbers])

#     print(ranks_list)
#     return ranks_list


def for_counting_suits(parsed_cards_suits):
    counting_suits = {}
    suits_list = []
    for card in parsed_cards_suits:
        if card not in counting_suits:
            counting_suits[card] = 1
        else:
            counting_suits[card] += 1
    print(counting_suits)
    for numbers in counting_suits:
        suits_list.append(counting_suits[numbers])

    print(suits_list)
    return suits_list

