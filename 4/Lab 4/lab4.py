import doctest


def compute_harmonic_series(n: int) -> float:
    """Return the sum of the first n terms of the harmonic series.

    Eg:
    >>> compute_harmonic_series(0)
    0
    >>> compute_harmonic_series(1)
    1.0
    >>> compute_harmonic_series(2)
    1.5
    >>> compute_harmonic_series(3)
    1.8333333333333333
    >>> compute_harmonic_series(4)
    2.083333333333333

    :param n: how many terms of the harmonic series to sum
    """
    sum_total = 0

    if n == 0:
        return n

    for i in range(1, n + 1):
        sum_total += 1 / i

    return sum_total


def get_fibonacci_sequence(n: int) -> str:
    """
    Return the first n terms of the Fibonacci sequence.

    Eg:
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(2)
    '0, 1'
    >>> get_fibonacci_sequence(3)
    '0, 1, 1'
    >>> get_fibonacci_sequence(4)
    '0, 1, 1, 2'
    >>> get_fibonacci_sequence(5)
    '0, 1, 1, 2, 3'
    >>> get_fibonacci_sequence(7)
    '0, 1, 1, 2, 3, 5, 8'

    :param n: how many steps of the fibonacci sequence to return
    :return: the first n terms of the fibonacci sequence
    """
    i, n1, n2, next_num = 0, 0, 1, 0
    output = ""

    while i < n:
        if i <= 1:
            next_num = i
        else:
            next_num = n1 + n2
            n1 = n2
            n2 = next_num

        output += str(next_num)

        if i != n - 1:
            output += ", "

        i += 1

    return output


def print_pattern(height: int, width: int, pattern1: str, pattern2: str):
    """
    Print a pattern of alternating characters.

    Example:
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    >>> print_pattern(1,1, '!@', '$$$')
    !@$$$
    >>> print_pattern(0,1, '!@', '$$$')
    <BLANKLINE>
    >>> print_pattern(1,0, '!@', '$$$')
    <BLANKLINE>
    >>> print_pattern(2,2, '#', '$')
    #$#$
    $#$#
    >>> print_pattern(4,2, '#', '&')
    #&#&
    &#&#
    #&#&
    &#&#

    :param height: how many layers the output pattern will have
    :param width:  how many times each pattern will be printed on each layer
    :param pattern1:  first pattern to print
    :param pattern2: second pattern to print
    """
    output = ""

    for i in range(0, height):
        for j in range(0, width*2):
            if (i + j) % 2 == 0:
                output += pattern1
            else:
                output += pattern2

        if i != height - 1:
            output += '\n'

    print(output)

