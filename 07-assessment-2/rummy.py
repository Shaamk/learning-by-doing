from pure_rummy import has_rummy

def main():

    user_input = input("Please enter your rummy hand: ")
    output = has_rummy(user_input)
    print(output)

if __name__ == '__main__':
    main()