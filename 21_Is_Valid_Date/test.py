from main import *


assert is_valid_date(1999, 12, 13) == True
assert is_valid_date(2000, 2, 29) == True
assert is_valid_date(2001, 2, 29) == False
assert is_valid_date(2029, 13, 1) == False
assert is_valid_date(1000000, 1, 1) == True
assert is_valid_date(2015, 4, 31) == False
assert is_valid_date(1970, 5, 99) == False
assert is_valid_date(1981, 0, 3) == False
assert is_valid_date(1666, 4, 0) == False

import datetime

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)

for i in range(100):
    assert is_valid_date(d.year, d.month, d.day) == True
    d += oneDay