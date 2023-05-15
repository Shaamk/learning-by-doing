def check_for_invalid(user_input):
    if isinstance(user_input, str):
        for i in user_input:
            if i.isalnum():
                return None
    #     return 'Sorry, that is invalid input'
    return 'Sorry, that is invalid input'

def clean_user_input(user_input):
    user_input_list = [i for i in user_input if i.isalnum()]
    user_input_str = "".join(user_input_list)
    return user_input_str.lower()

def check_for_palindrome(user_input):
    if user_input != user_input [::-1]:
        return 'Not a palindrome'
    return 'Palindrome'

# pass string, can not be empty
# checking if there are numbers or letters
# go through the string:
#       -check if there is number: not ret
#       -check if 