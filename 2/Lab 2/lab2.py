import math

MONTH_ZODIACS = {  # dictionary with each month and its respective two zodiacs an the day it changes
    "january": ("Capricorn", 20, "Aquarius"),
    "february": ("Aquarius", 19, "Pisces"),
    "march": ("Pisces", 21, "Aries"),
    "april": ("Aries", 20, "Taurus"),
    "may": ("Taurus", 21, "Gemini"),
    "june": ("Gemini", 21, "Cancer"),
    "july": ("Cancer", 23, "Leo"),
    "august": ("Leo", 23, "Virgo"),
    "september": ("Virgo", 23, "Libra"),
    "october": ("Libra", 23, "Scorpio"),
    "november": ("Scorpio", 22, "Sagittarius"),
    "december": ("Sagittarius", 22, "Capricorn")}


def print_longer(string_a: str, string_b: str):
    """
    Function to print the longer of given str arguments

    Example:
    >>> print_longer('hello','hi')
    hello
    >>> print_longer('foo','bar')
    foo

    :param string_a: first string to compare
    :param string_b:  second string to compare
    :return: the longer string, if length is equal first is printed
    """
    longer = string_b if len(string_b) > len(string_a) else string_a
    print(longer)


def print_real_roots(a: int, b: int, c: int):
    """
    Calculates and prints real roots using quadratic formula

    for a(x^2) + b(x) + c

    Normal Quadratic Formula (-b + or - sqrt(b^2 - 4ac)) / 2a
    Rearranged to split two terms between + or -
    Rearranged formula (-b/2a) + or - sqrt((b^2 - 4ac)/(4a^2))

    Let the first term = -b/2a
    Let the second term = sqrt((discriminant)/(4a^2))
    Let the discriminant = b^2 - 4ac

    Example:
    >>> print_real_roots(9, 6, 2)
    NO REAL ROOTS
    >>> print_real_roots(0, 6, 3)
    ERROR
    >>> print_real_roots(2, 4, 2)
    -1.000,-1.000
    >>> print_real_roots(2, 4, -1)
    -2.225,0.225
    >>> print_real_roots(7, 16, -1)
    -2.347,0.061


    :param a: coefficient of x^2 in a quadratic
    :param b: coefficient of x in a quadratic
    :param c: constant in a quadratic
    """
    if a == 0:  # make sure a isn't zero to avoid divide by zero error
        print("ERROR")
        return

    if (discriminant := (b ** 2 - 4 * a * c)) < 0:  # check discriminant positivity and assign variable discriminant
        print("NO REAL ROOTS")
        return

    first_term = (-1 * b) / (2 * a)
    second_term = math.sqrt(discriminant / (4 * a ** 2))

    print(f"{(first_term - second_term):.3f},{(first_term + second_term):.3f}")


def print_zodiac_sign(month: str, day: int):
    """
    Function to print name of zodiac sign for given month and day

    Example:
    >>> print_zodiac_sign('January', 22)
    Aquarius
    >>> print_zodiac_sign('February', 25)
    Pisces
    >>> print_zodiac_sign('July', 23)
    Leo
    >>> print_zodiac_sign('September', 1)
    Virgo


    :param month: month to check zodiac sign
    :param day: day to check zodiac sign
    :return: returns name of calculated zodiac sign
    """
    month_zodiac_info = MONTH_ZODIACS[month.lower()]
    zodiac = month_zodiac_info[0] if day < int(month_zodiac_info[1]) else month_zodiac_info[2]
    print(zodiac)


