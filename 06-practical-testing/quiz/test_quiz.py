# quiz program!!!
#
# show player high score and name of high scoring player
# - read high score from file <- input
# - format high score for printing <- process
# - print the high score <- output
#
# read questions from file and put them n a data structure
# - read data from file <- input
# - put them in records <- process
# 
# choose five of these questions
# - get the computer to choose five random numbers <-input
# # we need to show the answers in a random order each time
# # # choose random order <- input
# - choose the questions that match those numbers <- process
# # # put answers in that order <- process

from pure_quiz import choosing_function
from random import seed

def test_random_questions_are_chosen():
    # some qusetions
    questions = [
        {'q': 'Who am I?', 'p': ['dan', 'shaam', 'carla', 'Lady gaga'], 'a': 'dan'},
        {'q': 'Who is shaam?', 'p': ['what', 'why', 'huh', 'shaam'], 'a': 'shaam'},
        {'q': 'Carlas fave cake?', 'p': ['choc', 'vanilla', 'liver', 'squirrel'], 'a': 'choc'},
        {'q': 'Is this a question?', 'p': ['no', 'yes', 'yes, if this is the answer', 'oh, fuck off'], 'a': 'yes, if this is the answer'}
    ]

    # seed the generator, so this wil work always the same way
    seed(7)
    # call the choosing function
    result1 = choosing_function(questions, 2)
    # rember the order
    # cal the choosing function again
    result2 = choosing_function(questions, 2)
    # check second order is different
    assert result1 != result2
    # check that there are five
    assert len(result1) == 2
    assert len(result2) == 2

# write test asking for many questions


# ask the player to answer these questions
# # print the questions <- output
# # print the answers <- output
# # get the answer from the player <- input
# # convert player's string into a actual miltiple choice <- process
# # # player's feedback is that they're correct <- process
# # if it is right they score a point <- process
# # if it's wrong, <- process
# # # players's feedback is that the correct answers is X <- process
# #  print player's feedback <-output
#
# tell player their final score <- output
# if their score is at least equal to or the high score, replace high score
# # check the score against the previos one <- process
# # if needed, get their name <- input
# # write name and score to high score file <- output











# 1.17 uur