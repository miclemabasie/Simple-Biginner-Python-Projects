from leapyear import is_leap_year

def is_valid_date(year, month, day):
    """
    Check if a date is valid by checking the year, month and day
    Note:
    30 => Septempber(09), April(04), June(06), November(11)
    31 => 
    """

    SHORT_VALID_MONTHS = [4, 6, 9, 11]
    LONG_VALID_MONTHS = [1, 3, 5, 7, 8, 10, 12]
    is_leapyear = False
    result = False

    # Start by checking if the year is leap or not 
    if is_leap_year(year):
        is_leapyear = True
    
    if 1 <= month <= 12:
        # month is withen the range
        if month == 2: # Check if it's febaury
            if is_leapyear: # Then month should be max 29
                if 1 <= day <= 29:
                    result = True
                else:
                    result = False
            else:
                if 1 <= day <= 28:
                    result = True
                else:
                    month = False
        elif month in SHORT_VALID_MONTHS: # Means it is a 30 day month
            if 1 <= day <= 30:
                result = True
            else:
                result = False
        elif month in LONG_VALID_MONTHS: # menas it is a 31 day month
            if 1 <= day <= 31:
                result = True
            else:
                result = False
    else:
        result = False
    
    return result
        



def main():
    valid = is_valid_date(1666, 0, 29)
    print(valid)

if __name__ == "__main__":
    main()