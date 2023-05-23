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
    
    

def get_rummy_hand(user_input):
    ranks_count = get_ranks(user_input)
    suits_count = get_suits(user_input)
    three_ranks = three_of_a_kind(ranks_count)
    four_ranks = four_of_a_kind(ranks_count)
    straight_three = straight_of_three(suits_count, ranks_count)
    straight_four = straight_of_four(suits_count, ranks_count)
    return three_ranks, four_ranks, straight_three, straight_four

def check_for_winning_hand(three_ranks, four_ranks, straight_three, straight_four):
    if three_ranks:
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


def get_suits(user_input):
    suits_count = {}
    suits_list = [suit[-1:] for suit in user_input.split()]
    for suit in suits_list:
        if suit not in suits_count:
            suits_count[suit] = 0
        suits_count[suit] += 1
    return suits_count


def three_of_a_kind(ranks_count):
    return 3 in ranks_count.values()


def four_of_a_kind(ranks_count):
    return 4 in ranks_count.values()


def straight_of_three(suits_count, ranks_count):
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    given_ranks = sorted(ranks_count.keys())
    for three in range(11):
        makes_three = ranks[0 + three: 3 + three]
        if given_ranks == makes_three and 3 in suits_count.values():
            return True


def straight_of_four(suits_count, ranks_count):
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    given_ranks = sorted(ranks_count.keys())
    for four in range(10):
        makes_four = ranks[0 + four: 4 + four]
        if given_ranks == makes_four and 4 in suits_count.values():
            return True
    

