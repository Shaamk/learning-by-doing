from pure_palindrome import check_for_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome

def main():
    user_input = input("Please enter a word: ")
    invalid = check_for_invalid(user_input)
    if invalid is not None:
        print(invalid)
    else:        
    
        cleaned_string = clean_user_input(user_input)
        
        palindrome = check_for_palindrome(cleaned_string)
        print(palindrome)


if __name__ == '__main__':
    main()