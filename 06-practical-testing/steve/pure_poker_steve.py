def description_poker_hand(user_input):
    if not isinstance(user_input, str) or user_input == '' or len(user_input) < 14:
        return 'Invalid Input'
    frequency_ranks = {}

    ranks_list = [i[:1] for i in user_input.split()]
    for rank in ranks_list:
        if rank not in frequency_ranks:
            frequency_ranks[rank] = 1
        else:
            frequency_ranks[rank] += 1
    if len(frequency_ranks) == 4:
        return "One Pair"
    return "High Card"