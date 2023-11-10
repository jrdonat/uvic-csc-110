import datetime
import doctest
from typing import Type

Date = (int, int, int)  # (year, month, day)

NetflixMedia = (str,  # 1 - Type of media (e.g. 'Movie', 'TV Show')
                str,  # 2 - Title
                list[str],  # 3 - List of Directors
                list[str],  # 4 - List of Actors
                Date)  # 5 - Date Added to Netflix


def raise_to_power(base_list: list[float], power_list: [float]) -> None:
    """Return a list of the elements in base_list raised to the power of the
    elements in power_list.

    Preconditions: base_list and power_list are not empty and have the same
    length.

    >>> raise_to_power([2.0, 3.0, 4.0], [2.0, 3.0, 4.0])
    [4.0, 27.0, 256.0]
    >>> raise_to_power([2.0, 3.0, 4.0], [0.0, 0.0, 0.0])
    [1.0, 1.0, 1.0]
    >>>

    :param base_list: list of floats
    :param power_list: list of floats
    """
    if not base_list or not power_list:
        return

    for i in range(int(len(base_list))):
        base_list[i] = base_list[i] ** power_list[i]

    return


def create_date(input_string: str) -> Date:
    """
    Return a Date tuple from a string in the format 'day-month-year'.

    Examples:
    >>> create_date('1-Jul-19')
    (2019, 7, 1)
    >>> create_date('12-Dec-19')
    (2019, 12, 12)
    >>> create_date('31-Dec-19')
    (2019, 12, 31)
    >>> create_date('1-Jan-20')
    (2020, 1, 1)
    >>> create_date('1-Jan-21')
    (2021, 1, 1)

    :returns: returns a tuple in the format
    """
    date_list = input_string.split("-")
    year = int('20' + str(date_list[2]))
    month = int(convert_month((date_list[1])))
    day = int(date_list[0])

    return year, month, day


def create_show(media_type: str,  # Type of media (e.g. 'Movie', 'TV Show')
                title: str,  # Title
                collen_seperated_directors:  # Collen seperated string of directors
                str, collen_seperated_actors: str,  # Collen seperated string of actors
                date: str  # String date in formate 'day-month-year'
                ) -> NetflixMedia:
    """
    Return a NetflixMedia tuple from the given parameters.
    
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))  
        
    
    :param media_type: Type of media (e.g. 'Movie', 'TV Show')
    :param title: Title
    :param collen_seperated_directors: Collen seperated string of directors
    :param collen_seperated_actors: Collen seperated string of actors
    :param date: String date in formate 'day-month-year'
    :return: NetflixMedia Tuple
    """

    date = create_date(date)

    if not collen_seperated_directors:
        director_list = []
    else:
        director_list = collen_seperated_directors.split(':')

    if not collen_seperated_actors:
        actors_list = []
    else:
        actors_list = collen_seperated_actors.split(':')

    return media_type, title, director_list, actors_list, date


def get_titles(content_list: list[NetflixMedia]) -> list[str]:
    """
    Return a list of the titles of the media in content_list.

    Example:
    >>> loshows = [\
('Movie', "Viceroy's House", ['Gurinder Chadha'],\
 ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
  'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
  'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
 (2017, 12, 12)),\
('Movie', 'Superbad', ['Greg Mottola'], \
 ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'],\
 (2019, 9, 1)),\
('TV Show', 'Maniac', [], \
 ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
 (2018, 9, 21)),\
('Movie', 'Road to Sangam', ['Amit Rai'], \
 ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
  'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
 (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']

    :param content_list: list of NetflixMedia
    :return: list of titles of the media in content_list
    """
    title_list = []

    for media in content_list:
        title_list.append(media[1])

    return title_list


def is_actor_in_show(media: NetflixMedia, actor_name: str) -> bool:
    """
    Return True if actor_name is in the list of actors in media, False

    Examples:
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True

    :param media: NetflixMedia
    :param actor_name: name of actor to search for
    :return: True if actor_name is in the list of actors in media, False otherwise
    """

    for actor in media[3]:
        if actor.upper() == actor_name.upper():
            return True

    return False


def count_shows_before_date(content_list: list[NetflixMedia], date: Date) -> int:
    """
    Return the number of shows in content_list that were added to Netflix

    Examples:
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
     (2017, 4, 18))]

>>> count_shows_before_date(loshows, (2015, 1, 1))
0

>>> count_shows_before_date(loshows, (2018, 10, 20))
3

    :param content_list: list of NetflixMedia
    :param date: Date to compare to
    :return: number of shows in content_list that were added to Netflix before date
    """
    output_count = 0

    for content in content_list:
        if date_is_after(content[4], date):
            output_count += 1

    return output_count


def get_shows_with_actor(content_list: list[NetflixMedia], actor_name: str) -> list[NetflixMedia]:
    """
    Return a list of the shows in content_list that have actor_name in their

    Examples:
    >>> loshows = [\
('Movie', "Viceroy's House", ['Gurinder Chadha'], \
 ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
  'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
  'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
 (2017, 12, 12)),\
('Movie', 'Superbad', ['Greg Mottola'], \
 ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
 (2019, 9, 1)),\
('TV Show', 'Maniac', [], \
 ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
 (2018, 9, 21)),\
('Movie', 'Road to Sangam', ['Amit Rai'], \
 ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
  'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
 (2019, 12, 31))]

>>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
[('Movie', 'Superbad', ['Greg Mottola'], \
 ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
 (2019, 9, 1)), \
('TV Show', 'Maniac', [], \
 ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
 (2018, 9, 21))]

>>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
[('Movie', 'Superbad', ['Greg Mottola'], \
 ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
 (2019, 9, 1)), \
('TV Show', 'Maniac', [], \
 ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
 (2018, 9, 21))]

>>> get_shows_with_actor(loshows, 'Justin Bieber')
[]



    :param content_list: list of NetflixMedia
    :param actor_name: name of actor to search for
    :return: list of NetflixMedia
    """
    output_list = []

    for content in content_list:
        for actor in content[3]:
            if actor.upper() == actor_name.upper() and content not in output_list:
                output_list.append(content)

    return output_list


########################################################################################################################
#                                              HELPER FUNCTIONS                                                        #
########################################################################################################################


def must_equal(object_a: object, object_b: object) -> object:
    """
    Check if object_a is equal to object_b, if not raise an AssertionError.

    :param object_a: first object to compare
    :param object_b: second object to compare
    :return: returns object_a if object_a is equal to object_b
    """
    if object_a != object_b:
        raise AssertionError(str(object_a) + " != " + str(object_b))
    return object_a


def current_year() -> int:
    """
    Return the current year in the format YY.
    """
    year = datetime.datetime.now().year

    return year[-2:]


def convert_month(month_string: str) -> int:
    """
    Return the number of the month as an int.

    :param month_string: String of the month
    :return: Int of the month
    """
    month_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                  "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

    return month_dict[month_string]


def date_is_after(date_a: Date, date_b: Date):
    """
    Return True if date_a is after date_b, False otherwise.

    :param date_a: check if this date is after date_b
    :param date_b: check if date_a is after this date
    :return: returns True if date_a is after date_b, False otherwise.
    """
    if date_a[0] == date_b[0]:  # if year is equal
        if date_a[1] == date_b[1]:  # check if month is equal
            if date_a[2] < date_b[2]:  # compare days
                return True
        elif date_a[1] < date_b[1]:  # month is not equal check if month is older
            return True
    elif date_a < date_b:  # year is not equal check if year is older
        return True

    return False
