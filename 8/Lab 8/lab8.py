import math
import doctest
from typing import Type

Person = (str, int)  # (name, age)
NAME=0

def file_to_person_list(filename: str) -> list[Person]:
    """
    Read a file and return a list of tuples

    Example:
    >>> file_to_person_list('lab8-name-age.txt')
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]



    :param filename: The name of the file to read
    :return: Return a list of tuples containing the name and age of each person
    """
    file = open(filename, 'r')
    lines = file.readlines()
    person_list = []

    for line in lines:
        line = line.strip()
        line = line.split(' ')
        personnel = (line[0], int(line[1]))
        person_list.append(personnel)

    return person_list


def get_average_age(person_list: list[Person]) -> int:
    """
    Return the average age of the people in the list

    Example:
    >>> get_average_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)])
    31

    :param person_list:
    :return:
    """
    total_age = 0

    for person in person_list:
        total_age += person[1]

    return math.floor(total_age / len(person_list))


def get_above_age(person_list: list[Person], age: int) -> list[Person]:
    """
    Return a list of people above the given age

    Example:
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 30)
    [('Jose', 53), ('Rajan', 65)]

    :param person_list: list of people
    :param age: threshold age
    :return: a list of people above the given age
    """
    above_age = []

    for person in person_list:
        if person[1] > age:
            above_age.append(person)

    return above_age


def to_file(person_list: list[Person], filename: str) -> None:
    """
    Write the given list of people to the given file

    Example:
    >>> to_file([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 'lab8-above-avg.txt')

    :param person_list: list of people
    :param filename: name of the file to write
    :return:  the list of people to the given file
    """
    file = open(filename + '.csv', 'w')

    for person in person_list:
        file.write(person[0] + ',' + str(person[1]) + '\n')

    file.close()


def write_names_above_avg_age(input_file_name: str, output_file_name: str) -> None:
    """
    Write the names of the people above the average age to the given file

    Example:
    >>> write_names_above_avg_age('lab8-name-age.txt', 'lab8-above-avg.txt')

    :param input_file_name: filename of the input file
    :param output_file_name: filename of the output file
    :return: write the names of the people above the average age to the given file
    """
    person_list = file_to_person_list(input_file_name)

    if not person_list:
        return to_file([], output_file_name)

    average_age = get_average_age(person_list)
    above_age = get_above_age(person_list, average_age)
    to_file(above_age, output_file_name)
