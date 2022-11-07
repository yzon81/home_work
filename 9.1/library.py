# Задача
# функцію  is_string_capitalized
# потрібно дописати (в тому числі докстрінги) - очікування - прохід тестів
# напишіть функцію, яка перевірить, чи дане число є парним чи непарним (коментар з коду видаліть)
# ТА ПОКРИЙТЕ ЇЇ ТЕСТАМИ


def is_string_capitalized(string):
    """
    This function checks if the first letter of a string is capitalized.
    :param string: string
    :return: True|False
    """
    if string == '':
        return True
    elif string.isalnum():
        return True
    elif string[0].isupper() and string[1:].islower() == True:
        return True
    elif string[0].isupper() and string[1:].islower() == False:
        return False
    else:
        return False


def is_odd_or_even(number):
    """
    This function checks if the given number is odd or even.
    :param number: int
    :return: str
    """
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
