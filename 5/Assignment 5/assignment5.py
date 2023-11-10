import doctest
import math
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


############################################################################################
#                                                                                          #
#                                       PART 1                                             #
#                                                                                          #
############################################################################################


def get_sequence(a: int, b: int, max_val: int) -> str:
    """
    Returns a string of comma separated values of ints in the sequence
    a, a+b, a+2b, a+3b, ... up to but not including max_val.

    examples:
    >>> get_sequence(2, 5, 32)
    '2,7,12,17,22,27,32'
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    >>> get_sequence(2,5,1)
    ''

    :param a:
    :param b:
    :param max_val:
    :return:
    """
    i = 1
    next_value = a
    output = ''

    while next_value <= max_val:
        if i > 1:
            output += ','

        output += str(next_value)
        next_value = a + b * i

        i += 1

    return output


def digit_sum(n: int) -> int:
    """
    Returns the sum of the digits of n.

    examples:
    >>> digit_sum(123)
    6
    >>> digit_sum(123456789)
    45
    >>> digit_sum(0)
    0
    >>> digit_sum(1)
    1
    >>> digit_sum(-123)
    6
    >>> digit_sum(-123456789)
    45

    :param n:
    :return:
    """
    if n < 0:
        n = -n

    sum_of_digits = 0

    while n > 0:
        sum_of_digits += n % 10
        n //= 10

    return sum_of_digits


def sum_factors(n: int) -> int:
    """
    Returns the sum of the factors of n. Not including n itself.

    examples:
    >>> sum_factors(12)
    16
    >>> sum_factors(1)
    0

    :param n:
    :return:
    """
    return sum(get_factors(n)[:-1])


def is_perfect(n: int) -> bool:
    """
    Returns True if n is perfect, False otherwise.

    examples:
    >>> is_perfect(0)
    False
    >>> is_perfect(1)
    False
    >>> is_perfect(2)
    False
    >>> is_perfect(6)
    True
    >>> is_perfect(28)
    True
    >>> is_perfect(496)
    True
    >>> is_perfect(497)
    False

    :param n:
    :return:
    """
    return n == sum_factors(n)


def n_perfect_numbers(n: int) -> str:
    """
    Returns a string of the first n perfect numbers separated by commas.

    THEORY:

    From the Euclid Euler theorem there is a 1 to 1 relation between mersenne primes and perfect numbers.
    This means we can find perfect numbers by finding their respective mersenne primes. Which is less computationally
    expensive than finding the factors of a number and summing them. First we test if a number is prime and then using
    the lucas lehmer primality test we test if that prime can be used to formulate a mersenne prime. If a mersenne prime
    is found we use the formula 2^(p - 1) * (2^p - 1) to find the perfect number.

    Euclid Euler theorem: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    This theorem states that all perfect numbers are of the form 2^(p - 1) * (2^p - 1)
    where p is a prime number and the mersenne number 2^(p - 1) is also prime.

    Mersenne prime: https://en.wikipedia.org/wiki/Mersenne_prime
    A prime number that is of the form 2^(p - 1) where p must also be prime. If p is prime and through the lucas lehmer
    test 2^(p - 1) - 1 is also prime then we have a mersenne prime.

    Lucas Lehmer primality test: https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test
    This test is used to determine if a mersenne number is prime. Using this test saves a lot of computation time.
    If the mersenne number is prime then the number is a mersenne prime which can be used to calculate a perfect number.

    Examples:
    >>> n_perfect_numbers(0)
    ''
    >>> n_perfect_numbers(1)
    '6'
    >>> n_perfect_numbers(2)
    '6,28'
    >>> n_perfect_numbers(3)
    '6,28,496'
    >>> n_perfect_numbers(4)
    '6,28,496,8128'
    >>> n_perfect_numbers(5)
    '6,28,496,8128,33550336'

    :param n:
    :return:

    Why did I just make myself learn all of this math ):
    """
    perfects_found = 1  # since LLT fails for first perfect number we start at 1
    output = '6'  # first perfect number is 6
    i = 0

    if n == 0:
        return ''

    if n > 1:
        while perfects_found < n:  # keep searching for perfects if perfects found is less than required n
            if is_odd_prime(i) and lucas_lehmer_primality_test(i):  # test first for primality and then for mersenne
                perfects_found += 1
                if perfects_found > 1:
                    output += ','

                output += str(2**(i - 1) * (2**i - 1))  # euclid euler theorem formula for perfect numbers

            i += 1

    return output


############################################################################################
#                                                                                          #
#                                       PART 2                                             #
#                                                                                          #
############################################################################################


def take_turn(player_name: str, player_score: int, round_number: int) -> int:
    """
    Simulates a single turn of the game. Returns the score for the turn.

    :param player_name: the name of the player
    :param player_score: the score of the player
    :param round_number: the round number
    :return: the score for the turn
    """
    roll_score = None
    turn_score = 0

    while roll_score != 0 and (turn_score + player_score) < 21:
        roll_score = 0
        rolls = roll_three_dice()

        if all_same(rolls):
            if rolls[0] == round_number:    # all dice are equal to round number
                roll_score = 21
            else:                           # all dice are equal but not to round number
                roll_score = 5
        else:                               # not all dice are equal and some or no dice are equal to round score
            roll_score = amount_matching(rolls, round_number)

        turn_score += roll_score
        print_roll_results(player_name, rolls, roll_score, turn_score)

    return player_score + turn_score


def play_round(player_one_name: str, player_two_name: str, round_number: int) -> str:
    """
    Simulates a single round of the game. Returns the name of the winner.

    :param player_one_name:
    :param player_two_name:
    :param round_number:
    :return: returns the name of the winner
    """
    player_one_score = 0
    player_two_score = 0

    while True:
        print_turn_announcement(player_one_name, round_number, player_one_score)
        player_one_score = take_turn(player_one_name, player_one_score, round_number)

        if player_one_score >= 21:
            print_winner_announcement(player_one_name, player_two_name, player_one_score, player_two_score)
            return player_one_name

        print_turn_announcement(player_two_name, round_number, player_two_score)
        player_two_score = take_turn(player_two_name, player_two_score, round_number)

        if player_two_score >= 21:
            print_winner_announcement(player_one_name, player_two_name, player_one_score, player_two_score)
            return player_two_name


############################################################################################
#                                                                                          #
#                                   HELPER FUNCTIONS                                       #
#                                                                                          #
############################################################################################

#   ####################################################################################
    #                           PART 1 HELPER FUNCTIONS                                #
    ####################################################################################


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


def get_factors(n: int) -> list:
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
    output = []

    for i in range(1, n + 1):
        if is_multiple_of(n, i):
            output.append(i)

    return output


def is_odd_prime(n: int) -> bool:
    """
    Returns True if n is prime, False otherwise.

    Examples:
    >>> is_odd_prime(0)
    False
    >>> is_odd_prime(1)
    False
    >>> is_odd_prime(2)
    False
    >>> is_odd_prime(3)
    True
    >>> is_odd_prime(4)
    False
    >>> is_odd_prime(5)
    True

    :param n:
    :return:
    """

    if n <= 2:
        return False

    for i in range(2, math.ceil(n ** 0.5)+1):  # checks multiplicity of each number up to sqrt(n)
        if n % i == 0:
            return False

    return True


def lucas_lehmer_primality_test(odd_prime: int) -> bool:
    """
    Returns True if p is a mersenne prime, False otherwise.

    Examples:
    >>> lucas_lehmer_primality_test(2)
    False
    >>> lucas_lehmer_primality_test(3)
    True
    >>> lucas_lehmer_primality_test(4)
    False
    >>> lucas_lehmer_primality_test(5)
    True
    >>> lucas_lehmer_primality_test(11)
    False

    :param odd_prime:
    :return:
    """
    mersenne_num = 2 ** odd_prime - 1  # mersenne number
    s = 4

    for i in range(1, odd_prime - 1):
        s = (s * s - 2) % mersenne_num

    return s == 0


#   ####################################################################################
    #                           PART 2 HELPER FUNCTIONS                                #
    ####################################################################################

def roll_three_dice() -> list:
    roll_list = []

    for _ in range(3):
        roll_list.append(roll_one_die())

    return roll_list


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))

    return die


def all_same(value_list: list) -> bool:
    """
    Returns True if all the values in the list are the same, False otherwise.

    examples:
    >>> all_same([1,1,1])
    True
    >>> all_same([1,2,1])
    False
    >>> all_same([1,1,1,1])
    True
    >>> all_same([1,1,1,2])
    False

    :param value_list:
    :return:
    """
    compare = value_list[0]

    for i in value_list:
        if i != compare:
            return False

    return True


def amount_matching(value_list: list, value: int) -> int:
    """
    Returns the number of values in value_list that match value.

    :param value_list:
    :param value:
    :return:
    """
    match_count = 0

    for i in value_list:
        if i == value:
            match_count += 1

    return match_count


#           ####                 PART 2 PRINTER FUNCTIONS                 ####


def print_roll_results(player_name: str, rolls: list, roll_score: int, total_score: int):
    unicode_dice = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    print(f"""
    ┃Rolling dice...               
    ┃{unicode_dice[rolls[0] - 1]} {unicode_dice[rolls[1] - 1]} {unicode_dice[rolls[2] - 1]}                         
    ┃{player_name} rolled a {rolls[0]}, a {rolls[1]}, and a {rolls[2]}    
    ┃Score for this roll: {roll_score}     
    ┃Total Score: {total_score}   
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


def print_turn_announcement(player_name: str, round_number: int, score: int):
    print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃Player {player_name} is taking a turn in round {round_number}!
┃Current Score: {score}
┃""", end='')


def print_winner_announcement(player_one_name, player_two_name, player_one_score, player_two_score):
    winner = player_one_name if player_one_score > player_two_score else player_two_name

    print(f"""
            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ┃
            ┃           PLAYER {player_one_name.upper()} HAS WON!!!
            ┃
            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

    print(f"{player_one_name} has {player_one_score} points and {player_two_name} has {player_two_score} points")


play_round('a', 'b', 1)
