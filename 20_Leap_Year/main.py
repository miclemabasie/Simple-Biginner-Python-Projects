

def is_leap_year(year):
    """
    This function determines whether a year is a leap year of not,
    Returns True if yes and False if No
    Contraints: 
        Years Divisible by 4 === Leap Year
        Exception:
            Years Divisible by 100 === Not Leap Year
            Exception:
                Years Divisible by 400 === Leap Year
    """
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}: is a leap year")
            return True
        else:
            print(f"{year}: is not a leap year")
            return False
    elif year % 4 == 0 or year % 400 == 0:
        print(f"{year}: is a leap year")
        return True
    else:
        print(f"{year}: is not a leap year")
        return False



def main():
    is_leap_year(1999)


if __name__ == "__main__":
    main()