import doctest
import math


def get_powers(num_list: list[int], exponent: int) -> list:
    """
    This function takes a list of numbers and an exponent and returns a list of the numbers raised to the exponent.

    Examples:
    >>> get_powers([], 2)
    []
    >>> get_powers([1, 2, 3], 0)
    [1, 1, 1]
    >>> get_powers([1, 2, 3], 1)
    [1, 2, 3]
    >>> get_powers([1, 2, 3], 2)
    [1, 4, 9]
    >>> get_powers([1, 2, 3], 3)
    [1, 8, 27]

    :param num_list: list of numbers
    :param exponent: the exponent to raise the numbers to
    :return: list of numbers raised to the exponent
    """
    output_list = []

    for number in num_list:
        output_list.append(number ** exponent)

    return output_list


def concatenate(in_list: list[str]) -> str:
    """
    This function takes a list of strings and returns a string of the
    strings concatenated together with a space between each string.

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['abc', 'de'])
    'abc de'
    >>> concatenate(['abc', 'de', 'f'])
    'abc de f'
    >>> concatenate(['abc', 'de', 'f', 'ghi'])
    'abc de f ghi'
    >>> concatenate(['abc', '', 'f', '', 'j'])
    'abc  f  j'

    :param in_list:
    :return:
    """
    output_string = ""
    first_loop = True

    for item in in_list:
        if first_loop:
            output_string += item
            first_loop = False
        else:
            output_string += " " + item

    return output_string


def contains_multiple(in_list: list[int], multiple_value: int) -> bool:
    """
    Returns True if the list contains a multiple of the number, False otherwise.

    Examples:
    >>> contains_multiple([], 2)
    True
    >>> contains_multiple([1, 2, 3], 2)
    True
    >>> contains_multiple([1, 2, 3], 3)
    True
    >>> contains_multiple([1, 2, 3], 4)
    False
    >>> contains_multiple([2, 4, 6], 2)
    True
    >>> contains_multiple([10, 6, 20], 3)
    True




    :param in_list: list of numbers to check for multiples
    :param multiple_value: number to check if there is a multiple of
    :return:
    """
    if not in_list:
        return False

    for number in in_list:
        if is_multiple_of(number, multiple_value):
            return True

    return False


def get_long_enough(list_of_strings: list[str], min_length: int) -> list[str]:
    """
    Returns a list of strings that are at least as long as the min_length.

    Examples:
    >>> get_long_enough([], 2)
    []
    >>> get_long_enough(['a', 'ab', 'abc'], 0)
    ['a', 'ab', 'abc']
    >>> get_long_enough(['a', 'ab', 'abc'], 1)
    ['a', 'ab', 'abc']
    >>> get_long_enough(['a', 'ab', 'abc'], 2)
    ['ab', 'abc']
    >>> get_long_enough(['a', 'ab', 'abc'], 3)
    ['abc']
    >>> get_long_enough(['a', 'ab', 'abc'], 4)
    []

    :param list_of_strings: list of strings to check
    :param min_length: minimum length of string to return
    :return: list of strings that are at least as long as the min_length
    """
    output_list = []

    for string in list_of_strings:
        if len(string) >= min_length:
            output_list.append(string)

    return output_list


def all_multiples(list_of_ints: list[int], multiple_value: int) -> bool:
    """
    Returns True if all the numbers in the list are multiples of the number, False otherwise.

    Examples:
    >>> all_multiples([], 2)
    False
    >>> all_multiples([0],69)
    True
    >>> all_multiples([1, 2, 3], 2)
    False
    >>> all_multiples([1, 2, 3], 3)
    False
    >>> all_multiples([1, 2, 3], 4)
    False
    >>> all_multiples([2, 4, 6], 2)
    True
    >>> all_multiples([3, 6, 9], 3)
    True
    >>> all_multiples([4, 8, 12,0], 4)
    True


    :param list_of_ints:
    :param multiple_value:
    :return:
    """

    for number in list_of_ints:
        if not is_multiple_of(number, multiple_value):
            return False

    return True


def getting_shorter(list_of_strings: list[str]) -> bool:
    """
    Returns True if each string in the list is shorter than the previous string, False otherwise.

    Examples:
    >>> getting_shorter([])
    True
    >>> getting_shorter(['a', 'ab', 'abc'])
    False
    >>> getting_shorter(['abc', 'ab', 'a'])
    True
    >>> getting_shorter(['abc', 'ab', 'a', ''])
    True



    :param list_of_strings:
    :return:
    """
    previous_length = math.inf

    for string in list_of_strings:
        if (prev := len(string)) >= previous_length:
            return False
        previous_length = prev

    return True


def is_multiple_of(n1: int, n2: int) -> bool:
    """
    Function to print whether a number is a multiple of the other

    Example:
    >>> is_multiple_of(0,0)
    True
    >>> is_multiple_of(9,0)
    False
    >>> is_multiple_of(0,9)
    True
    >>> is_multiple_of(4,2)
    True
    >>> is_multiple_of(5,7)
    False

    :param n1: number to have multiples checked against
    :param n2: check if this number is a multiple of n1
    :return: True if n2 is a multiple of n1, False otherwise
    """

    return n1 == n2 or (n2 != 0 and (n1 % n2 == 0))










