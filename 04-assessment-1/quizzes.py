# 5 ramdom choices of the quizz
# shows the answers randomly
# stores 5 times if correct for the scoreboard
# stops after 5 quistions
# shows high score


import random

def main():
    game_data = getting_the_text()
    quiz_data = saving_as_data(game_data)
    start_quiz( quiz_data)



def getting_the_text():
    game_data = []
    with open('04-assessment-1/questions.txt', 'rt') as get_text:
        all_questions = get_text.read()
        #print(questions)
        game_data = all_questions.splitlines()
        del game_data[-1]
        #print(game_data)
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
    return random.choice(quiz_data)


def start_quiz(quiz_data):
    the_question = quiz_data["question"]
    keys = ["answers"]
    the_answers_list = [quiz_data["answers"] for key in keys if key in quiz_data]
    print(the_question)
    for answers in range(len(the_answers_list)):
        print(answers)
    print(the_answers_list)

    # I'm trying to.. dont know how to make the print look like as the example


    


def player_score():
    pass




if __name__ == "__main__":
    main()