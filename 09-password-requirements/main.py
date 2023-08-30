from mustMeetMinimumLenghtRequirement import MustMeetMinimumLenghtRequirement
from mustContainNumberRequirement import MustContainNumberRequirement
from mustContainCapitalRequirement import MustContainCapitalRequirement
from passwordChecker import PassWordChecker


def main():
    password = input('Enter a valid password: ')
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirements = [lenght, number, capital]
    checker = PassWordChecker(requirements)
    checker.check(password)
    messages = checker.messages()
    for message in messages:
        print(message)


if __name__ == '__main__':
    main()
