from main import *


assert area(10, 10) == 100
assert area(0, 999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(999, 0, 999) == 0
assert volume(10, 8, 5) == 400
assert surface_area(10, 10, 10) == 600
assert surface_area(20, 5, 2) == 300
