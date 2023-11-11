import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR = 0
MONTH = 1
DAY = 2

# column numbers of data within input csv file
INPUT_SID = 0
INPUT_TITLE = 2
INPUT_CAST = 4
INPUT_DATE = 6
INPUT_CATEGORIES = 10


def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.

    Examples :

    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})


    """
    id_date_dict = {}
    id_actor_dict = {}
    category_id_dict = {}
    id_title_dict = {}

    file = open(filename, "rt", encoding="utf8")
    file.readline()  # ignore header row
    lines = file.readlines()

    for line in lines:
        line = line.split(",")

        date = create_date(line[INPUT_DATE])
        actor_list = line[INPUT_CAST].split(":")
        category_list = line[INPUT_CATEGORIES].split(":")
        show_id = line[INPUT_SID]

        id_date_dict[show_id] = date

        if actor_list[0]:
            id_actor_dict[show_id] = uniques_only(actor_list)

        file_into_category_dict(category_list, show_id, category_id_dict)
        id_title_dict[show_id] = line[INPUT_TITLE]

    return id_date_dict, id_actor_dict, category_id_dict, id_title_dict


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
      If no actors are specified (empty list), all actors in library are valid;
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    {

    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]

     }
    """
    (id_date_dict,
     id_actor_dict,
     category_id_dict,
     id_title_dict) = read_file(filename)

    ids_matching_category = category_id_dict[category] if category in category_id_dict else []
    ids_with_actor = get_ids_with_actor(id_actor_dict, actors) if actors else list(id_title_dict.keys())
    ids_before_date = get_shows_before_date(id_date_dict, date)

    matching_ids = shared_items(ids_matching_category, ids_before_date, ids_with_actor)

    return get_show_name_id_list(matching_ids, id_title_dict)


####################################################################################################################
#                                               HELPER FUNCTIONS                                                   #
####################################################################################################################


def get_ids_with_actor(id_actor_dict: dict, actors: list):
    id_list = []

    for actor in actors:
        for id_number, actor_list in id_actor_dict.items():
            if actor in actor_list:
                id_list.append(id_number)

    return id_list


def get_shows_before_date(id_date_dict, test_date: Date):
    id_list = []

    for id_number, date in id_date_dict.items():
        if date_is_after(test_date, date):
            id_list.append(id_number)

    return id_list


def shared_items(ids_matching_category, ids_before_date, ids_with_actor):
    output_list = []

    for item in ids_matching_category:
        if item in ids_before_date and item in ids_with_actor:
            output_list.append(item)

    return output_list


def get_show_name_id_list(matching_ids, id_title_dict) -> list[tuple[str,    # title
                                                                     str]]:  # id
    output_list = []

    for id_number in matching_ids:
        output_list.append((str(id_title_dict[id_number]), str(id_number)))

    output_list.sort(key=lambda t: t[0])

    return output_list


def file_into_category_dict(category_list, show_id, category_id_dict):
    """
    Return a dictionary of categories and show ids.

    :param category_list: List of categories
    :param show_id: Show id
    :param category_id_dict: Dictionary of categories and show ids
    :return: Dictionary of categories and show ids
    """
    for category in category_list:
        if not (category in category_id_dict):
            category_id_dict[category] = [show_id]
        else:
            category_id_dict[category].append(show_id)


def uniques_only(input_list) -> list:
    found_items = []

    for item in input_list:
        if item not in found_items:
            found_items.append(item)

    return found_items


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

    Example:
    >>> date_is_after((2019, 7, 2), (2019, 7, 1))
    True
    >>> date_is_after((2019, 7, 1), (2019, 7, 2))
    False
    >>> date_is_after((9999, 7, 1), (2019, 6, 30))
    True

    :param date_a: check if this date is after date_b
    :param date_b: check if date_a is after this date
    :return: returns True if date_a is after date_b, False otherwise.
    """
    if date_a[0] == date_b[0]:  # if year is equal
        if date_a[1] == date_b[1]:  # check if month is equal
            if date_a[2] > date_b[2]:  # compare days
                return True
        elif date_a[1] > date_b[1]:  # month is not equal check if month is older
            return True
    elif date_a > date_b:  # year is not equal check if year is older
        return True

    return False


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
