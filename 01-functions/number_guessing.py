import random


def main():
    guesses = playing_game()    # calling playing game function, the returned value is assigned to guesses 
    lose_check(guesses)         # passed guesses as a argument


def playing_game():
    guesses = 6
    guess_the_number = random.randint(1, 101)
    number_to_guess = int(input("Guess the number between 1 and 100: "))
    while guess_the_number != number_to_guess and guesses > 0:
        print(f"guesses remaining {guesses}")
        if number_to_guess > guess_the_number:
            print("The guessed number", number_to_guess, "is too high")
            number_to_guess = int(input("Guess the number between 1 and 100: "))

        else:
            print("The guessed number", number_to_guess,"is too low")
            number_to_guess = int(input("Guess the number between 1 and 100: "))

        winner_check(number_to_guess, guess_the_number)
        guesses = counting_guesses(guesses)
    return guesses
        

def counting_guesses(dog):
    dog -= 1
    return dog


def winner_check(number_to_guess, guess_the_number):
    if number_to_guess == guess_the_number:
        print("You win!")
            

def lose_check(guesses):
    if guesses == 0:
        print("You loose!")
    


if __name__ == "__main__":
    main()