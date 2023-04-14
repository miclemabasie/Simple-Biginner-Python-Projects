import sys


def is_odd(number):
    try:
        mud = number % 2
        if isinstance(mud, float):
            return False
    except ValueError:
        print("Invalid Input")
        sys.exit()
    if mud != 0:
        return True
    else:
        return False


def is_even(number):
    try:
        mud = number % 2
        if isinstance(mud, float):
            return False
    except ValueError:
        print("Invlaue input")
        sys.exit()
    if mud != 0:
        return False
    else:
        return True
