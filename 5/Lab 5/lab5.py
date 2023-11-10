def print_name_age_v1():
    """
    Function to collect and display user input

    :return: prints user input
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    age_class = get_age_class(age)

    print(f"hello {name} {age_class}")


def print_name_age_v2():
    """
    Function to collect and display user input

    :return: prints user input
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if not str(age).isdigit():
        print(f"{name} you are lying about your age")
    else:
        age_class = get_age_class(int(age))

        print(f"hello {name} {age_class}")


def print_name_age_v3():
    """
    Function to collect and display user input

    :return: prints user input
    """
    name = input("Enter your name: ")
    age = get_num(0, "Enter your age: ")
    age_class = get_age_class(age)

    print(f"hello {name} {age_class}")


def get_num(min_value: int, prompt: str) -> int:
    """
    Function to return number entered by user

    :param min_value: the minimum value allowed
    :param prompt: the prompt to display to the user
    :return: number entered by user
    """
    input_value = -1

    while not(input_value.isdigit()) or not(int(input_value) >= min_value):
        input_value = input(prompt)

    return int(input_value)


def get_age_class(age):
    """
    Function to return age class based on age

    :param age: the age to check
    :return: the age class
    """
    if age < 18:
        return 'child'
    elif age <= 64:
        return 'adult'
    else:
        return 'senior'
