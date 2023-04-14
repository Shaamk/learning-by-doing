# 5 ramdom choices of the quizz             = working
# shows answers shuffeled                   = working
# stops after 5 quistions                   = working
# shows high score                          = working
# stores count for 5 times at scoreboard    = working


import random


def main():
    game_data = getting_the_text()
    quiz_data = saving_as_data(game_data)
    start_game(quiz_data)    


def getting_the_text():
    game_data = []
    with open('04-assessment-1/questions.txt', 'rt') as get_text:
        all_questions = get_text.read()
        game_data = all_questions.splitlines()
        del game_data[-1]
        return game_data


def saving_as_data(game_data):
    quiz_data = []
    for i in range(len(game_data)):
        if i % 3 == 0:
            quiz = {}
            quiz["question"] = game_data.pop(0)
            quiz["answers"] = game_data.pop(0)
            quiz["correct"] = game_data.pop(0)
            quiz_data.append(quiz)
    return quiz_data


def start_game(quiz_data):
    score = 0
    game = 5
    while game > 0:
        score = go_quiz(quiz_data, score)
        game -= 1
    score = save_player_score(score)        


def go_quiz(quiz_data, score):
    quiz_set = random.choice(quiz_data)
    correct_answer = quiz_set["correct"]
    question = quiz_set["question"]        
    answers = quiz_set["answers"]
    answers_list = answers.split(", ")
    random.shuffle(answers_list)
    abcd = ['A.', 'B.', 'C.', 'D.']

    print(correct_answer)
    print(question)
    for x, y in zip(abcd, answers_list):
        print(x, y)
    option = input("Your answer: ")
    option = option.upper()
    if option == "A":
        if answers_list[0] == correct_answer:
            score += 1
            print("Goooood guess !")
        else:
            print("incorrect !")
    elif option == "B":
        if answers_list[1] == correct_answer:
            score += 1
            print("Goooood guess !")
        else:
            print("incorrect !")
    elif option == "C":
        if answers_list[2] == correct_answer:
            score += 1
            print("Goooood guess !")
        else:
            print("incorrect !")
    elif option == "D":
        if answers_list[3] == correct_answer:
            score += 1
            print("Goooood guess !")
        else:
            print("incorrect !")
    
    print(f'Your score: {score}')
    print()
    return score


def save_player_score(score):
    print(f'Final score: {score}')
    player_score = []
    new_score = {}
    new_score["name"] = input("You set the high score! What is your name?: ")
    new_score["score"] = score
    player_score.append(player_score)
    for player in player_score:
        print(f'{player["name"]} {player["score"]}')
    return player_score

    

if __name__ == "__main__":
    main()




# Which of the following words describes cats?
# A. Caprine
# B. Feline
# C. Bovine
# D. Canine
# Your guess? > d
# Incorrect!
# Final score: 3
# You set the high score! What is your name? > Shaam

