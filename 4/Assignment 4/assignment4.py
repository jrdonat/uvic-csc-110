#######################################################################################
#                                   PART 1
#######################################################################################

def get_factors(n: int) -> str:
    """
    Return a string of the factors of n

    Eg:
    >>> get_factors(10)
    '1,2,5,10'
    >>> get_factors(11)
    '1,11'
    >>> get_factors(12)
    '1,2,3,4,6,12'
    >>> get_factors(1)
    '1'
    >>> get_factors(0)
    ''

    :param n: the number to get the factors of
    :return: string of the factors of n
    """
    output = ''

    for i in range(1, n + 1):
        if is_multiple_of(n, i):
            output += str(i)

            if i != n:
                output += ','

    return output


def get_range_of_factors(start: int, end: int) -> str:
    """
    Return a string of the factors of all numbers in the range [start, end)

    Eg:
    >>> print(get_range_of_factors(10,13))
    1,2,5,10
    1,11
    1,2,3,4,6,12
    >>> print(get_range_of_factors(1,4))
    1
    1,2
    1,3
    >>> print(get_range_of_factors(6,13))
    1,2,3,6
    1,7
    1,2,4,8
    1,3,9
    1,2,5,10
    1,11
    1,2,3,4,6,12


    :param start: inclusive start of the range
    :param end: exclusive end of the range
    :return: a string of the factors of all numbers in the range [start, end)
    """
    output = ''

    for i in range(start, end):
        output += get_factors(i) + '\n'

    return output


def sum_fibonacci_sequence(n: int) -> int:
    """
    Return the sum of the first n terms of the Fibonacci sequence.

    Eg:
    >>> sum_fibonacci_sequence(7)
    20
    >>> print(sum_fibonacci_sequence(0))
    0
    >>> print(sum_fibonacci_sequence(1))
    0
    >>> print(sum_fibonacci_sequence(2))
    1
    >>> print(sum_fibonacci_sequence(4))
    4
    >>> print(sum_fibonacci_sequence(20))
    10945

    :param n: how many terms of the fibonacci sequence to sum
    :return: the sum of the first n terms of the fibonacci sequence
    """
    i, n1, n2, next_num = 0, 0, 1, 0
    sum_total = 0

    while i < n:
        if i <= 1:
            next_num = i
        else:
            next_num = n1 + n2
            n1 = n2
            n2 = next_num

        sum_total += next_num

        i += 1

    return sum_total


#######################################################################################
#                                   PART 2
#######################################################################################


def print_tail(size: int):
    """
    prints tail portion of given size for rocket ship

    :param size: the size of the tail to print
    """
    # coneCount = 0
    #
    # if size <= 2:
    #     coneCount = 1
    # else:
    #     coneCount = size

    print('// ' + (' /\\ ' * size) + ' \\\\')


def print_booster(size: int):
    """
    prints booster portion of given size for rocket ship

    :param size: the size of the booster to print
    """

    print_card_tower(size, '.', '|', True)
    print_card_tower(size, '.', '|', False)
    print_separator(size)


def print_instrument_unit(size: int):
    """
    prints instrument unit portion of given size for rocket ship

    :param size: the size of the instrument unit to print
    """

    for i in range(0, 2):
        print('||' + '~#' + ('~#~#' * size) + '||')

    print_separator(size)


def print_lem_adapter(size: int):
    """
    prints lem adapter portion of given size for rocket ship

    :param size: the size of the lem adapter to print
    """

    bottom_count = size * 2 + 1
    top_count = bottom_count - 1

    print(' //' + (' %' * top_count) + '\\\\')
    print('//' + (' %' * bottom_count) + '\\\\')
    print_separator(size)


def print_space_craft(size: int):
    """
    prints spacecraft portion of given size for rocket ship

    :param size: the size of the spacecraft to print
    """

    if size == 0:
        print('  ++')
    else:

        for i in range(0, size*2):
            print((' ' * ((size*2+2)-i)) + ('/' * i) + '**' + ('\\' * i))

        print(' ' * 2, end='')
        print_separator(size-1)


def print_rocket_ship(size: int, boosters: int):
    """
    prints a rocket ship of given size and boosters


    :param size: size of the rocket ship
    :param boosters: amount of boosters on the rocket ship
    """
    print_space_craft(size)
    print_lem_adapter(size)
    print_instrument_unit(size)

    for i in range(0, boosters):
        print_booster(size)

    print_tail(size)


#######################################################################################
#                                HELPER FUNCTIONS
#######################################################################################


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


def print_separator(size: int):
    """
    prints a separator for the rocket ship

    :param size: the size of the separator to print
    """
    print('+' + '=*=*' * (size + 1) + '+')


def print_card_tower(size: int, negative: str, sides: str, up_facing: bool):
    """
    prints a card tower of given size

    :param sides: the sides of the card tower
    :param size: the size of the card tower
    :param negative: what to fill negative space with
    :param up_facing: whether the card tower is up facing or down facing
    """

    if size == 0 and up_facing:
        print('|/\\/\\|')
    elif up_facing:
        for i in range(0, size + 1):

            print(sides, end='')

            for j in range(0, 2):
                print('' + (negative * (size - i)) + ('/\\' * (i + 1)) + (negative * (size - i)), end='')

            print(sides)

    if size == 0 and (not up_facing):
        print('|\\/\\/|')
    elif not up_facing:
        for i in range(size, -1, -1):

            print(sides, end='')

            for j in range(0, 2):
                print('' + (negative * (size - i)) + ('\\/' * (i + 1)) + (negative * (size - i)), end='')

            print(sides)

