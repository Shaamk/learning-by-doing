from pure_palindrome import check_for_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome

def main():
    user_input = input('Please enter a word: ')
    is_invalid = check_for_invalid(user_input)
    if is_invalid is not None:
        print(is_invalid)
    
    cleaned_string = clean_user_input(user_input)
    print(cleaned_string)

    palindrome = check_for_palindrome(cleaned_string)
    print(palindrome)


if __name__ == '__main__':
    main()