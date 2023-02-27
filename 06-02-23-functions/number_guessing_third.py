# try functions not bigger than 8 lines


from random import randint


def main():
    guess_the_number = the_number_to_guess()
    guesses = playing_game(6, guess_the_number)     # calling playing game function, the returned value is assigned to guesses 
    lose_check(guesses)                             # passed guesses as a argument


def the_number_to_guess():
    guess_the_number = randint(1, 101)
    return guess_the_number
    

def playing_game(guesses, guess_the_number):
    number_to_guess = int(input("Guess the number between 1 and 100: "))    
    while guess_the_number != number_to_guess and guesses > 0:
        print(f"guesses remaining {guesses}")
        if number_to_guess > guess_the_number:
            number_to_guess = guess_is_high(number_to_guess)
        else:
            number_to_guess = guess_is_low(number_to_guess)

        winner_check(number_to_guess, guess_the_number)
        guesses = counting_guesses(guesses)
    return guesses


def guess_is_high(number_to_guess):
    print("The guessed number", number_to_guess, "is too high")
    number_to_guess = int(input("Guess the number between 1 and 100: "))
    return number_to_guess


def guess_is_low(number_to_guess):
    print("The guessed number", number_to_guess,"is too low")
    number_to_guess = int(input("Guess the number between 1 and 100: "))
    return number_to_guess


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