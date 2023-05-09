def check_if_invalid(user_input):
    if user_input is None or not str(user_input).isalpha() :
        return 'Sorry that is invalid'
    return None


def build_word_grid(word):
    word_list = []      # ['Pot', 'pOt', 'poT']
    for i in range(len(word)):
        previous_letters_lower = word[:i].lower()
        capital_letter = word[i].upper()
        last_letters_lowered = word[i+1:].lower()
        word = previous_letters_lower + capital_letter + last_letters_lowered
        word_list.append(word)
    return word_list    # ['Pot', 'pOt', 'poT']


# def build_word_grid(word):
#     word_list = [i for i in range(len(word)) word[:i].lower() + word[i].upper() + word[i+1:].lower()]
#     return word_list