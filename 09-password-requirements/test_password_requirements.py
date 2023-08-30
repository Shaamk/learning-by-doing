from mustContainCapitalRequirement import MustContainCapitalRequirement
from mustContainNumberRequirement import MustContainNumberRequirement
from mustMeetMinimumLenghtRequirement import MustMeetMinimumLenghtRequirement
from passwordChecker import PassWordChecker

def test_check_exists_capital():
    assert MustContainCapitalRequirement()

def test_check_method_true_capital():
    requirement = MustContainCapitalRequirement()
    result = requirement.check('123Smurfs')
    assert result == True

def test_check_method_false_capital():
    requirement = MustContainCapitalRequirement()
    result = requirement.check('123smurfs')
    assert result == False

def test_message_method_capital():
    requirement = MustContainCapitalRequirement()
    result = requirement.message()
    assert result == 'The password must contain at least one capital'

def test_check_exists_number():
    assert MustContainNumberRequirement()

def test_check_method_true_number():
    requirement = MustContainNumberRequirement()
    result = requirement.check('123Smurfs')
    assert result == True

def test_check_method_false_number():
    requirement = MustContainNumberRequirement()
    result = requirement.check('Smurfs')
    assert result == False

def test_check_message_method_number():
    requirement = MustContainNumberRequirement()
    result = requirement.message()
    assert result == 'The password must contain at least one number'

def test_check_exists_lenght():
    assert MustMeetMinimumLenghtRequirement()

def test_check_method_true_lenght():
    requirement = MustMeetMinimumLenghtRequirement()
    result = requirement.check('123Smurfs')
    assert result == True

def test_check_method_false_lenght():
    requirement = MustMeetMinimumLenghtRequirement()
    result = requirement.check('Smurfs')
    assert result == False

def test_check_message_method_lenght():
    requirement = MustMeetMinimumLenghtRequirement()
    result = requirement.message()
    assert result == 'The password must contain at least 8 characters'

def test_passwordchecker():
    assert PassWordChecker('')

def test_passwordchecker_method_check():
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirement = [lenght, number, capital]
    result = PassWordChecker(requirement)
    assert result.check('ABCabc123')

def test_passwordchecker_method_check_two():
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirement = [lenght, number, capital]
    result = PassWordChecker(requirement)
    assert result.check('12345678') == False

def test_passwordchecker_method_message():
    checker = PassWordChecker([])
    checker.check('1Smurfs')
    messages = checker.messages()
    assert messages == []

def test_passwordchecker_method_message_with_one_message_one():
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirements = [lenght, number, capital]
    checker = PassWordChecker(requirements)
    checker.check('1Smurf')
    messages = checker.messages()
    assert messages == ['The password must contain at least 8 characters']

def test_passwordchecker_method_message_with_one_message_two():
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirements = [lenght, number, capital]
    checker = PassWordChecker(requirements)
    checker.check('1abcdefgh')
    messages = checker.messages()
    assert messages == ['The password must contain at least one capital']


def test_passwordchecker_method_with_trhee_messages():
    lenght = MustMeetMinimumLenghtRequirement()
    number = MustContainNumberRequirement()
    capital = MustContainCapitalRequirement()
    requirements = [lenght, number, capital]
    checker = PassWordChecker(requirements)
    checker.check('smurf')
    messages = checker.messages()
    assert messages == ['The password must contain at least 8 characters',
                        'The password must contain at least one number',
                        'The password must contain at least one capital']

