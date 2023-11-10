import math


def print_bart():
    """
    Prints ascii art of bart simpson
    art credit: https://www.asciiart.eu/cartoons/simpsons (Unknown author)
    """

    bart_ascii = """  
      |\\/\\/\\/|
      |      |
      |      |
      | (o)(o)
      C      _)
      | ,___|
      |   /
     /____\\
    /      \\
    """

    print(bart_ascii)


def print_homer():
    """
    Prints ascii art of homer simpson
    art credit: https://www.asciiart.eu/cartoons/simpsons (Unknown author)
    """

    homer_ascii = """
       __\"\'_
      /     \\  
     |       |  
     |  (o)(o)  
     C  .---_)
      | |___|  
      |  \\__/  
      /_____\\ 
     /_____/ \\ 
    /         \\ 
    """

    print(homer_ascii)


def print_separator():
    """
    Prints ascii art separator
    """
    seperator = "/~~~~~~~~\\"

    print(seperator)


def print_logo():
    """
    prints a sequence of 4 ascii art piece seperated with ascii separator
    """
    print_separator()

    for _ in range(2):
        print_homer()
        print_separator()
        print_bart()
        print_separator()


print_logo()


def calculate_surface_area(height: float, diameter: float):
    """
    Calculates and prints the surface area of a cylinder
    given the height and diameter

    example:
    >>>calculate_surface_area(1.2, 3.5)
    cylinder area: 32.4

    :param height: height of cylinder
    :param diameter: diameter of cylinder
    """
    circumference = diameter * math.pi
    end_area = (math.pi * diameter ** 2)/4
    wall_area = circumference * height
    total_surface_area = 2 * end_area + wall_area

    print(f'cylinder area: {total_surface_area:.1f}')

