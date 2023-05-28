from main import *

LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
NUMBERS= string.digits
SPECIAL = '~!@#$%^&*()_+'

assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
print(pw)
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial