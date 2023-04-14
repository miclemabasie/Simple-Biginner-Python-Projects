from main import *


assert convert_to_fahranhiet(0) == 32
assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_celsius(200) == 93.33333333333334
assert convert_to_celsius(convert_to_fahranhiet(20)) == 20
