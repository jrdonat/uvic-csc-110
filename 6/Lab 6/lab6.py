import doctest


def sum_even_values(num_list: list) -> int:
    """
    Return the sum of all even values in num_list.

    Example:
    >>> sum_even_values([])
    0
    >>> sum_even_values([0])
    0
    >>> sum_even_values([1])
    0
    >>> sum_even_values([1, 3, 5])
    0
    >>> sum_even_values([2])
    2
    >>> sum_even_values([2, 4, 6])
    12
    >>> sum_even_values([1, 2, 3, 4, 5, 6])
    12

    :param num_list: list of integers
    :return: sum of all even values in num_list
    """
    even_sum_total = 0

    for number in num_list:
        if is_even(number):
            even_sum_total += number

    return even_sum_total


def count_above(num_list: list, threshold: int) -> int:
    """
    Return the number of values in num_list that are greater than the threshold.

    Example:
    >>> count_above([], 0)
    0
    >>> count_above([1], 0)
    1
    >>> count_above([1, 2, 3], 0)
    3
    >>> count_above([1, 2, 3], 1)
    2
    >>> count_above([1, 2, 3], 2)
    1
    >>> count_above([1, 2, 3], 3)
    0
    >>> count_above([1, 2, 3], 4)
    0

    :param num_list: list of integers
    :param threshold: the threshold to compare against
    :return: return the number of even values in num_list that are greater than the threshold
    """
    above_threshold_count = 0

    for number in num_list:
        if number > threshold:
            above_threshold_count += 1

    return above_threshold_count


def add1(num_list: list) -> list:
    """
    Return a new list with each value in num_list incremented by 1.

    Example:
    >>> add1([])
    []
    >>> add1([0])
    [1]
    >>> add1([1])
    [2]
    >>> add1([1, 2, 3])
    [2, 3, 4]
    >>> add1([1, 2, 3, 4, 5])
    [2, 3, 4, 5, 6]
    >>> add1([-1, -2, -3, -4, -5])
    [0, -1, -2, -3, -4]

    :param num_list: list of integers
    :return: return a new list with each value in num_list incremented by 1
    """
    output_list = []

    for number in num_list:
        output_list.append(number + 1)

    return output_list


def are_all_even(num_list: list) -> bool:
    """
    Return True if all values in num_list are even, False otherwise.

    Example:
    >>> are_all_even([])
    True
    >>> are_all_even([0])
    True
    >>> are_all_even([1])
    False
    >>> are_all_even([2])
    True
    >>> are_all_even([2, 4, 6])
    True
    >>> are_all_even([1, 2, 3, 4, 5, 6])
    False
    >>> are_all_even([-2, -4, -6])
    True
    >>> are_all_even([-2, -4, -6, -7])
    False

    :param num_list: list of integers
    :return: return True if all values in num_list are even, False otherwise
    """
    for number in num_list:
        if not is_even(number):
            return False

    return True


#######################################################################
#                           HELPER FUNCTION                           #
#######################################################################


def is_even(number: int) -> bool:
    """
    Return True if number is even, False otherwise.

    Example:
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    >>> is_even(0)
    True

    """
    return number % 2 == 0
