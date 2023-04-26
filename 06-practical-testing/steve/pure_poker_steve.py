def description_poker_hand(user_input):
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 14:
        return 'Invalid Input'
    
    frequency_ranks = {}
    frequency_suits = {}
    ranks_list = [i[:1] for i in user_input.split()]    # list with all ranks
    suits_list = [i[1:2] for i in user_input.split()]   # list with all suits

    
    for rank in ranks_list:
        if rank not in frequency_ranks:     # dictionary counted ranks 
            frequency_ranks[rank] = 0
        frequency_ranks[rank] += 1

    for suit in suits_list:
        if suit not in frequency_suits:     # dictionary counted suits 
            frequency_suits[suit] = 0
        frequency_suits[suit] += 1
    
    return return_card_function(frequency_ranks, frequency_suits)

def return_card_function(frequency_ranks, frequency_suits):
    number_of_ranks = len(frequency_ranks)
    number_of_suits = len(frequency_suits)

    checks = ((check_for_royal_flush, 'Royal Flush'),
              (check_for_straight_flush, 'Straight Flush'),
              (check_for_four_of_a_kind, 'Four Of A Kind'),
              (check_for_full_house, 'Full House'),
              (check_for_flush, 'Flush'),
              (check_for_straight, 'Straight'),
              (check_for_three_of_a_kind, 'Three of a Kind'),
              (check_for_two_pair, 'Two Pair'),
              (check_for_one_pair, 'One Pair'),
              (check_for_high_card, 'High Card'))
    
    for check_function, value in checks:
        if check_function(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
            return_card = value
            break

    return return_card

def check_for_royal_flush(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    ranks = list(frequency_ranks.keys())
    royal_flush = [['10', 'J', 'Q', 'K', 'A']]
    for item in royal_flush:
        if item == ranks and number_of_suits == 1:
            return True

def check_for_straight_flush(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    ranks = list(frequency_ranks.keys())
    straight = [['A', '2', '3', '4', '5'],['2', '3', '4', '5', '6'],['3', '4', '5', '6', '7'],['4', '5', '6', '7', '8'],['5', '6', '7', '8', '9'],['10', '6', '7', '8', '9'],['10', '7', '8', '9', 'J'],['10', '8', '9', 'J', 'Q'],['10', '9', 'J', 'Q', 'K'],['10', 'J', 'Q', 'K', 'A']]
    for item in straight:
        if item == ranks and number_of_suits == 1:
            return True

def check_for_four_of_a_kind(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_ranks == 2 and 4 in frequency_ranks.values()

def check_for_full_house(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_ranks == 2 and 3 in frequency_ranks.values()

def check_for_flush(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_suits == 1

def check_for_straight(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    ranks = list(frequency_ranks.keys())
    straight = [['A', '2', '3', '4', '5'],['2', '3', '4', '5', '6'],['3', '4', '5', '6', '7'],['4', '5', '6', '7', '8'],['5', '6', '7', '8', '9'],['10', '6', '7', '8', '9'],['10', '7', '8', '9', 'J'],['10', '8', '9', 'J', 'Q'],['10', '9', 'J', 'Q', 'K'],['10', 'J', 'Q', 'K', 'A']]
    for item in straight:
        if item == ranks:
            return True

def check_for_one_pair(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_ranks == 4

def check_for_two_pair(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_ranks == 3

def check_for_three_of_a_kind(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return number_of_ranks == 3 and 3 in frequency_ranks.values()

def check_for_high_card(number_of_ranks, frequency_ranks, number_of_suits, frequency_suits):
    return True

