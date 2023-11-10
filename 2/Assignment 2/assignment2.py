import math
import doctest


def check_funds(current_balance: float, purchase_price: float):
    """
    Function to print account fund status

    Example:
    >>> check_funds(20,9.99)
    you will have $ 10.01 left after this purchase
    >>> check_funds(20,20)
    you will have $ 0.00 left after this purchase
    >>> check_funds(20,24.99)
    you are short $ 4.99

    :param current_balance: amount of money in bank
    :param purchase_price: total price of item attempting to purchase
    :return:
    """
    if current_balance < 0:
        print('you have a negative balance')
        return

    difference = current_balance - purchase_price

    if current_balance >= purchase_price:
        print(f'you will have $ {difference:.2f} left after this purchase')
    else:
        print(f'you are short $ {(difference * -1):.2f}')


def print_biggest(input_float_a: float, input_float_b: float, input_float_c: float):
    """
    Function to print biggest of 3 numbers

    Example:
    >>> print_biggest(4.0,2.0,2.0)
    4.0
    >>> print_biggest(1.0,2.0,3.0)
    3.0
    >>> print_biggest(4.0,6.0,3.0)
    6.0
    >>> print_biggest(3.0,3.0,3.0)
    3.0


    :param input_float_a: first number to compare
    :param input_float_b: second number to compare
    :param input_float_c:  third number to compare
    """
    floats = (input_float_a, input_float_b, input_float_c)
    biggest = input_float_a

    for i in floats:
        if i > biggest:
            biggest = i

    print(biggest)


def convert_inches(inches: int):
    """
    Function to convert inches to larger units and print values

    Example:
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    >>> convert_inches(163409)
    2 mi, 1019 yd, 0 ft, 5 in
    >>> convert_inches(3409)
    0 mi, 94 yd, 2 ft, 1 in
    >>> convert_inches(29)
    0 mi, 0 yd, 2 ft, 5 in
    >>> convert_inches(9)
    0 mi, 0 yd, 0 ft, 9 in

    :param inches: input of inches to be split into other units

    """
    units = [
        [63360, 0],
        [36, 0],
        [12, 0],
        [1, 0],
    ]

    remainder = inches

    for value in units:
        value[1] = math.floor(remainder / value[0])
        remainder = remainder % value[0]

    print(f'{units[0][1]} mi, {units[1][1]} yd, {units[2][1]} ft, {units[3][1]} in')


def is_multiple_of(n1: int, n2: int):
    """
    Function to print whether a number is a multiple of the other

    Example:
    >>> is_multiple_of(0,0)
    0 is a multiple of 0
    >>> is_multiple_of(9,0)
    9 is not a multiple of 0
    >>> is_multiple_of(0,9)
    0 is a multiple of 9
    >>> is_multiple_of(4,2)
    4 is a multiple of 2
    >>> is_multiple_of(5,7)
    5 is not a multiple of 7

    :param n1: number to have multiples checked against
    :param n2: check if this number is a multiple of n1
    """

    if n1 == n2 or (n2 != 0 and (n1 % n2 == 0)):
        print(f'{n1} is a multiple of {n2}')
    else:
        print(f'{n1} is not a multiple of {n2}')


def maximum(float_a: float, float_b: float):
    """
    Made my own max func because prairie learn banned it

    :param float_a:
    :param float_b:
    :return:
    """
    return float_b if float_b > float_a else float_a


def display_charges(item_price: float, tax_rate: int, is_member: bool, discount_code: str, country: str):
    """
    Function to print whether a number is a multiple of the other

    Examples:
    >>> display_charges(0, 0, False, 'invalid', 'Afghanistan')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(6.69, 14, False, 'FIRST_PURCHASE', 'Belgium')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.67
    total charge: $ 0.67
    >>> display_charges(2.32, 11, False, 'NO_DISCOUNT', 'Czech Republic')
    price: $ 2.32
    tax: $ 0.26
    shipping: $ 0.23
    total charge: $ 2.81
    >>> display_charges(2.32, 11, True, 'NO_DISCOUNT', 'Czech Republic')
    price: $ 2.32
    tax: $ 0.26
    shipping: $ 0.00
    total charge: $ 2.58
    >>> display_charges(2.32, 11, False, 'NO_DISCOUNT', 'Canada')
    price: $ 2.32
    tax: $ 0.26
    shipping: $ 0.00
    total charge: $ 2.58
    >>> display_charges(2.32, 11, True, 'NO_DISCOUNT', 'Canada')
    price: $ 2.32
    tax: $ 0.26
    shipping: $ 0.00
    total charge: $ 2.58
    >>> display_charges(2.32, 11, False, 'FIRST_PURCHASE', 'Czech Republic')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.23
    total charge: $ 0.23
    >>> display_charges(19.27, 9, False, 'NO_DISCOUNT', 'Chile')
    price: $ 19.27
    tax: $ 1.73
    shipping: $ 1.93
    total charge: $ 22.93
    >>> display_charges(19.27, 9, True, 'NO_DISCOUNT', 'Chile')
    price: $ 19.27
    tax: $ 1.73
    shipping: $ 0.00
    total charge: $ 21.00
    >>> display_charges(19.27, 9, False, 'NO_DISCOUNT', 'Canada')
    price: $ 19.27
    tax: $ 1.73
    shipping: $ 0.00
    total charge: $ 21.00
    >>> display_charges(19.27, 9, True, 'NO_DISCOUNT', 'Canada')
    price: $ 19.27
    tax: $ 1.73
    shipping: $ 0.00
    total charge: $ 21.00
    >>> display_charges(19.27, 9, False, 'FIRST_PURCHASE', 'Chile')
    price: $ 9.27
    tax: $ 0.83
    shipping: $ 1.93
    total charge: $ 12.03
    >>> display_charges(19.27, 9, True, 'FIRST_PURCHASE', 'Chile')
    price: $ 9.27
    tax: $ 0.83
    shipping: $ 0.00
    total charge: $ 10.10
    >>> display_charges(19.27, 9, False, 'FIRST_PURCHASE', 'Canada')
    price: $ 9.27
    tax: $ 0.83
    shipping: $ 0.00
    total charge: $ 10.10
    >>> display_charges(19.27, 9, True, 'FIRST_PURCHASE', 'Canada')
    price: $ 9.27
    tax: $ 0.83
    shipping: $ 0.00
    total charge: $ 10.10
    >>> display_charges(19.27, 9, False, 'FREQUENT_BUYER', 'Chile')
    price: $ 19.27
    tax: $ 1.73
    shipping: $ 1.93
    total charge: $ 22.93
    >>> display_charges(0, 3, False, 'NO_DISCOUNT', 'Syria')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(0, 3, True, 'NO_DISCOUNT', 'Syria')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(0, 3, False, 'NO_DISCOUNT', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(0, 3, True, 'NO_DISCOUNT', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(0, 3, False, 'FIRST_PURCHASE', 'Syria')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(2, 9, False, 'NO_DISCOUNT', 'Azerbaijan')
    price: $ 2.00
    tax: $ 0.18
    shipping: $ 0.20
    total charge: $ 2.38
    >>> display_charges(2, 9, True, 'NO_DISCOUNT', 'Azerbaijan')
    price: $ 2.00
    tax: $ 0.18
    shipping: $ 0.00
    total charge: $ 2.18
    >>> display_charges(2, 9, False, 'NO_DISCOUNT', 'Canada')
    price: $ 2.00
    tax: $ 0.18
    shipping: $ 0.00
    total charge: $ 2.18
    >>> display_charges(2, 9, True, 'NO_DISCOUNT', 'Canada')
    price: $ 2.00
    tax: $ 0.18
    shipping: $ 0.00
    total charge: $ 2.18
    >>> display_charges(2, 9, False, 'FIRST_PURCHASE', 'Azerbaijan')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.20
    total charge: $ 0.20
    >>> display_charges(10, 10, False, 'NO_DISCOUNT', 'Nigeria')
    price: $ 10.00
    tax: $ 1.00
    shipping: $ 1.00
    total charge: $ 12.00
    >>> display_charges(10, 10, True, 'NO_DISCOUNT', 'Nigeria')
    price: $ 10.00
    tax: $ 1.00
    shipping: $ 0.00
    total charge: $ 11.00
    >>> display_charges(10, 10, False, 'NO_DISCOUNT', 'Canada')
    price: $ 10.00
    tax: $ 1.00
    shipping: $ 0.00
    total charge: $ 11.00
    >>> display_charges(10, 10, True, 'NO_DISCOUNT', 'Canada')
    price: $ 10.00
    tax: $ 1.00
    shipping: $ 0.00
    total charge: $ 11.00
    >>> display_charges(10, 10, True, 'FIRST_PURCHASE', 'Nigeria')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(10, 10, False, 'FIRST_PURCHASE', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(10, 10, True, 'FIRST_PURCHASE', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(10, 10, False, 'FREQUENT_BUYER', 'Nigeria')
    price: $ 10.00
    tax: $ 1.00
    shipping: $ 1.00
    total charge: $ 12.00
    """
    shipping_rate = 0.1
    shipping_cost = item_price * shipping_rate
    discount_amount = 0.0

    if is_member or country.lower() == "canada":
        shipping_cost = 0.0

    if discount_code == 'FREQUENT_BUYER' and is_member:
        discount_amount = 2.0
    elif discount_code == 'FIRST_PURCHASE':
        discount_amount = 10.0

    subtotal = maximum(0.0, item_price - discount_amount)
    tax_cost = subtotal * (tax_rate / 100)

    print(f'price: $ {subtotal:.2f}\n'
          f'tax: $ {tax_cost:.2f}\n'
          f'shipping: $ {shipping_cost:.2f}\n'
          f'total charge: $ {subtotal + tax_cost + shipping_cost :.2f}')
