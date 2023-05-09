from main import *

assert sec_conversion(30) == '30s'
assert sec_conversion(60) == '1m'
assert sec_conversion(90) == '1m 30s'
assert sec_conversion(3600) == '1h'
assert sec_conversion(3601) == '1h 1s'
assert sec_conversion(3661) == '1:1:1'
assert sec_conversion(90042) == '25h 42s'
assert sec_conversion(0) == '0s'