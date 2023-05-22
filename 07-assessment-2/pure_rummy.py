def has_rummy(user_input):
    invalid = check_for_invalid(user_input)
    if invalid is not None:
        return invalid
    else:
        get_rummy_hand(user_input)

    
def check_for_invalid(user_input):
    valid_suits = ['C', 'D', 'H', 'S']
    valid_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 20 or len(user_input) > 20 or user_input[:-1] not in valid_suits or user_input[-1:] not in valid_ranks:
        return 'Sorry, that is invalid'
    

def get_rummy_hand(user_input):
    ranks_count = get_ranks(user_input)
    suits_count = get_suits(user_input)
    



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



