from typing import Type

FlightInformation = tuple[str, str, float]


def swap(input_list: list[any], swap_index_a: int, swap_index_b: int) -> None:
    """
    Swaps the values at the given indices in the given list.

    Example:
    >>> print(swap([1, 2, 3], 0, 2))
    [3, 2, 1]
    >>> print(swap([1, 2, 3], 1, 1))
    [1, 2, 3]
    >>> print(swap([1, 2, 3], 0, 1))
    [2, 1, 3]
    >>> print(swap([1, 2, 3], 1, 0))
    [2, 1, 3]
    :param input_list: the list whose values are to be swapped
    :param swap_index_a: index of the first value to be swapped
    :param swap_index_b: index of the second value to be swapped
    :return:
    """
    temp_obj = input_list[swap_index_a]
    input_list[swap_index_a] = input_list[swap_index_b]
    input_list[swap_index_b] = temp_obj


def index_of_smallest(input_list: list) -> int:
    """
    Returns the index of the smallest value in the given list.

    Example:
    >>> print(index_of_smallest([1, 2, 3]))
    0
    >>> print(index_of_smallest([3, 2, 1]))
    2
    >>> print(index_of_smallest([2, 1, 3]))
    1
    >>> print(index_of_smallest([1, 1, 1]))
    0
    >>> print(index_of_smallest(['a','b','c']))
    0
    >>> print(index_of_smallest(['a','b','c','A']))
    3


    :param input_list: the list to be searched
    :return: index of the smallest value in the list
    """
    if not input_list:
        return -1

    smallest_index = 0

    for i in range(len(input_list)):
        if input_list[i] < input_list[smallest_index]:
            smallest_index = i

    return smallest_index


def total_duration(flight_list: list[FlightInformation]) -> float:
    """
    Returns the total duration of all flights in the given list.

    Example:
    >>> print(total_duration([('New York', 'Hell', 1.5), ('Hell', 'Chicago', 2.5)]))
    4.0
    >>> print(total_duration([('Bulgaria', 'Germany', 2.0), ('Germany', 'France', 3.0), ('France', 'Spain', 4.0)]))
    9.0
    >>> print(total_duration([('a','b',0)]))
    0.0
    >>> print(total_duration([]))
    0.0

    :param flight_list: list of flight information
    :return: returns the total duration of all flights in the given list
    """
    total_flight_duration = 0.0

    for flight_information in flight_list:
        total_flight_duration += flight_information[2]

    return total_flight_duration


def get_destinations_from(flight_list: list[FlightInformation], departure_city: str) -> list[str]:
    """
    Returns a list of all the destinations from the given departure city.

    Example:
    >>> print(get_destinations_from([('New York', 'Hell', 1.5), ('Hell', 'Chicago', 2.5)], 'Hell'))
    ['Chicago']
    >>> print(get_destinations_from([('Bulgaria', 'Germany', 2.0), ('Germany', 'France', 3.0), ('France', 'Spain', 4.0)], 'Bulgaria'))
    ['Germany']
    >>> print(get_destinations_from([('a','b',0)], 'a'))
    ['b']
    >>> print(get_destinations_from([('a','b',0)], 'b'))
    []
    >>> print(get_destinations_from([], 'a'))
    []
    >>> print(get_destinations_from([('a','b',0),('a','c',0)], 'a'))
    ['b', 'c']

    :param flight_list: list of flight information
    :param departure_city: the departure city
    :return: a list of all the destinations from the given departure city
    """
    city_list = []

    for information in flight_list:
        if (information[0] == departure_city) and (information[1] not in city_list):
            city_list.append(information[1])

    return city_list

