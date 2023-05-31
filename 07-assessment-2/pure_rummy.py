def has_rummy(user_input):
    invalid = check_for_invalid(user_input)
    if invalid is not None:
        return invalid
    else:
        output = get_rummy_hand(user_input)
        return output

    
def check_for_invalid(user_input):
    valid_suits = ['C', 'D', 'H', 'S']
    valid_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    if not isinstance(user_input, str) or user_input == '' or len(user_input.split()) != 7:
        return 'Sorry, that is invalid'
    for valid in user_input.split():
        if valid[-1] not in valid_suits:
            return 'Sorry, that is invalid'
    
    

def get_rummy_hand(user_input):
    ranks_count = get_ranks(user_input)
    three_ranks = three_of_a_kind(ranks_count)
    four_ranks = four_of_a_kind(ranks_count)
    ranks, ranks_sorted_straight_list, straight_list = getting_the_straight(ranks_count, user_input)
    suits_max = get_suits(straight_list)
    straight_three = straight_of_three(ranks, ranks_sorted_straight_list, suits_max)
    straight_four = straight_of_four(ranks, ranks_sorted_straight_list, suits_max)
    straight_seven = staight_with_three_and_four(ranks, ranks_sorted_straight_list, suits_max)
    output = check_for_winning_hand(three_ranks, four_ranks, straight_three, straight_four, straight_seven)
    return output


def check_for_winning_hand(three_ranks, four_ranks, straight_three, straight_four, straight_seven):
    if three_ranks and straight_four or straight_three and straight_four or three_ranks and four_ranks or straight_three and four_ranks:
        return 'WIN'
    elif straight_seven:
        return 'WIN'
    else:
        return 'LOSE'


def get_ranks(user_input):
    ranks_count = {}
    ranks_list = [rank[:-1] for rank in user_input.split()]
    for rank in ranks_list:
        if rank not in ranks_count:
            ranks_count[rank] = 0
        ranks_count[rank] += 1
    return ranks_count


def get_suits(straight_list):
    suits_count = {}
    suits_list = [suit[-1] for suit in straight_list]
    for suit in suits_list:
        if suit not in suits_count:
            suits_count[suit] = 0
        suits_count[suit] += 1
    suits_max = max(suits_count.values())
    return suits_max


def three_of_a_kind(ranks_count):
    return 3 in ranks_count.values()


def four_of_a_kind(ranks_count):
    return 4 in ranks_count.values()


def getting_the_straight(ranks_count, user_input):
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    straight_ranks = {k: v for k, v in ranks_count.items() if v == 1}   # if all the values = 1 , then its good for a straight 7
    ranks_sorted_straight_list = sorted(straight_ranks.keys())
    unwanted_string = max(ranks_count, key=ranks_count.get)  # getting the key with the maximum value
    straight_list = sorted([x for x in user_input.split() if unwanted_string not in x]) # make a new list for the sraight
    return ranks, ranks_sorted_straight_list, straight_list


def straight_of_three(ranks, ranks_sorted_straight_list, suits_max):
    for three in range(11):
        makes_three = sorted(ranks[0 + three: 3 + three])
        if ranks_sorted_straight_list == makes_three and suits_max == 3:
            return True


def straight_of_four(ranks, ranks_sorted_straight_list, suits_max):
    for four in range(10):
        makes_four = sorted(ranks[0 + four: 4 + four])
        if ranks_sorted_straight_list == makes_four and suits_max == 4:
            return True


def staight_with_three_and_four(ranks, ranks_sorted_straight_list, suits_max):
    for seven in range(7):
        makes_seven = sorted(ranks[0 + seven: 7 + seven])
        if ranks_sorted_straight_list == makes_seven and suits_max == 6:
            return True