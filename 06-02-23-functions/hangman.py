# Hangman. 
# The computer picks a word from a selection it knows, shows you the blanks, and asks you to guess. 
# Every successful guess fills in those blanks. 
# Every failed guess draws a new piece of the hangman. 
# You have six chances to win.


# 1- hide the word, before opening
# 2- compare the word index
# 3- if no match: chances -1 and draw
# 4- if match: input is index of list and joinlist

# input = letter
# print the word in underscores
# 6 chances to gues for hangman
# get a word from words
# good guess = show letter in word
# wrong guess = show pieces of hangman



# NOT FINISHED!

def main():
    remaining_chances = 6
    word = "PYTHON"
    hidden_word = word.replace("PYTHON", "######")


def playing(remaining_chances, hidden_word):
    while True and remaining_chances > 0:
        print(hidden_word)
        given_letter = input("Enter your letter: ").upper()
        return given_letter


def letter_check(given_letter, word):
    for letter in given_letter:
          letter_index = word.find(letter)
          return letter_index


def in_word_check(given_letter, word, letter_index):
    if given_letter in word:
        list_hidden_word = list(hidden_word)
        list_hidden_word[letter_index] = given_letter
        hidden_word = "".join(list_hidden_word)
    return given_letter


def not_in_word_check(given_letter, word, remaining_chances):
    if given_letter not in word:
        remaining_chances -= 1
        print(f"You missed!, chances remaining: {remaining_chances}")
    return remaining_chances, given_letter, word



if __name__ == "__main__":
    main()




        # if hidden_word == word:
        #     print("You win!")
        #     print(f"chances remainig: {remaining_chances}")