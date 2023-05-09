from pure_wordgrid import check_if_invalid
from pure_wordgrid import build_word_grid


def main():
    checked_word = True
    while checked_word:
        user_input = input('Type your word: ')
        checked_word = check_if_invalid(user_input)
        if checked_word:
            print(checked_word)
    correct_word = build_word_grid(user_input)
    
    for word in correct_word:
        print(word)


if __name__ == '__main__':
    main()

