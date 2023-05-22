from random import choices

def choosing_function(questions, number_to_choose=5):
    return choices(questions, k=number_to_choose)